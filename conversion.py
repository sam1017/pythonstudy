class stack():
    def __init__(self):
        self.stackvalue = []

    def is_stack_empty(self):
        if len(self.stackvalue) == 0 :
            return True
        else:
            return False

    def push(self, value):
        self.stackvalue.append(value)

    def pop(self):
        return self.stackvalue.pop()

input_number = int(input("input number:"))
defaut_number = input_number

my_stack = stack()
while input_number > 0:
    my_stack.push(input_number%8)
    input_number = input_number/8

result = ""

while my_stack.is_stack_empty() == False:
    result = result + str(my_stack.pop())
    #print(str(my_stack.pop()))

print("input Decimal number = " + str(defaut_number) + " And conversion Octal is = " + result)
