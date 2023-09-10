#a = input("Scrie numele tau")
#print("Privet, " + a)

#int = -4 #nr.intreg
#float = 3.14 #nr.cu rest
#string = "text" #text
#boolean = True #False #True or False

#print(int)
#print(float)
#print(string)
#print(boolean)

#print(str(int) + str(float) + string + str(boolean))
    #str() - переводит в текст

#print("Hello\n" + "world\n" + "!")
    #между текстом - конкатинация, между числами - вычисления


#print(not boolean) #False, not - opusul
#print(boolean and False) #False
#print(True or False) #True, or - intotdeauna adevarat

#True = R* (R nenul)
#False = 0


#If - Else - Elif
#a = int(input("Scrie varsta"))
#if a > 18:  #если
    #print("U are major")
#else:   #иначе
    #print("Deny")
#elif a == 18:   #не попадает ни в одно предыдущее условие
    #print("Congrats")


#Bucle

#a = 0
#while a != 100: #!= nu este egal
    #print(a)
    #a = a + 0.5   #eteratie - етерация(когда с каждым разом число увеливается на определенное значение
#print("Finish")

#for e in range(1, 100):
   #print(e)




#Русская рутлетка(угадай загаданное число от 1 до 25)

import random
#win - variabila cu nr. corect
#value - nr.
win = random.randint(1, 25)  #библиотека, отвечающая за рандомные числа
value = int(input("Scrie un numar\n"))

while win != value:
    if value > win:
        print("Mai mic")
    else:
        print("Mai mare")

    value = int(input("Incearca altul\n"))
print("Maladet")