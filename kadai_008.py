ver = x

if ver % 3 == 0 and ver % 5 == 0:
    print("FizzBuzz")
   
elif ver % 5 == 0:
    print("Buzz")
    
elif ver % 3 ==0:
    print("Fizz")
    
else:
    print(ver)