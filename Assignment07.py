Name : str = (input ("Enter your name : "))

Numbers = []
Numbers.append (int(input("Enter your 1st favorite number : ")))
Numbers.append (int(input("Enter your 2nd favorite number : ")))
Numbers.append (int(input("Enter your 3rd favorite number : ")))

print(f"\nHi,{Name}! Welcome to the number exploration tool : ")

for number in Numbers:
    if number % 2 == 0:
       print ( f"The Number {number} is Even.")
    else:
        print (f"Thr number {number} is odd.")

for number in Numbers:
    print (f"The number {number} and its square is : {number,number**2}")

total = sum(Numbers)
print (f"\nAmazing! The sum of your favorite number is : {total}")

# Step 6: Check if the sum is a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(total):
    print(f"The sum, {total}, is a prime number!")
else:
    print(f"The sum, {total}, is not a prime number.")