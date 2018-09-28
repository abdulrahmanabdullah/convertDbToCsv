from controller import Connection_
from model.student import Student
cxy = Connection_("my_new_test.db")
cxy._create_table()
             # TODO: import student class and retrive this data from it .

print(" Hello there , We very excatic to see you here !!")
print(" We need some info about your's ")
student_name = input(" Enter your Name Please :")
project_list = {'First project':' first project name','Second project':'second project name','Third project':'third project name'} 
# TODO: for loop to show all projects .
student_project = input(" Where you are now ? Choose one of this projects : ( type number ) ")


s = Student("test","test","test","test")
print(s._generate_id())
r = Student("test","test","test","test")
print(r._generate_id())
cxy.insert_new_student(r._generate_id(),"abdulrahman-x","First project","project_submit","project_date")
