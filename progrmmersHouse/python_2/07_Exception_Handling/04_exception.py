class ShortInputException(Exception):
    def __init__(self, length, at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least

try:
    text = input('enter something:\t')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except ShortInputException as ex:
    print(('ShortInputException: the input was '+'{0} long, expected at least {1}').format(ex.length, ex.at_least))
except KeyboardInterrupt:
    print('operation has been canceled')
finally:
    print('finally fired')