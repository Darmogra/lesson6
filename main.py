#print (f'NameError - {type(NameError)}')
#print(maxim) #zminna
#print("Hello")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print('start code')
    #print(10/0) #помилка
    print('no errors')
except NameError:
    print("We have an error NameError ")
except ZeroDivisionError:
    print("We have an error ZeroDivisionError ")
print('The end')


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print('start code')
    print(5/0) #помилка
    print('no errors')
except (NameError, ZeroDivisionError) as error:
    print("error")
print('The end')

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    try:
        print('start code')
        print(error)  # помилка
        print('no error')
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)