def hello():
    
    print("Hello world!")

hello()

def sum(num1=0,num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2

total = sum( )
print(total)


def  multiple_items(*args):
    print(args)
    print(type(args))
multiple_items(3,4,5)

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first = "Debojyoti", last = "Mondal")