

### HERMIONE PERSONAL FAVOUR 2 ###

### NICE PANTIES ###

label hg_pf_NicePanties:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(Я попрошу, чтобы она показала мне свои трусики. Легко и просто.){/size}"
    if hg_pf_NicePanties_OBJ.points < 1:

        menu:
            "\"(Да, сделаем это!)\"":
                pass
            "\"(В другой раз.)\"":
                jump silver_requests

    $ menu_x = 0.2 #Menu is moved to the left side.

    call her_main("Итак, что мне сделать, [genie_name]?")
    m "Ничего особенного, правда..."
    m "Я просто хочу чтобы ты показала мне свои трусики."

    #First Time Event.
    if hg_pf_NicePanties_OBJ.points == 0 and whoring <= 5:
        call her_main("Мои... трусики...?","open","base")
        call her_main("[genie_name]!","angry","angry")
        m "Знаю, это звучит немного странно..."
        call her_main(" {size=+7}Немного?!{/size}","shock","wide")
        her "Это совершенно неуместно!"
        m "Мы должны пройти эту фазу, чтобы перейти к более интересным вещам, верно?"
        call her_main("Эээ, \"интересным\"? [genie_name], я не понимаю...","open","base")
        m "Что ты не понимаешь, [hermione_name]?"
        m "Тебе нужны очки или нет?"
        call her_main("Ну да...","open","base")
        m "Ну так поднимай свою юбку..."
        call her_main(".............","angry","angry")
    else:
        if hg_pf_NicePanties_OBJ.points >= 1: #Not the first time
            call her_main("Ох... опять?","annoyed","worriedL")
            m "Не тяни время..."
        call her_main("..................","annoyed","worriedL")


    ### Setup ###

    hide screen bld1
    hide screen hermione_main
    with d3

    #First and Second Event
    if whoring < 9:
        $ hermione_wear_panties = True
        call h_action("lift_skirt")

    #Third Event
    else:
        if hg_pf_NicePanties_OBJ.hearts_level == 2: #Before third event happens.
            $ h_request_wear_panties = False
            $ hermione_wear_panties = False

        elif hg_pf_NicePanties_OBJ.hearts_level == 3: #Third event.
            if h_request_wear_panties:
                $ hermione_wear_panties = True
            else:
                $ hermione_wear_panties = False

    call her_chibi("lift_skirt","mid","base")
    with d3
    call play_music("playful_tension")



    #Fist event.
    if whoring >= 0 and whoring <= 2:

        $ new_request_02_heart = 1 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 1 #Event hearts level (0-3)

        pause.8

        show screen blktone
        call her_main(".....................","angry","angry",trans="fade",xpos="mid",ypos="base")
        call ctc

        menu:
            "-Смотреть на ее лицо-":
                ">Ты смотришь в глаза Гермионе..."
                call ctc
                ">Тебе интересно, что сейчас творится у нее в голове."
                call her_main(".......................","angry","annoyed",emote="01")
                call ctc
            "-Уставиться на ее трусики-":
                ">Простое скромное женское белье..."
                call her_main(".......................","angry","annoyed",emote="01")
                call ctc

    #Second Event.
    elif whoring >= 3 and whoring < 9:

        $ new_request_02_heart = 2 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 2 #Event hearts level (0-3)

        pause.8

        show screen blktone
        call her_main("Здесь, [genie_name]...","base","base",trans="fade",xpos="mid",ypos="base")
        call ctc 

        menu:
            "\"Ты не выглядишь смущенной...\"":
                call her_main("Это неправда...","base","squint")
                call her_main("Но я готова заплатить эту цену за победу \"Гриффиндора\" в этом году.","base","baseL")
                her "Я знаю, что так все будут счастливы..."
                call ctc
            "\"Мне нравятся твои трусики...\"":
                call her_main("Спасибо, [genie_name]...","base","squint")
                call ctc
            "-Продолжать смотреть ей в глаза-":
                call her_main("..............................","soft","base")
                her "...........................?"
                call her_main("................................","grin","baseL")
                call her_main("[genie_name], пожалуйста... Вы смущаете меня.","grin","worriedCl",emote="05")
                call ctc

    #Third Event.
    elif whoring >= 9:

        $ new_request_02_heart = 3 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 3 #Event hearts level (0-3)

        call ctc

        call her_head("..........................","base","baseL",cheeks="blush",xpos="base",ypos="base")

        if not hermione_wear_panties:
            g4 "?!!"

        call h_action("lift_skirt")

        show screen blktone
        call her_main("","base","glance",trans="fade",xpos="mid",ypos="base")
        call ctc

        #Event A (no panties)
        if not hermione_wear_panties:
            g4 "Где твои трусики, [hermione_name]?"
            call her_main("Ну, в последнее время мне совсем не хочется их носить...","base","down",cheeks="blush")

            menu:
                "\"Ты маленькая шлюха!\"":
                    her "Хмм..."
                    call her_main("Полагаю вы должны...","base","glance")
                    her "Дать дополнительные очки за это?"

                    menu:
                        "\"Несомненно!\"":
                            m "Совершенно верно!"
                            $ gryffindor +=10
                            m "Десять дополнительных очков \"Гриффиндору\"!"
                            call her_main("Спасибо, [genie_name]!","base","worriedCl")
                            call ctc
                        "\"Конечно нет!\"":
                            $ mad +=5
                            call her_main("Но почему?!","scream","angryCl")
                            m "Шлюхам не платят"
                            m "Собственно потому они шлюхи"
                            call her_main("Хорошо, но вы ведь дадите мне мои пять очков?","annoyed","angry")
                            m "Так ты шлюха или проститутка?"
                            her "{size=-4}...шлюха {/size}"
                            m "Хорошая девочка"
                            call ctc

                "\"Отлично! Пять очков!\"":
                    pass

        else: #Event B
            call her_main("Они вам нравятся, [genie_name]?","base","glance")
            m "Именно так, [hermione_name]..."
            m "Они выглядят очень мило на тебе!"
            call her_main("Спасибо, [genie_name].","base","baseL",cheeks="blush")
            call ctc


        #Hermione asks to put them back on/take them off.
        if not hermione_wear_panties:
            call her_main("Я могу одеть их, [genie_name], если вы хотите этого.","open","baseL")

            menu:
                "\"Верно, надевай!\"":
                    call her_main("Ох, ладно, [genie_name].","base","glance")
                    hide screen hermione_main
                    with d3
                    ">Гермиона одевает свои трусики."

                    $ h_request_wear_panties = True
                    $ hermione_wear_panties = True

                    call update_her_uniform
                    call update_chibi_uniform
                    call her_chibi("lift_skirt")
                    call set_hermione_action("lift_skirt")

                    call her_main("","base","glance")
                    call ctc

                    call her_main("я надеюсь они вам нравятся...","soft","baseL")

                "\"Нет, не смей!\"":
                    call her_main("Конечно, [genie_name].","soft","ahegao")
                    call ctc

                    $ h_request_wear_panties = False

        else:
            call her_main("Я могла бы снять их, если хотите, [genie_name].","open","baseL")

            menu:
                "\"Да, снимай!\"":
                    call her_main("Ладно, [genie_name].","soft","ahegao")
                    m "И чтобы я их больше не видел!"
                    call her_main("Как скажете, [genie_name].","base","glance")
                    hide screen hermione_main
                    with d3
                    ">Гермиона снимает свои трусики."

                    $ h_request_wear_panties = False
                    $ hermione_wear_panties = False

                    call update_her_uniform
                    hide screen hermione_chibi_lift_skirt
                    call update_chibi_uniform

                    call her_chibi("lift_skirt")
                    call set_hermione_action("lift_skirt")

                    call her_main("","base","glance")
                    call ctc

                    call her_main("Надеюсь вам нравится, [genie_name]...","angry","wink")

                "\"Нет, даже не думай об этом!\"":
                    call her_main("Конечно, [genie_name].","base","glance")
                    call ctc

                    $ h_request_wear_panties = True


    stop music fadeout 4.0

    if whoring <= 8:
        $ gryffindor +=5
        m "Пять очков \"Гриффиндору\", [hermione_name]. Отличная работа."

    call reset_hermione_main

    call her_chibi("stand","mid","base")

    hide screen blktone
    call her_main("Это все?","open","base",trans="fade",xpos="base",ypos="base")

    if whoring >= 13:
        menu:
            "-Позволить уйти-":
                m "Да, теперь можешь уходить."

                if hg_pf_NicePanties_OBJ.points == 0: #First time.
                    call her_main("Еще пять очков...","soft","baseL")
                    her "Не могу дождаться чтобы обрадовать ребят!"
                    call her_main("Хотя я никогда не смогу рассказать, что здесь было на самом деле...","annoyed","angryL")

                if daytime:
                    her "Спасибо, мне уже пора на занятия..."
                else:
                    her "Уже довольно поздно, [genie_name]... Я пойду..."

                if whoring <= 2:
                    $ whoring +=1

                $ hg_pf_NicePanties_OBJ.points += 1

                jump end_hg_pf
            "-Спросить о других услугах-":
                m "Интересны ли тебе дополнительные очки?"
                her "Почему бы и нет. Чего вы хотите?"
                hide screen hermione_main
                with d3
                m "Хмм, я хочу..."

                if whoring <= 2:
                    $ whoring +=1

                if hg_pf_NicePanties_OBJ.points < 3:
                    $ hg_pf_NicePanties_OBJ.points += 1

                $ menu_x = 0.5 #Menu is moved to the middle.
                $ menu_y = 0.5 #Menu is moved to the middle.

                jump silver_requests_root

    else:
        m "На сегодня все, можешь идти."
        if hg_pf_NicePanties_OBJ.points == 0: #First time.
            call her_main("Еще пять очков...","soft","baseL")
            her "Не могу дождаться чтобы рассказать ребятам!"
            call her_main("Пусть я никогда и не расскажу им, что здесь было на самом деле...","annoyed","angryL")

        if daytime:
            her "Спасибо, мне уже пора на занятия..."
        else:
            her "Уже довольно поздно, [genie_name]... Я пойду..."

        if whoring < 3: #Adds points till 3.
            $ whoring +=1

        $ hg_pf_NicePanties_OBJ.points += 1

        jump end_hg_pf #Hides screens. Hermione walks out. Resets Hermione.
