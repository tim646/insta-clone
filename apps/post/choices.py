from django.db.models import TextChoices


class NotoificationChoice(TextChoices):
    LIKE = ('like', 'Like'),
    COMMENT = ('comment', 'Comment'),
    FOLLOW = ('follow', 'Follow'),
