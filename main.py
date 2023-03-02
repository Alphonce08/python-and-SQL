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


class Teacher(Model):
    teacher_name = CharField()
    teacher_phone = CharField()
    teacher_subject = CharField()
    teacher_password = CharField()

    class Meta:
        database = db


Teacher.create_table(fail_silently=True)


