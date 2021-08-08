import pygame
from settings import *
from random import randint as rand

pygame.init()

Game = True
Time = True #Режим паузы и выхода
Exit = False #Режим выхода

Admin = True

DataInd = ""

Language = "eng"

Otvet = 0

x = 150 #Координата летящей фигуры по иксу
y = 60 #Координата летящей фигуры по игрику
z = 30 #Ширина и высота плитки, из которых состоят фигуры

SX = z * 12 #360
SY = z * 16 #480

Display = [SX+z*5, SY]

FPS = 60
FPSM = 30 #"Счётчик" падения фигуры

end = False

# Цвета
c = {
    "Black": (0, 0, 0),
    "Mid": (100, 100, 100),
    "Sage": (255, 255, 255), #Белый
    "Red": (255, 0, 0),
    "True": (200, 200, 200), #Цвет белой темы
    "False": (10, 10, 10) #Цвет чёрной темы
}

# Функция для рандомного определения цвета новой фигуры
def NewColor():
    Collor = [rand(0, 255), rand(0, 255), rand(0, 255)]
    return Collor

Color = NewColor()

AntiFon = [200, 200, 200]
Fon = [25, 25, 25]
if Tema:
    Fon = [245, 245, 245]
    AntiFon = [55, 55, 55]

Ci = 40

Sage = [Color[0]+Ci, Color[1]+Ci, Color[2]+Ci]
for i in range(3):
    if Sage[i] > 255:
        Sage[i] = 255

Black = [Color[0]-Ci, Color[1]-Ci, Color[2]-Ci]
for i in range(3):
    if Black[i] < 0:
        Black[i] = 0

icon = pygame.image.load("Om.png") # Загрузка иконки
icon.set_colorkey((c["Black"])) # Очистка картинки (плохо работает)
clock = pygame.time.Clock() # Заготовка для ограничение кадров


# Figur\Сама Фигура (Num)\Фигура (Vert)\x, y (плитки)
if not 1 != 1:
    # Список всех фигур во всех возможных вариантах
    Figur = [ [ [[x, y], [x, y-z], [x-z, y], [x+z, y]],
                [[x, y], [x, y-z], [x, y+z], [x+z, y]],
                [[x, y], [x, y+z], [x-z, y], [x+z, y]],
                [[x, y], [x-z, y], [x, y+z], [x, y-z]] ],
                [ [[x, y], [x, y-z], [x-z, y], [x-z, y-z]] ],
                [ [[x, y+z], [x, y], [x, y-z], [x+z, y-z]],
                [[x, y], [x-z, y], [x+z, y], [x+z, y+z]],
                [[x, y-z], [x, y], [x, y+z], [x-z, y+z]],
                [[x+z, y], [x, y], [x-z, y], [x-z, y-z]] ],
                [ [[x, y+z], [x, y], [x, y-z], [x-z, y-z]],
                [[x, y], [x-z, y], [x+z, y], [x+z, y-z]],
                [[x, y-z], [x, y], [x, y+z], [x+z, y+z]],
                [[x+z, y], [x, y], [x-z, y], [x-z, y+z]] ],
                [ [[x, y-z*2], [x, y-z], [x, y], [x, y+z]],
                [[x-z, y], [x, y], [x+z, y], [x+z*2, y]] ],
                [ [[x-z, y], [x, y], [x, y-z], [x+z, y-z]],
                [ [x, y-z], [x, y], [x+z, y], [x+z, y+z] ]],
                [ [[x, y], [x+z, y], [x, y-z], [x-z, y-z]],
                [[x, y], [x, y-z], [x-z, y], [x-z, y+z]]  ] ]

Num = rand(0, len(Figur) - 1) # "Сама Фигура"
Pos = rand(0, len(Figur[Num]) - 1)# "Повёрнутость"
Vert = Figur[Num][Pos] #Фигура


New = rand(0, len(Figur) - 1)
NewC = NewColor()

Old = Figur[New]
OldUp = False



Static = []
StaticColor = None

StaticX, StaticY = SX // 2, 0

Shtraf = 0 #z

# Удобный список максимального и минимального икса или игрика
X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
Log = [max(X), min(X)]

Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
Dawe = [max(Y), min(Y)]

#Разрешение на движения, типо эффект нажатия
Start = [False, False, False] #Вниз   вПраво  вЛево

# Счётчики для сброса и начала движения
Eternal = 0 #Вниз
Right = 0 #вПраво
Left = 0 #вЛево

Zone = [] # Хитбоксы поставленых фигур
LGBT = [] # Цвет пост. фигур
Ind = None # Буль для паралельного убирания хитбокса и его цвета

# Заполняем зону "риска" чтоб лет. фигура вниз не улитала, а ставилась
for i in range(12):
    Zone.append( [i*z, Display[1]] )
    LGBT.append(c["Black"])

#Райд
Raid = True #Райд

# Функция для определения заполнение плитками зону с выданным ей игриком
def Limbo(b):#b это должен быть у
    f = 0
    for q in range(12):
        if [q*z, b] in Zone:
            f += 1
            if f >= 12:
                return b #375

        else:
            return z**2 #625

Limb = 0 #Зеркало игрика который мы вложили в Limbo()

Evil = False
Stop = False

Sckore = 0


#< ЛАУНЧЕР ДАТА > (и немного < ЫГР. ДАТА >)

Menu = True #Буль главного цикла меню

# Локализация
Eng = ["Start", "Quit", "Tetris", "Pause", "Press agin on the", "SPACE to remove pause", "Yes", "No", "Getting out?", "Sckore", "Max", "Settings", "Tetris", "To return", "Fone:", "Black", "White", "<", ">", "Sound:", "False", "True", "Yes", "The Game needs a reboot", "New Figur", "Press", "C"]
if Language == "eng":
    Messege = Eng
    Gram = 7

# Обьекты
w = [125, 60] #Ширина и высота прямоугольников в меню на которых разположен текст

StartKnow = False
EndKnow = False

StartCol = Color
EndCol = Color


StartList = []
def Next(y):
    for q in range(w[0]):
        StartList.append( [z+i, y] )

for i in range(w[1]):
    Next(w[1]+i)


# Шрифты
Stand = pygame.font.Font(None, 50) # Старт и выход
Big = pygame.font.Font(None, 70) # Лого

Paus = pygame.font.Font(None, 33) # Пауза
PauseLIttle = pygame.font.Font(None, 25) #Выход из паузы

Little = pygame.font.Font(None, 20)

f1 = pygame.font.Font(None, 35) # Надпись счёт
f2 = pygame.font.Font(None, 31) # числа

# Текст для вывода
St = Stand.render(Messege[0], 1, AntiFon) #Старт
Qu = Stand.render(Messege[1], 1, AntiFon) #Выход
Opt = f1.render(Messege[11], 1, AntiFon)#Настройки
Tet = Big.render(Messege[2], 1, AntiFon) #Лого

Return = f1.render(Messege[13], 1, Fon) #Кнопка назад
Ofor = Paus.render(Messege[14], 1, Fon) #"Тема"

if Tema:
    Im = 16
else:
    Im = 15

Junqor = f1.render(Messege[Im], 1, Fon)

TextSckore = f1.render(Messege[9] + " " + str(Sckore), 1, Color)
TextMaxSckore = f1.render(Messege[9] + " " + Messege[10] + " " + str(Sckore), 1, Color)

# Разрешение экрана
Screen = [320, 230]

Event = 1
Str = False

Optional = False
U = 2

SettY = Screen[1]
Polet = False

Wibor = False

if not Tema:
    Slave = 15
elif Tema:
    Slave = 16

OldSlave = Slave
SoundX = Sound


Her = None
Orden = False
ColorN = Fon

TypeX = x
TypeY = y
