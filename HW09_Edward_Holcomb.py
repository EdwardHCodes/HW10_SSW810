"""
@Author: Edward Holcomb
Homework 09
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
#Student Class to store information about each student
#I worked on this while re-listening to the video, I
#I am still trying to wrap my head around actually implementing public/private methods
class Student:
    pt_hdr: Tuple[str, str, str] = ("CWID", "Name", "Completed Courses")
    def __init__(self, CWID: int, Name: str, Major: str) -> None:
        self.cwid: int = CWID
        self.name: str = Name
        self.major: str = Major
        self.courses: Dict[str, str] = dict() #NOT A DEFAULT DICTIONARY 

    def __str__(self) -> str: #Trying to not just copy the code, and want to try and differientiate my solution.
        return f"{Name} has the student ID of {CWID} and is a {Major}"

    def add_course(self, course: str, grade: str) -> None:
        self.courses[course] = grade
    
    def pt_row(self) -> Tuple[str, str, List[str]]:
        """return a list of values to populate the prettytable for this student"""
        return self.cwid, self.name, sorted(self.courses.keys())
    


#Expression to check for grades
class Instructor:
    pt_hdr: Tuple[str, str, str] = ("CWID", "Name", "Completed Courses")
    def __init__(self, CWID: int, Name: str, Courses: dict, Department: str):
        self.cwid: int = CWID
        self.name: str = Name
        self.dept: str = Department
        self.courses: DefaultDict[str, int] = defaultdict(int)  # key: course value: number of students

    def add_student(self, Name: str, Course: str, Grade: str): ##Why do we not need to add the grade of the course that the student obtained...?
        self.name: str = Name
        self.grade: str = Grade
        self.course: str = Course

class Grade:
    def __init__(self, CWID: int, Course: str, Grade: str):
        pass

class University:
    def __init__(self, Students: List: int, Name: str, Major: str):
        pass
    def __str__(self) -> str:
        self.Name = Name

class Repository:
    def __init__(self, dir_path: str, ptables: bool=True):
        self.dir_path: str = dir_path
        self.Student: str = Dict[str, Student] = dict() #This is the string and an instance of class student,
        self.instructor: str = Dict[str, instructor] = dict()
        # I am a little unfamiliar with how we are mapping this self.student and self.instructor because we dont pass those in as parameters in the __init__ method.
        try:
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

            print("\ninstructors Summary")
            self.instructor_table()
    def get_students(self, path: str) -> None:
        """read students from path and add them to self.students.
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



def main():
    stevens = Repository("C:\Users\Edward\OneDrive - stevens.edu\STEVENS - SSW810\Week 09\students.txt")
    test = Respository()
    njit = 

