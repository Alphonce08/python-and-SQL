from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Alkid.db"))

#creating our first table
class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db
Student.create_table(fail_silently=True)



class Product(Model):
    product_price = CharField()
    product_quantity = CharField()
    product_description = CharField()
    product_color = CharField()

    class Meta:
        database = db
Product.create_table(fail_silently=True)



class Users(Model):
    user_name = CharField()
    user_phone = CharField()
    user_email = CharField()
    user_password = CharField()

    class Meta:
        database = db
Users.create_table(fail_silently=True)
