from datetime import date, datetime

def calculate_age(birthdate_str):

  try:
    birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y").date()
  except ValueError:
    raise ValueError("Неверный формат даты рождения. Используйте формат день.месяц.год.")

  today = date.today()

  if birthdate > today:
    return "Вы еще не родились!"
  else:
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age_days = (today - birthdate).days

    return f"Ваш возраст: {age_years} лет или {age_days} дней."


if __name__ == "__main__":
  birthdate = input("Введите дату рождения в формате день.месяц.год: ")
  try:
    result = calculate_age(birthdate)
    print(result)
  except ValueError as e:
    print(f"Ошибка: {e}")



