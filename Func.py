def sayHello():
    print("Hello")

sayHello()

def multiply(n1,n2):
    print(n1,"X",n2,"=",n1*n2)

multiply(7,8)    

def displayWelcome(txt):
    borderChar = "*"
    print(borderChar*(len(txt)+4))
    print(borderChar,txt,borderChar)
    print(borderChar*(len(txt)+4))

displayWelcome("Welcomde to Coding World")
