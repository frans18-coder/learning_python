print("==================")
print("====Calculator====")
print("==================")

print('''
enter an operator below''')
pemilihan_operator = input("( + - * / )")
num1 = float (input("input the first number"))
num2 = float (input("input the second number"))

if pemilihan_operator == "+":
    result = num1 + num2
    print (round(result, 3))
elif pemilihan_operator == "-":
    result  = num1 - num2
    print (round(result, 3))
elif pemilihan_operator == "*":
    result = num1 * num2
    print (round(result, 3))
elif pemilihan_operator == "/":
    result = num1 / num2
    print (round(result, 3))
    
else:
    (f"{pemilihan_operator} bukan operator yang valid")