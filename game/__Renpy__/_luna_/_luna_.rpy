#LUNA PLOT
#Turned into a bitchy Slytherin by the sorting hat. Willing to do anything for money/fame/status. Incredibly vain

#Don't forget to incorporate the quibbler

#LUNA MECHANICS




label luna_day_flags:
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
    $ luna_busy = False
return

label luna_night_flags:
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_busy = False
return


label luna_door:
    call luna_reset 
    $ renpy.play('sounds/door.mp3')
    $ luna_chibi("stand")
    if luna_dom >= luna_sub:
        if luna_dom >= 4:
            call luna_main("[l_genie_name]...", 9, 2, 2, 2) 
        else:
            call luna_main("[l_genie_name]...", 8, 2, 3, 3) 
    else:
        call luna_main("[l_genie_name]...", 1, 1, 4, 2) 

label luna_door_menu:
    menu:
        "-Поболтать-":
            call luna_chitchat 
            jump luna_door_menu
        "-Услуги-":
            if gold <= 100:
                m "Хм, мне, наверное, нужно немного больше галлеонов, если я хочу попросить ее об услугах..."
                jump luna_door_menu
            jump luna_favour_menu
        "-Отмена-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Поговори со мной-" if not luna_reverted:
            jump luna_favour_1
        "-Сядь ко мне на колени-" if luna_corruption >= 3 and not luna_reverted:
            jump luna_favour_2
        "-Разденься для меня-" if luna_corruption >= 5 and not luna_reverted:
            jump luna_favour_3
        "-Потрогай меня-" if luna_corruption >= 9 and not luna_reverted:
            if luna_corruption == 9:
                jump luna_reversion_event
            jump luna_favour_4
        "-Потрогай меня и Гермиону-" if luna_corruption >= 11 and not luna_reverted:
            jump luna_favour_5
        "-Пососи его-" if luna_corruption >= 14 and not luna_reverted:
            jump luna_favour_6
        "-Секс-" if luna_corruption >= 17 and not luna_reverted:
            jump luna_favour_7
        "-Отмена-":
            jump luna_door_menu

label luna_summon:
    $ changeLuna(8, 2, 3, 3)
return

label luna_away:
    call luna_reset 
    $ luna_busy = True
    $ renpy.play('sounds/door2.mp3')
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    show screen genie
    hide screen luna
    hide screen luna_chibi
    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with d3
    jump day_main_menu

label luna_reset:
    $ luna_flip = 1
    $ luna_l_arm = 1
    $ luna_r_arm = 1
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_chibi_image = "characters/luna/chibis/luna_stand.png" 
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250
    $ luna_tears = 0
    $ luna_wear_skirt = True
    $ luna_wear_top = True
    $ luna_wear_cum = False 
    $ luna_wear_cum_under = False 
    return

label luna_no_money:
    call luna_main("Вы ждете, что я сделаю это даром?", 8, 2, 3, 3) 
    call luna_main("Пф!", 8, 2, 3, 3) 
    jump luna_away

###CHIBIS###------------------------------------------------------




###PLOT###--------------------------------------------------------
#After the sex favour, Luna will either return to normal if you choose the sub route or she will become a slytherin dom if you go the dom route
#All the private favours will then have a 4th level unlocked, tailored to either the sub or dom option
