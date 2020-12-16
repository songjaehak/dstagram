from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# 1. 모델 : 데이터베이스 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능, 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다 : 템플릿작성(html)


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])