a = 10              # global variable
def something():
    a = 15          # local variable
    print("print: ",a)
something()
print("print: ",a)

a = 10              # global variable
def something():

    print(globals())
    a = 15          # local variable
    print("print: ",a)
something()
print("print: ",a)