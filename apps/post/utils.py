import uuid
from time import timezone


def post_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'toy_photos/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'
