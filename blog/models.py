from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
from django.db.models import CharField, Model

# Create your models here.

#Admin id : pass
# chintan : Dhanswami@2011

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Post model in our database to store posts.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tech_stack = models.CharField(max_length=200, default='')
    github_url = models.URLField(max_length=200, default='n/a')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tech_image = models.ImageField(upload_to="tech_image", blank=True)
    #image_urls = models.TextField()
    images = ListCharField(
        base_field=CharField(max_length=100),
        size=6,
        blank=True,
        max_length=(6 * 1000)  # 6 * 10 character nominals, plus commas
    )

    class Meta:
        ordering = ['-created_on']  #sort results based on when they were created

    def __str__(self):
        return self.title
