

### The Gamble ###

label hg_pf_TheGamble:
    hide screen hermione_main
    with d3
    m "{size=-4}(Мне скучно...){/size}"
    g9 "{size=-4}(Должен ли я попробовать что-то совершенно другое?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        ">Это может быть {i}{size=+7}ее конец{/size}{/i}..."
        "\"(Да, давай!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump silver_requests

    call play_music("chipper_doodle")
    show screen hermione_main
    with d3

    m "Знаешь что? Я слишком много работаю в последнее время."
    call her_main("[genie_name]?","open","base") #247
    m "Ты меня слышала. В последнее время, ты только нагибаешься возле стола, а я трахаю твои дырочки и ты получаешь безумный оргазм."
    if whoring < 21:
        jump too_much

    call her_main("Я... Эмм... Что бы вы хотели сделать, тогда?","open","worriedL") #249
    m "Я собираюсь расслабиться, а ты будешь сидеть и подпрыгивать на моем члене."
    call her_main("Что?! [genie_name], я не-","angry","wide") #250
    m "Значит, Гриффиндору очки не нужны? Ну что ж. Я понял. Доброго дня, мисс Грейнджер."
    call her_main("Хорошо, хорошо. Так... Сколько очков дадите?","annoyed","frown") #252
    m "Как всегда. В последнее время я много работал. Думаю это справедливо."

    call play_music("playful_tension") # SEX THEME.

    call her_walk(400,325,1.25)

    show screen blkfade
    with fade

    hide screen blktone
    show screen bld1
    hide screen hermione_main

    call her_head("...Ладно. Просто позвольте мне... Вот так...","open","angryCl") #253

    #*Penetration transition*
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris

    call her_head("ААААААХХ! {image=textheart}","body_235") #254
    call her_head("Да...","body_236") #255

    hide screen hermione_main
    hide screen genie
    $ genie_chibi_xpos = -170 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 35
    $ g_c_u_pic = "bounce_ani_s"
    show screen desk_03
    show screen g_c_u
    hide screen blkfade
    with d3

    ">Гермиона начинает медленно скользить вверх и вниз по твоему члену."
    m "Ты можешь сделать это лучше! Подбери темп, шлюха!"
    call her_head("Aх... aх...{image=textheart}","body_237") #256
    "Она немного ускоряется..."
    $ g_c_u_pic = "bounce_ani"
    show screen g_c_u
    m "Ты меня слышишь, шлюха? Я сказал, давай быстрее, маленькая шлюха!"
    ">Ты чувствуешь, как дрожь проходит через нее с каждым оскорблением."
    m "Давай."
    call soft_slaps
    m "Быстрее."
    call soft_slaps
    #">You punctuate each word with a slap to her ass."
    call her_head("AAAХ! {image=textheart} {image=textheart} {image=textheart}","open_tongue","ahegao_raised",cheeks="blush") #257
    "Она начала еще быстрее прыгать."
    $ g_c_u_pic = "bounce_ani_f"
    show screen g_c_u
    call her_head("Да! Сильнее!","body_232") #258
    m "Быстрее."
    ">Ты кладешь под ее рубашку руку и начинаешь крутить и тянуть сосок."
    ">Ты начинаешь сильнее крутить ее сосок."
    call hard_slaps
    call her_head("БОЛЬНО! {image=textheart} {image=textheart}","smile","angry",cheeks="blush") #259
    m "Даже сейчас, я все еще беру на себя инициативу, ты самовлюбленная шлюха!"
    call her_head("Я- АХ! {image=textheart} Я- Aх-a!","body_235") #260
    m "Ты все еще утверждаешь, что все это только ради очков? Даже когда ты прыгаешь на моем члене? "
    call her_head("Я-Я-Я...  Э-Э-ТО... AХ! {image=textheart}","body_236") #261
    m "Хорошо. Докажи это. Если ты сможешь вытерпеть {i}ЦЕЛЫЙ МЕСЯЦ{/i} без сексуального удовлетворения."
    m "Я добавлю \"Гриффиндору\" {i}ТЫСЯЧУ{/i} очков и удвою очки любых услуг, которые ты решишь продать мне после этого."
    call her_head("!!!! СЕРЬЕЗНО?! (О боже, я так близко...)","soft","wide") #262
    m "Да. НО. Если не сможешь, ты будешь принадлежать мне. Больше никаких начислений очков. Ты будешь моей личной секс игрушкой. Мы договорились?"
    call her_head("Дааа...","body_236") #263
    m "Ответь мне четко, шлюха! Мы договорились?"
    call her_head("О БОЖЕ! ДА! ДА, МЫ ДОГОВОРИЛИСЬ!","body_234") #264
    call her_head("Я! Я-","body_234") #265
    stop music fadeout 1
    m "Хорошо."

    show screen blkfade
    with fade
    hide screen desk_03
    hide screen g_c_u
    $ hermione_SC.chibi.xpos = 500 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen genie

    ">Ты поднимаешь Гермиону с себя."
    call her_head("!!! Что вы делае-","shock","wide",cheeks="blush") #266
    m "Мы только что договорились. Конечно, если ты уже хочешь проиграть..."


    hide screen bld1
    hide screen blkfade
    with d3

    #show full sprite and chibi in middle

    call her_main("Я- Н-нет! Я была просто удивлена.","angry","worriedCl",cheeks="blush",emote="05") #267
    m "О, и прежде пока я не забыл."
    call cast_spell
    ">Ты наложил заклинание на Гермиону"
    m "Так-то."
    call her_main("Что вы только что сделали?","mad","wide",cheeks="blush")
    m "Я произнес заклинание, чтобы ты не чувствовала облегчения."
    m "В конце концов, из-за этого ты не проиграешь случайно! Это испытание характера, а не случайности. "
    call her_main("Я поняла.","annoyed","angryL",cheeks="blush") #*Looks at you cautiously*
    call her_main("...Спасибо.","open","baseL",cheeks="blush")
    m "Тебе нужно будет заходить каждое утро, чтобы я мог повторно применить его."
    call her_main("Я-- хорошо.","disgust","down_raised",cheeks="blush")

    call hermione_exit
    $ hermione_takes_classes = True

    m "Что ж, мои яйца вероятно разбухнут на некоторое время..."
    show screen blkfade
    with fade
    $ hg_pf_TheGamble_OBJ.points = 1
    $ hg_pf_TheGamble_Flag = True
    $ hg_pf_TheGamble_FlagA = True
    jump night_start

label hg_pf_TheGamble_complete:

    if hg_pf_TheGamble_FlagA:
        jump hg_pf_TheGamble_TellSnape
    elif hg_pf_TheGamble_FlagB:
        pass
    elif hg_pf_TheGamble_FlagC:
        jump hg_pf_TheGamble_MySlave_n


    if hg_pf_TheGamble_OBJ.points < 3:
        if hg_pf_TheGamble_OBJ.points == 1:
            #*Scene transitions to morning. Hermione enters.*

            call hermione_enter

            call her_main("","normal","worriedCl")
            call her_main("Д-доброе утро, [genie_name].","upset","wink")
            ">Гермиона не может перестать дергаться и ерзать."
            m "Доброе утро, мисс Грейнджер."
            m "Хм. Кажется, ты плохо спала. Что-то случилось?"
            call her_main("Я-нет! Я имею в виду- ладно.","disgust","narrow")
            m "...Если ты так говоришь."
            call cast_spell
            ">Ты накладываешь заклинание на Гермиону"
            m "Вот так. До скорого."
            call her_main("Я- да.","angry","worriedCl",emote="05")
            $ hg_pf_TheGamble_OBJ.points += 1
        elif hg_pf_TheGamble_OBJ.points == 2:
            #*Scene transitions to morning*

            m "Она опаздывает."
            pause 1.0
            ">Гермиона входит в комнату ошеломленная и рассеянная"
            call hermione_enter

            m "Мисс Грейнджер?"
            m "Утро доброе?"

            hide screen genie
            show screen chair_left
            hide screen desk
            show screen desk
            show screen genie_stand
            with d3
            #"You stand and move out from behind the desk."


            m "{size=+7}ШЛЮХА!{/size}"
            with hpunch
            "Гермиона прыгает"
            call her_main("Я- ОХ. Доброе утро [genie_name]...","grin","dead")
            ">Когда она затихает ты замечаешь ее неоднократное поглядываение на свой пах."
            m "Ты, кажется, не выспалась со вчерашнего дня. Ты спала вообще?"
            call her_main("Я-","base","down")
            ">Ее руки тянутся к клитору и груди, прежде чем она отдергивает их и убирает."
            call her_main("Я в порядке.","grin","dead")
            m "Ты уверена?"
            call her_main("Я, ах, мне нужно идти в класс.","soft","ahegao")
            m "Очень хорошо."
            call cast_spell
            ">Ты наложил заклинание на нее."
            call her_main("","base","down")
            ">Гермиона заглядывает на твой пах в последний раз, прежде чем уйти."
            $ hg_pf_TheGamble_OBJ.points += 1

        hide screen bld1
        hide screen hermione_main
        # hide screen desk
        # hide screen chair_left
        # show screen blkfade
        # with d3

        call hermione_exit
        $ hermione_takes_classes = True

        hide screen genie_stand

        jump day_main_menu
    else:
        jump hg_pf_TheGamble_MySlave
    return



    label hg_pf_TheGamble_TellSnape:
        #*Scene skips to Genie and Snape drinking wine by the fire.*
        show screen with_snape_animated
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        show screen fireplace_fire
        hide screen genie
        hide screen chair_right
        hide screen desk
        show screen desk

        hide screen snape_01 #Snape stands still.
        hide screen bld1
        hide screen snape_main
        with d3

        $ fire_in_fireplace = True

        hide screen blkfade
        with fade
        "Ты рассказываешь Снейпу о том, что случилось."
        sna_[5] "!!! Ты сделал что?! Ты совсем с ума сошел?!"
        m "Нет. Все находится в хороших руках. Хватит так волноваться."
        sna_[4] "Но-"
        m "Задумайся над этим."
        m "Сколько времени я потратил, чтобы подсадить ее на оргазмы? А теперь я заставил ее остыть."
        m "Независимо от того, сколько она мастурбирует или как отчаянно она трахается, она не может кончить."
        m "Хотя, она все еще может получить оргазм."
        m "С ее постоянно нарастающим возбуждением, я бы не дал ей много времени, прежде чем она сдастся. Неделя - полторы недели, максимум."
        sna_[11] "Хм... Что ж, будем надеяться на лучшее."
        m "Все наладится. Просто доверься мне."
        $ hg_pf_TheGamble_FlagA = False
        $ hg_pf_TheGamble_FlagB = True
        jump day_start

    label hg_pf_TheGamble_MySlave:
        #*Scene transitions to morning*
        pause 0.25
        # call play_sound("door") #Sound of a door opening.
        # $ walk_xpos=570 #Animation of walking chibi. (From)
        # $ walk_xpos2=400 #Coordinates of it's movement. (To)
        # $ hermione_speed = 2.1 #The speed of moving the walking animation across the screen.
        # call play_sound("door") #Sound of a door opening.
        # show screen hermione_walk_01
        # with d4
        # pause 2.1
        # $ hermione_SC.chibi.xpos = 500 #Near the desk.
        # show screen hermione_blink #Hermione stands still.
        # with d3
        ">Гермиона входит. Она не выглядит счастливой"
        call hermione_enter
        m "Мисс Грейнджер?"

        call her_walk(400,320,1.25)
        show screen blkfade
        with fade
        "Она ничего не говорит, она обходит стол."
        #show screen blktone
        m "Э..."


        call play_music("playful_tension") # SEX THEME.
        hide screen hermione_main
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_left
        show screen g_c_u

        hide screen hermione_blink #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        show screen bld1
        with d3
        #"You're interrupted as she jerks your pants down and swallows your cock to the root."
        ">Гермиона дергает твои брюки вниз и берет в рот твой член по самые яйца."



        m "МАТЕРЬ БОЖЬЯ! Я полагаю, это означает, что ты проиграла?"
        her "Gobble! Glurk! Gulp!"
        #"She says nothing, the only noise she makes are the desperate mewling and the sounds of gobbling your dick."
        ">Гермиона ничего не говорит, единственный шум, который она производит, - это отчаянное чавканье и заглатывание твоего члена."
        m "Именно это твой путь."
        ">Ты хватаешь ее голову и начинаешь трахать ее горло."
        m "ДА! ВОЗЬМИ ЕГО!"
        her "!!! Gobble -- Gobble -- Gobble!!!!"
        m "Используй свой язык, грязная сучка!"
        her "Gobble! Lick! Lick! Lick! Gobble!"
        m "(Черт. Последние пару дней были тяжелыми для меня. Я надеялся, что это случится раньше.)"
        ">Ты начинаешь долбить ее горло очень быстро, прежде чем кончаешь."

        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u # SUCKING
        with d3
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch


        her "GHT!!!!"
        m "АХ!!!"
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "Высоси все!"
        her "GULP! GULP! GULP! GULP!"
        m "Aх!"

        ">Когда ты освобождаешь ее, Гермиона падает на землю и дрожит."
        ">Она не кажется очень последовательной, поскольку она хватается за твою ногу."

        $ hermione_SC.chibi.xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_SC.chibi.ypos = 10
        $ h_c_u_pic = "hand_ani"
        call u_pause_ani
        # show screen h_c_u
        # hide screen g_c_u
        # with d3
        show screen blkfade
        with d3
        hide screen h_c_u # NOT SUCKING

        #her "Please- Give- Need- Please!"
        call her_head("Пожалуйста- Дайте- Еще- Пожалуйста!","grin","wink",cheeks="blush")
        m "Всего месяц! Ты не смогла даже продержаться неделю!"
        #her "Need- Please-"
        call her_head("Еще- Пожалуйста-","scream","wide",cheeks="blush")
        #">She scrambles to stand as you lift her by her hair and half toss her onto the desk."
        ">Гермиона вздрагивает, когда ты поднимаешь ее за волосы и бросаешь на стол."
        m "Ну, раз уж ты так вежливо спросила."

        #*penetration transition*
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris

        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u

        hide screen blkfade
        with d3


        #her "AAAAAAAAAAHHH! Biiiiiiig!!!!!"
        call her_head("АААААААХХ! Большооооооой!!!!!","open_tongue","ahegao_raised",cheeks="blush")
        m "Твоя киска стала более тугой?!"
        #her "AAAAH! NO! NO! STILL NEEEEED!!!"
        call her_head("ААААХ! НЕТ! НЕТ! ЕЩЕ!!!","mad","wide",cheeks="blush")
        m "Ох, правильно заклинание. Тебе просто нужно дождаться, пока я не кончу в тебя."
        #her "!!!"
        call her_head("!!!","mad","angry",cheeks="blush")
        ">Гермиона начинает гораздо быстрее двигаться."
        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        with hpunch
        #her "GIVE! GIVE! GIVE! GIVE! GIVE!"
        call her_head("ДАЙ! ДАЙ! ДАЙ! ДАЙ! ДАЙ!","base","ahegao_raised",cheeks="blush")
        ">С каждым толчком она становится все туже."
        m "ДА! ПОЧТИ! КОНЧАЮ!"
        ">Заклинание отменилось, когда ты начал спускать сперму во влагалище Гермионе."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen g_c_u
        pause .35
        with d3
        pause .15
        show screen remove_spell
        pause 1.7
        hide screen remove_spell
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc

        $ g_c_u_pic = "pause_sex"

        #her "!!!!"
        call her_head("!!!!","body_234")
        ">Гермиона пытается кричать, но может только тяжело дышать и дрожать, поскольку она, наконец, получила свой долгожданный оргазм."
        ">Ты смотришь на нее и ждешь, пока ее спазмы не утихнут."

        show screen blkfade
        with d3
        hide screen g_c_u

        m "Ты понимаешь меня, что я говорю?"
        ">Глаза Гермионы все еще бешенно бегают, но она кивает."
        m "Хорошо. Уговор - есть уговор. Теперь ты вся принадлежишь мне. Понимаешь?"
        #her "Yesss."
        call her_head("Дааа.","disgust","down_raised",cheeks="blush")
        m "Готова получить больше?"
        ">Все еще дергаясь на земле, она тихо говорит."
        #her "I... but... class..."
        call her_head("Я... но... класс...","shock","wide",cheeks="blush")
        m "Ох, ты не пойдешь сегодня на занятия."
        m "Я собираюсь полностью насладиться своим первым днем в качестве твоего владельца."
        ">Ты отправляешь сову за Снейпом."
        m "Теперь, что же делать дальше... Ага! Придумал!"
        ">Ты подходишь к Гермионе и поднимаешь ее. Ты держишь ее за бедра и раздвигаешь ноги."
        m "А теперь обними меня руками за шею и скажи, кто ты..."
        #her "Your whore."
        call her_head("Ваша шлюха.","grin","wink",cheeks="blush")
        m "Неправильно."
        #her "?"
        call her_head("?","scream","wide",cheeks="blush")
        m "Видишь ли, шлюхам платят. Шлюхи-это люди."
        m "Тебе не платят. Ты перестала быть человеком, когда ты продала себя мне."
        m "Теперь ты моя рабыня, моя игрушка. Мой маленький, милый инструмент."
        m "Скажи ЭТО."
        #her "I'm your fucktoy."
        call her_head("Я ваш инструмент.","disgust","down_raised",cheeks="blush")
        m "Тааак, теперь, что хочет инструмент?"
        ">Ты опускаешь ее, поддразнивая ее кончиком своего члена."
        #her "N-Nothing. A toy w-wants nothing. It's just used by its owner."
        call her_head("Н-ничего. Инструмент н-ничего не хочет. Он просто используется его владельцем.","wide_open_tongue","ahegao_mad",cheeks="blush")
        m "ОЧЕНЬ хорошо."
        ">Ты бросаешь ее на свой член."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #her "MY AAASS!!!"
        call her_head("МОЯ ЗАДНИЦА!!!","open_tongue","ahegao_raised",cheeks="blush")
        m "Чья задница?"
        ">Ты снимаешь ее со своего члена."
        #her "YOURS! YOUR FUCKTOY'S ASS!"
        call her_head("ВАША! ВАША ЗАДНИЦА!","soft","dead")
        ">В ее глазах видны отчаянные слезы."
        m "Поскольку это твой первый день, я буду нежным."
        m "Я дам тебе несколько вариантов."
        m "Ты хочешь, чтобы я трахал тебя в попку?"
        #her "Yes."215
        call her_head("Да.","wide_open_tongue","ahegao_mad",cheeks="blush")
        m "Как?"
        #her "Haaard. Pound me. Fill me with your cum!"
        call her_head("Сильнооо. Вставьте его. Наполните меня вашей спермой!","base","ahegao_raised",cheeks="blush")
        m "Как хочешь!"
        ">Ты надеваешь ее обратно на свой член и начинаешь биться об ее задницу, твой член никогда еще не был на столько твердый."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #her "MY ASS!!! YOU'LL BREAK IT!!"
        call her_head("МОЯ ЗАДНИЦА!!! ВЫ РАЗОРВЕТЕ Ее!!","open_tongue","ahegao_raised",cheeks="blush")
        ">Ты медленно поднимаешь ее."
        #her "AHH!! BREAK IT!! BREAK ME!! HARDER!!"
        call her_head("АХХ!! РАЗОРВИТЕ Ее!! РАЗОРВИТЕ Ее!! СИЛЬНЕЕ!!","body_236")
        call snape_enter
        sna_[1] "Что вы-"
        sna_[8] "!!!"
        #her "CUMMING!! MY ASS IS CUMMING!!"
        call her_head("КОНЧАЮ!! МОЯ ЗАДНИЦА КОНЧАЕТ!!","body_236")
        m "Как ты видишь, мисс Грейнджер нездорова..."
        ">Гермиона скользит вниз, и плюхается на твой стол. Она дрожит, ты пристраиваешься к ней сзади и начинаешь долбить ее еще сильнее."

        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        hide screen blkfade
        with d3

        m "Ты сможешь на завтра перенести свои занятия? А лучше на три дня?"
        #her "AAAAH! OH GOD!"
        call her_head("ААААХ! О БОЖЕ!","body_238")
        sna_[18] "Ха! Конечно!"
        #her "AGAIN!! CUMMING AGAIN!! {image=textheart} {image=textheart}"
        call her_head("ОПЯТЬ!! КОНЧАЮ!! {image=textheart} {image=textheart}","body_237")
        sna_[21] "(Это могут быть, самые счастливые дни в моей жизни!)"
        call snape_leave
        ">Гермиона продолжала кричать и двигать попой на твоем члене. Ты совершенно уверен, что она не заметила разговора."
        #her "I'm going insane! Your dick is driving your fucktoy insane!"
        call her_head("Я начинаю сходить с ума! Ваш член сводит меня с ума!","body_236")
        m "Это все ты и твои слова!"
        #her "CUMMING! STILL CUMMING!"
        call her_head(" КОНЧАЮ! ЕЩе КОНЧАЮ!","body_234")
        m "Позволь, я присоединюсь к тебе!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc


        #her "MY ASS! SO HOT!"
        call her_head("МОЯ ЗАДНИЦА! ГОРЯЧО!","body_235")
        #her "FILLING MY ASS!"
        call her_head("МОЯ ЗАДНИЦА ПОЛНА!","body_236")
        m "ТЕБЕ НРАВИТСЯ?"
        #her "YES!!!! {image=textheart} {image=textheart}"
        call her_head("ДА!!!! {image=textheart} {image=textheart}","body_234")
        m "ЕЩе НЕ МНОГО!"
        ">Гермиона пытается кричать, из-за того, что ты кончаешь в ее попу, но она только тяжело дышит, падая на твой стол, и дрожит."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc

        m "Итак, что хочет... Игрушка?"
        ">Гермиона лежит на столе и дрожит, не реагируя на твои слова."
        $ g_c_u_pic = "pause_sex"
        m "Да, она потеряла сознание. Ей запомнятся эти три дня."
        m "Так, как будем коротать это время..."
        $ hg_pf_TheGamble_FlagB = False
        $ hg_pf_TheGamble_FlagC = True
        jump night_start

    #transition to nighttime menu
    #after daytime menu

    label hg_pf_TheGamble_MySlave_n:
        #$ hermione_SC.chibi.xpos = 500 #Near the desk.
        #$ hermione_SC.chibi.ypos
        #show screen hermione_blink #Hermione stands still.
        #hide screen blkfade
        #with d3
        #$ h_c_u_pic = ""
        #show screen h_c_u

        her "Хм... Чт... Где..."
        m "Добрый вечер, игрушка. Я уже начал волноваться."
        her "Ох... O боже... Я - мы - спор-"
        m "Ты проиграла спор, да, и потом сдалась. Я хочу развлечься. Надеюсь ты не против."
        her "Я потеряла сознание?"
        m "Ты не заметила?"
        her "...Заметила, что?"
        m "Это."
        "Ты выдергиваешь анальные шарики одним движением."
        her "!!!!"
        "Она начала подниматься, но тут же падает обратно на стол."
        m "Теперь, когда ты более или менее в своем уме, я повторю еще раз. У нас был уговор."
        her "Я-"
        "Ты встаешь позади нее, схватываешь ее бедра и насильно засовываешь член ей в анус."
        m "Ты сделала свой выбор. У тебя был шанс. Но ты проиграла. Так что теперь ты, вся моя."
        "Ты подносишь свою руку к ее влагалищу и засовываешь пальцы внутрь."
        m "ЭТО принадлежит мне."
        her "Aх-"
        "Ты вынул пальцы. Ты шлепаешь ее по большой и мягкой заднице."
        m "ЭТО тоже МОЕ."
        her "ХАХ-AХ-"
        "Ты начинаешь засовывать пальцы ей в анус, параллельно засовывая член в ее киску."
        m "Это ясно?"
        her "..."
        her "*всхлип* да."
        m "Хорошо."
        "Ты открываешь ящик стола, берешь черный кожаный воротник и бросаешь его перед ее лицом."
        m "Надень его."
        "Удрученная, она медленно надевает его."
        m "Несколько ключевых моментов. Этот ошейник заколдован. Только ты можешь надеть его и только если захочешь. Если бы ты не хотела, он бы не закрылся."
        m "Только я могу его снять. Если ты откажешься от моих приказов, он активирует афродизиак, а также то заклинание, которое я применял на тебя в течение последних трех дней, пока ты не подчинишься."
        m "Я, конечно могу, активировать его и по желанию."
        m "Теперь встань на колени."
        "Как только она встала на колени, ты рвешь ее рубашку."
        "Ты грубо хватаешь ее за сиськи, дергая их вперед, и обхватывая ими свой член."
        "Ты скручиваешь ее соски, а после засунул член между ее грудями."
        her "...Aх... ха... aх..."
        m "Тебе нравится, игрушка?"
        her "...Aх... н-нет..."
        m "Скажи мне правду, игрушка. Тебе нравится это?"
        her "Н-нет- AХ-АХ-AХ!!!"
        "Ее дыхание становится еще тяжелее, и ее руки быстро направляются к киске."
        her "Я -AХ!- Я-"
        "Ее дыхание замирает, как она отчаянно масстурбирует свою киску пальцами."
        her "Н-AХ!- -ХАХ!- ДА! {image=textheart} {image=textheart} ДА! МНЕ НРАВИТСЯ!"
        "Ее бедра начинают качаться, и ты сжимаешь ее сиськи еще сильнее."
        her "AХ! {image=textheart}"
        m "Ты собираешься кончать?"
        her "ДА!! {image=textheart}"
        m "Ты собираешься кончить от того, что я шлепаю по твоим сиськам?"
        her "*Всхлип* ДА!!! {image=textheart}"
        m "Нет. Ты не можешь кончить раньше меня."
        her "!! АХ! НЕТ! ПОЖАЛУЙСТА!"
        m "Скажи мне, какая ты рабыня!"
        her "ХОЗЯИН! МОЙ ХОЗЯИН! ПОЖАЛУЙСТА, КОНЧИТЕ В МЕНЯ, ХОЗЯИН!"
        m "Что? Разве я не ясно выразился? Ты моя маленькая игрушка. Чего хочет эта маленькая игрушка?"
        her "КОНЧАЙТЕ НА МЕНЯ, МОЙ ГОСПОДИН! ПОКРОЙТЕ МЕНЯ СПЕРМОЙ! УТОПИТЕ МЕНЯ В НЕЙ!"
        m "Опять ты хорошие слова подбираешь!"
        "Когда ты кончаешь на ее волосы, лицо и дерзкие, покрасневшие сиськи, тело Гермионы начинает дрожать."
        "Ты не можешь ее держать, она начинает прыгать на месте."
        "Ты не можешь сказать, сколько раз боль, вызванная поркой, заставляет ее кончить."
        "В конце концов, она падает на тебя. Ты чувствуешь ее дыхание на своем члене."
        m "Посмотри на себя."
        m "Вся эта гордость и самоуверенность, что у тебя была в начале, а теперь ты упала на меня, пускаешь слюни на мой член, и..... ты даже не слышишь меня, не так ли?"
        "Ты хватаешь ее за волосы и шлепаешь по лицу."
        m "Подъем!"
        her "АХ!! {image=textheart} АХ!! {image=textheart} АХ!! {image=textheart}"
        "Твоя пощечина вызывает дрожь через ее тело."
        "Когда ты смотришь на ее бедра, ты чувствуете, что твой член становится больше."
        m "...Я не могу ждать до утра."
        m "Давай. Вставай."
        "Ты начинаешь бить по ее лицу своим членом, осторожно, чтобы не ударить достаточно сильно, чтобы отправить в нокаут."
        her "..."
        "Она стонет, как только ты бьешь членом по ее лицу."
        m "Вставай. Вставай. Теперь, что ты должна сделать?"
        "Ты отпустил ее волосы. Ее глаза все еще бешенные, когда она открывает рот, то пытается поймать языком твой, покачивающийся из стороны в сторону, член."
        "Сначала она фыркает, и тебе хочется подразнить ее. Пока ты думаешь, удасться ли словить ей член, она уже держит его во рту."
        "Она медленно посасывает твой член, и все глубже и глубже заталкивает его в горло."
        her "Glurk... Gobble... Lick..."
        m "Нужно ли мне объяснять, что произойдет, если ты не увеличишь темп?"
        "Угроза, кажется, разбудила ее."
        her "GLURK! GOBBLE! GOBBLE! GULP!"
        "Поскольку ее движения становятся более быстрыми, ты не можешь остановить шевелить своими бедрами."
        m "Видишь? Это было не так трудно. Теперь, глубоко вздохни через нос..."
        "Ты хватаешь ее за мокрые, спутанные волосы и заставляешь держать ее твой член во рту на столько, сколько она продержится."
        her "..............."
        m "Ох, да. Твое горло самое лучшее."
        her ".............................."
        m "Собственно, я не мог больше думать о какой-либо другой части твоего тела."
        her ".............................."
        m "Как будто ты была моей личной игрушкой!"
        her "......"
        m "Полагаю, я действительно благословлен."
        her "!!!"
        m "Хм? Что такое?"
        "Вы смотрите, как бедра Гермионы начинают трястись."
        her "!!!!!!!"
        m "Ох, это просто бесценно!"
        "Руки Гермионы приближаются к ее киске."
        her "!!!!!!!!!!"
        m "Вот я, душу тебя своим членом, и ты не вырываешься, ты на самом деле мастурбируешь!"
        "Она дико мастурбирует себя пальцами, а другой усердно трет твои яйца."
        her "!!!!!!!!!!!!!!"
        m "Я не знал, что я мог сделать, чтобы заслужить такую замечательную игрушку, как ты! Теперь получи!"
        her "GHT!!!!!!!!"
        "Глаза твоей игрушки откидываются назад, когда ты наполняешь ее горло, ее рука перестала массировать твои яйца и теперь скручивает один из сосков."
        her "GULP! GULP! GULP! GULP! GULP! GULP! GULP!"
        m "ВСЕ ЭТО! Тебе в глотку!"
        "Ты сильно держишь за ее волосы пока она глотает."
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "ДАВАЙ! ЕЩе НЕМНОГО!"
        her "GULP! GULP! GULP! GULP!"
        "Ты отталкиваешь ее от своего члена. Это требовало больше усилий, чем ты ожидал, и вознаграждается интересным звуком, и еще более интересным ощущением."
        $ renpy.play('sounds/pop02.mp3')
        "Не закончив, ты разбрызгиваешь по ее лицу еще больше своей спермы."
        m "Все!"
        "Ты отпустил волосы своей игрушки, и она падает на землю, по-прежнему дергаясь."
        m "Oooх, нет. Нет, ты не будешь. Ты не потеряешь сознание снова."
        "Ты слегка встряхиваешь ее, пытаясь разбудить."
        m "Я должен был догадаться. Вот."
        "После того, как ты уверен, что она снова не упадет в обморок, ты вручаешь ей листок бумаги."
        m "Возьми этот пропуск и иди прими душ. Пароль Лимонный фреш. Потом иди спать."
        "Она кивает тебе. Ты замечаешь, что она пытается сформировать последовательность мыслей."
        m "Не ошибись. Ты моя маленькая игрушка, я буду тебя использовать пока мне не надоест."
        m "Это означает, что я должен держать тебя в хорошем состоянии."
        m "Иди."
        "Гермиона покидает твой кабинет."
        $ hg_pf_TheGamble_Flag = False
        $ per_quest_30c = False

        jump day_start
