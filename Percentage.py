# take marks as input fro,m 

print("Enter the marks of 4 subjects: ")
math = int (input("math :"))
english = int (input("english :"))
science = int (input("science :"))
Bangla = int (input("Bangla :"))  

# Lets Calculate th epercentrage of the marks
sum = math + english + science + Bangla

print("sum of math, english, science, Bangla: ")
perc = (sum/400)*100

print(end= "Percentage of the marks: ")
print(perc)

#output