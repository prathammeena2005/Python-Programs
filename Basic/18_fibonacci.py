lst=[0,1]
first=0
second=1
third=0
for i in range(7):
    third=first+second
    first=second
    second=third
    lst.append(third)
tpl=tuple(lst)
print("First 9 terms of Fibonacci series are: ", tpl)