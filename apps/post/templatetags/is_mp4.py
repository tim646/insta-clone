import magic
from  django import template
register = template.Library()


@register.filter
def check_is_mp4(file):
    mime = magic.Magic(mime=True)
    return 'video/mp4' in mime.from_file(file.path)