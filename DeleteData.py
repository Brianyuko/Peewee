from peewee import *

sqlite_db = SqliteDatabase('login.db')


class Login(Model):
    username = CharField()
    point = IntegerField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()

# Delete Data Option One
user = Login.get(Login.id == 4)
user.delete_instance()

# Delete Data Option Two
Login.delete().where(Login.point < 3).execute()
