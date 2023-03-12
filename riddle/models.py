from django.db import models
from login.models import User

# Create your models here.

class Article(models.Model):
    """ 文助中的文章 """
    number = models.SmallIntegerField(default=1,unique=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    annotation = models.TextField()
    translate = models.TextField()
    hbread = models.BooleanField(default=False)
    seen_user = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s %s" %(str(self.number), self.name)

    class Meta:
        ordering = ['number']
        verbose_name = "文章"
        verbose_name_plural = "文章"

class Riddle(models.Model):
    """ 文助中的考题 """

    kind_choices = (
        (1, '字词翻译'),
        (2, '句子翻译'),
        (3, '特殊字词'),
        (4, '特殊成语')
    )
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    number = models.SmallIntegerField(null=True, blank=True)
    riddlesum = models.SmallIntegerField(null=True, blank=True)
    kind = models.SmallIntegerField(choices=kind_choices, default=1)
    topic = models.TextField()
    answer = models.TextField()
    keyword = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    turndict = {1:'字词翻译', 2:'句子翻译', 3:'特殊字词', 4:'特殊成语'}

    def __str__(self):
        if self.number:
            return "%s. %s %s Riddle%s" %(str(self.article.number), self.article.name, self.turndict[self.kind], str(self.number))
        else:
            return "%s. %s %s Riddle" %(str(self.article.number), self.article.name, self.turndict[self.kind])

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = "题目"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    child_comment = models.TextField(null=True, blank=True)
    text = models.TextField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "By %s On %s：%s" %(self.user, str(self.c_time), self.text)

    class Meta:
        ordering = ["c_time"]
        verbose_name = "评论"
        verbose_name_plural = "评论"

    