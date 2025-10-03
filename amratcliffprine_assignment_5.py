#challange 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
print("Sequence:", end=" ")
137
step_count = 0 

current_nums = []

current_nums.append(current_number)
while current_number != 1: #keeps looping as long as num is not = 1
    if current_number % 2 == 0:
        current_number = current_number // 2
        current_nums.append(current_number)
    elif current_number % 2 != 0:   #if number is not divisble by 2 odd
        current_number = current_number * 3 + 1  #if odd multiply 3 and add 1
        current_nums.append(current_number)
    step_count += 1

for num in current_nums:
    print(num, end=" ")
#output
print()
print("Steps:", step_count)


#challange 2
print("=== Challenge 2: Prime Number Checker ===\n")
n = int(input("Enter a number: ")) #input a number

if n <= 1: #if n is less than 1 or equal to one its not prime
    print(f"{n} is not positive integer greater than 1, so it cannot be prime.")
else:
    print(f"Testing divisors from 2 to {n-1}...")  #numbers in range

    for d in range(2,n): 
        if n % d == 0: # testing every number from 2 and up
            print(f"{n} is not prime (divisible by 3)")
            break #stops loop once divisor is found
    else:
        print(f"{n} is prime!")


#challange 3
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("   ", end="")

#prints header numbers 1-10 across the top
for header in range(1,11):
    print(f"{header:4}", end="")
print()

for row in range(1,11):
    print(f"{row:2} ", end="")
    for col in range(1,11):
        table_value = row * col #multiply row number by colum number
        print(f"{table_value:4}", end="") #keeps colums lined up 
    print()






