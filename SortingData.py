import datetime
# import random
from peewee import *

sqlite_db = SqliteDatabase('login.db')


class Login(Model):
    username = CharField()
    point = IntegerField()
    timeJoin = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([Login])

# Sorting Ascending
login_var = Login.select().order_by(Login.point)

# Sorting Descending -> Use .decs()
# login_var = Login.select().order_by(Login.timeJoin.desc())


for login in login_var:
    print(login.username + ' ' + str(login.point))

# def get_random():
#     return random.randint(1, 25)

# data = [
#     {'username': 'Brian', 'point': get_random()},
#     {'username': 'Reza', 'point': get_random()},
#     {'username': 'Annas', 'point': get_random()},
#     {'username': 'Taufiq', 'point': get_random()}
# ]
#
# Login.insert_many(data).execute()
