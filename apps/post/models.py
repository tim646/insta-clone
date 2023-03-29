from django.db import models

from apps.common.models import Base


class Post(Base):


    class Meta:
        db_table = "posts"