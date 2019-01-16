label desk:
    menu:
        "-Изучить-" if not desk_examined:
            $ desk_examined = True
            m "Какой-то письменный стол..."
            jump day_main_menu
        "-Делать отчет-" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}-Делать отчет-{/color}" if finished_report >= 6 and not got_paycheck:
            m "Я уже закончил шесть отчетов на этой неделе."
            jump desk
        "{color=#858585}-Делать отчет-{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "Мне нужно сперва получить оплату."
            jump desk
         
        #"-Book collection- {image=book.png}" if not day == 1 and cataloug_found: 
        "-Собрание книг-" if not day == 1 and cataloug_found: 
            jump books_list
        
        
        #"-The muggle oddities-" if have_catalogue: #Real thing
        #"-DAHR's oddities-" if cataloug_found: 
        #    if order_placed or package_is_here:
        #        show screen bld1
        #        with d3
        #        dahr "Please be patient. The owl has been dispatched."
        #        hide screen bld1
        #        with d3
        #        jump desk
        #   else:
        #         jump the_oddities
        
        
        "-Дремать-" if daytime and not day == 1:
            jump night_start
        "-Поспать-" if not daytime and not day == 1:
            jump day_start
        
        #"-Jerk 0ff on Hermione's panties-" if hg_ps_PantyThief_OBJ.inProgress: #True when Hermione has no panties on.
        #    jump jerk_off
        "-Вздрочнуть-" if not day == 1:
            jump jerk_off
        
        "-Выйти-":
            call screen main_room_menu
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Ты занимаешься бумажной работой."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if not daytime and (1 < weather_gen < 4): # FULL MOON
        call f_moon_bonus 
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
#   ### CONCENTRATION CHECK ###========================================================================
#   if concentration == 1:
#       $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
#       if concentraton_check == 1:
#           call concentration_label
#   if concentration == 2:
#       $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
#       if concentraton_check == 1:
#           call concentration_label
#   if concentration == 3:
#       $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
#       if concentraton_check == 1:
#           call concentration_label
#   if concentration == 4:                                                               #Golden book.
#       call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 3) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label 
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 3) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check > 1:
            call speedwriting_label 
    if speedwriting == 3:
            call speedwriting_label 
    if speedwriting >= 4:
            call speedwriting_label 
            call concentration_label 
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 4:
        ">Ты закончил отчет."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Полнолуние, в это время ты чувствуешь себя более продуктивным.\n>Ты закончил [report_chapters] дополнительную главу."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Ты закончил главу [report_chapters]."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Ты сохраняешь идеальную концентрацию во время работы.\n>И заканчиваешь еще одну дополнительную главу отчета.\n>Ты закончил главу[report_chapters]."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Ты используешь свои навыки скорописания.\n>И заканчиваешь еще одну дополнительную главу отчета.\n>Ты закончил главу[report_chapters]."
    return
    
    
    
    
    
