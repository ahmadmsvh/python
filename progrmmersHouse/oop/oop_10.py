


class Example:
    def __init__(self, *args):
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

        elif isinstance(args[0],int):
            self.answer = args[0] * args[0]

        elif isinstance(args[0], str):
            self.answer = 'hello' + args[0]



e1 = Example(10,20,30,6,9)
print(e1.answer)

e2 = Example(6)
print(e2.answer)

e3 = Example('Python')
print(e3.answer)
