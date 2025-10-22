# определение количества дней
def dni(Year, Month):
 print("Подпрограмма dni стартовала!")
 
 if (Month == 2): 
  if (is_visokos(Year)): 
   return (29) 
  else:  
   return (28)
 else:
  if (Month == 1): 
   return (31) 
  elif (Month == 3): 
   return (31) 
  elif (Month == 4): 
   return (30) 
  elif (Month == 5): 
   return (31) 
  elif (Month == 6): 
   return (30) 
  elif (Month == 7): 
   return (31) 
  elif (Month == 8): 
   return (31) 
  elif (Month == 9): 
   return (30) 
  elif (Month == 10): 
   return (31) 
  elif (Month == 11): 
   return (30) 
  elif (Month == 12): 
   return (31) 

# високосный ли год
def is_visokos(Year):
 print("Подпрограмма is_visokos стартовала!")
 
 result = False # значение по умолчанию (не високосный)
 # проверка остатков от деления
 if (Year % 400) == 0:
  result = True # високосный
 elif (Year % 100) == 0:
  result = False # не високосный
 elif (Year % 4) == 0:
  result = True # високосный 
 else: 
  result = False # не високосный. Строку можно исключить т.к. False значение по умолчанию    
 return result # возвращаем результат 
 
# Главная программа - Call Center
print("Приветствую Вас!")

God = int(input("Введите год"))
Mes = int(input("Введите номер месяца"))

Dni = dni(God, Mes)

print("В этом месяце", Dni, "дней")
print("Всего хорошего!")