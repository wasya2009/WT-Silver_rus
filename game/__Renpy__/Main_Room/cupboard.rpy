

label cupboard:
    menu:
        "-Осмотреть шкаф-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_left #Empty chair near the desk.
            hide screen genie
            call gen_chibi("stand","behind_desk","base",flip=True) 
            show screen desk
            with Dissolve(0.5)

            m "Хм....."
            m "Шкаф..."
            m "Может быть, мне в нем попозже порыться..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        
        "-Рыться в шкафу-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Рыться в шкафу-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        
        "-Твои вещи-" if not day == 1:
            label possessions:
                
            menu:
                "-Подарки-" if cataloug_found:
                    label possessions_gift_items:
                        $ choices = []
                        python:
                            for i in gift_list:
                                if gift_item_inv[i.id] > 0:
                                    choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
                        $ choices.append(("-Назад-", "nvm"))
                        $ result = renpy.display_menu(choices)
                        if result == "nvm":
                            jump possessions
                        else:
                            $ the_gift = result.image
                            show screen gift
                            with d3
                            ">[result.description]"
                            hide screen gift
                            with d3
                            jump possessions_gift_items
                
                "-Одежда-"if False:
                    label possessions_clothing:
                    menu:
                        "-Назад-":
                            jump possessions
                
                "-Зелья-" if False:
                    label possessions_potions:
                    menu:
                        "-Изготовление-" if False:
                            label possessions_potion_items:
                            menu:
                                "-Назад-":
                                    jump possessions_potions
                        "-Алхимия-":
                            label possessions_complete_potions:
                            menu:
                                "-Cum Addiction Potion-" if "Cum Addiction Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Ass Expansion Potion-" if "Ass Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Breast Expansion Potion-" if "Breast Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Cat Transformation Potion-" if "Cat Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Luna Transformation Potion-" if "Luna Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Lamia Transformation Potion-" if "Lamia Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Transparency Potion-" if "Transparency Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Назад-":
                                    jump possessions_potions
                        "-Назад-":
                            jump possessions
                
                "-Свиток Щупальца-" if tentacle_owned:
                    ">Должен ли я использовать этот свиток..."
                    menu:
                        "\"(Да, давай сделаем это!)\"":
                            jump tentacle_scene_intro
                        "\"(Нет, не сейчас.)\"":
                            jump possessions
                "-Свиток Щупальца-" if tent_scroll and not tentacle_owned:
                    m "Не хватает ключевого ингредиента."
                    jump possessions
                
                "-Бальное платье-" if "ball_dress" in gifts12 and not gave_the_dress:
                    $ the_gift = "images/store/01.png" # DRESS.
                    show screen gift
                    with d3
                    m "Модное вечернее платье, которое я купил..."
                    m "Надеюсь, оно подходящего размера."
                    hide screen gift
                    with d3
                    jump possessions
                    
                #"-\"П.У.К.Н.И.\" значок-" if badge_01 == 1:
                    $ the_gift = "images/store/29.png" # S.P.E.W. BADGE
                    show screen gift
                    with d3
                    m "значок \"П.У.К.Н.И.\"..."
                    hide screen gift
                    with d3
                    jump possessions
                    
                #"-Чулки в сеточку-" if nets == 1:
                    $ the_gift = "images/store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text 
                    hide screen gift
                    with d3
                    jump possessions
                    
                #"-Школьная мини-юбка-" if have_miniskirt:
                    $ the_gift = "images/store/07.png" # MINISKIRT.
                    show screen gift
                    with d3
                    m "Школьная мини-юбка ... Резко улучшает оценки."
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Вино Дамблдора-([wine])" if wine >= 1:
                    $ the_gift = "images/store/27.png" # WINE.
                    show screen gift
                    with d3
                    ">Бутылка вина из личного запаса профессора Дамблдора..." 
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Неизвестное зелье-([potions])" if  potions >= 1:
                    $ the_gift = "images/store/32.png" # HEALING POTION.
                    show screen gift
                    with d3
                    ">Какое-то зелье..." 
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Назад-":
                    jump cupboard
        
        "-Изготовление зелий-" if shop_found:
            jump potion_menu
        
        "-Опции-":
            menu:
                "-Изменить Имя Сохранения-":
                    jump custom_save
        
                "-Изменить Сложность Игры-":
                    menu:
                        "-Включить Легкую Сложность-":                                 #CHANGE IN 00_HT_Start, Start of game option.
                            #if hardcore_difficulty_active:
                            #    "Предупреждение: Это навсегда удалит ваши достижения за хардкорную сложность!"
                            #    #    menu:
                            #        "Хотите продолжить?"
                            #        "-Да, изменить сложность на легкую-":
                            #            menu:
                            #                "Вы правда уверены?"
                            #                "-Да, изменить сложность на легкую-":
                            #                    pass
                            #                "-Нет, вернуться-":
                            #                    jump day_main_menu
                            #        "-Нет, вернуться-":
                            #            jump day_main_menu
                            $ game_difficulty = 1
                            $ cheat_reading = True
                            $ hardcore_difficulty_active = False #removes hardcore rewards
                            "Игра установлена на Легко!"
                            "Увеличено вознаграждение за отчеты и других источников!" #CHANGE IN 01_hp_main_day and 15_mail.
                            "Больше пользы от поисков в шкафу!"    #CHANGE IN 11_cupboard, label rummaging.
                            "Снейп будет более щедр, очками со Слизерином!"    #CHANGE IN 06_points.
                            "Гермиона не будет злиться на тебя так долго!"           #CHANGE IN 01_hp_main_day.
                            jump day_main_menu
                        "-Включить Нормальную Сложность-":
                            #if hardcore_difficulty_active:
                            #    "Предупреждение: Это навсегда удалит ваши достижения за хардкорную сложность!"
                            #    menu:
                            #        "Хотите продолжить?"
                            #        "-Да, изменить сложность на нормальную-":
                            #            menu:
                            #                "Вы правда уверены?"
                            #                "-Да, изменить сложность на нормальную-":
                            #                    pass
                            #                "-Нет, вернуться-":
                            #                    jump day_main_menu
                            #        "-Нет, вернуться-":
                            #            jump day_main_menu
                            $ game_difficulty = 2
                            $ cheat_reading = False
                            $ hardcore_difficulty_active = False #removes hardcore rewards
                            "Игра установлена на Нормально!"
                            jump day_main_menu
                        #"-Включить Хардкорную Сложность-": #Original Game Difficulty
                        #    "Это не добавит хардкорных достижений за сложность!"
                        #    "Чтобы получить достижения за хадкорную сложность, вам нужно будет начать новую игру на хардкоре и оставаться на этой сложности!"
                        #    $ game_difficulty = 3
                        #    $ cheat_reading = False
                        #    "Игра изменена на Хардкорный!"
                        #    jump day_main_menu
                        #"-Чит добавит достижения на хардкорном уровне сложности-":
                        #    if hardcore_difficulty_active:
                        #        ">Rewards are now disabled."
                        #        $ hardcore_difficulty_active = False
                        #    else:
                        #        ">Rewards are now active."
                        #        $ hardcore_difficulty_active = True
                        #        jump day_main_menu
                        "-Назад-":
                            jump day_main_menu
                "-Заменить Чибиков Спрайтами-" if not use_cgs:
                    ">В последних двух личных услугах, теперь будут использоваться спрайты."
                    $ use_cgs = True
                    jump cupboard
                "-Заменить спрайты на Чибиков-" if use_cgs:
                    ">В последних двух личных услугах, снова будут использованы чиби-анимации."
                    $ use_cgs = False
                    jump cupboard
                "-Назад-":
                    jump cupboard

        "-Шалунишка-" if cheats_active:
            jump cheats
            
        "-Отправить снова письмо Министерству-" if day >= 25 and whoring >= 9 and not ministry_letter_received:
            $ ministry_letter = True
            $ letters += 1 #Displays Owl
            ">Ты получил новое письмо."
            jump cupboard

        "-Сбросить весь контент Полумны-":
            $ reset_luna_content = True
            call luna_init 
            call luna_progress_init 
            $ reset_luna_content = False
            ">Контент Полумны сброшен!"
            jump cupboard

        "-Выйти-":
            jump day_main_menu

label scrolls_menu:
    menu:
        "-Священные свитки том I-" if cataloug_found:
            $ scrolls_range = range(1,16)
        "-Священные свитки том II-" if cataloug_found:
            $ scrolls_range = range(16,31)
        "-Выйти-":
            jump day_main_menu

    label sc_col_men:
    python:
        scrolls_menu = []
        for scroll in scrolls_range:
            sc = sacred_scrolls[scroll]
            if sscroll_[sc.id]:
                scrolls_menu.append( ("-Свиток №"+str(sc.id)+": "+str(sc.name)+"-", scroll) )
        scrolls_menu.append(("-Назад-", "nvm"))
        result = renpy.display_menu(scrolls_menu)

    if result == "nvm":
        jump scrolls_menu
    else:
        $ the_gift = "images/misc/extras/"+str(result)+".png" # SACRED SCROLL
        show screen gift
        show screen ctc
        with d3
        pause
        hide screen gift
        hide screen ctc
        with d3
        jump sc_col_men

    
label custom_save:
    $ temp_name = renpy.input("(Введите имя сохранения.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "День - "+str(day)+"\nРазвращение - "+str(whoring)
    $ save_name = temp_name
    "Готово."
    jump cupboard

label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen genie
    show screen rum_screen
    with d3
    show screen bld1
    with d3
    ">Какое-то время, ты рылся в шкафу..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "images/store/32.png"
            show screen gift
            with d3
            ">Ты нашел какое-то зелье..." 
            hide screen gift
            with d3
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start
    
    if rum_times >= 7 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "images/store/31.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">Ты нашел карту территории школы...\n>Теперь ты можешь покидать башню."
        hide screen gift
        with d3
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    if game_difficulty >= 2:                   #Normal and hardcore difficulty
        if i_of_iv == 4: # Found something.
            jump rum_rewards
        else:                                  #Easy difficulty
            ">...Ты не находишь ничего ценного."
            show screen genie
            hide screen rum_screen
    
            hide screen bld1
            with d3
    
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
    else:
        jump rum_rewards 

label rum_rewards:
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            if one_of_tw == 20:
                call rum_block(PlushOwl) 
            elif one_of_tw == 1 or one_of_tw == 2:
                call rum_block(Lollipop) 
            elif one_of_tw >= 3 and one_of_tw <= 9  or one_of_tw == 18:
                call rum_block("gold1") 
            elif one_of_tw >= 10 and one_of_tw <= 16:
                call rum_block("wine") 
            elif one_of_tw == 17:
                call rum_block(Chocolate) 
            elif one_of_tw == 19:
                call rum_block(SexyLingerie) 
        
        
        ### EVENT LEVEL 02 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 6 and whoring <= 11: # Lv 3-4. 
            if one_of_tw == 20:
                call rum_block(PornMagazines) 
            elif one_of_tw == 1 or one_of_tw ==2:
                call rum_block(Lollipop) 
            elif one_of_tw >= 3 and one_of_tw <= 10 or one_of_tw == 18:
                call rum_block("gold2") 
            elif one_of_tw >= 11 and one_of_tw <= 15:
                call rum_block("wine") 
            elif one_of_tw == 16:
                call rum_block(SexyLingerie) 
            elif one_of_tw == 17:
                call rum_block(Chocolate) 
            elif one_of_tw == 19:
                call rum_block(ViktorKrumPoster) 
        
        
        ### EVENT LEVEL 03 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            if one_of_tw == 20:
                call rum_block(Vibrator) 
            elif one_of_tw >= 1 and one_of_tw <= 4:
                call rum_block(PackOfCondoms) 
            elif one_of_tw == 5 or one_of_tw == 6:
                call rum_block("gold1") #Bugfix? Previously was just (1). 
            elif one_of_tw >= 7 and one_of_tw <= 14:
                call rum_block("gold3") 
            elif one_of_tw >= 15 and one_of_tw <= 18:
                call rum_block("wine") 
            elif one_of_tw == 19:
                call rum_block(ViktorKrumPoster) 
        
        
        ### EVENT LEVEL 04 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 18: # Lv 7+  
            if one_of_tw == 20:
                call rum_block(SpeedStick2000) 
            elif one_of_tw >= 1 and one_of_tw <= 4:
                call rum_block(Butterbeer) 
            elif one_of_tw >= 5 and one_of_tw <= 8:
                call rum_block(Chocolate) 
            elif one_of_tw >= 9 and one_of_tw <= 16:
                call rum_block("gold4") 
            elif one_of_tw == 17:
                call rum_block(AnalPlugs) 
            elif one_of_tw == 18:
                call rum_block(ViktorKrumPoster) 
            elif one_of_tw == 19:
                call rum_block(ThestralStrapon) 
        
        show screen genie
        hide screen rum_screen
    
        hide screen bld1
        with d3
    
        if daytime:
            jump day_main_menu
        else: 
            jump night_main_menu
        
label rum_block(item = None):
    if isinstance(item, gift_item):
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ gift_item_inv[item.id] += 1
        $ the_gift = item.image
        show screen gift
        with d3
        ">Ты нашел [item.name]..."
        ">[item.description]"
        hide screen gift
        with d3
    else:
        if "wine" in item:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ wine += 1
            $ the_gift = "images/store/27.png" # WINE
            show screen gift
            with d3
            ">Ты нашел бутылку вина из личных запасов профессора Дамблдора..." 
            hide screen gift
            with d3
        if "gold" in item:
            if item == "gold1":
                $ tmp_gold = gold1
            if item == "gold2":
                $ tmp_gold = gold2
            if item == "gold3":
                $ tmp_gold = gold3
            if item == "gold4":
                $ tmp_gold = gold4
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ the_gift = "images/store/28.png" # GOLD.
            show screen gift
            with d3
            ">Ты нашел [tmp_gold] галлеонов..." 
            $ gold += tmp_gold
            hide screen gift
            with d3
    return
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "Я уже сегодня это делал..."
    hide screen bld1
    with d3
    return
