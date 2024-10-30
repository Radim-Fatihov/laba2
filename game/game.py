import random

def get_user_choice():
 """
 Запрашивает выбор пользователя и проверяет его корректность.
 """
 while True:
  user_choice = input("Выберите: камень, ножницы, бумага или stop: ").lower()
  if user_choice in ("камень", "ножницы", "бумага"):
   return user_choice
  elif user_choice == "stop":
   return "stop"
  else:
   print("Неверный выбор. Пожалуйста, выберите камень, ножницы, бумага или stop.")

def get_computer_choice():
 """
 Генерирует случайный выбор компьютера.
 """
 choices = ["камень", "ножницы", "бумага"]
 return random.choice(choices)

def determine_winner(user_choice, computer_choice):
 """
 Определяет победителя раунда.
 """
 if user_choice == computer_choice:
  return "Ничья!"
 elif (user_choice == "камень" and computer_choice == "ножницы") or \
    (user_choice == "ножницы" and computer_choice == "бумага") or \
    (user_choice == "бумага" and computer_choice == "камень"):
  return "Вы победили!"
 else:
  return "Компьютер победил!"

def play_game():
 """
 Запускает игру "Камень-ножницы-бумага".
 """
 while True:
  user_choice = get_user_choice()
  if user_choice == "stop":
   break # Выход из цикла, если пользователь ввел "stop"

  computer_choice = get_computer_choice()

  print(f"Вы выбрали: {user_choice}")
  print(f"Компьютер выбрал: {computer_choice}")
  print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
 play_game()
