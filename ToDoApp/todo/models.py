from django.db import models

# Create your models here.
# class名はキャメルケースで書くことが通例
# 継承を使う場合 'from hoge import 継承name' で文頭に宣言 
# 継承をする場合はclass name(継承するmethod)で記述する
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    # モデルオブジェクトに名前をつける
    #  __str__(self)...modelオブジェクト自身を文字列として受け取り、titileを表示名に使う
    def __str__(self):
        return self.title
