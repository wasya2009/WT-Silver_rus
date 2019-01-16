

### Tonks Chitchats ###

label tonks_chit_chat:

    $ chitchated_with_tonks = True
    $ random_number = renpy.random.randint(1, 31)
    
    ### Susan Spell level 1 ###
    if whoring >= 0: #PLACEHOLDER FOR SUSANS LEVEL #JUST FOR TESTING
        if random_number == 1:
            call ton_main("Сьюзан такая милая девушка...","open","base","base","mid") 
            call ton_main("Но она действительно не очень довольна своим телом...","open","base","raised","R") 
            call ton_main("Я надеюсь, что ваши маленькие игры помогут ей немного раскрыться...","base","base","base","mid") 
        
        elif random_number == 2:
            call ton_main("Обучение было таким веселым!","open","base","raised","mid") 
            call ton_main("Это намного лучше, чем работать в Министерстве.","open","base","angry","mid") 
            call ton_main("Не могу поверить, сколько времени я провела в этой дыре...","base","base","angry","R") 

        elif random_number == 3:
            call ton_main("Сегодня на уроках я заметила еще одну милую девочку...","open","base","angry","R") 
            call ton_main("Надеюсь, она так же любит очки, как и остальные.","horny","base","raised","mid") 

        elif random_number == 4:
            call ton_main("Метаморфмаги не могут переодеться при морфинге... ","open","base","base","mid") 
            call ton_main("Однажды я изменила цвет своей кожи и сделала ее похожей на обтягивающую рубашку...","open","base","base","R") 
            call ton_main("Возможно, я работала топлесс один или два раза...","horny","base","raised","mid") 

        elif random_number == 5:
            call ton_main("Не рассказывай профессору МакГонагалл, но однажды я использовала ее внешний вид, чтобы обыскать одну из студенток...","open","base","worried","L") 
            call ton_main("Они ничего не заподозрили.","base","base","base","mid") 

        elif random_number == 6:
            call ton_main("Быть учителем имеет свои преимущества. Если бы меня в студенческие годы поймали с firewisky меня бы точно исключили.","open","base","base","mid") 
            call ton_main("Теперь я могу пить столько, сколько захочу, и даже делиться с кем нибудь.","base","base","base","mid") 

        elif random_number == 7:
            call ton_main("Мне иногда кажется, что я должна была пойти в область медицины ...","open","base","base","R") 
            call ton_main("Я могла уже получить работу мадам Помфри...","open","base","base","mid") 
            call ton_main("Может, ее спросить, нужна ли ей помощь в мое свободное время.","base","base","base","mid") 

        elif random_number == 8:
            call ton_main("Я чувствую, что у меня гораздо больше общего со студентами, чем с учителями...","open","base","base","R") 
            call ton_main("Они все такие старые...","base","base","base","up") 
            call ton_main("Мадам Хуч клевая, хотя, мы с ней выглядим одинаково... Во многих отношениях.","base","base","base","mid") 

        elif random_number == 9:
            call ton_main("Меня часто задерживали, превращаясь в префектов...","open","base","base","R") 
            call ton_main("Это стоило того, поскольку у меня был свободный доступ в ванную префектов...","open","base","base","mid") 

        elif random_number == 10:
            call ton_main("Мне пришлось оставить одного из учеников после занятий для специального обучения.","open","base","base","mid") 
            call ton_main("Как учитель темных искусств это моя работа - защищать их как от внешних угроз, так и от внутренних демонов ...","open","base","base","L") 
            call ton_main("Ей еще многому нужно научиться, но она приближается к цели.","horny","base","raised","L") 

        elif random_number == 11:
            call ton_main("Кажется, я не очень нравлюсь Снейпу...","base","base","base","R") 
            call ton_main("Сначала я думала, это потому, что я украла girding зелье в юности... (зелье выносливости)","open","base","base","L") 
            call ton_main("Но, кажется, больше, потому что он хочет мою работу...","open","base","raised","mid") 
            call ton_main("Небольшой загар, возможно, будет ему полезен.","base","base","angry","mid") 

        elif random_number == 12:
            call ton_main("Когда я впервые увидела Снейпа, я подумала, что он вампир...","open","base","base","mid") 
            call ton_main("Оказывается, он нормальный только с бледной кожей...","open","base","base","R") 
            call ton_main("Если бы он был вампиром, я на него набросилась...","horny","base","raised","R") 

        elif random_number == 13:
            call ton_main("Хорошие студенты получают от меня звездочку в углу на каждом тесте.","open","base","base","mid") 
            call ton_main("Это не обязательно означает хорошие оценки...","base","base","base","mid") 

        elif random_number == 14:
            call ton_main("Сегодня в классе произошел несчастный случай с эльфом. Не могу поверить, что их не исключили из учебной программы.","open","base","base","R") 
            call ton_main("Одна из учениц полностью уничтожила свою одежду...","open","base","base","mid") 
            call ton_main("Возможно, пока нет необходимости удалять обучение эльфов","base","base","base","down") 

        elif random_number == 15:
            call ton_main("Я не собираюсь бросаться метлой в других учителей с методами обучения, но...","open","base","base","down") 
            call ton_main("Я стараюсь не отбирать очки за простые ошибки, я была довольно неуклюжей...","open","base","worried","mid") 
            call ton_main("Я предпочитаю вознаграждать своих учеников, а не наказывать их...","base","base","base","mid") 

        elif random_number == 16:
            call ton_main("Есть тайный ход к Honeydukes прямо из моего класса...(прим. Сладкое королевство - или Тележка со сладостями)","open","base","base","mid") 
            call ton_main("Наличие свободного доступа в кондитерскую было настоящим преимуществом, для вознаграждения моих студентов.","base","base","base","R") 

        elif random_number == 17:
            call ton_main("Надеюсь, у меня будет достаточно времени, чтобы оказать положительное влияние на эту школу и на учеников...","open","base","base","L") 
            call ton_main("Если я не смогу оставить след в школе, то по крайней мере, оставлю его на учениках.","horny","base","angry","mid") 

        elif random_number == 18:
            call ton_main("Стать мракоборцем чрезвычайно сложно, и в этой работе почти полностью доминируют мужчины...","open","base","worried","R")            
            call ton_main("Думаю, я сделала правильный выбор, став преподавателем.","base","base","base","mid") 

        elif random_number == 19:
            call ton_main("Большинство моих способностей основаны на эмоциях...","open","base","base","mid") 
            call ton_main("Мои волосы могут покраснеть, когда я расстроена или зла...","open","base","base","mid") 
            call ton_main("Никому не говори, но мой натуральный цвет волос более темный...","open","base","base","R") 
            call ton_main("Люди думают, что он розовый, но это потому, что я все время возбуждена.","base","base","base","down") 

        elif random_number == 20:
            call ton_main("Моя мать была чистокровной, но была сожжена семейством Black после женитьбы на маглорожденном...","open","base","base","down") 
            call ton_main("Некоторые люди не понимают, но я думаю, мы должны иметь возможность любить, тех, кого захотим...","open","base","base","mid") 

        elif random_number == 21:
            call ton_main("Никому не говори, но, вероятно, я потратила целое состояние на Blemish Blitzer в свое время обучения в Хогвартсе...(Пятновыводитель Блитзера)","open","base","base","L") 
            call ton_main("Мои родители думали, что я такая неуклюжая транжира, но большую часть денег что они прислали, было потрачено на косметику и средства для волос...","open","base","base","R") 
  
        elif random_number == 22:
            call ton_main("Я преследовала мальчиков в школе, потому что все остальные девочки...","open","base","raised","down") 
            call ton_main("В тайне я просто хотела, чтобы они преследовали меня...","open","base","base","L") 

        elif random_number == 23:
            call ton_main("Я многому научилась под руководством Аластора Грюм,...","open","base","base","mid") 
            call ton_main("Никогда не думала, что сама стану учителем....","open","base","raised","down") 
            call ton_main("Хотя мои методы немного отличаются от его...","base","base","base","mid") 

        elif random_number == 24:
            call ton_main("Есть слухи, что он создал возрастную линию в своем кабинете, чтобы держать студентов подальше от личного тайника...","open","base","base","R") 
            call ton_main("Мне не помешают некоторые зелья, хотя... Не то, чтобы они мне нужны...","open","base","base","R") 
            call ton_main("Но, может быть, я найду девушку, которая не против выпить с ним и повеселиться.","horny","base","raised","R") 

        elif random_number == 25:
            call ton_main("Мне не нравится, когда меня называют Нимфадора... Я Тонкс!","open","base","angry","mid") 
            call ton_main("В прошлый раз кто-то просил меня использовать обаяние расширения на одном из его колец.","open","base","angry","R") 
            call ton_main("Откуда мне было знать, что это не для его пальца...","base","base","base","up") 

        elif random_number == 26:
            call ton_main("Мое любимое животное-волк...","base","base","base","L") 
            call ton_main("их звериная натура меня возбуждает...","base","base","base","mid") 
            call ton_main("Возможно, в другой жизни...","base","base","raised","down") 

        elif random_number == 27:
            call ton_main("Ученики рассмеялись, когда я случайно споткнулась на последнем уроке...","open","base","base","R") 
            call ton_main("Они не догадываются, что мне открылся прекрасный вид на их...","horny","base","raised","mid") 

        elif random_number == 28:
            call ton_main("Одна из девушек превратила боггарта в студента, указывающего на нее пальцем и смеющегося над ней...","open","base","base","R") 
            call ton_main("Я собираюсь научить ее не стыдиться своего тела.","base","base","base","mid") 

        elif random_number == 29:
            call ton_main("Я метаморф. Я могу изменять свою внешность по желанию...","open","base","base","mid") 
            call ton_main("Это делает шпионаж за другими учителями и студентами намного проще...","open","base","raised","mid") 

        elif random_number == 30:
            call ton_main("Я могу изменить форму и длину своего языка так, как захочу.","open","base","base","mid") 
            call ton_main("Вообразите возможности...","tongue_wide","base","raised","up") 

        elif random_number == 31:
            call ton_main("Сегодня я рассказывала студентам о Tanglepest...","open","base","base","mid") 
            call ton_main("Мерзкое существо, которое тянется к обуви...","open","base","base","R") 
            call ton_main("На самом деле его не существует, я просто хотела, чтобы студенты показали мне свои ноги.","horny","base","base","mid") 
            
            
    return
