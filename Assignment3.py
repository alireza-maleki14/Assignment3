import math

op=input("Enter op(+ ,- , * , / , sin , cos , tan , cot , factorial , sqrt):")

if op=="+":
    a=int(input("a ra vared konid:"))
    b=int(input("b ra vared konid:"))
    r=a+b
if op=="-":
    a=int(input("a ra vared konid:"))
    b=int(input("b ra vared konid:"))
    r=a-b
if op=="*":
    a=int(input("a ra vared konid:"))
    b=int(input("b ra vared konid:"))
    r=a*b
if op=="/":
    a=int(input("a ra vared konid:"))
    b=int(input("b ra vared konid:"))
    if b==0:
        b=int(input("b ra vared konid:"))
    r=a/b
if op=="sin":
    a=int(input("sin ra vared konid:"))
    r=(math.sin(math.radians(a)))
if op=="cos":
    a=int(input("cos ra vared konid:"))
    r=(math.cos(math.radians(a)))
if op=="tan":
    a=int(input("tan ra vared konid:"))
    r=(math.tan(math.radians(a)))
if op=="cot":
    a=int(input("cot ra vared konid:"))
    r=(1)/(math.tan(math.radians(a)))
if op=="factorial":
    a=int(input("adade made nazar ra vared konid:"))
    r=(math.factorial(a))
if op=="sqrt":
    a=int(input("sqrt ra vared konid:"))
    r=(math.sqrt(a))
print(r)


