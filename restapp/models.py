from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):

    class PostObjects(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(status="published")


    options=(
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_post")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    detail = models.TextField(null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=options, default='published')

    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)
