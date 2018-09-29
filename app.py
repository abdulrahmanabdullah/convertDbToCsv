from controller import Connection_
from model.student import Student

#static  Dic projects :
all_projects = {1 : " Animal Card", 2:" Rock Paper Scissor", 3:" Pixel Art Maker"}

student_project_list = [] # empty list because student add his project.

#
# while True:
#     for item in all_projects.items(): # for loop to extract all projects .
#         print(item)
#
#     try:
#         current_project = int(input(" Please choose which project you work in ? ( type numbers )"))
#     except ValueError as e:
#         print(" Only numbers Accepted ", e)
#         break
#
#     if current_project not in all_projects.keys():
#         print(" Please choose correct number") # if user type number over dic , like 4,5...
#     else:
#         student_project_list.append(all_projects.get(current_project))
#         print(" Ok nice  , Keep going .")
#
#         for item in student_project_list: # for loop to show which project student choice .
#             print(item)
#
#         break
# print(" Hello there , We very excatic to see you here !!")
# print(" We need some info about your's ")
# student_name = input(" Enter your Name Please :")
# init app like create new db and table
# Then create new student obj .
# TODO: Find way to call this method once one.
def init_():
    global conn
    conn = Connection_("my_new_test.db")
    conn._create_table()
    s = Student("aa","bb","cc","gg")
    # conn.insert_new_student(s._generate_id(),s.get_student_name(),"b","c","d")
    # TODO: pass student_name object here, To avoid space or wrong name .
    print(conn.is_user_exists(s.get_student_name()))

 # TODO: import student class and retrive this data from it .

if __name__ == '__main__':
    init_()
