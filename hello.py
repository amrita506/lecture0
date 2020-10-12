#python 3 of python web programming
'''name=input()
print(f"Hello,{name}!")#format string
'''
#-----------------------------------------
'''
i=28
print(f"i is {i}")
f=2.8
print(f"f is {f}")
b=True
print(f"b is {b}")
n=None
print(f"n is {n}")
'''
#----------------------------------------------
'''
x=20
if x> 0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x is zero")
'''
#-----------------------------------------------
'''
name="Alice"#string
coordinates=(10.0,20.0)#tuple
names=["Alice","Bob","Charlie"]#list
print(name)
'''

#--------------------------------------
'''
#sets do not have order and no duplicate type
s=set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)
'''
#---------------------------------------------

def square(x):
    return x*x
def main():
    for i in range(10):
        print("{} squared is {}".format(i,square(i)))
if __name__=="__main__":
    main()











