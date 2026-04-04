---

Краткая шпаргалка по основам Python: методы, функции и конструкции.

---

## Строки (str)
```python
s.lower()         # нижний регистр → 'HELLO' → 'hello'
s.upper()         # верхний регистр → 'hello' → 'HELLO'
s.title()         # каждое слово с заглавной → 'hello world' → 'Hello World'
s.capitalize()    # первая буква заглавная → 'hello world' → 'Hello world'
s.swapcase()      # меняет регистр на противоположный → 'Hello' → 'hELLO'

s.strip()         # убрать пробелы с обеих сторон
s.lstrip()        # убрать пробелы слева
s.rstrip()        # убрать пробелы справа

s.replace('a', 'b')  # заменить все вхождения 'a' на 'b'
s.split()             # разбить строку по пробелам → список слов
s.split(',')          # разбить по разделителю
' '.join(lst)         # собрать строку из списка через пробел

s.find('a')       # индекс первого вхождения, -1 если не найдено
s.rfind('a')      # индекс последнего вхождения, -1 если не найдено
s.index('a')      # как find(), но выбрасывает ошибку если не найдено
s.rindex('a')     # как rfind(), но выбрасывает ошибку если не найдено
s.count('a')      # количество вхождений подстроки

s.startswith('a') # True если строка начинается с 'a'
s.endswith('z')   # True если строка заканчивается на 'z'

s.isalnum()       # True если только буквы и цифры
s.isalpha()       # True если только буквы
s.isdigit()       # True если только цифры
s.islower()       # True если все буквы строчные
s.isupper()       # True если все буквы заглавные
s.isspace()       # True если только пробельные символы

ord('A')          # символ → код (65)
chr(65)           # код → символ ('A')
```

---

## Списки (list)
```python
lst.append(x)      # добавить элемент в конец
lst.extend([1, 2]) # добавить несколько элементов из другого списка
lst.insert(i, x)   # вставить x по индексу i
del lst[i]         # удалить элемент по индексу

lst.remove(x)      # удалить первое вхождение значения x
lst.pop()          # удалить и вернуть последний элемент
lst.pop(i)         # удалить и вернуть элемент по индексу i
lst.clear()        # очистить список

lst.index(x)       # индекс первого вхождения x
lst.count(x)       # количество вхождений x
sum(lst)           # сумма элементов (встроенная функция)

lst.sort()                # сортировка по возрастанию
lst.sort(reverse=True)    # сортировка по убыванию
lst.reverse()             # перевернуть список

lst.copy()         # поверхностная копия списка
```

> ⚠️ `split()` и `join()` — методы **строк**, не списков!

---

## Модуль math
```python
import math

math.sqrt(4)       # квадратный корень → 2.0
math.ceil(2.3)     # округление вверх → 3
math.floor(2.7)    # округление вниз → 2
math.factorial(5)  # факториал → 120
math.pi            # число π → 3.14159...
math.abs(x)        # модуль числа (встроенная: abs(x))
```

---

## Модуль random
```python
import random

random.randint(1, 10)   # случайное целое от 1 до 10 включительно
random.choice([1,2,3])  # случайный элемент из списка
random.shuffle(lst)     # перемешать список (изменяет оригинал)
random.random()         # случайное float от 0.0 до 1.0
```

---

## Мини-проекты

- [Числовая угадайка](mini_projects/Number_Guessing_Game)
- [Магический шар](mini_projects/Magic_8_Ball)
- [Генератор безопасных паролей](mini_projects/Secure_Password_Generator)
- [Шифр Цезаря](mini_projects/Caesar_Cipher)
- [Калькулятор](mini_projects/Number_Base_Converter)
- [Угадайка слов](mini_projects/Word_Guessing_Game)