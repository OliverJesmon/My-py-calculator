#This program is under development.
#o.py
#importing module
import sys

print("Type exit to exit.")
myOp = input("Enter your mathematical operator:")
  break
#ask number to be operated
if myOp != "exit":
  a = int(input("Enter number:"))
  b = int(input("Enter another number:"))
#condition to stop program
elif myOp == "exit":
  sys.exit()
  print("Program terminated")

#func is defined
def my_function(a,b):
  if myOp == "*" :
    print(int(a*b))
  elif myOp == "+" :
    print(int(a + b))
  elif myOp == "-" :
    print(int(a - b))
  elif myOp == "/" :
    print(int(a / b))

my_function(a,b)
