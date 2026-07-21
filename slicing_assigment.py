numbers= input("type in four numbers :")
split_numbers = numbers.split()
total =0
for num in  split_numbers:
    total += int(num)
print(total)

def largest (*args):
    return max (args)
results= largest(3,5,100,20,20,6)
print (results)             
#employee details 
#name,department,salary,position
square= lambda x:x*x
print(square)
cube = lambda x:x**3
print(cube)
is_divisible_by_5= lambda x: x% 5 ==0
marks=[20,45,89,76,12,99]
high_mark = [m for m in marks if m>50]
numbers= [x for x in range (1,21)]
add = lambda a,b:a+b
subtract= lambda a,b:a-b
multiply= lambda a,b: a*b
divide = lambda a,b: (a/b) if b !=0 else "ERROR: division by zero"
add_res= add(10,5)
sub_res = subtract(10,5)
multiply_res = multiply(10,5)
divide_res =divide (10,5)
print(add_res)
print(sub_res)
print(multiply_res)
print(divide_res)


