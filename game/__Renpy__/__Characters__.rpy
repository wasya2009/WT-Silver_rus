
###HARRY POTTER CHARACTERS###
init python:
    # Character tables
    dev = Character('Red Machine', color = "#FF0000")
    
    ### GENIE ### (others are in scripts.rpy)
    m = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")
    g4 = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage4.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")
    g9 = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage9.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")

    
    ### SNAPE HEAD ###
    sna_ = [""]
    for i in range(1,26):
        sna_.append("")
        sna_[i] = Character("Северус Снейп", color="#402313", show_side_image=Image("characters/snape/head/head_" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    
    ### HERMIONE HEAD (OLD) ###
    her_ = [""]
    for i in range(1,43):
        her_.append("")
        her_[i] = Character('[hermione_name]', color="#402313", window_left_padding=250, window_right_padding=270, show_side_image=Image("images/15_hermione_head/" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")

        
    ### DUMBLEDORE HEAD ###
    dum_ = [""]
    for i in range(1,6):
        dum_.append("")
        dum_[i] = Character(None, window_left_padding=250, color="#402313", show_side_image=Image("characters/dumbledore/dum_"+str(i)+".png", xpos=20, yalign=1.0), show_two_window=False, ctc="ctc3", ctc_position="fixed")
        

    
    ### STUDENTS ###
    her  = Character('[hermione_name]', color="#402313", window_left_padding=250, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)
    her2 = Character('[hermione_name]', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    lher = Character('Гермиша', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)
    herA = Character('Скромница Гермиона', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)
    
    lun  = Character('Полумна', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cho  = Character('Чоу', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sus  = Character('Сьюзен', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ast  = Character('Астория', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    twi  = Character('Фред и Джордж', color="#402313", show_two_window=True, show_side_image=Image("characters/weasley_twins/base_01.png", xalign=1.0, yalign=1.0), ctc="ctc3", ctc_position="fixed", window_right_padding=100)
    fre  = Character('Фред', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/weasley_twins/fred_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)
    ger  = Character('Джордж', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/weasley_twins/george_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)
    
    
    
    ### TEACHERS ###
    sna  = Character('Северус Снейп', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sna  = Character('Северус Снейп', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    ton  = Character('Тонкс', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    spo  = Character('Профессор Спраут', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hoo  = Character('Мадам Хуч', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hat  = Character('Шляпа', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/misc/hat/hat.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)
    msp  = Character('Джинн', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    
    
    ### Other Characters ###
    s = Character(None, color="#402313", ctc="ctc3", ctc_position="fixed")
    nar = Character(None, color="#402313", show_two_window=False, ctc="ctc3", ctc_position="fixed")
    
    maf  = Character('Мадам Помфри', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/mafkin/maf_1.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=270)
    abe  = Character('Аберфорт', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    vol  = Character('Волан-де-Морт', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    faw  = Character('Фоукс', color="#f21111", window_right_padding=270, show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
   
    fem  = Character('Студентка', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal  = Character('Студент # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal2 = Character('Студент # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly1 = Character('Студент Слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly2 = Character('Другой Студент Слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ann  = Character('Диктор', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr1  = Character('Кто-то из толпы', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr2  = Character('Кто-то другой, из толпы', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    l    = Character('Лола', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed")
    dahr = Character(None, color="#402313", window_left_padding=270, show_side_image=Image("images/store/dahr.png", xalign=0.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc4", ctc_position="fixed")

