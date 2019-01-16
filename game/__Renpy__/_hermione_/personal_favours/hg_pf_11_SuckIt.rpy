

label hg_pf_SuckIt: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Попросить ее сделать мне минет?){/size}"
    else:
        m "{size=-4}(Попросить ли девочку сделать мне еще раз минет?){/size}"

    if hg_pf_TouchMe_OBJ.points < 1:
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    if hg_slythCheer_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, пойди и переоденься."
                call her_main("Во что?","open","worriedL",xpos=140)
                m "В болельщицу Слизерина."
                if whoring >= 10:
                    call her_main("Слизерина?","scream","angryCl")
                    m "Всего на минутку."
                    call her_main("...","angry","worriedCl",emote="05")
                    call her_main("Ладно.","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_slythCheer_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Нет, не сейчас.)\"":
                pass

    call set_u_ani("blowjob_ani","hand_ani",0,10)
    $ mouth_full_of_cum = False

    call bld

    #Intro
    if hg_pf_SuckIt_OBJ.points == 0: #<=== EVENT 01   FIRST EVENT

        m "[hermione_name]?"
        call her_main("Да, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "Я хочу сегодня дать \"Гриффиндору\" 55 очков ..."
        m "Если ты отсосешь мне..."

        if whoring < 15: # LEVEL 05
            jump too_much

        call her_main("Ох...","open","down")
        call her_main("Хорошо.","base","down")
        m "Правда? Так просто?"
        call her_main("Да. Я знаю, что я должна возмутиться...","angry","down_raised")
        call her_main("Но я этого не делаю...","angry","base")
        call her_main("Наверное, я просто рада, что могу помочь своему факультету...","base","down")
        call her_main("И если для этого я должна положить ваш пенис себе в рот, то пусть будет так...","upset","closed")
        m "Ну, хорошо."
        call her_main("Хотя...","angry","down_raised")
        m "Поздно! Ты уже сказала \"да\"!"
        call her_main("Я знаю...","grin","worriedCl",emote="05")

        call her_walk_desk_blkfade

        label blowjob_jumping:  # BLOWJOB
        call play_music("playful_tension") # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        call her_chibi("hide")
        show screen chair_left
        call u_play_ani
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        show screen bld1
        call her_head("*Slurp!* *Gulp!* *Slurp!*",xpos="base",ypos="base")
        m "Да..."
        m "Попытайся глубже..."
        her "*Gulp!* *Gobble!* *Gobble!*"
        m "Да, мне нравится. Хорошо."
        her "*Slurp!* *Gltch!* *Gulp!*"
        m "Да, вот так, хорошая девочка."

        menu:
            m "Хм..."
            "\"Что с твоим клубом \"ДПМ\"?\"":
                her "*Slurp?*"
                call u_pause_ani
                call her_head("О, ну...","angry","down_raised")
                call her_head("Мы по-прежнему активны, но...")
                call u_play_ani
                her "*Slurp!* *Gobble!*"
                call u_pause_ani
                call her_head("Но мы не получаем такой популярности и поддержки, как я думала...","angry","wink")
                call u_play_ani
                her "*Slurp!* *Gulp!* *Gulp!*"
                m "Ох... Как хорошо..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Хм..."
                m "Так что, ты не возражаешь продавать мне сексуальные услуги, позволяя мне играть с твоими сиськами и тому подобное..."
                her "*Gobble!* *Gltch!* *Slurp!*"
                m "А потом осуждать такое поведение перед другими студентами."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Ты извращенка и маленькая лицемерка."
                her "*Gulp--"
                call u_pause_ani
                call her_head("Мы не за это выступаем, [genie_name].","angry","base")
                m "А за что?"
                call her_head(" \"ДПМ\" о гендерном равенстве.","open","closed")
                call her_head("Мы не так сильно против продажи сексуальных услуг...")
                call her_head("По этому мы против гендерного неравенства, которое создает продажа сексуальных услуг...")
                m "Хм..."
                m "Этот разговор начинает мне надоедать..."
                m "Соси, прежде чем мы продолжим."
                call her_head("Конечно, [genie_name].","soft","ahegao")
                call u_play_ani
                her "*Gobble!* *Slurp!* *Slurp!*"
                m "Да, так намного лучше..."
                m "Но ты все еще не одобряешь продажу услуг, верно?"
                her "*Slurp--"
                call u_pause_ani
                call her_head("Да, это не одобряется...","upset","closed")
                m "И все же, ты самая главная лицемерка на сегодняшний день."
                call her_head("Но какой у меня есть выбор?","upset","closed")
                call her_head("Меня поставили в очень трудное положение...")
                m "Член, [hermione_name]."
                call her_head("Ой, простите...","upset","closed")
                call u_play_ani
                her "*Slurp!* *Gulp!* *Gltch!*"
                her "*Slurp--"
                call u_pause_ani
                call her_head("Однажды у нас была встреча сразу после того, как я продала вам услугу, [genie_name].","angry","base")
                call her_head("Я должна была произнести речь в грязной и запачканной форме...")
                call her_head("Это было, ужасно...")
                m "Но тебе все же это понравилось...."
                call her_head("Ну...","angry","down_raised")
                m "Признай это."
                call her_head("...............","angry","base")
                m "Да, я так и знал. Ты получила удовольствие от этого, маленькая извращенка."
                call her_head("Я полагаю, что это было неловко и интересно одновременно...","angry","down_raised")
                call her_head("И это заставило меня чувствовать себя еще хуже.")
                m "Бедняжка."
                m "Возьми член обратно в рот."
                call her_head("Хорошо, [genie_name].","angry","base")
                call u_play_ani

            "\"Твои родители должны гордиться тобой....\"":
                her "*Slurp--"
                call u_pause_ani
                call her_head("Да, я считаю, что они...","smile","happyCl")
                call her_head("Я была отличной студенткой, несмотря на то, что родилась в семье маглов и все такое...","base","happyCl")
                call her_head("Хотя сначала они хотели отправить меня в \"Богус\", школу-интернат.","angry","base")
                call her_head("Потребовалось приложить немного усилий, чтобы убедить их, что \"Хогвартс\" приличное заведение.","base","happyCl")
                m "Да, действительно, вполне приличное заведение."
                m "Возьми член обратно в рот [hermione_name]."
                call u_play_ani
                her "*Slurp!* *Gulp!* *Gobble!*"
                m "Да, просто продолжай в том же духе..."
                her "*Slurp!* *Gltch!* *Gulp!*"
                m "Хорошо, хорошо..."
                m "Итак, что бы сказали твои родители, если бы увидели тебя сейчас, [hermione_name]?"
                her "*Slurp--"
                call u_pause_ani
                call her_head("Они бы этого не поняли...","open","down")
                call her_head("Но мне все равно.")
                call her_head("Я не боюсь \"испачкать руки\" и сделать то, что нужно.","upset","closed")
                m "Ты, как бы, бунтуешь, не так ли?"
                call her_head("Хм... Я думаю, что да.","angry","wink")
                m "Тогда возвращайся к отсосу. Покажи как ты умеешь бунтовать."
                call u_play_ani
                her "*Slurp!* *Slurp!* *Slurp!*"

            "\"Расскажи мне о \"Гриффиндоре\".\"":
                her "*Slurp--"
                call u_pause_ani
                call her_head("Что я могу рассказать, что вы еще не знаете, [genie_name]?","soft","baseL")
                m "Да... Хм... Я конечно все знаю."
                m "Но я хочу услышать, как много ты знаешь."
                m "Проверить твои знания, это вроде теста."
                call nar(">Как только ты упомянул \"тест\" у Гермионы начали светиться глаза от восторга.")
                call her_head("ХОРОШО. Но мне нужно время собраться с мыслями...","smile","happyCl",emote="06")
                call u_play_ani
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Ох, да... Используй столько времени, сколько тебе нужно, [hermione_name]."
                her "*Slurp!* *Gulp!* *Slurp!*"
                her "*Gulp--"
                call u_pause_ani
                call her_head("Факультет \"Гриффиндор\" был основан Годриком Гриффиндором, таким образом получилось название.","open","down")
                call her_head("Гербовое животное \"Гриффиндора\" лев...")
                call her_head("Алый и золотой, цвета.","open","closed")
                call u_play_ani
                her "*Gulp!* *Slurp!* *Slurp!*"
                call u_pause_ani
                call her_head("Профессор Минерва МакГонагалл - директор нашего факультета.","open","closed")
                call her_head("\"Гриффиндор\" подчеркивает черты мужества...")
                call her_head("А также \"храбрость, смелость и благородство\"...")
                call her_head("И поэтому гриффиндорцы обычно считаются храбрыми, но безрассудными...")
                call u_play_ani
                her "*Slurp!* *Slurp!* *Slurp!*"
                call u_pause_ani
                call her_head("\"Гриффиндору\" соответствует стихия-огонь...","open","closed")
                call her_head("И по этой причине были выбраны цвета: красный и золотой.")
                call u_play_ani
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Хм..."
                m "Ну, я думаю, что могу немного высмеять тебя..."
                her "*Чавк?*"
                m "Ну, с твоим факультетом, олицетворяющим мужество, справедливость и все такое..."
                m "Но тем не менее, ты - шлюха..."
                call u_pause_ani
                call her_head("[genie_name]!","scream","angry",emote="01")
                m "Но если честно..."
                m "\"Смелость, мужество, огонь, безрассудство\"..."
                m "Такие качества описывает твою личность довольно хорошо..."
                call her_head("[genie_name]...","base","base")
                call u_play_ani
                her "*Gobble!!* *Gltch!!* *Gobble!!!*"
                m "Хорошая девочка..."

        m "Хорошо..."
        her "*Gobble!* *Slurp!* *Slurp!*"
        m "Хорошо... Туда-сюда, туда-сюда... Хорошая девочка."
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        call u_pause_ani
        call her_head("[genie_name]... Я... шлюха.","open","down")
        m "Что?"
        call u_play_ani
        her "*Slurp-Slurp-Slurp!*"
        call u_pause_ani
        call her_head("Я действительно шлюха и наслаждаюсь вашим членом.","angry","base")
        m "О, да, да... Говори еще, мне это нравится."
        call u_play_ani
        her "*Slurp!* *Gulp!* *Slurp!*"
        call u_pause_ani
        call her_head("Пожалуйста, [genie_name]. Кончите на меня.","soft","ahegao")
        with hpunch
        g4 "Ах! Ты маленькая...!!!"
        g4 "{size=-4}(Скоро кончу. Стоит ли предупредить ее?){/size}"

        menu:
            m "..."
            "-Предупредить-":
                call her_head("Да, я люблю сосать и--","soft","ahegao")
                g4 "Берегись, [hermione_name]! Кончаю!"
                call her_head("!!!","angry","wide")
                call ctc
                hide screen bld1
                call blkfade

                call set_u_ani("cum_in_mouth_ani")
                call u_play_ani
                ">Гермиона быстро вставляет твой член в рот и продолжает сосать его с большой страстью."
                call cum_block
                g4 "{size=+7}АХ!{/size}"
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Еще немного!"
                her "*Gulp!* *Gulp!* *Gulp!*"
                call hide_blkfade
                call ctc

                call bld
                m "Я думаю, что закончил."
                call u_pause_ani
                call her_head("..............","cum","worriedCl")
                m "С тобой все в порядке, [hermione_name]?"
                call her_head("Да, [genie_name]...","grin","dead")
                call her_head("Вы так много кончили...")
                m "Тебе удалось все проглотить."
                call her_head("Да... Я думала, что задохнусь...","grin","dead")
                call her_head("Но я пообещала себе, что не отпущу ваш пенис, несмотря ни на что!")
                m "Хорошая девочка."
                call her_head("Спасибо, [genie_name].","grin","dead")
                call her_head("Но... Вы так много кончили...")
                call her_head("Я чувствую, как будто меня только что покормили...","soft","ahegao")
                call her_head("Мой желудок полон...")
                g9 "Да, я накормил тебя своей спермой!"

                if daytime:
                    call her_head("Я думаю, что могу пропустить обед и пойти прямо на урок.","soft","ahegao")
                else:
                    call her_head("Я думаю, что могу пропустить ужин...","soft","ahegao")

                call her_head("Могу ли я получить очки?","angry","wink")
                call ctc
                call blkfade

            "-Не предупреждать-":
                call her_head("Да, я люблю сосать и--","soft","ahegao")
                call cum_block
                g4 "{size=+7}Шлюха!{/size}"
                call her_head("?!!","shock","wide")
                hide screen bld1
                call set_u_ani("cum_on_face_ani")
                call u_play_ani

                call ctc

                call bld
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_07.png"
                call her_head("[genie_name]...","shock","wide")
                g4 "Не двигайся, [hermione_name]."
                g4 "Успокойся и возьми его."
                g4 "Ах! Ты маленькая шлюха! Ты делаешь все правильно, что мне трудно не кончить, [hermione_name]!"
                call her_head("..............","angry","base",tears="soft")
                m "Фух..."
                call set_u_ani("cum_on_face_blink_ani")
                call her_head("..............","normal","worriedCl")
                m "Хорошо, я все..."
                call her_head(".................","open","base")

                if daytime:
                    her "Мои занятия вот-вот начнутся..."
                else:
                    pass

                m "Просто вытри все, и будет хорошо."
                call her_head("............","open","base")
                m "Или ты хочешь..."
                call her_head("А?","angry","worriedCl",emote="05")
                m "Выйти на улицу в таком виде."
                m "И пусть все увидят, какая ты лицемерная маленькая шлюшка."
                call her_head("Конечно, же нет, [genie_name]!","angry","worriedCl",emote="05")
                call ctc
                call blkfade

                stop music fadeout 1.0

                if daytime:
                    m "Тебе бы лучше пойти на занятия, пока не опоздала..."
                else:
                    m "Уже довольно поздно..."
                    call her_head("Да...","angry","worriedCl",emote="05")

                call her_head("Могу ли я получить очки, [genie_name]?","upset","wink")
                call blkfade
                $ aftersperm = True

    #Second Event.
    elif hg_pf_SuckIt_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base")
        m "Как насчет еще одного минета?"
        call play_music("playful_tension") # SEX THEME.
        call her_main("[genie_name], как вы смеете предлагать такое одной из своих учениц!","scream","angry",emote="01")
        m "Чт...?"
        call her_main("Это неприлично для человека вашей должности.","scream","angry",emote="01")
        call her_main("Вам должно быть стыдно [genie_name]!","angry","angry")

        menu:
            m "???"
            "\"Ладно. Не хочешь очков. Уходи!\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("[genie_name], успокойтесь, пожалуйста.","grin","worriedCl",emote="05")
                m "Уходи, [hermione_name]."
                call her_main("[genie_name], пожалуйста, я ничего из этого не имела в виду...","grin","worriedCl",emote="05")
                m "Что?"

            "\"Эм... Что, прости?\"":
                stop music fadeout 1.0
                call her_main("*Giggle*","base","base")
                m "А?"
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("Я вас поняла... [genie_name].","grin","worriedCl",emote="05")
                m "Что?"

        call her_main("Ну, в последнее время много всего произошло...","base","base")
        her "У меня было так много новых впечатлений и это изменило мой взгляд на некоторые вещи..."
        her "Я просто пыталась представить, как \"старец\" отреагирует на это."
        m "Так..."
        g4 "Ты прикалывалась надо мной?"
        call her_main("Эм... Простите [genie_name], я не хотела...","angry","worriedCl",emote="05")
        g4 "Ты противная маленькая девочка! Ты должна быть наказана!"
        g9 "И я накажу тебя, своим членом!"
        call her_main("...............................","angry","worriedCl",emote="05")

        call blkfade #Needs to be active first!
        jump blowjob_jumping

    #Third Event.
    elif hg_pf_SuckIt_OBJ.points >= 2 and whoring < 21:
        call play_music("playful_tension") # SEX THEME.
        m "Соси мой член, [hermione_name]."
        call her_main("Конечно...","base","base",xpos="mid",ypos="base")

        call her_walk_desk_blkfade

        call play_music("playful_tension") #HERMIONE
        hide screen genie
        call her_chibi("hide")
        show screen chair_left
        call u_play_ani
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        show screen bld1
        call her_head("*Slurp!* *Slurp!* *Gulp!*","","",xpos="base",ypos="base")
        m "Да, хорошая девочка..."
        her "*Slurp!* *Gobble!* *Slurp!*"

        call play_sound("knocking") #Sound someone knocking on the door.
        call nar("> *Тук-тук-тук!*")
        her "{size=+7}!!!{/size}"
        m "Эм?"

        if daytime:
            m "Кто бы это мог быть?"
        else:
            m "Кого принесло в такой поздний час?"

        call u_pause_ani

        if not luna_known:
            call her_head("([genie_name], что мне делать?)","shock","wide")
            m "Просто продолжай сосать мой член, [hermione_name]. Это тебя не касается."
            sna "Альбус? Ты здесь? Я хочу поговорить с тобой."
            call her_head("(Это профессор Снейп!)","angry","base")
            call her_head("([genie_name], пожалуйста, скажите, что бы он ушел, умоляю вас!)")

            menu:
                m "..."
                "\"Пожалуйста, заходи, Северус.\"":
                    $ mad = 30
                    stop music fadeout 1.0
                    call her_head("([genie_name], нет!)","angry","angry",emote="01")

                    call nar(">Гермиона начинает сжимать твои яйца.")
                    g4 "Ай!"
                    hide screen bld1
                    # SNAPE COMES IN
                    call play_sound("door") #Sound of a door opening.
                    call sna_chibi("stand","door","base")
                    pause.2
                    call sna_walk("door","mid",4)
                    pause.2

                    call bld
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME

                    call sna_head("Хорошо, ты здесь.","snape_01",xpos="base",ypos="base")
                    call u_play_ani
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("Слушай, надо кое-что обсудить...","snape_06")
                    call sna_head("Хм...?","snape_05")
                    call sna_head("Джинни? Ты в порядке?")
                    her "{size=-4}(Джинни?!! Как, она тоже здесь?!){/size}"
                    her "{size=-4}(Нет, пожалуйста! Я умру от стыда!){/size}"
                    m "Да, Северус, я в порядке..."
                    her "{size=-4}(Что? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
                    call sna_head("Что ты...","snape_05")
                    m "Эм... Просто восхищаюсь...{w} шкафом."
                    m "Пожалуйста, продолжай..."
                    call sna_head("...............","snape_05")
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    m "Ты хотел что-то обсудить?"
                    call sna_head("Да. Эта девочка, Гермиона.","snape_06")
                    her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                    m "Ох... Что такое?"
                    call sna_head("Ты обещал, что позаботишься о маленькой ведьме..","snape_04")
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("Но она по-прежнему доставляет мне неприятности!","snape_04")
                    call sna_head("Ее тактика изменилась...")
                    call sna_head("Но количество беспокойства, которое ей удается доставить мне, остается неизменным...","snape_03")
                    m "Понятно... ах..."
                    call sna_head("Клянусь, эта девчонка сводит меня с ума!","snape_10")
                    g4 "Да, она и меня сводит с ума.... Ах..."
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("Ты позаботишься об этом?","snape_04")
                    m "Да. Она получит по заслугам."
                    call sna_head("Хорошо. Это все, что я хотел услышать.","snape_06")

                    if daytime:
                        m "Что ж, хорошего дня, Северус..."
                        call sna_head("Да, спасибо и тебе.","snape_06")
                    else:
                        m "Доброй ночи, Северус."
                        call sna_head("Взаимно...","snape_06")

                    # SNAPE LEAVES
                    hide screen bld1
                    with d3

                    call sna_chibi("stand","mid","base",flip=True)
                    pause.2
                    call sna_walk("mid","leave",3)
                    stop music fadeout 1.0
                    call ctc
                    call blkfade

                    call play_music("playful_tension") # SEX THEME.
                    ">Гермиона ничего не говорит. Ее лицо все красное из-за смущения, стыда и волнения."
                    ">При своем состоянии она, все же продолжает выполнять свою задачу."
                    g4 "(Сейчас кончу!)"
                    call hide_blkfade

                "\"Я занят, Северус.\"":
                    call her_head("(Спасибо, [genie_name].)","angry","base")
                    sna "Занят? Чем?"
                    sna "Все, что ты делаешь, это сидишь на заднице целый день в этом кабинете."
                    sna "Мне действительно нужно поговорить с тобой."
                    m "Я сказал, что занят, Северус."
                    m "Понятно? Я \"занят\"!"
                    sna "Ох... Ааа, ты в этом смысле \"Занят\"? Понятно!"
                    sna "Ну, тогда я поговорю с тобой позже."

        #Scene with Luna.
        else:
            call her_head("([genie_name], что мне делать?)","shock","wide")
            m "Просто соси мой член, [hermione_name]. Это тебя не касается."
            lun "[l_genie_name]? Вы здесь? Мне нужно поговорить с вами."
            call her_head("(Это Полумна!)","angry","base")
            call her_head("Пожалуйста, [genie_name], пожалуйста, скажите, что бы она ушла, умоляю вас!")

            menu:
                m "..."
                "\"Пожалуйста, входи, [luna_name].\"":
                    $ mad += 10
                    stop music fadeout 1.0
                    call her_head("([genie_name], нет!)","angry","angry",emote="01")
                    hide screen bld1
                    with d3

                    #Luna comes in
                    call play_sound("door") #Sound of a door opening.
                    $ luna_chibi("stand", 400, 250)
                    $ changeLuna(1, 1, 4, 1)
                    call bld
                    lun "Здравствуйте [l_genie_name]."
                    $ g_c_u_pic = "blowjob_ani" # sucking
                    call u_play_ani

                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ changeLuna(1, 2, 4, 1)
                    lun "Эм, может вы повернетесь ко мне лицом, сэр..."
                    m "Не могу, сейчас я немного занят."
                    $ changeLuna(1, 1, 5, 1)
                    lun "Чем?."
                    her "{size=-4}(Что? *Slurp...?* *Gulp...?*){/size}"

                    menu:
                        "-Сказать правду-":
                            if collar == 0:
                                $ collar = 5
                            m "Мисс Грейнджер помогает мне, пока мы говорим."
                            $ changeLuna(1, 2, 5, 4)
                            lun "Вы имеете в виду, что Гермиона под вашим столом..."
                            $ changeLuna(10, 1, 4, 9)
                            lun "Удовлетворяет вас, пока мы разговариваем."
                            ">Лицо Гермионы становится красным от стыда, но она продолжает делать минет."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Ну да."
                            lun "В таком случае, я думаю, мне лучше уйти, раз вы заняты с другим студентом."
                            m "Спасибо [luna_name]"

                            if daytime:
                                m "Удачного дня.."
                                $ changeLuna(1, 1, 1, 5)                                                       # SNAPE
                                lun "Да, спасибо. Я знаю, что вы будете..."
                            else:
                                m "Доброй ночи, [luna_name]."
                                $ changeLuna(1, 1, 4, 1)
                                lun "Доброй ночи [l_genie_name].."
                                $ changeLuna(5, 2, 3, 1)
                                lun "Доброй ночи Гермиона..."

                        "-Соврать-":
                            m "Эм... Просто восхищаюсь...{w} шкафом."
                            m "Продолжай..."
                            lun "..............."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Ты хотела что-то обсудить?"
                            $ changeLuna(2, 1, 4, 1)
                            lun "Да. Про мозгошмыгов."
                            her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                            m "Ох... Что не так?"
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            lun "Независимо от того, что бы я ни делала, не могу от них избавиться!"
                            $ changeLuna(1, 2, 4, 1)
                            lun "Кажется, что все только становится хуже!"
                            m "Ясно... ах..."
                            $ changeLuna(1, 1, 4, 1)
                            lun "Они сводят меня с ума, я больше не могу справляться"
                            g4 "Да, они и меня сводят с ума.... ах..."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            $ changeLuna(1, 1, 4, 1)                            # SNAPE
                            lun "Вы можете позаботиться о них?"
                            m "Да. Я скоро найду способ справиться с этими насильниками."
                            $ changeLuna(1, 2, 5, 1)
                            lun "...Спасибо [l_genie_name]."

                            if daytime:
                                m "Удачного дня, [luna_name]."
                                $ changeLuna(1, 2, 1, 1)
                                lun "Спасибо."
                            else:
                                m "Доброй ночи, [luna_name]."
                                lun "Доброй ночи [l_genie_name]..."

                    #Luna leaves.
                    hide screen luna
                    hide screen bld1
                    with d3
                    call play_sound("door") #Sound of a door opening.
                    hide screen luna_chibi
                    stop music fadeout 1.0
                    pause.5
                    call blkfade

                    call play_music("playful_tension") # SEX THEME.
                    ">Гермиона ничего не говорит. Ее лицо все красное из-за смущения, вины и волнения."

                "\"Я сейчас занят, [luna_name].\"":
                    call her_head("(Спасибо, [genie_name].)","angry","base")
                    lun "Заняты? Как так?"
                    lun "Вы помогаете другим студентам бороться с мозгошмыгами?"
                    m "Да, это именно то, чем я занят."
                    lun "Ну... Тогда я приду к вам позже."

            call blkfade
            her "*Slurp!* *Slurp!* *Gulp!*"
            ">Гермиона продолжает сосать твой член довольно жестко."
            ">Ее техники не хватает, но она компенсирует это скоростью."
            hide screen bld1
            call hide_blktone
            call ctc

            call bld
            m "Да... Я люблю твой, шустрый ротик..."
            her "*Gobble!* *Gobble!* *Gobble!*"
            call u_pause_ani
            call her_head("[genie_name]?","soft","ahegao")
            m "Хм?"
            call her_head("Вы собираетесь кончить мне на лицо?","soft","ahegao")
            call her_head("Или вы планируете кончить мне в ротик?")

            menu:
                "\"Я планирую кончить на лицо!\"":
                    call her_head("Понятно...","soft","ahegao")
                    m "Зачем ты спросила?"
                    call her_head("Ох... Я недавно прочитала в книге, что сперма содержит много антиоксидантов...","grin","dead")
                    call her_head("Это полезно для кожи лица...")
                    m "Отлично."
                    m "Продолжай взбивать себе крем-маску."
                "\"Я планирую кончить в рот!\"":
                    call her_head("Понятно...","grin","dead")
                    m "Почему ты спросила?"
                    call her_head("Ну, я пытаюсь соблюдать за потреблением калорий...","soft","ahegao")
                    call her_head("Мне просто интересно, сколько калорий содержится в вашей сперме, [genie_name].")
                    call her_head("Скорее всего, я после этого не пойду в столовую...")
                    m "[hermione_name]."
                    call her_head("Да?","soft","ahegao")
                    m "Возьми в ротик мой член."
                "\"Я пока не планирую.\"":
                    call her_head("Понятно...","soft","ahegao")
                    m "Ты не любишь сюрпризы?"
                    call her_head("На самом деле, нет...","soft","ahegao")
                    call her_head("Я предпочитаю заранее планировать...")
                    m "Ну, некоторые вещи в жизни просто непредсказуемые."
                    m "Существует только один способ узнать наверняка."

                "\"А что тебе больше нравится?\"":
                    call her_head("Если вам все равно, [genie_name]...","soft","ahegao")
                    if generating_points == 1:
                        call her_head("Я хочу, чтобы вы кончили мне на лицо, [genie_name].","grin","dead")
                        call her_head("Я читала, что это хорошо для кожи.")
                    else:
                        call her_head("Я хочу, чтобы вы кончили мне в рот.","grin","dead")
                        call her_head("Вы обычно, много кончаете, по этому я после могу не идти в столовую...")
                        call her_head("И сделать домашнюю работу.")
                    m "Ну, посмотрим."
                    m "Продолжай сосать."

        call u_play_ani
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Мм..."
        m "У тебя получается лучше [hermione_name]."
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Хорошо, скажи что-нибудь грязное..."
        her "*Slurp--?"
        call u_pause_ani

        if whoring < 21:
            call her_head("Эм...","angry","down_raised")
            call her_head("Я ем тараканов?","angry","base")
            m "Чего?"
            call her_head("О-они довольно грязные, [genie_name]...","angry","base")
            m "Нет, [hermione_name], я имею в виду, что-то непристойное!"
            m "И не смей говорить \"грязное\"!"
            m "Я имею в виду сексуальную грязь или грязную сексуальность!"
            call her_head("Ох... Эм...","angry","down_raised")
            m "Ах, неважно, момент ушел..."
            call her_head("Эм... Простите, [genie_name].","angry","base")
            m "Да, ничего. Просто увеличь скорость."
            call her_head("Конечно, [genie_name].","upset","closed")

        else:
            call her_head("Я шлюха, [genie_name].","base","suspicious")
            call her_head("Шлюха, помешанная на вашей сперме.","base","glance")
            m "Продолжай, [hermione_name]."
            call her_head("Все, что я знаю [genie_name].","base","down")
            call her_head("Это как сосать ваш член...")
            m "Хорошо, тогда тебе лучше вернуться к этому занятию [hermione_name]"
            call her_head("Спасибо, [genie_name].","grin","dead")
            m "Приятно познакомится, конченная шлюха."
            call her_head("...","base","ahegao_raised")

        call u_play_ani
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Да, мне это нравится... Хорошо..."
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Знаешь что? Я думаю, что скоро кончу."
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Да, определенно."
        her "*Slurp!* *Gobble!* *Gobble!*"
        m "Хорошо, [hermione_name], еще чуть-чуть."
        g4 "Покажи мне, как ты еще умеешь."
        her "!!! *Gobble-goble-slurp-goble!* !!!"
        g4 "Да, мне нравится!"
        her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
        g4 "{size=+5}Да! Да! Да! Да!{/size}"
        g4 "Ghr!!!"

        menu:
            g4 "!!!"
            "-Кончить в рот-":
                g4 "Кончаю, [hermione_name]! Будь готова быстро глотать!"
                her "!!!"
                call ctc
                call blkfade

                call set_u_ani("cum_in_mouth_ani")
                call u_play_ani
                call cum_block
                g4 "{size=+7}АХ!{/size}"
                g4 "Глотай мою сперму, шлюха!"
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Да!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen bld1
                call hide_blkfade
                stop music fadeout 1.0
                call ctc

                call bld
                m "Я думаю, что я закончил."
                m "Ты можешь идти..."
                call u_pause_ani

                call her_main("...........................","full_cum","dead",xpos="mid",ypos="base")
                call her_main("................")
                call her_main("........")
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_main("*GULP!*","cum","worriedCl")
                call her_main("Gua-ha...","open_wide_tongue","base")
                m "Ты в порядке?"
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("Да, [genie_name]...","grin","dead")
                m "Пропустишь следующий прием пищи?"
                call her_main("Я так думаю...","grin","dead")
                call her_main("Вы всегда так много кончаете, [genie_name]...")
                m "Хех... И кто же в этом виноват?"
                call her_main(".............","grin","dead") #Smile.
                call her_main("Могу ли я получить очки?")

                if whoring >= 21:
                    if daytime:
                        m "Что, даже после того, как я накормил тебя обедом?"
                    else:
                        m "Что, даже после того, как я накормил тебя ужином"
                    call her_main(".............","annoyed","suspicious") #Smile.
                    call her_main("Ладно, я полагаю, это стоило еды")

                call ctc
                call blkfade

            "-Кончить на лицо-":
                call blkfade

                call u_pause_ani
                g4 "Готовь свое лицо, [hermione_name]?"
                call her_head("Да [genie_name]!","grin","dead")
                g4 "Кончаю!"
                hide screen bld1
                call set_u_ani("cum_on_face_ani")
                call u_play_ani
                call hide_blkfade
                call cum_block

                call bld
                g4 "{size=+7}Шлюха!{/size}"
                call her_head("?!!","shock","wide")
                hide screen bld1
                with d3
                call ctc

                call bld
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_07.png"
                call her_head("[genie_name]...","shock","wide")
                g4 "Все на твоем ебанном лице!"
                call her_head("Ах!","grin","dead")
                call set_u_ani("cum_on_face_blink_ani")

                m "Я все."
                call her_head("....................................","grin","dead")
                m "Я сказал, что я уже все, [hermione_name]."
                call her_head("Да, я слышала вас [genie_name]...","grin","dead")
                m "Так... Разве ты не собираешься сходить умыться?"
                call her_head("В настоящее время...","grin","dead")
                call her_head("Я даю антиоксидантам впитаться в свою кожу...")
                m "Хм... Я думаю, что мне это нравится..."
                m "Не торопись, [hermione_name]..."

                call blkfade
                stop music fadeout 1.0
                ">Некоторое время спустя."
                call u_pause_ani
                $ uni_sperm = True
                $ aftersperm = True
                call her_chibi("stand","desk","base")
                show screen genie
                hide screen bld1
                hide screen blktone
                call hide_blkfade
                pause.5

                call her_main("Я так понимаю, вам понравилось, [genie_name]?","angry","wink",xpos="mid",ypos="base")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                m "Да, [hermione_name]."
                call her_main("Хорошо, так, могу я получить очки?","grin","dead")

                if whoring >= 21:
                    m "Что, даже после того, как я сделал тебе маску?"
                    m "Женщины тратят много денег на уход за лицом."
                    call her_main(".............","annoyed","suspicious") #Smile.
                    call her_main("Хорошо, завтра моя кожа будет выглядеть лучше.")

                call blkfade

    #Fourth Event
    elif hg_pf_SuckIt_OBJ.points >= 2 and whoring >= 21:
        call play_music("playful_tension") # SEX THEME.
        m "Соси мой член, [hermione_name]."
        call her_main("Конечно [genie_name]...","base","ahegao_raised",xpos="mid",ypos="base")

        call her_walk_desk_blkfade

        call play_music("playful_tension") #HERMIONE
        hide screen genie
        call her_chibi("hide")
        show screen chair_left
        call u_play_ani
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        show screen bld1
        call her_head("*Slurp!* *Slurp!* *Gulp!*","","",xpos="base",ypos="base")
        m "Да, хорошая девочка..."
        her "*Slurp!* *Gobble!* *Slurp!*"
        m "Полижи мою палочку..."
        her "*lick!* *Slurp!* *lick!*"
        call nar(">Гермиона продолжает сосать твой член, так как будто ее жизнь зависит от этого.","start")
        call nar(">Ее техника почти совершенна, и она невероятно увлечена процессом.","end")
        m "Да... Я люблю твой шустрый, маленький рот, шлюха..."
        her "*Gobble!* *Gobble!* *Gobble!*"
        call u_pause_ani
        call her_head("[genie_name]?","base","down")
        m "Хм?"
        call her_head("Как бы вы хотели, чтобы я порадовала вас?","soft","ahegao")

        menu:
            "\"Представь, что я твой отец..\"":
                call her_head("Мой отец?","angry","wink")
                m "Ничего плохого?"
                call her_head("Я думаю, нет...","base","down")
                call her_head("Я имею в виду, что буду притворяться...","grin","dead")
                m "Хорошо. Возьми мой член обратно в рот."
                call u_play_ani
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "На этом все, принцесса. Соси папину пипиську."
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Скажи мне, как сильно ты этого хочешь."
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani
                call her_head("Очень сильно, папа...","soft","ahegao")
                call u_play_ani
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani
                call her_head("Это все, о чем я думаю, когда мы вместе...","base","ahegao_raised")
                call u_play_ani
                her "*Gobble!* *Gulp!* *Gobble!*"
                call u_pause_ani
                call her_head("Когда мы сидим вместе на диване и смотрим телевизор...","base","ahegao_raised")
                call her_head("Я просто представляю, что я сосу твой член...","base","ahegao_raised")
                call u_play_ani
                her "*lick!* *Slurp!* *Slurp!*"
                call u_pause_ani
                call her_head("Я даже жалею, что мама тебя не бросила...","annoyed","down")
                call u_play_ani
                her "*Gobble!* *Slurp!* *lick!*"
                m "Почему?"
                call u_pause_ani
                call her_head("Так я стану единственной, кто получит твой член...","soft","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Ты будешь приходить домой каждый день...","soft","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Бросать меня на кровать...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("И использовать меня...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Когда ты захочешь...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Так долго, как ты захочешь...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Ты даже не будешь спрашивать...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Просто возьмешь меня...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Даже если я говорю нет...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                m "Да, так принцесса, я скоро кончу..."
                call u_pause_ani
                call her_head("Куда хочешь кончить, пап?","soft","ahegao")
                call her_head("На лицо?","soft","ahegao")
                call her_head("Или заставишь все проглотить?","grin","dead")
                call her_head("{size=-4}Даже если я не хочу...{/size}","grin","dead")
                m "Давай это выясним?"
                call her_head("Да, папа...","soft","ahegao")
                call u_play_ani
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Да, мне нравится... Хорошая девочка..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Сделай это для папочки."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Давай, принцесса."
                her "*Slurp!* *Gobble!* *Gobble!*"
                m "Хорошо [hermione_name], я сейчас кончу."
                g4 "Сделай папочку, счастливым!"
                her "!!! *Gobble-goble-slurp-goble!* !!!"
                g4 "Да, мне нравится!"
                her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
                g4 "{size=+5}Да! Да! Да! Да!{/size}"
                g4 "Ghr!!!"

                menu:
                    g4 "!!!"
                    "-Кончить в рот-":
                        call hide_blkfade
                        g4 "Кончаю, [hermione_name]!"
                        her "!!!"
                        call ctc
                        call blkfade

                        call set_u_ani("cum_in_mouth_ani")
                        call u_play_ani
                        call cum_block
                        g4 "{size=+7}АХ!{/size}"
                        g4 "Глотай мою сперму, шлюха!"
                        #Cumming.
                        her "*Gulp!-Gulp!-Gulp!*"
                        with hpunch
                        g4 "Да! Получай в свой грязный рот!"
                        her "*Gulp-gulp-gulp-gulp-gulp!*"
                        hide screen bld1
                        call hide_blkfade

                        stop music fadeout 1.0
                        call ctc
                        show screen bld1
                        with d3
                        m "Я закончил."
                        m "Ты можешь идти..."
                        call u_pause_ani
                        call her_head("...........................","full_cum","dead")
                        call her_head("................")
                        call her_head("........")
                        $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                        call her_head("*GULP!*","cum","worriedCl")
                        call her_head("Gua-ha...","open_wide_tongue","base")
                        m "Как тебе?"
                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                        call her_head("Очень вкусно...","grin","dead")
                        m "Серьезно?"
                        call her_head("Да, папа...","grin","dead")
                        call her_head("У тебя всегда вкусно....")
                        m "Хех... Это так?"
                        call her_head(".............","grin","dead") #Smile.
                        ">Она высовывает твой член изо рта и целует его."
                        call her_head("Спасибо, папочка.","base","baseL") #Smile.
                        call ctc
                        call blkfade

                    "-Кончить на лицо-":
                        call hide_blkfade
                        call u_pause_ani
                        g4 "Ты готова получить сперму, маленькая принцесса?"
                        call her_head("Да, папа!","grin","dead")
                        g4 "Кончаю!"
                        call cum_block
                        g4 "{size=+7}Шлюха!{/size}"
                        call her_head("?!!","shock","dead")
                        call set_u_ani("cum_on_face_ani")
                        call u_play_ani
                        hide screen bld1
                        with d3
                        call ctc

                        call bld
                        $ uni_sperm = True
                        $ u_sperm = "characters/hermione/face/auto_07.png"
                        call her_head("Папа...","shock","wide")
                        g4 "Готово, принцесса!"
                        call her_head("Аах!","grin","dead")
                        call set_u_ani("cum_on_face_blink_ani")
                        m "Я кончил."
                        call her_head("....................................","grin","dead")
                        m "Я сказал, что кончил, [hermione_name]."
                        call her_head("Да, я услышала тебя, папочка...","grin","dead")
                        m "Так... Ты не собираешься умыться?"
                        call her_head("Через минуту...","grin","dead")
                        call her_head("Я просто наслаждаюсь моментом...")
                        m "Хм..."
                        m "Не торопись, [hermione_name]..."
                        call blkfade

                        stop music fadeout 1.0
                        ">Некоторое время спустя."
                        call u_pause_ani
                        $ uni_sperm = False
                        $ aftersperm = True
                        call her_main("Я так понимаю, вам понравилось, сэр?","angry","wink")
                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                        m "Да, принцесса."
                        $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

            "\"Взбивай мои сливки.\"": ###IN PROGRESS
                call her_head("Повзбивать сливки?","angry","wink")
                m "Соси мой член"
                call her_head("Ну...","base","down")
                call her_head("Хорошо...","soft","ahegao")
                m "Отлично. Ты можешь начать, положив его в рот."
                call u_play_ani
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Вот так."
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Скажи мне, как сильно ты любишь мой член."
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani
                call her_head("Очень сильно [genie_name]...","soft","ahegao")
                call u_play_ani
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani
                call her_head("Все, о чем я думаю, когда нахожусь в классе...","base","ahegao_raised")
                call u_play_ani
                her "*Gobble!* *Gulp!* *Gobble!*"

                if lock_public_favors == True:
                    call u_pause_ani
                    call her_head("Это как сосу, ваш прекрасный член.","base","ahegao_raised")
                    call her_head("Никто не услышит...","base","ahegao_raised")
                    call u_play_ani
                    her "*lick!* *Slurp!* *Slurp!*"
                    call u_pause_ani
                    call her_head("Ваш {p}прекрасный, {p}великолепный {p}{size=-4}член{/size}","grin","dead")
                    call u_play_ani
                    her "*Gobble!* *Slurp!* *lick!*"

                else:
                    call u_pause_ani
                    call her_head("Даже когда вы заставляете меня сосать член другого парня...","base","ahegao_raised")
                    call her_head("Я думаю, что это ваш...","base","ahegao_raised")
                    call u_play_ani
                    her "*lick!* *Slurp!* *Slurp!*"
                    call u_pause_ani
                    call her_head("Представьте, как ваша сперма заполняет мое горло...","soft","ahegao")
                    call u_play_ani
                    her "*Gobble!* *Slurp!* *lick!*"
                    call u_pause_ani
                    call her_head("Представьте, как струя вашей горячей спермы выстреливает и летит мне на лицо...","grin","dead")
                    call u_play_ani
                    her "*Gobble!* *Slurp!* *lick!*"

                m "Это правда?"
                call u_pause_ani
                call her_head("Да [genie_name]...","soft","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Иногда...","soft","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("После того, как вы заставляете меня сосать ваш прекрасный член...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Я не чищу зубы...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Только так я могу заснуть...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("С отличным послевкусием во рту...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("А когда я чищу зубы...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Я думаю только о вашем прекрасном члене...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani
                call her_head("Я даже начала стонать, чистя их...","grin","dead")
                call u_play_ani
                her "*Gobble!* *lick!* *Gobble!*"
                m "Вот шлюха, я скоро кончу..."
                call u_pause_ani
                call her_head("Куда вы хотите кончить [genie_name]?","soft","ahegao")
                call her_head("Я знаю, что с моей стороны не очень хорошо спрашивать...","angry","down_raised")
                call her_head("Но можете кончить мне в рот?","angry","wink")
                call her_head("{size=-4}Пожалуйста...{/size} Обещаю, я не пропущу ни капельки..","soft","ahegao")
                m "Думаю, это можно устроить. "
                call her_head("Спасибо [genie_name]!","smile","happyCl",cheeks="blush",emote="06")
                call u_play_ani
                call nar(">Гермиона начинает еще быстрее сосать.")
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Да, мне нравится... ты хорошая маленькая шлюха..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Глубже."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Давай, членососка."
                her "*Slurp!* *Gobble!* *Gobble!*"
                m "Хорошо, [hermione_name], я сейчас кончу."
                g4 "Глубже!"
                her "!!! *Gobble-goble-slurp-goble!* !!!"
                g4 "Да, мне нравится!"
                her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
                g4 "{size=+5}Да! Да! Да! Да!{/size}"
                g4 "Ghr!!!"
                hide screen blkfade
                with d3
                g4 "Кончаю, [hermione_name]! Вот твоя награда!"
                her "!!!"

                call ctc
                call blkfade

                call set_u_ani("cum_in_mouth_ani")
                call u_play_ani
                call cum_block
                g4 "{size=+7}АХ!{/size}"
                g4 "Глотай мою сперму, шлюха!"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Да!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen bld1
                call hide_blkfade
                stop music fadeout 1.0
                call ctc

                call bld
                m "Я закончил."
                m "Ты можешь идти..."
                call u_pause_ani
                call her_main("...........................","full_cum","dead",tears="mascara",xpos="mid",ypos="base",trans="fade")
                call her_main("................","full_cum","dead",tears="mascara")
                call her_main("........","full_cum","dead",tears="mascara")
                m "Как тебе?"
                call her_main("...")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                m "Ты собираешься глотать?"
                call her_main("*Качает головой из стороны в сторону*","full_cum","dead",tears="mascara")

                if daytime:
                    m "Итак, ты собираешься пойти в класс с полным ртом спермы?"
                else:
                    m "Так ты собираешься лечь спать с полным ртом спермы?"

                call her_main("*Она восторженно кивает головой вверх-вниз*","full_cum","ahegao",cheeks="blush",tears="mascara") #Smile.
                m "Хорошая девочка."
                call ctc

                call blkfade
                $ mouth_full_of_cum = True

    $ gryffindor += current_payout #35

    call blkfade
    hide screen hermione_main
    call u_end_ani
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide")
    show screen genie
    call her_chibi("stand","desk","base")
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    pause.5

    call bld
    if whoring < 21:
        m "Да, [hermione_name]. 55 очков \"Гриффиндору\"."
        $ gryffindor +=55

    if mouth_full_of_cum:
        call her_main("...","full_cum","ahegao",cheeks="blush",tears="mascara",xpos="right",ypos="base")
    else:
        call her_main("Спасибо, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if whoring < 18:
        $ whoring +=1

    if hg_pf_SuckIt_OBJ.points == 0:
        $ new_request_22_heart = 1
        $ hg_pf_SuckIt_OBJ.hearts_level = 1 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points == 1:
        $ new_request_22_heart = 2
        $ hg_pf_SuckIt_OBJ.hearts_level = 2 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points >= 2:
        $ new_request_22_heart = 3
        $ hg_pf_SuckIt_OBJ.hearts_level = 3 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points >= 2 and whoring > 21:
        $ hg_pf_SuckIt_OBJ.hearts_level = 4 #Event hearts level (0-4)

    $ hg_pf_SuckIt_OBJ.points += 1

    $ custom_outfit_old = temp_outfit

    hide screen hermione_main
    hide screen bld1
    with d3
    pause.5

    jump end_hg_pf #Hides screens. Hermione walks out. Resets Hermione.
