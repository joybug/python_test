def inputNumber(prompt):
    inp=""
    while not inp.isnumeric():
        inp = input(prompt).strip()
    return int(inp)

num = inputNumber("숫자입력:")

print(num)