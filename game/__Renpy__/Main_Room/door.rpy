label door:

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    menu:
        "-Осмотреть дверь-" if not door_examined:
            $ door_examined = True
            hide screen genie
            show screen chair_left #Empty chair near the desk.
            show screen chair_right
            call gen_chibi("stand","door","base") 
            show screen desk
            with Dissolve(0.5)
            m "На вид очень крепкая..."
            m "Интересно, что за ней стоит."
            label examining_the_door:
            menu:
                "-Стучать в дверь-":
                    show screen blktone8
                    with d3
                    call play_sound("knocking") 
                    "*Тук-тук-тук*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "Нет ответа..."
                    jump examining_the_door
                "-Приложить к ней ухо-":
                    show screen blktone8
                    with d3
                    ">Ты прислоняешь ухо к двери и пристально слушаешь..."
                    m "Ничего не слышно."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "-Выбить дверь-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Ударить!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "Эта дверь сможет выдержать и тысячу ударов, и все равно не сломается..." 
                    m "Не похоже, что она заперта, хотя..."
                    jump examining_the_door
                "-Оставить ее в покое-":
                    m "Кто знает, какие опасности могут таиться за этой дверью?"
                    m "Но думаю, всему свое время..."
                    pass

            call gen_chibi("hide") 
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            show screen genie
            with d3
            jump day_main_menu

        "-Исследовать замок-" if door_examined:
            if cataloug_found:
                hide screen main_room_menu
                call screen map_screen
            else:
                m "Я почти наверняка заблужусь без карты."
                m "Может, существует карта спрятанная где-то в этой комнате..."
                jump day_main_menu
                
                
                
        "{color=#858585}-Вызвать Асторию-{/color}" if astoria_busy and astoria_unlocked:
            if daytime:
                call nar(">Астория сейчас посещает уроки.") 
                jump day_main_menu
            else:
                call nar(">Астория уже спит.") 
                jump night_main_menu
        
        "-Вызвать Асторию-" if not astoria_busy and astoria_unlocked: #Summoning after intro events done.
            call play_music("chipper_doodle") 
            jump summon_astoria
            
            

        "{color=#858585}-Вызвать Сьюзан-{/color}" if susan_unlocked and susan_busy:
            if daytime:
                call nar(">Сьюзен сейчас посещает уроки.") 
                jump day_main_menu
            else:
                call nar(">Сьюзен уже спит.") 
                jump night_main_menu
        
        "-Вызвать Сьюзан-" if susan_unlocked and not susan_busy:
            jump summon_susan

            
            
        "{color=#858585}-Вызвать Гермиону-{/color}" if summoning_hermione_unlocked and hermione_takes_classes or hermione_sleeping:
            if hermione_takes_classes:
                call nar(">Гермиона сейчас посещает уроки.") 
                $ cust_char_1_enabled = True
                $ cust_char_2_enabled = True
                $ cust_char_3_enabled = True
                jump day_main_menu
            elif hermione_sleeping:
                call nar(">Гермиона уже спит.") 
                jump night_main_menu
        
        "-Вызвать Гермиону-" if summoning_hermione_unlocked and not hermione_takes_classes and not hermione_sleeping:
            jump summon_hermione

                
                
        "{color=#858585}-Вызвать Полумну-{/color}" if luna_known and luna_unlocked and luna_busy:
            if daytime:
                call nar(">Полумна сейчас посещает уроки.") 
                jump day_main_menu
            else: 
                call nar(">Полумна уже спит.") 
                jump night_main_menu
            
        "-Вызвать Полумну-" if luna_known and luna_unlocked and not luna_busy:
            call play_music("dark_fog") # LUNA'S THEME (placeholder probably)
            jump luna_door

            
            
        "{color=#858585}-Вызвать Чоу-{/color}" if cho_met and cho_busy:
            if daytime:
                call nar(">Чоу сейчас посещает уроки.") 
                jump day_main_menu
            else: 
                call nar(">Чоу уже спит.") 
                jump night_main_menu
            
        "-Вызвать Чоу-" if cho_met and not cho_busy:
            call play_music("chipper_doodle") # CHO'S THEME (placeholder probably)
            jump cho_menu
                  

                  
        "{color=#858585}-Вызвать Снейпа-{/color}" if hanging_with_snape and snape_busy:
            call nar(">Профессор Снейп сейчас недоступен.") 
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Вызвать Снейпа-" if hanging_with_snape and not snape_busy:
            call play_music("dark_fog") # SNAPE'S THEME
            jump summon_snape
            
            
            
        "{color=#858585}-Вызывать Тонкс-{/color}" if tonks_unlocked and tonks_busy:
            call nar(">Тонкс сейчас недоступна.") 
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
        
        "-Вызывать Тонкс-" if tonks_unlocked and not tonks_busy:
            jump summon_tonks
            
            
        "-Неважно-":
            jump day_main_menu
    


