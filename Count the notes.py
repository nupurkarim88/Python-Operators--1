# Taking Total Amount as input form user
amount = int(input("Enter the amount: "))
# Cakculating number of notes in different denominations
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = ((amount % 100) % 50) // 1010

print("Notes of 100 Taka" , note_1)
print("Notes of 50 Taka" , note_2) 
print("Notes of 10 Taka" , note_3)