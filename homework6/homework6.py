def get_number():

 for i in range(30):
  if i % 2 != 0:
   yield i

numbers = get_number()

first_num = next(numbers)
print(f"Первое число: {first_num}")

for _ in range(3):
 next(numbers)

fifth_num = next(numbers)
print(f"Пятое число: {fifth_num}")

last_num = None
for num in numbers:
 last_num = num
print(f"Последнее число: {last_num}")
