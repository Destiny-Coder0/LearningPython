# Find if the number is prime or not
# Prime numbers are numbers that have only 2 factors: 1 and themselves. 2,3,5,7,11...

print("= Welcome to the prime number checker =")
num=int(input("Enter a number: "))

isPrime=True
if(num<0):
    print("You entered a negative number.")

elif(num>=0 and num<2):
    print("The smallest prime number is 2.")

else:
    for i in range(2, int(num**0.5)+1):
        if (num%i ==0):
            isPrime=False
            break
    
    if(isPrime):
        print(f"{num} is a prime number.")

    else:
        print(f"{num} is not a prime number.")