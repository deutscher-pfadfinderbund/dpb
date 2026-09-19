"""Shared helpers for rendering form fields with Bootstrap 5 classes."""

from django import template
from django.forms import CheckboxInput, RadioSelect, Select
from django.forms.boundfield import BoundWidget
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

register = template.Library()


def widget_css_class(widget):
    """Return the Bootstrap 5 class that belongs on this widget element."""
    if isinstance(widget, (CheckboxInput, RadioSelect)):
        return "form-check-input"
    if isinstance(widget, Select):
        return "form-select"
    return "form-control"


def render_widget(field, *extra_classes):
    """
    Render the widget of a bound field with the given css classes applied to
    the widget element itself (instead of patching the rendered html).
    """
    classes = field.field.widget.attrs.get("class", "").split()
    for extra in extra_classes:
        for css_class in extra.split():
            if css_class not in classes:
                classes.append(css_class)
    return field.as_widget(attrs={"class": " ".join(classes)})


def field_label(field, css_class):
    """Render the label of a bound field, or an empty string if it has none."""
    if not field.label:
        return ""
    if not field.id_for_label:
        return format_html('<span class="{}">{}</span>', css_class, field.label)
    return format_html(
        '<label class="{}" for="{}">{}</label>',
        css_class,
        field.id_for_label,
        field.label,
    )


def field_help_text(field):
    """Render the help text of a bound field as a Bootstrap 5 form hint."""
    if not field.help_text:
        return ""
    # Django treats help_text as trusted markup, same as its own renderers do.
    return format_html('<div class="form-text">{}</div>', mark_safe(field.help_text))


def field_errors(field):
    """Render the errors of a bound field as Bootstrap 5 feedback elements."""
    errors = getattr(field, "errors", None)
    if not errors:
        return ""
    return format_html_join(
        "\n",
        '<div class="invalid-feedback d-block">{}</div>',
        ((error,) for error in errors),
    )


@register.filter(is_safe=True)
def bootstrap_widget(field):
    """
    Render a bound field (or a single choice of one) with the Bootstrap 5 class
    its widget needs.

    django-forms-bootstrap puts `form-control` on every widget, which is wrong
    for selects and for checkboxes. Dropping the classes it already stamped on
    and recomputing them is the point of this filter, so it does not go through
    `render_widget`.
    """
    if isinstance(field, BoundWidget):
        attrs = {**field.data["attrs"], "class": "form-check-input"}
        return BoundWidget(
            field.parent_widget, {**field.data, "attrs": attrs}, field.renderer
        ).tag()
    if not hasattr(field, "as_widget"):
        return field
    css_class = widget_css_class(field.field.widget)
    if field.errors:
        css_class += " is-invalid"
    return field.as_widget(attrs={"class": css_class})
