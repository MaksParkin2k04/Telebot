import sys
input("Введите число с ковычками")
input("s = ")
s = input()
if len(s) > 15 :
    sys.exit("errors!")
new_s = [*s]
new_s_2 = new_s
new_list =    ["I", "V", "X", "L", "C", "D", "M"]
new_list_num = [1,   5,  10,  50,  100, 500, 1000]
num = 0
i = 0
x = 0

del new_s[0]
del new_s[-1]

while new_s[i] != new_list[x]:
    x += 1
    if x >= 7:
        sys.exit("errors!")

while new_s_2[i] == new_list[x]:

        if x == 0:
            num = num + 1
        if x == 1:
            num = num + 5
        if x == 2:
            num = num + 10
        if x == 3:
            num = num + 50
        if x == 4:
            num = num + 100
        if x == 5:
            num = num + 500
        if x == 6:
            num = num + 1000

        if len(new_s) > 1:
            if new_s[0] == new_list[0] and new_s[1] == new_list[1]:
                num = num - 2
            if new_s[0] == new_list[0] and new_s[1] == new_list[2]:
                num = num - 2
            if new_s[0] == new_list[2] and new_s[1] == new_list[3]:
                num = num - 20
            if new_s[0] == new_list[2] and new_s[1] == new_list[4]:
                num = num - 20
            if new_s[0] == new_list[4] and new_s[1] == new_list[5]:
                num = num - 200
            if new_s[0] == new_list[4] and new_s[1] == new_list[6]:
                num = num - 200

        del new_s_2[i]
        x = 0
        if i >= len(new_s):
            break
        while new_s[i] != new_list[x]:
            x += 1
            if x >= 7:
                sys.exit("errors!")
        if i >= len(new_s):
            break

print(num)