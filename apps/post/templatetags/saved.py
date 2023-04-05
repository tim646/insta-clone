from  django import template

from apps.post.models import Like
from apps.user.models import Saved

register = template.Library()


@register.filter
def check_post_saved(post, user):
   return Saved.objects.filter(post_id=post, user=user).exists()
