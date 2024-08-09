first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third:
    print('Всечисла совпадают:', '3')
elif (first == second != third or first == third != second
      and second == first != third or second==third != first
      and third == second != first or third == first != second):
    print('Cовпадают два числа','2')
elif first != second != third:
    print('Числа не совпадают: ' '0')