from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length = 20)
    def __str__(self):
        return self.type_name


class Blog(models.Model):
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建日期')
    last_updated_time = models.DateTimeField(auto_now_add=True,verbose_name='更新日期')
    def __str__(self):
        return "<Blog: %s>" % self.title
    # 对文章列表进行排序 为了使用pajinator
    class Meta:
        ordering = ['created_time']