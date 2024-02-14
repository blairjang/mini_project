from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=100)
    user = models.ForeignKey("users.User", verbose_name="작성자", on_delete=models.CASCADE)
    content = models.TextField("포스트 내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)
    

    def __str__(self):       # 제목을 문자열로 보여쥼 
        return self.title 