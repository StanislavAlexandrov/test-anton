# create a function (myFunction) with 2 arguments (arg1, arg2). It must return the sum of the args. 

def myFunction(arg1, arg2):
  return arg1+arg2
  
print(myFunction(2, 3))

#create a function (helloFunction) that takes any number of arguments and prints 'hello third argument'

def helloFunction(*args):
  print("Hello "+ args[2])
  
helloFunction("Vasya", "Lena", "Navukhodonosor")