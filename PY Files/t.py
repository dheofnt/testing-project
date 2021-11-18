y = 30
def my_func():
    global x
    x = 10
    print('Value Inside Function:',y)
x = 20
my_func()
print('Value outside Function:',x)


dict = {
    'nama' : 'Dheo',
    'Kelas' : '10',
    'Nilai' : '90'
}


def sum_all(numbers):
    total = 0
    for x in numbers:
        if x%2 == 0:
            total += x

print(sum_all(8,4,7,2,5))