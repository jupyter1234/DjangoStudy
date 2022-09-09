from django.db import models
from django.contrib.auth.models import User

#qustionModel
class Question(models.Model):
    subject = models.CharField(max_length=200)   #제목
    content = models.TextField() #내용
    create_date = models.DateTimeField()  #작성일시
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

#answermodel
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   #question과 연결됨
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)