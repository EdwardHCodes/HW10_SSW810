"""
@Author: Edward Holcomb
Homework 11
This is an assignment that is part of the homework assignment
"""
import os
from typing import Any, List, Tuple, DefaultDict, Optional, Sequence, Iterator
import collections
from collections import defaultdict
import prettytable as ptables
from HW08_Edward_Holcomb import file_reader

"""
We will be using 4 data files:
students.txt
CWID Studentsname Major

instructors file
CWID InstructorName Department

grades file
StudentsID Class Grade InstructorID

majors file
Major RequiredCourse
"""
#Class to contain the Majors
class Major:
    #pt header row to help generate pretty table
    passing_grades: List[str] = ("A", "A-", "B+", "B", "B-", "C+", "C", "C-")
    numerical_grades: Dict[str, float] = {'A': 4.0, 'A-': 3.75,

    'B+': 3.25, 'B': 3.0, 'B-': 2.75,

    'C+': 2.25, 'C': 2.0, 'C-': 0,

    'D+': 0, 'D': 0, 'D-': 0,

    'F': 0}
    #To calculate Student GPA
    #Take Average of the the students courses divided by the total possible score
    #student takes 5 courses and makes B, 3.0, 15.0/20.0
    pt_hdr: Tuple[str, List[str], List[str]] = ("Major", "Required Courses", "Elective Courses")
    
    #initializes a class of major
    def __init__(self, major: str):
        self.major: str = major
        self.req: Set[str] = set()
        self.ele: Set[str] = set()
    
    #need a way to add a course
    #appears that the format
    def add_course(self, course: str, isreq: str):
        if isreq == "R":
            self.req.add(course)
        else:
            self.ele.add(course)

    def pt_row(self) -> Tuple[str, List[str], List[str]]:
        return self.major, sorted(self.req), sorted(self.ele)

    #Remainig REquired Courses
    #what do we need to know
    #What courses did the student take, and what grade did they make?
    def remain_req(self, courses: Dict[str, str]) -> List[str]:
        passed_courses: Dict[str, str] = self.passed(courses)
        return sorted(self.req - set(passed_courses.keys()))
    #REmaining Elective COurses
    def remain_elec(self) -> List[str]:
        passed_courses: Dict[str, str] = self.passed(courses)
        #are there any courses in common between self.req and pass_courses.keys()
        if self.ele.intersection(set(passed_courses.keys())):
            return list()
        else:
            return sorted(self.ele)

    #GPA
    def gpa(self, courses: Dict[str, str]) -> float:
        number_courses: int = 0
        total_points: float = 0.0
        for grade in courses.values():
            if grade in Major.numerical_grades:
                total_points += Major.numerical_grades[grade]
                number_courses += 1
        if number_courses == 0:
            return 0.0
        else:
            return total_points/number_courses
            
            
        
    def passed(self, courses: Dict[str, str]) -> Dict[str, str]:
        passing_dict: Dict[str, str] = dict()
        for course, grade in courses.values():
            if grade in passing_grades:
                passing_dict[course] = grade
        return passing_dict
        

#Student Class to store information about each student
#I worked on this while re-listening to the video, I
#I am still trying to wrap my head around actually implementing public/private methods
class Student:
    pt_hdr: Tuple[str, str, str, List[str], List[str]] = ("CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives", "GPA")
    def __init__(self, cwid: int, name: str, major: Major) -> None:
        self.cwid: int = cwid
        self.name: str = name
        self.major: str = major
        self.courses: Dict[str, str] = dict() #NOT A DEFAULT DICTIONARY Key:Value Course:Grade

    def __str__(self) -> str: #Trying to not just copy the code, and want to try and differientiate my solution.
        return f"{name} has the student ID of {cwid} and is a {major}"

    def add_course(self, course: str, grade: str) -> None:
        self.courses[course] = grade
    
    def pt_row(self) -> Tuple[str, str, str, List[str], List[str], List[str], float]:
        """return a list of values to populate the prettytable for this student"""
        return self.cwid, self.name, self.major, sorted(self.major.passed(self.courses).keys()),\
            sorted(self.courses.keys()), self.major.remain_req(self.courses), \
            self.major.remain_ele(self.courses), self.major.gpa(courses)


#Expression to check for grades
class Instructor:
    pt_hdr: Tuple[str, str, str] = ("CWID", "Name", "Completed Courses")
    def __init__(self, cwid: int, name: str, courses: dict, department: str):
        self.cwid: int = cwid
        self.name: str = name
        self.dept: str = department
        self.courses: DefaultDict[str, int] = defaultdict(int)  # key: course value: number of students

    def add_student(self, Name: str, Course: str, Grade: str): ##Why do we not need to add the grade of the course that the student obtained...?
        self.courses[course] += 1
    
    def pt_rows(self) -> Iterator[Tuple[str, str, str, str, int]]:
        """A generator returning rows to be added to the Instructor pretty table
        The PT
        """
        for course, count in self.courses.items():
            yield self.cwid, self.name, self.dept, course, count

class Repository:
    def __init__(self, dir_path: str, ptables: bool=True):
        self.dir_path: str = dir_path
        self.students: Dict[str, Student] = dict() #This is the string and an instance of class student,
        self.instructors: Dict[str, Instructor] = dict()
        self.majors: Dict[str, Major] = dict() ##
        # I am a little unfamiliar with how we are mapping this self.student and self.instructor because we dont pass those in as parameters in the __init__ method.
        try:
            self.get_majors(os.path.join(dir_path, 'majors.txt'))
            self.get_students(os.path.join(dir_path, 'students.txt'))
            self.get_instructors(os.path.join(dir_path, 'instructor.txt'))
            self.get_grades(os.path.join(dir_path, 'grades.txt'))
        except ValueError as ve:
            print(ve)
        except FileNotFoundError as fnfe:
            print(fnfe)
        if ptables:
            print("\nStudent Summary")
            self.student_table()

            print("\nInstructors Summary")
            self.instructor_table()
   
    def get_majors(self, path:str) -> None:
        """gets majors and required/elective classes"""
        for major, required, course in file_reader(path, 3, sep='\t', header=False):
            if major not in self.majors:
                self.majors[major] = Major(major)
            self.majors[major].add_course(course, isreq)

    def get_students(self, path: str) -> None:
        """
        read students from path and add them to self.students.
        Allow exceptions from reading the file to flow back to the CALLER
        """
        for cwid, name, major in file_reader(path, 3, sep='\t', header=False):
            self.students[cwid] = Student(cwid, name, major)
    
    def get_instructors(self, path:str):
        for cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
            self.instructors[cwid] = Instructor(cwid, name, dept)

    def get_grades(self, path: str):
        """reads GRADES similar to students doc string
        """
        for student_cwid, course, grade, instructor_cwid in file_reader( path, 4, sep="\t", header=False):
            if student_cwid in self.students:
                self.students[student_cwid].add_course(course, grade)
            else:
                print(f"Found grade for unknown student '{student_cwid}'")
            if instructor_cwid in self.instructors:
                self.instructors[instructor_cwid].add_student(course)
            else:
                print(f"Found grade for unknown instructor '{instructor_cwid}'")

    def student_table(self) -> None:
        """print a PT
        """
        pt: PrettyTable = PrettyTable(field_names=Student.pt_hdr)
        for student in self.students.values():
            pt.add_row(student.pt_row())
        print(pt)
    
    def instructor_table(self) -> None:
        """instructor table
        """
        pt: PrettyTable = PrettyTable(field_names=Instructor.pt_hdr)
        for instructor in self.instructors.values():
            for row in instructor.pt_rows():
                pt.add_row(row)
        print(pt)

    def majors_table(self) -> None:
        """instructor table
        """
        pt: PrettyTable = PrettyTable(field_names=Instructor.pt_hdr)
        for major in self.majors.values():
            for row in majors.pt_rows():
                pt.add_row(row)
        print(pt)

    def student_grade_table_db_data(self, dbpath) -> Iterator[Tuple[str, str, str, str, str]]:
        query = """ SELECT s.name AS "Student's Name", s.cwid, g.course, g.grade, i.name AS "Teacher's Name"
                    FROM students AS s
                        JOIN grades AS g ON s.cwid=g.StudentCWID
                        JOIN instructors AS i ON g.InstructorCWID=i.CWID
                        ORDER BY s.name"""
        for row in db.execute(query):
            yield row

    
    def student_grade_table_db(self, dbpath):
        #function to generate a pretty table to that comes from the query above, joining grade table and student table in sqlite.
        pt = PrettyTable(fields = ["Name", "CWID", "Course", "Grade", "Instructor"])
        for row in self.student_grades_table_db_data(dbpath):
            pt.add_row(row)
        print(pt)


def main():
    stevens = Repository(r"C:\Users\Edward\OneDrive - stevens.edu\STEVENS - SSW810\Week 09\students.txt")
    db_file: str = r"C:\Users\Edward\Documents\GitHub\SSW810\HW11DB"
