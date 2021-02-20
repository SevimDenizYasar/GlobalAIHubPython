students_information = []


def createStudent(name, surname):
    return [name, surname]

def createGrades(midterm, final, homework):
    return [midterm, final, homework]



while True:

    print("[1] - Create Student Information\n")
    print("[2] - List Students Grades\n")
    print("[q] - Quit Program\n")
    option = input("Choose Option: \n")

    if option == "1":

        student = dict()

        name = input("Please Enter Name")
        surname = input("Please Enter Surname")
        student['personal'] = createStudent(name, surname)
        
        midterm = int(input("Enter Midterm Grade"))
        final = int(input("Enter Final Grade"))
        homework = int(input("Enter Homework Grade"))
        student['grades'] = createGrades(midterm, final, homework)

        student['average'] = int(sum([grade for grade in student['grades']]) / 3)

        students_information.append(student)

        print("Student created")

    elif option == "2":

        print("********************* STUDENTS LISTED ***********************")

        for student in students_information:
            name, surname = [i for i in student['personal']]
            midterm, final, homework = [i for i in student['grades']]
            average = student['average']
            print(f"fullname: {name} {surname}, midterm: {midterm}, final: {final}, homework: {homework} -- AVERAGE: {average}")

    elif option == "q":
        break

    else:
        raise Exception("Please Enter Acceptable Values!!")