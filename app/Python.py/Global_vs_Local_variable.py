a = 10              # global variable
def something():
    a = 15          # local variable
    print("print: ",a)
something()
print("print: ",a)

a = 10                    # global variable
def something():

    print(globals())     # Using Global variable 
    a = 15               # local variable
    print("print: ",a)
something()
print("print: ",a)

a = 10                    # global variable
def something():

    print(globals()["a"])    # Using Global variable 
    a = 15               # local variable
    print("print: ",a)
something()
print("print: ",a)

a = 10                    # global variable
def something():
    a = 15                      # # local variable
    globals()["a"]# Global variable 
                
    print("print: ",a)
something()
print("print: ",a)


x = 20
def update():
    global x
    x = 10
    print("Inside function: ", x)

update()
print("Outside function: ",x)