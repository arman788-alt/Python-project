# Basic calculator project

def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}\n')

def subsraction(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}\n')

def multiplication(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}\n')

def division(num1, num2):
      if num2 == 0:
          print(f'Sorry zero is not divided by {num1}\n')
      else: 
          
        result = num1 /num2
        print(f'{num1} / {num2} = {result}\n')


    

while True:

    print('What do you want to do ?')
    print('1 for addition')
    print('2 for subsraction')
    print('3 for multiplication')
    print('4 for division')
    print('Enter Q or q for Exit the calculation\n')
       
    choice = input('Enter your choice : ')
    num1 = float(input('Enter number 1 : '))
    num2 = float(input('Enter number 2 : '))

    if choice == '1':
      addition(num1, num2)

    elif choice == '2':
      subsraction(num1, num2)

    elif choice == '3':
       multiplication(num1, num2)

    elif choice == '4':
      division(num1, num2)

    elif choice == ' Q' or choice == 'q':
       break

    else: 
       print('Invalid choice\n')




