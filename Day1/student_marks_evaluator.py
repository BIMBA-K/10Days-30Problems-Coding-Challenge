name=input()
marks=list(map(int,(input().split())))
total_marks=sum(marks)
average_marks=total_marks/len(marks)
print(f"Student name: {name}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")
if average_marks>=35:
    print("Result: Pass")
else:
    print("Result: Fail")