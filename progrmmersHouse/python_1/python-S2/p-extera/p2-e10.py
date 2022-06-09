decimal_number=int(input("enter a number between 0 and 255 to show it into binary:\t"))

remaining=decimal_number%2
counter=decimal_number//2
if remaining ==1:
    bit_0=1;
else:
    bit_0=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_1=1;
else:
    bit_1=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_2=1;
else:
    bit_2=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_3=1;
else:
    bit_3=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_4=1;
else:
    bit_4=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_5=1;
else:
    bit_5=0

remaining=counter%2
counter=counter//2
if remaining ==1:
    bit_6=1;
else:
    bit_6=0;

if counter==1:
    bit_7=1;
else:
    bit_7=0;

print("the binary number is\t %d%d%d%d%d%d%d%db"%(bit_7,bit_6,bit_5,bit_4,bit_3,bit_2,bit_1,bit_0))