from main import Teacher


try:
    teacher_name = input("Enter name \n")
    teacher_phone = input("Enter phone \n")
    teacher_subject = input("Enter subject \n")
    teacher_password = input("Enter password \n")

    Teacher.create(teacher_name=teacher_name, teacher_phone=teacher_phone, teacher_subject=teacher_subject, teacher_pasword=teacher_password,)
    print("successfully creat account")
except:
    print("fail to creat account")