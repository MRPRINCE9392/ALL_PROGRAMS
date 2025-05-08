from random import choice

import  mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prudhvi12@",
    database="pdbcdb"

)
cursor=conn.cursor()
def add_student():
    id=input("enter id:")
    name=input("enter name:")
    age=input("enter age:")
    grade=input("enter grade")
    cursor.execute("insert into student(id,name,age,grade) values(%s,%s,%s,%s)",(id,name,age,grade))
    conn.commit()
    print("student added.")

def view_students():
    cursor.execute("select *from student")
    for student in cursor.fetchall():
            print(student)

def update_student():
    student_id=input("enter student id to update:")
    name=input("new name:")
    age=input("new age:")
    grade=input("new grade:")
    cursor.execute("update student set name=%s,age=%s,grade=%s where id=%s",(name,age,grade,student_id,))
    conn.commit()
    print("student update.")

def delete_student():
    student_id=input("enter id to delete:")
    cursor.execute("delete from student where id=%s",(student_id,))
    conn.commit()
    print("student delete.")

def menu():
    while True:
        print("\n--- student management system ---")
        print("1.add student")
        print("2.view students")
        print("3.update student")
        print("4.delete students")
        print("5.exit")

        choice=input("enter choice:")

        if choice=="1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("invalid choice")

menu()



