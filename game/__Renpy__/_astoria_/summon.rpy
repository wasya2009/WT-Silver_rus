

label summon_astoria:

    call load_astoria_clothing_saves

    call play_sound("door") #Sound of a door opening.

    #Events
    if spells_unlocked and not susan_unlocked:
        $ susan_unlocked = True
        $ third_curse_got_cast = True
        $ spells_locked = True
        jump astoria_susan_intro

    ### RANDOM CLOTHING EVENTS ###
    call astoria_door_event

    call update_ast_uniform
    call update_sus_uniform #For events.

    #call ast_chibi("stand","mid","base")

    if one_of_ten < 4:
        call ast_main("Я вас категорически приветствую, [genie_name]!","tongue_silly","wink","base","mid",xpos="base",ypos="base")
    elif one_of_ten < 7:
        call ast_main("Здравствуйте, [genie_name].","smile","base","base","mid",xpos="base",ypos="base")
    else:
        call ast_main("Здрасьте, [genie_name]!","grin","angry","base","mid",xpos="base",ypos="base")

    $ astoria_busy = True

    label astoria_requests:

    $ menu_x = 0.1 #Menu is moved to the left.
    $ menu_y = 0.5 #Menu is moved to the middle.

    $ wardrobe_active = False

    menu:
        "-Говорить-":
            if not chitchated_with_astoria:
                call astoria_chit_chat
                jump astoria_talk
            else:
                jump astoria_talk

        "-Обучение Заклинаниям-" if snape_gave_spellbook:
            if not astoria_book_intro_happened:
                $ astoria_book_intro_happened = True
                jump astoria_book_intro
            else:
                jump astoria_spell_training
        "{color=#858585}-Обучение заклинаниям-{/color}" if spells_unlocked and not snape_gave_spellbook:
            call nar(">Для этого тебе нужно будет найти книгу.")
            jump astoria_requests
        "{color=#858585}-Скрыто-{/color}" if not spells_unlocked:
            call nar(">Ты еще не разблокировал эту функцию.")
            jump astoria_requests

        "-Использовать заклинание-" if spells_unlocked and not spells_locked:
            label astoria_target_select:
            menu:
                ">Выберать цель."
                "-Сьюзан-" if not susan_busy:
                    jump curse_susan
                "{color=#858585}-Сьюзан-{/color}" if susan_busy:
                    call nar(">Сьюзан недоступна.")
                    jump astoria_target_select
                "{color=#858585}-Гермиона-{/color}": #Hermione?
                    call nar(">Эта функция еще не добавлена.")
                    jump astoria_target_select
                "-Неважно-":
                    jump astoria_requests

            label curse_susan:
                menu:
                    ">Выбрать заклинание."
                    "-Imperio-" if astoria_spells[0] >= 1:
                        jump imperio_spell_1
                    "-Imperio Tempus-" if astoria_spells[0] >= 2:
                        jump imperio_spell_2
                    "-IMPERIO MAXIMUS-" if astoria_spells[0] >= 3:
                        jump imperio_spell_3
                    "-Imperio Tempo-" if susan_wardrobe_unlocked and not susan_imperio_influence:
                        "Примечание Разработчика:" ">Это временное заклинание, которое, скорее всего, будет удалено в будущем.\n>В настоящее время он открывает гардероб Сьюзан на короткое время."
                        jump susan_imperio
                    "{color=#858585}-Imperio Tempo-{/color}" if susan_wardrobe_unlocked and susan_imperio_influence:
                        call nar(">Сьюзан все еще под влиянием этого заклинания!")
                        jump curse_susan

                    "{color=#858585}-Скрыто-{/color}" if not susan_wardrobe_unlocked:
                        call nar(">Ты еще не разблокировал эту функцию.")
                        jump astoria_target_select
                    "{color=#858585}-Скрыто-{/color}" if astoria_spells[0] < 1:
                        call nar(">Ты еще не разблокировал эту функцию.")
                        jump astoria_target_select
                    "{color=#858585}-Скрыто-{/color}" if astoria_spells[0] < 2:
                        call nar(">Ты еще не разблокировал эту функцию.")
                        jump astoria_target_select
                    "{color=#858585}-Скрыто-{/color}" if astoria_spells[0] < 3:
                        call nar(">Ты еще не разблокировал эту функцию.")
                        jump astoria_target_select

                    "-Назад-":
                        jump astoria_target_select
        "{color=#858585}-Использовать заклинание-{/color}" if tonks_unlocked and spells_locked:
            call nar(">Ты недавно использовал непростительное проклятие!\n>Тонкс захочет поговорить с тобой, прежде чем ты сможешь использовать повторно.")
            jump astoria_requests
        "{color=#858585}-Использовать заклинание-{/color}" if not tonks_unlocked:
            call nar(">Тебе нужно будет найти способ разобраться с Министерством Магии прежде, чем использовать больше проклятий!")
            jump astoria_requests


        "{color=#858585}-Скрыто-{/color}" if not astoria_wardrobe_unlocked:
            call nar(">Ты еще не разблокировал эту функцию.")
            jump astoria_requests
        "-Инвентарь-" if astoria_wardrobe_unlocked:
            $ active_girl = "astoria"

            call load_astoria_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ wardrobe_active = 1 #True
            call ast_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        "-Отпустить ее-":
            if daytime:
                call ast_main("Тогда я вернусь к занятиям, [ast_genie_name].","smile","base","base","mid")
            else:
                call ast_main("О, хорошо. Спокойной ночи, [ast_genie_name].","smile","base","base","mid")

            hide screen astoria_main
            #hide screen astoria_blink #Astoria chibi.

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).

            $ astoria_busy = True

            if daytime:
                jump day_resume #Other return events can trigger after this!
            else:
                jump night_resume #Other return events can trigger after this!


label astoria_talk:
    menu:
        #"--":
        "-Обращайся ко мне только, как-":
            menu:
                "-Сэр-":
                    $ ast_genie_name = "Сэр"
                    call ast_main("Очень хорошо, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Дамблдор-":
                    $ ast_genie_name = "Тупица"
                    call ast_main("[ast_genie_name]!","smile","happyCl","base","mid")
                    m "Нет, я сказал Дамблдор!-- Дамблдор! (прим. игра слов: Dumby-дурачек, тупой; Dumbledore)"
                    call ast_main("Но мне больше нравится [ast_genie_name]!","grin","base","base","mid")
                    m "Черт возьми."
                    m "Хорошо, будь по-твоему..."
                    jump astoria_talk
                "-Профессор-":
                    $ ast_genie_name = "Профессор"
                    call ast_main("Конечно, [ast_genie_name].","pout","base","base","R")
                    jump astoria_talk
                "-Старик-":
                    $ ast_genie_name = "Старик"
                    call ast_main("Чудненько, [ast_genie_name].","grin","base","base","mid")
                    jump astoria_talk
                "-Джинн-":
                    $ ast_genie_name = "Джинн"
                    call ast_main("Что?! Вы джинн? Серьезно?","scream","wide","wide","wide")
                    call ast_main("Это так классно!","grin","wide","wide","wide")
                    m "(Ах да. Никто не должен об этом знать.)"
                    m "Это просто мое имя, [astoria_name]..."
                    call ast_main("О... ладно, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Лорд Волдеморт-":
                    $ ast_genie_name = "Лорд Волдеморт"
                    call ast_main("Волдеморт? Как этот злобный волшебник?","worried","wink","worried","mid")
                    call ast_main("Вы ведь не он, да?","clench","wide","wide","wide")
                    m "Нет, просто ролевая игра..."
                    call ast_main("О, тогда хорошо!","grin","happyCl","base","mid")
                    call ast_main("[ast_genie_name].","smile","narrow","narrow","mid")
                    jump astoria_talk
                "-Папочка-":
                    $ ast_genie_name = "Папочка"
                    call ast_main("Папочка? Вам не кажется это немного странным?","worried","wink","worried","mid")
                    m "Вовсе нет!"
                    call ast_main("Пфф...","pout","angry","angry","R")
                    call ast_main("Хорошо, почему бы и нет. Все равно никто об этом не узнает.","pout","angry","base","R")
                    jump astoria_talk
                "-Хозяин-":
                    $ ast_genie_name = "Хозяин"
                    call ast_main("Хахахаха-- Вы хотите, чтобы я называла вас хозяин?","happy","happyCl","worried","mid")
                    call ast_main("Это так глупо!","grin","happyCl","base","mid")
                    m "(...)"
                    call ast_main("Ну хорошо... Х-хозяин--","grin","ahegao","ahegao","ahegao")
                    call ast_main("Хахахаха--","happy","happyCl","base","mid")
                    m "Ты уже закончила?"
                    call ast_main("Да... Извините, пожалуйста... Я постараюсь, не смеяться в следующий раз. Обещаю.","smile","base","base","mid")
                    jump astoria_talk
                "-Свой вариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ ast_genie_name = "Sir"
                        call ast_main("Я просто буду называть вас [ast_genie_name] снова.","smile","base","base","mid")
                    else:
                        $ ast_genie_name = temp_name
                        call ast_main("Хм... ладно. Я буду звать вас [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Неважно-":
                    jump astoria_talk


        "-Отныне я буду называть тебя-":
            menu:
                "-Мисс Гринграсс-":
                    $ astoria_name = "Мисс Гринграсс"
                    call ast_main("Конечно, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Девочка-":
                    $ astoria_name = "Девочка"
                    call ast_main("Ладно, [ast_genie_name].","smile","base","worried","R")
                    jump astoria_talk
                "-Принцесса-":
                    $ astoria_name = "Принцесса"
                    call ast_main("Я действительно чувствую себя принцессой!","happy","angry","angry","mid")
                    call ast_main("В конце концов, я могу делать все, что захочу!","grin","angry","angry","angry")
                    jump astoria_talk
                "-Милашка-":
                    $ astoria_name = "Милашка"
                    call ast_main("Прекрасно... Если вам так действительно нужно, [ast_genie_name].","pout","base","worried","R")
                    jump astoria_talk
                "-Рабыня-":
                    $ astoria_name = "Рабыня"
                    call ast_main("Я вам не рабыня, [ast_genie_name]!","pout","angry","angry","R")
                    m "Конечно, ты ей не являешься! Мы просто играем в игру, вот и все..."
                    call ast_main("О, мне нравятся игры!","grin","wide","base","wide")
                    call ast_main("Вот и славненько!","grin","happyCl","worried","mid")
                    jump astoria_talk
                "-Свой ввариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ astoria_name = "Мисс Гринграсс"
                    else:
                        $ astoria_name = temp_name
                        call ast_main("Это немного чересчур, вам не кажется, [ast_genie_name]?","pout","angry","angry","R")
                        m "Вовсе нет!"
                        m "Я буду называть тебя так только когда мы будем одни, обещаю!"
                        call ast_main("Ну... Хорошо....","pout","angry","base","mid")
                    jump astoria_talk
                "-Назад-":
                    jump astoria_talk


        "-Назад":
            jump astoria_requests