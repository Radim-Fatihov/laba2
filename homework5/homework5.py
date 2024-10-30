import random

def find_multiples(x, numbers):
 """
 Функция, которая находит все числа, кратные заданному числу x,
 в списке numbers с помощью лямбда-функции.

 Args:
  x: Число, на кратность которому проверяются числа.
  numbers: Список чисел для проверки.

 Returns:
  Список чисел, кратных x.
 """

 is_multiple = lambda num: num % x == 0
 multiples = list(filter(is_multiple, numbers))
 return multiples

if __name__ == "__main__":
 x = int(input("Введите число X: "))
 numbers = random.sample(range(201), 10) # Генерируем 10 случайных чисел от 0 до 200

 print(f"Список чисел: {numbers}")
 multiples = find_multiples(x, numbers)

 if multiples:
  print(f"Числа, кратные {x}: {multiples}")
 else:
  print(f"В списке нет чисел, кратных {x}.")
