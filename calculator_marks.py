#Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum.
def calculate_total(marks):
    # Calculates the total sum of marks in the list.
    total = 0
    for mark in marks:
        total = total + mark
    return total


#Task 2. Write a function calculate_average(marks) that calls calculate_total() and returns the average.
def calculate_average(marks):
    #Calculates the average of marks by using calculate_total()
    total = calculate_total(marks)
    average = total / len(marks)
    return average


#Task 3. Write a function get_grade(average) that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.
def get_grade(average):
    """
    Returns grade based on average marks.
    A: average > 90
    B: average > 75
    C: otherwise
    """
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    else:
        return "C" 
    
#Task 4. Write a function display_report(marks) that calls all three functions above and prints:

def display_report(marks):
    
 #Displays total, average, and grade for the given marks.

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

#Task 5. Add a docstring to each function describing what it does.
#Test your solution with the list [88, 76, 95, 60, 82]

marks = [88, 76, 95, 60, 82]
display_report(marks)