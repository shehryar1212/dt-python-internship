def get_student_data():
    # dictionary containing info of studetns and their grades
    data=[{'name':'asad','age':20,'grades':'90,98,78'},
          {'name':'ahmed','age':24,'grades':'89,87,91'},
          {'name':'ali','age':21,'grades':'77,70,90'}]
    return data

def filter_students(data):
    # asks user to enter threshhold int
    threshhold=int(input("Enter the grade threshhold"))
    # created empty list of filtered students
    filtered_students=[]
    # iter through each student in data from above function
    for student in data:
        # using split function separated grades by ',' in each student and then used map func to convert each into int
        grades=list(map(int,student['grades'].split(',')))
        # checking if all grades in each student are > threshhold
        if all(grade>=threshhold for grade in grades):
            # putting data of students into previously created empty list whos grades> threshhold
            filtered_students.append(student)
    return filtered_students



def calculate_average_grade(data):
    avgs=[]
    for student in data:

        grades=list(map(int,student['grades'].split(',')))
        
        avg=sum(grades)/len(grades)
        avgs.append({'name': student['name'], 'average_grade': avg})
    return avgs



def sort_students_by_age(data):
    # Sort the data (list of dictionaries) based on the 'age' key
    sorted_students = sorted(data, key=lambda student: student['age'])
    return sorted_students

def explorer():
    while True:
        try:
            data=get_student_data()
            #view options
            print("\t\t\t Choose an option:")
            print("\n 1-Get student data")
            print("\n 2-Filter students")
            print("\n 3-Calculate average grade")
            print("\n 4-Sort students by age")
            print("\n 5-Exit")

            choice=input("\nEnter 1-5\n")
            if choice=='1':
                print('\n Students data:')
                for student in data:
                    print(f"Name: {student['name']},Age: {student['age']},Grades:{student['grades']}")
            elif choice =='2':
                filtered_students=filter_students(data)
                if filtered_students:
                    print("\n Filtered students: ")

                    for student in filtered_students:
                        print(f"Name:{student['name']},Grade:{student['grades']}")
                else:
                    print('No record found meeting the provided threshhold')
            elif choice=='3':
                print("\n Average grades:")
                avg_grades=calculate_average_grade(data)
                for student in avg_grades:
                    print(f"Name:{student['name']},Average Grade:{student['average_grade']:.2f}")
            elif choice=='4':
                print("\n Sorted students by age:")
                sorted_students=sort_students_by_age(data)
                for student in sorted_students:
                    print(f"Name:{student['name']},Age:{student['age']}")
            elif choice=='5':
                print("Exiting the program")
                break
            else:
                print("Invalid choice")
                
        except Exception as e :
            print(f'An exception occured:{e}')
if __name__=="__main__":
    explorer()
        
        







