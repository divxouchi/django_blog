from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=25)
  slug = models.SlugField()
  intro = models.TextField()
  body = models.TextField()
  posted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=25)
  email = models.EmailField()
  body = models.TextField()
  posted_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('posted_date',)

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)