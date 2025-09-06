marks_in_exam1 = float(input("Enter marks obtained in Exam 1: "))
marks_in_exam2 = float(input("Enter marks obtained in Exam 2: "))

tota_marks = marks_in_exam1 + marks_in_exam2
avg_marks = tota_marks/2

sport = float(input("Enter makrks scored in sports : "))
act1 = float(input("Enter the Ist activities marks: "))
act2 = float(input("Enter the IInd 3 activities marks: "))
act3 = float(input("Enter the IIrd 3 activities marks: "))
avg_activity = (act1 + act2 +act3)/3

result = (avg_marks*0.5) + (sport*0.2) + (avg_activity*0.3)
print(f"The Student result based on the weightage is : {result} %")