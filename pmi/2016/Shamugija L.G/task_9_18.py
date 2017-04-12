#Задача 9. Вариант 18.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли 
#какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем 
#игрок должен попробовать отгадать слово.

#Shamugija L.G.
#13.03.2017

import random
WORDS = ("питон","анаграмма","простая", "сложная", "ответ", "подстаканник", "абсолютный", "мнение",
	"поступить","академия", "оранжевый","апельсин", "громкий","аплодисменты", "цирк","арена", "атака",
	"благоприятный","атмосфера", "старинный", "играть","баскетбол", "беседовать","профессия", "размешиват", 
	"бетон", "благородный", "прочитать", "брошюра", "программа", "заключение", "печать", "кортеж",   "виселица", "игрокон", "устройство", "выбор", "словарь", "книга", "корзина", "фильмы")
print("""
	               Добро пожаловать! 
	Сейчас я загадаю слово. Вам необходимо его отгадать. 
	    Я сообщю вам, сколько в этом слове букв и 
	дам 5 попыток узнать, есть ли какая-либо буква в слове.
	  После вам предоставиться шанс отгадать само слово. 
	\n\t\t\t\t\t\t   Желаю удачи. \n\t\t\t\t\t Она вам понадобиться :) 
	""")
word = random.choice(WORDS)
print("Букв в слове ", len(word))
i = 0
while i != 5 :
 charr = input("По вашему, какая буква есть в этом слове? ")
 if charr in word :
  print("Да")
 else :
  print("Нет")
 i += 1
print("Ну ладно, пришло время угадываать слово.")
entered_name = input("Что за слово я загадал? ")
if entered_name == word :
	print("Да, все верно!")
else :
	print("Нет, ты не угадал")
input("Press Enter for Exit")
