import sys
import time

f = None
try:
    f = open('07_Eception_Handling/txt.text', 'r') 
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")
        sys.stdout.flush()
        print('press Ctrl+c now')
        time.sleep(4)
except IOError:
    print('could not find text.txt file')
except KeyboardInterrupt:
    print('you canceled reading file')
except AttributeError as er:
    print(er)
finally:
    if f:
        f.close()
    print('the file has been closed')