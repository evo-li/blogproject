from django.db import models
from django.utils.six import python_2_unicode_compatible


# 这里并没有实现附加的评论
# 也没有实现对md的支持


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)#评论数据保存到数据库时，自动把 created_time 的值指定为当前时间

    post = models.ForeignKey('blog.Post',models.CASCADE)#级联删除

    def __str__(self):
        return self.text[:20]
