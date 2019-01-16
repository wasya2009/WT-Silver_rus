label phoenix_lbl:
    if bird_interact == 2: # Counts how many times you have interacted with the bird.
        stop music fadeout 3.0
        $ bird_interact += 1 # Counts how many times you have interacted with the bird.
        show screen blktone8
        with d7
        m "Интересная птичка."
        hide screen blktone8
        with d3
        call music_block 
        jump day_main_menu
    jump phoenix_menu

label phoenix_menu:
    menu:
        "-Изучить-" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            #$ tt_xpos=270
            #$ tt_ypos=90
            #show screen genie_stands
            call gen_chibi("stand","mid","base",flip=True) 
            show screen chair_left #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Даже эта странная птица излучает магию ..."
            show screen genie
            hide screen genie_stands
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        "-Покормить птицу-" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding
        #"-Pet the bird-" if bird_examined:
        #    jump petting
        #"-Talk to the bird-" if bird_examined and fawkes_intro_done: #FIXED CODE DUPLICATION HERE
        #    jump talkingfawkes
        "-Неважно-":
            call screen main_room_menu
        
### FEEDING ###
label feeding:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = 1 #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "Кушай птичка..."
    elif genie_speaks == 2 and fawkes_intro_done:
        m "Тебе вообще это нравится?"
        faw "Это помогает мне выжить."
        m "Это отличный взгляд на жизнь."
    elif genie_speaks == 3 and fawkes_intro_done:
        faw "Вы когда-либо задавались вопросом, устают ли собаки от наличия того же самого собачьего корма каждый день?"
        m "Едва ли."
        faw "Ну, я уверен, что вы могли бы купить мне новую еду!"
        g4 "В магазине ничего нет!"
        m "Иногда мне интересно, почему я терплю тебя ..."
    else:
        pause .5
    show screen genie
    hide screen feeding
    with Dissolve(0.3)
    call screen main_room_menu
    
### PETTING ###
label petting:
    $ ce_name = "phoenix"
    if fawkes_intro_done:
        if day >= 20 and bird_interact >= 10: # Counts how many times you have interacted with the bird.
            stop music fadeout 3.0
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
            hide screen genie
            show screen petting
            with d7
            ">Птица начинает нагреваться, когда ты ее поглаживаешь."
            m "?"
            hide screen petting
            show screen petting
            ">Птица становится все горячее и горячее."
            menu:
                "-Продолжить гладить птицу-":
                    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
                    m "М... чертовски приятное тепло."
                    hide screen petting
                    show screen petting
                    ">Ты чувствуешь, что в комнате нарастает энергия."
                    ">Вдруг вся комната гудит."
                    hide screen petting
                    show screen petting
                    m "Почему я до сих пор ласкаю эту птицу?"
                    ">Жужжание быстро перестает оставлять вас со звоном в ушах."
                    $ renpy.play('sounds/door3.mp3')
                    "Профессор?"
                    m "Хм?"
                    "Ты вызвал меня сюда?"
                    m "? ... Нет."
                    $ renpy.play('sounds/door.mp3')
                    ">Ты видишь кого-то, стоящего прямо у двери, слишком далеко, чтобы рассмотреть."
                    her "Я почувствовала, как кто-то зовет меня сюда."
                    m "Тогда заходи, прямо сейчас..."
                    call her_walk(610,400,2) 
                    show screen hermione_02
                    pause.5
                    show screen bld1
                    with d3
                    show screen hermione_01
                    call her_main("Нечто... чувствую себя иначе...","open","worriedL",xpos=390,ypos=0) 
                    ">Она смотрит на птицу, которую вы ласкаете, и ее глаза растут."
                    call her_main("Профессор. Что-то не так.","angry","wide") 
                    m "Почему бы тебе сперва не сказать мне, почему ты здесь?"
                    her "Профессор! Феникс-!"
                    $ renpy.play('sounds/pistol2.mp3')
                    ">Шум нарастает по всей комнате."
                    hide screen hermione_main
                    with d3
                    m "Что за?! Что происходит?!"
                    $ ce_hair_style = "B"
                    $ ce_hair_color = "4"
                    call ce_her_main("","fawkes_1",xpos=140,ypos=0) 
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main
                    call ce_her_main("","fawkes_1",xpos=390) 
                    "Гермиона- я думаю"
                    m "..."
                    m "Что?"
                    "Гермиона- Я думаю, ты не можешь сказать, что происходит?"
                    m "Почему бы тебе просто не рассказать мне."
                    "Гермиона-я думаю, учитывая, что ты не можешь понять, это я Фокс."
                    m "... Это должно что-то значить?"
                    call ce_her_main("","fawkes_2") 
                    faw "Птица, которую ты так хорошо гладил последние несколько дней."
                    m "?"
                    m "Тогда как ты оказалась в этой девушке?"
                    call ce_her_main("","fawkes_1") 
                    faw "Серьезно?"
                    faw "Это называется магия.  Ты был так возбужден, что это начало влиять на меня."
                    call ce_her_main("","fawkes_3") 
                    faw "Так что я подумал, что запрыгну в девушку ненадолго и посмотрю, не смогу ли я исправить твою маленькую... проблему."
                    m "О?"
                    g9 "И как ты планируешь это сделать?"
                    call ce_her_main("","fawkes_2") 
                    faw "Ну, это зависит от вас. Я могу взять ее только в том случае, если ее защита будет падать."
                    m "Да?"
                    faw "Вы должны сделать ее озабоченной, чтобы я запрыгнул в нее."
                    faw "Чем она старше, тем дольше я могу оставаться."
                    faw "Ты так сильно хотел трахнуть эту девушку последние несколько дней...  Это то, что позволяет мне держаться так долго, но это не сработает снова."
                    faw "У меня осталось не так много времени, но как насчет того, чтобы показать тебе другие мои наряды?"
                    m "Небольшое утешение."
                    faw "Наслаждайся."
                    call ce_her_main("","fawkes_4") 
                    show screen ctc
                    pause
                    hide screen ctc
                    faw "Как тебе это?"
                    m "Так нет оригинального Контента?"
                    faw "Мэверик не художник."
                    g4 "Нет, блин"
                    hide screen hermione_01
                    $ hermione_SC.chibi.xpos=400
                    $ hermione_SC.chibi.ypos=240
                    show screen hermione_02_b
                    call ce_her_main("","fawkes_5") 
                    show screen ctc
                    pause
                    hide screen ctc
                    faw "Вам нравится этот?"
                    g9 "Теперь я могу отстать!"
                    faw "Держу пари, тебе это понравится."
                    call ce_her_main("","fawkes_6") 
                    faw "Не так ли?"
                    g5 "..."
                    g10 "..."
                    m "Ты, черт побери, готов поспорить."
                    call ce_her_main("","fawkes_7") 
                    faw "Ну, это было весело, но я собираюсь вернуть девушку обратно."
                    m "Это длилось не так долго, как я надеялся."
                    faw "Я сделаю тебе небольшое одолжение и оставлю ее в таком виде."
                    hide screen custom_event_h
                    with d3
                    $ ce_hair_color = 1
                    call ce_her_main("...","hermione_1") 
                    hide screen custom_event_h
                    with d3
                    $ ce_hair_style = "A"
                    call ce_her_main("Профессор?!","hermione_2") 
                    call ce_her_main("Что происходит?!","hermione_3") 
                    m "Черт побери, если я знаю"
                    call ce_her_main("Почему я ношу это? Что происходит? Какие-!") 
                    hide screen hermione_02
                    hide screen hermione_02_b
                    hide screen custom_event_h
                    with d3
                    call her_walk(400,610,0.75) 
                    $ renpy.play('sounds/door.mp3')
                    m "Ну, я думаю, это было интересно"
                    $ fawkes_intro_done = True #Makes this non-repeatable
                    hide screen petting
                    show screen genie
                    hide screen blktone8
                    hide screen bld1
                    with d3
                    call music_block 
                    jump day_main_menu
                "-Хватит гладить птицу-":
                    $ bird_interact -= 2 # Counts how many times you have interacted with the bird.
                    m "Ну, это чертовски странно"
                    hide screen petting
                    show screen genie
                    hide screen blktone8
                    with d3
                    call music_block 
                    jump day_main_menu

        else: #needs more interactions for introduction

            ###DEFAULT PETTING WHEN NOT INTRODUCED###

            $ bird_interact += 1 # Counts how many times you have interacted with the bird.
            hide screen genie
            show screen petting
            with Dissolve(0.3)
            pause 3
            show screen sad_phoenix #SMILEY
            pause 1.5
            m "Птица выглядит не очень хорошо. Больна или что-то еще?"
            pause .5
            hide screen sad_phoenix #SMILEY
            hide screen petting
            show screen genie
            with Dissolve(0.3)
            call screen main_room_menu

    else:  #fawkes_intro_done == True

        if whoring <=2:
            stop music fadeout 3.0
            $ bird_interact += 1
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
            hide screen genie
            show screen petting
            with d7
            #faw "You realize petting me wont make something happen every time don't you?"
            faw "Вы понимаете, что каждый раз лаская меня что-то, не так ли?"
            m "..."
            m "Как именно, ты сейчас со мной разговариваешь?"
            faw "Магия.  Когда вы собираетесь научиться перестать задавать вопросы и понять, что ответ всегда волшебство."
            m "Ты мне нравилась намного больше, когда была в теле той ведьмы."
            hide screen petting
            hide screen blktone8
            show screen genie
            with d3
            call music_block 
            jump day_main_menu

        elif bird_interact == 20 and whoring ==1:
            stop music fadeout 3.0
            $ bird_interact += 1
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
        #elif whoring > 9000:
            #scene
            #remember to sort the scenes from highest to lowest whoring, this way the highest possible event will happen
        #else:
            #DEFAULT PETTING WHEN INTRODUCED GOES HERE (if you want)


### TALKING ###
label talkingfawkes:
    $ ce_name = "phoenix"
    $ bird_interact += 1
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    $ genie_speaks = renpy.random.randint(1, 3)
    if genie_speaks == 1:
        m "Хорошо, ты ничего не скажешь?"
        faw "..."
        m "..."
        m "Ты мне очень помогаешь... Чертова птица"
    elif genie_speaks == 2:
        faw "Я могу вам помочь?"
        m "Хочешь превратиться в горячую девушку и заняться сексом?"
        faw "Может быть, если вы позовете эту ведьму в раннем возбуждении, я могу взять под контроль ее снова."
    elif genie_speaks == 3 and whoring >= 10:
        faw "У меня внутренний конфликт."
        m "Почему?"
        faw "Часть меня очень возбуждена и хочет тебя прямо сейчас."
        g9 "И это проблема, потому что?"
        faw "Другая часть меня возмущена тем, во что вы превратили эту девушку."
        g4 "Просто перестань играть в скромницу и приведи ее сюда."
        faw "Если ты продолжишь так говорить, я найду кого-нибудь другого."
    elif genie_speaks == 3 and whoring < 5:
        faw "Слушай, я возбужден, но чтобы заполучить эту девушку, мне нужно, чтобы она была слабее."
        m "Я слушаю."
        faw "Сделать ее нравы немного слабее, и я действительно смогу трахнут вас."
        m "..."
        g9 "Это я тебя трахну."
    elif genie_speaks == 3 and whoring >= 5:
        faw "Кажется, я что-то чувствую!"
        m "Серьезно?"
        g9 "{size=-4}(Наконец-то мне снова повезет!){/size}"
        faw "Это определенно нарастает!"
        g9 "{size=-4}(О, я буду приходить хорошо.){/size}"
        $ faw_sneeze4 = renpy.random.randint(1, 2)
        if faw_sneeze4 == 1:
            faw "{size=+5}АПЧХИИИИИ!{/size}"
            faw "..."
            g11 "Ты чихнул?"
            faw "Думаю, это то, что я чувствовала."
            g11 "{size=+3}Со мной?!{/size}"
            faw "Бог не благословит вас?"
            g4 "{size=-4}Чертова птица...{/size}"
        elif faw_sneeze4 == 2 and whoring >= 3:
            $ renpy.play('sounds/door3.mp3')
            g4 "Что тебе надо? Я занят!"
            her "{size=-2}Вы уверены, что хотите, чтобы я ушла?{/size}"
            m "Нет, нет! Заходи!"
            $ renpy.play('sounds/door.mp3')
            $ walk_xpos=620
            $ walk_xpos2=400
            $ hermione_speed = 02.0
            show screen hermione_chibi_robe
            pause 2
            hide screen hermione_chibi_robe
            $ hermione_SC.chibi.xpos=400
            $ hermione_SC.chibi.ypos=240
            show screen hermione_02_b
            $ tmp_robe = hermione_wear_robe
            $ hermione_wear_robe = True
            call her_main("Профессор.  Что-то... позвало меня сюда.","open","worriedL",xpos=390,ypos=0) 
            g9 "И зачем оно позвало тебя сюда?"
            her "Я не уверена... Может, мне не следовало приходить сэр."
            m "Нет, нет, останься."
            her "До свидания, профессор."
            hide screen hermione_main
            with d3
            $ hermione_wear_robe = hermione_wear_robe
            $ walk_xpos=400
            $ walk_xpos2=610
            $ hermione_speed = 4
            show screen hermione_chibi_robe_f
            g4 "Останови ее, проклятая птица!"
            faw "В теме!"
            $ renpy.play('sounds/magic2.mp3')
            pause 1
            $ walk_xpos=620
            $ walk_xpos2=400
            $ hermione_speed = 02.5
            show screen hermione_chibi_robe
            pause 2.5
            hide screen hermione_chibi_robe
            show screen hermione_02_b
            call ce_her_main("...","h0a",xpos=390,ypos=0) 
            her "Профессор... Меня здесь быть не должно."
            g9 "О Нет, ты там, где должна быть."
            $ renpy.play('sounds/glass_break.mp3')
            call ce_her_main("{size=+3}Нет профессор я-{w=.5}{nw}","h0b") 
            faw "О нет, нет!"
            $ renpy.play('sounds/magic2.mp3')
            hide screen custom_event_h
            with d3
            $ ce_hair_color = 4
            call ce_her_main("","h1a") 
            faw "Не волнуйтесь.  Она никуда не денется."
            hide screen custom_event_h
            with d3
            $ ce_hair_style = "A"
            $ ce_hair_color = 1
            call ce_her_main("Нет! Почему я не могу двигаться?","h1b") 
            faw "Черт возьми! Трудно держать ее под контролем!"
            $ renpy.play('sounds/magic2.mp3')
            call ce_her_main("","h2") 
            ">..."
            m "..."
            m "Девочка?"
            call ce_her_main("","h3") 
            "Гермиона?" "Это то, что Вы хотите?"
            m "Вот дерьмо.  Думаю, мы ее сломали."
            "Гермиона?" "О, Не волнуйся."
            hide screen custom_event_h
            with d3
            $ ce_hair_style = "B"
            $ ce_hair_color = 4
            call ce_her_main("","f_new") 
            faw "Теперь она подконтрольна."
            g9 "Наконец-то! Теперь я могу выебать тебе мозги."
            call ce_her_main("","f_dis") 
            faw "Ну ... я бы с удовольствием, но сейчас это не вариант."
            m "Что?"
            faw "Она все еще слишком сопротивляется моей магии."
            m "..."
            g4 "{size=+4}ЧТО?!{/size}"
            call ce_her_main("","f_wor") 
            faw "Да ладно тебе."
            faw "Я привел ее сюда, и я заставил ее носить это, не так ли?"
            m "Это еще не значит, что я счастлив."
            faw "Просто заставьте ее быть ближе к Вам."
            faw "Как только Вы сможете развратить ее еще немного, я смогу контролировать ее дольше."
            m "Я думаю, что в первую очередь я здесь для этого."
            faw "Надеюсь, вам понравился вид, но она возвращается."
            faw "Вы бы предпочли, чтобы я оставил ее здесь?..."
            call ce_her_main("","f_sin") 
            faw "Или удивить ее и заставить носить это снаружи?"
            menu:
                "-Заставь ее остаться-":
                    g9 "Иди сюда и оставайся здесь"
                    faw "О, мне нравится, ход ваших мыслей."
                    call ce_her_main("","f_trans") 
                    $ renpy.play('sounds/magic2.mp3')
                    hide screen custom_event_h
                    with d3
                    $ ce_hair_style = "A"
                    $ ce_hair_color = 1
                    call ce_her_main("...","h_trans") 
                    call ce_her_main("...","h_react1") 
                    call ce_her_main("Профессор?","h_react2") 
                    her "О Боже. Что происходит?!"
                    hide screen hermione_02_b
                    hide screen custom_event_h
                    with d3
                    $ walk_xpos=400
                    $ walk_xpos2=610
                    $ hermione_speed = 02.0
                    show screen hermione_chibi_robe_f
                    pause 2
                    $ renpy.play('sounds/door.mp3')
                    hide screen hermione_chibi_robe_f
                    g9 "Замечательное шоу."
                    faw "Не так ли?"
                "-Пусть идет в коридор.-":
                    g9 "Выведи ее наружу..."
                    faw "Как пожелаете."
                    hide screen hermione_02_b
                    hide screen custom_event_h
                    with d3
                    $ walk_xpos=400
                    $ walk_xpos2=640
                    $ hermione_speed = 02.0
                    show screen hermione_chibi_robe_f
                    $ renpy.play('sounds/door.mp3')
                    hide screen hermione_chibi_robe_f
                    g9 "{size=-4}(Вот так!){/size}"
                    ">..."
                    g9 "{size=-4}(В любую секунду!){/size}"
                    ">..."
                    m "..."
                    her "{size=+6}ААААААААААА!!{/size}"
                    g9 "{size=-4}(Вот и все.){/size}"
                    her "{size=+3}Где моя одежда?{/size}"
                    her "{size=+4}Почему на мне это надето?{/size}"
                    her "{size=+4}Нет! Хватит на меня смотреть!{/size}"
                    $ renpy.play('sounds/run_02.mp3')
                    her "{size=+2}Не смотрите, не смотрите, не смотрите, не смотрите!{/size}"
            g9 "Я начинаю любить тебя все больше и больше, тупая птица."
            faw "Фокс."
            m "Не дави."
        else:
            faw "Там определенно есть энергия!  Мне просто тяжело сосредоточиться!"
            g4 "Хорошо сосредоточиться!"
            faw "{size=+3}Я пытаюсь, но не могу.{/size}"
            faw "Вы должны больше Гермиону развратить, если хотите, чтобы я взял ее под свой контроль."
            m "..."
            m "Гермионау?"
            faw "Серьезно?  Ведьма, на которую ты пускаешь слюни и пытаешься трахнуть?"
            m "У нее есть имя?"
            faw "Просто сделайте ее развращеннее и попробуйте еще раз.  Иначе я не смогу привести ее сюда."
    show screen genie
    hide screen petting
    with Dissolve(0.3)
    call screen main_room_menu




