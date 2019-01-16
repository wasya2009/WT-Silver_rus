

label summon_tonks:
    
    call play_sound("door") 
    $ menu_x = 0.5
    $ menu_y = 0.5

    #ADD Tonks chibi here.
    
    call ton_main("Вы звали, [ton_genie_name]?","base","base","base","mid",xpos="base",ypos="base") 
    
    label tonks_requests:
    
    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!
    
    menu:
        "-Говорить-":
            if not chitchated_with_tonks: 
                call tonks_chit_chat 
                #jump tonks_talk
                jump tonks_requests
            else:
                #jump tonks_talk
                jump tonks_requests
            
            
        "{color=#858585}-Отправить Асторию с ней-{/color}" if spells_locked and (astoria_busy or not daytime):
            if daytime:
                call nar(">Астория в настоящее время недоступна.") 
            else:
                call nar(">Слишком поздно посылать Асторию с Тонкс сегодня! Попробуй завтра.") 
            jump tonks_requests
        "-Отправить Асторию с ней-" if spells_locked and daytime and not astoria_busy:
            call blkfade 
            call nar(">Ты вызываешь Асторию.") 
            pause.5
            hide screen blkfade
            call ast_main("Привет, [ast_genie_name]!","grin","base","base","mid",xpos="mid",ypos="base",trans="fade") 
            call ast_main("Здравствуйте, Мисс Тонкс.","worried","base","worried","R") 
            call ton_main("Здравствуйте, [ton_astoria_name].","horny","base","raised","L") 
            call ast_main("{size=-2}[ast_tonks_name]...{/size}","pout","narrow","narrow","L") 
            if one_out_of_three == 1:
                m "Астория, я хочу, чтобы Вы снова провели день с мисс Тонкс."
            if one_out_of_three == 2:
                m "Мисс Гринграсс, вы сегодня проведете некоторое время с мисс Тонкс."
            if one_out_of_three == 3:
                m "Девочка, ты сегодня пойдешь с мисс Тонкс. Нравится тебе это или нет..."
            call ast_main("Еще раз?! Неужели мне это нужно?","pout","base","worried","mid") 
            m "Да."
            call ton_main("Не волнуйся [ton_astoria_name]. Это будет весело!","base","base","base","L") 
            call ton_main("Береги себя, [ton_genie_name].","base","base","base","mid") 
            call ast_main("...","pout","base","worried","L") 
            call play_sound("door") 
            hide screen tonks_main
            with d3
            
            pause.5
            call play_sound("door") 
            hide screen astoria_main
            hide screen bld1
            with d3
            
            $ astoria_busy = True
            $ tonks_busy = True
            
            $ astoria_tonks_event_in_progress = True
            
            call play_music("brittle_rille") #Day Theme
            jump day_main_menu
            
            
        "-Неважно-":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)

            if daytime:
                ton "Хорошо, вернемся к работе ..."
            else: 
                ton "Сладких снов, [ton_genie_name]."

            $ tonks_busy = True
            hide screen bld1
            hide screen tonks_main
            with d3
            call play_sound("door") 

            if daytime:
                call play_music("brittle_rille") #Day Theme
                jump day_main_menu
            else: 
                call play_music("manatees") #Night Theme
                jump night_main_menu