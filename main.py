

from ast import While


print("=====================================")
print(r"""
 __   __     ______   __     ______
/\ "-.\ \   /\  == \ /\ \   /\  ___\
\ \ \-.  \  \ \  _-/ \ \ \  \ \ \____
 \ \_\\"\_\  \ \_\    \ \_\  \ \_____\
  \/_/ \/_/   \/_/     \/_/   \/_____/
""")
print("=====================================")
print("Welcome to the Student Management System")



def main_menu():
    while True:
     print("System Menu:")
     print("1. Add Student")
     print("2. View Students")
     print("3. Update Student")
     print("4. Delete Student")
     print("5. Find Top Student")
     print("6. Exit")
    
     choice = input("Enter your choice: ")

     if choice == '1':
        add_student()
     elif choice == '2':
        view_students()
     elif choice == '3':
        update_student()
     elif choice == '4':
        delete_student()
     elif choice == '5':
        find_top_student()
     elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
     else:
        print("Invalid choice. Please try again.")
        break

students = []

def add_student():
   id = len(students) + 1
   name = str(input("Please Enter Student Name: "))
   score = float(input("Please Enter Student Score: "))
   students.append({"id": id, "name": name, "score": score})

   print("Student added successfully!")

def view_students():
   if not students:
      print("No students found.")
   else:
      print("Student Lists:")
      print("===============================")

      for stu in students:
         print(f"ID: {stu['id']}, Name: {stu['name']}, Score: {stu['score']}")
      print("===============================")
def update_student():
      print("Update Student")
      print("===============================")
      id = int(input("Please Enter Student ID to Update: "))
      for stu in students:
          if stu['id'] == id:
              name = str(input("Please Enter New Student Name: "))
              score = float(input("Please Enter New Student Score: "))
              stu['name'] = name
              stu['score'] = score
              print("Student updated successfully!")
              return
      else:  
         print("Student not found.")
def delete_student():
   print("Delete Student")
   print("===============================")
   student_id = int(input("Please Enter Student ID to Delete: "))
   for stu  in students:
      if stu['id'] == student_id:
         students.remove(stu)
         print("Student deleted successfully!")
         return
      else:
       print("Student not found.")
   print("===============================")

def find_top_student():
   print("Find Top Student")
   print("===============================")
   if not students:
      print("No students found.")
      return
   max_score_student = students[0]
   for stu in students:
      if stu['score'] > max_score_student['score']:
         max_score_student = stu
   print(f"Top student: Id: {max_score_student['id']}, Name: {max_score_student['name']}, Score: {max_score_student['score']}")
   print("===============================")

if __name__ == "__main__":
   main_menu()

