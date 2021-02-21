import turtle as t

def printl(a):
        t.penup()
        for i in range(2):
            t.right(a[2 * i])
            t.forward(a[2 * i + 1])
        for i in range(2, len(a) // 2):
            t.pendown()
            t.forward(a[2 * i])
            t.right(a[2 * i + 1])
        t.penup()
        t.right(90)
        t.forward(15)
        t.pendown()

t.shape("turtle")
t.goto(0, 0)
file = open('num.txt', 'r')
stroka = file.readlines()
count = 0
for i in stroka:
    stroka[count] = i.split(' ')
    count += 1
for list in stroka:
    list.pop()
for list in stroka:
    for i in range(len(list)):
        list[i] = float(list[i])

for i in [0, 1, 2, 3, 4, 5]:
    printl(stroka[i])

input()

