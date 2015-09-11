from django import template

register = template.Library()


def sizify(value):
    """
    Simple kb/mb/gb size snippet for templates:
    
    {{ product.file.size|sizify }}
    """
    #value = ing(value)
    if value < 512000:
        value = value / 1024.0
        ext = 'KB'
    elif value < 4194304000:
        value = value / 1048576.0
        ext = 'MB'
    else:
        value = value / 1073741824.0
        ext = 'GB'
    return '%s %s' % (str(round(value, 2)), ext)


def faAttachment(extension):
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
    else:
        return extension


register.filter('sizify', sizify)
register.filter('faAttachment', faAttachment)