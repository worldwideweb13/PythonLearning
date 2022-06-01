from django.db import models

# class名はキャメルケースで書くことが通例
# 継承を使う場合 'from hoge import 継承name' で文頭に宣言 
# 継承をする場合はclass name(継承するmethod)で記述する

# PRIORITY...タプル型. (任意の選択肢で変更不可のデータ形式).((val),(key),,)形式で記述する
PRIORITY = (('danger','hight'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices= PRIORITY
    )
    duedate = models.DateField()
    # モデルオブジェクトに名前をつける
    #  __str__(self)...modelオブジェクト自身を文字列として受け取り、titileを表示名に使う
    def __str__(self):
        return self.title
