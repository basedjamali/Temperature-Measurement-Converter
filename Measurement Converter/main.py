import math

print('==== Temperature / Measurement Converter ====')

def fahrenheit_in_celsius():
  while True:
    try:
      fahrenheit = float(input('\n\r[1] Fahrenheit: '))
      formula = (fahrenheit - 32) * 5/9
      print('Celsius:', formula)
      again()
      break
    except ValueError:
      print('Invalid input')


def celsius_in_fahrenheit():
  while True:
    try:
      celsius = float(input('\n\r[2] Celsius: '))
      formula2 = (celsius * 9/5) + 32
      print('Fahrenheit:', formula2)
      again()
      break
    except ValueError:
      print('Invalid input')


def inches_in_centimeter():
  while True:
    try:
      inches = float(input('\n\r[3] Inches: '))
      formula3 = inches * 2.54
      print('Centimeter:', formula3)
      again()
      break
    except ValueError:
      print('Invalid input')


def centimeter_in_inches():
  while True:
    try:
      centimeter = float(input('\n\r[4] Centimeter: '))
      formula4 = centimeter / 2.54
      print('Inches:', formula4)
      again()
      break
    except ValueError:
      print('Invalid input')


def foot_in_meter():
  while True:
    try:
      foot = float(input('\n\r[5]Foot: '))
      formula5 = foot / 3.281
      print('Meter:', formula5)
      again()
      break
    except ValueError:
      print('Invalid input')

      
def meter_in_foot():
  while True:
    try:
      meter = float(input('\n\r[6] Meter: '))
      formula6 = meter * 3.281
      print('Foot:', formula6)
      again()
      break
    except ValueError:
      print('Invalid input')

      
def again():
  asking_user = input('Back to the starting screen [y/n]: ')
  
  while True:
    if asking_user == 'y':
      return starting_screen()
    else:
      print('See you next time!')
      break

      
def starting_screen():
  options = '\n\r[1] Fahrenheit in Celsius\n[2] Celsius in Fahrenheit\n[3] Inches in Centimeter\n[4] Centimeter in Inches\n[5] Foot in Meter\n[6] Meter in Foot\n\r'
  print(options)
  user_chosen_option = int(input('Choose one number from above: '))
  
  while True:
    if user_chosen_option == 1:
      fahrenheit_in_celsius()
      break
      
    elif user_chosen_option == 2:
      celsius_in_fahrenheit()
      break
      
    elif user_chosen_option == 3:
      inches_in_centimeter()
      break
      
    elif user_chosen_option == 4:
      centimeter_in_inches()
      break
      
    elif user_chosen_option == 5:
      foot_in_meter()
      break
      
    elif user_chosen_option == 6:
      meter_in_foot()
      break
      
    else:
      print('Invalid input')
      break
starting_screen()
