from data import *
pygame.init()

Launch = pygame.display.set_mode((Screen))

pygame.display.set_icon(icon) # Установление действующий иконки
pygame.display.set_caption(Messege[12])

# Главный цикл меню
while Menu:
    clock.tick(FPSM)

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            Menu = False
            end = True

        elif i.type == pygame.KEYDOWN:

            #НАСТРОЙКИ
            if (i.key == pygame.K_RETURN or i.key == pygame.K_SPACE) and Optional:
                if Str or Event == 1:
                    Optional = False
                    Event = 1
                    Str = True

                elif Event == 2:
                    if not Wibor:
                        Wibor = True

                    elif Wibor:
                        Wibor = False

                elif Event == 0:
                    if Sound:
                        Sound = False
                    elif not Sound:
                        Sound = True


            #МЕНЮ
            elif (i.key == pygame.K_RETURN or i.key == pygame.K_SPACE) and not Optional:
                if Str:
                    Optional = True

                if Event == 0:
                    Menu = False
                elif Event == 2:
                    Menu = False
                    end = True


            if ((i.key == pygame.K_DOWN or i.key == pygame.K_s) or (Optional and (i.key == pygame.K_UP or i.key == pygame.K_w))) and not Wibor:
                Str = True
                Event = 1

            if ((i.key == pygame.K_UP or i.key == pygame.K_w) or (Optional and (i.key == pygame.K_DOWN or i.key == pygame.K_s))) and not Wibor:
                if not Optional:
                    Str = False
                elif Optional:
                    Str = True

            if not Wibor:
                if i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                    if Event < 2 and not Polet:
                        Event += 1
                        Str = False

                if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                    if Event > 0 and not Polet:
                        Event -= 1
                        Str = False

            elif Wibor:
                if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                    Slave -= 1

                if i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                    Slave += 1


                if Slave > 16:
                    Slave = 15

                elif Slave < 15:
                    Slave = 16



    # Прорисовка
    Launch.fill((Fon)) #Фон

    # Прямоугольники на каторых расположен текст
    pygame.draw.rect(Launch, (Color), (25*2 + 25//2, 25*3-Screen[1]+SettY, 200, 2))#Лого

    #Старт
    if Event == 0 and not Optional:
        pygame.draw.rect(Launch, (StartCol), (25, Screen[1]-25*4-Screen[1]+SettY, w[0], w[1]), 5)

    #Выход
    elif Event == 2 and not Optional:
            pygame.draw.rect(Launch, (EndCol), (25*2 + w[0]-Screen[1]+SettY, Screen[1]-25*4, w[0], w[1]), 5)

    #Кружок ВКЛ
    elif Event == 1 and not Str and not Optional:
        pygame.draw.circle(Launch, Color, (37+w[0], Screen[1]-25*3-Screen[1]+SettY), 11)

    #Кружок ВЫКЛ
    if Event != 1 or Str:
        pygame.draw.circle(Launch, Color, (37+w[0], Screen[1]-25*3-Screen[1]+SettY), 6)

    # Прямоугольник обтикающий надпись настройкАв
    if Str and Language == "eng" and not Optional:
        pygame.draw.rect(Launch, (EndCol), (w[0]-23, Screen[1]-25*2-Screen[1]+SettY, w[0]-7, 50), 5)


    # Текст на кнопках
    Launch.blit(Tet, (25*3 + 25//2, 25*1-Screen[1]+SettY)) #Лого

    Launch.blit(St, (25+20, Screen[1] - 25*4 + 10-Screen[1]+SettY))#Старт
    Launch.blit(Opt, (112, Screen[1] - 25*3 +38-Screen[1]+SettY))#Настройки
    Launch.blit(Qu, (25*3 + w[0], Screen[1] - 25*4 + 10-Screen[1]+SettY))#Выход


    # Меню настроек
    # Фон
    pygame.draw.rect(Launch, (Color), (10, 10+SettY, Screen[0]-20, Screen[1]-20))

    # Рамка у надписи звука
    if Event == 0:
        pygame.draw.rect(Launch, (Fon), (20, Screen[1]+25*6-(Screen[1]-SettY)-5, w[0]-7, 65), 5)


    # Фон и рамка выбора фона
    elif Event == 2 and Optional:
        if not Wibor:
            pygame.draw.rect(Launch, (Fon), (155+30, Screen[1]+25*6-(Screen[1]-SettY)-5, w[0]-7, 65), 5)
        elif Wibor:
            pygame.draw.rect(Launch, (Fon), (155+30, Screen[1]+25*6-(Screen[1]-SettY)-5, w[0]-7, 65))


    #"Вернуться"
    if Optional and Str or Event == 1 and not Polet:
        pygame.draw.rect(Launch, (Fon), (w[0]-20, Screen[1]+15-Screen[1]+SettY, w[0]-7, 50), 5)


    # Подчёркнутость отсутствие звука
    if not Sound:
        pygame.draw.line(Launch, (Fon), [30, Screen[1]+25*7-(Screen[1]-SettY)-3], [127, Screen[1]+25*7-(Screen[1]-SettY)-3], 3)

    #Надпись "настройки"
    Launch.blit(Return, (111, Screen[1] + 25-Screen[1]+SettY))

    # Надпись "звук"
    Launch.blit(Paus.render(Messege[19], 1, Fon), (42, Screen[1]+25*6-(Screen[1]-SettY)) )
    if Sound:
        Launch.blit(f1.render(Messege[22], 1, Fon), (55, Screen[1]+25*7-(Screen[1]-SettY)+5) )


    # Настройки фона
    if not Wibor:
        Launch.blit(Paus.render(Messege[14], 1, Fon), (155+60, Screen[1]+25*6-(Screen[1]-SettY)) )
        Launch.blit(f1.render(Messege[Slave], 1, Fon), (130+80, Screen[1]+25*7-(Screen[1]-SettY)+5) )
    elif Wibor and Event == 2:
        Launch.blit(Paus.render(Messege[14], 1, Color), (155+60, Screen[1]+25*6-(Screen[1]-SettY)) )
        Launch.blit(f1.render(Messege[Slave], 1, Color), (130+80, Screen[1]+25*7-(Screen[1]-SettY)+5) )
        Launch.blit(f1.render(Messege[17], 1, Color), (130+60, Screen[1]+25*7-(Screen[1]-SettY)+5) )
        Launch.blit(f1.render(Messege[18], 1, Color), (130+155, Screen[1]+25*7-(Screen[1]-SettY)+5) )

    if (OldSlave != Slave) or (Sound != SoundX):
        Launch.blit(Paus.render(Messege[23], 1, Fon), (30, Screen[1]+25*3-(Screen[1]-SettY)) )



    # Плавный здвиг меню к настройкам и наоборот
    if SettY > 0 and Optional:
        SettY -= 10
        Polet = True

    elif SettY <= 0 and Polet:
        Polet = False

    if not Optional and SettY < Screen[1]:
        SettY += 10
        Polet = True
    elif SettY >= Screen[1] and Polet:
        Polet = False


    pygame.display.update()

# Сис. даные для начала главного цикла игры
if not end:
    Scr = pygame.display.set_mode((Display))#Дисплейлй

    pygame.display.set_icon(icon) #Иконка
    pygame.display.set_caption(Messege[12]) #капча

# Сама игра
while not end:
    # Сис. данные и обновленные данные
    if not end:
        if not end:
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

        Vert = Figur[Num][Pos]
        X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
        Log = [max(X), min(X)]

        Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
        Dawe = [max(Y), min(Y)]

        if OldUp:
            New = rand(0, len(Figur) - 1) #Рандомим индекс  новой фигуры
            Old = Figur[New] #Меняем индкс. старой на новый, и фигура новая ! (?)
            OldUp = False #Выкл "функцию" нов. фигуры

        Sage = [Color[0]+Ci, Color[1]+Ci, Color[2]+Ci]
        for i in range(3):
            if Sage[i] > 255:
                Sage[i] = 255

        Black = [Color[0]-Ci, Color[1]-Ci, Color[2]-Ci]
        for i in range(3):
            if Black[i] < 0:
                Black[i] = 0

        clock.tick(FPS)

        if not Exit:
            Otvet = 0

        if Sckore > MaxSckore:
            MaxSckore = Sckore

    #Регистр кнопАк
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            if not Exit:
                Exit = True
            else:
                Exit = False

        # KEYDOWN и KEYUP используем для создании эффекта зажатия
        if i.type == pygame.KEYUP: #Отжатие

            if i.key == pygame.K_i and Admin:
                print("\n< DATA > " + str(DataInd) + "\nx = " + str(x) + "; y = " + str(y) + "\n|\nOld = " + str(Old) + "\n|\nWork's Object (Python ind.) = " + str(len(Eng)-1) + "\n|\nStatic = " +  str(Static) + "\n|\nStaticX = " + str(StaticX) + "; StaticY = " + str(StaticY) + "\n")
                if DataInd == "":
                    DataInd = 0
                DataInd += 1

            if i.key == pygame.K_ESCAPE:
                if not Exit:
                    Exit = True

                else:
                    Exit = False

            # Остонавливаем "время"
            if i.key == pygame.K_SPACE and not Exit:
                if Time:
                    Time = False

                else:
                    Time = True

            if i.key == pygame.K_s:
                Start[0] = False

            if i.key == pygame.K_d:
                Start[1] = False

            if i.key == pygame.K_a:
                Start[2] = False

        if i.type == pygame.KEYDOWN: #Нажатие
            # Начало движения Вниз
            if i.key == pygame.K_s:
                Start[0] = True

            # Начало движения вПраво
            if i.key == pygame.K_d:
                # Start
                Start[1] = True

            # Начало движения вЛево
            if i.key == pygame.K_a:
                # Start
                Start[2] = True

            if i.key == pygame.K_c:
                StaticX, StaticY = x, y
                x, y = SX // 2, 0

                if not end:
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

                Vert = Figur[Num][0]
                X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
                Log = [max(X), min(X)]

                Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
                Dawe = [max(Y), min(Y)]

                Static = Vert
                StaticColor = Color

                Num = New
                Pos = rand(0, len(Figur[Num]) - 1)
                Vert = Figur[Num][Pos]

                OldUp = True
                if Shtraf == 0:
                    Shtraf = z

                #"New Color"
                Color = NewC
                NewC = NewColor()

                Vert = Figur[Num][Pos]
                X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
                Log = [max(X), min(X)]

                Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
                Dawe = [max(Y), min(Y)]

                if OldUp:
                    New = rand(0, len(Figur) - 1) #Рандомим индекс  новой фигуры
                    Old = Figur[New] #Меняем индкс. старой на новый, и фигура новая ! (?)
                    OldUp = False #Выкл "функцию" нов. фигуры


                x, y = StaticX, StaticY

            #Выбираем кнопачку в окне "выхода"
            if (i.key == pygame.K_RIGHT or i.key == pygame.K_d) and Exit:
                Otvet += 1

            elif (i.key == pygame.K_LEFT or i.key == pygame.K_a) and Exit:
                Otvet -= 1

            #Нажимаем кнопку
            if (i.key == pygame.K_SPACE or i.key == pygame.K_RETURN) and Exit:
                if Otvet == 0:
                    end = True

                elif Otvet == 1:
                    Exit = False

            # Вращение фигуры наПраво
            if (i.key == pygame.K_RIGHT or i.key == pygame.K_e) and Time and not Exit:

                Pos += 1
                if Pos > len(Figur[Num]) - 1:
                    Pos = 0

                elif Pos < 0:
                    Pos = len(Figur[Num]) - 1

                Vert = Figur[Num][Pos]

                if Vert[0] in Zone or Vert[1] in Zone or Vert[2] in Zone or Vert[3] in Zone:
                    Pos -= 1
                    if Pos > len(Figur[Num]) - 1:
                        Pos = 0

                    elif Pos < 0:
                        Pos = len(Figur[Num]) - 1

                    Vert = Figur[Num][Pos]

                    if Vert[0] in Zone or Vert[1] in Zone or Vert[2] in Zone or Vert[3] in Zone:
                        Pos -= 1
                        if Pos > len(Figur[Num]) - 1:
                            Pos = 0

                        elif Pos < 0:
                            Pos = len(Figur[Num]) - 1

                        Vert = Figur[Num][Pos]
                        X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
                        Log = [max(X), min(X)]

                        Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
                        Dawe = [max(Y), min(Y)]

            # Вращение фигуры наЛево
            if (i.key == pygame.K_LEFT or i.key == pygame.K_q) and Time and not Exit:
                Pos -= 1
                if Pos > len(Figur[Num]) - 1:
                    Pos = 0

                elif Pos < 0:
                    Pos = len(Figur[Num]) - 1

                Vert = Figur[Num][Pos]

                if Vert[0] in Zone or Vert[1] in Zone or Vert[2] in Zone or Vert[3] in Zone:
                    Pos += 1
                    if Pos > len(Figur[Num]) - 1:
                        Pos = 0

                    elif Pos < 0:
                        Pos = len(Figur[Num]) - 1

                    Vert = Figur[Num][Pos]
                    X = [ Vert[0][0], Vert[1][0], Vert[2][0], Vert[3][0] ]
                    Log = [max(X), min(X)]

                    Y = [ Vert[0][1], Vert[1][1], Vert[2][1], Vert[3][1] ]
                    Dawe = [max(Y), min(Y)]


    # Движение фигуры вПраво
    if Start[1] and Log[0] + z < SX and not ([X[0]+z, Y[0]] in Zone or [X[1]+z, Y[1]] in Zone or [X[2]+z, Y[2]] in Zone or [X[3]+z, Y[3]] in Zone) and Time and not Exit:
        Right += 1
        if Right >= 4:
            x += z
            Right = 0

    # Движение фигуры вЛево
    if Start[2] and Log[1] > 0 and not ([X[0]-z, Y[0]] in Zone or [X[1]-z, Y[1]] in Zone or [X[2]-z, Y[2]] in Zone or [X[3]-z, Y[3]] in Zone) and Time and not Exit:
        Left += 1
        if Left >= 4:
            x -= z
            Left = 0


    # Возврат X если тот зашел за парвый край
    if Log[0] >= SX:
        x -= z

    # Возврат X если тот зашел за левый край
    if Log[1] < 0:
        x += z


    # Движение фигуры вниз по Y-ку
    if Time and not Exit:
        FPSM += 1
        #Само движение вниз после 30 сек. или зажатия "s"
        if FPSM >= FPS or Start[0]:
            y += z
            FPSM = 0

    # Недаём игроку выбрать что-то болшее чем "да" или "нет" в окошке выхода
    if Otvet < 0:
        Otvet = 0

    elif Otvet > 1:
        Otvet = 1

    # Убираем заполненый слой пост. фигур на одном игрике
    for i in range(16):
        yb = Limbo(i*z)
        if yb <= SY:
            for q in range(12):
                Ind = Zone.index([q*z, yb])
                Zone.remove(Zone[Ind])
                LGBT.remove(LGBT[Ind])

            for j in range(len(Zone)):
                if Zone[j][1] < yb:
                    Zone[j][1] += z

            Sckore += rand(20, 30)
            break

    # Поставление фигур
    for i in range(4):
        if ( [Vert[i][0], Vert[i][1]] in Zone):
            # Добовления хитбоксов "мёртвых" фигур для будущего отоброжения через цикл
            Zone.append( [X[0], Y[0]-z])
            Zone.append( [X[1], Y[1]-z])
            Zone.append( [X[2], Y[2]-z])
            Zone.append( [X[3], Y[3]-z])

            # Добовление цвета поставленых фигур и реализация их как и хитбоксов
            LGBT.append(Color)
            LGBT.append(Color)
            LGBT.append(Color)
            LGBT.append(Color)

            # Вернуть новую фигуры на станд. координаты
            y = 0
            x = SX // 2

            # Рандомизация индекса, для прорисовки из списка всех фигур
            Num = New
            Pos = rand(0, len(Figur[Num]) - 1)
            Vert = Figur[Num][Pos]

            OldUp = True
            if Shtraf == 0:
                Shtraf = z

            #"New Color"
            Color = NewC
            NewC = NewColor()

            break



    # < Прорисовка >
    Scr.fill(([Fon[0]-10, Fon[0]-10, Fon[0]-10,])) #Фон   #235 or 15

    #Полоска отделяющая HUD от игровой зоны
    pygame.draw.rect(Scr, (Sage), (SX, 0, 3, SY))

    #Поствленные фигуры
    for i in range(len(Zone)):
        pygame.draw.rect(Scr, ((LGBT[i])), (Zone[i][0], Zone[i][1], z, z))

    #Весь остальной HUD
    if Sckore >= 0:
        if Tema:
            pygame.draw.rect(Scr, c["True"], (SX+9, 22, 134, 82), 3)
            pygame.draw.rect(Scr, (220, 220, 220), (SX+9+4, 22+4, 137-12, 82-9))

            pygame.draw.rect(Scr, c["True"], (SX+9, z*4, 134, z*5+(z//3)), 3)
            pygame.draw.rect(Scr, (220, 220, 220), (SX+9+4, z*4+(z//5), 137-12, z*5))

            pygame.draw.rect(Scr, c["True"], (SX+9, z*9+(z)-5, 134, z*5+25), 3)
            pygame.draw.rect(Scr, (220, 220, 220), (SX+9+4, z*9+(z), 137-12, z*5+(z//2)))

            Scr.blit(f1.render(Messege[9], 1, Color), (SX+47-Gram, 27))

            Scr.blit(f2.render(str(MaxSckore), 1, Color), (SX+15, 53) )#Действующий счёт
            Scr.blit(f2.render(str(Sckore), 1, Color), (SX+15, 77) )#Максимальный счёт

            Scr.blit(f2.render(Messege[24], 1, NewC), (SX+27, z*4+10))#Действующий счёт

        elif not Tema:
            pygame.draw.rect(Scr, c["False"], (SX+9, 22, 134, 82), 3)
            pygame.draw.rect(Scr, (10, 10, 10), (SX+9+4, 22+4, 137-12, 82-9))

            pygame.draw.rect(Scr, c["False"], (SX+9, z*4, 134, z*5+(z//3)), 3)
            pygame.draw.rect(Scr, (10, 10, 10), (SX+9+4, z*4+(z//5), 137-12, z*5))

            pygame.draw.rect(Scr, c["False"], (SX+9, z*9+(z)-5, 134, z*5+25), 3)
            pygame.draw.rect(Scr, (10, 10, 10), (SX+9+4, z*9+(z), 137-12, z*5+(z//2)))

        #Надписи
        Scr.blit(f2.render(str(MaxSckore), 1, Color), (SX+15, 53) )#Цифровой макс. счёт
        Scr.blit(f2.render(str(Sckore), 1, Color), (SX+15, 77) )#Цифровой действ. счёт

        if Static == []:
            Scr.blit(f2.render(str(Messege[25]), 1, Color), (SX+50, 320) )
            Scr.blit(Big.render(str(Messege[26]), 1, Color), (SX+60, 350) )


    #Старая фигура, новая и запасная
    for i in range(4):
        pygame.draw.rect(Scr, (NewC), (Old[0][i][0]+z*9-(Shtraf), Old[0][i][1]+z*5 +(Shtraf*2), z, z)) #Новая
        pygame.draw.rect(Scr, (Color), (Vert[i][0], Vert[i][1], z, z)) #Действующая

        if Static != []:
            pygame.draw.rect(Scr, (StaticColor), (Static[i][0]+z*8, Static[i][1]+z*13, z, z)) #Действующая

    #Окно паузы и выхода
    if Exit or not Time:
        if Tema:
            pygame.draw.rect(Scr, c["True"], (Display[0]//2 - 100, 100, 200, 120), 3)
            pygame.draw.rect(Scr, (220, 220, 220), (Display[0]//2 - 100+3, 100+3, 200-6, 120-6))

        elif not Tema:
            pygame.draw.rect(Scr, c["False"], (Display[0]//2 - 100, 100, 200, 120), 3)
            pygame.draw.rect(Scr, (10, 10, 10), (Display[0]//2 - 100+3, 100+3, 200-6, 120-6))

        if Exit:

            if Otvet == 0:
                pygame.draw.rect(Scr, Color, (Display[0]//2-62, 195, 43, 2))

            elif Otvet == 1:
                pygame.draw.rect(Scr, Color, (Display[0]//2+29, 195, 43, 2))


            Scr.blit( Paus.render(Messege[8], 1, Color) , (Display[0]//2 - 55, 106))

            if Language == "eng":
                Scr.blit( Paus.render(Messege[6], 1, Color) , (Display[0]//2 - 57, 170))
                Scr.blit( Paus.render(Messege[7], 1, Color) , (Display[0]//2 + 30, 170))

            elif Language == "rus":
                Scr.blit( Paus.render(Messege[6], 1, Color) , (Display[0]//2 - 57, 170))
                Scr.blit( Paus.render(Messege[7], 1, Color) , (Display[0]//2 + 30, 170))


        elif not Time:

            Scr.blit( Paus.render(Messege[3], 1, Color) , (Display[0]//2 - 33, 103))

            if Language == "eng":
                Scr.blit( PauseLIttle.render(Messege[4], 1, Color) , (Display[0]//2 - 75, 170))
                Scr.blit( PauseLIttle.render(Messege[5], 1, Color) , (Display[0]//2 - 97, 195))

            elif Language == "rus":
                Scr.blit( PauseLIttle.render(Messege[4], 1, Color) , (Display[0]//2 - 87, 170))
                Scr.blit( PauseLIttle.render(Messege[5], 1, Color) , (Display[0]//2 - 65, 195))

    pygame.display.update()

#Обновляем файл настроек
open("settings.py", "w")
open("settings.py", "w").write("Tema = " + Messege[Slave+5] + '\nSound = ' + str(Sound) + "\nMaxSckore = " + str(MaxSckore))
open("settings.py").close()
