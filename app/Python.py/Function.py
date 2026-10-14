# A function is like a machine.
# You put something in, it does work, and gives you something back.
# You make it once, and use it many times.

def add(x,y):
    a  = x
    b = y
    c = a + b
    return c
   
result = add(2,4)
print("result is", result)


# PRACTICE PROBLEM
def add(x,y):
    a = x
    b = y
    c = a + b 
    print(c)

add(3,2)

def greet(name):
    return f"Hello, {name}!"

print(greet("Ari"))


def create_user(name: str, age: int = 18) -> dict:
    return {"name": name, "age": age, "active": True}

print(create_user("Monda"))
print(create_user("Monda", 21))

def api_response(status, *args, **kwargs):
    return {
        "status": status,
        "data": args,
        "meta": kwargs
    }

print(api_response(200, "user1", "user2", page=1, limit=10))