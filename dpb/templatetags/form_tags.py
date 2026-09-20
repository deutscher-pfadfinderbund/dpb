"""Shared helpers for rendering form fields with Bootstrap 5 classes."""

from django import template
from django.forms import CheckboxInput, RadioSelect, Select
from django.forms.boundfield import BoundWidget
from django.template.loader import get_template
from django.utils.safestring import mark_safe

register = template.Library()

FORM_TEMPLATE = "dpb/form.html"
FIELD_TEMPLATE = "dpb/form_field.html"


def widget_css_class(widget):
    """Return the Bootstrap 5 class that belongs on this widget element."""
    if isinstance(widget, (CheckboxInput, RadioSelect)):
        return "form-check-input"
    if isinstance(widget, Select):
        return "form-select"
    return "form-control"


def field_kind(field):
    """
    Classify a bound field into the three shapes the field template renders:
    a group of checkboxes/radios, a single checkbox, or a plain input.

    `CheckboxSelectMultiple` subclasses `RadioSelect`, so the first test covers
    both choice groups.
    """
    widget = field.field.widget
    if isinstance(widget, RadioSelect):
        return "choice_group"
    if isinstance(widget, CheckboxInput):
        return "checkbox"
    return "input"


register.filter("field_kind", field_kind)


@register.filter(is_safe=True)
def bootstrap_widget(field):
    """
    Render a bound field (or a single choice of one) with the Bootstrap 5 class
    its widget needs.

    This is the single place that decides a widget's class, so it sets the
    `class` attribute outright rather than merging into whatever the widget
    already carries.
    """
    if isinstance(field, BoundWidget):
        # A single choice of a radio/checkbox group: the group itself, not the
        # subwidget, is what `widget_css_class` can classify.
        attrs = {
            **field.data["attrs"],
            "class": widget_css_class(field.parent_widget),
        }
        return BoundWidget(
            field.parent_widget, {**field.data, "attrs": attrs}, field.renderer
        ).tag()
    if not hasattr(field, "as_widget"):
        return field
    css_class = widget_css_class(field.field.widget)
    if field.errors:
        css_class += " is-invalid"
    return field.as_widget(attrs={"class": css_class})


def render_field(field, css_classes=None):
    """Render one bound field through the shared Bootstrap 5 field template."""
    if not hasattr(field, "as_widget"):
        return ""
    return mark_safe(
        get_template(FIELD_TEMPLATE).render({"field": field, "css_classes": css_classes or {}})
    )


@register.filter(is_safe=True)
def as_bootstrap(form):
    """Render a whole form as stacked Bootstrap 5 form groups."""
    return mark_safe(get_template(FORM_TEMPLATE).render({"form": form}))


@register.filter(is_safe=True)
def as_bootstrap_inline(form):
    """
    Render a whole form with the labels hidden and repeated as placeholders.

    Checkboxes and radios keep their visible labels: a placeholder means
    nothing on them.
    """
    for field in form.fields.values():
        if not isinstance(field.widget, (CheckboxInput, RadioSelect)):
            field.widget.attrs["placeholder"] = field.label
    context = {
        "form": form,
        "css_classes": {"label": "visually-hidden"},
    }
    return mark_safe(get_template(FORM_TEMPLATE).render(context))
