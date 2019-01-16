


label summon_susan:

    call load_susan_clothing_saves 

    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    #call susan_door_event

    call update_sus_uniform 

    #call sus_chibi("stand","mid","base")

    if one_of_ten < 4:
        if daytime:
            call sus_main("Добрый день, [genie_name].","base","base","base","mid",xpos="base",ypos="base") 
        else:
            call sus_main("Добрый вечер, [genie_name].","base","base","base","mid",xpos="base",ypos="base") 
    elif one_of_ten < 7:  
        call sus_main("Чем я могу вам помочь, [genie_name]?","base","base","worried","R",xpos="base",ypos="base") 
    else:
        call sus_main("Вы хотели меня видеть, [genie_name]?","base","base","worried","down",xpos="base",ypos="base") 

    label susan_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        "-Говорить-":
            if not chitchated_with_susan: 
                call susan_chit_chat 
                jump susan_talk
            else:
                jump susan_talk 
                
        "-Инвентарь-" if susan_wardrobe_unlocked and susan_imperio_influence:
            $ active_girl = "susan"

            call load_susan_clothing_saves 

            call reset_wardrobe_vars 
            call update_wr_color_list 

            $ wardrobe_active = 1 #True
            call sus_main(xpos="wardrobe",ypos="base") 
            call screen wardrobe
        "{color=#858585}-Инвентарь-{/color}" if susan_wardrobe_unlocked and not susan_imperio_influence:
            call nar(">Сьюзан не позволит тебе изменить ее гардероб!") 
            jump susan_requests
        "{color=#858585}-Скрытый-{/color}" if not susan_wardrobe_unlocked:
            call nar(">Вы еще не разблокировали эту функцию.") 
            jump susan_requests
            
        "-Отпустить ее-":
            if daytime:
                call sus_main("Тогда я вернусь к занятиям, [sus_genie_name].","base","base","base","down") 
            else:
                call sus_main("Хм... спокойной ночи, [sus_genie_name].","base","base","base","down") 

            hide screen susan_main
            #hide screen susan_blink #Susan chibi.

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).
                    
            $ susan_busy = True  
            
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
                    
                    
label susan_talk: 
    menu: 
        #"--":
        "-Обращайся ко мне...-":
            menu:
                "-Сэр-":
                    $ sus_genie_name = "Сэр"
                    call sus_main("Хорошо, [sus_genie_name].","base","base","base","mid") 
                    jump susan_talk
                "-Дамблдор-":
                    $ sus_genie_name = "Дамблдор"
                    call sus_main("Ладно, [sus_genie_name].","base","base","worried","down") 
                    jump susan_talk
                "-Профессор-":
                    $ sus_genie_name = "Профессор"
                    call sus_main("Конечно, [sus_genie_name].","base","base","base","R") 
                    jump susan_talk
                "-Старик-":
                    $ sus_genie_name = "Старик"
                    call sus_main("Это было бы не очень вежливо, профессор.","open","closed","base","mid") 
                    m "Не волнуйся, [susan_name]. Я всегда говорю своим ученикам называть меня глупыми именами."
                    g9 "Это помогает сблизиться с ними!"
                    call sus_main("Если вы так говорите..... Хм-- [sus_genie_name].","base","base","base","mid") 
                    g4 "И скоро я собираюсь сблизиться с твоими сиськами!"
                    jump susan_talk
                "-Джинн-":
                    $ sus_genie_name = "Джинн"
                    call sus_main("Я...--","upset","base","base","L") 
                    call sus_main("Все люди называют вас так?","upset","narrow","worried","mid") 
                    m "Да-да--, все!"
                    m "Это совершенно нормально!"
                    call sus_main("(...)","upset","base","worried","down") 
                    call sus_main("Х-хорошо,... [sus_genie_name].","base","base","worried","R") 
                    jump susan_talk
                "-Лорд Волдеморт-":
                    $ sus_genie_name = "Лорд Волдеморт"
                    call sus_main("Почему вы хотите, чтобы я вас так называла?","open","closed","worried","mid") 
                    call sus_main("Мы не должны упоминать это имя!","open","narrow","worried","down") 
                    m "Это всего лишь имя, девочка..."
                    call sus_main("Это имя, сами знаете кого!","upset","closed","worried","mid") 
                    call sus_main("Это имя действительно пугает меня, профессор!","open","closed","worried","mid") 
                    m "Я не хочу, чтобы мои ученики боялись имен, Сьюзан! Это тренировка."
                    m "Давай... скажи."
                    call sus_main("Ладно...","open","narrow","worried","down") 
                    call sus_main("В-Волдеморт--...","upset","closed","worried","mid") 
                    jump susan_talk
                "-Папочка-":
                    $ sus_genie_name = "Папочка"
                    call sus_main("Сэр, нет!","scream","closed","worried","mid") 
                    call sus_main("Я не могу вас так называть!","scream","wide","angry","wide") 
                    m "Но я так хочу."
                    g9 "Нет ничего плохого в том, чтобы называть меня папочкой."
                    call sus_main("Но это же!--","open","narrow","angry","mid") 
                    call sus_main("(Это неправильно, Сьюзан!)","upset","narrow","worried","down") 
                    call sus_main("Хорошо,... Профессор-- Ээээх--... П-папочка.","base","closed","worried","mid") 
                    jump susan_talk
                "-Хозяин-":
                    $ sus_genie_name = "Хозяин"
                    call sus_main("Х-Хозяин?","upset","narrow","base","mid") 
                    call sus_main("Не думаю, что мне стоит так называть своих учителей.","open","closed","worried","mid") 
                    m "Нет-нет--, это то, как вы нынче называете своих учителей!"
                    m "Но только зови меня так!"
                    call sus_main("Хм--... хорошо, [sus_genie_name].","upset","narrow","worried","R") 
                    jump susan_talk
                "-Ввести свой вариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ sus_genie_name = "Сэр"
                        call sus_main("Я буду называть вас [sus_genie_name] снова.","base","base","base","mid") 
                    else:
                        $ sus_genie_name = temp_name
                        call sus_main("Хм... ладно. Я буду звать вас [sus_genie_name].","upset","narrow","base","L") 
                    jump susan_talk
                "-Неважно-":
                    jump susan_requests
                
             
        "-Отныне, я буду называть тебя-":
            menu:
                "-Мисс Боунс-":
                    $ susan_name = "Мисс Боунс"
                    call sus_main("Конечно, [sus_genie_name].","base","base","base","mid") 
                    jump susan_talk
                "-Девочка-":
                    $ susan_name = "Девочка"
                    call sus_main("Меня это устраивает, [sus_genie_name].","base","base","worried","R") 
                    jump susan_talk
                "-Коровка-":
                    $ susan_name = "Коровка"
                    call sus_main("Почему вы хотите называть меня так, [sus_genie_name]?","upset","narrow","worried","down") 
                    call sus_main("Другие девушки уже называют меня так, и я ненавижу это...","open","base","worried","down") 
                    m "Бедняжка!"
                    m "Видишь ли, если бы кто-то вроде меня назвал тебя так, возможно, это не повлияло бы на тебя так сильно."
                    call sus_main("Я--... Возможно, вы правы.","upset","narrow","base","down") 
                    call sus_main("Вы можете называть меня буренка, [sus_genie_name].","base","base","base","mid") 
                    jump susan_talk
                "-Шлюха-":
                    $ susan_name = "Шлюха"
                    call sus_main("[sus_genie_name]!","scream","closed","angry","R") 
                    call sus_main("Вы серьезно!","scream","wide","base","wide") 
                    m "Почему нет. Никто не узнает..."
                    call sus_main("Как вы могли так обо мне подумать!","open","base","worried","down") 
                    call sus_main("Я не... шлюха.","upset","narrow","worried","R") 
                    m "Конечно, нет. Это просто для того, чтобы укрепить твою самооценку."
                    m "Поверь мне, я знаю, что делаю."
                    m "Назваться шлюхой, всегда повышает уверенность у девушки!"
                    call sus_main("П-правда?","open","base","base","mid") 
                    m "Да. Теперь... мы должны попробовать?"
                    call sus_main("... Хорошо, [sus_genie_name]...","upset","narrow","worried","R") 
                    jump susan_talk
                "-Ввести свой вариант-":
                    $ temp_name = renpy.input("(Пожалуйста, введите имя.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ susan_name = "Мисс Боунс"
                    else:
                        $ susan_name = temp_name
                        call sus_main("Мне это не нравится, но--","open","closed","worried","mid") 
                        call sus_main("Обещайте, что будете меня так называть, только когда мы будем одни.","upset","base","worried","mid") 
                        g9 "Обещаю!"
                    jump susan_talk
                "-Неважно-":
                    jump susan_talk

                    
        "-Назад":
            jump susan_requests