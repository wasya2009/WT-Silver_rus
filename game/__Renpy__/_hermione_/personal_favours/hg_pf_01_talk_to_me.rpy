

### HERMIONE PERSONAL FAVOUR 1 ###

### TALK TO ME ###

label hg_pf_TalkToMe:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(Все что мне нужно - это невинный разговор...){/size}"
    if hg_pf_TalkToMe_OBJ.points < 1:

        menu:
            "\"(Да, сделаем это.)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    if hg_maid_OBJ.purchased or hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased or hg_msMarvel_OBJ.purchased or hg_heartDancer_OBJ.purchased or hg_powerGirl_OBJ.purchased or hg_harleyQuinn_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Сделаем это!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, я бы хотел попросить тебя одеться как..."
                call her_main("Как?","open","worriedL")
                menu:
                    "-Горничная-" if hg_maid_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_maid_OBJ)
                        pass
                    "-Болельщица-" if hg_gryffCheer_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_gryffCheer_OBJ)
                        pass
                    "-Болельщица Слизерина-" if hg_slythCheer_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_slythCheer_OBJ)
                        pass
                    "-Мисс Марвел-" if hg_msMarvel_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_msMarvel_OBJ)
                        pass
                    "-Танцовщица сердец-" if hg_heartDancer_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_heartDancer_OBJ)
                        pass
                    "-Power Girl-" if hg_powerGirl_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_powerGirl_OBJ)
                        pass
                    "-Harley Quinn-" if hg_harleyQuinn_OBJ.purchased:
                        her "Хорошо, скоро вернусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_harleyQuinn_OBJ)
                        pass
            "\"(В другой раз.)\"":
                pass

    call play_music("chipper_doodle")

    m "Хорошо, тогда..."
    m "Просто расскажи что-нибудь о себе."
    call her_main("","open","suspicious")

                       
                                         
                                          
    
    if hg_pf_TalkToMe_OBJ.points == 0: #First time this event taking place.
        her "Ох... Ладно..."
        her "Я просто стою здесь и говорю... Верно?"
    else:
        her "Стоять здесь и рассказывать, я помню..."

    call her_main("","base","base",xpos="mid",ypos="base",trans="fade")
    call ctc

    m "Все хорошо?"

    #First time event
    if hg_pf_TalkToMe_OBJ.points == 0 and whoring <=5:

        $ new_request_01_heart = 1 #Event hearts level (0-3)#Event hearts level (0-3)
        $ hg_pf_TalkToMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        call her_main("Э... очень хорошо...","open","worried")
        call nar(">Гермиона в замешательстве...")
        call her_main("...................","annoyed","angryL")

    #Event 1 and 2
    if whoring >= 0 and  whoring <= 5:
        if whoring >= 3 and whoring <= 5:

            $ new_request_01_heart = 2 #Event hearts level (0-3)
            $ hg_pf_TalkToMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        call her_main("Моя жизнь не очень примечательна в последнее время...","annoyed","angryL")
        her "Кроме, конечно того дня, когда я провалила тест..."
        her "Никак не могу понять, как это могло случиться..."

        menu:
            "-Передернуть-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.
                hide screen hermione_main
                call nar(">Ты тянешься руками к члену...")

                hide screen genie
                show screen genie_jerking_off
                hide screen bld1
                with d3

                call ctc

                call her_main("[genie_name], что вы делаете?","open","base",xpos="mid")
                m "Что? О, не переживай. Я просто чешу ногу."
                m "Так о чем ты?"
                call her_main("Верно... Ну, я провалилась на том тесте...","open","base")
            "-Поддержать разговор-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Должно быть для тебя это большая трагедия..."
                her "Точно! Я рада, что вы понимаете меня, [genie_name]."
                #pass

        her "Знаете, мне больше не хочется говорить об этом..."
        m "Понимаю, что еще произошло в последнее время?"
        her "Эмм... Ну, я делаю неплохие успехи в травологии..."
        her "Я имею в виду, я всегда получаю высший балл, но и я ведь всегда хорошо училась, верно?..."
        her "И иногда мне кажется, что я знаю больше, чем сама профессор Спраут..."

        if d_flag_01:
            m "{size=-4}(Да... ах...){/size}"
        else:
            m "(Профессор Спраут(Стебль)... Хе-хе, что за глупое имя...)"

        call her_main("Вы что-то сказали, [genie_name]?","normal","frown")
        m "Не обращай внимания, продолжай..."
        call her_main("Ну, многие студенты высмеивают профессора Квирелла за его спиной...","open","base")

        her "Я, конечно, этого не одобряю."
        if d_flag_01:
            m "{size=-4}(Ну же! Скажи что-нибудь грязное...){/size}"
        else:
            m ".................."

        her "Ах да, мое \"Движение за Права Мужчин\" набирает популярность..."
        her "Я очень довольна нашими успехами..."
        call her_main("Думаю со временем мы сможем внести реальные изменения...","open","closed")
        call her_main("Осознание того, что делаешь что-то хорошее, {w}так будоражит!","base","base")
        her "Вы не согласны, профессор?"

        if d_flag_01:
            m "{size=-4}(Чтоб тебя, совсем настроение испортила...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
        else:
            m "Zzzz........"

        call her_main("[genie_name]?","angry","angry")
        m "Да-да, я весь во внимании..."
        m "Похоже ты уверена в своих силах..."
        m "Я имею в виду, все это очень будоражит..."
        call her_main("..........................","normal","frown")

    #Event 3
    elif whoring >= 6:

        $ new_request_01_heart = 3 #Event hearts level (0-3)
        $ hg_pf_TalkToMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        call her_main("Ничего интересного не случалось в последнее время...","annoyed","angryL")
        her "Хмм..."
        her "Сейчас очень жесткая конкуренция между \"Слизерином\" и \"Гриффиндором\"."
        her "Если быть честной, [genie_name], у нас не лучшие дни..."
        her "\"Гриффиндор\" лидировал бы, если бы не те \"Слизеринские\" шлюхи..."
        her "Я слышала, чем они занимаются, чтобы получить несколько дополнительных очков..."
        call her_main("Как же это подло!","open","angryCl")
        m "И что делаешь ты, [hermione_name]?"
        call her_main("Точно!","normal","base")
        m "Чего?"
        call her_main("Я должна работать еще лучше, чтобы возместить ущерб, нанесенный нам этими мерзкими девками...","open","angryCl")
        call her_main("Спасибо, что помогаете мне, [genie_name].","normal","base")

        menu:
            "-Передернуть-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.
                hide screen hermione_main
                call nar(">Ты нащупываешь руками свой член...")
                hide screen genie
                show screen genie_jerking_off
                with d3

                call ctc

                call her_main("[genie_name], что вы делаете?","open","base",xpos="mid")
                her "Ах, ничего.....?"
                call her_main("Вы...?","annoyed","worriedL")
                m "Что? О, не обращай внимания. Продолжай"
                call her_main("Хмм...","normal","frown")
                m "{size=-4}(Она подозревает? Ох, вряд-ли...){/size}"
            "-Поддержать разговор-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Не упоминать об этом."

        call her_main("В общем, как я говорила...","open","closed",xpos="mid")
        her "Я слышала, что одна девочка продала свои неприличные фотографии, одному из преподавателей, за десять очков факультету..."

        if d_flag_01:
            m "{size=-4}(Какая шлюха... ох... да...){/size}"
        else:
            m "Десять очков, всего?"

        her "Да..."

        if d_flag_01:
            call her_main("Про двух других девочек...","annoyed","worriedL")
            her "Ходят слухи, что они спят с профессором Снейпом..."
            m "{size=-4}(ДА... Грязные \"слизеринские\" шлюхи!){/size}"
            call her_main("Кроме того, есть слух, что одна девочка передернула профессору прямо на занятии...","base","base")
            m "{size=-4}(Да... Это интересно, продолжай!){/size}"
            call her_main("А еще одна девочка отсосала преподователю!","annoyed","worriedL")
            m "{size=-4}(Да! ДА!){/size}"
            call her_main("а еще одна позволила учителю кончить ей прямо в рот...","smile","baseL")
            her "А потом проглатывала и говорила, что ей все очень понравилось!"
            m "{size=-4}(Погоди-ка... Она это все специально выдумывает?){/size}"
            call her_main("Я тоже плохая девочка, вы же знаете...","smile","glance")
            g4 "Чего?!"
            call her_main("Я тоже хочу сосать член...","open_tongue","glance")
            her "Хочу, чтобы на мое лицо кончали, как в тех видео, что я смотрю!"
            g4 "{size=-4}(Ты маленькая шлюха! Ты сделала это!) *Ох!*{/size}"

            hide screen hermione_main
            with d3

            call cum_block

            g4 "Ох! ДА!"
            hide screen bld1
            with d1
            show screen genie_jerking_sperm
            with d3
            call ctc

            if whoring <= 10:
                $ mad = +7
                call her_main("Я знала! Вы трогали себя, [genie_name]!","angry","angry")
                #show screen genie_jerking_sperm_02
                #with d3
                g4 "Что? Но... Черт, это было и правда неплохо ..."
                show screen genie
                with d3
                call her_main("Это отвратительно! как вы могли?!","scream","worriedCl")
                her "[genie_name], Вы - директор! вы должны подавать хороший пример!"
                m "Эй, юная мисс, вы пришли сюда осуждать меня или хотите получить свои очки?"
                call her_main("...мои очки, пожалуйста, думаю после подобного я их заслужила.","angry","worriedCl",emote="05")
                m "Да, это правда."
                call her_main("Фу... чувствую себя грязной после этого...","angry","angry")
                hide screen genie_jerking_sperm_02
                with d3
            else:
                call her_main("Я знала! Вы трогали себя, [genie_name]!","smile","glance")
                #show screen genie_jerking_sperm_02
                #with d3
                g4 "Что? Но... Черт, это было и правда неплохо..."
                show screen genie
                with d3
                call her_main("Как вы могли, [genie_name]? Перед невинной ученицей!","scream","angryCl")
                m "Эй, юная мисс, то что вы говорили никак нельзя назвать невинным."
                call her_main("Не понимаю, о чем вы говорите...","smile","baseL")
                m "Ну конечно, тебе нужны твои очки или нет?"
                call her_main("{size=-4}Как же много он кончил{image=textheart}{/size}","base","base")
                hide screen genie_jerking_sperm_02
                with d3

        else:
            her "Мы должны положить этому конец, [genie_name]!"
            m "Да, конечно..."
            her "Так вы согласны со мной?"
            her "Я думаю, мы должны создать систему наказаний для девочек, которые продают услуги..."
            m "(Все что я слышал это \"наказать девочек\"...)"
            her "А так же это поможет мальчикам в нашей школе не чувствовать себя обделенными!"
            m "Мальчики?"
            m "Верно... Никому ведь не нужны сексуальные услуги от мальчиков... Жалкие ублюдки."
            her "я так рада что вы прониклись этой проблемой, [genie_name]."
            m "Да да, конечно..."

    stop music fadeout 2.0

    if whoring >= 11:
        m "Пять очков \"Гриффиндору\", [hermione_name]. Хорошая работа."
        her "О, не волнуйтесь о очках, [genie_name]. мне понравилась эта беседа."
        m "Серьезно? Так что насчет победы \"Гриффиндора\"?"
        call her_main("Это всего пять очков...","soft","baseL")
        m "Ну, если ты так говоришь."
        call her_main("Мы закончили на сегодня?","base","base")
        m "Да, можешь идти."
    else:
        $ gryffindor +=5
        m "Пять очков \"Гриффиндору\", [hermione_name]. Хорошая работа."
        show screen hermione_main
        hide screen hermione_stand_f #Hermione stands still.
        with d3
        her "Мы закончили на сегодня?"
        if whoring >= 0 and whoring <= 2: #LEVEL 01
            her "*вздох облегчения*"
        m "Да, можешь идти."

    if hg_pf_TalkToMe_OBJ.points == 0:
        call her_main("Еще пять очков... Ребята будут счастливы.","base","base")
        her "Спасибо, [genie_name]."

    if whoring < 3: #Adds points till 3.
        $ whoring +=1

    $ hg_pf_TalkToMe_OBJ.points += 1

    jump end_hg_pf












