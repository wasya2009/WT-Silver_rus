label fireplace:
    if fireplace_examined:
        if not day == 1:
            $ fire_in_fireplace = not fire_in_fireplace 
        if fire_in_fireplace:
            show screen fireplace_fire
        else:
            hide screen fireplace_fire
            stop bg_sounds #Stops playing the fire SFX.
        jump day_main_menu
    else:
        menu:
            "-Осмотреть камин-" if not fireplace_examined:
                $ fireplace_examined = True
                hide screen genie
                call gen_chibi("stand","mid","base") 
                show screen chair_left #Empty chair near the desk.
                show screen desk
                with Dissolve(0.5)
                m "Хм... Выглядит как обычный камин..."
                show screen genie
                hide screen genie_stands
                hide screen chair_left #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu

            "-Назад-":
                jump day_main_menu
