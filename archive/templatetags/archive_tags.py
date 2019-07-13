from django import template
from easy_thumbnails.files import get_thumbnailer
from filer.models import File

register = template.Library()


@register.filter
def extension(file: File):
    """
    Return the filename.
    """
    if file.extension in ["jpg", "png", "svg", "gif"]:
        return _prepare_image(file)

    return """
        <div class='panel panel-default'>
            <div class='panel-body'>
                <p>{}</p>
                <p>
                    <a class='btn btn-default' href='{}' target='_blank'>Datei öffnen</a>
                </p>
            </div>
        </div>
    """.format(file, file.url)


def _prepare_image(file):
    options = {'size': (350, 350), 'crop': False, 'quality': 100}
    thumb_url = get_thumbnailer(file).get_thumbnail(options).url
    return f"<a href='{file.url}' target='_blank'><img src='{thumb_url}' class='img-thumbnail'></a>"


@register.filter(is_safe=True)
def row_if_exists(field, name):
    if field:
        return """
            <div class="row">
              <div class="col-md-3 col-sm-4">
                {}:
              </div>
              <div class="col-md-9 col-sm-8">
                {}
              </div>
            </div>
        """.format(name, field)
    return ""
