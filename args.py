# def add(a,*args):
#     print("a=",a)
#     print("args= ",args)
#     sum=0
#     for i in args:
#         sum += i
#     print("Sum = ",sum)
# add(20,10,204,49)

def add(**kwargs):
    print(kwargs)
    Sum=0
    for i,v in kwargs.items():
        Sum += v
    print("kwargs Sum = ", Sum)
add(a=10, b=30,c=40)
