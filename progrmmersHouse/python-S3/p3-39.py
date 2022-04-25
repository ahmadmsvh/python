star_max = 27

for i in range(1,15):
    star = str()
    for j in range(1,star_max+1):
        star += "*"
    star_max -= 2
    print(star)