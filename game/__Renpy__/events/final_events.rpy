
#hermione asks genie about who will be in-charge of the ball
label want_to_rule:
    
    $ event_chairman_happened = True #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    
    call hg_event_EnterRoom_block #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    
    #her "Professor Dumbledore?"
    call her_main("[genie_name]?","soft","base",xpos="right",ypos="base") 
    m "Мисс Грейнджер, чем я могу помочь?"
    call her_main("Сэр, вы уже приняли решение, кто будет руководить \"ОКОБ\" в этом году?","open","base") 
    m "\"ОКОБ\"?"
    call her_main("\"Организационным Комитетом Осеннего Бала\", сэр...","open","closed") 
    m "Эм... Конечно..."
    call her_main("Прошу прощения, если я слишком прямо говорю об этом, сэр...","normal","frown") 
    call her_main("Но я думаю, вы должны поставить меня главной.","open","angryCl") 
    her "Я делала его в прошлом году, и это был лучший \"Осенний бал\" организованный в Хогвартсе за много лет."
    call her_main("Вы сами так сказали, сэр. Помните?","normal","base") 
    m "Да, конечно..."
    call her_main("Значит, это да?","base","base") 
    her "Значит ли это, что в этом году я снова буду руководить?"

    menu:
        m "..."
        "\"Вы будете за главную, мисс Грейнджер.\"":
            jump one_thing

        "\"Нет. Думаю профессор Снейп будет руководить!\"":
            call her_main("Профессор Снейп, сэр?","normal","frown") 
            her "Но традиционно за организацию и проведение бала несут ответственность студенты..."
            her "Учителя присутствуют только в качестве почетных гостей..."
            m "Ну конечно... Я просто пошутил."
            m "Ты будешь главной, [hermione_name]..."
            label one_thing:
                call her_main("Спасибо, [genie_name].","base","base") 
            m "Но есть одно условие..."
            call her_main("Условие, [genie_name]?","normal","frown") 
            
            $ d_flag_04 = False
            label no_sleeping_with_professor:
                pass
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            menu:  
                m "..."
                "\"Сперва покажи мне свои сиськи.\"":
                    $ mad += 9
                    $ d_flag_01 = True
                    pass
                "\"Сперва покажи мне свою киску.\"":
                    $ mad += 9
                    $ d_flag_02 = True
                    pass
                "\"Сперва разденься для меня.\"":
                    $ mad += 17
                    $ d_flag_03 = True
                    pass
                "\"Тебе придется переспать со мной.\"" if not d_flag_04:
                    $ mad += 17
                    $ d_flag_04 = True
                    call her_main("Мне придется... переспать...?","angry","wide") 
                    call her_main("...................","angry","angry",cheeks="blush") 
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    her "Я не глупа, сэр... Как раз совсем наоборот."
                    her "И я прекрасно понимаю, что характер услуг, которые я в последнее время вам оказываю..."
                    her "...Возможно, это заставило вас поверить, что я готова..."
                    her "...В конце концов, позволить вам поиметь меня, сэр..."
                    m "Что-о-о...? Я бы никог--"
                    call her_main("Пожалуйста сэр, дайте мне закончить.","scream","angry",emote="01") 
                    m "Ладно..."
                    call her_main("Сэр, я знаю, что вы довольно мудры.","angry","angry") 
                    call her_main("Так, что, пожалуйста, поймите...","disgust","glance") 
                    her "Я могу пожертвовать своей гордостью и даже достоинством ради своего факультета..."
                    her "Но спать со своим директором?"
                    call her_main("Сэр, это для меня черта недопустимого.","angry","angry",cheeks="blush") 
                    m "Получи должность. Давай просто забудем, последние несколько минут и о том, что я говорил."
                    call her_main("{size=-5}(Мне бы тоже, очень этого хотелось...){/size}","angry","suspicious",cheeks="blush") 
                    jump no_sleeping_with_professor 
       
                "\"Так и быть. Должность твоя.\"":
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    call blkfade 
                    pass
    

            if d_flag_01 or d_flag_02 or d_flag_03:
                call her_main("Что?!","open","base") 
                m "Что?"
                #her "Professor!"
                call her_main("[genie_name]!","angry","angry") 
                m "Что?"
                call her_main("Вы злоупотребляете своей властью, сэр. Снова!","disgust","glance") 
                m "Серьезно? После всех тех услуг, которые ты мне обменяла?"
                call her_main("Это было ради блага моего факультета, сэр.","annoyed","annoyed") 
                m "Ну, а это ради \"Осеннего променада\"."
                call her_main("Это \"осенний бал\", сэр...","upset","closed") 
                m "Ну, давай..."
                m "Доверить это кому-то другому было бы преступлением, ты же знаешь."
                call her_main("..........","annoyed","angryL") 
                m "Тебя совсем не волнуют твои одноклассники?"
                call her_main("Что?","open","base") 
                m "Хоть раз отложить в сторону свой эгоизм, трудно?"
                call her_main("Мой... эгоизм?","annoyed","worriedL") 
                m "Ваши одноклассники заслуживают лучшего организатора балов!"
                m "И только {size=+5}ТЫ{/size} лучший организатор!"
                call her_main("...на самом деле это правда.","angry","down_raised") 
                m "Приятный вечер многих людей зависит от тебя, девочка!"

                if d_flag_01:
                    m "Так что, я предлагаю тебе перестать быть эгоисткой и показать мне свои сиськи!"
                elif d_flag_02:
                    m "Так что, я предлагаю тебе перестать быть эгоисткой и показать мне свою киску!"
                elif d_flag_03:
                    m "Так что, я предлагаю тебе перестать быть эгоисткой и раздеться для меня!"

                #her "You are completely right, professor!"
                call her_main("Вы совершенно правы, [genie_name]!","open","down") 
                call her_main("Я должна это сделать. Все зависят от меня.","upset","closed") 
                call her_main("Просто дайте мне секундочку, пожалуйста...","base","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d5   
                m "............"

                if d_flag_01: # SHOW ME TITS
                    call play_music("playful_tension") # SEX THEME.
                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    pause.3
                    call her_chibi("lift_top","mid","base") 
                    with fade
                    pause.8
                    
                    $ hermione_wear_bra = False
                    call h_action("lift_top") 
                    pause.5
                    
                    show screen blktone
                    call her_main("","annoyed","base") 
                    call ctc 

                    m "Очень хорошо, мисс Грейнджер..."
                    m "Твоя пышная грудь, всегда желанное зрелище..."
                    call her_main("....................","disgust","down_raised") 
                    call ctc 

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade 
                    call reset_hermione_main 

                elif d_flag_02: # SHOW ME PUSSY
                    call play_music("playful_tension") # SEX THEME.
                    
                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    call ctc 

                    $ hermione_wear_panties = False
                    call her_chibi("lift_skirt","mid","base") 
                    with fade
                    call ctc 
            
                    call h_action("lift_skirt") 
                    pause.5
                    
                    show screen blktone
                    call her_main("","annoyed","base") 
                    call ctc 
                    
                    call her_main("","base","worriedCl") 
                    call ctc 
                    
                    her ".............................."
                    with hpunch
                    g4 "Что ты делаешь, девочка?!"
                    g4 "Я твой школьный директор! Как тебе не стыдно?!"
                    call her_main("Что?! Но--","angry","angry",cheeks="blush") 
                    g9 "Хи-хи... Расслабься, девочка. Я просто прикалываюсь."
                    call her_main("[genie_name], Это было очень подло.","scream","angryCl") 
                    g9 "Хи-хи..."
                    call her_main(".....................................","annoyed","angry") 
                    m "Мне нравится твоя выбритая маленькая киска..."
                    call her_main(".....спасибо, сэр.","annoyed","angry") 
                    call ctc 

                    hide screen hermione_main   
                    hide screen blktone   
                    call blkfade 

                    call reset_hermione_main 
                
                elif d_flag_03: # STRIP NAKED
                    call play_music("playful_tension") # SEX THEME.

                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    
                    
                    #Walks to the door
                    call her_walk("mid","door",2) 
                    
                    #Locks the door
                    pause.5
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    call her_chibi("stand","door","base") 
                    pause.5
                    
                    #Returns from the door
                    m "??!"
                    call her_walk("door","mid",3) 
                    pause.2
                    show screen bld1
                    with d3
                    
                    call her_main("На всякий случай...","annoyed","angryL") 
                    call ctc 
                    m ".........................."

                    show screen blktone
                    call nar(">Гермиона раздевается...") 
                    pause.2
                    
                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top") 
                    pause.5
                
                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update") 
                    pause.5

                    call nar(">Одна вещь за другой...") 

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt") 
                    pause.5
                
                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update") 
                    pause.5

                    call nar(">Жилет, рубашка, юбка, и, наконец,...") 
                    
                    $ hermione_wear_panties = False
                    call set_hermione_action("covering") 
                    pause.5

                    call nar(">Трусики.") 
                    call ctc 
                    
                    g9 "Ми-и-и-ло!"
                    call her_main("","soft","squintL") 
                    call ctc 
                    her "*Хнык!*"
                    m "А?"
                    
                    $ display_h_tears = True
                    $ u_tears_pic = "characters/hermione/face/tears_01.png"
                    
                    call her_main("О, пожалуйста, не смотрите на меня так пристально, сэр.","open","baseL",) 
                    call her_main("Просто наслаждайтесь... {w}... {w}видом...","soft","squintL") 
                    m "Ты... плачешь?"
                    call her_main("*Хнык!* Нет, не совсем, сэр... *хнык!*...","angry","worriedCl") 
                    her "Просто я стою перед директором абсолютно голая... *ХНЫК!*"
                    call her_main("Это слезы стыда, сэр.","shock","angryL",tears="messy") 
                    her "Ничего не могу с этим поделать! *Хнык!*"
                    m "Ты уверена, что все в порядке?"
                    call her_main("Да, да, сэр, пожалуйста.... *Хнык!*","soft","angry",tears="messy") 
                    call her_main("Прошу смотрите, на мое нагое тело... *Хнык!*","shock","wide",tears="messy") 
                    
                    call her_main("","angry","angry",cheeks="blush",tears="messy") 
                    call set_hermione_action("lift_breasts") 
                    pause.2
                    
                    g4 "(Что...?)"
                    call her_main("Сэр, я прошу вас!","angry","angry",cheeks="blush",tears="messy") 
                    m "Звучит как приказ--"       
                    call her_main("Мне это нужно!","angry","dead_mad",cheeks="blush",tears="messy") 
                    her "...Мне нужно бесстыдно показывать вам свое обнаженное тело!"
                    m ".............?"
                    call her_main("Мне нужно почувствовать это смущение и унижение! *ХНЫК!*","upset","dead_mad",cheeks="blush",tears="messy") 
                    call her_main("Судьба \"Осеннего бала\" зависит от этого...","grin","ahegao_mad",cheeks="blush",tears="messy") 
                    her "Поэтому, сэр, пожалуйста..."
                    call her_main("Продолжайте смотреть на мою обнаженную грудь и писечку...","grin","angry",cheeks="blush",tears="messy") 
                    call ctc 

                    call her_main("Да! Заставьте мою кожу покраснеть от позора, сэр... *Хнык!*","open","ahegao_raised",cheeks="blush",tears="messy") 
                    m "Эмм... Да... Хорошо..."
                    m "Слушай, думаю, этого хватит..."
                    call set_hermione_action("pinch") 
                    call her_main("Вы уверены, сэр?","angry","angry",cheeks="blush",tears="messy") 
                    her "Вы уверены, что достаточно меня унизили, сэр?"
                    m "...................."
                    m "(Она от этого получает удовольствие? Она язвит? Я ничего не понимаю...)"
                    her ".........................."
                    call ctc 

                    m "Просто оденься обратно, мисс Грейнджер. Ты заставляешь меня чувствовать неловкость."
                    call her_main("Как пожелаете, сэр...","annoyed","angryL",tears="messy") 
                    
                    call ctc 
                    
                    hide screen hermione_main  
                    hide screen blktone
                    call blkfade 

                    $  u_tears_pic = "characters/hermione/face/tears_03.png"

                    call reset_hermione_main 

                
                    
                    
                    
    call play_music("chipper_doodle") # HERMIONE'S THEME.             
                    
    call her_chibi("stand","mid","base") 
    call hide_blkfade 
    call ctc 

    show screen bld1
    call her_main("Так, как? Я теперь официально в этом году возглавляю \"Комитет Организации Осеннего Бала\"?","base","happyCl",xpos="right",ypos="base") 
    m "Так и есть."
    her "Спасибо, сэр! Вы не пожалеете об этом, я обещаю!"
    m "{size=-4}(С чего бы мне?){/size}"
    m "{size=-4}(Меня все это совершенно не волнует...){/size}"
    call her_main("Я лучше прямо сейчас побегу. Мне нужно столько всего сделать!","grin","baseL") 
    m "Безусловно, мисс Грейнджер. Хорошего дня."
    hide screen hermione_main
    hide screen bld1
    with d3 
    pause.2
    
    call her_walk("mid","leave",2) 

    pause.5
    call bld 
    m "........................................"
    m "Бал, да?"
    m "Интересно, придется ли мне на нем появиться..."
    hide screen bld1
    with d3

    $ hermione_takes_classes = True
    $ days_without_an_event = 0

    $ display_h_tears = False
    
    call music_block 
    
    return
    
#==========================

#Snape confronts genie about his ABOC decision

label against_the_rule:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    $ snape_against_chairman_hap = True # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ days_without_an_event = 0
    
    call play_sound("door") #Sound of a door opening.
    call sna_walk("door","mid",3) 
    pause.2

    show screen bld1
    call sna_main("Ты что, совсем рехнулся?!","snape_01",xpos="base",ypos="base") 
    m "Знаешь, иногда мне кажется, что это возможно..."
 
    call sna_main("Ты назначил ее главной в \"Комитет Организации Осеннего Бала\"?!!","snape_01") 
    m "Полагаю, это плохо?"
    call sna_main("Плохо?{w} {size=+5}ПЛОХО?!{/size}","snape_10") 
    call sna_main("{size=+5}Это катастрофа!{/size}","snape_15") 
    call sna_main("Прошлогодний бал был просто ужасен!","snape_16") 
    m "Разве? Я слышал другое..."
    call sna_main("Неужели? И кто тебе это сказал?","snape_10") 
    m "Очевидно, не очень надежный источник..."
    call sna_main("Проклятье... Проклятье, все к черту...","snape_08") 
    call sna_main("У меня большие планы на...","snape_07") 
    m "Правда? Например?"
    call sna_main("О, теперь это не имеет значения...","snape_06") 
    #sna "The girl is a complete control freak..."
    sna "Теперь она будет использовать префектов или призраков, чтобы следить за мной на протяжении всей подготовки..."
    m "Точно, это напомнило мне..."
    m "Я тоже должен появиться?"
    call sna_main("Появиться?","snape_03") 
    sna "Ожидается, что ты проведешь это мероприятие!"
    call sna_main("Но не стоит беспокоиться! Я что-нибудь придумаю!","snape_09") 
    call sna_main("Хм... Может, вероятно, мне придется провести этот бал...","snape_06") 
    m "............"
    call sna_main("Ну, Осенний бал вот-вот произойдет и Гермиона Грейнджер за главную...","snape_09") 
    sna "Теперь, ничего не изменить..."
    call sna_main("Прости за вспышку гнева...","snape_05") 
    call sna_main("Эта девушка проявляет во мне столько негатива...","snape_16") 
    m "Не парься..."
    call sna_main("Знаешь, что...?","snape_06") 
    sna "Мне не хочется сегодня работать..."
    call sna_main("У нас еще осталось вино Дамблдора?","snape_05") 
    m "Думаю, да..."
    call sna_main("Отлично! Налей мне немного...","snape_02") 
    m "Серьезно? Ты просто так бросишь свои уроки?"
    call sna_main("Да, велика новость - Я ненавижу свою работу.","snape_03") 
    sna "И так как ты, мой начальник..."
    call sna_main("Я даже не знаю, почему я утруждаю себя обучением этих так называемых студентов...","snape_06") 
    m "Поддержать шараду?"
    m "По той же самой причине, почему я никогда не покидаю эту башню...?"
    call sna_main("Верно...","snape_05") 
    sna "Но знаешь, что еще может поставить под угрозу наше маленькое предприятие?"
    call sna_main("Как я потеряю самообладание над собой и во время занятий, задушу парочку \"Гриффиндорских\" пустозвонов голыми руками...","snape_07") 
    m "Хм... Я понимаю, к чему ты клонишь..."
    call sna_main("Серьезно, чувак... Мне нужно выпить...","snape_06") 

    hide screen snape_main
    call blkfade 
    
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk
    
    $ fire_in_fireplace = True
    call sna_chibi("hide") 
    hide screen bld1
    call hide_blkfade 
    
    call bld 
    call nar("Профессор Снейп проводит целый день в твоем кабинете, снимая алкоголем стресс.") 
    
    if not sfmax:# Turns TRUE when friendship with Snape been maxed out.
        call nar(">Ваши отношения с ним улучшились.") 
        $ snape_friendship +=1
   
    call blkfade 
    
    hide screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    hide screen fireplace_fire
    show screen genie
    show screen chair_right
    show screen desk
    hide screen desk
    
    hide screen bld1

    stop bg_sounds #Stops playing the fire SFX.
   
    jump night_start
         
    
#============================

label crying_about_dress:
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    call hg_event_EnterRoom_block #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    
    call her_main("Мои родители прислали мне не то платье!","angry","base",tears="soft",xpos="right",ypos="base") 
    m "Ты шутишь?!"
    call her_main("Они прислали мне платье, которое я надевала на бал в прошлом году...","angry","base",tears="soft") 
    m "Какие неосмотрительные ублюдки!"
    call her_main("Вы смеетесь надо мной, сэр?","mad","worried",tears="soft") 
    m "Ты будешь винить меня за это?"
    call her_main("Я стану посмешищем Хогвартса! *Хнык!*","clench","worried",cheeks="blush",tears="soft") 
    call her_main("Моя Репутация почти разрушена! *Хнык!*","angry","dead",cheeks="blush",tears="crying") 
    m "Серьезно? После всех услугах, что ты мне оказала, ты заботишься о таких вещах?"
    call her_main("Сэр, надеть одно и то же платье, два года подряд на \"Осенний Бал\" было бы унизительнее, чем любая услуга, которую я вам продала.","shock","down_raised",cheeks="blush",tears="crying") 
    with hpunch
    g4 "Должно быть, ты шутишь..."
    call her_main("О, вам этого не понять...","angry","suspicious",cheeks="blush",tears="messy") 
    call her_main("Вы такой же как мой отец!","scream","angry",cheeks="blush",tears="messy") 
    m "Непонял."
    call her_main("Я имею в виду... Эм...","open","surprised",cheeks="blush",tears="messy") 
    her "Простите меня, сэр..."
    call her_main("Не знаю, зачем я вам все это рассказываю...","shock","down_raised",cheeks="blush",tears="crying") 
    m "................"
    call her_main("......................*хнык!*","angry","dead",cheeks="blush",tears="crying") 
    call her_main("Думаю, мне лучше сейчас уйти...*хнык*","angry","suspicious",cheeks="blush",tears="messy") 
    m "Не смею тебя, более задерживать, мисс Грейнджер...."
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3
    
    call her_walk("mid","door",2) 
    pause.3 

    show screen bld1
    call her_head("(Моя жизнь полностью разрушена...)","angry","suspicious",cheeks="blush",tears="messy",xpos="base",ypos="base") 
    pause.1
    call her_chibi("leave","door","base") 
 
    m "Хм... Я не помню, чтобы я ее видел в таком отчаянии..."
    m "И это говорит о многом, учитывая все обстоятельства..."
    m "Я полагаю, блядовать за очки факультету, значительно меньшая проблема, чем отсутствие надлежащего выпускного платья..."
    m ".............."
    m "Школьницы..."
       
    hide screen bld1
    with d3
    
    $ hermione_takes_classes = True
    
    call music_block 
    
    return 
    
#===========================

label sorry_about_hesterics:
    $ sorry_for_hesterics = True # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    $ days_without_an_event = 0
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    call hg_event_EnterRoom_block #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    
    m "Мисс Грейнджер?"
    call her_main("Извините за беспокойство, сэр...","open","worried",xpos="right",ypos="base") 
    call her_main("Я пришла извиниться за свое...","open","worriedL") 
    her "...мою вчерашнюю истерику."
    m "Конечно, не беспокойся об этом."
    call her_main("Благодарю вас, сэр.","open","base") 
    call her_main("Тем не менее, я ничего не могу поделать, но чувствую себя ужасно, за свою вчерашнюю истерику...","open","angryCl") 
    m "Значит, вопрос решен?"
    call her_main("Не совсем...","open","worried") 
    call her_main("Вообще-то, совсем нет...","annoyed","angryL") 
    m "Хм..?"
    call her_main("Но это не имеет никакого значения...","annoyed","down") 
    her "Я просто слишком остро реагирую..."
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("Я не буду присутствовать на балу в этом году... ну и что?","annoyed","down") 
    call her_main("Я потратила бесчисленные часы на организацию мероприятия...","normal","worriedCl") 
    call her_main("Я так усердно работала... и...","open","worried",tears="soft") 
    call her_main("А сейчас я даже не смогу пойти... на... *Хнык!*","shock","baseL",cheeks="blush",tears="soft") 
    call her_main("На... *ХНЫК!*","shock","down_raised",cheeks="blush",tears="crying") 
    call her_main("Простите, сэр!","angry","suspicious",cheeks="blush",tears="messy") 
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    hide screen no_groping_02
    hide screen bld1
    show screen genie
    with d1
    
    call her_walk("mid","leave",2,action="run") 
    pause.5
    
    call bld 
    m "......................................."
    m "Hm..."

    $ hermione_takes_classes = True

    hide screen bld1
    with d3
    
    call music_block 
    
    return
    
    
#=========================

label giving_the_dress:
    hide screen wardrobe_gifts
    "Уверены, что хотите начать это событие?"

    menu: 
        "Да!":
            jump giving_thre_dress
        "Нет.":
            pass

    call screen wardrobe_gifts

label giving_thre_dress:
    $ gave_the_dress = True #Turns True when Hermione has the dress.
    $ days_without_an_event = 0

    hide screen hermione_main
    with d5
    
    $ mad = 0
    stop music fadeout 1.0
    m "Здесь... Это для тебя..."
    $ the_gift = "images/store/01.png" # DRESS.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Ты отдаешь бальное платье Гермионе..."
    hide screen gift
    with d3
    call her_main("Хм...? Что там?","base","base") 
    call her_main("{size=+7}ПЛАТЬЕ?!{/size}","angry","wide") 
    with hpunch
    m "Я думал, что ты--"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]!","angry","base",tears="soft") 
    g4 "Что? Что случилось? Не говори мне, что это не тот цвет, фасон или что-то подобное!"
    call her_main("Оно восхитительно, сэр... *хнык!*","angry","base",tears="soft") 
    her "Оно прекрасно... *хнык!* ...Мне очень нравится."
    m "Оно точно не похоже на прошлогоднее..?"
    her "Я прошу прощения, сэр... *Хнык!*"
    call her_main("Я... Я просто...","clench","worried",cheeks="blush",tears="soft") 
    call her_main("Я так счастлива...","shock","down_raised",cheeks="blush",tears="crying") 
    her "Спасибо, сэр. Огромное спасибо."
    call her_main("Я не могу поверить, что вы сделали что-то подобное для меня...","angry","suspicious",cheeks="blush",tears="messy") 
    m "Так и есть. А теперь перестань плакать."
    call her_main("Я не могу, сэр. Я так счастлива и так благодарна...","scream","worriedCl",cheeks="blush",tears="messy") 
    call her_main("Хотите, чтобы я отсосала у вас, сэр?","open","surprised",cheeks="blush",tears="messy") 
    m "Что?"
    call her_main("Поскольку я намереваюсь это сделать!","open","surprised",cheeks="blush",tears="messy") 
    her "А я буду глотать и все такое!"
    call her_main("И вам не придется платить мне ни одного очка!","shock","down_raised",cheeks="blush",tears="crying") 
    m "Хм... Может, как-нибудь в другой раз..."
    m "Это не тот плач, который я нахожу возбуждающим..."
    call her_main("Я сожалею, сэр. Я такая неряха...","angry","suspicious",cheeks="blush",tears="messy") 
    call her_main("Но это так неожиданно...","shock","down_raised",cheeks="blush",tears="crying") 
    her "Вы сделали меня такой счастливой, сэр... *хнык!*"
    call her_main("Спасибо, сэр! *ХНЫК!* Спасибо вам! *ХНЫК!*","angry","suspicious",cheeks="blush",tears="messy") 
    m "Ну... э... там, там..."
    m "Лучше перестань плакать, пока ты слезами не испачкала свое новое платье..."
    call her_main("Мое новое платье! *ХНЫК!*","scream","worriedCl",cheeks="blush",tears="messy") 
    m "Хорошо, знаешь что? Просто убирайся из моего кабинета."
    m "Просто забирай платье и уходи."
    call her_main("Конечно... Извините, сэр!","angry","suspicious",cheeks="blush",tears="messy") 
    hide screen hermione_main  
    hide screen bld1                                                                                                                                                                               #HERMIONE
    with d3          
    pause.1
    
    call her_chibi("stand","mid","base") 
    pause.3
    call her_chibi("stand","mid","base",flip="True") 
    pause.2
    
    call her_walk("mid","leave",2) 
    
    call bld 
    m "......................"
    m "Женщины..."
    hide screen bld1
    with d3

    call music_block 
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
    
    
    
###======================================================================
    
    
label good_bye_snape:

    $ days_without_an_event = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    call play_sound("door") #Sound of a door opening.
    call sna_walk("door","desk",2.5) 
    pause 1.5

    show screen bld1
    call sna_main("Джинн...","snape_01",xpos="base",ypos="base") 
    m "Северус?"
    call sna_main("Думаю, у меня есть догадка, почему твоя магия не работает так, как должна...","snape_05") 
    g4 "Серьезно?!"
    call sna_main("Да...","snape_23") 
    sna "Это довольно очевидно на самом деле... Я удивлен, что раньше это не приходило мне в голову."
    call sna_main("Видишь ли, дело в том, что каждое здание \"Хогвартса\" заколдовано всеми видами защитных заклинаний...","snape_24") 
    m "Защитные заклинания, да?"
    call sna_main("Да...","snape_23") 
    sna "Очень мощная, старая и мерзкая магия..."
    call sna_main("Даже сама земля сильно зачарована на километры во всех направлениях...","snape_24") 
    m "Hm..."
    call sna_main("В принципе, здесь любое заклинание может мешать твоим способностям...","snape_25") 
    m "Подожди, тогда почему у тебя нет проблем с заклинаниями?"
    call sna_main("Моя магия \"Хогвартская\", местная...","snape_05") 
    sna "Но держу пари, твои силы достаточно сильны, чтобы восприниматься как угроза."
    m "Интересно..."
    call sna_main("Я думаю, если отдалиться достаточно далеко от территории школы...","snape_24") 
    m "Я смогу вернуться домой... наконец..."
    call sna_main("Да, и лучшее время для этого-сегодня вечером...","snape_02") 
    call sna_main("В то время как все озабочены этим чертовым \"Осенним балом\" ты можешь улизнуть незамеченным...","snape_23") 
    
    ### SHAKE HANDS WITH SNAPE ###
    hide screen snape_main
    call blkfade 
    
    hide screen genie
    hide screen bld1
    call sna_chibi("hide") 
    show screen chair_left
    show screen g_c_u
    $ genie_chibi_xpos = 220
    $ genie_chibi_ypos = 205
    $ g_c_u_pic = "images/main_room/hand_00.png"
    play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 # EPIC THEME.
    pause 1
    
    m "Правильно, сегодня вечером, всю ночь будет идти \"Осенний бал\"..."
    m "Значит, сегодня все и закончится..."
    call sna_head("Похоже на то...","snape_09") 
    call hide_blkfade 
    pause.5

    call sna_head("На случай, если я прав и больше никогда тебя не увижу...","snape_05") 
    m "Верно..."
    call blkfade 

    $ g_c_u_pic = "images/main_room/hand_01.png"
    call hide_blkfade 
    pause 2

    call bld 
    call sna_head("Последние несколько месяцев были самыми лучшими месяцами в моей жизни, Джини...","snape_26") 
    call sna_head("И спасибо тебе за это, невероятный путешественник из другого мира...") 
    call sna_head("Благодарю тебя, мой друг...") 
    m "Я не знаю, что сказать, Северус..."
    call sna_head("Тогда ничего не говори...","snape_06") 
    call sna_head("Просто переходи к следующему приключению...- прим. обдолбаный @ ©Акабур™ продолжений не пилит") 
    call sna_head("Наш мир задержал тебя достаточно, долго...") 
    m "Спасибо, что составил мне компанию и был моим единственным другом, Северус."
    call sna_head("Спасибо, что был моим...","snape_27") #TEARS?
    call sna_head("Я лучше прямо сейчас пойду...","snape_06") 
    #Goes to the door, stops and turns around.
    
    hide screen s_head2
    call blkfade 

    hide screen chair_left
    hide screen g_c_u
    show screen genie
    pause.5

    call sna_chibi("stand","desk","base") 
    hide screen bld1
    call hide_blkfade 
    pause.5
    
    call sna_walk("desk","door",3) 
    pause.5

    call sna_chibi("stand","door","base") 
    pause.5

    call bld 
    call sna_head("Но есть еще кое-что...","snape_01") 
    m "Да?"
    call sna_head("Если все пройдет хорошо...","snape_24") 
    call sna_head("Завтра я найду настоящего Альбуса Дамблдора в этом кресле?") 
    m "Я так думаю..."
    call sna_head("Хм...","snape_04") 
    call sna_head("Альбус не должен знать, что я знал о его отсутствии...","snape_03") 
    call sna_head("Есть ли способ отличить вас друг от друга?","snape_01") 
    m ".............."
    m "Как насчет секретного пароля?"
    call sna_head("Пароль?","snape_05") 
    m "Да... просто спроси меня завтра: \"Кто рулит?\"."
    call sna_head("\"Кто рулит?\"","snape_01") 
    g9 "\"Akabur рулит!\""
    call sna_head("Akuba... гм... Что это означает?","snape_05") 
    m "Просто фраза, которую ты сможешь услышать только от настоящего меня..."
    call sna_head("Я понимаю...","snape_02") 
    call sna_head("Тогда ладно...","snape_06") 
    call sna_head("Безопасного тебе, пути домой...") 
    hide screen s_head2
    m "Спасибо тебе. Удачи с проведением бала..."
    call sna_head("*Sigh*","snape_06") 
    pause.3

    hide screen bld1
    with d3
    pause.3
    
    stop music fadeout 1.0

    call sna_chibi("stand","door","base",flip=True) 
    pause.3

    call sna_chibi("leave","door","base") 
    pause.8
    
    m "............................"
    m "Значит, на этом все и заканчивается...?"
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    m "Похоже, мое время в этом мире подошло к концу..."
    m "......................."

    if not public_whore_ending: #YOUR PERSONAL WHORE ENDING. WRITING A LETTER.
        m "Это значит, что я, вероятно, больше никогда не увижу эту девочку..."
        m "..........."
        m "Когда я впервые встретил ее, она была такой занозой..."
        m "Честно говоря, через, что я ее провел, мало что изменилось в этом отношении..."
        m "Но у нас было несколько особенных моментов вместе..."
        m ".............."
        m "......................"
        m "Я не считаю правильным оставлять ее, не попрощавшись должным образом..."
        m "И все же я не хочу упустить свой шанс улизнуть незамеченным..."
        m "Я не люблю долгие прощания..."
        m "Хм..."
        m "Думаю, я мог бы оставить ей записку или письмо..."
        
        m "Давай посмотрим..."
        call bld 
        hide screen genie
        show screen paperwork
        with d3
        m "\"Дорогая...\""
        show screen genie
        hide screen paperwork
        with d3
        m "Хм... Как мне к ней обратиться?"

        menu:
            m "Дорогая..."
            "\"Мисс Грейнджер\"":
                 $ word_01 = "Гермиона Грейнджер" 
            "\"Противная шлюха\"":
                $ word_01 = "Противная шлюха"
            "\"Потаскушка\"":
                $ word_01 = "Потаскушка"
            "\"Спермоглотка\"":
                $ word_01 = "Спермоглотка"
            "\"Человеческая самка\"":
                $ word_01 = "Человеческая самка"
            "\"Подруга\"":
                $ word_01 = "Подруга"

        hide screen genie
        show screen paperwork
        with d3
        m "Да, \"Дорогая [word_01]\" идеально подходит..."
        ">писулька-каракуля-закорючка..."
        ">писулька-каракуля-закорючка..."
        m "\"...пришло время, мне вернуться...\""
        show screen genie
        hide screen paperwork
        with d3
        m "Что я должен написать сейчас?"

        menu:
            m "...время вернуться..."
            "\"домой\"":
                $ word_02 = "домой"
            "\"на Материнский Корабль\"":
                $ word_02 = "на Материнский Корабль"
            "\"в Измерение \"X\"":
                $ word_02 = "в Измерение \"X\""
            "\"в свой мир\"":
                $ word_02 = "в свой мир"
            "\"На свою родную планету-Криптон\"":
                $ word_02 = "на свою родную планету-Криптон"

        hide screen genie
        show screen paperwork
        with d3
        m "Да, \"Время возвращаться [word_02]\" этого достаточно..."
        ">писулька-каракуля-закорючка..."
        ">писулька-каракуля-закорючка..."
        m "\"...прощай моя маленькая...\""
        show screen genie
        hide screen paperwork
        with d3
        m "Что же мне сейчас написать?"

        menu:
            m "...прощай моя маленькая... "
            "\"Шалава\"":
                $ word_03 = "Шалава"
            "\"Спермоглотка\"":
                $ word_03 = "Спермоглотка"
            "\"Девочка\"":
                $ word_03 = "Девочка"
            "\"Ведьма\"":
                $ word_03 = "Ведьма"

        hide screen genie
        show screen paperwork
        with d3
        m "Да, \"прощай моя маленькая [word_03]\" звучит здорово..."
        ">писулька-каракуля-закорючка..."
        ">писулька-каракуля-закорючка..."
        show screen genie
        hide screen paperwork
        with d3
        m "А теперь подпишем его как..."

        label stupid_kent:
            pass

        menu:
            m "..."
            "\"Джинн\"":
                $ word_04 = "Джинн"
            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                hide screen genie
                show screen paperwork
                with d3
                m "Да, \"с уважением, [word_04]\"..."
                show screen genie
                hide screen paperwork
                with d3
                m "..........."
                m "Нет, это не имеет никакого смысла..."
                jump stupid_kent
            "\"лорд Волдеморт\"":
                $ word_04 = "лорд Волдеморт"
            "\"Странник\"":
                $ word_04 = "Странник"

        hide screen genie
        show screen paperwork
        with d3
        m "Да, \"[word_04]\"..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "........................"
        m "Да, этого должно хватить..."

    hide screen bld1
    with d3
    m "Что ж, тогда я отправляюсь..."
    
    call blkfade 

    hide screen genie
    show screen chair_left
    hide screen desk
    show screen desk
    call gen_chibi("stand","desk","base") 
    hide screen bld1
    call hide_blkfade 
    
    m "........."

    call gen_walk("desk","door",3) 
    pause 1

    m "...................."
    m "Аграба... Я иду..."
    call ctc 
    
    call gen_chibi("leave","door","base") 
    pause.3
    ">..............{w}..................{w}...................."
    pause.7
    call blkfade 
    
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Окраина Хогвартса{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen blkback # Hide room

    $ end_u_1_pic =  "images/yule_ball/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    call hide_blkfade 
    call ctc 
    
    m "Северус был прав..."
    pause.5
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "images/yule_ball/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7      
    
    m "Чем дальше я удаляюсь от территории школы..."
    m "Тем больше я начинаю чувствовать свою силу..."
    
    $ end_u_4_pic =  "images/yule_ball/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    m "Думаю, этого достаточно..."
    m "Время, отменить заклинание и вернуться домой..."
    m ".........."
    m "...................."
    m "Аграба... Я иду..."

    if not persistent.game_complete: # FIRST PLAYTHOURGH. 
        call ctc 
        
        show screen blkfade 
        with d9
        pause .5
        
        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.
        
        centered "{size=+7}{color=#cbcbcb}Поздравляем с завершением игры!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}Это концовка \"00\" из \"02\".{/color}{/size}"
        
        centered "{size=+7}{color=#cbcbcb}Спасибо за игру!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}AKABUR 2014{/color}{/size}"
        
        
        #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
        #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
        #scene image "08_ending/e05.png" with Dissolve(2)
        # show akaani with d5

        
        centered "{cps=20}{size=+5}{color=#ea91b0}-Hermione Trainer-{/color}{/size}\n\n
        {size=+5}{color=#e5e297}-Producer-{/color}{/size}\n{color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Head programmer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Writer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Artwork-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Additional Artwork-{/color}{/size}\n     {color=#cbcbcb}DAHR{/color}\n\n
        {size=+5}{color=#e5e297}-Sound Effects-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n"
    #    {size=+5}{color=#e5e297}-MUSIC-{/color}{/size}\n\n

    #    {color=#e5e297}(From \"NEWGROUNDS\")\n
    #    {color=#e5e297}\"Eastern Journey\" {/color}{color=#cbcbcb}by Pike270.{/color}\n
    #    {color=#e5e297}\"Grape Soda Is Fucking Raw\"{/color} {color=#cbcbcb}by jrayteam6.{/color}\n
    #    {color=#e5e297}\"The Eastern Wind\"{/color} {color=#cbcbcb}by roensb.{/color}\n
    #    {color=#e5e297}\"Silly Cat\" {/color}{color=#cbcbcb}by Maverlyn.{/color}\n
    #    {color=#e5e297}\"Kabul Flight\" {/color}{color=#cbcbcb}by Jumpstart.{/color}\n
    #    {color=#e5e297}\"Sleep Walking\" {/color}{color=#cbcbcb}by hektikmusic.{/color}{/cps}"
        #nvl clear
    #    hide akaani
        
        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Подождите, я все еще здесь!"
        centered "{size=+7}{color=#cbcbcb}ЧТО?!{/color}{/size}"
        g4 "Я сказал, что я все еще здесь, черт возьми!"
        centered "{size=+7}{color=#cbcbcb}О... :({/color}{/size}"
        
        
        
        hide screen end_u_4
        with d1
        hide screen blkfade 
        with d9
        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
        
    m "....................."
    if persistent.game_complete:
        m "Нет, я не могу просто так уйти!"
    else:
        m "Я не могу просто так уйти!"
    
    m "Я должен увидеть эту девушку в последний раз..."
    
    call ctc 
    
    show screen blkfade
    with d7
    
    stop music fadeout 1.0
    
    if not persistent.game_complete: # FIRST PLAY THROUGH.
        centered "{size=+7}{color=#cbcbcb}Ладно, неважно...{/color}{/size}"
    play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
    centered "{size=+7}{color=#cbcbcb}\"Ежегодный Осенний Бал В Хогвартсе\"{/color}{/size}"

    hide screen end_u_4
    jump your_whore
    
    return
    
    
    
    
    

label hg_event_EnterRoom_block: #Chibi stands mid. bld1 active.
    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2) 
    pause.5
    call bld 
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
