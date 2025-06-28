#Problem Statement: Student Score Management System

# You're developing a Student Score Management System for a school administrator. 

#Each student has:
# A name
# A unique student ID (string, e.g., "S101")
# A list of scores (integers) for different subjects/tests

# Your program should allow the admin to manage student records through a menu-based interface.

#1- Add New Student

    #Input: Name, Student ID
    #If the ID already exists, reject it.

#2-Add Test Scores for a Student

    #Input: Student ID, then one or more scores (allow adding multiple in one go)
    #Append scores to the existing list of that student.

#3-View Student Report

    # Input: Student ID
    # Output: Name, Scores, Highest, Lowest, Average Score

#4-Update Student Score

    # Input: Student ID, index of score to update, and the new score

#5-Delete a Student Record

    # Input: Student ID

#6-Class Analytics

    #Show:

        # Total number of students

        # Average score across all students

        # Student with the highest average score

#7-Top N Students by Average Score

#8-Exit


# students = {
#     "S101": {
#         "name": "Alice",
#         "scores": [85, 90, 78]
#     },
#     "S102": {
#         "name": "Bob",
#         "scores": [70, 88]
#     }
# }


students = {
    "S1": {
        "name": "Alice",
        "scores": [85, 90, 78]
    },
    "S2": {
        "name": "Bob",
        "scores": [70, 88, 91]
    }
}


def add_new_student():
    
    id = f"S{len(students)+1}" 
    name = input ("Give me the students's name.:")
    students[id] = {"name": name, "scores": []}
    # output : Student Zi E with ID S03 is added to database
    print(f"Student {name} with ID {id} is totally added to database")
    print(students)

def add_test_scores(): 
    id = input("What is the student's ID? ")
    if id in students:
        while True:
            ans = input("Press 'a' to add score or 'd' when you are done.")
            if ans == "a":
                score = int(input("What is the score?"))
         
                students[id]["scores"].append(score)
            elif ans == "d":
                break
            else:
                print("Invalid choice")
    else:
        print(f"Student ID {id} is not in our database.")

    print(f"The score for Student ID {id} is added to our database.")
    print(students)
    

    
def view_student_report():
    id = input("What is the student's ID? ")
    if id in students:
        name = students[id]["name"]
        scores = students[id]["scores"]
        print(f"Report for {name} (ID: {id}):")
        print(f"scores: {scores}")
        print(f"Overall Highest: {max(scores)}")
        print(f"Overall Lowest: {min(scores)}")
        sum_score = sum(scores)
        len_score = len(scores) 
        avg_score = sum_score/len_score
        print(f"Overall Average: {avg_score:.3f}")
    else:
        print(f"Error 404. Student not in our database")
    

def change_student_score():
    id = input("What is the student's ID? ")
    if id in students:
        indexValue = int(input(f"Your scores :{students[id]["scores"]}, which index score do you want to update? First value starts from 0 index.") ) 
        updatedScore = int(input("What is the new score? ") )          
        students[id]["scores"][indexValue] = updatedScore  
    else:
        print(f"Student ID {id} is not in our database.")                                       
    
    print(f"Score for Student Id:{id} is updated in our database")
    print(students)
    


def delete_student_record(): 
    # ask which student id to be deleted
    #variable name = information
    id = input ("Which student id would you like to delete???????")

    # check if student delete id is in students dict
    if id in students:
        # if there is a student, delete the student from dict using del function
        del students[id] 
    else: 
        # if not then show the error message that student doesnt exists
        print(f"Student Id:{id} doesn't exist in our database")
    print(students)
        
    

def main():
    
    while True:
        print("\n=====Student Score Management System=====")
        print("1. Add New Student")
        print("2. Add Test Scores")
        print("3. View Student Report")
        print("4. Update Student Score")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-8) here ->")

        # check conditions for choice and call def functions accordingly
        if choice == '1':
            add_new_student()
        elif choice == '2':
            add_test_scores()
        elif choice == '3':
            view_student_report()
        elif choice == '4': 
            change_student_score()
        elif choice == '5':
            delete_student_record()     
        elif choice == '6':
            break
        else:
            print("Invalid choice, only select 1-8 options!")        
                  
            

if __name__ == "__main__":
    main()





# HOMEWORK: Do view_student_report.