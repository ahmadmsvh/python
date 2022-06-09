decimal_number=int(input("enter a number between 0 and 255 to show it into binary:\t"))

counter=decimal_number//128
remaining=decimal_number%128
if counter ==1:
    bit_7=1;
else:
    bit_7=0

counter=remaining//64
remaining=decimal_number%64
if counter ==1:
    bit_6=1;
else:
    bit_6=0

counter=remaining//32
remaining=decimal_number%32
if counter ==1:
    bit_5=1;
else:
    bit_5=0

counter=remaining//16
remaining=decimal_number%16
if counter ==1:
    bit_4=1;
else:
    bit_4=0

counter=remaining//8
remaining=decimal_number%8
if counter ==1:
    bit_3=1;
else:
    bit_3=0

counter=remaining//4
remaining=decimal_number%4
if counter ==1:
    bit_2=1;
else:
    bit_2=0

counter=remaining//2
remaining=decimal_number%2
if counter ==1:
    bit_1=1;
else:
    bit_1=0;

if remaining==1:
    bit_0=1;
else:
    bit_0=0;

print("the binary number is\t %d%d%d%d%d%d%d%db"%(bit_7,bit_6,bit_5,bit_4,bit_3,bit_2,bit_1,bit_0))