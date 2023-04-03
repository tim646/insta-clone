from  django import template

from apps.post.models import Like

register = template.Library()


@register.filter
def check_like(post, user):
   return Like.objects.filter(post_id=post, user=user).exists()
