

label summon_snape:
    
    call play_sound("door") 
    $ menu_x = 0.5
    $ menu_y = 0.5

    $ snape_chibi_xpos = 500 #Mid
    $ snape_chibi_ypos = 240
    show screen snape_01 #Snape stands still.
    call bld 

    call sna_main("Да, чего звал?","snape_01",xpos="base",ypos="base") 

    label snape_ready:
        pass

    menu:
        "-Получить зелье-" if whoring > 10:
            hide screen snape_main
            with fade
            
            sna_[9] "Я заметил, что ты добился некоторого прогресса с мисс Грейнджер."
            sna_[21] "У меня есть разные зелья, которые обычно не доступны для студентов."
            sna_[21] "Они могут ускорить процесс..."
            menu:
                "-Lactantium-" if potion_inv.has("p_milk_potion"):
                    ">У вас уже есть зелье Lactantium."
                    jump snape_ready
                "-Lactantium-" if not potion_inv.has("p_milk_potion"):
                    if potion_scene_11_progress < 1:
                        sna_[9] "Ах да, моя уникальная смесь. У меня всегда под рукой есть пузырек."
                        sna_[13] "На всякий случай..."
                        sna_[18] "Вот, возьми!"
                        ">Снейп передает тебе зелье Lactantium в руки."
                        ">Получено Lactantium!"
                        $ potion_inv.add("p_milk_potion")
                    elif potion_scene_11_progress == 1:
                        sna_[9] "Хорошая мысль заставить ее принять его."
                        sna_[13] "Ее грудь действительно великолепно выглядела в классе."
                        sna_[13] "мммм, и я думаю, что она даже немного набухла..."
                        sna_[20] "Пусть примет еще одну!"
                        sna_[18] "Вот, я даже дам тебе доитель для шлюхи!"
                        ">Снейп вручает тебе странную кожано-металлическую упряжь."
                        m "Что-"
                        ">Снейп передает тебе зелье Lactantium в руки."
                        ">Получено Lactantium!"
                        sna_[12] "Не волнуйся об этом, просто заставь ее это надеть. Он заколдован, поэтому справится с остальным..."
                        sna_[6] "Но я хочу, чтобы ты мне его вернул, прежде чем вернешься в свой мир!"
                        sna_[20] "Я потратил целое состояние на модель с самоочисткой..."
                        $ potion_inv.add("p_milk_potion")
                    else:
                        sna_[13] "Мммм, жаль, что я не смогу воочию увидеть, как ты будешь ее доить..."
                        m "..."
                        m "(Вероятно, это не очень хорошая идея...)"
                        sna_[12] "Все это {b}лакомое{/b} молочко..."
                        m "(Определенно не очень хорошая идея.)"
                        sna_[13] "..."
                        sna_[9] "В любом случае, это интересно..."
                        sna_[9] "Хочешь, я дополню зелье?"
                        m "Дополнишь?"
                        m "Я же об этом никогда не просил..."
                        sna_[6] "Я знаю... Я просто предлагаю тебе..."
                        m "Ах да, извини. Какое дополнение?"
                        sna_[10] "Ну, я могу оставить зелье как есть..."
                        sna_[12] "Или я могу добавить к этому еще кое-что."
                        m "Например?"
                        sna_[9] "Ну..."
                        label snape_potion_choice:
                            pass
                        menu:
                            "-Обычное зелье-":
                                sna_[7] "Вот, пожалуйста, мистер Авантюрист..."
                                $ potion_version = 1
                            "-Futa зелье-":
                                sna_[17] "Что? Ты уверен,что хочешь этого?"
                                sna_[18] "В смысле, я догадывался, что ты немного извращенец..."
                                sna_[19] "Но о таком даже, не думал..."
                                sna_[18] "Ну что ж, если ты этого хочешь, то оно твое..."
                                menu:
                                    "-Дай его мне-":
                                        sna_[17] "Действительно?"
                                        sna_[18] "Ты более предприимчив, чем я думал!"
                                        sna_[20] "Вот, я даже дам тебе дополнительную насадку для дояра!"
                                        ">Снейп вручает тебе другую канистру с мягким пластиковым отверстием внизу. Выглядит почти как анус."
                                        sna_[19] "Я также наложил заклятие незримого расширения на канистру... Обещай рассказать мне, подробности!"
                                    "-Нет-":
                                          sna_[7] "Жаль..."
                                          jump snape_potion_choice  
                                          
                                $ potion_version = 2
                            "-Зелье увеличения груди-":
                                sna_[18] "Производство молока по-прежнему будет длиться только день..."
                                sna_[9] "Но ее увеличенная грудь будет постоянна..."
                                sna_[18] "Ты уверен, что хочешь этого?"
                                sna_[20] "Ей это может не понравиться..."
                                menu:
                                    "-Да--":
                                        sna_[19] "Фантастика!!!"
                                    "-Нет-":
                                          sna_[7] "Жаль..."
                                          jump snape_potion_choice  

                                $ potion_version = 3
                        ">Снейп передает тебе зелье Lactantium в руки."
                        ">Получено Lactantium!"
                        $ potion_inv.add("p_milk_potion")
                    jump snape_ready
                
                "-Veritaserum-" if potion_inv.has("p_veritaserum"):
                    ">У вас уже есть зелье Veritaserum."
                    jump snape_ready
                "-Veritaserum-" if not potion_inv.has("p_veritaserum"):
                    sna_[1] "Зелье правды."
                    sna_[1] "Это опасная штука, Джинн..."
                    sna_[21] "Используй его, чтобы заставить кого-нибудь говорить правду."
                    sna_[8] "Только не на мне!"
                    ">Снейп вручает тебе крошечный пузырек, наполненный странной золотой жидкостью."
                    ">Получено Veritaserum!"
                    $ potion_inv.add("p_veritaserum")
                    jump snape_ready
                
                "-Voluptatem-" if potion_inv.has("p_voluptatem"):
                    ">У вас уже есть зелье Voluptatem."
                    jump snape_ready
                "-Voluptatem-" if not potion_inv.has("p_voluptatem"):
                    m "Volupwhatem?"
                    sna_[1] "Это мое экспериментальное зелье..."
                    sna_[7] "Я не уверен, что оно готово для тестирования на людях."
                    ">Снейп вручает тебе маленькую бутылочку, наполненную кружащейся розово-фиолетовой жидкостью."
                    ">Получено Voluptatem!"
                    $ potion_inv.add("p_voluptatem")
                    jump snape_ready

                "\"Неважно.\"":
                    jump snape_ready

        "\"-Поболтать-\"" if not chitchated_with_snape:
            $ chitchated_with_snape = True
            jump snape_talk
        
        "\"Развеятся\"" if not daytime and not sfmax: # Turns TRUE when friendship with Snape been maxed out.
            if one_of_ten == 10 and game_difficulty >= 2:  #Doesn't happen with easy difficulty.
                jump not_today #Snape says: "I am busy tonight."
#            elif snape_friendship >= 39 and whoring <= 5: # Whoring level <= 2. Makes sure you don't proceed after Date #6 until reached Whoring lvl 3.
#                jump not_today #Snape says: "I am busy tonight."
            elif snape_friendship >= 88 and whoring <= 14: # Whoring level <= 5. Makes sure you don't proceed after Date #12 until reached Whoring lvl 6.
                jump not_today #Snape says: "I am busy tonight."
            else:
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                jump snape_dates
                
        "\"Увидимся позже\"":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)

            if daytime:
                sna "Ладно, тогда вернусь к работе..."
            else: 
                sna "Тогда спокойной ночи."

            $ snape_busy = True
            hide screen snape_01 #Snape stands still.
            hide screen bld1
            hide screen snape_main
            with d3
            call play_sound("door") 

            if daytime:
                call play_music("brittle_rille") #Day Theme
                jump day_main_menu
            else: 
                call play_music("manatees") #Night Theme
                jump night_main_menu

label snape_dates:  ### HANGING WITH SNAPE ###
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    show screen blkfade
    $ fire_in_fireplace = True
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk
    show screen with_snape_animated
    show screen fireplace_fire
    
    hide screen snape_01 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    
    hide screen blkfade
    with fade
    
   
    if snape_against_hermione: #Turns True after event_08 (Hermione shows up for the first time).
                               #Activates special event when hanging out with Snape next time.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape
    
    if snape_against_hermione_02: #Activates after second visit from Hermione (event_09).
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_02

    if hg_pf_DanceForMe_OBJ.points >= 2 and not snape_invated_to_watch: #After second dance where Snape entered room.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_03
    
    #ADD sQuest here "Pensieve Event"
    
    if wine >= 1 and not wine_not: # Using Dumbledor's wine for the first time.
        $ wine_not = True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
        call wine_first 
    elif wine >= 1 and wine_not: # Using Dumbledor's wine not for the first time.
        call wine_not_first 
    else:
        pass
    
    
    
    
    
    if snape_friendship >= 5 and snape_events == 0:
        call date_with_snape_01 
        
    elif snape_friendship >= 12 and snape_events == 1: #LEVEL 02
        call date_with_snape_02 
        
    elif snape_friendship >= 19 and snape_events == 2: #LEVEL 03
        call date_with_snape_03 
        
    elif snape_friendship >= 27 and snape_events == 3: #LEVEL 04
        call date_with_snape_04 
        
    elif snape_friendship >= 34 and snape_events == 4: #LEVEL 05
        call date_with_snape_05 
        
    elif snape_friendship >= 41 and snape_events == 5: #LEVEL 06. Can't proceed after this until whoring >= Lv 3.
        call date_with_snape_06 
      
    elif snape_friendship >= 48 and snape_events == 6: #LEVEL 07
        call date_with_snape_07 
         
    elif snape_friendship >= 55 and snape_events == 7: #LEVEL 08
        call date_with_snape_08 
        
    elif snape_friendship >= 62 and snape_events == 8: #LEVEL 09
        call date_with_snape_09 
        
    elif snape_friendship >= 69 and snape_events == 9: #EVENT 10
        call date_with_snape_10 
        
    elif snape_friendship >= 76 and snape_events == 10: #EVENT 10
        call date_with_snape_11 
        
    elif snape_friendship >= 83 and snape_events == 11: #EVENT 11
        call date_with_snape_12 
         
    elif snape_friendship >= 88 and snape_events == 12: #EVENT 12. If whoring level > 5.
        call date_with_snape_13 
        
    elif snape_friendship >= 93 and snape_events == 13: #EVENT 13
        call date_with_snape_14 
        
    elif snape_friendship >= 98 and snape_events == 14: #EVENT 14
        call date_with_snape_15 
        
    else:
            
        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Ты проводишь вечер с профессором Снейпом..\n>Ваши отношения с ним улучшились."
        hide screen bld1
        with d3
        
        

 
    $ snape_friendship +=1
   
    jump day_start
    
   
### SPECIAL DATE ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    sna_[2] "..........................."
    m "...............................?"
    sna_[3] "Я так сильно ее ненавижу..."
    menu:
        "\"Да! Вот сучка!\"":
            sna_[1] "Приятно знать, что мы на одной волне..."
            sna_[2] "Эта девушка..."
        "\"Кого ты ненавидишь?\"":
            sna_[1] "Почему ты спрашиваешь об этом?"
            sna_[1] "Это конечно же Гермиона!"
        "\"Неужели она такая плохая?\"":
            sna_[1] "Она хуже всех!"

    sna_[2] "Лучшая студентка..."
    sna_[3] "Ведет всевозможные внеклассные мероприятия и кружки..."
    sna_[3] "Президент учебного студенческого совета школы ..."
    sna_[3] "Скорее всего, станет девушкой года..."
    sna_[2] "................"
    sna_[3] "............"
    with hpunch
    sna_[5] "{size=+7}Я ненавижу эту чертову ведьму!!!{/size}"
    g4 "{size=-4}(Что за...?){/size}"
    sna_[2] ".............."
    sna_[2] "Раньше она меня просто раздражала, но сейчас..."
    sna_[1] "Она стала полноценной угрозой..."
    sna_[1] "Эта ведьма, теперь официально, моя самая нелюбимая ученица во всей школе..."
    m "Что насчет мальчишки Поттера?"
    sna_[6] "Мальчишка Поттер? Ха! Это еще кто?!"
    sna_[1] "Нет, я говорю серьезно..."
    sna_[1] "Я даже скажу, что Поттер и его убогий отец, вместе взятые..."
    sna_[1] "Никогда не причиняли мне столько горя, как в последнее время эта маленькая ведьма..."
    m "Ну, ну. Мы оба знаем, что это неправда..."
    sna_[2] "Да... Ты, наверное, прав..."
    sna_[7] "Этот ублюдок Джеймс Поттер действительно испортил мне жизнь--"
    sna_[6] "Подожди, откуда ты это знаешь?"
    m "Ну... Я прочитал несколько книг..."
    sna_[6] "Что? Каких книг?"
    m "Нет, не обращай внимания. Я Джинн, помнишь? Я много знаю..."
    sna_[9] "Хм... И все же тебе нужно, чтобы я научил тебя чему-нибудь..."
    m "Ну, я же тебе говорил. Моя магия действует со сбоями в твоем мире..."
    sna_[9] "Конечно, конечно..."
    m "......"
    m "Она приходила на днях..."
    sna_[10] "Кто она?"
    m "Девушка, Гермиона..."
    sna_[1] "Что?!"
    sna_[2] "Я думал, мы договорились о \"никаких контактов с людьми\" правилом."
    sna_[7] "(Хотя в последнее время мне интересно, человек она или нет...)"
    m "Я знаю... Она не оставила мне выбора, прямо вломившись ко мне..."
    sna_[1] "Думаю, она на это способна..."
    sna_[1] "Что она хотела?"
    
    if jerk_off_session:
        m "Я не уверен..."
        sna_[11] "??"
        m "Я дрочил все время, пока она говорила..."
        sna_[2] "Ты..."
        sna_[2] "... что делал?"
        m "Эй, не осуждай меня!"
        m "Ты не знаешь, каково это, сидеть взаперти в этой башне, как заключенному!"
        sna_[2] "Ты... т-ты...."
        sna_[12] "......"
        sna_[15] "Ха.... ха-ха... ХА-ХА-ХА!!!"
        m "Чт..? Что ты сказал?"
        sna_[14] "Ха-ха-ха! Ты потрясающий!"
        sna_[9] "Все Джины такие... удивительные нигилисты?"
        m "Да... Мы бессмертные, как правило, не зациклены на сексе."
        sna_[9] "Понятно..."
        sna_[10] "К сожалению, мы, простые смертные, не можем позволить себе такую роскошь..."
        
    else:
        m "Не уверен... Она много говорила..."
        m "Что-то о \"грифинду\" очках... и..."
        m "Э-э..... Честно говоря, я не обращал внимания..."
        sna_[1] "Хах... Наверное, еще куча нравоучений..."
        sna_[7] "Она знаменита именно этим..."
    

    sna_[7] "У меня завтра рано утром занятия, так что давай закончим на сегодня."
    m "Как насчет того, чтобы научить меня магии?"
    sna_[10] "Да, естественно..."
    sna_[10] "В следующий раз..."
    m "Хорошо..."
    
    

    
    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    
    jump day_start
    
#######################################################################################################################    
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Гермиона Грейнджер приходила снова..."
    sna_[1] "Не упоминай имя этой ведьмы, когда я не на работе..."
    sna_[2] "..............."
    sna_[3] "Черт возьми! Я взрослый человек, Альбус!"
    m "Меня зовут не Альб--"
    sna_[3] "Уважаемый чародей..."
    m "Ну, ладно, пусть будет так..."
    sna_[2] "Как так получилось, что одна крошечная....пизденка, способна причинить мне столько вреда?!"
    sna_[4] "Я думал, что с тобой, как своим союзником, у меня будет шанс--"
    m "Чтобы освободиться?" 
    sna_[2] "Да, примерно это слово..."
    sna_[16] "Но все, что я сделал, это дал ей больше рычагов, чтобы преследовать меня..."
    sna_[16] "Она даже настроила некоторых учителей против меня..."
    sna_[3] "................."
    sna_[7] "Она должна исчезнуть..."
    m "Что ты имеешь в виду?"
    with hpunch
    sna_[5] "{size=+6}Мне придется ее убить!{/size}"
    g4 "Буквально убить ее?"
    sna_[6] "У меня есть другой выбор?"
    m "Ты ведь шутишь, правда?"
    sna_[6] "Я?!"
    sna_[11] "Ты можешь сделать это для меня?"
    m "Э..."
    m "Как бы я \"насладился\" убийством молоденькой девушки..."
    m "Но Джины не могут убивать..."
    sna_[7] "Чепуха!"
    m "И мы осуждаем убийц..."
    if jerk_off_session:
        sna_[17] "Правда? Я думал, тебе наплевать..."
        m "В определенной степени..."
        sna_[7] "............."
    sna_[2] "Ну... не обращай на меня внимания..."
    sna_[2] "И на этот разговор..."
    sna_[2] "Я бы никогда не навредил ученику..."
    sna_[3] "(...то есть совсем)"
    m "Слушай, если она тебя так достает, почему бы просто не найти менее радикальный способ справиться с ней?"
    sna_[7] "Ну... Порка была объявлена вне закона уже довольно давно..."
    m "Это не то, что я имел ввиду..."
    sna_[1] "А?"
    m "Она лучшая ученица, верно?"
    sna_[2] "Да, будь она проклята. Девочка трудолюбивая, я так скажу."
    m "Она также имеет репутацию, всегда убежденной в своей правоте."
    sna_[6] "О да!"
    m "И она думает, что она лучше всех остальных..."
    sna_[17] "Что ты собираешься делать с этим?"
    m "Ну, кажется, что вся ее власть исходит из ее репутации..."
    sna_[11] "......................?"
    m "Что если мы заберем это у нее?"
    sna_[10] "Полагаю, это заставило бы ее притихнуть..."
    sna_[2] "Но как? Она практически святая."
    sna_[7] "Даже студенты, которые ненавидят ее, тайно восхищаются ею."
    sna_[2] "Она не провалила ни одного теста за все время пребывания здесь..."
    sna_[2] "Она всегда опережает график..."
    sna_[3] "Черт, как я ненавижу, когда она поправляет меня во время занятий..."
    sna_[6] "И благодаря ей \"Гриффиндор\" сейчас намного опережает всех остальных..."
    sna_[7] "Даже \"Слизерин\" не сравнится с ними в этом году..."
    sna_[16] "........................"
    sna_[6] "Проклятие... Мне нужно больше вина..."
    m "Вино может подождать. Выслушай меня!"
    sna_[1] "Да...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Хм... Думаю попробуем..."
    menu:
        m "..."
        "{size=-3}\"Она больше не будет лучшим студентом!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_[1] "Что? Ты имеешь в виду, несправедливо оценивать ее?"
            sna_[2] "Не... Дамблдор никогда не позволи--"
            sna_[9] "Секундочку!"
            m "Вот именно!"
            sna_[18] "Ты прав! Я могу несправедливо оценивать ее тесты! Я могу попробовать даже убедить других учителей сделать то же самое!"
            sna_[18] "Я могу им сказать, что приказ исходит от вас..."
            sna_[19] "И когда настоящий Дамблдор вернется, я притворюсь, что понятия не имел, что приказы исходили не от него..."
            m "Работал на меня."
            sna_[10] "Э..."
            sna_[10] "Это все еще ты, Джинн, верно?"
            m "Да, да, я все еще здесь..."
            sna_[18] "ОК, хорошо."  
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Гриффиндор потеряет Кубок в этом году!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            sna_[1] "Ты имеешь в виду просто начать вычитать у них очки, без весомой причины?"
            m "Не совсем, лучше найди способ накидывать очки факультету \"Слизерин\"."
            sna_[18] "О, мне это нравится!"
            sna_[20] "Есть несколько \"Слизеринких\" девушек, которые уже давно созрели для получения дополнительных очков факультету."
            sna_[19] "О, это будет великолепно!"
            sna_[18] "Ты действительно гений!"
            m "Да, я гениальный Джинн. Каковы шансы, что... (прим. игра слов : genius genie)"
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Разрушим ее репутацию!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            sna_[1] "Запятнаем ее репутацию?"
            sna_[1] "Но девочка неподкупна..."
            m "Ерунда!"
            m "Все, что мы должны сделать - убедить ее, что она должна принести некоторые жертвы \"для общего блага\"."
            sna_[9] "О, ну конечно..."
            sna_[21] "Она с удовольствием \"Испачкает руки\", чтобы спасти честь своего драгоценного факультета\"Гриффиндор\"!"
            sna_[9] "И когда она это сделает, у нас будет необходимый рычаг..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_[9] "Это действительно может сработать!"
    m "Я тоже так думаю."
    sna_[19] "О, я почувствовал в себе прилив жизненных сил!"
    sna_[15] "Налей мне еще один бокал!"
    sna_[19] "Завтра занятия \"Защиты от темных искусств\" начнутся поздно!"
    m "....."
    m "Тебе не кажется, что это слишком жестоко?"
    m "Я имею в виду, она же просто девушка..."
    sna_[8] "Просто девушка?"
    sna_[8] "О нет, нет, нет..."
    sna_[4] "Она-воплощение чистого зла!"
    sna_[2] "Если мы не сделаем это сейчас..."
    sna_[3] "В один из прекрасных дней я кину на нее \"Avada Kedavra\" заклинание!"
    m "Что ты сделаешь?"
    sna_[4] "Убью ее по-настоящему!"
    m "Хорошо, хорошо ... понял."
    m "Тогда выберем меньшее из двух зол."
    sna_[7] "Да..."
    sna_[6] "Теперь налей мне еще немного вина."

    ">Вы проводите остаток вечера в компании Снейпа, запивая свои проблемы."
    
    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.   
    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)
   

    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start
   
   
#######################################################################################################################    
label special_date_with_snape_03: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5

    sna_[2] "Так..."
    sna_[7] "Ты заставил девушку раздеться для тебя..."
    sna_[3] "И ты даже не пригласил меня?!"
    m "Ну..."
    m "Я не думаю, что девушка была готова--"
    sna_[12] "Эти обнаженные груди идеальной формы..."
    sna_[13] "Эти великолепные стройные ножки..." 
    sna_[12] "Ее пышный и нежный зад..." 
    sna_[13] "Я уже все повидал..."
    sna_[20] "Я уже все это повидал!"
    m "(...)"
    sna_[16] "Сколько же проблем. Я думаю, что девушка..."
    sna_[5] "{size=+7}Я могу таращится на ее сиськи весь день!!!{/size}"
    m "..."
    sna_[7] "Ты должен пригласить меня в следующий раз, мой друг!"
    sna_[8] "Моя жизнь зависит от этого!"

    menu:
        m "..."
        "-Конечно, почему бы и нет-":
            pass
        "-Гм-":
            pass

    sna_[19] "Прекрасно!"
    sna_[9] "Я с нетерпением жду, что скажу!"
    sna_[21] "Как ты думаешь, она позволит мне коснуться их ...?"

    ">Вы проводите остаток вечера в компании Снейпа, болтающего об обнаженной груди Гермионы."

    $ snape_invated_to_watch = True

    hide screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes

    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start
    
   
   
    
####Snape bonus###
#label snape_bonus:
#    if snape_events == 1:
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=3
#            "Slytherin got +3 points as a Snape-Bonus."
    
#    if snape_events == 2:#WEEK No.2
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=7
#            "Slytherin got +7 points as a Snape-Bonus."
    
#    if snape_events == 3:#WEEK No.3
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=10
#            "Slytherin got +10 points as a Snape-Bonus."
            
#    if snape_events == 4:#WEEK No.4
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=12
#            "Slytherin got +12 points as a Snape-Bonus."
            
#    if snape_events == 5:#WEEK No.5
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=16
#            "Slytherin got +16 points as a Snape-Bonus."
            
#    if snape_events == 6:#WEEK No.6
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=22
#            "Slytherin got +22 points as a Snape-Bonus."
            
#    if snape_events == 7:#WEEK No.7
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=26
#            "Slytherin got +26 points as a Snape-Bonus."
            
#    if snape_events == 8:#WEEK No.8
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=32
#            "Slytherin got +32 points as a Snape-Bonus."
            
#    if snape_events == 9:#WEEK No.9
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=36
#            "Slytherin got +36 points as a Snape-Bonus."
            
#    if snape_events == 10:#WEEK No.10
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=43
#            "Slytherin got +43 points as a Snape-Bonus."
            
#    if snape_events == 11:#WEEK No.11
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=46
#            "Slytherin got +46 points as a Snape-Bonus."
            
#    if snape_events == 12:#WEEK No.12
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=50
#            "Slytherin got +50 points as a Snape-Bonus."
            
#    if snape_events == 13:#WEEK No.13
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=56
#            "Slytherin got +56 points as a Snape-Bonus."
            
#    if snape_events == 14:#WEEK No.14
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=61
#            "Slytherin got +61 points as a Snape-Bonus."
            
#    if snape_events == 15:#WEEK No.15
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=66
#            "Slytherin got +66 points as a Snape-Bonus."

#return




####################################
label wine_first:
    m "Посмотри, что у меня есть!"
    call sna_head("Хм? ...","snape_05") 
    call sna_head("Дай-ка подумать...") 
    pause.1
    $ the_gift = "images/store/27.png" # WINE.
    show screen gift
    with d3
    ">Ты передаешь бутылку профессору Снейпу, которую нашел в шкафу..." 
    hide screen gift
    with d3
    $ wine -= 1
    
    
    call sna_head("Она должна быть из личных запасов Альбуса!","snape_24") 
    call sna_head("Дорогая и невероятно редкая вещь.","snape_06") 
    m "И мы будем его пить?"
    call sna_head("Мы непременно будем!","snape_02") 
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Ваши отношения с профессором Снейпом улучшились."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return


label wine_not_first:
    m "Посмотри, что у меня есть!"
    hide screen s_head2    
    pause.1
    $ the_gift = "images/store/27.png" # WINE.
    show screen gift
    with d3
    ">Ты показываешь бутылочку Снейпу, которую нашел в шкафу..." 
    hide screen gift
    with d3
    $ wine -= 1

    call sna_head("Еще одна?","snape_05") 
    if one_of_ten == 1:
        call sna_head("Великолепно!","snape_02") 
    elif one_of_ten == 2:
        call sna_head("Хорошо!","snape_02") 
    elif one_of_ten == 3:
        call sna_head("Потрясающие!","snape_02") 
    elif one_of_ten == 4:
        call sna_head("Отлично, дружище!","snape_02") 
    elif one_of_ten == 5:
        call sna_head("Ты нашел тайник Альбуса или это был его личный винный погреб?","snape_05") 
    elif one_of_ten == 6:
        call sna_head("В последнее время мне уже трудно пить чего-то иное, кроме этого вина!","snape_02") 
    elif one_of_ten == 7:
        call sna_head("Отлично! Я уже чувствую себя более раслабленным!","snape_02") 
    elif one_of_ten == 8:
        call sna_head("Становится все лучше и лучше!","snape_02") 
    elif one_of_ten == 9:
        call sna_head("Серьезно, и насколько велик там тайник?","snape_05") 
    elif one_of_ten == 2:
        call sna_head("Это, очень хорошо, чтобы быть правдой! Давай расспробуем этого ублюдка!","snape_02") 
    
    call bld 
    call give_reward(">Ваши отношения с профессором Снейпом улучшились.","images/store/01.png") 
    #">Your relationship with Professor Snape has improved."

    if game_difficulty < 2:      #Easy difficulty
        $ snape_friendship +=3
    else:                        #Normal and hard difficulty
        $ snape_friendship +=2

    return
    
    
  ########
label not_today:
    if one_out_of_three == 1:
        sna "Прости, я не могу сегодня вечером..."
    elif one_out_of_three == 2:
        sna "Извини, у меня есть другие дела на сегодня..."
    elif one_out_of_three == 3:
        sna "Извини, у меня другие планы. Может в другой раз?"
    
    jump snape_ready
        
        
         
    
    
    