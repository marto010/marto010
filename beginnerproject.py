Check if a user-entered string contains any digits using a for loop
user = input("Enter: ")
count = 0
for x in user:
   if x.isdigit():
      count += 1

print(f"The number of digits is: {count}")







