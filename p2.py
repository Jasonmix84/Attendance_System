"""
File: py2.py
Author: Jason Rojas
Date:
Lab Section: YOUR LAB Section
Email:  YOUREMAIL@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

# Comment the line below out if your have the load_dictionary function working!!
# Comment the line below out if your have the load_dictionary function working!!

from dataEntryP2 import fillAttendanceData

# Comment the line above out if your have the load_dictionary function working!!
# Comment the line above out if your have the load_dictionary function working!!

# my own function
time_list = []
def seperate_times_from_dates(list):
    for i in list:
        time_list.append(i.split(',')[0])
    return time_list

# my own function
date_list = []
def seperate_dates_from_times(list):
    for i in list:
        date_list.append(i.split(', ')[1])
    return date_list

#completed
def print_list(xlist):
    for i in xlist:
        print(i)

def connect_to_data_file(filename):
    # will return connection to data file
    infile = ""

    try:
        #infile = open("data.txt", "r")
        #infile = open("dataAllShow1stClass.txt", "r")
        #infile = open("dataAllShow1stAnd2ndClass.txt", "r")
        infile = open(filename, "r")

    except FileNotFoundError:
        print("file was not found, try again")

    return infile  # connection with the file

# completed
def display_attendance_data_for_student(student_name, attendance_data):
    for names in attendance_data:
        if student_name in attendance_data:
            return print(student_name, attendance_data[names])
        else:
            return print("No student of this name in the attendance log")

#completed not fully tho need to finish others to finish this one
# prob gonna be the hardest one take a day to solve
students_in_for_n_days = []
def list_students_attendance_count(number, attendance, roster_file):
    class_roster = load_roster(roster_file)
    if number == 0:
        for student in class_roster:
            if student not in attendance.keys():
                students_in_for_n_days.append(student)
            
    else:
        for name, check_ins in attendance.items():
            if number == len(check_ins):
                students_in_for_n_days.append(name)
    return students_in_for_n_days

#completed
def print_count(results):
    """

    :param results:
    :return:
    """
    count = 0
    for i in results:
        count +=1
    return print('There were', count, 'records for this query')

# completed
def print_dictionary(dictionary):
    for name, check_ins in dictionary.items():
        print(name, check_ins)

# completed
def list_all_students_checked_in(date, attendance):
    """

    :param date:
    :param attendance:
    :return:list
    """
    list_of_students_checked_in = []
    for names in attendance:
        for i in attendance[names]:
            if i.endswith(date):
                list_of_students_checked_in.append(names)
    return list_of_students_checked_in


def list_all_students_checked_in_before(date, time, attendance):
    """
    scheck students in before a time and on a date
    param: date
    param: time
    param: file
    return: studnets checked in before a time and on a date
    
    """
    students_on_time = []
    for names, check_ins in attendance.items():
        for check in check_ins:
            date_time = check.split(', ')
            entry_time = date_time[0]
            entry_dates = date_time[1]

        if entry_dates == date:
            if entry_time < time:
                students_on_time.append(names)
    return students_on_time


def is_present(name, date, attendance):
    """
    check if student present on a day
    param: student name
    param: date
    param: data file
    return: True or False
    """
    for student in attendance:  
        if name == student:
            for i in attendance.values():
                check_date_list = seperate_dates_from_times(i)
            for items in check_date_list:
                if date == items:
                    check = True
                else:
                    check = False

    return check


entry_times_on_day = []
def get_first_student_to_enter(date, attendance):
    """
    Get first student to enter
    param: day
    param: datafile
    return: first student to enter
    """
    for names, check_ins in attendance.items():
        for check in check_ins:
            date_time = check.split(', ')
            entry_time = date_time[0]
            entry_dates = date_time[1]

            if entry_dates == date:
                entry_times_on_day.append(entry_time)
                min_time = entry_times_on_day[0]
                for i in entry_times_on_day:
                    if i < min_time:
                        min_time = i
                return names

def load_dictionary(infile):
    """
    Makes a dictionary from text
    Param: textfile
    Returns: a dictionary
    """
    dictionary = {}
    for line in infile:
        all_data = line.split(', ')
        last_name = all_data[0]
        first_name = all_data[1]
        time_stamp = all_data[2]
        date = all_data[3]
        new_line = len(date) - 1
        date = date[0:new_line]
        names = last_name + ', ' + first_name
        time_and_date = time_stamp + ', ' + date

        if names not in dictionary:
            dictionary[names] = []
            dictionary[names].append(time_and_date)
        else:
            dictionary[names].append(time_and_date)

    infile.close()
    return dictionary

def load_roster(roster_file_name):
    """
    Loads the roster
    param: the txt file
    Return: a list of names
    """
    roster = open(roster_file_name, 'r')
    first_and_last_list = []
    for line in roster:
        first_and_last_names = line.split(', ')
        first_name = first_and_last_names[0]
        last_name = first_and_last_names[1]
        new_line = len(last_name) - 1
        last_name = last_name[0:new_line]
        each_name = first_name + ',' + last_name
        first_and_last_list.append(each_name)

    roster.close()
    print(first_and_last_list)
    return first_and_last_list

if __name__ == '__main__':

    infile = connect_to_data_file("dataAllShow1stAnd2ndClass.txt")
    if(infile):
        print("connected to data file...")
    else:
        print("issue with data file... STOP")
        exit(1)

    data = load_dictionary(infile)

    #data = fillAttendanceData()  # write load_dictionary first, never really need this
    # eventually remove line above
    # ************************
    # OR MANUALLY!!!
    # ************************

    # just making sure the data collected is good
    print_dictionary(data)

    print("********* Looking up Student Attendance Data ***********")
    display_attendance_data_for_student("Morrison, Simon", data)
    display_attendance_data_for_student("Arsenault, Al", data)

    print("********* Looking to see if Student was present on date ***********")
    print(is_present("Bower, Amy", "11/5/2022", data))
    print(is_present("Bower, Amy", "11/17/2022", data))

    # # display when students first signed in
    print("**** Students present on this date ****")
    result = list_all_students_checked_in("11/5/2022", data)
    print_list(result)
    print_count(result)

    print("**** Those present on date & before a time assigned ****")
    result = list_all_students_checked_in_before("11/5/2022", "08:55:04", data)
    print_list(result)
    print_count(result)

    # # list the good students that showed up both days
    print("**** Those who attended BOTH classes ****")
    both_days = list_students_attendance_count(2, data, 'rosters.txt')
    print_list(both_days)
    print_count(both_days)

    # # list the  students that showed up ONE of the days
    # # write own stuff
    print("**** Those who attended ONE class ****")
    both_days = list_students_attendance_count(1, data, 'rosters.txt')
    print_list(both_days)
    print_count(both_days)

    # # list the  students that have not shown up
    print("**** Those who have NOT attended a SINGLE class ****")
    both_days = list_students_attendance_count(0, data, 'rosters.txt')
    print_list(both_days)
    print_count(both_days)

    # # Print the first student in the set date
    print('**** First student to enter on 11/2/2022 ****')
    print(get_first_student_to_enter('11/5/2022', data))

    # # print('\nload_roster test')
    # # print_list(load_roster('rosters.txt'))

    # # print('\nload_dictionary test')
    # # print_dictionary(load_dictionary('dataAllShow1stClass.txt'))
