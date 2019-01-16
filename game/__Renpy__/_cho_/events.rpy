label cho_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ changeCho(1, 1, 2, 1)
    menu:
        "-Приватные услуги-":
            menu:
                "-Разденься-":
                    jump cho_favor_1
                "-Играть с ее булочками-" if cho_whoring == 1:
                    jump cho_favor_2
                "-Попросить сделать минет-":
                    jump cho_favor_3
                "-Неважно-":
                    jump cho_menu
        "-Публичные услуги-":
            "Будет в следующей версии, когда-нибудь."
            jump cho_menu
        "-Отпустить ее-":
            hide screen cho_chang
            with d3
            jump day_main_menu

###CHO END EVENT





###ONE OFF EVENTS###

label cho_intro:
    $ cho_known = True

    call bld 
    m "Мисс Грейнджер. Как бы ты сегодня хотела заработать очки?"
    call her_main("Что я должна сделать?","soft","baseL",cheeks="blush") 
    m "Ничего. Просто стой."
    call her_main("Я вам не верю.","annoyed","angryL",cheeks="blush") 
    m "Ну, конечно. Я собираюсь вплотную занятся твоей попкой."
    call her_main("Вы же не собираетесь снова меня отшлепать?","annoyed","frown",cheeks="blush") 
    m "Тебе не нравится, когда я шлепаю тебя по попке?"
    call her_main("Это... дело не в этом. Просто вы слишком громко это делаете.","annoyed","baseL") 
    call her_main("Что бы вы сделали, если бы кто-нибудь проходил мимо, пока вы... пока я 'здесь просто стою'? Они могут нас услышать.","annoyed","angryL",cheeks="blush") 
    m "Что? Чушь. Эти стены из плотного материала. Они должны быть волшебниками, чтобы что-то заметить."
    call her_main("Это бессмыслица!","soft","wide") 
    m "Тебе нужны очки или нет?"
    call her_main("Да, пожалуйста.","angry","worriedCl",cheeks="blush") 

    hide screen bld1
    call her_walk("mid","desk",3, redux_pause = 2) 
    call blkfade 

    call her_chibi("hide") 
    hide screen genie
    show screen groping_02
    pause.5

    call hide_blkfade 
    call ctc 

    show screen blktone
    call her_main("...","annoyed","baseL", xpos="mid",ypos="base") 

    menu:
        "-Шлепнуть ее по заднице-":
            pass
        "-Кого ты обманываешь, получай!-":
            pass

    call slap_her 

    call her_main("Профессор!","open","wide") 

    menu:
        "-Еще раз шлепнуть!-":
            call slap_her 

            call her_main("Профессор!","angry","angry",cheeks="blush") 

            call slap_her 

            call her_main("Не-","angry","angry",cheeks="blush") 

            call slap_her 

            call her_main("Так-","angry","worriedCl",cheeks="blush") 

            call slap_her 

            call her_main("Сильно!","angry","worriedCl",cheeks="blush") 
            m "Ты что-то сказала, мисс Грейнджер?"
            call her_main("Я сказала, не так сильно.","angry","angry",cheeks="blush",tears="down") 
            call her_main("Кто-нибудь может услышать!","scream","angry",cheeks="blush",tears="down") 
            m "Мисс Грейнджер, пожалуйста. Нет необходимости кричать."

            menu:
                "-Продолжать шлепать ее по заднице-":

                    call slap_her 
                    call slap_her 
                    call slap_her 
                    call her_main("Профессор!","scream","worriedCl",cheeks="blush",tears="messy") 
                "-Потрогать ягодички-":
                    "Ты осторожно скользишь руками по ногам Гермионы, залазя под юбку."
                    call her_main("...........","angry","worried",cheeks="blush",tears="down") 
                    "Твои руки нежно гладят ее. Ты чувствуешь тепло от ее задницы."
                    call her_main("......","angry","worriedCl",cheeks="blush",tears="crying_blink") 
                    "Ты чувствуешь мурашки, которые проходят по ее коже."
                    call her_main("Профессор?","angry","worried",cheeks="blush",tears="down") 
                    "Ты замечаешь, что ее дыхание стало реже."
                    call her_main("Мы можем остановиться, пожалуйста?","disgust","down_raised",cheeks="blush") 
                    m "Тебе не нравится?"
                    call her_main(".......Да.","angry","worriedCl",cheeks="blush",tears="soft_blink") 
                    call her_main("Я имею в виду, нет.","disgust","wink",cheeks="blush",tears="soft_blink") 

                    menu:
                        "-Перестать-":
                            pass
                        "-Продолжить играть с ее попкой-":
                            "Ты игнорируешь Гермиону и нежно скользишь руками в ее трусики."
                            "Твоя левая рука нежно оттягивает ее ягодицу в сторону, обнажая гладкую, чистую дырочку."
                            "Ты вытягиваешь средний палец и нежно касаешься ее дырочки."
                            call her_main("!","scream","wide",cheeks="blush") 
                            call her_main("Проф-","scream","wideL",cheeks="blush") 
                            m "Тшш. Не слишком громко, девочка. Не хотел бы никого тревожить в коридоре."
                            "Ты прижимаешь палец к колечку ануса и начинаешь его массировать, круговыми движениями."
                            call her_main("......","mad","wide",cheeks="blush") 
                            call her_main("...","disgust","wink",cheeks="blush",tears="soft_blink") 
                            "Ты чувствуешь, как задница Гермионы начинает дергаться."
                            call her_main("Я-я думаю, мне пор-","angry","worriedCl",cheeks="blush") 
                            "Ты замечаешь, что ее анус расслабляется."

        "-Вставить палец ей в анус-":
            pass

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with fade
    pause.5

    $ days_since_cho = 0
    $ renpy.play('sounds/door.mp3')
    $ cc_xpos = 550
    #call cho_main("Professor Dumbledore! I'm sorry for rushing in without knocking, but I finally have proof the Slytherin team is cheating! Draco and his goons are-", 3, 2, 3, 4)
    call cho_main("Профессор Дамблдор! Извините, что врываюсь без стука, но я наконец-то--", 3, 2, 3, 4) 

    $ renpy.play('sounds/scratch.wav')
    with hpunch

    call cho_main("", 4, 2, 4, 3) 
    pause.2

    hide screen groping_02
    show screen no_groping_02

    call her_main("...","angry","wide",cheeks="blush") 
    call her_main(".............","soft","ahegao",cheeks="blush") 
    call cho_main("Эм...", 4, 2, 4, 2) 

    call her_main("Это не то, что ты думаешь!","shock","worriedCl",cheeks="blush") 
    call cho_main("Лживая сука!", 2, 2, 1, 3) 
    call cho_main("Движение За права мужчин через задницу!", 2, 2, 2, 4) 
    call her_main("...","shock","worriedCl",cheeks="blush",emote="01") 
    call her_main("{size=-7}(Я хочу умереть!){/size}","disgust","down_raised",cheeks="blush") 
    call her_main("Он просто массировал потянутые мышцы в моей... в моей... ноге!","open","worriedCl",cheeks="blush") 
    call cho_main("Лгунья!", 1, 2, 1, 2) 
    call her_main("Ты... ты...","annoyed","frown",cheeks="blush") 
    call her_main("Страхолюдина с плоской грудью!","scream","angryL",cheeks="blush") 
    call cho_main("Двуличная корова!", 5, 2, 1, 3) 
    call her_main("Троешница!","scream","angryL",cheeks="blush") 

    menu:
        "-Сказать им заткнуться-":
            m "Стунденты! О Великие пески! Успокойтесь! Существует вполне разумное объяснение!"
            call her_main("...","annoyed","frown",cheeks="blush") 
            call cho_main("...", 2, 2, 1, 2) 
            call cho_main("....Ну?", 2, 2, 1, 3) 
            m "Мисс Грейнджер просто помогала мне убраться в кабинете, когда потянула мышцу на ноге. Это довольно болезненно. Вот почему она так взволнована."
            call cho_main("...", 5, 2, 2, 2) 
            call cho_main("Я в это не верю!", 5, 2, 2, 3) 
            hide screen cho_chang
            with d3
            show screen bld1
            with d3
            $ renpy.play('sounds/door.mp3')
            call her_main("Грязный старикашка!","scream","angryL",cheeks="blush") 
            m "Теперь смотрите сюда, юная леди. Не ошибайся, я способен только на простые трю-"
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            m "Успокойся, девоч-"
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white

            call her_main("Я больше никогда не продам вам услугу!","angry","angry",cheeks="blush",tears="down") 
            $ mad += 15
    
        "-Не вмешиваться-":
            call her_main("Ничего! Убирайся!","angry","worriedCl",cheeks="blush") 
            call cho_main("Шлюха!", 5, 2, 1, 3) 
            with d3
            hide screen cho_chang
            show screen bld1
            $ renpy.play('sounds/door.mp3')
            call her_main("Не могу поверить, что это случилось.","angry","worriedCl",cheeks="blush") 
            call her_main("Какой человек просто врывается в кабинет директора без стука!","angry","angryCl",cheeks="blush") 
            call her_main("Это была ваша вина!","annoyed","frown",cheeks="blush") 
            $ mad += 5

    hide screen hermione_main
    hide screen bld1
    hide screen blktone
    hide screen no_groping_02
    show screen genie
    call her_chibi("stand","desk","base") 
    with fade

    call her_walk("desk","leave",1.5,action="run") 

    m "Сучки..."

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu   
    

label hermione_cho:
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "-Войдите-":
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            call her_chibi("stand","desk","base") 
            pause.2

            show screen bld1
            call her_main("Сэр, я просто хотела...","annoyed","baseL") 
            call her_main("...к...","annoyed","angryL",cheeks="blush") 
            m "О Великие пескам пустыни, девочка! Что?!"
            call her_main("Я хотела извиниться за то, что произошло.","open","baseL",cheeks="blush") 
            m "Ты имеешь ввиду инцидент с той девочкой?"

            menu:
                "-Мисс Чанг-":
                    m "Мисс Чанг. Да?"
                    call her_main("Да, сэр.","annoyed","baseL") 
                    call her_main("Она всегда пытается конкурировать со мной.","open","baseL",cheeks="blush") 
                    m "Ну, будучи девочками, это естественно."
                    call her_main("Да, сэр. Но она заходит слишком далеко.","annoyed","baseL") 
                "-Мисс Член-":
                    m "Мисс Член, не так ли?"
                    call her_main("Чанг, сэр.","annoyed","baseL") 
                    m "Конечно."

            call her_main("Я просто хотела сказать вам, что я...","open","baseL",cheeks="blush") 
            call her_main("Я все объяснила Чоу.","angry","worriedCl",cheeks="blush",tears="soft_blink") 
            call her_main("Это было так неловко.","angry","worriedCl",cheeks="blush") 
            m "И?"
            call her_main("Так что все в порядке.","base","base",cheeks="blush") 
            call her_main("Я сказала ей, что вы дали мне очки за уборку вашего кабинета.","base","worriedCl",cheeks="blush") 
            call her_main("Очень умно, да?","base","glance",cheeks="blush") 
            m "Да. Очень, мисс Грейнджер. Полагаю, мисс...."

            menu:
                "-Мисс Чанг-":
                    m "Полагаю, с мисс Чанг не будет проблем?"
                    call her_main("Нет!","base","worriedCl",cheeks="blush") 
                    m "Великолепно."
                    call her_main("Что ж, мне нужно идти на занятия. Доброго дня, сэр.","annoyed","baseL") 
                    m "Конечно, мисс Грейнджер."

                "-Мисс Чика-":
                    m "Полагаю, тогда с ней не будет проблем?"
                    m "С мисс Чикой?"
                    call her_main("Чанг, сэр.","open","baseL",cheeks="blush") 
                    m "Член?"
                    call her_main("Ее имя Чоу Чанг!","annoyed","angryL",cheeks="blush") 
                    m "Чика, Член, Чоу Чанг?!"
                    m "Это расизм!"
                    call her_main("Что?","mad","wide",cheeks="blush") 
                    m "А разве у тебя нет занятий?"

            hide screen hermione_main
            with d3

            call her_walk("desk","leave",2.5) 

        "-Не сейчас, я занят-":
                $ days_since_cho = 0
                if daytime:
                    $ hermione_takes_classes = True
                    jump day_main_menu
                else:
                    $ hermione_sleeping = True
                    jump night_main_menu   
            
label end_cho_event:
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    hide screen cho_chang
    show screen genie
    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with fade
    
    if daytime:
        ## set cho unavailable
        jump day_main_menu
    else:
        ## set cho unavailable
        jump night_main_menu   
        
label cho_favor_1:
    menu:
         "-Разденься-":
            pass
         "-Неважно-":
             jump cho_menu
    
    if cho_whoring == 0:
         jump cho_favor_1_1
    if cho_whoring >= 1:
        jump cho_favor_1_2


label cho_intro_2:
$ renpy.play ('sounds/knocking.mp3')
menu:
    "-Это ты, мисс Грейнджер?-":
        "Нет, это я. Чоу Чанг."
        m "Aх, мисс Член."
        call cho_main("Чанг!", 5, 2, 1, 2) 
        m "Что?"
        call cho_main("Меня зовут Чанг, сэр!", 5, 2, 1, 3) 
        m "Aх, что ж, заходи уже, мисс Чика."
        jump cho2begin
    "-Заходи.-":
        jump cho2begin
    "-Я занят.-":
        $ days_since_cho = 3
        jump end_cho_event

label cho2begin:
    #enable her character for future reference
    $ cho_met = True
    $ cho_mad = 0
    $ cho_whoring = 0
    $ renpy.play ('sounds/door.mp3')
    $ changeCho(3, 3, 3, 4)
    ">Чоу входит и стоит посреди комнаты."
    m "Расскажи, что это было?"
    call cho_main("Я... эм...", 1, 3, 2, 2) 
    call cho_main("Я знаю, что вы покупаете услуги у Гермионы.", 2, 3, 1, 2) 
    m "И почему ты так думаешь?"
    call cho_main("Потому что я видела вас!", 1, 2, 1, 2) 
    m "Oх, верно."
    m "Ну, есть что-нибудь еще? Или ты просто пришла сообщить мне о том, что я уже знаю."
    call cho_main("Что ж......", 2, 3, 2, 5) 
    m "Что? Говори, девочка."
    call cho_main("Сэр, я хочу, чтобы вы тоже покупали у меня услуги!", 2, 3, 1, 1) 
    m "У тебя? Что случилось с тем, что бы быть выше этих 'неприятных' бизнес услуг, и не нужно быть 'грязной', чтоб выиграть кубок?"
    call cho_main("Команда Слизерина жульничает, сэр.", 6, 2, 5, 9) 
    m "Это что-то меняет?"
    call cho_main("Это не имеет значения...", 6, 2, 6, 7) 
    call cho_main("Я буду хорошо стараться!", 6, 2, 5, 7) 
    call cho_main("Я не могу победить их по-другому.", 5, 2, 1, 7) 
    $ changeCho(5, 2, 1, 9)
    m "Понятно."
    m "Но... зачем продавать свои услуги именно мне?"
    m "Если ты подозреваешь, что мисс Грейнджер продает мне услуги, а ты разве не заработаешь очки у менее 'занятого' профессора?"
    call cho_main("Я... эм... Я посмотрела, но единственный другой профессор, еще торгующий услугами - Снейп.", 6, 3, 6, 9) 
    call cho_main("И я не буду продавать Слизеринской мрази свои услуги!", 6, 2, 5, 10) 
    menu:
        "-Мне кажется, что это неуместно.-":
            m "Я не думаю, что это будет уместно. Я уверен, ты понимаешь."
            call cho_main("Что?!", 4, 2, 4, 7) 
            m "Я просто не могу покупать у тебя услуги."
            m "Ты должна уйти."
            call cho_main("Что?", 6, 2, 5, 4) 
            m "Ты должна... уйти"
            call cho_main("Не могу поверить, что вы предпочли эту глупую Гриффиндорку! ", 2, 2, 1, 3) 
            call cho_main("Вы отвратительный человек. Я собираюсь связаться с министерством магии и послушать, что они думают о своем любимом волшебнике, действующем как... как...", 2, 2, 2, 4) 
            call cho_main("ЖУЛИК!", 2, 2, 1, 9) 
            #Cho storms out
            pause 
            hide screen cho_chang
            $ renpy.play ('sounds/door.mp3')
            m "Болтающиеся яички старого Крокуса! Надеюсь, это не всплывет снова."
            jump cho2end
            
        "-Хорошо, мисс Чанг. Я позволю тебе продать мне услуги.-":
            m "Хорошо мисс Чанг. Я позволю тебе продать мне услуги."
            call cho_main("Правда?", 1, 1, 1, 1) 
            m "Да. Теперь вытри глаза."
            call cho_main("Простите, профессор Дамблдор, сэр.", 2, 3, 2, 7) 
            m "..."
            call cho_main("...", 1, 1, 2, 5) 
            m "..."
            call cho_main("Эм?...", 1, 3, 1, 7) 
            m "Да?"
            call cho_main("Что я должна сделать?", 1, 3, 2, 7) 
            menu:
                "-\"Сними жилет\"-":
                    #Cho removes her vest
                    call cho_main("Что? Не хотите сначала немного поговорить?", 4, 3, 4, 7) 
                    m "Нет..."
                    m "Кроме того, мисс Грейнджер? более чем счастлива показать мне сис-"
                    call cho_main("Ладно!", 1, 2, 2, 9) 
                    ">Чоу быстро стаскивает с себя жилет."
                    $ cc_wear_vest = False
                    m "Хорошо..."
                    menu:
                        "-\"А теперь сними рубашку.\"-":
                            call cho_main("Хорошо...", 1, 3, 2, 5) 
                            ">Чоу быстро снимает галстук, прежде чем начать расстегивать рубашку."
                            ">Ты видишь, что она еще не опытна, но Чоу пытается сделать это красиво."
                            #Cho removes her shirt
                            $ cc_wear_top = False
                            $ cc_wear_acc = False
                            call cho_main("Простите, насчет этого.", 1, 3, 1, 7) 
                            menu:
                                "-\"Не плохо\"-":
                                    call cho_main("Спасибо.", 1, 3, 2, 1) 
                                    m "Теперь сними юбку..."
                                    call cho_main("Хорошо...", 1, 3, 1, 7) 
                                    ">Чоу делает глубокий вдох, а затем быстро снимает юбку."
                                    $ cc_wear_skirt = False
                                    jump cho2keepgoing
                                "-\"Теперь юбка\"-":
                                    call cho_main("Хорошо...", 1, 3, 1, 7) 
                                    ">Чоу делает глубокий вдох, а затем быстро снимет юбку."
                                    $ cc_wear_skirt = False
                                    jump cho2keepgoing
                        "-\"А теперь сними юбку\"-":
                                call cho_main("Хорошо...", 1, 3, 1, 7) 
                                ">Чоу делает глубокий вдох, а затем быстро снимает юбку."
                                #Cho removes her skirt
                                $ cc_wear_skirt = False
                                menu:
                                    "-Не плохо-":
                                        call cho_main("Спасибо.", 1, 3, 2, 1) 
                                        m "Теперь сними рубашку...."
                                        call cho_main("Хорошо...", 1, 3, 2, 5) 
                                        ">Чоу быстро снимает галстук, прежде чем начать расстегивать рубашку."
                                        ">Ты видишь, что она еще не опытна, но Чоу пытается сделать это красиво."
                                        jump cho2keepgoing
                                    "-Теперь твоя рубашка-":
                                        #Cho is now wearing only her underwear
                                        call cho_main("Хорошо...", 1, 3, 2, 5) 
                                        ">Чоу быстро снимает галстук, прежде чем начать расстегивать рубашку."
                                        ">Ты видишь, что она еще не опытна, но Чоу пытается сделать это красиво."
                                        label cho2keepgoing:
                                        call cho_main("Эм, я забыла спросить, сколько очков я получу за это?", 2, 3, 1, 7) 
                                        m "Ты ужасный переговорщик."
                                        call cho_main("Я знаю.", 2, 3, 2, 1) 
                                        call cho_main("сколько вы платите Гермионе?", 2, 3, 1, 1) 
                                        menu:
                                            "-5 очков-":
                                                call cho_main("Всего пять?", 6, 1, 5, 9) 
                                                call cho_main("Я уверена, что она выглядит как корова по сравнению со мной.", 6, 1, 6, 1) 
                                                pass
                                            "-15 очков-":
                                                call cho_main("{size=-3}(Это хорошая цена?){/size}", 6, 1, 6, 5) 
                                                pass
                                            "-30 очков-":
                                                call cho_main("Так много, да?", 1, 1, 2, 7) 
                                                pass
                                            "-100 очков-":
                                                call cho_main("100?", 4, 3, 4, 3) 
                                                call cho_main("Но она такая...", 1, 3, 2, 2) 
                                                call cho_main("У нее даже не получается!", 1, 2, 1, 2) 
                                                pass
                                        call cho_main("Как вы думаете, сколько стоит мое тело?", 1, 1, 1, 1) 
                                        label cho2howmuch:
                                        menu:
                                            "-5 очков-":
                                                call cho_main("Всего пять?", 4, 2, 4, 3) 
                                                call cho_main("Пять жалких очков!", 6, 2, 5, 4) 
                                                menu:
                                                    "-Бери или уходи-":
                                                        call cho_main("Вы серьезно?", 6, 2, 5, 4) 
                                                        call cho_main("Я просыпаюсь каждое утро перед рассветом и тренируюсь в квиддич до восхода солнца!", 6, 2, 5, 7) 
                                                        call cho_main("Я поддерживаю свое тело в абсолютном пике человеческого и волшебного тонуса!", 6, 2, 6, 7) 
                                                        call cho_main("Это стоит намного больше, чем 5 очков.", 6, 2, 5, 9) 
                                                        ">Чоу раздраженно собирает свою одежду."
                                                        call cho_main("Не могу поверить, я думала, что заработаю больше.", 6, 2, 5, 4) 
                                                        hide screen cho_chang
                                                        $ cho_mad +=10
                                                        #Cho storms out
                                                        $ renpy.play ('sounds/door.mp3')
                                                        m "..."
                                                        jump cho2end
                                                    "-Я сказал пять? Я имел в виду больше-":
                                                        $ changeCho(6, 2, 5, 4)
                                                        $ cho_mad +=5
                                                        jump cho2howmuch
                                            "-15 очков-":
                                                call cho_main("(Это хорошая цена?)", 6, 3, 6, 5) 
                                                call cho_main("Думаю, этого достаточно...", 6, 3, 5, 7) 
                                                $ cho_points = 15
                                            "-30 очков-":
                                                call cho_main("Хорошо.", 1, 1, 1, 5) 
                                                call cho_main("Договорились.", 1, 1, 2, 1) 
                                                $ cho_points = 30
                                            "-100 очков-":
                                                call cho_main("100?", 4, 1, 4, 1) 
                                                call cho_main("Серьезно?", 4, 1, 4, 7) 
                                                call cho_main("Это ооочень много, профессор.", 1, 1, 2, 5) 
                                                call cho_main("Хотите, я сниму остальное?", 2, 3, 2, 6) 
                                                $ cho_points = 100
                                        $ changeCho(2, 1, 2, 5)
                                        m "Мисс Чанг, остальное, пожалуйста."
                                        call cho_main("Конечно, сэр.", 1, 1, 1, 5) 
                                        ">Чоу начинает медленно снимать бюстгальтер.{p}Ее маленькие груди едва двигаются, когда она низко опускается и стягивает свои трусики вниз по подтянутым ножкам."
                                        ">Закончив, она гордо откидывается назад и нервно улыбается."
                                        $ cc_wear_bra = False
                                        call cho_main("Я уверена, мое подтянутое тело выглядит лучше чем у Гермионы.", 6, 1, 6, 5) 
                                        menu:
                                            "-Да, она корова-":
                                                m  "Тело мисс Грейнджер ничто по сравнению с твоим."
                                                call cho_main("Правда?", 4, 1, 4, 1) 
                                                m  "Ее сиськи слишком сильно провисают, а ее толстые бедра отвратительны."
                                                call cho_main("Она действительно...", 6, 2, 6, 5) 
                                                call cho_main("...глупая...", 6, 2, 6, 4) 
                                                call cho_main("...жирная...", 6, 2, 6, 10) 
                                                call cho_main("...корова, не так ли?", 6, 2, 5, 6) 
                                                ">Со своего стола ты видешь, как рука Чоу опускается ниже. Она явно намокла."
                                            "-Я не могу выбрать-":
                                                m  "Вы оба горячие."
                                                call cho_main("Я думаю, вы правы.", 6, 2, 6, 9) 
                                            "-Нет, ты проиграла-":
                                                m "Боюсь, мисс Грейнджер просто более сексуальна. Ревность совсем не подобает молодой ведьме."
                                                call cho_main("Что?", 6, 2, 5, 7) 
                                                call cho_main("Но она даже не отрабатывает, сэр.", 6, 2, 6, 10) 
                                                $ cho_mad +=5
                                        menu:
                                            "-Достать член и начать дрочить под столом-":
                                                ">Ты откидываешься на спинку стула и высовываешь свой член из мантии."
                                                hide screen blktone8
                                                with d3
                                                hide screen genie
                                                show screen genie_jerking_off
                                                with d3
                                                call cho_main("Вы...", 6, 3, 5, 1) 
                                                ">Голос Чоу немного тихий и хрипловатый. Она кажется почти... возбужденной."
                                                ">Ты обхватываешь рукой свой толстый член."
                                                call cho_main("Профессор...", 6, 1, 5, 6) 
                                                menu:
                                                    "-Начать дрочить-":
                                                        ">Твои глаза бешено разглядывают тело Чоу."
                                                        ">Ты откидываешься на спинку стула и начинаешь дрочить."
                                                        call cho_main("...", 6, 1, 6, 6) 
                                                        ">Невинные глаза Чоу прилипли к твоему толстому члену."
                                                        call cho_main("...", 6, 1, 5, 6) 
                                                        ">Она в ступоре от твоих действий."
                                                        ">Наконец, ваши глаза встречаются, и она краснеет."
                                                        call cho_main("Я-я никогда не видела такого.", 6, 3, 5, 7) 
                                                        call cho_main("Всегда ли они такие... БОЛЬШИЕ?", 6, 3, 5, 1) 
                                                        menu:
                                                            "-Заткнуть ее-":
                                                                m "Тише, девочка!"
                                                                call cho_main("...", 6, 3, 6, 5) 
                                                                ">По твоему приказу девочка закрывает рот и позволяет тебе спокойно продолжать."
                                                                ">Пока ты продолжаешь гладить свой член замечаешь, как Чоу начала переминатся с ноги на ногу.{w=0.4}Ее бедра сжимаются с твоим ритмом."
                                                                ">Ты начинаешь дрочить еще быстрее"
                                                                call cho_main("Я-я думаю я... Я пойду...", 4, 3, 4, 5) 
                                                                ">Бедра Чоу сжимаются все быстрее и быстрее."
                                                                call cho_main("Кончаю!......", 4, 3, 4, 6) 
                                                                ">Внезапно, ее тело полностью напрягается  и мышцы живота сокращаются в такт с нахлынувшим оргазмом."
                                                                ">Ноги Чоу сильно дрожат, она не может устоять и падает."
                                                            "-Подыграть-":
                                                                m  "Только когда я рядом с такими студентками, как ты, мисс Чанг."
                                                                $ changeCho(6, 3, 6, 5)
                                                                ">Пока ты продолжаешь гладить свой член замечаешь, как Чоу начала переминатся с ноги на ногу.{w=.04} Ее бедра сжимаются с твоим ритмом."
                                                                hide screen cho_chang
                                                                m "Мисс Чанг, что ты делаешь?"
                                                                call cho_main("Я-я п-просто... Я просто...", 4, 3, 4, 5) 
                                                                ">Бедра Чоу сжимаются все быстрее и быстрее."
                                                                call cho_main("Кончаю!......", 4, 3, 4, 6) 
                                                                ">Внезапно, ее тело полностью напрягается и мышцы живота сокращаются в такт с нахлынувшим оргазмом."
                                                                ">Ноги Чоу сильно дрожат, она не может устоять и падает."
                                                        "Ты полностью обкончал свой стол."
                                                        $ cc_ypos = 150
                                                        with d3
                                                        hide screen bld1
                                                        with d3
                                                        show screen genie_jerking_sperm
                                                        with d3
                                                        "О Великие пески!"
                                                        "Твой стол полностью покрыт спермой. В кабинете слышно только твое медленное, тяжелое дыхание и *кап* *кап* твоей спермы, стекающей со стола."
                                                        show screen genie_jerking_sperm_02
                                                        with d3
                                                        "Чоу с пола смотрит на тебя."
                                                        call cho_main("...", 6, 3, 6, 5) 
                                                        call cho_main("Не могу поверить, что я это сделала.", 6, 3, 5, 7) 
                                                        call cho_main("Могу я получить очки?!", 1, 1, 2, 1) 
                                                        ">Чоу вскакивает на ноги."
                                                        $ cc_ypos = 0
                                                        #go to [End Points]
                                                    "-Убрать его-":
                                                        ">Ты тактично подворачиваешь свой все еще пульсирующий эрегированный член назад в свою мантию."
                                                        #go to [End Points]
                                            "-Не надо.-":
                                                ">Ты решаешь не вестись на свои инстинкты."
                                                #go to [End Points]
                "-\"Соси мой член\"-":
                    m "Я бы хотел, чтобы ты мне отсосала, мисс Чанг."
                    call cho_main("Это сликом. Что с вами не так?", 4, 2, 4, 3) 
                    call cho_main("Вы никогда не слышали о развитии характера!", 6, 2, 6, 4) 
                    call cho_main("Вы должны начинать с малого!", 6, 2, 5, 4) 
                    #Cho storms out
                    $ renpy.play ('sounds/door.mp3')
                    m "Болтающиеся яички старого Крокуса! Надеюсь, это не укусит меня за лампу.."
                    jump end_cho_event
                    #Go to [END]
                "-\"Ты пробовала задницу на вкус, мисс Член?\"-":
                            m "Ты пробовала задницу на вкус, мисс Член?"
                            call cho_main("Повторяю в последний раз.", 4, 2, 4, 3) 
                            call cho_main("Мое имя не Член, меня зовут Чоу Чанг!", 4, 2, 4, 4) 
                            call cho_main("...", 6, 2, 5, 9) 
                            call cho_main("..", 6, 2, 5, 4) 
                            call cho_main(".", 6, 2, 6, 9) 
                            call cho_main("Профессор.", 6, 2, 5, 7) 
                            call cho_main("Вы отвратителены!", 6, 2, 5, 10) 
                            $ cho_mad += 10
                            $ renpy.play ('sounds/door.mp3')
                            g9 "Черт. Я должен был знать, что только интернет-извращенцы и дерьмовые писатели разрушают хорошее порно с assplay."
                            jump end_cho_event
                            #Go to [End]
    show screen genie
    hide screen genie_jerking_off
    with d3
    m "Отлично, мисс Чанг."
    m "[cho_points] очков Гриффиндору!"
    call cho_main("Я из Когтеврана, сэр.", 6, 2, 5, 9) 
    m "Верно, а что я сказал?"
    m "[cho_points] очков Когтеврану!"
    $ ravenclaw += cho_points
    call cho_main("Спасибо, сэр...", 6, 2, 6, 9) 
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Чоу быстро одевается."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump end_cho_event

label cho2end:
    hide screen cho_chang
    $ days_since_cho = 3
    $ cho_met = False
    jump end_cho_event

######FAVORS ARE FROM HERE ON######


###Favor 1###
label cho_favor_1_1:
    $ cho_points = 15
    if cho_whoring < 1:
        $ cho_whoring += 1

    m "Мисс Чанг, не хочешь легко заработать 15 очков?"
    call cho_main("Что я должна делать?", 6, 3, 5, 7) 
    m "Могу я снова увидеть твое тело?"
    call cho_main("Вы хотите, чтобы я разделась, сэр?", 1, 3, 2, 9) 
    m "Конечно."
    m "Если тебе не интересно, уверен, Гермиона будет не против..."
    call cho_main("!!!", 4, 3, 4, 9) 
    call cho_main("Я разденусь.", 1, 3, 2, 5) 
    menu:
        "-Быть агрессивным-":
            "Несмотря на ее кажущуюся уверенность, руки Чоу дрожат, когда она начинает снимать топ."
            m "Смирись с этим, девочка."
            call cho_main("Да, сэр!", 1, 3, 2, 7) 
            $ cc_wear_top = False
            $ cc_wear_vest = False
            $ cc_wear_acc = False 
            "Чоу скрипит зубами и снимает свой топ одним быстрым движением."
            m "Так лучше. Теперь черед низа."
            call cho_main("Да, сэр.", 1, 3, 1, 9) 
            $ cc_wear_skirt = False 
            "Чоу расстегивает юбку своими нежными пальцами и стягивает ее вниз."
            call cho_main("(Очки... много очков...)", 3, 3, 3, 5) 
            "Ее руки нервно двигаются к лифчику."
            $ cc_wear_bra = False
            "Она тянет его вверх и кидает на пол."
            $ cc_wear_panties = False 
            "Наконец, она снимает трусики."
            m "Отлично."
            call cho_main("........", 3, 3, 3, 4) 
            call cho_main("...............", 1, 3, 1, 4) 
            call cho_main("......................", 1, 3, 1, 9) 
            call cho_main("Эм...", 1, 3, 2, 7) 
            call cho_main("Эм... этого достаточно?", 6, 3, 5, 7) 
            menu:
                "-Достаточно-":
                    m "Ты можешь одеться."
                    m "15 очков Когтеврану."
                    $ ravenclaw += cho_points
                    call cho_main("Спасибо, сэр...", 6, 2, 6, 9) 
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Чоу быстро одевается."
                    hide screen cho_chang
                    jump end_cho_event
                "-Дрочить-":
                    "Ты засовываешь руку под мантию и вытаскиваешь член."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Спортивное и подтянутое тело Чоу, начинает слегка дрожать."
                    call cho_main("Что вы делаете?", 4, 2, 4, 3) 
                    call cho_main("Я не собираюсь смотреть на это за 15 очков.", 6, 2, 5, 7) 
                    "Ты проигнорировал Чоу, обхватывая свой толстый член."
                    call cho_main(".......", 6, 3, 5, 9) 
                    "Чоу делает глубокий вдох."
                    call cho_main("20 очков.", 6, 3, 6, 7) 
                    menu:
                        "-Предложить 15-":
                            "Ты смотришь бедняжке в глаза и продолжаешь дрочить."
                            m "Я дам 15 очков. Не больше."
                            call cho_main("Ладно.", 6, 2, 5, 9) 
                            $ cho_mad += 4
                            jump cho_favor_1_1_1
                        "-Согласиться на 20 очков-":
                            $ cho_points = 20
                            "Ты, дроча, киваешь."
                            m "Звучит не плохо."
                            jump cho_favor_1_1_1
                        "-Дать 25 очков-":
                            $ cho_points = 25
                            "Я дам тебе 25 очков."
                            call cho_main("Серьезно?", 1, 3, 1, 7) 
                            $ cho_mad -= 1
                            jump cho_favor_1_1_1
                            
                            
        "-Быть вежливым-":
            "Несмотря на ее кажущуюся уверенность, руки Чоу дрожат, когда она притрагивается к верхней части одежды."
            m "Давай, девочка."
            call cho_main("Да, сэр!", 1, 3, 2, 1) 
            $ cc_wear_top = False
            $ cc_wear_vest = False
            $ cc_wear_acc = False 
            "Чоу улыбнулась и быстро сняла с себя вверх."
            m "Отлично."
            call cho_main("Спасибо, сэр.", 3, 1, 3, 7) 
            $ cc_wear_skirt = False 
            "Чоу расстегивает юбку своими нежными пальцами."
            call cho_main("Так лучше?", 1, 3, 1, 9) 
            "Ее руки нервно двигаются к лифчику."
            $ cc_wear_bra = False 
            "Она тянет его вверх, над головой, и кидает его на пол."
            call cho_main("Что вы думаете?", 2, 3, 2, 5) 
            m "Просто. великолепно."
            $ cc_wear_panties = False 
            "Наконец, она начинает стягивать с себя трусики."
            m "Очень хорошо."
            call cho_main("........", 3, 3, 3, 4) 
            call cho_main("...............", 1, 3, 1, 4) 
            call cho_main("......................", 1, 3, 1, 9) 
            call cho_main("Эм...", 1, 3, 2, 7) 
            call cho_main("Эм... могу я теперь одеться?", 6, 3, 5, 7) 
            menu:
                "-Достаточно-":
                    m "Ты можешь одеться."
                    m "15 очков Когтеврану."
                    $ ravenclaw += cho_points
                    call cho_main("Спасибо, сэр...", 6, 2, 6, 9) 
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Чоу быстро одевается."
                    hide screen cho_chang
                    jump end_cho_event
                "-Дрочить-":
                    "Ты засовываешь руку под мантию и вытаскиваешь член."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Спортивное тело Чоу тебя сильно возбудило."
                    call cho_main("Что вы делаете?", 4, 2, 4, 3) 
                    call cho_main("Я не соглашалась на это!", 6, 2, 5, 7) 
                    "Ты игнорируешь Чоу, обхватывая свой толстый член."
                    call cho_main(".......", 6, 3, 5, 9) 
                    "Чоу делает глубокий вдох."
                    call cho_main("20 очков.", 6, 3, 6, 7) 
                    menu:
                        "-Предложить 15 очков-":
                            "Ты смотришь бедняжке в глаза и продолжаешь дрочить член."
                            m "Ты получишь 15 очков. Не больше."
                            call cho_main("Ладно.", 6, 2, 5, 9) 
                            $ cho_mad += 2
                            jump cho_favor_1_1_1
                        "-Согласиться на 20 очков-":
                            $ cho_points = 20
                            m "Звучит не плохо."
                            jump cho_favor_1_1_2
                        "-Дать 25 очков-":
                            $ cho_points = 25
                            m "Я дам тебе 25 очков."
                            call cho_main("Серьезно?", 1, 3, 1, 7) 
                            $ cho_mad -= 2
                            jump cho_favor_1_1_2
                            
label cho_favor_1_1_1: 
    call cho_main("....", 6, 3, 5, 5) 
    call cho_main("........", 6, 3, 6, 5) 
    call cho_main("........ Ваш... Такой большой и...", 6, 3, 5, 7) 
    call cho_main(".....толстый.", 6, 3, 6, 6) 
    "Ты видишь как она жадно смотрит на твой член."
    call cho_main("....", 6, 3, 5, 6) 
    call cho_main("Вы скоро закончите, не так ли?", 6, 3, 6, 1) 
    call cho_main("Вы опять все запачкаете.", 6, 3, 5, 7) 
    call cho_main("Вы должно быть думаете, что я очень сексуальна, не так ли?", 6, 3, 6, 9) 
    "Предэякулят стекает с твоего члена."
    call cho_main("О боже...", 6, 3, 5, 5) 
    call cho_main("О боже... Ее так много.", 6, 3, 6, 5) 
    "Испытывая удовольствие от нежных слов Чоу, ты начинаешь бурно кончать."
    m "Ты тормозишь!"
    #-Genie chibi Cums-
    with d3
    hide screen bld1
    with d3
    show screen genie_jerking_sperm
    with d3
    call cho_main("....", 6, 2, 5, 4) 
    call cho_main(".... Что вы сказали?", 6, 2, 5, 7) 
    #-Genie Chibi continues to cum-
    m "Заткнись. Не испорть все."
    call cho_main("......", 6, 3, 6, 9) 
    call cho_main("............", 6, 3, 5, 4) 
    #-Genie Chibi stops cumming-
    show screen genie_jerking_sperm_02
    with d3
    call cho_main("Могу я получить очки?", 1, 3, 2, 9) 
    show screen genie
    hide screen genie_jerking_off
    hide screen genie_jerking_sperm
    with d3
    m "....."
    m "......Очень хорошо. [cho_points] очков Когтеврану."
    $ ravenclaw += cho_points
    call cho_main("Спасибо, сэр...", 6, 3, 5, 1) 
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Чоу быстро одевается."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump end_cho_event
    
label cho_favor_1_1_2:
    "Ты смотришь в глаза Чоу, ее спортивное, молодое тело вызывает у тебя бурное возбуждение."
    call cho_main("....", 6, 3, 5, 5) 
    call cho_main("........", 6, 3, 6, 5) 
    call cho_main("........ваш... такой большой и...", 6, 3, 5, 7) 
    call cho_main(".....толстый.", 6, 3, 6, 6) 
    "Ты видишь как она жадно смотрит на твой член."
    call cho_main("Как скоро вы закончите?", 6, 3, 6, 1) 
    call cho_main("И испачкаете весь свой стол.", 6, 3, 5, 7) 
    "Предэякулят выходит из твоего набухшего члена, стекая по руке."
    call cho_main("Мое тело настолько хорошо?", 6, 3, 6, 9) 
    call cho_main("Вы везде накапали, профессор.", 6, 3, 5, 5) 
    call cho_main("О боже... ваши яички выглядят такими массивными. Там так много.", 6, 3, 6, 5) 
    "Слова Чоу подталкивают тебя к кульминации."
    "Ты очень быстро дрочишь и начинаешь яростно кончать."
    m "Да, шлюха!"
    #-Genie chibi Cums-
    with d3
    hide screen bld1
    with d3
    show screen genie_jerking_sperm
    with d3
    call cho_main("....", 6, 2, 5, 4) 
    call cho_main(".... Что вы сказали?", 6, 2, 5, 7) 
    #-Genie Chibi continues to cum-
    m "Ты... ебанная... шлюха."
    call cho_main("......", 6, 3, 6, 9) 
    call cho_main("............", 6, 3, 5, 4) 
    #-Genie Chibi stops cumming-
    show screen genie_jerking_sperm_02
    with d3
    "Ты обкончал весь стол."
    call cho_main("(Посмотрите на все это!)", 4, 3, 4, 5) 
    call cho_main("......", 6, 3, 5, 5) 
    call cho_main("(Интересно, какой вкус у сп-)", 6, 3, 5, 6) 
    call cho_main("!", 4, 3, 4, 5) 
    call cho_main("Могу я получить очки?", 1, 3, 2, 5) 
    show screen genie
    hide screen genie_jerking_off
    hide screen genie_jerking_sperm
    with d3
    m "....."
    m "......А? Ох, да. Конечно. [cho_points] очков Когтеврану."
    $ ravenclaw += cho_points
    call cho_main("Спасибо, сэр...", 6, 3, 5, 1) 
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Чоу быстро одевается."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump end_cho_event



label cho_favor_1_2:
    $ cho_points = 15
    if cho_whoring < 1:
        $ cho_whoring += 1
    m "Мисс Чанг, не хочешь очень легко заработать 15 очков?"
    call cho_main("Что вы хотите?", 2, 3, 1, 7) 
    m "Могу я снова увидеть твое тело?"
    call cho_main("Вы хотите, чтобы я разделась, сэр?", 6, 3, 5, 7) 
    m "Конечно."
    m "Если тебе не интересно, то думаю, Гермиона будет не против..."
    call cho_main("!", 4, 3, 1, 3) 
    call cho_main("Я разденусь.", 1, 1, 2, 1) 
    call cho_main("Только...", 2, 3, 1, 7) 
    call cho_main("Вы не делайте... вы знаете что... хорошо, сэр?", 2, 3, 1, 5) 
    m "Ты про что, девочка?"
    "Чоу неловко перебирает ногами."
    call cho_main("Не заставляйте меня говорить это, профессор.", 2, 3, 2, 7) 
    m "Что сказать, девочка?"
    call cho_main(".... Мастурбация.", 2, 3, 1, 5) 
    m "Что?"
    call cho_main("Вы опять будете дрочить?", 1, 2, 1, 8) 
    menu:
        "-Конечно-":
            m "Конечно. Потому что ты голая."
            "Чоу делает глубокий вдох."
            call cho_main("Я хочу 20 очков.", 2, 3, 1, 5) 
            menu:
                "-Дать 15 очков-":
                    m "Я дам тебе 15 очков. Не больше."
                    call cho_main("Ладно.", 6, 2, 5, 9) 
                    $ cho_mad += 3
                    $ cho_points = 15
                    pass
                "-Согласить на 20 очков-":
                    m "Хорошо, получишь 20 очков."
                    call cho_main("Хорошо.", 1, 3, 2, 9) 
                    $ cho_points = 20
                    pass
                "-Дать 25 очков-":
                    m "Я дам тебе 25 очков."
                    call cho_main("Серьезно?", 1, 3, 1, 7) 
                    $ cho_mad -= 1
                    $ cho_points = 25
                    pass
            menu:
                "-Быть настойчивым-":
                    "Несмотря на ее кажущуюся уверенность, руки Чоу дрожат, когда она притрагивается к верхней одежде."
                    m "Продолжай, девочка."
                    call cho_main("Да, сэр!", 1, 3, 2, 7) 
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Чоу, дрожа, быстро снимает вверх."
                    m "Так лучше. А теперь низ."
                    call cho_main("Да, сэр.", 1, 3, 1, 9) 
                    $ cc_wear_skirt = False 
                    "Чоу расстегивает юбку своими нежными пальцами и стягивает ее вниз."
                    call cho_main("(Очки... много очков...)", 1, 1, 1, 1) 
                    "Ее руки, дрожа, приближаются к лифчику"
                    $ cc_wear_bra = False
                    "Она тянет его вверх и кидает на пол."
                    $ cc_wear_panties = False 
                    "Наконец, она снимает трусики."
                    m "Очень хорошо."
                    call cho_main("........", 1, 1, 1, 1) 
                    call cho_main("...............", 1, 1, 1, 1) 
                    call cho_main("......................", 1, 1, 1, 1) 
                    call cho_main("Эм...", 1, 1, 1, 1) 
                    call cho_main("Эм... вы собираетесь", 1, 1, 1, 1) 
                    call cho_main("Эм... Вы собираетесь... делать это?", 1, 1, 1, 1) 
                    "Ты засовываешь руку под мантию и вытаскиваешь член."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Спортивное тело Чоу возбуждает тебя."
                    call cho_main("....", 3, 3, 3, 9) 
                    call cho_main("........", 1, 3, 2, 5) 
                    call cho_main("........ваш... такой большой и...", 1, 3, 1, 6) 
                    call cho_main(".....толстый.", 4, 3, 1, 6) 
                    "Ты видишь как она жадно смотрит на твой член."
                    call cho_main("....", 1, 3, 2, 6) 
                    call cho_main("Вы скоро, не так ли?", 1, 3, 1, 5) 
                    call cho_main("Вы опять испачкаете все.", 1, 3, 2, 6) 
                    "Предэякулят выходит из твоего набухшего члена, стекая по руке."
                    call cho_main("Вы наверное думаете какая я сексуальная, да?", 1, 3, 1, 1) 
                    call cho_main("Oх боже...", 1, 3, 2, 7) 
                    call cho_main("Ох боже... Такой большой.", 1, 3, 1, 6) 
                    "Нежные слова Чоу подталкивают тебя к кульминации, ты начинаешь бурно кончать."
                    m "Ты тормозишь!"
                    #-Genie chibi Cums-
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    call cho_main("....", 6, 2, 5, 4) 
                    call cho_main(".... Что вы сказали?", 6, 2, 5, 7) 
                    #-Genie Chibi continues to cum-
                    m "Заткнись. Не испорть все."
                    call cho_main("......", 1, 3, 2, 5) 
                    call cho_main("............", 1, 3, 1, 6) 
                    #-Genie Chibi stops cumming-
                    call cho_main("Могу я получить очки?", 1, 3, 2, 9) 
                    show screen genie
                    hide screen genie_jerking_off
                    hide screen genie_jerking_sperm
                    with d3
                    m "....."
                    m "......Хорошо. [cho_points] очков Когтеврану."
                    $ ravenclaw += cho_points
                    call cho_main("Спасибо, сэр...", 6, 3, 5, 1) 
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Чоу быстро одевается."
                    hide screen cho_chang
                    hide screen genie_jerking_sperm_02
                    jump end_cho_event
                "-Быть любезным-":
                    "Несмотря на ее кажущуюся уверенность, руки Чо дрожат, когда она притрагивается к верху."
                    m "Продолжай, девочка."
                    call cho_main("Да, сэр!", 1, 3, 2, 1) 
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Чоу, улыбаясь, срывает с себя рубашку."
                    m "Отлично."
                    call cho_main("Спасибо, сэр.", 3, 1, 3, 7) 
                    $ cc_wear_skirt = False 
                    "Чоу расстегивает юбку своими нежными пальцами и стягивает вниз."
                    call cho_main("Все нормально?", 1, 3, 1, 9) 
                    "Ее руки, дрожа, притрагиваются к лифчику."
                    $ cc_wear_bra = False 
                    "Она тянет его вверх, над головой, и кидает на пол."
                    call cho_main("Что вы думаете?", 2, 3, 2, 5) 
                    m "Великолепно."
                    $ cc_wear_panties = False 
                    "Наконец, она стягивает вниз трусики."
                    m "Отлично."
                    call cho_main("........", 3, 3, 3, 4) 
                    call cho_main("...............", 1, 3, 1, 4) 
                    call cho_main("......................", 1, 3, 1, 9) 
                    call cho_main("Эм...", 1, 3, 2, 7) 
                    call cho_main("Эм... вы собираетесь...", 1, 3, 1, 5) 
                    call cho_main("Эм... вы собираетесь... делать это?", 1, 3, 4, 6) 
                    m "Что?"
                    call cho_main("Вы добавили очки, так что вы можете подрочить, если захотите!", 3, 2, 3, 7) 
                    m "Что ж, если ты настаиваешь."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Ты засовываешь руку под мантию и вытаскиваешь член."
                    "Ты смотришь в глаза Чоу, ее подтянутое молодое тело круче задницы тролля."
                    call cho_main("....", 3, 3, 3, 9) 
                    call cho_main("........", 1, 3, 2, 5) 
                    call cho_main("........ваш... такой большой и...", 1, 3, 1, 6) 
                    call cho_main(".....толстый.", 4, 3, 1, 6) 
                    "Ты видишь как она жадно смотрит на твой член."
                    call cho_main("Вы скоро закончите?", 1, 3, 1, 5) 
                    call cho_main("И все испачкаете, опять.", 1, 3, 2, 6) 
                    "Предэякулят выходит из твоего набухшего члена, стекая по руке."
                    call cho_main("Мое тело настолько хорошо?", 1, 3, 1, 1) 
                    call cho_main("Вы заляпали все вокруг, профессор.", 1, 3, 2, 7) 
                    call cho_main("О боже... ваши яички такие большие. Там так много.", 1, 3, 1, 6) 
                    "Слова Чоу подталкивают тебя к кульминации."
                    "Ты начинаешь быстро дрочить и яростно кончать."
                    m "Да, шлюха!"
                    #-Genie chibi Cums-
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    call cho_main("....", 6, 2, 6, 5) 
                    call cho_main(".... что вы сказали?", 6, 2, 5, 6) 
                    #-Genie Chibi continues to cum-
                    m "Ты... ебанная... шлюха."
                    call cho_main("......", 1, 3, 2, 5) 
                    call cho_main("............", 1, 3, 1, 6) 
                    #-Genie Chibi stops cumming-
                    "Ты обкончал весь стол."
                    show screen genie
                    hide screen genie_jerking_off
                    hide screen genie_jerking_sperm
                    with d3
                    call cho_main("(Посмотрите на все это!)", 4, 3, 4, 5) 
                    call cho_main("......", 4, 3, 4, 6) 
                    call cho_main("(Интересно, какой вкус у сп-)", 6, 3, 5, 5) 
                    call cho_main("!", 4, 2, 4, 6) 
                    call cho_main("Могу я получить очки?", 1, 3, 2, 9) 
                    m "....."
                    m "......А? Oх, да. Конечно. [cho_points] очков Когтеврану."
                    $ ravenclaw += cho_points
                    call cho_main("Спасибо, сэр...", 6, 3, 5, 1) 
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Чоу быстро одевается."
                    hide screen cho_chang
                    hide screen genie_jerking_sperm_02
                    jump end_cho_event
        "-Я не планировал-":
            m "Я не планировал это делать."
            call cho_main("Oх.", 1, 1, 2, 9) 
            call cho_main("Тогда ладно.", 1, 1, 2, 7) 
            menu:
                "-Быть настойчивым-":
                    "Несмотря на ее кажущуюся уверенность, руки Чоу дрожат, когда она притрагивается к верху."
                    m "Давай, девочка."
                    call cho_main("Да, сэр!", 3, 1, 3, 3) 
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Чоу, скрипя зубами, снимает с себя верхнюю одежду."
                    m "Так лучше. А сейчас низ."
                    call cho_main("Да, сэр.", 3, 3, 3, 7) 
                    $ cc_wear_skirt = False 
                    "Чоу расстегивает юбку своими нежными пальцами и тянет ее вниз."
                    call cho_main("(Очки... много очков...)", 3, 3, 3, 4) 
                    "Ее руки нервно приближаются к лифчику."
                    $ cc_wear_bra = False
                    "Она тянет его вверх, над головой, и кидает на пол."
                    $ cc_wear_panties = False 
                    "Наконец, она стянула трусики."
                    m "Отлично."
                    call cho_main("........", 3, 3, 3, 4) 
                    call cho_main("...............", 1, 3, 1, 4) 
                    call cho_main("......................", 1, 3, 1, 9) 
                    call cho_main("Эм...", 1, 3, 2, 7) 
                    call cho_main("Эм... этого достаточно?", 1, 3, 1, 5) 
                    menu:
                        "-Достаточно-":
                            m "Ты можешь одеться."
                            m "15 очков Когтеврану."
                            $ ravenclaw += cho_points
                            call cho_main("Спасибо, сэр...", 6, 2, 6, 9) 
                            $ cc_wear_top = True
                            $ cc_wear_bra = True
                            $ cc_wear_stockings = True 
                            $ cc_wear_skirt = True
                            $ cc_wear_panties = True
                            $ cc_wear_vest = True
                            ">Чоу быстро одевается."
                            hide screen cho_chang
                            jump end_cho_event
                        "-Дрочить-":
                            "Ты засовываешь руку под мантию и вытаскиваешь член."
                            "Спортивное тело Чоу возбуждает тебя."
                            call cho_main("Что вы делаете?", 4, 2, 4, 3) 
                            call cho_main("Я не собираюсь смотреть на это за 15 очков.", 6, 2, 5, 7) 
                            "Ты проигнорировал Чоу, обхватывая свой член."
                            call cho_main(".......", 6, 3, 5, 9) 
                            "Чоу делает глубокий вдох."
                            call cho_main("20 очков.", 6, 3, 6, 7) 
                            menu:
                                "-Настаивать на 15 очках-":
                                    "Ты смотришь бедняжке в глаза и продолжаешь дрочить член."
                                    m "Ты получишь 15 очков. Не больше."
                                    call cho_main("Ладно.", 6, 2, 5, 9) 
                                    $ cho_mad += 2
                                    $ cho_points = 15
                                    jump cho_favor_1_1_1
                                "-Согласиться на 20 очков-":
                                    m "Звучит не плохо."
                                    $ cho_points = 20
                                    jump cho_favor_1_1_1
                                "-Дать 25 очков-":
                                    m "Я дам тебе 25 очков."
                                    call cho_main("Серьезно?", 1, 3, 1, 7) 
                                    $ cho_mad -= 2
                                    $ cho_points = 25
                                    jump cho_favor_1_1_1
                "-Быть милым-":
                    "Несмотря на ее кажущуюся уверенность, руки Чоу дрожат, когда она притрагивается к верху."
                    m "Продолжай, девочка."
                    call cho_main("Да, сэр!", 1, 3, 2, 1) 
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Чоу, улыбаясь, снимает вверх."
                    m "Отлично."
                    call cho_main("Спасибо, сэр.", 3, 1, 3, 7) 
                    $ cc_wear_skirt = False 
                    "Чоу расстегивает юбку своими нежными пальцами и тянет ее вниз."
                    call cho_main("Все нормально?", 1, 3, 1, 9) 
                    "Ее руки нервно приближаются к лифчику."
                    $ cc_wear_bra = False 
                    "Она тянет его вверх, над головой, и кидает его на пол."
                    call cho_main("Что вы думаете?", 2, 3, 2, 5) 
                    m "Великолепно."
                    $ cc_wear_panties = False 
                    "Наконец, она стягивает трусики."
                    m "Очень хорошо."
                    call cho_main("........", 3, 3, 3, 4) 
                    call cho_main("...............", 1, 3, 1, 4) 
                    call cho_main("......................", 1, 3, 1, 9) 
                    call cho_main("Эм...", 1, 3, 2, 7) 
                    call cho_main("Эм... Этого достаточно?", 6, 3, 5, 7) 
                    menu:
                                
                        "-Достаточно-":
                            m "Ты можешь одеваться."
                            m "15 очков Когтеврану."
                            $ ravenclaw += cho_points
                            call cho_main("Спасибо, сэр...", 6, 2, 6, 9) 
                            $ cc_wear_top = True
                            $ cc_wear_bra = True
                            $ cc_wear_stockings = True 
                            $ cc_wear_skirt = True
                            $ cc_wear_panties = True
                            $ cc_wear_vest = True
                            ">Чоу быстро одевается."
                            hide screen cho_chang
                            jump end_cho_event
                        "-Дрочить-":
                            "Ты засовываешь руку под мантию и достаешь член."
                            hide screen blktone8
                            with d3
                            hide screen genie
                            show screen genie_jerking_off
                            with d3
                            "Спортивное тело Чоу возбуждает тебя."
                            call cho_main("Что вы делаете?", 4, 2, 4, 3) 
                            call cho_main("Я не соглашалась на это!", 6, 2, 5, 7) 
                            "Игнорируя Чоу, ты обхватываешь свой член."
                            call cho_main(".......", 6, 3, 5, 9) 
                            "Чоу делает глубокий вдох."
                            call cho_main("20 очков.", 6, 3, 6, 7) 
                            menu:
                                "-Настаивать на 15 очков-":
                                    "Ты смотришь бедняжке в глаза и продолжаешь дрочить член."
                                    m "Ты получишь 15 очков. Не больше."
                                    call cho_main("Ладно.", 6, 2, 5, 9) 
                                    $ cho_mad += 2
                                    jump cho_favor_1_1_1
                                "-Согласиться на 20 очков-":
                                    $ cho_points = 20
                                    m "Звучит не плохо."
                                    jump cho_favor_1_1_2
                                "-Дать 25 очков-":
                                    $ cho_points = 25
                                    m "Я дам тебе 25 очков."
                                    call cho_main("Серьезно?", 1, 3, 1, 7) 
                                    $ cho_mad -= 2
                                    jump cho_favor_1_1_2

###Favor 2###
label cho_favor_2:
    m "(Может, мне потрогать немного задницу Чоу.)"
    menu:
        "-Потрогать ее задницу-":
            if chof2_first: #have to include new boolean chof2_first=False
                $ chof2_first = False
                g9 "Мисс Чанг, я бы хотел потрогать твою задницу."
                call cho_main("Мою... задницу?", 6, 3, 6, 1) 
                m "Да. Я хочу потрогать твою задницу."
                call cho_main("Я знала, что вам нравится моя попка.", 5, 1, 1, 5) 
                call cho_main("{size=-4}(Я так и знала, что он не сможет долго сопротивляться.){/size}", 5, 1, 2, 6) 
                call cho_main("Если вы хотите потрогать мою попку, это будет дополнительно стоить вам.", 3, 1, 3, 3) 
                call cho_main("40 очков.", 1, 1, 2, 7) 
                m "Это много, чтоб схватить за задницу."
                ">Чоу вертит свое гибкое тело."
                ">Ты видишь очертания попки под ее формой."
                call cho_main("Давайте, профессор... разве это не стоит того?", 1, 1, 1, 1) 
                m "Отличная задница..."
                m "Но я могу попросить Гермиону..."
                menu:
                    "-25 очков-":
                        m "Я могу попросить Гермиону за 25 очков."
                        call cho_main("25?", 4, 2, 1, 3) 
                        call cho_main("25? Так дешево.", 5, 2, 2, 4) 
                        call cho_main("Я дам вам потрогать за 40.", 1, 2, 1, 7) 
                        m "Хорошо, 40. Это стоит того."
                        jump chofbm
                    "-35 очков-":
                        m "Я могу попросить Гермиону за 35 очков."
                        call cho_main("{size=-2}35? Серьезно?....{/size}", 6, 2, 5, 9) 
                        call cho_main("{size=+2}Если ее жирная задница стоит 35, то моя должна стоить 40.{/size}", 3, 2, 3, 8) 
                        m "Ладно."
                        jump chofbm
                    "-50 очков-":
                        m "Я могу попросить Гермиону за 50 очков."
                        call cho_main("50!", 4, 2, 1, 7) 
                        call cho_main("50! Вы серьезно? Ни за что.", 6, 2, 5, 1) 
                        call cho_main("Но, у нее даже не получается...", 6, 3, 6, 9) 
                        m "Но, твоя задница сойдет на 40."
                        call cho_main("Моя задница сойдет?!", 6, 2, 5, 3) 
                        call cho_main("Я покажу вам, чья задница лучше!", 6, 2, 5, 1) 
                        $ cho_mad +5 #new variable cho_mad
                        jump chofbm
                    "-Бесплатно-":
                        m "Я могу заставить Гермиону сделать это абсолютно бесплатно."
                        call cho_main("Бесплатно?", 4, 2, 1, 7) 
                        call cho_main("Что за маленькая шлюха.", 6, 1, 6, 5) 
                        call cho_main("Конечно, вам все равно придется заплатить мне.", 3, 2, 3, 7) 
                        call cho_main("40 очков.", 6, 2, 5, 8) 
                        m "Хорошо, мисс Чанг."
                        jump chofbm
            else:
                    m "Мисс Чанг. Я бы хотел снова потрогать твою задницу."
                    if cho_whoring  == 1: #new variable cho_whoring 
                        call cho_main("Что ж... хорошо. Но это будет стоить 40 очков", 2, 3, 2, 7) 
                        m "Отлично. А теперь иди сюда, девочка."
                        jump chofbm
                    if cho_whoring  == 2:
                        call cho_main("Хорошо, профессор.", 1, 3, 2, 5) 
                        call cho_main("40 очков, верно?", 2, 1, 1, 7) 
                        m "Конечно, мисс Чанг."
                        jump chofbm
                    if cho_whoring  == 3:
                        call cho_main("Что вы хотите?", 1, 1, 1, 5) 
                        call cho_main("Вы собираетесь дрочить?", 6, 3, 5, 6) 
                        menu:
                            "Конечно.":
                                m "Конечно."
                                call cho_main("Наверное, мне лучше снять трусики.", 6, 3, 6, 6) 
                            "Нет.":
                                m "Конечно нет. За кого ты меня принимаешь, извращенка?"
                                call cho_main("Что ж...", 6, 1, 2, 1) 
                        jump chofbm

label chofbm:
#Cho chibi walks over to Dumbledore's desk and turns around.
    if cho_whoring  == 1:
        if not chof2_first:
            call cho_main("Ладно...{w=2} вы можете потрогать меня.", 1, 3, 2, 5) 
            ">Чоу стоит всего в нескольких дюймах перед тобой, ты видишь какая у нее упругая попка."
            stop music
            $ renpy.play('sounds/scratch.wav')
            call cho_main("Здравствуйте! Хогвартс, как и большинство респектабельных заведений для магического обучения, находится в Великобритании.", 3, 2, 3, 3) 
            call cho_main("Пожалуйста, придерживайтесь метрической системы.", 3, 2, 3, 4) 
            ">Aх, да... конечно..."
            #play music fadein 1.5
        else:
            call cho_main("Хорошо...", 1, 3, 2, 5) 
            call cho_main("Хорошо... вы можете меня потрогать.", 1, 3, 2, 6) 
        ">Чоу стоит всего в нескольких дюймах перед тобой, ты видишь какая у нее упругая попка."
        ">Чоу руками схватилась за стол."
        ">Ты чувствуешь ее дрожь, когда притрагиваешься к ее ногам."
        ">Руки Чоу крепко вцепились в стол, поскольку твои руки начинают подниматься вверх по ее ногам."
        ">Ты дотрагиваешься до ее трусиков и начинаешь гладить ее ягодицы."
        ">Ты сжимаешь пару раз попку и даешь оценку ее заднице."
        call cho_main("Проф-профессор...", 3, 3, 3, 5) 
        ">Ты слышишь нервный голос Чоу. Ее попка сжимается."
        call cho_main("Этого достаточно, верно профессор?", 1, 3, 2, 9) 
        menu:
            "-\"Да\"-":
                m "Да. Думаю, я закончил."
                call cho_main("Спасибо, Профессор.", 1, 1, 2, 1) 
                m "40 очков Когтеврану."
                $ ravenclaw += 40
                jump chof2end
            "-\"Абсолютно нет!\"-":
                m "Абсолютно нет. Я заплатил тебе 40 очков за это, девочка."
                call cho_main("Но, сэр, я-", 4, 3, 1, 7) 
                ">Ты еще сильнее сжимаешь ее попку."
                m "Я скажу, когда будет достаточно."
                call cho_main("Ладно.", 5, 2, 2, 9) 
                $ cho_mad += 2
                ">Попка Чоу гладкая и теплая при прикосновении. Тем не менее, ты начинаешь дико щупать попку бедной девушки."
                call cho_main("Оу.", 5, 2, 1, 4) 
                call cho_main("Оу. Оу. Больно!", 5, 2, 1, 7) 
                call cho_main("Профессор!", 5, 2, 1, 3) 
                call cho_main("Профессор! Профессор, остановитесь, пожалуйста.", 5, 2, 1, 8) 
                menu:
                    "-Остановиться-":
                        ">Ты приходишь в себя и останавливаешься."
                        ">Чоу быстро опускает юбку, поглаживая попу."
                        call cho_main("Спасибо, сэр.", 3, 1, 3, 4) 
                        call cho_main("Спасибо, сэр. Могу я получить очки?", 2, 3, 1, 7) 
                        m "Конечно, мисс Чанг. Ты их заработала."
                        m "40 очков Когтеврану."
                        $ ravenclaw += 40
                        jump chof2end
                    "-Продолжать-":
                        ">Ты игнорируешь глупый девичий крик и продолжаешь издеваться над ее попкой, скользя руками под ее трусики."
                        call cho_main("Остановитесь!", 4, 2, 1, 3) 
                        ">Ты сильнее сжимаешь задницу Чоу."
                        ">Игрок в квиддич падает на колени перед тобой."
                        call cho_main("Больно!", 4, 3, 1, 3) 
                        ">Ты поднимаешь ее, затем приближаешься большим пальцем к ее тугой, коричневой дырочке."
                        ">Ты чувствуешь, как она борется с тобой, когда ты схватил ее за задницу."
                        call cho_main("Профессор Дамблдор!", 3, 2, 3, 3) 
                        ">Ты внезапно отпускаешь ее и начинаешь охаживать ее ягодицы."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("...", 3, 3, 3, 4) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        hide screen white 
                        with hpunch
                        call cho_main("Ой!", 6, 3, 6, 4) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        hide screen white
                        with hpunch 
                        call cho_main("(Это так больно!)", 4, 3, 1, 1) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        hide screen white 
                        with hpunch
                        ">Чоу тяжело дышит, а ее ноги дрожат."
                        ">Контуры твоей ладони отпечатались на ягодицах девушки."
                        call cho_main("Ай!", 4, 3, 1, 3) 
                        call cho_main("Ай!...", 4, 2, 1, 5) 
                        call cho_main("Ай!...Профессор!", 4, 2, 1, 3) 
                        ">Чоу вырывается и быстро уходит."
                        #Cho chibi walks to the middle of the room.
                        call cho_main("Вы зашли слишком далеко!", 3, 2, 3, 3) 
                        call cho_main("Я никогда не соглашалась на что-то подобное.", 5, 2, 1, 3) 
                        call cho_main(".......я хочу 60 очков.", 3, 2, 3, 3) 
                        menu:
                            "-Ты заработала 60 очков-":
                                m "Хорошо. Меня немного занесло. 60 очков Когтеврану."
                                call cho_main("Спасибо, сэр.", 5, 1, 2, 4) 
                                $ cho_mad += 5
                                $ ravenclaw += 60
                                jump chof2end
                            "-\"Это было слишком. 80 очков\"-":
                                m "Кажется, я немного увлекся."
                                call cho_main("...", 6, 2, 6, 4) 
                                m "Хорошо, 80 очков Когтеврану."
                                call cho_main("Серьезно?", 6, 2, 5, 7) 
                                call cho_main("Что ж, я полагаю, это было не так уж плохо...", 6, 3, 6, 9) 
                                $ cho_mad +1
                                $ ravenclaw += 80
                                jump chof2end
                            "-\"(Да как она посмела?!) 0 очков!\"-":
                                m "Как ты посмела ослушаться своего директора, Гномблдора!"
                                m "Если ты не подойдешь обратно ко мне, то ничего не получишь."
                                call cho_main("Что!", 4, 3, 1, 3) 
                                call cho_main("Это нечестно!", 4, 2, 1, 3) 
                                m "Ну?"
                                call cho_main("Ладно!", 6, 2, 5, 4) 
                                $ cho_mad +15
                                #Cho chibi returns to Dumbledore's desk.
                                ">Чоу возращается к твоему столу."
                                ">Ты видишь ее слезы, когда она оттопыривает тебе свою попу."
                                ">Не теряя времени, ты быстро срываешь с бедной девочки трусики и начинаешь лапать."
                                call cho_main("...", 4, 2, 2, 5) 
                                pause
                                ">Потянув в разные стороны ее ягодицы, ты начинаешь тереть большим пальцем по ее дырочке."
                                call cho_main("...", 6, 3, 6, 5) 
                                call cho_main("......", 6, 3, 5, 6) 
                                ">Ты чувствуешь, как тело Чоу напрягается."
                                ">Ты смочил свой палец слюной и начал стимулировать в дырочку."
                                call cho_main(".........", 4, 3, 4, 5) 
                                m "Расслабься."
                                ">Наконец, твой палец вошел и ты начинаешь шевелить им."
                                call cho_main("Профес-....", 6, 3, 6, 6) 
                                ">Чоу пытается закричать, но она борется с этим."
                                ">Понятно, она хочет получить, как можно больше очков."
                                m "{size=-2}(Не волнуйся, девочка. Ты получишь свои очки.){/size}"
                                ">После того как твой палец полностью вошел в нее, ты вытягиваешь его."
                                ">Она сжала ягодицы и ты не смог вытащить палец."
                                call cho_main("...", 1, 3, 2, 5) 
                                ">Ты чувствуешь, что она опять сжала ягодицы."
                                ">Палец скользит в ее дырочке."
                                ">Чоу падает на стол. Ее дыхание становится чаще и более глубоким."
                                call cho_main("...", 3, 3, 3, 5) 
                                ">Внезапно, ты чувствуешь ее пульсацию, сжимающую палец сильнее."
                                call cho_main("Профессор!", 4, 3, 4, 6) 
                                ">Чоу кончает на твой палец."
                                m "40 очков Когтеврану."
                                call cho_main("{size=-2}.....да.{/size}", 6, 3, 5, 5) 
                                $ ravenclaw += 40
                                jump chof2end
    if cho_whoring  == 2:
        call cho_main("...", 1, 1, 1, 1) 
        call cho_main("......", 1, 1, 1, 1) 
        call cho_main("......Вы хотите потрогать меня?", 1, 1, 1, 1) 
        ">Чоу задирает юбку и наклоняется перед тобой."
        call cho_main("Ну?", 1, 1, 1, 1) 
        ">Чоу перед тобой крутит своей попкой."
        m "Великие пески...."
        ">Твои руки устремляются к попке Чоу и крепко сжимают ее."
        ">Ты пару раз сильно сжал ее булочки."
        cho_sexy "Проф-профессор..."
        ">Ты слышишь тихий голос Чоу. Ее задница напряглась от прикосновения."
        call cho_main("Еще не все, верно, профессор?", 1, 1, 1, 1) 
        menu:
            "-Нет, этого вполне достаточно.-":
                m "Нет, нет. Этого вполне достаточно. Спасибо, мисс Чанг."
                call cho_main("....ах. Спасибо вам, профессор.", 1, 1, 1, 1) 
                m "40 очков Когтеврану."
                $ ravenclaw += 40
                jump chof2end
            "-Да, верно.-":
                m "Ты права. В конце концов, я дам тебе 40 очков за это, девочка."
                call cho_main("Да, сэр. Но...", 1, 1, 1, 1) 
                m "Что но?"
                ">Чоу начинает покачивать попкой."
                ">Она оттягивает в сторону приталенную часть трусиков, немного оголяя ягодицы."
                cho_sexy "Что ж, сэр. Я полагаю, за 60 очков я могла бы снять эти раздражающие трусики."
                call cho_main("И дать вам почувствовать меня, сэр...", 1, 1, 1, 1) 
                menu:
                    "-60 очков, хорошо.-":
                        m "Хорошо, 60 очков твои."
                        $ ravenclaw += 60
                        call cho_main("{size=-4}(Ничего себе, это было легко.){/size}", 1, 1, 1, 1) 
                        call cho_main("{size=-4}(Я уверена, что его член сильно возбужден...){/size}", 1, 1, 1, 1) 
                        ">Чоу стягивает трусики вниз."
                        ">Она снимает их, затем широко расставляет ноги."
                        ">Молодая звезда квиддича прогибает спину и облокачивается на стол."
                        m "Очень хорошо, мисс Чанг."
                        call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                        jump chof2wl2
                    "-50 очков, не больше.-":
                        m "Я думаю, 50 очков хорошая цена. Верно?"
                        call cho_main("50?", 1, 1, 1, 1) 
                        ">Чоу начинает вилять своей попой."
                        call cho_main("Посмотрите, я думаю, что это стоит гораздо больше...", 1, 1, 1, 1) 
                        menu:
                            "-50 очков.-":
                                m "50 очков."
                                call cho_main("Что ж, хорошо.", 1, 1, 1, 1) 
                                call cho_main("{size=-4}(60 очков было бы много.){/size}", 1, 1, 1, 1) 
                                $ ravenclaw += 50
                                ">Чоу стягивает трусики вниз и кладет руки на стол."
                                jump chof2wl2
                            "-Ладно. 55 очков.-":
                                m "Очень хорошо, мисс Чанг. Я дам тебе 55 очков."
                                call cho_main("Хм. 55 очков, справедливо.", 1, 1, 1, 1) 
                                $ ravenclaw += 55
                                ">Чоу соблазнительно виляет попкой, затем приспускает трусики и облокачивается на стол."
                                call cho_main("Но, Профессор...", 1, 1, 1, 1) 
                                m "Да?"
                                cho_sexy "Не думаю, что смогу дотянуться. Вы мне поможете?"
                                m "Конечно, мисс Чанг. Это важно для директора, взять инициативу в свои руки."
                                ">Ты наклоняешься вперед и медленно снимаешь трусики Чоу, освобождая идеальную попку."
                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                jump chof2wl2
                            "-Нет.-":
                                ">Ты с силой сжимаешь попку Чоу."
                                m "Нет. Я так не думаю."
                                call cho_main("Что?", 1, 1, 1, 1) 
                                call cho_main("Что ж... я думаю, могу и за 50 очков сделать.", 1, 1, 1, 1) 
                                menu:
                                    "-Да.-":
                                        m "Хорошо. 50 очков. Хорошо торгуешься, мисс Член."
                                        call cho_main("Меня зовут Чанг. И да, я сейчас разденусь.", 1, 1, 1, 1) 
                                        $ ravenclaw += 50
                                        $ cho_mad +1
                                        ">Чоу быстро стягивает трусики, затем облокачивается на стол."
                                        jump chof2wl2
                                    "-Нет.-":
                                        m "Нет."
                                        call cho_main("Oх, хорошо.", 1, 1, 1, 1) 
                                        ">Трусики Чоу снова оказываются одетыми. Тем не менее, ты начинаешь нежно тискать упругую попку девушки."
                                        call cho_main("...", 1, 1, 1, 1) 
                                        call cho_main("......", 1, 1, 1, 1) 
                                        call cho_main(".........", 1, 1, 1, 1) 
                                        call cho_main("Этого достаточно, сэр?", 1, 1, 1, 1) 
                                        menu:
                                            "-Да. Достаточно.-":
                                                ">Ты киваешь."
                                                m "Да. Это было прекрасно, мисс Чанг."
                                                ">Чоу быстро тянет юбку вниз, разглаживая трусики."
                                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                                m "40 очков Когтеврану."
                                                $ ravenclaw += 40
                                                jump chof2end
                                            "-Продолжать.-":
                                                ">Ты ингнорируешь вопрос и продолжаешь трогать ее попку, при этом засовывая руки под трусики."
                                                call cho_main("Я знала, что вы не сможете устоять.", 1, 1, 1, 1) 
                                                ">Ты хватаешься за ее задницу и пару раз сжимаешь."
                                                m "40 очков Когтеврану."
                                                call cho_main("Спасибо, профессор.", 1, 1, 1, 1) 
                                                $ ravenclaw += 40
                                                jump chof2end

        label chof2wl2:
        ">Ты смотришь на молодую, упругую попку Чоу."
        ">Похоже, все ее тренировки в квиддич окупились."
        ">Попка азиатских девочек прекрасна."
        cho_seductive "Ну?"
        ">Ты хватаешь попку и сжимаешь ее."
        ">Твой член очень возбужден."
        menu:
            "-Дрочить-":
                ">Ее задница очаровывает тебя."
                ">Ты продолжаешь сжимать ее попку одной рукой, второй ты достаешь член из-под мантии."
                call cho_main("Что вы делаете?", 1, 1, 1, 1) 
                ">Ты начинаешь дрочить, сжимая ее попку."
                cho_seductive "Х-хорошо, но я хочу дополнительно 5 очков... {w=.5} нет, ДЕСЯТЬ очков."
                menu:
                    "-Ладно.-":
                        ">Ты киваешь."
                        m "Ладно. Ты получишь свои очки, девочка."
                        call cho_main("Хорошо, профессор. Но вам лучше остановиться заранее... вы знаете.", 1, 1, 1, 1) 
                        ">Чоу трясет попкой из стороны в сторону."
                        ">Ты поглаживаешь свой член."
                        cho_sexy_surprise "..."
                        ">Чоу трясет своей задницей вверх и вниз. Ты шлепнул."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=-4}(Больно...){/size}", 1, 1, 1, 1) 
                        call cho_main("Профессор Дамбл-{nw}", 1, 1, 1, 1) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=-4}(Ох черт. Мне становится очень хорошо.){/size}", 1, 1, 1, 1) 
                        ">Каждый ШЛЕПОК по ее попке, возбуждает тебя, пока ты не почувствовал знакомое чувство в своих яичках."
                        menu:
                            "-Кончить-":
                                ">Наконец, ты решаешь на последок шлепнуть ее-"
                                $ renpy.play('sounds/slap_02.mp3')
                                show screen white
                                "{size=+4}ШЛЕП!{/size}"
                                #Shake the screen
                                hide screen white 
                                ">Твой член начал извергаться."
                                m "АХ, ты чертова шлюха!"
                                #Genie cums. - I'd need to know which screen to put here
                                cho_wideEyes "Что, {size=+2}Что?{/size}"
                                cho_wideEyesLookingBack "{size=+4}Вы кончаете?{/size}"
                                ">Твоя сперма брызгает на задницу Чоу."
                                call cho_main("O боже...", 1, 1, 1, 1) 
                                ">Последние капли спермы падают на попку Чоу."
                                call cho_main("Вы {size=+2}закончили{/size} пачкать меня своей {size=+2}отвратительной{/size}, {size=+3}старой{/size}, {size=+4}волшебной спермой!{/size}", 1, 1, 1, 1) 
                                call cho_main("Я в полном недоумении, придурок!", 1, 1, 1, 1) 
                                call cho_main("Вы должны мне еще 10 очков!", 1, 1, 1, 1) 
                                $ cho_mad +=1
                                menu:
                                    "-Да.-":
                                        m "Да, конечно. 10 дополнительных очков Когтеврану."
                                        $ ravenclaw += 10
                                        call cho_main("Посмотрите на этот беспорядок!", 1, 1, 1, 1) 
                                        call cho_main("...", 1, 1, 1, 1) 
                                        call cho_main("{sIze=-2}...Спасибо, сэр.{/size}", 1, 1, 1, 1) 
                                        ">Чоу быстро надевает на, пропитанную спермой, задницу трусики и разглаживает юбку."
                                        call cho_main("Так должно быть лучше.", 1, 1, 1, 1) 
                                        jump chof2end
                                    "-Сожалею.-":
                                        m "Это не моя вина, ты заставила меня кончить."
                                        call cho_main("!!", 1, 1, 1, 1) 
                                        m "Ты должна быть более осторожнее."
                                        call cho_main("Вы, наверное, шутите!", 1, 1, 1, 1) 
                                        call cho_main("Ваша вонючая сперма на моей попе! Я пахну как...как...как Гермиона!", 1, 1, 1, 1) 
                                        m "Сожалею."
                                        call cho_main("Вы-грязный, старый волшебник!", 1, 1, 1, 1) 
                                        ">Чоу хватает трусики с пола и уходит."
                                        $ cho_mad +5
                                        jump chof2end
                            "-Остановиться.-":
                                ">Ты останавливаешься в последний момент и убираешь свой член."
                                ">Твои яички пульсируют."
                                call cho_main("Вы в порядке?", 1, 1, 1, 1) 
                                m "Я волшебник, девочка."
                                jump chof2end
                    "-Я дам тебе 15 очков.-":
                        ">Ты делаешь несколько быстрых движений по пульсирующему члену, прежде чем коснуться ее ягодиц..."
                        m "Я дам тебе 15 очков."
                        call cho_main("15?... Хорошо, профессор.", 1, 1, 1, 1) 
                        ">Чоу трясет попкой из стороны в сторону, слегка притрагиваясь к кончику члена."
                        ">Ты начинаешь дрочить еще быстрее."
                        cho_sexy_surprise "Что вы там делаете..."
                        ">Чоу шевелит задницей вверх и вниз."
                        call cho_main("{size=-4}(О боже... я не могу поверить, что я позволяю старику тереться членом о свою попку.){/size}", 1, 1, 1, 1) 
                        call cho_main("Профессор Дамблдор, скажите мне, когда вы-{w=.5}{nw}", 1, 1, 1, 1) 
                        ">Ты членом шлепаешь по ее заднице, а затем и рукой."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("Профессор Дамблдор, скажите мне, когда вы-КОНЧИТЕ!", 1, 1, 1, 1) 
                        call cho_main("(Ох черт!)", 1, 1, 1, 1) 
                        ">Немного предэякулята попадает на попку Чоу."
                        call cho_main("Профессор...", 1, 1, 1, 1) 
                        ">Ты снова шлепаешь членом по ее заднице."
                        ">Ты дрочишь еще быстрее, пока не почувствовал знакомое ощущение в своих яичких."
                        menu:
                            "-Кончить.-":
                                ">Ты кончаешь на попку Чоу."
                                m "О, Великий молот Грабтора! (прим. отсылка к фильму - В поисках галактики. ориг. Galaxy Quest 1999 года.)"
                                #Genie cums. - Find chibi
                                cho_wideEyes "О боже... Что это такое?"
                                cho_wideEyesLookingBack "{size=+2}Вы кончаете?{/size}"
                                ">Твоя сперма брызгает по заднице Чоу."
                                call cho_main("Боже...", 1, 1, 1, 1) 
                                ">Ты до выхода последней капли надрачиваешь свой член."
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("Моя задница вся покрыта!", 1, 1, 1, 1) 
                                call cho_main("Очень липко. Вы должны мне 10 дополнительных очков!", 1, 1, 1, 1) 
                                menu:
                                    "-Почему нет?-":
                                        m "Да, конечно. 10 дополнительных очков Когтеврану."
                                        $ ravenclaw += 10
                                        call cho_main("Посмотрите на этот беспорядок!", 1, 1, 1, 1) 
                                        call cho_main("...", 1, 1, 1, 1) 
                                        call cho_main("{sIze=-2}...Спасибо, сэр.{/size}", 1, 1, 1, 1) 
                                        ">Чоу быстро надевает трусики и рукой приглаживает юбку."
                                        call cho_main("Так должно быть лучше.", 1, 1, 1, 1) 
                                        jump chof2end
                                    "-Сожалею.-":
                                        m "Это не моя вина, что ты заставила меня кончить."
                                        call cho_main("!!!", 1, 1, 1, 1) 
                                        m "Ты должна быть более осторожнее."
                                        call cho_main("Вы, наверное, шутите!", 1, 1, 1, 1) 
                                        call cho_main("Ваша вонючая сперма вся на моей попе! Я пахну как... как... как Гермиона!", 1, 1, 1, 1) 
                                        m "Сожалею."
                                        call cho_main("Вы всего лишь грязный, старый волшебник!", 1, 1, 1, 1) 
                                        ">Чоу хватает трусики с пола и уходит."
                                        $ cho_mad +5
                                        jump chof2end
                            "-Предупредить ее.-":
                                m "Я почти!"
                                call cho_main("Правда?", 1, 1, 1, 1) 
                                ">Внезапно, ты чувствуешь, как Чоу прижимается к тебе."
                                ">Твой член плотно обхватывают ягодицы Чоу."
                                cho_sexy "Кончайте, профессор!"
                                ">Попкой Чоу трется об твой член."
                                ">Наконец, ты яростно кончаешь на нее."
                                m "Поддержи Aka-{nw}"
                                cho_sexy "Кончайте молча, старик!"
                                m "Поддержи Aka-ахххх! Шлюха!"
                                #Genie cums. - find chibi
                                ">Твой член выстреливает спермой на ее попку."
                                call cho_main("Я чувствую как моя попа становится грязной!", 1, 1, 1, 1) 
                                ">После последней капли, ты облокачиваешься на кресло."
                                m "Молодец, девочка."
                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                ">Чоу надевает трусики."
                                ">Затем она слегка хлопает по своей липкой заднице."
                                call cho_main("Я не могу быть неопрятной в коридоре, не так ли?", 1, 1, 1, 1) 
                                jump chof2end
    if cho_whoring  ==3:
        ">Чоу приподнимает юбку, обнажая голую задницу, затем наклоняется на твой стол."
        call cho_main("Ну?", 1, 1, 1, 1) 
        ">Чоу вертит своей задницей перед тобой."
        m "Великие пески... Пепослушная девочка."
        ">Твои руки трогают ее задницу и сжимают."
        ">Ты еще пару раз сжал их."
        cho_sexy "Дамблдор..."
        ">Ты слышишь стон Чоу."
        call cho_main("Я знаю, вы хотите большего, не так ли?", 1, 1, 1, 1) 
        call cho_main("Вы...{w=1.5} вы хотите кончить, верно?", 1, 1, 1, 1) 
        menu:
            "-Нет, я сдержусь.-":
                m "Нет, мисс Чанг. Я контролирую себя!"
                call cho_main("....ах. Что?", 1, 1, 1, 1) 
                m "40 очков Когтеврану."
                $ ravenclaw += 40
                call cho_main("...спасибо, эм?", 1, 1, 1, 1) 
                jump chof2end
            "-Конечно!-":
                m "{size=-4}(Я понимаю. Противная маленькая девочка.){/size}"
                m "Ты же хочешь заработать 40 очков, девочка."
                call cho_main("Да, сэр. Но...", 1, 1, 1, 1) 
                m "Что, но?"
                ">Чоу начинает покачивать задницей."
                ">Время от времени ты замечаешь ее маленькую дырочку."
                ">Чоу наклоняется и разводит  разную сторону свои ягодицы."
                call cho_main("Что ж, сэр. За 65 очков я могла бы...", 1, 1, 1, 1) 
                cho_sexy "Что ж, сэр. За 65 очков я могла бы позволить вам приложить член меж моих ягодиц."
                cho_sexy "И трясти задницей, пока вы не кончите."
                menu: #[No.]
                    "-65 очков, хорошо.-":
                        m "Что ж, я согласен."
                        call cho_main("{size=-4}(Ничего себе, это было легко.){/size}", 1, 1, 1, 1) 
                        call cho_main("{size=-4}(Уверена, что его яички полны грязной спермы.){/size}", 1, 1, 1, 1) 
                        ">Чоу выгибает спину и приближается к тебе."
                        ">Затем, звездочка квиддича обхватывает твой член своими ягодицами."
                        m "Отлично, мисс Чанг."
                        call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                        jump chof2hd
                    "-55 очков будет вполне достаточно.-":
                        m "Я думаю 55 очков будет достаточно. Верно?"
                        call cho_main("55?", 1, 1, 1, 1) 
                        ">Чоу начинает соблазнительно покачивать своей попкой."
                        call cho_main("Давайте, я думаю, что это стоит гораздо больше, чем...", 1, 1, 1, 1) 
                        cho_seductively "{size=-4}Кончить...{/size}"
                        cho_seductively "{size=-2}Кончить правильно...{/size}"
                        cho_seductively "{size=-1}Кончить правильно{/size}...{w} сюда."
                        menu:
                            "-55 очков.-":
                                m "55 очков."
                                call cho_main("Что ж, хорошо.", 1, 1, 1, 1) 
                                call cho_main("{size=-4}(60 очков, довольно много.){/size}", 1, 1, 1, 1) 
                                ">Чоу соблазнительно покачивает попкой."
                                jump chof2hd
                            "-Ладно. 60 очков.-":
                                m "Хорошо, мисс Чанг. Я дам тебе 60 очков."
                                call cho_main("Хм. 60 очков, не плохо.", 1, 1, 1, 1) 
                                ">Чоу соблазнительно двигает задницей, затем она раздвигает ягодицы и обратно обхватывает ими твой член."
                                call cho_main("Профессор Дамблдор...", 1, 1, 1, 1) 
                                m "Да?"
                                call cho_main("Ваш член такой...", 1, 1, 1, 1) 
                                cho_sexy "Такой большой."
                                ">Ты медленно скользишь членом меж ягодиц Чоу."
                                call cho_main("Ммм. Спасибо, сэр.", 1, 1, 1, 1) 
                                jump chof2hd
                    "-Нет.-":
                        ">Ты шлепаешь своим членом по ее заднице."
                        m "Нет. Я так не думаю."
                        call cho_main("Что?", 1, 1, 1, 1) 
                        call cho_main("Что ж... я думаю, что сделаю это за 50 очков.", 1, 1, 1, 1) 
                        menu:
                            "-Да-":
                                m "Отлично. 50 очков. Ты умеешь торговаться, мисс Член."
                                call cho_main("Меня зовут Чанг. И да, я сейчас.", 1, 1, 1, 1) 
                                $ ravenclaw += 50
                                $ cho_mad +1
                                ">Чоу быстро двигает задницей."
                                jump chof2hd
                            "-Нет.-":
                                m "Нет."
                                call cho_main("Oх, хорошо.", 1, 1, 1, 1) 
                                ">Чоу отпускает свои ягодицы так, что они начинают хлопать."
                                ">Она наклоняется над твоим столом и начинаешь тискать упругую, голую попку девушки. "
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("......", 1, 1, 1, 1) 
                                call cho_main(".........", 1, 1, 1, 1) 
                                call cho_main("Этого достаточно, сэр?", 1, 1, 1, 1) 
                                menu:
                                    "-Да. Достаточно.-":
                                        ">Ты киваешь."
                                        m "Да. Это было прекрасно, мисс Чанг."
                                        ">Чоу быстро тянет юбку вниз, поглаживая ее."
                                        call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                        m "40 очков Когтеврану."
                                        $ ravenclaw += 40
                                        jump chof2end
                                    "-Продолжать.-":
                                        ">Ты игнорируешь ее вопрос и продолжаешь мять ее задницу и засовывая глубже меж ягодиц."
                                        call cho_main("Я знала, что вы не сможете устоять.", 1, 1, 1, 1) 
                                        ">Ты наклоняешься и легонько кусаешь ее."
                                        m "40 очков Когтеврану."
                                        call cho_main("Спасибо, профессор.", 1, 1, 1, 1) 
                                        $ ravenclaw += 40
                                        jump chof2end

        label chof2hd:
        ">Ты чувствуешь, как тепло распространяется по ее телу."
        ">Ты шлепаешь ее по упругим ягодицам."
        $ renpy.play('sounds/slap_02.mp3')
        show screen white
        "{size=+4}ШЛЕП!{/size}"
        #Shake the screen
        hide screen white 
        cho_seductive "Профессор!"
        ">Ты хватаешь за попку Чоу и обхватываешь ягодичками свой член."
        ">Твой член сильно пульсирует."
        call cho_main("Позвольте мне сделать всю работу.", 1, 1, 1, 1) 
        menu:
            "-Трахать ее ягодицы.-":
                ">Ты очарованно смотришь на попку девочки."
                ">Наконец, ты встаешь и хватаешь ее за задницу."
                call cho_main("Сэр, что вы делаете?", 1, 1, 1, 1) 
                ">Ты плотно сжимаешь ее ягодицы и начинаешь скользить членом меж них."
                cho_seductive "Х-хорошо, вы можете делать это, но я хочу пять дополнительных очков."
                menu: #[I'll give you 15] [No more очков]
                    "-Ладно.-":
                        ">Прежде чем ответить, ты пару раз проскользил членом."
                        m "Ладно, девочка."
                        call cho_main("Отлично, Профессор, но... но предупредите меня, перед тем как кончите.", 1, 1, 1, 1) 
                        ">Чоу трясет своей задницей из стороны в сторону."
                        ">Ты легонько укусил ее ягодичку."
                        cho_sexySurprise "..."
                        ">Ты очень сильно возбуждаешься. Ты шлепаешь Чоу."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=+4}(О боже!){/size}", 1, 1, 1, 1) 
                        ">Ты чувствуешь, как ягодицы Чоу сжались."
                        call cho_main("{size=+4}(От этого ему хорошо?){/size}", 1, 1, 1, 1) 
                        cho_sexy "{size=+4}(Моей киске щекотно от каждого толчка его члена...){/size}"
                        call cho_main("Профессор Дамбл-{w=.5}{nw}", 1, 1, 1, 1) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{sizE=+4}(Ох! Oх, черт!){/size}", 1, 1, 1, 1) 
                        ">Ты чувствуешь, что Чоу шатает, затем замечаешь ее руки между ног."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        m "Тебе нравится, не так ли?"
                        call cho_main("Нет! Нет, мне не нравится!", 1, 1, 1, 1) 
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        m "Лгунья!"
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}ШЛЕП!{/size}"
                        #Shake the screen
                        hide screen white 
                        ">Внезапно, ты чувствуешь, как ноги Чоу сильно дрожат."
                        call cho_main("Проф {w}проф-профессор! Я.{w=.75}{nw}", 1, 1, 1, 1) 
                        call cho_main("Профессор! Я-я.{w=.75}{nw}", 1, 1, 1, 1) 
                        call cho_main("Я{W=.5}-я КОНЧИЛА!", 1, 1, 1, 1) 
                        ">После ее оргазма, ты чувствуешь, как твои яички наполняются."
                        menu:
                            "-Кончить на ягодицы.-":
                                "Наконец, твой член извергается на ягодицы Чоу."
                                m "Держи, шлюха!"
                                #Genie cums.
                                cho_stupid"..."
                                cho_stupid"......"
                                "Твоя сперма брызгает на ягодицы."
                                cho_stupid"........."
                                "Когда последняя капля падает, ты облокачиваешься на спинку кресла."
                                m "(очков) Когтеврану."
                                cho_stupid"........даа."
                            "-Кончить в ее попку.-":
                                ">Когда ты толкаешь свой член вперед, ты чувствуешь ее дырочку."
                                ">Ты пытаешься засунуть член в ее дырочку."
                                cho_stupid "...Аххх"
                                ">Ты толкая вперед, борешься с ней."
                                cho_stupid "...Ахх....Oххх"
                                ">Наконец, твой член *появляется* в ее заднице."
                                cho_stupid "...аххх....оххх...охххх!"
                                ">Твой член взрывается и ты кончаешь в нее."
                                #Genie cums - find sprite
                                m "Ах! Ты ебанная шлюха!"
                                ">Ты чувствуешь как ее живот надувается."
                                cho_stupid "Gack!"
                                cho_stupid "ооомхх!"
                                $ renpy.play('sounds/pop02.mp3')
                                "Твой член выскакивает из бедной задницы девочки, и ты измученно, падаешь в кресло. "
                                show screen blktone
                                #Cho chibi is standing in the middle of the room.
                                call cho_main("Мне не хорошо... Что случилось?", 1, 1, 1, 1) 
                                menu:
                                    "-Я кончил тебе в попу.-":
                                        m "Ты потеряла сознание и я кончил в твою попу."
                                        cho _Shocked "..."
                                        cho _Shocked "......"
                                        cho _Shocked "........."
                                        cho_mouthfull "...."
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("Мне нужно идти!", 1, 1, 1, 1) 
                                        jump chof2end
                                    "-Я не знаю. Это было странно.-":
                                        m "Я не знаю. Это было странно."
                                        m "Но, ты получила очки."
                                        call cho_main("Спасибо, проф...", 1, 1, 1, 1) 
                                        cho_mouthfull "Проф-"
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("Думаю, мне нужно увидеть плаксу Миртел!", 1, 1, 1, 1) 
                                        $ renpy.play('sounds/run.mp3')
                                        jump chof2end
            "-Позволить ей.-":
                m "Как пожелаешь, мисс Чанг."
                ">Ты садишься на стул и Чоу прижимается к твоим коленям своими упругими ляшками."
                call cho_main("Так хорошо?", 1, 1, 1, 1) 
                ">Чоу медленно поднимает и опускает свою задницу."
                m "Великолепно, девочка."
                ">Чоу сжимает задницу вокруг твоего члена."
                ">Звездочка квиддича выгибает спину и подпрыгивает, касаясь своей дырочкой твоего члена  ."
                m "Ты дразнишь!"
                ">Ты поднес руку к ее ягодице."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}ШЛЕП!{/size}"
                #Shake the screen
                hide screen white 
                cho_sexySurprise "Профессор!"
                ">Чоу подпрыгивает еще пару раз, прежде чем остановиться."
                call cho_main("{size=-4}(О боже...я не могу поверить, что делаю это.){/size}", 1, 1, 1, 1) 
                call cho_main("{size=-4}(Моя попка такая скользкая...){/size}", 1, 1, 1, 1) 
                call cho_main("Профессор Дамблдор, с-скажите мне, когда вы-", 1, 1, 1, 1) 
                ">Ты уже чувствуешь, что скоро кончишь."
                ">Ты несколько раз шлепаешь по заднице Чоу..."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}ШЛЕП!{/size}"
                #Shake the screen
                hide screen white 
                call cho_main("Профессор Дамблдор, скажите мне, когда вы-{w=.75}{nw}", 1, 1, 1, 1) 
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}ШЛЕП!{/size}"
                #Shake the screen
                hide screen white 
                call cho_main("Профессор Дамблдор, скажите мне, когда вы-КОНЧИТЕ!", 1, 1, 1, 1) 
                call cho_main("{size=+4}(Ох черт!){/size}", 1, 1, 1, 1) 
                ">Чоу сползает обратно на колени и начинает двигаться стимулируя член ягодицами."
                cho_arounsed "Профессор..."
                ">Ты видишь головку члена, как она выскакивает."
                ">Ты понимаешь, что уже кончишь..."
                menu:
                    "-Кончить.-":
                        ">Твой член извергается на задницу Чоу."
                        m "Черт возьми, чертовка!"
                        #Genie cums. - find chibi
                        cho_wideEyes "О боже... Что такое?"
                        cho_wideEyesLookingBack "{size=+2}Вы кончаете?{/size}"
                        ">Твоя сперма брызжет между ягодицами Чоу."
                        call cho_main("О боже...", 1, 1, 1, 1) 
                        ">Ты покачиваешь член и чувствуешь, как последняя капля упала на ее задницу."
                        call cho_main("...", 1, 1, 1, 1) 
                        call cho_main("Моя задница вся в ней!", 1, 1, 1, 1) 
                        call cho_main("Она такая липкая.", 1, 1, 1, 1) 
                        cho_sexy "Так липко. Вы должны мне дополнительно 10 очков!"
                        menu:
                            "-Да.-":
                                m "Да, конечно. 10 дополнительных очков Когтеврану."
                                $ ravenclaw += 10
                                call cho_main("Посмотрите на этот беспорядок!", 1, 1, 1, 1) 
                                call cho_main("Я никогда не приведу себя в порядок...", 1, 1, 1, 1) 
                                call cho_main("{sIze=-2}...Спасибо, сэр.{/size}", 1, 1, 1, 1) 
                                ">Чоу встает. Сперма стекает по ее ногам."
                                call cho_main("{size=-4}(Так много...){/size}", 1, 1, 1, 1) 
                                cho_happy "{size=-4}(По любому, Гермиона не смогла заставить, его так кончить.){/size}"
                                ">Чоу натягивает юбку и проглаживает, появляющиеся темные пятна."
                                call cho_main("Это должно быть нормально.", 1, 1, 1, 1) 
                                m "Да, конечно. Хотя, на всякий случай, тебе стоит избегать старост..."
                                jump chof2end
                            "-Сожалею.-":
                                m "Ты заставила меня кончить."
                                call cho_main("!!!", 1, 1, 1, 1) 
                                m "Ты должна быть более осторожна."
                                call cho_main("Вы, наверное, шутите!", 1, 1, 1, 1) 
                                call cho_main("Ваша вонючая сперма на моей заднице! Я пахну как... как... как Гермиона!", 1, 1, 1, 1) 
                                m "Сожалею."
                                call cho_main("Вы-грязный, старый волшебник!", 1, 1, 1, 1) 
                                "Чоу натягивает юбку, на ней видны темные пятна."
                                $ cho_mad +5
                                jump chof2end
                    "-Предупредить.-":
                        m "Я собираюсь кончить!"
                        call cho_main("Серьезно?", 1, 1, 1, 1) 
                        ">Внезапно, ты чувствуешь, что она начинает быстрее шевелить задницей."
                        ">Твой член охвачен ее ягодицами и плотно прижат к ее девственной киске."
                        ">Чоу качает бедрами вперед и назад."
                        cho_sexy "Кончайте, Профессор!"
                        ">Ты чувствуешь членом, как ее киска потекла."
                        ">Наконец, ты хватаешь за бедра девочки и яростно кончаешь."
                        m "Ах, шлю-{w=.75}{nw}"
                        cho_sexy "Заткнитесь и кончайте, мерзкий старый волшебник!"
                        m "Ах, шлю-хааааа!"
                        #Genie cums. - find chibi
                        ">Ты кончая, попадаешь на стол, выстреливая на ноги Чоу."
                        cho_sexy "Так много спермы!"
                        ">Уставший, ты падаешь в кресло."
                        m "Хорошая работа, мисс Чанг."
                        call cho_main("Спасибо, профессор.", 1, 1, 1, 1) 
                        ">Чоу тщательно расправляет юбку."
                        ">Затем она наклоняется к твоему столу и проводит пальцем по твоей теплой сперме."
                        call cho_main("Я думаю, у вас тут грязно...", 1, 1, 1, 1) 
                        ">После, она облизывает свой палец."
                        call cho_main("Уупс...", 1, 1, 1, 1) 
                        jump chof2end

    label chof2end:
    #cho walking out
    $ renpy.play('sounds/door.mp3')
    hide screen cho_chang
    jump day_main_menu
    
    
    
label cho_favor_3:

        m "Мисс Чанг, ты знаешь, что такое минет?"
        call cho_main("?", 1, 1, 1, 1) 
        call cho_main("Вы хотите, чтобы я положила в свой рот ваш...", 1, 1, 1, 1) 
        call cho_main("Вы хотите, чтобы я положила в рот ваш... пенис?", 1, 1, 1, 1) 
        m "Я думал, ты не хочешь отставать от мисс Грейнджер."
        call cho_main("Вы имеете ввиду, что она-", 1, 1, 1, 1) 
        menu:
            "-Конечно-":
                m "Полагаю, Мисс Грейнджер более конкурентоспособна, чем ты."
                call cho_main("...", 1, 1, 1, 1) 
                call cho_main("(Не могу в это поверить.)", 1, 1, 1, 1) 
                call cho_main("(Какая...)", 1, 1, 1, 1) 
                call cho_main("(Какая... тупая шлюха.)", 1, 1, 1, 1) 
                call cho_main("Я тоже могу это сделать!", 1, 1, 1, 1) 
                call cho_main("Я думаю возьму за 60 очков.", 1, 1, 1, 1) 
                menu:
                    "-Я дам тебе 70 очков-":
                        m "Я дам тебе 70 очков."
                        call cho_main("Серьезно?", 1, 1, 1, 1) 
                        call cho_main("Серьезно? 70 очков?", 1, 1, 1, 1) 
                        call cho_main("Хорошо.", 1, 1, 1, 1) 
                        $ cho_mad -= 1
                        $ cho_points = 70
                        jump cho_favor_3_1
                        
                    "-Хорошо, 60-":
                        m "60, вполне не плохо."
                        call cho_main("Хорошо.", 1, 1, 1, 1) 
                        $ cho_points = 60
                        jump cho_favor_3_1
                    
                    "-Мисс Грейнджер берет за это 55 очков...-":
                        m "Мисс Грейнджер берет за это 55 очков..."
                        call cho_main("55?...", 1, 1, 1, 1) 
                        call cho_main("55?... почему она-", 1, 1, 1, 1) 
                        call cho_main("Я сделаю это за 50!", 1, 1, 1, 1) 
                        $ cho_points = 50
                        jump cho_favor_3_1
                        
            "-Конечно нет-":
                m "Не будь сумасшедшей. Конечно нет."
                m "У мисс Грейнджер есть стандарты."
                call cho_main("...", 1, 1, 1, 1) 
                m "Она просто зарабатывала много очков в последнее время."
                call cho_main("Она?", 1, 1, 1, 1) 
                m "Ну, она лучшая ученица в школе..."
                call cho_main("Я сделаю это за 60 очков.", 1, 1, 1, 1) 

                menu:
                    "-Я дам тебе 70 очков-":
                        m "Я дам тебе 70 очков."
                        call cho_main("Серьезно?", 1, 1, 1, 1) 
                        call cho_main("Серьезно? 70 очков?", 1, 1, 1, 1) 
                        call cho_main("Ладно.", 1, 1, 1, 1) 
                        $ cho_mad -= 1
                        $ cho_points = 70
                        jump cho_favor_3_1
                        
                    "-Хорошо, 60-":
                        m "60, вполне не плохо."
                        call cho_main("Хорошо.", 1, 1, 1, 1) 
                        $ cho_points = 60
                        jump cho_favor_3_1
                    
                    "-Ты получишь 40 очков-":
                        m "Я дам 40 очков."
                        call cho_main("40! Я получала и больше... за другие вещи, которые вам продаю.", 1, 1, 1, 1) 
                        call cho_main("Я сделаю за 50 очков.", 1, 1, 1, 1) 
                        
                        menu:
                            "-Хорошо-":
                                m "Договорились."
                                $ cho_points = 50
                                jump cho_favor_3_1
                            
                            "-Не получится-":
                                m "Не получится, девочка. Ты не стоишь больше 40."
                                call cho_main("Ладно!", 1, 1, 1, 1) 
                                $ cho_mad += 10
                                m "И постарайся не выглядеть такой несчастной."
                                $ cho_mad += 10
                                call cho_main("(Мудак.)", 1, 1, 1, 1) 
                                call cho_main("(А как я вообще должна это делать?)", 1, 1, 1, 1) 
                                $ cho_points = 40
                                jump cho_favor_3_1

        m "Я предполагаю, что ты знакома с древним китайским искусством 'SukiSuki'."
        call cho_main("Что?", 1, 1, 1, 1) 
        m "Я хочу минет."
        if cho_mad >= 6:
            jump cho_mad_blowjob
        call cho_main("Хорошо. Но я делаю это, чтобы помочь своему факультету...", 1, 1, 1, 1) 
        call cho_main("И, я хочу [cho_points] очков.", 1, 1, 1, 1) 
        m "Да, да. Соси."
        jump cho_favor_3_1

label cho_favor_3_1:

    call cho_main("Эм...", 1, 1, 1, 1) 
    call cho_main("Эм... Что мне делать...", 1, 1, 1, 1) 
    
    menu:
        "-Ты шутишь?-":
            m "Ты шутишь?"
            call cho_main("Я не шучу! Я не шлюха, как Гермиона.", 1, 1, 1, 1) 
            m "Просто соси мой член, как леденец."
            call cho_main("(Как КОНФЕТА? Фу. Не получится старый, грязный... он не как конфета...)", 1, 1, 1, 1) 
            call cho_main("([cho_points]! [cho_points]!)", 1, 1, 1, 1) 
            "Чоу неуклюже падает на колени и открывает рот, высовывая язык."
            call cho_main("Как долго профессор?", 1, 1, 1, 1) 
            "Ты чувствуешь, как член дергается под одеждой при виде студентки на коленях."
            m "Да...это будет быстро."
            "Ты высовываешь член из-под мантии и встаешь над Чоу."
            "Эротическое зрелище заставляет прякулят сочиться с кончика твоего члена."
            "Чоу вздрагивает, когда твой член показывается перед ней."
            call cho_main("Будте! Будте осторожны!", 1, 1, 1, 1) 
            "Ты косаешься кончиком члена ее носа."
            call cho_main("ааххх...", 1, 1, 1, 1) 
            call cho_main("'О ахое?(Что такое?)", 1, 1, 1, 1) 
            "Изо рта Чоу капают слюни."
            "Ты направляешь свой член ей в рот."
            call cho_main("(Фуу. странный вкус...)", 1, 1, 1, 1) 
            m "Да... Так лучше."
            "Ты даешь отдохнуть своему члену. Греясь во рту Чоу."
            call cho_main("Хммм.", 1, 1, 1, 1) 
            m "Не сдавайся."
            "Ты медленно толкаешь глубже свой член."
            call cho_main("Хммм!", 1, 1, 1, 1) 
            "Ты чувствуешь невероятные ощущения."
            "Внезапно, ты упираешься в горло."
            call cho_main("*cough* *ack!*", 1, 1, 1, 1) 
            "Ты тянешь свой член назад с толстым потоком слизи и слюны изо рта Чоу."
            call cho_main("Блэ!", 1, 1, 1, 1) 
            call cho_main("Блэ!...", 1, 1, 1, 1) 
            call cho_main("О боже!", 1, 1, 1, 1) 
            call cho_main("Простите, Профессор!", 1, 1, 1, 1) 
            
            menu:
                "-15 очков-":
                    m "Ладно! Просто сделай это!"
                    call cho_main("Хорошо.", 1, 1, 1, 1) 
                    "Чоу наклоняется и начинает быстро двигать головой над членом."
                    "Она пытается скрыть, что она не опытна в этом, но постоянные покачивания заставляют тебе кончить."
                    m "Ты ебанная шлюха!"
                    "Ты кончаешь ей в рот."
                    "Ее щеки начинают раздуваться."
                    "Когда ты закончил, твой член выскакивает изо рта бедной девочки, оставив ее с полным ртом."
                    call cho_main("Хмм!", 1, 1, 1, 1) 
                    "Чоу ищет место, где сплюнуть."

                "-5 очков-":
                    m "Я дам тебе 5 очков."
                    call cho_main("... Договорились.", 1, 1, 1, 1) 
                    "Чоу наклоняется вперед и начинает быстро качать головой над членом."
                    "Она пытается скрыть, что она не опытна в этом, но постоянные покачивания заставляют тебе кончить."
                    m "Да, возьми его!"
                    "Ты кончаешь ей в рот."
                    "Ее щеки начинают раздуваться."
                    "Когда ты закончил, твой член выскакивает изо рта бедной девочки, оставив ее с полным ртом."
                    call cho_main("Хмм!", 1, 1, 1, 1) 
                    "Чоу ищет место, где сплюнуть."

                    menu:
                        "-Дать ей пустой бокал-":
                            "Единственный предмет в твоем кабинете-бокал, который остался после последней встречи с Северусом."
                            "Ты даешь бокал Чоу."
                            call cho_main("Блэ..кх...", 1, 1, 1, 1) 
                            "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                            "Через несколько мгновений он полностью заполнен."
                            call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                            "#получен предмет [Cum Goblet]"
                            m "Да... что ж, [cho_points] очков Когтеврану."
                            jump end_cho_event

                        "-Заставить проглотить.-":
                            m "Эй, я заплачу дополнительно, если ты проглотишь."
                            call cho_main("Охои?!(Проглотить?!)", 1, 1, 1, 1) 
                            m "Ты хочешь очки, не так ли?"
                            call cho_main("(Ах, старый извращенец!)", 1, 1, 1, 1) 
                            call cho_main("(Меня сейчас стошнит!)", 1, 1, 1, 1) 
                            "Глаза Чоу становятся красными."
                            $ renpy.play('sounds/gulp.mp3')
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("Блэг...", 1, 1, 1, 1) 
                            call cho_main("Все...", 1, 1, 1, 1) 
                            call cho_main("Все... все, готово.", 1, 1, 1, 1) 
                            m "Отлично. [cho_points] очков Когтеврану."
                            call cho_main("Спасибо, Профессор-", 1, 1, 1, 1) 
                            $ renpy.play('sounds/burp.mp3')
                            call cho_main("...", 1, 1, 1, 1) 
                            jump end_cho_event
                "-Пошла ты!-":
                    m "(Что за наглая сучка!)"
                    m "Жадная шлюха!"
                    "Ты хватаешь член и дрочишь."
                    "Некоторое время спустя, ты кончаешь на Чоу."
                    call cho_main("Ч-что?...", 1, 1, 1, 1) 
                    m "[cho_points] очков Когтеврану. А теперь убирайся из моего кабинета."
                    call cho_main("Но я не могу пойти в таком виде!", 1, 1, 1, 1) 
                    m "Уходи."
                    call cho_main("...", 1, 1, 1, 1) 
                    call cho_main("...Ладно!", 1, 1, 1, 1) 
                    $ cho_mad += 10
                    #Cho storms out.
                    m "Сука..."
                    jump end_cho_event
            
        "-Положи мой член себе в рот.-":
            m "Просто положи мой член в свой рот."
            call cho_main("Я знаю!", 1, 1, 1, 1) 
            call cho_main("Я знаю! Но, после что...", 1, 1, 1, 1) 
            m "Ты его сосешь и касаешься язычком."
            call cho_main("(Касаться своим языком? фу. звучит мерзко...)", 1, 1, 1, 1) 
            call cho_main("([cho_points]! [cho_points]!)", 1, 1, 1, 1) 
            "Чоу неуклюже падает на колени и открывает рот, высовывая язык."
            call cho_main("Вы можете положить его в рот...", 1, 1, 1, 1) 
            "Ты чувствуешь, как твой член возбуждается."
            m "Что ж, приступим..."
            "Ты высовываешь член из-под мантии и встаешь над Чоу."
            "Не много предэякулята сочится из твоего члена."
            "Чоу вздрагивает, когда твой член показывается перед ней."
            call cho_main("Будте осторожны!", 1, 1, 1, 1) 
            "Ты дотрагиваешься кончиком члена ее носа."
            call cho_main("Ахх...", 1, 1, 1, 1) 
            call cho_main("Что такое?)", 1, 1, 1, 1) 
            "Изо рта Чоу капают слюни."
            "Ты засовываешь свой член ей в рот."
            call cho_main("(Фуу. странный вкус...)", 1, 1, 1, 1) 
            m "Даа... Так лучше."
            "Ты даешь отдохнуть своему члену. Греясь во рту Чоу."
            call cho_main("Хмм.", 1, 1, 1, 1) 
            m "Держись."
            "Ты медленно толкаешь член глубже."
            call cho_main("Хммм!", 1, 1, 1, 1) 
            "Невероятные ощущения пронзают тебя."
            "Внезапно, ты упираешься в горло девочки."
            call cho_main("*cough* *ack!*", 1, 1, 1, 1) 
            "Ты тянешь свой член назад с толстым потоком слизи и слюны изо рта Чоу."
            call cho_main("Блэ!", 1, 1, 1, 1) 
            call cho_main("Блэ!...", 1, 1, 1, 1) 
            call cho_main("О боже!", 1, 1, 1, 1) 
            call cho_main("Простите, профессор!", 1, 1, 1, 1) 
            
            menu:
                "-Этого, наверное, достаточно-":
                    m "Возможно, я зашел слишком далеко."
                    jump end_cho_event

                "-Продолжать-":
                    m "Ты не получишь своих очков, если не закончишь."
                    call cho_main("Простите, профессор!", 1, 1, 1, 1) 
                    m "Все в порядке, девочка."
                    "Ты засовываешь член обратно ей в рот."
                    "Чоу начинает двигать своим языком гораздо лучше, чем в прошлый раз."
                    "К твоему удивлению, мысль о ее неопытности заставляет тебя кончить."
                    
                    menu:
                        "-Кончить-":
                            "#Джинн кончает в рот Чоу."
                            call cho_main("Хммм!", 1, 1, 1, 1) 
                            m "За счет прибыли Диснея..."
                            call cho_main("Хмм!...", 1, 1, 1, 1) 
                            call cho_main("Хммм!...Хммм!", 1, 1, 1, 1) 
                            "В панике, Чоу пытается проглотить сперму, но у нее не получается"
                            call cho_main("Блэг!", 1, 1, 1, 1) 
                            "Твоя сперма выливается из ее рта."
                            call cho_main("(О боже... это так противно...)", 1, 1, 1, 1) 
                            call cho_main("Вы должны мне дополнительные очки!", 1, 1, 1, 1) 

                            menu:
                                "-Ладно 5 дополнительных очков-":
                                    m "Хорошо, мисс Чанг. [cho_points] очков Когтеврану."
                                    call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                    $ cho_points += 5
                                    jump end_cho_event

                                "-Что? Конечно нет.-":
                                    m "Что? Конечно же нет."
                                    call cho_main("Это нечестно!", 1, 1, 1, 1) 
                                    m "Соглашайся или уходи, мисс Член."
                                    call cho_main("Меня зовут Чанг, старый придурок!", 1, 1, 1, 1) 
                                    m "Ты хочешь очки или нет?"
                                    call cho_main("Да, пожалуйста.", 1, 1, 1, 1) 
                                    m "[cho_points] очков Когтеврану."
                                    jump end_cho_event
                        "-Предупредить ее-":
                            m "Я сейчас кончу!"
                            call cho_main("Хм!", 1, 1, 1, 1) 
                            call cho_main("Хм!...Блэ!", 1, 1, 1, 1) 
                            "Чоу вытаскивает твой член изо рта."
                            "Ты ждешь, пока она закончит с этим, а вместо этого она просто сидит."
                            call cho_main("Я хочу еще 15 очков.", 1, 1, 1, 1) 
                            m "Что?!"
                            call cho_main("Вы сказали, что я должна сосать. Если вы хотите кончить, то я хочу еще 15 очков.", 1, 1, 1, 1) 
                            
                            menu:
                                "-15 очков-":
                                    m "Ладно! Заканчивай с этим!"
                                    call cho_main("Хорошо.", 1, 1, 1, 1) 
                                    "Чоу наклоняется и качает своей головой."
                                    "Она пытается скрыть, что она не опытна в этом, но постоянные покачивания заставляют тебя кончить."
                                    m "Ты ебанная шлюха!"
                                    "Ты кончаешь в рот Чоу."
                                    "Ее щеки начинают раздуваться."
                                    "Когда ты закончил, твой член выскакивает изо рта бедной девочки, оставив ее с полным ртом."
                                    call cho_main("Хммм!", 1, 1, 1, 1) 
                                    "Чоу ищет место, чтоб сплюнуть."

                                "-5 очков-":
                                    m "Я дам тебе 5 очков."
                                    call cho_main("... Договорились.", 1, 1, 1, 1) 
                                    "Чо наклоняется вперед и начинает быстро качать головой над членом."
                                    "Она пытается скрыть, что она не опытна в этом, но постоянные покачивания заставляют тебе кончить."
                                    m "Да, возьми его!"
                                    "Ты кончаешь ей в рот."
                                    "Ее щеки начинают раздуваться."
                                    "Когда ты закончил, твой член выскакивает изо рта бедной девочки, оставив ее с полным ртом."
                                    call cho_main("Хмм!", 1, 1, 1, 1) 
                                    "Чоу ищет место, где сплюнуть."

                                    menu:
                                        "-Дать ей пустой бокал-":
                                            "Единственный предмет в твоем кабинете-бокал, который остался после последней встречи с Северусом."
                                            "Ты даешь бокал Чоу."
                                            call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                            "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                                            "Через несколько мгновений он полностью заполнен."
                                            call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                            "#получен предмет [Cum Goblet]"
                                            m "Да... что ж, [cho_points] очков Когтеврану."
                                            jump end_cho_event
                                        "-Заставить проглотить.-":
                                            m "Эй, я заплачу дополнительно, если ты проглотишь."
                                            call cho_main("Охои?!(Проглотить?!)", 1, 1, 1, 1) 
                                            m "Ты хочешь очки, не так ли?"
                                            call cho_main("(Ах, старый извращенец!)", 1, 1, 1, 1) 
                                            call cho_main("(Меня сейчас стошнит!)", 1, 1, 1, 1) 
                                            "Глаза Чоу становятся красными."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                            call cho_main("Все...", 1, 1, 1, 1) 
                                            call cho_main("Все... все, готово.", 1, 1, 1, 1) 
                                            m "Отлично. [cho_points] очков Когтеврану."
                                            call cho_main("Спасибо, професс-", 1, 1, 1, 1) 
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1) 
                                            jump end_cho_event
                                "-Пошла ты!-":
                                    m "(Вот сучка!)"                        
                                    m "Жадная шлюха!"
                                    "Ты хватаешь член и дрочишь."
                                    "Некоторое время спустя, ты кончаешь на Чоу."
                                    call cho_main("Ч-что?...", 1, 1, 1, 1) 
                                    m "[cho_points] очков Когтеврану. А теперь убирайся из моего кабинета."
                                    call cho_main("Но я не могу пойти в таком виде!", 1, 1, 1, 1) 
                                    m "Уходи."
                                    call cho_main("...", 1, 1, 1, 1)
                                    call cho_main("...Ладно!", 1, 1, 1, 1) 
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Сучка..."
                                    jump end_cho_event
        "-Сделай это медленно-":
            m "Просто сделай это медленно."
            call cho_main("Спасибо, профессор Дамблдор.", 1, 1, 1, 1) 
            call cho_main("Я просто... Вы знаете, пососу его?", 1, 1, 1, 1) 
            m "Да. Думай об этом как о конфете."
            call cho_main("(Как о конфете? Думаю, это поможет...)", 1, 1, 1, 1) 
            call cho_main("(Надо забыть, что у меня во рту старый член волшебника...)", 1, 1, 1, 1) 
            call cho_main("([cho_points]! [cho_points]!)", 1, 1, 1, 1) 
            "Чоу неуклюже падает на колени и открывает рот, высовывая язык."
            call cho_main("А овофо офефо?(Вам хорошо, профессор?)", 1, 1, 1, 1) 
            "Ты нежно гладишь щеки Чоу."
            call cho_main("(Вау... это приятно.)", 1, 1, 1, 1) 
            $ cho_mad -= 1
            m "Да, девочка... так будет лучше."
            "Ты высовываешь свой твердый член и встаешь над Чоу."
            "Эротическое зрелище вызывает немного предэякулят, который сочиться из кончика твоего члена."
            "Глаза Чоу вздрагивают, когда твой член качается над лицом."
            "Ее длинные азиатские ресницы быстро моргают."
            "Не много предэякулята падает ей на лицо."
            call cho_main("Будьте осторожны!", 1, 1, 1, 1) 
            "Ты медленно дотрагиваешься кончиком члена к ее языку."
            call cho_main("Ахх...", 1, 1, 1, 1) 
            call cho_main("'О эо?(Что это?)", 1, 1, 1, 1) 
            "У Чоу изо рта текут слюни."
            "Ты начинаешь тереть членом о язык."
            call cho_main("(Странный вкус...)", 1, 1, 1, 1) 
            m "Даа... так лучше."
            "Ты даешь отдохнуть своему члену. Греясь во рту Чоу."
            call cho_main("Хмм.", 1, 1, 1, 1) 
            m "Шшш. Все хорошо, девочка."
            "Ты медленно скользишь членом у нее во рту."
            call cho_main("Хмм....", 1, 1, 1, 1) 
            "Ты чувствуешь невероятные ощущения."
            "Ты остановился на мгновение."
            call cho_main("(Это не плохо...)", 1, 1, 1, 1) 
            "Ты высовываешь член изо рта Чоу."
            call cho_main("Ммм.", 1, 1, 1, 1) 
            call cho_main("Ммм....", 1, 1, 1, 1) 
            "Чоу широко открывает рот, позволяя слюням капать на пол."
            
            menu:
                "-Этого, наверное, достаточно-":
                    m "Достаточно."
                    m "[cho_points] очков Когтеврану."
                    jump end_cho_event

                "-Продолжить-":
                    m "Мы почти закончили, девочка."
                    call cho_main("(Это определенно стоит [cho_points]...)", 1, 1, 1, 1) 
                    "Ты нежно всовываешь свой член в ее рот."
                    "Язык Чоу извивается на головке твоего члена."
                    "К твоему удивлению, ее язык находит дырочку в твоем члене и ты вот-вот кончишь."
                    
                    menu:
                        "-Кончить-":
                            #Genie cums in Cho's mouth.
                            call cho_main("Хмммм!", 1, 1, 1, 1) 
                            m "Х-хорошая... девочка..."
                            call cho_main("Хмммм!...", 1, 1, 1, 1) 
                            call cho_main("Хмммм!...Ммммм!", 1, 1, 1, 1) 
                            "В панике, Чоу пытается проглотить сперму, но у нее не получается."
                            call cho_main("Blehg!", 1, 1, 1, 1) 
                            "Твоя сперма вытекает из ее рта."
                            call cho_main("(О боже... ее так много..)", 1, 1, 1, 1) 
                            call cho_main("Много!", 1, 1, 1, 1) 
                            call cho_main("Много! Предупредите меня в следующий раз, хорошо?", 1, 1, 1, 1) 
                            m "Это было здорово. [cho_points] очков Когтеврану."
                            jump end_cho_event

                        "-Предупредить-":
                            m "Я скоро кончу!"
                            call cho_main("Хм?", 1, 1, 1, 1) 
                            call cho_main("Хм?...Blehrg!", 1, 1, 1, 1) 
                            "Чоу выплевывает твой член изо рта."
                            "Ты ждешь пока она закончит с этим, но она просто смотрит на тебя, улыбаясь."
                            call cho_main("Если вы дадите 5 дополнительных очков я все проглочу.", 1, 1, 1, 1) 
                            m "Ты все проглотишь?"
                            call cho_main("Ну, конечно. Я имею в виду, это отвратительно, но мне нужны очки...", 1, 1, 1, 1) 
                            
                            menu:
                                "-15 очков-":
                                    m "Я дам тебе 15 очков."
                                    call cho_main("Что? Серьезно?", 1, 1, 1, 1) 
                                    call cho_main("Хорошо.", 1, 1, 1, 1) 
                                    "Чоу быстро хватает твой член и берет его в рот."
                                    "Ее язык обхватывает твою головку и начинает извиваться."
                                    call cho_main("(Ммм. Это как конфета!)", 1, 1, 1, 1) 
                                    m "Великая сила Серого Черепа!(отсылка к He-Man and the Masters of the Universe 1983-1985)"
                                    #Genie cums in Cho's mouth.
                                    "Твой член начинает пульсировать."
                                    "Внезапно, ты хватаешь за голову Чоу и начинаешь яростно кончать ей в рот."
                                    "Ты чувствуешь, как она пытается проглотить, но ее щеки начинают раздуваться еще больше."
                                    "Когда ты закончил, вынул свой член."
                                    call cho_main("Хммммм!", 1, 1, 1, 1) 
                                    "Чоу ищет место куда сплюнуть."

                                    menu:
                                        "-Дать ей пустой бокал-":
                                            "Единственный предмет в твоем кабинете был бокал, оставшийся после последней встречи с Северусом."
                                            "Ты даешь Чоу пустой бокал."
                                            call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                            "Сперма медленно стекает изо рта девочки в бокал."
                                            "Через несколько мгновений он полностью заполнен."
                                            call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                            #gain item [Cum Goblet]
                                            m "Да... что ж, [cho_points] очков Когтеврану."
                                            jump end_cho_event
                                        "-Заставить проглотить.-":
                                            m "Эй, я заплачу дополнительно очков, если ты проглотишь."
                                            call cho_main("Огоий?!(Проглотить?!)", 1, 1, 1, 1) 
                                            m "Ты хочешь очки, не так ли?"
                                            call cho_main("(Меня серьезно сейчас стошнит...)", 1, 1, 1, 1) 
                                            call cho_main("Мм хммм!", 1, 1, 1, 1) 
                                            "Глаза Чоу становятся красными."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Блэ...", 1, 1, 1, 1) 
                                            call cho_main("...", 1, 1, 1, 1) 
                                            call cho_main("...Все.", 1, 1, 1, 1) 
                                            m "Отлично. [cho_points] очков Когтеврану."
                                            call cho_main("Спасибо, профес-", 1, 1, 1, 1) 
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1) 
                                            jump end_cho_event
                                "-5 очков-":
                                    m "Конечно, я дам тебе 5 очков."
                                    call cho_main("Дадите?", 1, 1, 1, 1) 
                                    "Чоу наклоняется и качает головой."
                                    "Она пытается сделать все отлично, но неопытный рот ее подводит."
                                    "Вскоре, ты чувствуешь, как сперма брызгает из члена."
                                    m "Это волшебно!"
                                    #Genie cums in Cho's mouth.
                                    Cho_WideEyes"!..."
                                    Cho_WideEyes"(Что?)"
                                    "Щеки Чоу раздуваются из-за твоей спермы."
                                    "Когда ты закончил, твой член выскакивает из ее рта."
                                    call cho_main("Хмм!", 1, 1, 1, 1) 
                                    "Чоу ищет место, чтоб сплюнуть."

                                    menu:
                                        "-Дать ей пустой бокал-":
                                            "Единственный предмет в твоем кабинете был бокал, оставшийся после последней встречи с Северусом."
                                            "Ты даешь Чоу пустой бокал."
                                            call cho_main("Блэгх...", 1, 1, 1, 1) 
                                            "Сперма медленно стекает изо рта девочки в бокал."
                                            "Через несколько мгновений он полностью заполнен."
                                            call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                            #gain item [Cum Goblet]
                                            m "Да... что ж, [cho_points] очков Когтеврану."
                                            jump end_cho_event
                                        "-Заставить проглотить.-":
                                            m "Эй, я заплачу дополнительно очков, если ты проглотишь."
                                            call cho_main("Огоий?!(Проглотить?!)", 1, 1, 1, 1) 
                                            m "Ты хочешь очки, не так ли?"
                                            call cho_main("(Меня серьезно, сейчас стошнит...)", 1, 1, 1, 1) 
                                            call cho_main("Мм хммм!", 1, 1, 1, 1) 
                                            "Глаза Чоу становятся красными."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Блэ...", 1, 1, 1, 1) 
                                            call cho_main("...", 1, 1, 1, 1) 
                                            call cho_main("...Все.", 1, 1, 1, 1) 
                                            m "Отлично. [cho_points] очков Когтеврану."
                                            call cho_main("Спасибо, профес-", 1, 1, 1, 1) 
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1) 
                                            jump end_cho_event
                                "-Пошла ты!-":
                                    m "(Я не знал, что Член-еврейское имя?!)"
                                    m "Жадная шлюха!"
                                    "Ты хватаешь член."
                                    m "После нескольких быстрых фрикций, ты кончаешь."
                                    #Genie cums.
                                    "Ты кончаешь на Чоу, некошерной спермой."
                                    call cho_main("Ч-что?...", 1, 1, 1, 1) 
                                    m "[cho_points] очков Когтеврану. А теперь убирайся из моего кабинета."
                                    call cho_main("Но я не могу идти в таком виде!", 1, 1, 1, 1) 
                                    m "Уходи."
                                    call cho_main("...", 1, 1, 1, 1) 
                                    call cho_main("...Ладно!", 1, 1, 1, 1) 
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Сучка..."
                                    jump end_cho_event

label cho_favor_3_2:

        m "Мисс Чанг, я бы хотел, чтобы ты сделала мне еще один минет."
        if cho_mad > 10:
            jump cho_mad_blowjob
            
        call cho_main("[cho_points] очков.", 1, 1, 1, 1) 
        m "Конечно."
        "Чоу падает на колени и терпеливо ждет."
        call cho_main("Когда будете готовы...", 1, 1, 1, 1) 
        m "Открой рот."
        "Чоу открывает рот и высовывает язык."
        call cho_main("Я ооа...(Я готова...)", 1, 1, 1, 1) 
        "Твой член возбудился."
        m "Вот почему я начал преподавать..."
        "Ты высовываешь свой член из-под мантии и стоишь над Чоу."
        "Изо рта Чоу капают слюни."
        "Ты пару раз хлопнул членом по ее языку."
        call cho_main("(Что он делает...)", 1, 1, 1, 1) 
        m "Даа... Так лучше."
        "Ты даешь отдохнуть своему члену. Греясь во рту Чоу."
        call cho_main("Хммм.", 1, 1, 1, 1) 
        m "Держись."
        "Ты медленно толкаешь член в горло девочки."
        call cho_main("Хммм!", 1, 1, 1, 1) 
        "Ты чувствуешь невероятные ощущения."
        "Внезапно, ты уперся в него."
        call cho_main("*cough* *ack!*", 1, 1, 1, 1) 
        "Ты высовываешь член изо рта Чоу."
        call cho_main("Bleh!", 1, 1, 1, 1) 
        call cho_main("Bleh!...", 1, 1, 1, 1) 
        call cho_main("О боже!", 1, 1, 1, 1) 
        call cho_main("Простите, профессор!", 1, 1, 1, 1) 
        menu:
                    "-Быть добрым-":
                        m "Это совершенно нормально, мисс Чанг."
                        m "Мы рассмотрим часть твоего образования."
                        call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                        "Чоу обхватывает твой член своими губами."
                        "Затем, она берет его в рот."
                        "Ты чувствуешь, как она медленно засовывает его себе в горло."
                        m "Очень хорошо. Расслабься."
                        call cho_main("Мммм.", 1, 1, 1, 1) 
                        "Чоу пытается расслабить свое горло."
                        m "Ммм. Хорошо. Попробуй заглотнуть."
                        call cho_main("*GuL* *Gul* *Glug*", 1, 1, 1, 1) 
                        "Наконец, ты чувствуешь, как головка члена упирается в ее горло."
                        "Ты чувствуешь невероятные ощущения."
                        call cho_main("...", 1, 1, 1, 1) 
                        call cho_main("......", 1, 1, 1, 1) 
                        call cho_main("..........", 1, 1, 1, 1) 
                        call cho_main("*cough* *sputTer*! У меня почти получилось.", 1, 1, 1, 1) 
                        call cho_main("Дайте попробовать еще раз.", 1, 1, 1, 1) 
                        "Чоу обратно засовывает его в рот."
                        "Ты решительно смотришь ей в глаза."
                        call cho_main("*Gul* *gulp* *Gluck*", 1, 1, 1, 1) 
                        "Твой член снова уперся в ее горло."
                        "Ты чувствуешь, как Чоу пытается засунуть его еще глубже."
                        "Она начинает сжимать горло."
                        "Эти ощущения подталкивают тебя к кульминации."

                        menu:

                            "-Кончить-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Gluuuuuuh!*", 1, 1, 1, 1) 
                                m "Дааа..."
                                call cho_main("*Glurck!*...", 1, 1, 1, 1) 
                                call cho_main("*GlUrck!*...*gluglugulgh...*", 1, 1, 1, 1) 
                                "Чоу пытается все проглотить, но большая часть выливается из ее рта."
                                call cho_main("Blehg!", 1, 1, 1, 1) 
                                "Сперма вытекает из ее рта и стекает по подбородку, пачкая форму."
                                call cho_main("(О боже... это было так противно...)", 1, 1, 1, 1) 
                                call cho_main("gross! Моя форма! Вы должны мне больше очков, придурок!", 1, 1, 1, 1) 

                                menu:

                                    "-Ладно. 5 дополнительных очков-":
                                        m "Ладно, мисс Чанг. [cho_points] очков Когтеврану."
                                        call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                        jump end_cho_event

                                    "-Что? Конечно нет.-":
                                        m "Конечно нет."
                                        call cho_main("Но! Это не справедливо!", 1, 1, 1, 1) 
                                        m "Соглашайся или уходи, мисс Член."
                                        call cho_main("Меня зовут Чанг, старый придурок!", 1, 1, 1, 1) 
                                        call cho_main("Это не сложное имя...", 1, 1, 1, 1) #Cho_Sad "Это не сложное имя..."
                                        m "Ты хочешь получить очки или нет?"
                                        call cho_main("Да, пожалуйста.", 1, 1, 1, 1) 
                                        m "[cho_points] очков Когтеврану."
                                        jump end_cho_event

                            "-Предупредить-":
                                m "Я скоро кончу!"
                                call cho_main("Хм!", 1, 1, 1, 1) 
                                call cho_main("Хм!...Blehrg!", 1, 1, 1, 1) 
                                "Чоу высовывает твой член."
                                "Ты ждешь, пока она закончит с ним."
                                "Но вместо этого, она хитро улыбается."
                                call cho_main("15 очков.", 1, 1, 1, 1) 
                                m "Что?!"
                                call cho_main("Договор был насчет минета. Если вы хотите больше, заплатите еще 15 очков.", 1, 1, 1, 1) 

                                menu:

                                    "-15 очков-":
                                        m "Ладно, девочка! Закончи с этим!"
                                        call cho_main("Хорошо.", 1, 1, 1, 1) 
                                        "Чоу берет твой член обратно в рот."
                                        "Она начинает быстро двигать головой."
                                        "Внезапно, такое ощущение приводит тебя к оргазму."
                                        m "Держи, плебейская шлюха!"
                                        #Genie cums in Cho's mouth.
                                        "Твои яички сильно напряжены и ты кончаешь ей прямо в горло."
                                        "Девочка пытается все проглотить, но все лезет обратно."
                                        "Ее щеки начинают раздуваться."
                                        "Когда ты закончил, твой член выскакивает изо рта Чоу."
                                        call cho_main("Хммм!", 1, 1, 1, 1) 
                                        "Чоу ищет место, чтобы сплюнуть."

                                        menu:

                                            "-Дать ей пустой бокал-":
                                                "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                                "Ты даешь бокал Чоу."
                                                call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                                "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                                                "Через несколько мгновений он полностью был заполнен."
                                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                                #gain item [Cum Goblet]
                                                m "Да... что ж, [cho_points] очков Когтеврану."
                                                jump end_cho_event

                                            "-Заставить проглотить.-":
                                                m "Эй, я заплачу дополнительно, если ты проглотишь все."
                                                call cho_main("Охои е?(Проглотить все?)", 1, 1, 1, 1) 
                                                m "Ты же хочешь очки, не так ли?"
                                                call cho_main("(Конечно.)", 1, 1, 1, 1) 
                                                call cho_main("(Надо представить, что это пудинг.)", 1, 1, 1, 1) 
                                                "Глаза Чоу становятся красными."
                                                call cho_main("(Соленый, скользкий пудинг....)", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Блэ...", 1, 1, 1, 1) 
                                                call cho_main("Это все...", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Это все... что вы хотели?", 1, 1, 1, 1) 
                                                m "Да. [cho_points] очков Когтеврану."
                                                call cho_main("Спасибо, gрофес-", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1) 
                                                jump end_cho_event
                                    "-5 очков-":
                                        m "Я дам тебе 5 очков."
                                        call cho_main("... Договорились.", 1, 1, 1, 1) 
                                        "Чоу наклоняется и быстро двигает головой."
                                        "Ее рот быстро работает с твоим членом."
                                        "Внезапно, она хватает твои яички и начинает их поглаживать."
                                        "Приятные ощущения настигают тебя."
                                        m "Да, держи!"
                                        #Genie cums in Cho's mouth.
                                        "Ты кончаешь в ее рот."
                                        "Ее щеки начинают раздуваться."
                                        "Когда ты закончил, твой член выскакивает из ее рта."
                                        call cho_main("Хммм!", 1, 1, 1, 1) 
                                        "Чоу ищет место, чтобы сплюнуть."

                                        menu:

                                            "-Дать ей пустой бокал-":
                                                "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                                "Ты даешь бокал Чоу."
                                                call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                                "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                                                "Через несколько мгновений он полностью был заполнен."
                                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                                #gain item [Cum Goblet]
                                                m "Да... Что ж, [cho_points] очков Когтеврану."
                                                jump end_cho_event
                                            "-Заставить проглотить.-":
                                                m "Эй, я заплачу тебе, если ты все проглотишь."
                                                call cho_main("Охои е?!(Проглотить все?!)", 1, 1, 1, 1) 
                                                m "Ты же хочешь очки, не так ли?"
                                                call cho_main("(Ах, старый извращенец!)", 1, 1, 1, 1) 
                                                call cho_main("(Меня сейчас стошнит!)", 1, 1, 1, 1) 
                                                "Глаза Чоу становятся красными."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Блэ...", 1, 1, 1, 1) 
                                                call cho_main("Все...", 1, 1, 1, 1) 
                                                call cho_main("Все... Все проглотила.", 1, 1, 1, 1) 
                                                m "Отлично. [cho_points] очков Когтеврану."
                                                call cho_main("Спасибо, Профес-", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1) 
                                                jump end_cho_event
                                    "-Пошла ты!-":
                                        m "(Вот сучка!)"
                                        m "Жадная шлюха!"
                                        "Ты хватаешь свой член и быстро дрочишь."
                                                                                    
                                        #Genie cums.
                                        "Через некоторое время, ты кончаешь на Чоу."
                                        call cho_main("Ч-что?...", 1, 1, 1, 1) 
                                        m "[cho_points] очков Когтеврану. А теперь убирайся из моего кабинета."
                                        call cho_main("Но, я не могу пойти в таком виде!", 1, 1, 1, 1) 
                                        m "Уходи."
                                        call cho_main("...", 1, 1, 1, 1) 
                                        call cho_main("...Ладно!", 1, 1, 1, 1) 
                                        $ cho_mad += 10
                                        #Cho storms out.
                                        m "Сучка..."
                                        jump end_cho_event


                        jump end_cho_event

                    "-Быть серьезным-":
                        m "Ты много говоришь."
                        call cho_main("Прост-ММХХ", 1, 1, 1, 1) 
                        "Ты обратно всунул свой член в ее рот."
                        m "Все в порядке, девочка."
                        "Язык Чоу быстро извивается."
                        "Ты держишь ее за голову и упираешься в горло."
                        call cho_main("мммм! мммм!", 1, 1, 1, 1) 
                        "К твоему удивлению, неистовое извивание ее языка кажется невероятным."
                        "Твой член, наконец, проходит в горло и ты чувстуешь тепло."
                        m "Это место..."
                        "Невероятные ощущения приближают тебя к кульминации."
                        
                        menu:

                            "-Кончить-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Glllll!* *Glp!*", 1, 1, 1, 1) 
                                m "Для прибыли, Диснея..."
                                call cho_main("*glp!* *Gack!*", 1, 1, 1, 1) 
                                call cho_main("Хмммм!", 1, 1, 1, 1) 
                                "Чоу пытается проглотить, но сперма лезет обратно в рот "
                                call cho_main("Blehg!", 1, 1, 1, 1) 
                                "Твоя сперма течет изо рта Чоу."
                                "Она стекает по подбородку и пачкает форму."
                                call cho_main("(О боже... он чуть не убил меня...)", 1, 1, 1, 1) 
                                call cho_main("Вы-вы... кретин! Я чуть не захлебнулась! Вы должны дополнительно заплатить!", 1, 1, 1, 1) 

                                menu:

                                    "-Я был немного груб. 10 дополнительных очков.-":
                                        m "Хорошо, мисс Чанг. [cho_points] очков Когтеврану."
                                        call cho_main("Это все? Я хочу больше в следующий раз.", 1, 1, 1, 1) 
                                        jump end_cho_event

                                    "-Что? Конечно нет.-":
                                        m "Что? Конечно нет."
                                        call cho_main("Но вы чуть не придушили меня!", 1, 1, 1, 1) 
                                        call cho_main("Я не могла дышать!", 1, 1, 1, 1) 
                                        m "Бери очки или уходи, мисс Член."
                                        call cho_main("Меня зовут Чанг, старый придурок!", 1, 1, 1, 1) 
                                        m "Ты хочешь очки или нет?"
                                        call cho_main("Да, пожалуйста.", 1, 1, 1, 1) 
                                        m "[cho_points] очков Когтеврану."
                                        jump end_cho_event

                            "-Предупредить-":
                                m "Я скоро кончу!"
                                call cho_main("Хм!", 1, 1, 1, 1) 
                                call cho_main("Хм!...Blehrg!", 1, 1, 1, 1) 
                                "Чоу выплевывает твой член изо рта."
                                "Твой мокрый член пару раз ударяется о щеки Чоу."
                                call cho_main("Я хочу 15 очков.", 1, 1, 1, 1) 
                                m "Что?!"
                                call cho_main("Я согласна была на минет. Что бы кончить-платите дополнительно. Я хочу 15 очков.", 1, 1, 1, 1) 
                                
                                menu:

                                    "-15 очков-":
                                        m "Договорились, покончи с этим!"
                                        call cho_main("Хорошо.", 1, 1, 1, 1) 
                                        "Чоу наклоняется и пару раз шлепает по головке члена, прежде чем взять в рот."
                                        "Она начала сосать его, иногда посматривая на тебя с открытым ртом."
                                        "Вскоре, ты нереально возбуждаешься."
                                        m "Шлюха!"
                                        #Genie cums in Cho's mouth.
                                        "Ты кончаешь в рот Чоу."
                                        "Ее щеки начинают раздуваться."
                                        "Когда ты закончил, твой член выскакивает изо рта Чоу."
                                        call cho_main("Хммм!", 1, 1, 1, 1) 
                                        "Чоу ищет место, чтобы сплюнуть."

                                        menu:

                                            "-Дать ей пустой бокал-":
                                                "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                                "Ты даешь ей пустой бокал."
                                                call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                                "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                                                "Через некоторое время, он был полон."
                                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                                #gain item [Cum Goblet]
                                                m "Так... ну что же, [cho_points] очков Когтеврану."
                                                jump end_cho_event

                                            "-Заставить проглотить.-":
                                                m "Эй, я заплачу дополнительно, если ты проглотишь все."
                                                call cho_main("Охои е?!(Проглочу все?!)", 1, 1, 1, 1) 
                                                m "Ты же хочешь очки, не так ли?"
                                                call cho_main("(Ах, мерзкий старик!)", 1, 1, 1, 1) 
                                                call cho_main("(Меня сейчас стошнит!)", 1, 1, 1, 1) 
                                                "Глаза Чоу становятся красными."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Блэ...", 1, 1, 1, 1) 
                                                call cho_main("Все...", 1, 1, 1, 1) 
                                                call cho_main("Все... я все проглотила.", 1, 1, 1, 1) 
                                                m "Отлично. [cho_points] очков Когтеврану."
                                                call cho_main("Спасибо, Профес-", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1) 
                                                jump end_cho_event
                                    "-5 очков-":
                                        m "Я дам тебе 5 очков."
                                        call cho_main("... Договорились.", 1, 1, 1, 1) 
                                        "Чоу наклоняется вперед и начинает гладить твой член."
                                        "Затем, она целует его."
                                        "Она обхватила член губами и лижет языком."
                                        "Из-за этих ощущений не приходиться долго ждать."
                                        m "Да, держи!"
                                        #Genie cums in Cho's mouth.
                                        "Твой член начинает извергаться во рту Чоу."
                                        "Рот Чоу наполняется твоей спермой."
                                        "Ее щеки начинают раздуваться."
                                        "Когда ты закончил, твой член выскакивает изо рта девочки."
                                        call cho_main("Хммм!", 1, 1, 1, 1) 
                                        "Чоу ищет место, чтобы сплюнуть."

                                        menu:

                                            "-Дать ей пустой бокал-":
                                                "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                                "Ты даешь ей пустой бокал."
                                                call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                                "Сперма медленно льется из маленького ротика девочки, сочась в бокал."
                                                "Через некоторое время, он был полон."
                                                call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                                #gain item [Cum Goblet]
                                                m "Да... Что ж, [cho_points] очков Когтеврану."
                                                jump end_cho_event
                                            "-Заставить проглотить.-":
                                                m "Эй, я заплачу дополнительно, если ты проглотишь все."
                                                call cho_main("Огоий вс?(Проглотить все?)", 1, 1, 1, 1) 
                                                m "Ты же хочешь очки, не так ли?"
                                                call cho_main("(Да.)", 1, 1, 1, 1) 
                                                call cho_main("(Это так отвратительно...)", 1, 1, 1, 1) 
                                                "Глаза Чоу становятся красными."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Блэ...", 1, 1, 1, 1) 
                                                call cho_main("Все...", 1, 1, 1, 1) 
                                                call cho_main("Все... Я все проглотила.", 1, 1, 1, 1) 
                                                m "Отлчино. [cho_points] очков Когтеврану."
                                                call cho_main("Спасибо, Профес-", 1, 1, 1, 1) 
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1) 
                                                jump end_cho_event
                                    "-Пошла на!-":
                                        m "(Кто здесь главный?!)"
                                        m "Жадная сучка!"
                                        "Ты берешь член и засовываешь ей в рот."
                                        call cho_main("Хм!*Gluck!*", 1, 1, 1, 1) 
                                        "Ты очень быстро трахаешь ее горло."
                                        call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1) 
                                        "Ты чувствуешь, что вот-вот кончишь."
                                        m "Ебанная шлюха!"
                                        "С жесткой ухмылкой ты высовываешь член из ее рта."
                                        #Genie cums.
                                        "Твой член взрывается, покрывая девочку твоей вонючей спермой."
                                        call cho_main("...", 1, 1, 1, 1) 
                                        m "[cho_points] очков Когтеврану. А теперь убирайся из моего кабинета."
                                        call cho_main("......", 1, 1, 1, 1) 
                                        m "Уходи."
                                        call cho_main("...", 1, 1, 1, 1) 
                                        call cho_main("...Х-хорошо...", 1, 1, 1, 1) 
                                        $ cho_mad += 10
                                        #Cho shuffles out.
                                        m "Сучка..."
                                        jump end_cho_event


label cho_favor_3_3:
    m "Соси мой член."
    
    if cho_mad > 10:
        jump cho_mad_blowjob

    call cho_main("Хорошо!", 1, 1, 1, 1) 
    m "Разве ты не хочешь очков за это?"
    call cho_main("Что?", 1, 1, 1, 1) 
    call cho_main("Oх, да.", 1, 1, 1, 1) 
    call cho_main("Я хочу [cho_points] очков.", 1, 1, 1, 1) 
    
    menu:

        "-Давай сделай это-":
            
            m "Встань на колени и открой рот."
            "Чоу встает на колени и открывает рот, высунув язык."
            "Тебя сводит с ума твоя студентка, которая стоит на коленях с открытым ртом."
            "Твой член сильно возбужден и упирается в складку мантии."
            call cho_main("Ау аия?(Вам нравится?)", 1, 1, 1, 1) 
            m "Очень, мисс Чанг."
            call cho_main("Аио.(Спасибо.)", 1, 1, 1, 1) 
            "Ты высовываешь свой член из-под мантии и держишь его на небольшем расстоянии от рта Чоу."
            "Ты дразнишь ее, качая бедрам вперед и назад."
            call cho_main("...", 1, 1, 1, 1) 
            call cho_main("......", 1, 1, 1, 1) 
            call cho_main("......Э!ооие ео!(Эй! положите его!)", 1, 1, 1, 1) 
            m "Умоляй."
            call cho_main("Что?", 1, 1, 1, 1) 
            m "Умоляй меня об этом."
            call cho_main("Хорошо. эм... д-дайте мне его.", 1, 1, 1, 1) 
            call cho_main("Пожалуйста. Положите свой член в мой...рот?", 1, 1, 1, 1) 
            
            menu:
                
                "-Ты называешь - это умолять?-":
                    m "Ты, вот это, называешь - умолять?"
                    call cho_main("...", 1, 1, 1, 1) 
                    m "Давай. Ты можешь сделать лучше."
                    call cho_main("Пожалуйста. Дайте мне пососать ваш член.", 1, 1, 1, 1) 
                    "Ты наклоняешься вперед, позволяя своему кончику коснуться ее носа."
                    "Твой предэякулят оставляет тонкую полоску слизи между вами.."
                    m "Ты можешь лучше."
                    call cho_main("...", 1, 1, 1, 1) 
                    call cho_main("......", 1, 1, 1, 1) 
                    call cho_main(".........", 1, 1, 1, 1) 
                    call cho_main("............пожалуйста, трахните мой ротик!", 1, 1, 1, 1) 
                    call cho_main("Мой маленький похотливый ротик, как моя киска.", 1, 1, 1, 1) 
                    call cho_main("Пожалуйста, пожалуйста, пожалуйста, дайте мне пососать ваш идеальный член!", 1, 1, 1, 1) 
                    call cho_main("Я буду лизать ваши яички и проглатывать всю сперму.", 1, 1, 1, 1) 
                    call cho_main("Пожалуйста, позвольте мне быть вашей личной сосалкой.", 1, 1, 1, 1) 
                    m "Это было... не плохо."
                    pass

                "-Отлично.-":
                    m "Отлично, девочка."
                    call cho_main("Спасибо.", 1, 1, 1, 1) 
                    pass

            "Ты, наконец наклоняшься, позволяя Чоу взять член в рот"
            call cho_main("*chomp* *ommph* *Sluuurp*", 1, 1, 1, 1) 
            "Чоу начинает яростно сосать."
            "Ты чувствуешь, как ее язык щекочет твою головку."
            call cho_main("*oomph* *Gluck*", 1, 1, 1, 1) 
            "Ты упираешься в горло."
            call cho_main("*gack!* *Cough*", 1, 1, 1, 1) 
            "Слюни Чоу вытекают изо рта."
            call cho_main("О боже... У меня почти получилось в этот раз.", 1, 1, 1, 1) 
            "Еще больше слюней падает из ее рта."
            "Ты шлепаешь своим членом по ее языку, прежде чем протолкнуть его в горло."
            call cho_main("(Нахальный старик...)", 1, 1, 1, 1) 
            m "Больше практики."
            "Чоу проталкивает член в горло."
            call cho_main("Хммм.", 1, 1, 1, 1) 
            m "Не спеши."
            "Чоу проигнорировала тебя. Она проталкивает твой член все глубже."
            call cho_main("Хммм!*Gluck!*", 1, 1, 1, 1) 
            "Наконец, твой член прошел в ее горло."
            call cho_main("Ммм!", 1, 1, 1, 1) 
            "Ощущения, которые ты чувствуешь, невероятны."
            "Чоу начинает быстро шевелить головой."
            call cho_main("*UgG* *Gug* *Gug!*", 1, 1, 1, 1) 
            "Ее усилия дают плоды, и ты чувствуешь, что вот-вот кончишь."
            
            menu:

                "-Кончить-":
                    ##Genie cums in Cho's mouth.
                    call cho_main("*ахх!* *Glp!*", 1, 1, 1, 1) 
                    $ renpy.play('sounds/gulp.mp3')
                    m "Я-ИЗБРАННЫЙ!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*", 1, 1, 1, 1) 
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Хммм!", 1, 1, 1, 1) 
                    "Чоу все проглатывает, до последней капли"
                    call cho_main("Вы знаете, профессор Дамблдор, сэр, ваша сперма, не такая уж плохая.", 1, 1, 1, 1) 
                    call cho_main("Для старикашки, я имею в виду.", 1, 1, 1, 1) 
                    m "Хм, спасибо?"
                    call cho_main("Могу я получить очки.", 1, 1, 1, 1) 
                    m "..."
                    m "...Да, конечно. [cho_points] очков Когтеврану."
                    jump end_cho_event


                "-Предупредить-":
                    m "Я вот-вот кончу!"
                    call cho_main("Хм?", 1, 1, 1, 1) 
                    call cho_main("Хм!...Блэгх!", 1, 1, 1, 1) 
                    "Чоу высовывает твой член из ее горла."
                    "Твой член выскакивает из ее рта и только длинная слюна соединяет вас."
                    call cho_main("Вы хотите, чтобы я проглотила?", 1, 1, 1, 1) 
                    m "Что?"
                    "Чоу наклоняется вперед и прижимает губы к члену."
                    call cho_main("Если вы хотите, я проглочу все.", 1, 1, 1, 1) 
                    call cho_main("И я даже не попрошу дополнительных очков...", 1, 1, 1, 1) 
                                
                    menu:

                        "-Кончить в рот.-":
                            m "Я хочу кончить в твой рот."
                            call cho_main("Хорошо.", 1, 1, 1, 1) 
                            "Чоу пару раз ударяет твой член об язык прежде чем засунуть его в рот."
                            "Она продолжает надрачивать его, смотря тебе в глаза."
                            "Вскоре, ты не можешь совладать с собой и кончаешь."
                            m "Шлюха!"
                            #Genie cums in Cho's mouth.
                            "Ты начинаешь кончать в ее рот.."
                            call cho_main("Хмммм....", 1, 1, 1, 1) 
                            call cho_main("(Вот дерьмо!)", 1, 1, 1, 1) 
                            "Чоу пытается изо всех сил проглотить все."
                            "Но небольшая струя спермы стекает по ее губам."
                            "Чо умоляюще смотрит тебе в глаза."
                            
                            menu:

                                "-Дать ей пустой бокал-":
                                    "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                    "Ты даешь ей бокал."
                                    call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                    "Твоя сперма медленно стекает по ее губам, она все сплевывает."
                                    "Через некоторое время, он был полон."
                                    call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                    "Чоу облизывает края бокала."
                                    #gain item [Cum Goblet]
                                    m "[cho_points] очков Когтеврану."
                                    jump end_cho_event

                                "-Заставить проглотить.-":
                                    m "Проглоти все."
                                    call cho_main("Оои е?(Проглотить все?)", 1, 1, 1, 1) 
                                    m "Да. Проглоти как шлюха."
                                    call cho_main("(А, эу!)", 1, 1, 1, 1) 
                                    call cho_main("(мммм...такая скользкая.)", 1, 1, 1, 1) 
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Ах...", 1, 1, 1, 1) 
                                    call cho_main("...", 1, 1, 1, 1) 
                                    call cho_main("...Вкусно.", 1, 1, 1, 1) 
                                    m "Шлюха. [cho_points] очков Когтеврану."
                                    call cho_main("Спасибо, профес-", 1, 1, 1, 1) 
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...", 1, 1, 1, 1) 
                                    jump end_cho_event

                        "-Кончить в горло-":
                            m "Я хочу кончить в твое горло."
                            call cho_main("Да?", 1, 1, 1, 1) 
                            "Чоу заглатывает твой член."
                            "Она отдыхает, привыкая к размеру."
                            "Затем, она начинает трахать горлом твой член."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*", 1, 1, 1, 1) 
                            m "Великие шары Гендальфа..."
                            call cho_main("*Hnnnng!*", 1, 1, 1, 1) 
                            "Чоу очень глубоко взяла член."
                            "Ты кончаешь."
                            #Genie cums in Cho's mouth.
                            call cho_main("!", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(Боже, старик...)", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(Так много...)", 1, 1, 1, 1) 
                            "Ты вытаскиваешь, член из ее рта, оставляя ее в ошеломлении."
                            call cho_main("Спасибо, профессор Дамблдор...", 1, 1, 1, 1) 
                            m "[cho_points] очков Когтеврану."
                            jump end_cho_event

                        "-Кончить на лицо.-":

                                m "Я хочу кончить на твое лицо."
                                call cho_main("Вы хотите кончить на мое тупое лицо?", 1, 1, 1, 1) 
                                call cho_main("Ладно.", 1, 1, 1, 1) 
                                "Чоу хватает твой член и сосет."
                                call cho_main("Mmm!*Gluck!*", 1, 1, 1, 1) 
                                "Чоу заглатывает его."
                                call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1) 
                                "Наконец, ты чувствуешь, что вот-вот кончишь."
                                m "Я уже-"
                                "Чоу выплевывает твой член и держит возле лица."
                                call cho_main("Кончите на меня, профессор!", 1, 1, 1, 1) 
                                ##Genie cums.
                                "Твой член разрывается, кончая на лицо молодой волшебницы."
                                call cho_main("Да...", 1, 1, 1, 1) 
                                call cho_main("О боже...", 1, 1, 1, 1) 
                                call cho_main("Это было потрясающе.", 1, 1, 1, 1) 
                                m "[cho_points] очков Когтеврану."
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("... Я полностью покрыта, не так ли?", 1, 1, 1, 1) 
                                m "Уходи."
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("Хорошо, профессор.", 1, 1, 1, 1) 
                                jump end_cho_event


        "-Я хочу трахнуть твое лицо.-":
            m "Я хочу трахнуть твое лицо."
            call cho_main("Что?...", 1, 1, 1, 1) 
            m "Я хочу использовать твой рот как киску."
            call cho_main("Профессор!", 1, 1, 1, 1) 
            call cho_main("Профессор! Это звучит так пошло.", 1, 1, 1, 1) 
            m "Встань на колени и открой рот."
            call cho_main("Что ж...", 1, 1, 1, 1) 
            call cho_main("Что ж... я получу [cho_points] очков...", 1, 1, 1, 1) 
            "Чоу сползает на колени и открывает рот, высунув язык."
            call cho_main("Ы ооы?(Вы готовы?)", 1, 1, 1, 1) 
            "Твой член пульсирует под мантией."
            m "Хорошо, девочка."
            "Ты высовываешь член из-под мантии."
            call cho_main("(Так страшно...)", 1, 1, 1, 1) 
            "Ты направляешь член в ее рот."
            call cho_main("Хммм...", 1, 1, 1, 1) 
            call cho_main("Хммм...(Он такой толстый!)", 1, 1, 1, 1) 
            "Рот молодой ведьмы теплый и удивительно гостеприимный."
            "Ты глубже засовываешь член."
            "Ты останавливаешься, когда чувствуешь, что твой член уперся в ее горло."
            call cho_main("*Hrk!*", 1, 1, 1, 1) 
            call cho_main("*Hrk!* *Ack!*", 1, 1, 1, 1) 
            call cho_main("*Hrk!* *Ack!* *Glg*...", 1, 1, 1, 1) 
            m "О, Великие пески пустыни!"
            "К твоему удивлению, Чоу проталкивает его глубже, давясь им."
            "Это занимает около минуты."
            "Затем ты хватаешь голову Чоу и крепко держишь."
            m "Хорошая ведьмочка..."
            "Ты высовываешь член из ее горла."
            "Затем обратно засовываешь, еще глубже."
            call cho_main("AALG! HHHGGGGG!", 1, 1, 1, 1) 
            call cho_main("AALG! HHhgGggG! (Боже, он меня задушит!)", 1, 1, 1, 1) 
            "Ты хорошо чувствуешь ее горло, по этому начинаешь трахать ее."
            call cho_main("*glug* *GluG* *glg* *Gluck*", 1, 1, 1, 1) 
            call cho_main("(О боже....)", 1, 1, 1, 1) 
            call cho_main("*GlG* *Glg* *Glg*", 1, 1, 1, 1) 
            call cho_main("(Мое горло...)", 1, 1, 1, 1) 
            call cho_main("(Мое горло... так хорошо...)", 1, 1, 1, 1) 
            
            menu:

                "-Кончить-":
                    #Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*", 1, 1, 1, 1) 
                    $ renpy.play('sounds/gulp.mp3')
                    m "Я-ИЗБРАННЫЙ!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*", 1, 1, 1, 1) 
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Хммм!", 1, 1, 1, 1) 
                    "Чоу проглатывает все, причмокивая губаками"
                    call cho_main("Знаете, профессор Дамблдор, ваша сперма не такая уж и плохая.", 1, 1, 1, 1) 
                    call cho_main("Для такого старикашки, я хотела сказать.", 1, 1, 1, 1) 
                    m "Эм, спасибо?"
                    call cho_main("Могу я получить очки?", 1, 1, 1, 1) 
                    m "..."
                    m "...Да, конечно. [cho_points] очков Когтеврану."
                    jump end_cho_event


                "-Предупредить-":
                    m "Я вот-вот кончу!"
                    call cho_main("Хм?", 1, 1, 1, 1) 
                    call cho_main("Хм!...Блэгх!", 1, 1, 1, 1) 
                    "Чоу высовывает твой член изо рта."
                    "Твой член выскакивает из ее губ и только длинная слюна соединяет вас."
                    call cho_main("Хотите, чтоб я все проглотила?", 1, 1, 1, 1) 
                    m "Что?"
                    "Чоу наклоняется вперед и прижимает губы к члену."
                    call cho_main("Я проглочу все.", 1, 1, 1, 1) 
                    call cho_main("И я не попрошу дополнительных очков...", 1, 1, 1, 1) 
                                
                    menu:

                        "-Кончить в рот.-":
                            m "Я хочу кончить в твой рот."
                            call cho_main("Хорошо.", 1, 1, 1, 1) 
                            "Чоу наклоняется вперед и пару раз ударяет членом о свой язык, прежде чем засунуть его в рот."
                            "Она продолжает сосать, полизывая языком."
                            "Вскоре, ты не можешь совладать с собой."
                            m "Шлюха!"
                            #Genie cums in Cho's mouth.
                            "Ты яростно кончаешь в ее ротик..."
                            call cho_main("Хммммм....", 1, 1, 1, 1) 
                            call cho_main("(Вот дерьмо!)", 1, 1, 1, 1) 
                            "Чоу изо всех сил пытается проглотить все."
                            "Небольшая струя спермы уже стекает по губам."
                            "Чо умоляюще смотрит тебе в глаза."
                            
                            menu:

                                "-Дать ей пустой бокал-":
                                    "Единственный предмет в твоем кабинете-это бокал, оставшийся от ваших ночных бесед с Северусом."
                                    "Ты даешь ей бокал."
                                    call cho_main("Блэ..гх...", 1, 1, 1, 1) 
                                    "Твоя сперма медленно стекает по ее губам, она все сплевывает."
                                    "Через некоторое время, он был полон."
                                    call cho_main("Спасибо, сэр.", 1, 1, 1, 1) 
                                    "Чоу слизывает края бокала."
                                    #gain item [Cum Goblet]
                                    m "[cho_points] очков Когтеврану."
                                    jump end_cho_event

                                "-Заставить проглотить.-":
                                    m "Проглоти все."
                                    call cho_main("Огоий вс?(Проглотить все?)", 1, 1, 1, 1) 
                                    m "Да. Проглоти как шлюха."
                                    call cho_main("(Да, сэр!)", 1, 1, 1, 1) 
                                    call cho_main("(мммм... такая скользкая.)", 1, 1, 1, 1) 
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Ах...", 1, 1, 1, 1) 
                                    call cho_main("...", 1, 1, 1, 1) 
                                    call cho_main("... Вкусно.", 1, 1, 1, 1) 
                                    m "Шлюха. [cho_points] очков Когтеврану."
                                    call cho_main("Спасибо, профес-", 1, 1, 1, 1) 
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...", 1, 1, 1, 1) 
                                    jump end_cho_event

                        "-Кончить в горло-":
                            m "Я хочу кончить в твое горло."
                            call cho_main("Да?", 1, 1, 1, 1) 
                            "Чоу наклоняется и засовывает член в горло."
                            "Она остановилась на мгновение, привыкая к его размерам."
                            "Затем, она начинает трахать горлом твой член."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*", 1, 1, 1, 1) 
                            m "Великие шары Гендальфа..."
                            call cho_main("*Hnnnng!*", 1, 1, 1, 1) 
                            "Чоу еще глубже заталкивает твой член."
                            "Ты начинаешь кончать."
                            #Genie cums in Cho's mouth.
                            call cho_main("!", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(Боже, старик...)", 1, 1, 1, 1) 
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(Так много...)", 1, 1, 1, 1) 
                            "Ты вытаскиваешь, член из ее рта, оставляя ее в ошеломлении."
                            call cho_main("Спасиб-", 1, 1, 1, 1) 
                            call cho_main("Спасибо", 1, 1, 1, 1) 
                            call cho_main("Спасибо, сэр...", 1, 1, 1, 1) 
                            m "[cho_points] очков Когтеврану."
                            jump end_cho_event

                        "-Кончить на лицо.-":

                                m "Я хочу кончить на твое лицо."
                                call cho_main("Вы хотите кончить на мое глупое лицо?", 1, 1, 1, 1) 
                                call cho_main("Хорошо.", 1, 1, 1, 1) 
                                "Чоу хватает твой член и засовывает в рот."
                                call cho_main("Ммм!*Gluck!*", 1, 1, 1, 1) 
                                "Чоу заглатывает его."
                                call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1) 
                                "Наконец, ты чувствуешь, что вот-вот кончишь."
                                m "Я уже-"
                                "Чоу выплевывает твой член и держит возле лица."
                                call cho_main("Кончите на меня, профессор!", 1, 1, 1, 1) 
                                ##Genie cums.
                                "Твой член разрывается, кончая на лицо молодой волшебницы."
                                call cho_main("Да...", 1, 1, 1, 1) 
                                call cho_main("О боже...", 1, 1, 1, 1) 
                                call cho_main("Это было потрясающе.", 1, 1, 1, 1) 
                                m "[cho_points] очков Когтеврану."
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("... Я полностью покрыта, не так ли?", 1, 1, 1, 1) 
                                m "Уходи."
                                call cho_main("...", 1, 1, 1, 1) 
                                call cho_main("Хорошо, профессор.", 1, 1, 1, 1) 
                                jump end_cho_event
            

        "-Мисс Член, тебе нравится аннилингус?-":
            m "Мисс Член, тебе нравится аннилингус?"
            call cho_main("Вы спрашиваете или утверждаете?", 1, 1, 1, 1) 
            m "Подойди сюда."
            "Чоу прыгает к тебе, останавливаясь перед столом."
            call cho_main("Ну?", 1, 1, 1, 1) 
            m "(Что она делает?)"
            m "(Может, она пытается мне что-то сказать...)"

            menu:

                "-Относиться к ней, как к шлюхе.-":
                    "Слова для социалистов и слабаков."
                    "Ты хватаешь ее за волосы и опускаешь на колени."
                    call cho_main("!", 1, 1, 1, 1) 
                    call cho_main("Профес-", 1, 1, 1, 1) 
                    "Прежде чем она сможет что-то сказать, ты высовываешь член из-под мантии и затыкаешь ее."
                    call cho_main("(Дааа...)", 1, 1, 1, 1) 
                    call cho_main("*Hrk!*", 1, 1, 1, 1) 
                    call cho_main("*Hrk!* *Ack!*", 1, 1, 1, 1) 
                    call cho_main("*Hrk!* *Ack!* *Glg*...", 1, 1, 1, 1) 
                    "Ты чувствуешь, как ее язык извивается вокруг твоей головки."
                    call cho_main("*oomph* *Gluck*", 1, 1, 1, 1) 
                    "Ты заталкиваешь свой член глубоко в ее горло."
                    call cho_main("*gack!* *Cough*", 1, 1, 1, 1) 
                    "Она начинает задыхаться."
                    call cho_main("(Я сейчас умру...)", 1, 1, 1, 1) 
                    call cho_main("(Противный старик...)", 1, 1, 1, 1) 
                    "Изо рта Чоу капают слюни."
                    "Твои яички шлепают ей по лицу."
                    call cho_main("(Я такая шлюха...)", 1, 1, 1, 1) 
                    m "Все хорошо, конченная шлюха."
                    call cho_main("(Да!)", 1, 1, 1, 1) 
                    "Внезапно, ты чувствуешь, что руки Чоу давно ухватились за твою задницу и тебе не нужно удерживать ее."
                    "Обезумевшая молодая ведьма отчаянно сосет твой член."
                    "Ты чувствуешь себя замечательно, но у тебя есть и другие планы."
                    "Ты хватаешь Чоу за руки и толкаешь."
                    $ renpy.play('sounds/pop.mp3')
                    "Твой член выскакивает из ее горла, и она падает на корточки."
                    m "Начни лизать мою задницу."
                    call cho_main("Да, профессор!", 1, 1, 1, 1) 
                    "Чоу лезет под одежду."
                    "Внезапно, ты чувствуешь, как мокрый язык лижет твою волосатую задницу."
                    m "Вот так."
                    m "Давай. Давай..."
                    "В то время как она лижет твою задницу, ты продолжаешь дрочить."
                    "Она убирает твои руки и начинает тебе дрочить."
                    m "Чертов Еврей-Акабур..."
                    "Руки Чоу работают в такт с языком, через некоторое время, ты кончаешь."
                    #Genie Cums.
                    "Твой член кончает на ее руки."
                    "Длинные струи падают на пол."
                    call cho_main("Вау!", 1, 1, 1, 1) 
                    call cho_main("Вау! Это было круто...", 1, 1, 1, 1) 
                    m "Хорошая работа, мисс Член. [cho_points] очков Когтеврану..."
                    call cho_main("Спасибо, профессор Дамблдор.", 1, 1, 1, 1) 
                    jump end_cho_event
                    
                    
label cho_mad_blowjob:
    call cho_main("Не могу поверить, старый извращенец.", 1, 1, 1, 1) 
    call cho_main("Ладно.", 1, 1, 1, 1) 
    call cho_main("Ладно. Я сделаю это.", 1, 1, 1, 1) 
    "Чо падает на колени и хватает твой полутвердый член."
    call cho_main("Он у вас еще не твердый.", 1, 1, 1, 1) 
    "Чоу наклоняется и плюет на него."
    "Злая, молодая ведьмочка начинает дрочить его."
    m "Успокойся."
    call cho_main("Успокоиться?", 1, 1, 1, 1) 
    "Чоу берет его в рот."
    "Ее язык извивается вокруг твоей головки."
    "Затем, она быстро шевелит головой вперед и назад."
    m "Так лучше."
    "Чоу выплевывает твой член и дрочит."
    call cho_main("Вы собираетесь кончать, старый придурок?", 1, 1, 1, 1) 
    m "Думаю, что скоро."
    "Чоу обратно сует его в рот."
    "Вскоре, ты понимаешь, что вот-вот кончишь."
    call cho_main("Вы скоро?", 1, 1, 1, 1) 
    "Чоу неудобно сжимает твой член и полизывает его языком."
    ##Genie cums
    "Внезапно, ты начинаешь кончать, Чоу замечает это и наклоняет его на пол."
    m "Aх! Чоу, какая ты сучка!"
    "Как только последние капли падают на пол, она отпускает твой член."
    "Она вытирает с рук твою сперму."
    call cho_main("Ну..? Я получу свои очки?", 1, 1, 1, 1) 
    m "Ладно. Но ты нахалявила здесь , за это я вычту 5 очков [points-5], маленькая сучка..."
    $ cho_mad += 5
    m "[points-5] Когтеврану."
    call cho_main("Придурок.", 1, 1, 1, 1) 
    jump end_cho_event
