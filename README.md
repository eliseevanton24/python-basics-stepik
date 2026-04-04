# Python Cheat Sheet (Stepik)

Краткая шпаргалка по основам Python: методы, функции и конструкции.

---

# Строки (str)

```python
s.lower()        # нижний регистр
s.upper()        # верхний регистр
s.title()        # Каждое Слово С Заглавной
s.capitalize()   # Первая буква заглавная

s.strip()        # убрать пробелы с двух сторон
s.lstrip()       # убрать пробелы слева
s.rstrip()       # убрать пробелы справа

s.replace('a', 'b')   # заменить символы
s.split()             # разбить строку в список
' '.join(list)        # собрать строку из списка

s.find('a')     # индекс первого вхождения (-1 если нет)
s.count('a')    # количество вхождений

s.startswith('a')
s.endswith('z')
```

## Списки (list)

```
lst.append(x)     # добавить элемент
lst.extend([1,2]) # добавить несколько
lst.insert(i, x)  # вставить по индексу

lst.remove(x)     # удалить по значению
lst.pop()         # удалить последний
lst.pop(i)        # удалить по индексу
lst.clear()       # очистить список

lst.index(x)      # индекс элемента
lst.count(x)      # количество

lst.sort()        # сортировка
lst.sort(reverse=True)
lst.reverse()     # переворот списка
```

## Модуль math

```
import math

math.sqrt(4)
math.ceil(2.3)
math.floor(2.7)
math.factorial(5)
```

## random

```
import random

random.randint(1, 10)
random.choice([1,2,3])
random.shuffle(list)
```


```markdown
## Мини-проекты

- [Числовая угадайка](mini_projects/Number_Guessing_Game)
- [Магический шар](mini_projects/Magic_8_Ball)
- [Генератор безопасных паролей](mini_projects/password_generatoSecure_Password_Generator)
- [Шифр Цезаря](mini_projects/Caesar_Cipher)
- [Калькулятор](mini_projects/Number_Base_Converter)
- [Угадайка слов](mini_projects/Word_Guessing_Game)