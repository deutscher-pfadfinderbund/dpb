import os

from django import template
from django.db.models import FileField

register = template.Library()


@register.filter(is_safe=True)
def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:

    {{ product.file.size|sizify }}
    """
    # value = ing(value)
    if value < 512000:
        value /= 1024.0
        ext = 'KB'
    elif value < 4194304000:
        value /= 1048576.0
        ext = 'MB'
    else:
        value /= 1073741824.0
        ext = 'GB'
    return '%s %s' % (str(round(value, 2)), ext)


@register.filter(is_safe=True)
def fa_attachment(extension):
    """
    Add fontawesome icon if found. Else return normal extension as string.

    :param extension: file extension
    :return: matching fontawesome icon as string
    """
    if extension == 'pdf':
        return "<i class='fa fa-file-pdf-o fa-lg'></i>"
    elif extension == 'jpg' or extension == 'png':
        return "<i class='fa fa-picture-o fa-lg'></i>"
    elif extension == 'doc' or extension == 'docx':
        return "<i class='fa fa-file-word-o fa-lg'></i>"
    elif extension == 'xls' or extension == 'xlsx':
        return "<i class='fa fa-file-excel-o fa-lg'></i>"
    elif extension == 'extern':
        return "<i class='fa fa-external-link'></i>"
    elif extension == 'zip':
        return "<i class='fa fa-file-archive-o fa-lg'></i>"
    else:
        return extension


@register.filter
def filename(file: FileField):
    """
    Return the filename.

    :param file:
    :return:
    """
    return os.path.basename(file.file.name)


@register.filter
def extension(file: FileField):
    """
    Return the filename.

    :param file:
    :return:
    """
    _, ext = os.path.splitext(file.file.name)
    return ext[1:]


@register.filter(is_safe=True)
def house_details(value, text):
    if value:
        return f"""<div class="row">
            <div class="col-md-4">
              {text}
            </div>
            <div class="col-md-8">
              {value}
            </div>
          </div>
        """
    else:
        return ""


@register.filter(is_safe=True)
def house_details_link(value, text):
    if value:
        return f"""<span style='margin-right: 1em;'>
                  <a href='{value}'>
                    {text}
                  </a>
              </span>
        """
    else:
        return ""


@register.filter(is_safe=True)
def has_errors(value):
    try:
        if value.errors:
            return f"""
                <div class="alert alert-warning" role="alert">
                    <strong>{value.errors}</strong>
                </div>
            """
    except AttributeError:
        pass
    return ""


@register.filter(is_safe=True)
def table_row(value, args):
    if value or value == 0:
        args = args.split(",")
        text = args[0]
        tdurl = f"<td>{value}</td>"
        errors = has_errors(value)
        if len(args) > 1:
            if len(value) > 40:
                url = value[:40] + "..."
            else:
                url = value
            tdurl = f"<td><a href='{value}' target='_blank'>{url}</a></td>"
        return f"""
            {errors}
            <tr>
                <td>{text}</td>
                {tdurl}
            </tr>
        """
    return ""


@register.filter(is_safe=True)
def bool_icon(value, text=""):
    if value:
        icon = "<i class='fa fa-check'></i>"
    else:
        icon = "<i class='fa fa-times'></i>"
    return f"{icon} {text}"


@register.filter(is_safe=True)
def form_item(val):
    errors = has_errors(val)
    try:
        label = val.label_tag()
    except AttributeError:
        label = ""
    return f"""
        <div class="form-group">
            {label}
            {errors}
            {val}
        </div>"""


@register.filter(is_safe=True)
def form_checkbox(val):
    return f"""
        <div class="checkbox">
            {val.errors}
            <label>
            {val} {val.label}
            </label>
        </div>"""
