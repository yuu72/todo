from django.db import models

#           🔻右画面上に表示される文字列　左-実際に保存されるデータ
#              データ今回の例 list.htmlでitem.priorityの中身
PRIORITY = (('danger','high'),('info','nomal'),('success','low'))

# classによってテーブルを作ることができる
#      🔻任意の名前  🔻継承　modelsのオブジェクト
class TodoModel(models.Model):
    title = models.CharField(max_length=100)# titleはchar
    memo = models.TextField() # 長めの文章はtext
    # 🔻list.htmlより　ググって調べるのもよし
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY #選択肢を１つ１つ指定する場合choices 
                # 🔺 上で作る必要がある
    )
    duedate = models.DateField() #（）に何も入れなくても使用することができる
    # 🔻オブジェクトを文字列として返す　これがなければタイトルにオブジェクト名が表示される
    def __str__(self):
        return self.title