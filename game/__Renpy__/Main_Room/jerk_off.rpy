label jerk_off:

    $ d_flag_01 = False #Jasmine
    $ d_flag_02 = False #Lara
    $ d_flag_03 = False #


    if i_of_iv <= 2:
        $ d_flag_01 = True
    else:
        $ d_flag_02 = True
        
#    $ cum_on_panties = True #True when choose to cum on Hermione's panties.
#    m "Hm... Who shall be my target?"
#    menu:
#        "\"Princess Jasmine!\"":
#            m "Yes, the princess... That dirty slut!"
#            $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
#            pass
#        "\"Lara Croft\"":
#            $ jerking_off_to_lara = True
#            pass
#        "-Cancel-":
#            jump desk

    hide screen bld1
    hide screen genie
    call gen_chibi("jerking_off_behind_desk") 
    with d3
    pause 1
    
    call bld 
    m "Куда бы кончить?"
    
    label how_to_finish:
    menu:
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if not hg_ps_PantyThief_OBJ.inProgress:
            ">Отсутствует элемент(трусики), необходимый для этого параметра."
            jump  how_to_finish
        "-Трусики Гермионы-" if hg_ps_PantyThief_OBJ.inProgress:
            $ cum_on_panties = True #True when choose to cum on Hermione's panties.
        "-На пол!-":
            $ cum_on_panties = False #TRUE when chosen to cum on the floor.

### JERKING OFF ###
hide screen bld1
show screen blktone
call nar(">Ты решил вздрочнуть, вспоминая былые времена...") 
pause.5

if d_flag_01 and not cum_on_panties:
    call nar(">Ты фантазируешь о принцессе Жасмин...") 
    #g9 "Ух...да, та еще шлюшка..." -SadCrab
    g9 "Ух...да, та еще шлюшка..."
    
if d_flag_02 and not cum_on_panties:
    call nar(">Ты фантазируешь о Ларе Крофт...")
    #g9 "О да... эта соска была великолепна..." -SadCrab
    g9 "О да... эта соска была великолепна..."  
if cum_on_panties:
    call nar(">Ты фантазируешь о Гермионе...") 
    g4 "Да... она хорошая шлюха!"
    
pause.5

call nar(">Ты готов кончить...") 
pause.2

if d_flag_01 and not cum_on_panties:
    g4 "Архг! ПОЛУЧАЙ ПОТАСКУХА! Возьми все, принцесса-шлюха!!!"
if d_flag_02 and not cum_on_panties:
    g4 "Архг! ПОЛУЧАЙ ПОТАСКУХА! Возьми все, шлюха!!!"
if cum_on_panties:
    g4 "Архг! ПОЛУЧАЙ ПОТАСКУХА! Возьми все, маленькая шлюха!!!"

hide screen blktone
call gen_chibi("cumming_behind_desk") 
with hpunch
pause 1

if not cum_on_panties:
    call nar(">Ты кончаешь на пол.") 
if cum_on_panties:
    $ hg_ps_PantyThief_SoakedPantiesFlag = True #TRUE when you have the panties in your possession (before you return them to Hermione).
    call nar(">Ты кончаешь на трусики Гермионы, а затем используешь их, чтобы вытереть сперму с пола...") 
    call gen_chibi("cum_on_desk") 
    pause.5
    
    call nar(">Ты получил: \"Пропитанные спермой трусики\".") 

call gen_chibi("cum_on_desk") 
pause.2

call bld 
m "..."
m "Это было довольно, захватывающе..."
m "Вернусь к работе!"
    
### SETTING ALL THE FLAGS BACK TO DEFAULT ###
$ d_flag_01 = False
$ d_flag_02 = False
$ d_flag_03 = False
$ cum_on_panties = False #True when choose to cum on Hermione's panties.

hide screen genie_jerking_sperm_02
call gen_chibi("hide") 
show screen genie
hide screen bld1

if daytime:
    jump night_start
else: 
    jump day_start
