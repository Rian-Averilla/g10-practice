from pyscript import display
#integer

# 0 /
# Using comma /
#using underscore works

fullname = 'Juan Dela Cruz' # string 
age = 25 # integer

display(f'Hi! I am {fullname} and I am {age} years old.', target="result")

_cool = "Cool"
b = ["one", "two", "three"]
Wow = (1, 2, 3)

display(type(_cool))
display(type(b))
display(type(Wow))

display((_cool))
display((b))
display((Wow))

a = 0
f = 0.1

display(bool(a))
display(bool(f))
