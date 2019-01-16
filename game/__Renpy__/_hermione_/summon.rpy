

label summon_hermione:

    call load_hermione_clothing_saves

    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    call hermione_door_event

    call update_her_uniform

    call her_chibi("stand","mid","base")

    if mad >= 1:

        if mad >=1 and mad < 3:
            call her_main("","normal","base",xpos="base",ypos="base")
            ">Похоже, Гермиона все еще немного расстроена из-за тебя..."
        elif mad >=3 and mad < 10:
            call her_main("","normal","base",xpos="base",ypos="base")
            ">Гермиона тобой недовольна."
        elif mad >=10 and mad < 20:
            call her_main("","annoyed","frown",xpos="base",ypos="base")
            ">Гермиона очень расстроилась из-за тебя."
        elif mad >=20 and mad < 40:
            call her_main("","angry","angry",xpos="base",ypos="base")
            ">Гермиона злится на тебя."
        elif mad >=40 and mad < 50:
            call her_main("","angry","angry",xpos="base",ypos="base")
            ">Гермиона очень разозлилась на тебя."
        elif mad >=50 and mad < 60:
            call her_main("","angry","angry",xpos="base",ypos="base")
            ">Гермиона в ярости от тебя."
        elif mad >=60:
            call her_main("","angry","angry",xpos="base",ypos="base")
            ">Гермиона тебя ненавидит."

    else:
        if not hermione_door_event_happened:
            call her_main("Да, [genie_name]?","base","base",xpos="base",ypos="base")
        else:
            call her_main("...","base","base",xpos="base",ypos="base")

    label day_time_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        "-Спросить о новом ученике-" if hat_known and not luna_known:
            call luna_init
            $ luna_known = True
            jump hat_intro_2
        "-Говорить-":
            if not chitchated_with_her:
                jump hermione_talk_branches
                label hermione_talk_branches_return:
                if mad <= 7:
                    $ chitchated_with_her = True
                    call chit_chat
                    jump hermione_talk
                else:
                    her "Мне нечего вам сказать, сэр..."
                    jump day_time_requests
            else:
                jump hermione_talk
        "-Репетиторство-" if not daytime and v_tutoring < 14: #13 is last level.
            if mad >=1 and mad < 3:
                her "Извините, может быть, завтра..."
                jump day_time_requests
            elif mad >=3 and mad < 10:
                her "Я сегодня не в настроении..."
                jump day_time_requests
            elif mad >= 10 and mad < 20:
                her "Абсолютно нет, [genie_name]"
                her "Я {i}может{/i} рассмотрю предложение после ваших извинений"
                jump day_time_requests
                # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
            elif mad >=20:
                her "После того что вы сделали, [genie_name]?"
                her "Я так не думаю..."
                jump day_time_requests
            else:
                jump l_tutoring_check

        "-Купить сексуальные услуги-" if buying_favors_from_hermione_unlocked:
            if mad >=1 and mad < 3:
                her "Мне жаль, [genie_name], может быть, в другой раз..."
                jump day_time_requests
            elif mad >=  3 and mad < 10:
                her "Мне сегодня не хочется..."
                her "Может через пару дней..."
                jump day_time_requests
            elif mad >= 10 and mad < 20:
                her "Нет, спасибо..."
                jump day_time_requests
            elif mad >= 20 and mad < 30:
                her "После того, что вы сделали, [genie_name]?"
                her "Я так не думаю..."
                jump day_time_requests
            elif mad >= 30 and mad < 40:
                her "Вы же не серьезно?!"
                jump day_time_requests
            elif mad >= 40:
                her "Это какая-то извращенная шутка, сэр?!"
                her "После того, что вы сделали, я не хочу делать это снова!"
                jump day_time_requests
            else:
                jump silver_requests

        "-Гардероб-":
            $ active_girl = "hermione"

            call load_hermione_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ wardrobe_active = 1 #True
            call her_main("","","",xpos="wardrobe",ypos="base")
            call screen wardrobe

        #"-Ending \"Your whore\"-":
        #    $ public_whore_ending = False
        #    jump your_whore

        #"-Ending \"Public whore\"-":
        #    $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
        #    jump your_whore

        "-Отпустить ее-":
            if daytime:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "*Humph!*..."
                else:
                    her "О, хорошо. Я тогда пойду на занятия."
            else:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "Tch..."
                else:
                    her "О, хорошо. Тогда я отправлюсь спать."

            hide screen bld1
            hide screen blktone

            hide screen hermione_main
            hide screen hermione_blink #Hermione stands still.

            hide screen ctc
            with d3

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).

            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu



label hermione_talk:
    menu:
        "-Деятельность-":
            label working_menu:
            menu:
                "-Работа горничной-" if daytime and hg_maid_OBJ.purchased:
                    jump job_1

                "-Работа горничной-" if daytime and not hg_maid_OBJ.purchased:
                    m "(Мне нужна спецодежда для Гермионы, если я хочу, чтобы она этим занималась.)"
                    jump working_menu

                "{color=#858585}-Работа горничной-{/color}" if not daytime:
                    "Эта работа доступна только в течение дня."
                    jump working_menu

                "-Работа в качестве болельщика Гриффиндора-" if daytime and hg_gryffCheer_OBJ.purchased:
                     jump job_3

                "-Работа в качестве болельщика Гриффиндора-" if daytime and not hg_gryffCheer_OBJ.purchased:
                    m "(Мне нужна спецодежда для Гермионы, если я хочу, чтобы она этим занималась.)"
                    jump working_menu

                "{color=#858585}-Работа в качестве болельщика Гриффиндора-{/color}" if not daytime:
                    "Эта работа доступна только в течение дня."
                    jump working_menu

                "-Работа в качестве болельщика Слизерина-" if daytime and hg_slythCheer_OBJ.purchased:
                    jump job_4

                "-Работа в качестве болельщика Слизерина-" if daytime and not hg_slythCheer_OBJ.purchased:
                    m "(Мне нужна спецодежда для Гермионы, если я хочу, чтобы она этим занималась.)"
                    jump working_menu

                "{color=#858585}-Работа в качестве болельщика Слизерина-{/color}" if not daytime:
                    "Эта работа доступна только в течение дня."
                    jump working_menu

                "-Назад-":
                    jump hermione_talk

        "-Обращайся ко мне...-":
            menu:
                "-Сэр-":
                    $ genie_name = "Сэр"
                    jump genie_change
                "-Дамблдор-":
                    $ genie_name = "Дамблдор"
                    jump genie_change
                "-Профессор-":
                    $ genie_name = "Профессор"
                    jump genie_change
                "-Старик-":
                    $ genie_name = "Старик"
                    jump genie_change
                "-Джинн-":
                    if whoring >=5:
                        $ genie_name = "Джинн"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Мой Господин-":
                    if whoring >=7:
                        $ genie_name = "Мой Господин"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Любимый-":
                    if whoring >=10:
                        $ genie_name = "Любимый"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Лорд Волдеморт-":
                    if whoring >=15:
                        $ genie_name = "Лорд Волдеморт"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Папочка-":
                    if whoring >=20:
                        $ genie_name = "Папочка"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Хозяин-":
                    if whoring >=20:
                        $ genie_name = "Хозяин"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Ввести свой вариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ genie_name = "Сэр"
                        jump genie_change
                    if whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Назад-":
                    jump hermione_talk

        "-Отныне, я буду называть тебя-":
            menu:
                "-Мисс Грейнджер-":
                    $ hermione_name = "Мисс Грейнджер"
                    jump hermione_change
                "-Девушка-":
                    $ hermione_name = "Девушка"
                    jump hermione_change
                "-Хорошая девочка-":
                    if whoring >=5:
                        $ hermione_name = "Хорошая девочка"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Рабыня-":
                    if whoring >=10:
                        $ hermione_name = "Рабыня"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Принцесса-":
                    if whoring >=10:
                        $ hermione_name = "Принцесса"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Шлюха-":
                    if whoring >=15:
                        $ hermione_name = "Шлюха"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Маленькая девочка-":
                    if whoring >=15:
                        $ hermione_name = "Маленькая девочка"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Гриффиндорская шлюха-":
                    if whoring >=18:
                        $ hermione_name = "Гриффиндорская шлюха"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Грязнокровка-":
                    if whoring >=20:
                        $ hermione_name = "Грязнокровка"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Ввести свой вариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя)")
                    $ temp_name = temp_name.strip()
                    if hermione_name == "":
                        $ hermione_name = "Мисс Грейнджер"
                    if whoring >=20:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Назад-":
                    jump hermione_talk

        "-Назад-":
            jump day_time_requests


label genie_change:
    call her_main("Хорошо, отныне я буду называть вас [genie_name].","base","base")
    jump hermione_talk

label genie_change_fail:
    call her_main("Я не буду, вас так называть!","scream","angryCl")
    jump hermione_talk

label hermione_change:
    if whoring >= 20:
        call her_main("Вы можете называть меня как угодно, [genie_name]!","base","glance")
    else:
        call her_main("Уверена, [genie_name]. Мне нравится это имя.","base","base")
    jump hermione_talk

label hermione_change_fail:
    call her_main("Я не позволю вам, меня так называть!","scream","angryCl")
    jump hermione_talk
