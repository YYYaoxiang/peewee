from peewee import *

db = SqliteDatabase('uuu.db')


class Student(Model):
    name: str = CharField()
    age: int = IntegerField()

    class Meta:
        database = db
        table_name = 'Student'


db.connect()
db.create_tables([Student])
#------------------------------------------
s1 = Student(name='色法规飞', age=18)
s1.save()
# ------------------------------------------
#Student.delete().where(Student.name=='吴京').execute()
# ------------------------------------------
# s1 = Student(name='扬长吉', age=199)
# s1.id=2
# s1.save()
# ------------------------------------------
# Student.update({Student.name:'西安'}).where(Student.name=='吴京').execute()

#查询
# s1=Student.get(Student.name=='西安')
# print(s1.name,s1.age)
#
# s2=Student.select().where(Student.name=='西安')
# for i in s2:
#     print(i.name,i.age)
#
# s3=Student.select().execute()
# for j in s3:
#     pass