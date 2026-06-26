mark = int(input("Enter Your Marks:"))

if mark <0 or mark>100:
  print("Marks must be between 0 and 100.")
elif mark >=90 and mark <=100 :
  grade = 'GRADE A'
elif mark >=80 and mark <=89 :
  grade = 'GRADE B'
elif mark >=70 and mark <=79 :
  grade = 'GRADE C'
elif mark >=60 and mark <=69 :
  grade = 'GRADE D'
else :
  grade = 'FAIL'

print(grade)
