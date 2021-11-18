def fizzBuzz(num):
    # i starts from 1 to num
    for i in range(1, num+1) :

        # Number divisible by 15, (dibisible by both 3 & 5),
        # Print 'FizzBuzz' in place of the number
        if (i % 15 == 0) :
            print('FizzBuzz')

        # Number divisible by 3,
        # print 'fizz' in place of the number
        elif (i % 3 == 0) :
            print('Fizz')

        # Number divisible by 5,
        # print 'Buzz' in place of the number 
        elif (i % 5 == 0) :
            print('Buzz')
        
        # print the number
        else :
            print(i)

fizzBuzz(20)
 
