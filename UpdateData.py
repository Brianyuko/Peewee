from peewee import *

sqlite_db = SqliteDatabase('login.db')


class Login(Model):
    username = CharField()
    point = IntegerField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()

# Update Data Option One
user = Login.select().where(Login.username == 'Annas').get()
user.username = 'Annas Firmansyah'
user.save()

# Update Data Option Two
Login.update(point=100).where(Login.username == 'Brian Yuko').execute()
