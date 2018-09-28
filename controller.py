import sqlite3
class Connection_:
    table_name = " student"
    sql = ''' create table if not exists'''+table_name+'''
        (student_id INTEGER PRIMARY KEY NOT NULL  ,
        student_name VARCHAR(45),
        projects VARCHAR(45) ,
        project_status VARCHAR(45),
        project_submit date
        )
'''
    connection = None
    # init and connect to db .
    def __init__(self,db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

    # Create new table .
    def _create_table(self): # priavte method
        global connection
        try:
            cursor_ =self.connection.cursor()
            cursor_.execute(self.sql)
        except sqlite3.Error as e :
            print(" Failed to connection : %s "%e)
        except Exception as e :
            print(" Unkown Error : %s"%e)

    def insert_new_student(self,student_id, student_name,projects,project_status,project_date):
        try:
            cursor_ = self.connection.cursor()
            list_=[student_id, student_name, projects, project_status, project_date]
            # TODO :solve unique id .
            cursor_.execute(" INSERT INTO "+self.table_name+" VALUES(?, ?,?,?,?)",list_)
            self.connection.commit()
        except sqlite3.Error as e:
            print(" Failed to  insert data : %s"%e)
        except Exception as e :
            print(" Some thing wrong:  %s"%e)
