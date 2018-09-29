import uuid
class Student:
    def __init__(self,student_name,projects,project_status,project_date):
        self.student_name = student_name
        self.projects  = projects
        self.project_status = project_status
        self.project_date = project_date
        self.student_id = self._generate_id()


    #Private method , to set student id .
    def _generate_id(self):
        return uuid.uuid4().int & (1<<16)-1

    # TODO: setatter and getatter for all atributte .
    def get_student_name(self):
        return self.student_name
