#from module_3_4 import result


#def summa(n):
#    if n == 0:
#       return 0
#        return n + summa (n - 1)

#print(summa(5))
###stack.append(2)
#stack.append(3)
#print("Добавили элемент",stack)
#print(stack)
#stack.pop()
#print("Убрали элемент",stack)
#stack.pop()
#print("Убрали элемент",stack)
#stack.pop()
#print("Убрали элемент",stack)


def get_multiplied_digits(number):
   str_number = str(number)
   if len(str_number) > 1:
       first = int(str_number[0])
       return first * get_multiplied_digits(int(str_number[1:]))

   else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(510024)
print(result2)


#def get_multiplied_digits(nomber):
#    str_number = str(nomber)
#    if len (str_number) > 1:
#        first = int(str_number[0])
#       return first * get_multiplied_digits(int(str_number[1:0]))

#   else:
#        return int(str_number)



#result = get_multiplied_digits(40203)
#print(result)
#result2 = get_multiplied_digits(402030)
#print(result2)