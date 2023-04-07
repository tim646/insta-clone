import uuid

from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_file_extension(value):
    ext = str(value.name).split('.')[-1]
    if not ext.lower() in ['mp4','svg' ,'avi', 'mkv', 'jpg', 'jpeg', 'png']:
        raise ValidationError('File type not supported.')

def history_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'posts/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'


def post_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'posts/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'

