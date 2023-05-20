from peewee import *

db = SqliteDatabase('Goods.db')


class GoodsIn(Model):
    name:str = CharField()
    weight= DoubleField()

    class Meta:
        database = db
        table_name = 'GoodsIn'


db.connect()
db.create_tables([GoodsIn])
