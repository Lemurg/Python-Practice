# -*- coding: utf-8 -*-
"""Копия блокнота ""Практика 0.2.0 .ipynb""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wtODvdgTzq1oPF99QX_w7gMZOMzb0LgT

# Основы

Задание 1: Напиши программу, выводящую на экран сообщение "Привет, мир!"
"""

print('Привет, мир')

"""Задание 2: Напиши программу которая запрашивает имя пользователя и выводит сообщение:

`Привет, <Имя пользователя>`
"""

name=input()
print('Привет,', name)

"""Задание 3: Напиши программу определяющую является ли число четным или нечетным:

Пример:

`Введите число:` 2

`Ваше число четное!`
"""

a = int(input('Введите число:'))
if a%2==0:
  print('Число:', a,'четное')
else:
  print('Число:', a,'нечетное')

"""Задание 4: Напишите программу которая запрашивает длинну и ширину прямоугольника и выводит его площадь:



`Введите длинну прямоугольника:`

`Введите ширину прямоугольника:`

`Площадь прямоугольника: `


"""

a = int(input('Введите длинну прямоугольника:'))
b = int(input('Введите ширину прямоугольника:'))
s = a*b
print('Площадь прямоугольника:', s)

"""Задание 5: Напишите программу, которая будет вычислять среднее арифметическое введенных чисел"""

a = list(map(int, input().split())) #Вводить числа через пробел
b=0
for i in range(len(a)):
    b+=int(a[i])
print(b//len(a))

"""Задание 6: Напиши программу, которая бы определяла является ли год високосным"""

a = int(input('Введите год:'))
if a%400==0 and a%100==0:
  print(a,'год високосный')
else:
  if a%100==0:
    print(a,'год не високосный')
  else:
    if a%4==0 and a%100!=0:
      print(a,'год високосный')
    else:
      print(a,'год не високосный')

"""Задание 7: Необходимо создать простой калькулятор, который позволяет пользователю выбрать одну из четырёх операций (+, -, *, /), ввести два числа и получить результат выполнения операции."""

a = str(input('Выберите операцию:'))
b = int(input('Введите число 1:'))
c = int(input('Введите число 2:'))
if a=='+':
  sums=b+c
  print(sums)
if a=='-':
  mins=b-c
  print(mins)
if a=='*':
  sloz=b*c
  print(sloz)
if a=='/':
  deli=b//c
  print(deli)

"""--------------------------------------------------------------------------------

**Да, задания ниже тоже обязательны, вам необходимо выполнить веееееесь файл**

--------------------------------------------------------------------------------

# Практика 0.2.1

**Шахматы**

Даны стартовые и конечные координаты, а также фигура

Необходимо определить, может ли заданная фигура так ходить?
"""

fig = int(input('Веберите фигуру 1.Король 2.Ферзь 3.Ладья 4.Слон 5.Конь 6.Пешка '))
x1,y1=list(map(int,input('Начальные кординаты, x y:').split()))
x2,y2=list(map(int,input('Конечные кординаты, x y:').split()))
def rastxP(z1, z2):
  a=[]
  if 8-z1<=7:
    for i in range(1,abs(8-z1)+1):
      a.append(i*1)
  for i in range(len(a)):
    if (z1+a[i])==z2:
        return True
def rastxM(z1):
  a=[]
  if 8-z1<=7:
    for i in range(1,abs(8-z1-2)):
      a.append(i*1)
  for i in range(len(a)):
    if (z1+a[i])==z2:
        return True
if fig==1:
  if (x2==x1+1 and y2==y1+1) or (x2==x1+1  and y2==y1) or (x2==x1+1 and y2==y1-1) \
   or (x2==x1-1 and y2==y1+1) or (x2==x1-1  and y2==y1) or (x2==x1-1 and y2==y1-1)\
   or (x2==x1 and y2==y1-1) or (x2==x1 and y2==y1+1):
    print('Можно')
  else:
    print('Нельзя')
if fig==5:
  if (x2==x1+2 and y2==y1+1) or (x2==x1+1 and y2==y1+2) or (x2==x1-2 and y2==y1+1)\
   or (x2==x1+2 and y2==y1-1) or (x2==x1-2 and y2==y1-1) or (x2==x1-1 and y2==y1-2)\
   or (x2==x1-1 and y2==y1+2) or (x2==x1-2 and y2==y1+1):
    print('Можно')
  else:
    print('Нельзя')
if fig==6:
  if (x2==x1 and y2==y1+1):
    print('Можно')
  else:
    print('Нельзя')
if fig==3:
  if (rastxP(x1,x2) and y2==y1) or (rastxM(x1,x2) and y2==y1) or (rastxP(y1,y2) and x2==x1) or (rastxM(y1,y2) and x2==x1):
    print('Можно')
  else:
    print('Нельзя')

"""# Практика 0.2.2

**Цифра на определенном месте:**

Последовательно записан натуральный ряд чисел.

Какая цифра стоит в N позиции
"""

a = list(map(int,input().split()))
b = int(input())
s=''
for i in range(len(a)):
  s=s+str(a[i])
print(s[b-1])