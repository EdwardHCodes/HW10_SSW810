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
#Class to contain the Majors
class Major:
    #pt header row to help generate pretty table
    pt_hdr: Tuple[str, List[str], List[str]] = ("Major", "Required Courses", "Elective Courses")
    passing_grades: List[str] = ("A", "A-", "B+", "B", "B-", "C+", "C", "C-")

    #initializes a class of major
    def __init__(self, major: str):
        self.major = major
        self.req_courses = list()
        self.ele_courses = list()
    
    #need a way to add a course
    #appears that the format
    def add_course(self, course: str, isreq: str):
        self.major[course] = course
    
    def isreq(self):
        self.req_course = req_course
        self.ele_course = ele_course

    def pt_row(self) -> Tuple[str, List[str], List[str]]:
        return self.major, self.req_courses, self.ele_courses

#Student Class to store information about each student
#I worked on this while re-listening to the video, I
#I am still trying to wrap my head around actually implementing public/private methods
class Student:
    pt_hdr: Tuple[str, str, str, str, str] = ("CWID", "Name", "Major", "Completed Courses", "Required Courses", "GPA")
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
        self.Student: str = Dict[str, Student] = dict() #This is the string and an instance of class student,
        self.instructor: str = Dict[str, instructor] = dict()
        # I am a little unfamiliar with how we are mapping this self.student and self.instructor because we dont pass those in as parameters in the __init__ method.
        try:
            self.get_students(os.path.join(dir_path, 'students.txt'))
            self.get_instructors(os.path.join(dir_path, 'instructor.txt'))
            self.get_grades(os.path.join(dir_path, 'grades.txt'))
            self.get_majors(os.path.join(dir_path, 'majors.txt'))
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
        for 

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


def main():
    stevens = Repository("C:\Users\Edward\OneDrive - stevens.edu\STEVENS - SSW810\Week 09\students.txt")
