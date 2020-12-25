#FizzBuzz
i = 0
while (i<101):
    if i%3 == 0:
        print("Fizz", end="")
        if i%5 == 0:
            print("Buzz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print (i)
    print();
    i+=1
        
