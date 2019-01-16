

label your_whore:

    #Daytime interface.
    $ interface_color = "gold"
    
    hide screen bld1
    hide screen blktone
    call her_chibi("hide") 
    show screen blkback
    show screen end_u_1
    $ end_u_1_pic =  "images/yule_ball/02.png"
    
    
    #Setting up Hermione's outfit.
    
    #Hermione Hair
    $ h_hair_style = "B"
    $ h_hair_color = 1
    call update_her_hair 

    #Hermione Clothes
    $ transparency             = 1 #Disabled
    $ h_neckwear               = "00_blank"
    $ hermione_body_accs_list  = []
    $ h_gloves                 = "00_blank"
    $ h_stockings              = "00_blank"
    $ hermione_wear_robe       = False
    $ h_request_wear_robe      = False

    $ h_ears                   = "00_blank"
    $ hermione_makeup_list     = []
    $ h_glasses                = "00_blank"
    $ h_hat                    = "tiara"
    $ hermione_wear_hat        = True
    $ h_request_wear_hat       = True

    call h_outfit_OBJ(hg_ballDress_OBJ) #Updates uniform.
    
    hide screen hermione_main
    hide screen room # MAIN BG (DAY).
    
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_near_fire
    hide screen candlefire
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    hide screen main_room_menu  

    with fade
    #hide screen end_u_1                                           #<---- SCREEN
    #hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    #hide screen end_u_4                                           #<---- SCREEN
    pause.1
    hide screen bld1
    hide screen blktone
    call hide_blkfade 
    call ctc 

    show screen bld1
    with d7
  
    m "Лучше я постараюсь, чтобы меня не заметили..."
    m "......................"
    m "Там очень много людей..."
    m "Насколько велика эта школа?"
    m ".................."
    m ".................................."
    m "Я нигде не вижу эту девочку..."
    m ".............."
    m "......................"
    m "Она должна быть где-то здесь..."
    m "................"
    m "................................."

    show screen blktone
    with d7
    
    #Public whore ending.
    if public_whore_ending: #Students talking.
        mal "Вы слышали эти слухи о Гермионе Грейнджер?"
        mal2 "Что она первоклассная шлюха?"
        mal "А? Нет, это не слухи, это факт."
        mal "Ходили слухи,что ей платят очки факультета за то, чтобы она раздевалась."
        mal2 "Хм... Я не могу в это поверить. Я думал, она просто шлюха."
        fem "Кто шлюха?"
        mal "О, привет..."
        fem "Итак, кто здесь шлюха?"
        mal2 "Гермиона Грейнджер..."
        fem "Тсс! Вы, ребята, снова говорите о этой шлюхе?"
        fem "Эта девушка, дрочит пару членов, делает несколько минетов и теперь она новая школьная сенсация."
        fem "Жалкая маглорожденная..."
        mal "Ты не должна ей завидовать.--"
        fem "Ревнуешь? К ней? Обалдеть!"
        fem "Мне не нужна популярность, приходящая от члена во рту!"
        mal "Ну, если ты когда-нибудь передумаешь..."
        fem "А?"
        mal "Не стесняйся использовать меня, в качестве ступеньки на своем пути к славе!"
        fem "Смешно!"
        mal2 "Эй, ребята, я думаю это Гермиона, вон там!"
        mal "Ты прав!"
        mal2 "Ты думаешь, если я приглашу ее потанцевать, мне что-нибудь перепадет?"
        mal "Нет, если я приглашу ее первым!"
        $ renpy.play('sounds/run_04.mp3')    #<--------------------Sound of running off.
        pause 2
        mal2 "Эй, подожди! Это была моя идея!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 2
        fem "Ребята...?"
        fem "........................."
        fem "Тсс... Парни........"

    #Your whore ending.
    else: #Students talking.
        mal "(Вы слышали слухи?)"
        mal2 "(Да. Говорят, Гермиона одна обслужила целую команду.)"
        fem "(Переспала за очки факультета!)"
        fem "(Какой позор!)"
        mal "(Это всего лишь слухи!)"
        fem "(Я думаю, что это больше, чем просто...)"
        mal "(Ой, заткнись. Ты просто завидуешь.)"
        mal2 "(Да, жаль, что у тебя нет смелости, как у Гермионы!)"
        mal "(Вот именно! Она верна принципам \"Гриффиндора\", как никто другой!)"
        mal "(Даже если это правда, и что?)"
        mal "(Благодаря ей наш факультет получит Кубок в этом году!)"
        mal2 "(Да, а что ты сделал для нашего факультета?)"
        fem "(Я..... Но....)"
        mal "(Вот именно! Так что у Гермионы, тогда не плохой рот!)"
        mal2 "(Верно, чувак.)"
        fem "(*Дуется*)"
        
    hide screen bld1
    call hide_blktone 
    call ctc 
    
    
    $ end_u_2_pic =  "images/yule_ball/01.png"
    show screen end_u_2
    with d7
    call ctc 

    call bld 
    m "(Вот она!)"
    
    mal "Эй, Гермиона..."
    call her_head("О, привет.","base","base",xpos="base",ypos="high") 
    mal "Ты выглядишь так красиво сегодня, Гермиона."
    call her_head("Спасибо, ты очень мил.","base","closed") 
    mal2 "Потанцуем следующий танец?"
    mal "Что? Отвали, приятель, я был первым!"
    mal2 "Черт тебя побери!"
    mal "Хорошо, приятель! Вот и все!"
    mal2 "Я тебе не \"приятель\"!"
    call her_head("..............","open","surprised") 
    
    show screen blktone8
    with d3
    stop music fadeout 3.0
    m "Вот мой шанс!"
    m "(Пс! Девочка!)"
    call her_head("???","upset","base") 
    m "(Девочка, это я! Здесь!)"
    call her_head("[genie_name]?","open","base") 
    #her "Professor Dumbledore?"
    m "(Тише! Говори тише и следуй за мной.)"
    call her_head("А?","open","base") 
    pause.1
    $ end_u_1_pic =  "images/yule_ball/02.png"
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    show screen end_u_1 #<---- SCREEN
    with fade
    call ctc 

    call bld 
    # ALCOVE 
    call her_head("Сэр, что происходит? Почему вы скрываетесь?","upset","base") 
    m "Просто молчи и послушай секунду! Ты можешь сделать кое-что сделать для меня?"
    call play_music("playful_tension") # SEX THEME.
    call her_head("Да, сэр...","upset","base") 
    m "Ну, тогда вот в чем дело..."
    m "Есть то, что тебе нужно зна--"
    call her_head("Конечно, сэр!","grin","squint",cheeks="blush") 
    m "Что?"
    call her_head("Давайте сделаем это быстро, хорошо?","soft","glanceL",cheeks="blush") 
    g4 "Давай сделаем что быстро?"
    call her_head("Вы хотите, чтобы я поблагодарила вас за платье, не так ли, сэр?","base","glance",cheeks="blush") 
    m "Платье? Нет, нет, я здесь не из-за этого."
    call her_head("Все в порядке, сэр. Я не против.","soft","glanceL",cheeks="blush") 
    m "Послушай меня, девочка! Я не тот, за кого ты меня принимае--"
    call her_head("Пожалуйста, сэр, позвольте мне немного пососать ваш член.","open_tongue","concerned",cheeks="blush") 
    g4 "Ах--!!!"
    call her_head("Просто немного. Пожалуйста. Я умоляю вас...","open_tongue","concerned",cheeks="blush") 
    g4 "Проклятье, чертова ведьма!"
    g4 "Прекрати! Мне правда нужно с тобой поговорить!"
    call her_head("Ну конечно, сэр.","base","glance",cheeks="blush") 
    call her_head("Засуньте свой член мне в рот и говорите со мной.","open_tongue","concerned",cheeks="blush") 
    call her_head("Говорите грязно со мной...") 
    g4 "*рык!*"
    m "*Вздох....*"
    m "Ладно, давай сделаем по-твоему..."
    m "Но ты злоупотребляешь своей властью, девочка!"
    call her_head("*Хихикает!*","crooked_smile","worriedCl",cheeks="blush") 
    m "И после того, как мы закончим, мы поговорим об этом!"
    
    # SUCKING
    
    show screen blkfade
    with d7
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "................."
    
    $ end_u_1_pic =  "images/yule_ball/03.png" #<---- SCREEN
    hide screen blkfade
    hide screen bld1
    with d7
    call ctc 
    her "*Slurp!* *Gulp!* *Slurp!*"
    her "*Slurp--"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    # LOOKING BACK
    her "А?.........."
    her "...................."
    $ end_u_1_pic =  "images/yule_ball/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Да... Вроде того.... о... да..."
    her "*Gulp!* *Slurp!* *Slurp!*"
    her "*Gulp--"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "...................." #LOOKING BACK
    m "Просто продолжай, девочка."
    m "Я дам тебе знать, если увижу, что кто-то идет..."
    her "О... Это не так, сэр..."
    m "Хм?"
    her "Должны сделать объявление в ближайшее время..."
    $ end_u_1_pic =  "images/yule_ball/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Объявление?"
    her "*Slurp!* *Slurp!* *Slurp!*"
    her "*Slurp--"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Да. Насчет коронации..."
    $ end_u_1_pic =  "images/yule_ball/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Gulp!* *Slurp!* *Gulp!*"
    m "Что...?"
    her "*Slurp--"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Коронация королевы осеннего бала в Хогвартсе, сэр."
    m "О... Что это?"
    m "Есть шанс, что тебя выберут?"
    her "Шанс?"
    her "Решение уже принято, сэр."
    m "Что?"
    her "Я имею в виду, я надеюсь, что выиграю..."
    her "Так как я тот, кто организовал осенний бал, то это справедливо..."
    her "Разве вы не согласны, сэр?"
    m "Ну... Звучит как обман--"
    $ end_u_1_pic =  "images/yule_ball/07.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Slurp!* *Slurp!*"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Разве вы не согласны, сэр?"
    m "Эм..."
    her "Разве вы не согласны, сэр?"
    $ end_u_1_pic =  "images/yule_ball/06.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    with hpunch
    her "{size=+7}*gobble!*{/size}" #DEEPTHROATING
    g4 "{size=+7}О, да!!!{/size}"
    her "*gobble!* *gobble!* *gobble!*"
    her "*gobble---"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Хорошо. Я знала, что вы согласитесь."
    $ end_u_1_pic =  "images/yule_ball/07.png" #<---- SCREEN
    show screen end_u_1                                            #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "О... Это великолепно..."
    her "*Slurp!* *Slurp!* *Gulp!*"
    
    show screen bld1
    with d5
    sna "*Кхем!*"
    sna "Внимание, бездари!" 
    m "(Снейп?)"
    sna "Я сказал, успокойтесь все!"
    sna "Пришло время объявить, кто будет королевой этого года \"осеннего бала Хогвартса\"."
    
    
#    ann "Quiet down everyone, quiet down..."
#    ann "It is time to choose this year's queen of the annual \"Hogwarts autumn ball\"."
    hide screen bld1
    with d5
    
    
    her "Хлюп--"
    $ end_u_2_pic =  "images/yule_ball/04.png" #<---- SCREEN
    show screen end_u_2                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "О нет! Думаю, все вот-вот начнется..."
    her "Но я не могу просто оставить вас в таком..."
    her "...состоянии, сэр."
    
    
    her "Что я должна делать?"
    m "Просто иди, девочка. Мы можем закончить позже."
    her "Но... Но вы купили мне это платье, сэр. И..."
    her ".........."
    her "Нет, я не могу оставить вас в таком состоянии, сэр."
    m "Отлично! Тогда закончи работу."
    m "Если ты приложишь немного усилий, мы сделаем это в кратчайшие сроки."
    m "Я верю в тебя, девочка."
    her "Хм..."
    her "Тогда вы должны мне кое-что пообещать, сэр."
    m "Да, и что же это?"
    her "Пожалуйста, не сдерживайтесь."
    g9 "Хех... Я редко это делаю, девочка."
    show screen bld1
    with d5
    sna "В этом году на \"Хогвартском Осеннем Балу\" королева..."
    sna "Давайте посмотрим... Не могу открыть чертов конверт..."
    hide screen bld1
    with d5
    her "Хорошо. Не будем терять время."
    m "Да! Вот это настрой!"
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ end_u_1_pic =  "images/yule_ball/03.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Да..."
        $ end_u_2_pic =  "images/yule_ball/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Gulp!* *Slurp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "images/yule_ball/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Сэр, это действительно правильный способ относиться к одному из своих учеников?"
        m "А?"
        $ end_u_2_pic =  "images/yule_ball/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "images/yule_ball/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я как хрупкая и впечатлительная маленькая голубка..."
        her "Довереная вам своими родителями..."
        $ end_u_2_pic =  "images/yule_ball/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы должны были относиться ко мне \"правильно\", сэр..."
        her "И что вы сделали вместо этого?"
        m "*Кхем!* Позволь мне повторить мое предыдущее заявление:.."
        m "{size=+7}\"да?\"{/size}"
        $ end_u_1_pic =  "images/yule_ball/94.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы помещаете свой пенис в мой невинный рот, сэр!"
        $ end_u_2_pic =  "images/yule_ball/95.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g9 "О, да! Мне нравится, что делает эта невинная девочка!"
        her "*Slurp--"
        $ end_u_1_pic =  "images/yule_ball/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы притворялись добродетелем..."
        her "Вы купили мне это платье..."
        $ end_u_2_pic =  "images/yule_ball/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "И....................."
        $ end_u_1_pic =  "images/yule_ball/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_2_pic =  "images/yule_ball/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы воспользовались мной, сэр!"
        her "Заставили сосать свой большой член!"
        g4 "О... Да! Ты великолепна!"
        $ end_u_1_pic =  "images/yule_ball/96.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я должна была, со своми одноклассниками праздновать победу нашей команды по Квиддичу..."
        $ end_u_2_pic =  "images/yule_ball/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Но что я делаю вместо этого?"
        $ end_u_1_pic =  "images/yule_ball/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Ох..."
        $ end_u_2_pic =  "images/yule_ball/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "images/yule_ball/98.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я на коленях, отсасываю директору!"
        $ end_u_2_pic =  "images/yule_ball/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "О, да, маленькая шлюшка!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "Ты действительно хороша, в таких пошлых разговорах..."
        g9 "Ты должна попробовать писать детские книги, или что-то вроде того..."
        $ end_u_1_pic =  "images/yule_ball/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp--"
        $ end_u_2_pic =  "images/yule_ball/91.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Но я не знаю, как это сделать, сэр..."
        $ end_u_1_pic =  "images/yule_ball/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "потому что я сама, еще всего лишь ребенок..."
        g4 "Ты мерзкая маленькая шлюшка!"
        $ end_u_2_pic =  "images/yule_ball/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!* *Slurp!* *Slurp!*"
        
        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "{size=-4}(Где эта девочка?){/size}"
        ">В толпе, студенты начинают перешептываться..."
        hide screen bld1
        with d5
        
        her "*Slurp!* *Slurp!* *Gulp!*"
        her "*Gulp--"
        $ end_u_1_pic =  "images/yule_ball/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Сэр, я правда, послушная маленькая шлюшка?"
        g4 "Да, конечно, девочка!"
        $ end_u_2_pic =  "images/yule_ball/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "По вашему, я хорошая студентка?"
        g9 "Я бы сказал, что ты отличная студентка, девочка!"
        $ end_u_1_pic =  "images/yule_ball/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Хорошо..."
        $ end_u_2_pic =  "images/yule_ball/99.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я заставлю маму и папу гордиться собой!"
        $ end_u_1_pic =  "images/yule_ball/95.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "Ох, девочка, ты убиваешь меня!"
        her "*Slurp-slurp-slurp-slurp!!!*"
        g4 "О, да! Вот так!"
        her "*Slurp--"
        $ end_u_2_pic =  "images/yule_ball/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я заслуживаю награды, сэр?"
        $ end_u_1_pic =  "images/yule_ball/100.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Пожалуйста, я хочу награды, в виде вашей спермы."
        g4 "Гр!"
        $ end_u_2_pic =  "images/yule_ball/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Ге! Почти...!"
        her "{size=+5}*Slurp-Gulp-slurp-slurp!!!*{/size}"
        g4 "{size=+5}Вот оно наподхо--{/size}"
        $ end_u_1_pic =  "images/yule_ball/101.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp--.........................."
        her "!!!"
        call ctc 
        
        show screen blkfade 
        with d7
        $ end_u_2_pic =  "images/yule_ball/102.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        g4 "{size=+5}Что...?! Почему ты остановилась?!{/size}"
        g4 "{size=+5}Какого черта ты делаешь--{/size}"
        hide screen blkfade 
        with d7
        call ctc 
        
        her "{size=+5}Кончите на меня. сэр! Кончите на меня!{/size}"
        with hpunch
        g4 "{size=+5}Что такое, черт возьми?!{/size}"
        $ end_u_1_pic =  "images/yule_ball/103.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Кончите на меня. сэр! Я хочу, вашу горячую сперму!{/size}"
        g4 "Аргх! Ты шлюха!"
        $ end_u_2_pic =  "images/yule_ball/104.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Да, Я!{/size}"
        her "{size=+5}Очень голодная до спермы шлюха, сэр!{/size}"
        with hpunch
        g4 "{size=+7}Аргх!!!{/size}"
        g4 "{size=+7}Тогда получай ее!!!{/size}"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}АРГХ!{/size}"
        $ end_u_1_pic =  "images/yule_ball/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Ах! Да, сэр! Да! Кончайте на меня!{/size}"
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}АРГХ!{/size}"
        g4 "{size=+7}Аргх!!! ДА!!!{/size}"
        $ end_u_2_pic =  "images/yule_ball/106.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ах... да... ах..."
        g4 "Ох... хт... *отдышка*"
        $ end_u_1_pic =  "images/yule_ball/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Спасибо, сэр..."
        $ end_u_2_pic =  "images/yule_ball/107.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "..........................................."
        call ctc 
        
        show screen blkfade
        with d7
        
        # CUMMING
        pause.5
        m "Что только что произошло, девочка?!"
        $ her_head_ypos = her_head_tits
        call her_head("Что вы имеете в виду, сэр?","soft","glanceL",cheeks="blush") 
        $ end_u_1_pic =  "images/yule_ball/02.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        hide screen blkfade
        with d7
        m "Мне правда нужно указать на это, девочка?"
        g4 "{size=+5}Правда, правда?{/size}"
        call her_head("О... Вы имеете в виду прическу...?","soft","glanceL",cheeks="blush") 
        m "Да...\"прическу\"..."
        call her_head("Что вы ожидали от меня, сэр?","crooked_smile","worriedCl",cheeks="blush") 
        m "Буквально все..."
        g4 "...но {size=+7}ЧТО!{/size}"
        call her_head("Но... Мне нужно выглядеть лучше для коронации...","open","base") 
        m "А прическа полная спермы, тебе это обеспечит?"
        call her_head("Ну да...","soft","glanceL",cheeks="blush") 
        call her_head("Видите ли, сперма - это отличный фиксатор волос и--","open","base") 
        
        show screen bld1
        with d5
        stop music fadeout 1.0
        sna "Мисс Грейнджер..................?"
        sna "Ты пропустишь свою коронацию, девочка!"
        sna "(Не то, чтобы это меня волновало...)"
        hide screen bld1
        with d5
        
        call her_head("Коронация! Я должна идти!","open","surprised") 
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        
        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}КАКОГО ЧЕРТА...?!!{/size}"
        call ctc 
        
        show screen blkfade
        with d7
        

        ">..............{w}..................{w}...................."
        
        
        
        
    else:
        $ end_u_1_pic =  "images/yule_ball/06.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+5}*GOBBLE!*{/size}"
        g4 "{size=+5}Даааааааа!{/size}"
        show screen bld1
        with d5
        sna "Там! Хм...?"
        sna "(Ну конечно... Почему меня это не удивляет?)"
        sna "Мисс Гермиона Грейнджер - факультет \"Гриффиндор\"..."
        ">Громкие овации и аплодисменты."
        sna "Мисс Грейнджер, будьте так добры, украсьте нас своим присутствием..."
        hide screen bld1
        with d5
        her "*GOBBLE--GOBBLE--GOBBLE!*"
        m "Да! Она хорошая шлюха!"
        her "{size=+5}*gobble--gobble--gobble!!!*{/size}"
        m "Да. Теперь пошевели язычком..."
        m "Лижи мне яйца, девочка. Давай же!"
        $ end_u_2_pic =  "images/yule_ball/10.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *Lick!* *Lick!* *gobble!*"
        m "Да... Вроде этого."
        m "Какая ты хорошая шлюха..."
        her "*Lick!* *Lick!* *gobble!* *Lick!*"
        m "Теперь посмотри на меня, шлюха."
        $ end_u_1_pic =  "images/yule_ball/11.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "???................"
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "images/yule_ball/12.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        call ctc 
        
        her "*gobble??!*"
        m "Нет, только не останавливайся!"
        $ end_u_2_pic =  "images/yule_ball/13.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble--gobble--gobble!*"
        m "Да, шлюха! Да!"
        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "Выходите на сцену..."
        sna "Мисс Грейнджер?"
        hide screen bld1
        with d5
        $ renpy.play('sounds/spit.mp3')    #<--------------------Sound of spiting. 
        show screen white
        pause.3
        $ end_u_2_pic =  "images/yule_ball/14.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        hide screen white
        with vpunch
        call ctc 
        
        her "!!!!!!!!!!!"
        her "......................................?"
        m "Что случилось, моя маленькая спермососка?"
        m "Продолжай сосать мой член!"
        $ end_u_1_pic =  "images/yule_ball/15.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble--gobble--gobble!*"
        m "Да. Хорошая шлюха."
        her "*gobble--gobble--gobble!*"
        m "Продолжай заглатывать глубоко, да!"
        her "*gobble!* *gobble!* *gobble!*"
        m "Яички! Не забудь поработать языком!"
        $ end_u_2_pic =  "images/yule_ball/16.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *Lick!...* *Lick!...*"
        m "Да! Продолжай так же, и мы скоро закончим!"
        m "О, я чуть не забыл..."
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.3
        $ end_u_2_pic =  "images/yule_ball/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with vpunch
        call ctc 
        
        her "..........................."
        her ".................."
        $ end_u_2_pic =  "images/yule_ball/18.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Ты выглядишь так красиво с обслюнявленым лицом!"
        $ end_u_1_pic =  "images/yule_ball/19.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Хм ..."
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Возможно, надо показать твое симпатичное лицо всем?"
        m "Мне позвать твоих одноклассников?"
        $ end_u_2_pic =  "images/yule_ball/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "!!!!!!!!!!!!!!!"
        m "Расслабься..."
        m "Я не хочу быть пойманным, как и ты."
        $ end_u_1_pic =  "images/yule_ball/19.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        
        
        

        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "{size=-4}(Где эта девочка?){/size}"
        ">По толпе студентов пробегает ропот..."
        hide screen bld1
        with d5
        
        m "Ладно, слушай сюда, шлюшка."
        $ end_u_2_pic =  "images/yule_ball/20.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble??*"
        m "Мне нужно, чтобы ты не двигалась."
        her "???"
        $ end_u_1_pic =  "images/yule_ball/21.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Да, именно так."
        her "................"
        
        $ end_u_2_pic =  "images/yule_ball/22.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "....................................."
        m "Я собираюсь немного задушить тебя своим членом ..."
        m "Это будет весело... просто расслабься..."
        her "......................................"
        m "Твое горло самое лучшее, девочка."
        her "..........."
        $ end_u_1_pic =  "images/yule_ball/23.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Так тепло и туго..."
        her "............................................."
        her "...................."
        her "......."
        $ end_u_2_pic =  "images/yule_ball/24.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "!!!"
        m "Я знаю, я знаю, ты не можешь дышать ..."
        g9 "Но это доставляет мне неземное удовольствие!"
        
        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Хватит сопротивляться, шлюха. Ты никуда не пойдешь!"
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"
        
        show screen bld1
        with d5
        sna "Мисс Грейнджер..................?"
        sna "Девочка, вы собираетесь пропустить свою собственную коронацию!"
        hide screen bld1
        with d5
        
        g9 "Хех..."
        g9 "Ваша королева находится прямо здесь..."
        g4 "Обрабатывает мой набухший член!"
        $ end_u_1_pic =  "images/yule_ball/26.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "О. Любовь, ты кажется посинела."
        m "Все в порядке?"
        $ end_u_1_pic =  "images/yule_ball/27.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        m "Взгляни вверх, шлюха!"
        her "{size=+3}........................{/size}"
        g4 "Я сказал, посмотри на меня!"
        $ end_u_2_pic =  "images/yule_ball/28.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}??!.....................{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.5
        
        $ end_u_1_pic =  "images/yule_ball/29.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
       # with d7                                                                        #<---- SCREEN
        with vpunch
        her "{size=+9}*!!!!!!!!!!!!!!!!!!*{/size}" # 4 (EYE)
        
        $ end_u_2_pic =  "images/yule_ball/30.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................................................."
        g4 "Вот так! Ты хорошо работаешь!"
        $ end_u_1_pic =  "images/yule_ball/31.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...........................................................*SOB!*"
        with hpunch
        g4 "Гхт!"
        g4 "Я скоро!"
        g4 "Я знаю, что тебе не хватает воздуха..."
        $ end_u_2_pic =  "images/yule_ball/32.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        g4 "Но все, что ты получишь от меня, это много горячей спермы!"
        $ end_u_1_pic =  "images/yule_ball/33.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+9}ГХТ!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        g4 "{size=+9}АРГХ!{/size}"
        with hpunch
        $ end_u_2_pic =  "images/yule_ball/34.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}*Gulp!-Gulp!-Gulp!-Gulp!-Gulp!*{/size}"
        g4 "{size=+5}Да, шлюха! Выпей всю мою сперму!{/size}"
        her "*Gulp!-Gulp!-Gulp!-Gulp......*"
        with hpunch
        g4 "Я еще не закончил. Продолжай! Аргх!"
        $ end_u_1_pic =  "images/yule_ball/35.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-4}*Gulp!* *Gulp!* *Gulp...*{/size}"
        m "О, да..."
        $ end_u_2_pic =  "images/yule_ball/36.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................."
        m "Ну, я думаю, что ты высосала все, до последней капли--"
        with hpunch
        g4 "{size=+5}Ха?!!{/size}"
        show screen blkfade
        with d3
        stop music fadeout 1.0
        g4 "Эй, что ты--"
        ">Гермиона резко встает и убегает, не сказав ни слова..."
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "Хм...?"
        m "О, правильно... Коронация..."
        m "............."
        #m "Still need to talk to her though..."
        ">..............{w}..................{w}...................."
    
    pause 1
    
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ snape_head_xpos = 330 # x = 330,
        $ snape_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        call sna_head("Мисс Грейнджер...?","snape_03") 
        call sna_head("Вы все-таки решили появиться?","snape_04") 
        $ s_sprite = "characters/snape/main/.png"
        call sna_head("Какой неприятный сюрприз...","snape_03") 
        #her "Professor..."
        call her_head("Профессор...","upset","base") 
        call sna_head("Что ж, тогда вперед...","snape_10") 
        call sna_head("Вот диадема...") 
        call sna_head("И сцена ваша...") 
        $ tiara = True #Tiara is displayed.
        #her "Thank you, professor."
        call her_head("Благодарю вас, профессор.","base","closed") 
        pause.7
        
        $ end_u_1_pic =  "images/yule_ball/108.png" #<---- SCREEN
        hide screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        call ctc 
        
        her "..............."
        her ".................................."
        $ end_u_2_pic =  "images/yule_ball/109.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Всем привет!"
        her "Спасибо за то, что сделали меня своей королевой бала, второй год подряд!"
        
        show screen blktone
        show screen bld1
        with d3
        m "!!!"
        m "Ее прическа выглядит идеально!"
        m "Я полагаю, я был неправ и--"
        g4 "Нет, вон там!"
        g4 "Капает, позади ее уха!"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_1_pic =  "images/yule_ball/110.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я хотела бы посвятить свою речь каждой девушке в этой комнате ..."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Что она думала, вытворяя этот трюк?"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_2_pic =  "images/yule_ball/111.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я не буду заходить так далеко, чтобы говорить, что не заслуживаю этой чести..."
        her "Потому что я думаю, что я..."
        $ end_u_1_pic =  "images/yule_ball/112.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Но я по-прежнему очень благодарна за то, что сегодня стою здесь, перед всеми вами..."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(а?)"
        mal "(Что это у нее на лбу, парни?)"
        mal2 "(Пот...?)"
        mal "(Хм... Вероятно..)"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "images/yule_ball/113.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Особенно хотелось бы поблагодарить наших уважаемых учителей за их тяжелый труд."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Разве она не чувствует?!"
        g4 "Ей лучше прервать свою речь!"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Хогвартс действительно стал вторым домом для всех нас..."
        $ end_u_1_pic =  "images/yule_ball/114.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я знаю, что говорю от имени каждого студента."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(Это не похоже на пот, хотя ...)"
        mal2 "(Да...)"
        mal2 "(Какая-то странная слизь просачивается из ее волос...)"
        fem "(Вы, ребята, действительно {size=+5}тупые{/size}?)"
        mal "(Почему?)"
        fem "(Это же очевидно... сперма)"
        mal2 "(Что? Чушь собачья!)"
        fem "(Я думаю, что узнаю сперму, если увижу ее.)"
        mal "(Держу пари, что да. *Хихиканье*)"
        fem "(Вон. Взгляните получше...)"
        fem "(Она, должно быть, позволила какому-то парню засунуть член в свою прическу и обильно туда кончить.)"
        mal "(Хм... Трахать мозг? Теперь в этом выражении есть смысл?)"
        mal2 "(Вы, девочки, делаете самые сумасшедшие вещи.)"
        fem "(*Хамф!* Знаешь, не все из нас шлюхи.)"
        mal "(К сожалению, нет...)"
        fem "(\"Сожалению\"?!)"
        fem "(Тс! Вы, мужчины такие невежи во всем!)"
        fem "(Вы никогда не построите серьезные отношения со шлюхой!)"
        mal "(Что такое \"серьезные отношения\"?)"
        fem "(Это когда твоя девушка, еще и твоя лучшая подруга.)"
        mal "(О, мне не нужна {size=+5}подруга{/size}!)"
        mal "(У меня уже есть лучший друг, этот уродливый засранец..)"
        mal2 "(Зашибись, приятель!)"
        mal "(Но я уверен, что могу использовать шлюху в своей жизни!)"
        mal2 "(Зашибись, приятель!)"
        fem "(...вы, парни...)"
        fem "Такие идиоты!!!"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "images/yule_ball/115.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я помню, когда я была маленькой девочкой..."
        
        show screen blktone
        show screen bld1
        with d3
        m "А?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Испугалась своей силы..."
        
        show screen blktone
        show screen bld1
        with d3
        m "Хм..."
        m "Вон... Она сделала это еще раз..."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Кто знает, что было бы со мной, если бы не Хогвартс!"
        show screen blktone
        show screen bld1
        with d3
        m "И снова..."
        m "Почему она постоянно, так неуклюже дергает плечом...?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Мне так повезло быть здесь студентом..."
        call ctc 
        
        stop music
        #$ renpy.play('sounds/scratch.wav')
        hide screen ctc
        $ end_u_1_pic =  "images/yule_ball/116.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        call ctc 
        
        # TIT BARES
        # MUSIC STOPS
        
        show screen blktone
        show screen bld1
        with hpunch
        g4 "!!!"
        #call play_music("playful_tension")# SEX THEME.
        call sna_head("!!!","snape_11") 
        hide screen blktone
        hide screen bld1
        call ctc 
        
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Спасибо всем большое..."
        $ end_u_2_pic =  "images/yule_ball/117.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Позвольте я повторюсь..."
        $ end_u_1_pic =  "images/yule_ball/118.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Спасибо за то, что сделали меня вашей королевой бала в этом году..."
        call ctc 
        
        # SEX MUSIC STARTS TO PLAY
        
        show screen blktone
        with d7
        #call play_music("playful_tension")# SEX THEME.
        mal "(У меня галлюцинации?)"
        mal2 "(Нет, это действительно происходит... Я тоже это вижу...)"
        mal "(Гермиона... Грейнджер... сиська...)"
        mal "(Конфуз с одеждой, приятель!)"
        fem "(О, нет! Бедняжка! Мы должны сказать ей!)"
        mal "(Не смей отнимать это у нас, девочка!)"
        fem "(Но...!!)"
        hide screen blktone
        with d7
        call ctc 
        
        her "И больше всего я благодарна моим родителям..."
        her "Люди, которые воспитали меня..."
        her "Мама... Папа..."
        $ end_u_2_pic =  "images/yule_ball/119.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Мне жаль, что вы не видели насколько Хогвартс изменил меня..."
        her "Мне жаль, что вы не видете свою маленькую девочку..."
        her "{size=-5}Ах...{/size}{image=textheart}"
        call ctc 
        
        show screen blktone
        with d7
        g4 "Шлюха покраснела! Она прекрасно понимает, что происходит!"
        g4 "Противная шлюха!"
        g4 "(Она это все спланировала??!)"
        m "(О Великие Пески Пустыни... Что я наделал?!)"
        hide screen blktone
        with d7
        
        $ end_u_1_pic =  "images/yule_ball/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "..............................."
        her ".................."
        call ctc 
        
        show screen blktone
        with d7
        mal "(Теперь она просто стоит...)"
        mal2 "(Дает нам насмотреться...?)"
        mal "(Как вы думаете, она вообще знает, что ее сиська всем видна?)"
        fem "(Какое бесстыдство...)"
        fem "(И подумать только, мне чуть не стало жалко эту щалаву...)"
        fem "........................"
        with hpunch
        fem "{size=+7}Прикройся, бесстыжая шлюха!!!{/size}"
        mal "(!!!)"
        mal2 "(Ты с ума сошла?!)"
        with hpunch
        fem "{size=+7}Гриффиндорская шлюха!!!{/size}"
        hide screen blktone
        with d7
        
        $ end_u_2_pic =  "images/yule_ball/121.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-3}Ах...{/size}{image=textheart}"
        her "...............................а-ха...{image=textheart}{image=textheart}{image=textheart}"
        call ctc 
        
        show screen bld1
        with d7
        cr1 "Покажи нам обе, Гермиона!"
        cr2 "Посмотрите! На ее лице сперма!"
        cr1 "Как тебе не стыдно, Гермиона?!"
        cr2 "Прикройся, шлюха!"
        hide screen bld1
        with d7
        
        $ end_u_1_pic =  "images/yule_ball/122.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "О... Верно..."
        her "Я чуть не забыла..."
        $ end_u_2_pic =  "images/yule_ball/123.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+5}Вперед, Гриффиндор!{/size}"
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        "*Дикие овации и апплодисменты!*"
        $ end_u_1_pic =  "images/yule_ball/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "......................................"
        her ".........................................................."
        call ctc 
        
        show screen bld1
        with d7
        $ s_sprite = "characters/snape/main/snape_12.png"
        show screen s_head2
        sna "Успокойтесь все!"
        sna "Что касается вас, мисс Грейнджер..."
        sna "Думаю, этого достаточно."
        sna "Прикройся и проваливай со сцены... Убирайся..."
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        
        $ end_u_2_pic =  "images/yule_ball/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "\"Прикрыться\", сэр?"
        $ end_u_1_pic =  "images/yule_ball/119.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "А? Что? Ой, моя грудь выпала из платья..."
        $ end_u_2_pic =  "images/yule_ball/120.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Как неловко..."
        $ end_u_1_pic =  "images/yule_ball/121.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ах...{image=textheart}{image=textheart}{image=textheart}"
        call ctc 
        
        show screen bld1
        with d7
        cr1 "Шлюха!"
        cr2 "Гриффиндорская шалава!"
        cr1 "Я люблю тебя, Гермиона!"
        cr2 "Гриффиндор рулит!!!"
        
        $ s_sprite = "characters/snape/main/snape_18.png"
        show screen s_head2
        sna "Мисс Грейнджер, я сказал, что достаточно!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        her "Как скажите, профессор..."
        show screen bld1
        with d7
        $ s_sprite = "characters/snape/main/snape_12.png"
        show screen s_head2
        sna "И вытри свое лицо, девочка. Ты выглядишь отвратительно."
        hide screen s_head2
        pause.1
        hide screen bld1
        $ end_u_2_pic =  "images/yule_ball/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "О, это? Это просто мой--"
        show screen bld1
        with d7
        $ s_sprite = "characters/snape/main/snape_18.png"
        show screen s_head2
        sna "Все равно! Убирайся уже со сцены!"
        sna "Сейчас же!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        $ end_u_1_pic =  "images/yule_ball/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        call ctc 
        
        show screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Дикий свист и аплодисменты сохраняются, когда Гермиона сходит со сцены ..."
        pause 1
        stop music fadeout 3.0
        ">..............{w}..................{w}...................."
        
        # BACK AT THE ALCOVE (BLACK SCREEN STILL).
        $ end_u_2_pic =  "images/yule_ball/02.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        hide screen blkfade
        with d7
        show screen bld1
        with d5
        call ctc 
        
        $ her_head_ypos = her_head_tits
        call her_head("[genie_name]...","soft","glanceL",cheeks="blush") 
        #her "Professor Dumbledore..."
        call her_head("Вы что-то хотели обсудить со мной?") 
        g4 "Не сейчас, шлюха.!"
        show screen blkfade
        with d5
        call her_head("Сэр?!","base","glance",cheeks="blush") 
        g4 "Я так сильно хочу тебя трахнуть! Подойди сюда!"
        call play_music("playful_tension") # SEX THEME.
        call her_head("Конечно, сэр...","silly","ahegao_squint",cheeks="blush") 
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        pause.5
        g4 "{size=+7}О, ДА!{/size}"
        
        
        $ end_u_1_pic =  "images/yule_ball/46.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        hide screen blkfade
        hide screen bld1
        with d7
        
        call ctc 
        
        
        her "ААА!!!"
        g4 "Твоя речь была позорной, девочка!"
        $ end_u_2_pic =  "images/yule_ball/50.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я думаю, все прошло неплохо..."
        g4 "Демонстрируя свою грудь?!"
        $ end_u_1_pic =  "images/yule_ball/56.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Только одну... ах..."
        g4 "Что?"
        her "Только одну грудь, сэр..."
        g4 "Что случилось с той идеалистичной и самодовольной девочкой, которой ты когда-то была?!"
        $ end_u_2_pic =  "images/yule_ball/59.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Сэр, вы ее протрахали из меня!"
        g4 "Ты чертовски права, я это сделал!"
        $ end_u_1_pic =  "images/yule_ball/124.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Сэр, вы ее протрахали из меня своим огромным членом!"
        g4 "Ох! Шлюха!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_2_pic =  "images/yule_ball/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ах!!!"
        g4 "Тише шлюха! Нас могут услышать!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        
        #her "Ah! Professor!"
        her "Ах! [genie_name]!"
        g4 "Я сказал, тише!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_1_pic =  "images/yule_ball/55.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                       #<---- SCREEN
        #her "Ah! Professor!"
        her "Ах! [genie_name]!"
        $ end_u_2_pic =  "images/yule_ball/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Да! Трахните меня жестче!"
        m "Ты нарочно говоришь громко, шлюха?"
        g4 "Хочешь, чтобы тебя застукали?"
        g4 "На члене профессора?"
        $ end_u_1_pic =  "images/yule_ball/125.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах! Возможно..."
        $ end_u_2_pic =  "images/yule_ball/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Сэр, зовите меня \"грязнокровка\"!"
        m "Что?"
        $ end_u_1_pic =  "images/yule_ball/51.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Зовите меня \"грязнокровка\", пожалуйста!"
        m "\"грязнокровкой\"?"
        $ end_u_2_pic =  "images/yule_ball/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах! Да! Да! Я грязнокровая шлюха!"
        g4 "Да, как хочешь!"
        
        #SLAP
        #SLAP
        #SLAP
        #SLAP
        
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.5
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.4
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.2
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        
        $ end_u_1_pic =  "images/yule_ball/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        her "ААААААААААААААААХ!"
        her "Да!!! Дааа! Ах!"
        $ end_u_2_pic =  "images/yule_ball/63.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "Fuck me professor! Fuck me harder!!!"
        her "Трахайте меня [genie_name]! Трахните меня жестче!!!"
        g4 "Грт! Жестче, чем сейчас, шлюха?!"
        g4 "!!!"
        g4 "Дерьмо!  Кто-то идет!"
        $ end_u_1_pic =  "images/yule_ball/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Нет, сэр, недостаточно. Продолжайте шлепать меня--"
        g4 "Нет, шлюха! Кто-то идет сюда!"
        $ end_u_2_pic =  "images/yule_ball/127.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Что?!"
        
        # STUDENTS
        
        sly1 "Так, так, так... Кто тут у нас?"
        $ end_u_1_pic =  "images/yule_ball/126.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        call ctc 
        
        her "!!!"
        sly1 "Я ожидал, что это будет кто-то из \"Гриффиндора\"..."
        sly1 "Стонет, как шлюха..."
        sly1 "Трахается... О..."
        with hpunch
        sly1 "Профессор Дамблдор?!"
        m "Привет, ребятки..."
        her ".........................."
        sly1 "О... Эм... Мы не знали..."
        sly1 "Мы сейчас уйдем..."
        m "Что? Не будьте глупыми, парни."
        m "Вы можете остаться, и..."
        sly1 "Мы?"
        $ end_u_2_pic =  "images/yule_ball/128.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Что?!"
        m "Конечно."
        $ end_u_1_pic =  "images/yule_ball/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        #her "Professor?!!!"
        her "[genie_name]?!!!"
        m "Ее голова полностью в вашем распоряжении."
        $ end_u_2_pic =  "images/yule_ball/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "Professor! No!"
        her "[genie_name]! Нет!"
        m "Что случилось, блядь?"
        $ end_u_1_pic =  "images/yule_ball/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Сэр, не называйте меня так перед ними, пожалуйста..."
        m "В чем дело? Почему ты вдруг стала такой застенчивой?"
        her "Разве вы не видите, что они из \"Слизерина\"?!"
        m "Ну и что?"
        her "Наши факультеты... у нас всегда были конфликты."
        m "О..."
        m "Ну, тогда ты станешь мостом между \"Слизерином\" и \"Гриффиндором\"."
        m "Гермиона Грейнджер, миротворец!"
        $ end_u_2_pic =  "images/yule_ball/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Нет, сэр! Я отказываюсь!"
        her "И перестаньте двигать бедрами, пока мы разговариваем, сэр!"
        m "Парни, чего медлим?"
        m "Я сказал, ротик шлюхи ваш!"
        #her "Professor Dumbled--"
        her "[genie_name]--"
        sly1 "Заткнись, мерзавка!"
        
        # FACE SPIT
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "images/yule_ball/132.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        call ctc 
        
        $ end_u_1_pic =  "images/yule_ball/133.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        m "Вот, держи!"
        
        sly2 "Ха-ха-ха! Отлично! Посмотри на ее глупое лицо!"
        $ end_u_2_pic =  "images/yule_ball/134.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Вы... Вы...!"
        sly1 "Нам очень понравилась твоя речь, \"Гриффиндорская шлюха\"."
        sly2 "Да... Конечно..."
        her "Она не для вас предназначалась, мерзавцы Слизеринцы!"
        sly1 "Не предназначалась для нас? Ты что, тупая?"
        sly1 "Ты обнажила свою грязную грудь на сцене! Прямо перед всей школой!"
        sly1 "{size=+7}Конечно, это было для всех, тупая пизда!{/size}"
        
        $ end_u_1_pic =  "images/yule_ball/135.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN

        her "Сэр! Хватит меня трахать!"
        m "А? Ты имеешь в виду, вот так?"
        with hpunch
        pause.3
        #her "Ah-aha! No, professor, stop it!"
        her "Ах, ага! Нет, [genie_name], прекратите!"
        m "Прекратить? Думаю, я буду ебать тебя жестче!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        $ end_u_2_pic =  "images/yule_ball/133.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Аахах!!!"
        sly1 "Да... Ты теперь наша, шлюха!"
        call ctc 
        
        # DICKS OUT
        $ end_u_1_pic =  "images/yule_ball/136.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Что?! Что вы задумали?!"
        $ end_u_2_pic =  "images/yule_ball/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Немедленно уберите свои грязные хуи!"
        with hpunch
        pause.3
        $ end_u_1_pic =  "images/yule_ball/138.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... Аха..."
        sly1 "Да... Я давно хотел сделать подобное..."
        #her "Professor!"
        her "[genie_name]!"
        m "А? Не обращай на меня внимания, девочка."
        m "Представь, что меня здесь нет..."
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_1_pic =  "images/yule_ball/139.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        call ctc 
        
        $ end_u_2_pic =  "images/yule_ball/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Прекратите! Хватит плевать мне в лицо, ублюдки!"
        sly1 "Заставь нас, шлюха!"
        her "Я предупрежда--"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "images/yule_ball/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        call ctc 
        
        # SPIT!
        $ end_u_1_pic =  "images/yule_ball/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp!*{/size}"
        sly2 "Ха-ха-ха! Прямо в рот! Хорошая точность, приятель!"
        sly1 "И она его проглотила!"
        $ end_u_2_pic =  "images/yule_ball/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Это было случайно!"
        sly1 "Разве? Давай посмотрим."
        her "А?"
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "images/yule_ball/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        call ctc 

        
        # SPIT!
        $ end_u_1_pic =  "images/yule_ball/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp!*{/size}"
        
        

        sly2 "Она сделала это, снова!"
        $ end_u_2_pic =  "images/yule_ball/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Это потому, что я этого не ожидала... Это всего лишь рефлекс!"
        sly1 "Какой горячий рефлекс!"
        g4 "О... да..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "Ах... Ах-аха..."
        her "Ты заплатишь за это, скользкий слизери--"
        sly1 "Заткнись, грязнокровка!"
        $ end_u_1_pic =  "images/yule_ball/143.png" #<---- SCREEN
        show screen end_u_1                                                #<---- SCREEN
        with hpunch                                                                        #<---- SCREEN
        
        # DICK IN MOUTH
        call ctc 
        
        her "!!!........................................................."
        sly2 "Круто! Я следующий!"
        her "*Gulp!*"
        sly1 "Отсоси у меня, сучка! Соси я сказал!"
        m "Делай то, что тебе говорят, девочка."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        # SLAP!
        
        m "Ну же!"
        $ end_u_2_pic =  "images/yule_ball/144.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp...*"
        sly1 "Она делает это! Гермиона Грейнджер отсасывает мне, парни!"
        sly2 "Потрясающе! Не могу дождаться своей очереди!"
        sly1 "О... ничего себе... она хороша..."
        her "*Slurp!* *Slurp!* *Gulp!*"
        sly1 "О, да... Да..."
        sly1 "О... Ты так хороша в этом, шлюха!"
        sly1 "Это... Я..."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/145.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!!*{/size}"
        sly1 "{size=+5}Да, да! Глотай все!!!{/size}"
        

        $ end_u_2_pic =  "images/yule_ball/146.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Gulp-Gulp-Gulp-Gulp!*{/size}"
        her "*{size=+3}Gulp-Gulp-Gulp...*{/size}"
        her "*Gulp-Gulp-Gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        $ end_u_1_pic =  "images/yule_ball/147.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Gu-aha..."
        her "Это все, что у тебя есть? Убожество!"
        sly2 "А... Заткнись, шлюха... Ты высосала из меня все соки..."
        $ end_u_2_pic =  "images/yule_ball/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ну же! Кто следующий?!"
        sly2 "Я! Я следующий!"
        $ end_u_1_pic =  "images/yule_ball/148.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch                                                                       #<---- SCREEN
        call ctc 
        
        $ end_u_2_pic =  "images/yule_ball/149.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "О... Да... Да!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly2 "О! Ее рот такой скользкий и теплый!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Да! Отсоси у него, шлюха!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Gulp!* Gulp!* *Slurp!*"
        sly2 "Я не знаю... Как долго..."
        sly2 "...Я смогу продержаться."
        her "*Slurp--Slurp-Slurp-slurp!*"
        her "*Slurp-Gulp-Slurp-Slurp-Gulp!!!*"
        sly2 "О, боже... О, боже..."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        sly2 "Я... Я..."
        sly2 "..................."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        with hpunch
        sly2 "{size=+7}Я кончааааааааю!{/size}"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_2_pic =  "images/yule_ball/150.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!!*{/size}"
        $ end_u_1_pic =  "images/yule_ball/149.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp-Gulp-Gulp-Gulp!*{/size}"
        her "{size=+3}*Gulp-Gulp...*{/size}"
        her "*Gulp....."
        sly2 "Ах... мой член..."
        $ end_u_2_pic =  "images/yule_ball/152.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Gu-aha..."
        $ end_u_1_pic =  "images/yule_ball/151.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Следующий! Ну же! И это все?"
        sly1 "Я следующий, грязнокровка!"
        $ end_u_2_pic =  "images/yule_ball/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=-5}Ах... Не называй меня так, ублюдок...{/size}{image=textheart}"
        sly1 "Я трахну тебя в рот по-настоящему, шлюха!"
        sly1 "И после того, как я наполню твой рот своей спермой, ты поблагодаришь меня!"
        sly1 "Не так ли, шлюха-грязнокровка?"
        $ end_u_1_pic =  "images/yule_ball/153.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Пошел ты!"
        
        # Spit!
        
                
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "images/yule_ball/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        call ctc 

        
        # SPIT!
        $ end_u_1_pic =  "images/yule_ball/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp!*{/size}"
        
        
        
        

        sly1 "Это то, что я подумал!"
        $ end_u_2_pic =  "images/yule_ball/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ты ничтожество...\"слизе-"
        $ end_u_1_pic =  "images/yule_ball/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "?!!"
        $ end_u_2_pic =  "images/yule_ball/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Да! Да, скверная грязнокровка! Соси у меня! Соси!"
        m "Это довольно необычно..."
        sly1 "Сэр?"
        m "Просто..."
        m "Ее киска..."
        $ end_u_1_pic =  "images/yule_ball/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "*Slurp?*"
        m "Она сжимается у нее каждый раз, когда ты называешь ее \"грязнокровкой!\"..."
        m "Попробуй еще раз так ее назвать."
        sly1 "С удовольствием, сэр."
        $ end_u_2_pic =  "images/yule_ball/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Да, шлюха! Мне нравится трахать тебя в \"грязнокровное!\" лицо!"
        sly1 "И тебе нравится это, не так ли?"
        sly1 "Не так ли, грязнокровка?"
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Да... Каждый раз, когда ты это говоришь..."
        m "А?"
        m "Что такое? У нее трясутся ноги!"
        m "Ты кончаешь, моя девочка?"
        $ end_u_1_pic =  "images/yule_ball/157.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "..............................................."
        m "Да!"
        m "Давай, парень, давай немного ускорим процесс!"
        m "Давай трахнем ее с обоих сторон, пока она бьется в оргазме, как грязная шлюха!"
        sly1 "Конечно, сэр."
        sly1 "Возьми его, \"грязнокровная\" шлюха!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3
        g4 "И его!!!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "{size=+7}!!!!!!!!{/size}"
        g4 "Да! Ее киска наполнена соком!"
        sly1 "Ах! А также ее рот, сэр."
        sly1 "Я не знаю, как долго я... о..."
        sly1 "Argh!"
        sly1 "{size=+3}Возьми, шлюха!{/size}"
        
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/159.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!!*{/size}"
        sly1 "{size=+5}Да, да! Проглоти все!!!{/size}"
        

        $ end_u_2_pic =  "images/yule_ball/160.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Gulp-Gulp-Gulp-Gulp!*{/size}"
        her "*{size=+3}Gulp-Gulp-Gulp...*{/size}"
        her "*Gulp-Gulp-Gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        her "....................."
        $ end_u_1_pic =  "images/yule_ball/154.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Gu-aha..."
        sly2 "Ты осушила мои яйца, сучка..."
        m "Ладно, ребята! Давайте доведем эту маленькую вечеринку до достойного завершения."
        her "{size=+7}Я кончаю!{/size}"
        m "Да, что угодно, шлюха."
        m "Так, остальные парни, просто дрочите ей в лицо, хорошо?"
        sly1 "Конечно, сэр."
        sly2 "Да, сэр!"
        m "Да, просто залейте ее лицо спермой. Она любит такое дерьмо!"
        $ end_u_2_pic =  "images/yule_ball/161.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+3}Нет! Я уже начинаю кончать... Хватит!{/size}"
        sly1 "Хех... Гермиона Грейнджер... Какая же ты шлюха!"
        sly2 "Да! Ничего, кроме грязнокровной пизды!"
        her "{size=+9}ААААААА!!!!!{/size}"
        her "{size=+3}Да! Я шлюха! Я шлюха!{/size}"
        sly1 "Она уже сама признается в этом!"
        sly2 "Не думаю, что смогу продержаться долго!"
        sly1 "Я тоже!"
        sly2 "ARGH!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/162.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        call ctc 

        
        her "{size=+8}АААААААААХ!{/size}"
        her "{size=+3}На лицо!{/size}"
        sly1 "Все для тебя, шлюха!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/163.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        call ctc 
        
        her "{size=+5}АААААААААХ!{/size}"
        sly2 "Argh! Вот! Я тоже!"
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/164.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        call ctc 
        
        $ end_u_2_pic =  "images/yule_ball/165.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        call ctc 
        
        her "{size=+4}Я кончаю!{/size}"
        m "Ну, не возражаешь, если и я тоже!"
        $ end_u_1_pic =  "images/yule_ball/166.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "{size=+3}No professor, I............!{/size}"
        her "{size=+3}Нет [genie_name], Я............!{/size}"
        g4 "Argh!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/167.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        call ctc 
        
        her "{size=+8}АААААААААХ!{/size}"
        $ end_u_2_pic =  "images/yule_ball/168.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Нет! Мое лицо! Моя киска! Ах! Я не перестаю кончать!!!{/size}"
        sly1 "Какая же все-таки она шлюха!"
        sly2 "Шлюха!"
        sly1 "Грязнокровка!"
        her "{size=+8}АААААААААХ!{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "images/yule_ball/169.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        call ctc 
        
        $ end_u_2_pic =  "images/yule_ball/170.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+8}*Gulp!*{/size}"
        $ end_u_1_pic =  "images/yule_ball/168.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        her "{size=+8}Я схожу с ума!{/size}"
        
        # SPIT!
        call ctc 
        
        show screen white
        with d9
        pause 1
        
        
        # WHITE FADE
        
        ">..............{w}..................{w}...................."
        
        # Character sprites.
        
        m "Ну, спасибо за содействие, парни"
        sly1 "Конечно, сэр, профессор Дамблдор."
        sly2 "Рад быть полезным, сэр."
        sly1 "Благодарю вас, профессор."
        sly2 "Хорошо, давайте вернемся на бал?"
        sly1 "Да, пойдем!"
        sly2 "Пока, грязнокровка шлюха!"
        sly1 "Да, спасибо, что была такой шлюхой!"
        call her_head("..........................","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        $ renpy.play('sounds/footsteps.mp3') #Walking away sound
        # Walking away sound...."
        
        $ end_u_1_pic =  "images/yule_ball/02.png" #<---- SCREEN
        
        pause 2
        
        hide screen white
        with d9
        
        sly1 "{size=-4}(Парни, профессор Дамблдор - классный чувак.){/size}"
        sly2 "{size=-4}(Да... Кто бы мог подумать.){/size}"
        sly1 "{size=-4}(Верно. Я не могу не уважать этого человека...){/size}"
        m "Ай... Какие классные парни..."
        sly2 "{size=-4}(Да... Надеюсь, я буду таким же проворным, как он, когда стану таким же древним.){/size}"
        g4 "Я не древний, неопытные юнцы!"
        m "Хотя, полагаю, в каком-то смысле..."
        
        call her_head("..........................","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Шлюха! Чего притихла?"
        call her_head("Я...","silly","ahegao",cheeks="blush",tears="mascara_soft") 
        call her_head("Я... не уверенна...") 
        call her_head("Что...? Что.......","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Давай же девочка. Возьми себя в руки!"
        call her_head("Я... я... Что?","open","concerned",cheeks="blush",tears="mascara_soft") 
        call her_head("Я не понимаю... я...") 
        m "Хм..."
#        m "Doesn't look like you are in any condition for serious talks..."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "characters/hermione/face/body_178.png" # HERMIONE
#        her "Serious talks?"
#        hide screen h_head2
#        m "Well, so be it, then."
#        m "I wrote you a letter."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "characters/hermione/face/body_177.png" # HERMIONE
#        her "A letter...? What...? I...."
#        hide screen h_head2
#        m "Yes! Concentrate for a second, would you?"
#        m "I wrote you a letter. It should explain a couple of things."
        m "Я собираюсь уходить."
        call her_head("Уходить...?","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Да. Может быть, тебе тоже стоит..."
        m "Иди приведи себя в порядок и отдохни."
        call her_head("Но я не могу уйти... нет... я должна...","open","concerned",cheeks="blush",tears="mascara_soft") 
        call her_head("Главный танец... я должна...") 
        m "Танец? Ты не можешь танцевать в таком состоянии."
        call her_head("Нет! Я Королева бала! Я должна....","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Хорошо, делай как хочешь."
        m "А я ухожу..."
        call her_head("До свидания... сэр...","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "............."
        m "Прощай, девочка."
        call ctc 
        
        show screen blkfade 
        $ end_u_2_pic =  "images/yule_ball/90.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d9                                                                        #<---- SCREEN
        pause.5
        hide screen blkfade
        with d5
        
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        call ctc 
        
        m "Хм..."
        m "Может мне остаться и посмотреть на танцы Гермионы после множественного оргазма?"
        m "Нет... Бал почти закончился. Это мой единственный шанс улизнуть незамеченным."
        call ctc 
        
        show screen blkfade 
        with d7
        pause.5
    
    else: # Ending "Your whore".
        $ snape_head_xpos = 330 # x = 330,
        $ snape_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        $ s_sprite = "characters/snape/main/snape_03.png"
        show screen s_head2
        sna "Мисс Грейнджер...?"
        $ s_sprite = "characters/snape/main/snape_04.png"
        sna "Вы все-таки решили появиться? Какой неприятный сюрприз..."
        call her_head("...............................","full","ahegao",cheeks="blush",tears="mascara") 
        $ s_sprite = "characters/snape/main/snape_13.png"
        show screen s_head2
        sna "Что с вашим лицом, девочка?"
        call her_head(".......................................","full","down",cheeks="blush",tears="mascara") 
        $ s_sprite = "characters/snape/main/snape_13.png"
        show screen s_head2
        sna "Хм... Хорошо, тогда продолжайте..."
        sna "Вот тиара..."
        sna "И сцена в вашем распоряжении..."
        hide screen s_head2
        pause.7
        
        
        
        $ end_u_2_pic =  "images/yule_ball/37.png" #<---- SCREEN
        hide screen blkfade
        with d7
        
        $ renpy.play('sounds/applause01.ogg')
        call ctc 
        
        her "..............."
        her ".................................."
        her ".........................................................................."
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "images/yule_ball/38.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "А-а.........................................."
        show screen bld1
        with d5
        m "Это...?"
        m "остатки спермы у нее во рту?"
        g4 "Что, черт возьми, она делает?"
        hide screen bld1
        with d5
        
        $ end_u_2_pic =  "images/yule_ball/39.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "...................................."
        her "Пивет хем..." #Misspelled on purpose.
        $ end_u_1_pic =  "images/yule_ball/40.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Хахифо фам фа хефоняий фефе..." #Misspelled on purpose.
        show screen bld1
        with d5
        m "Я едва могу понять, что она говорит..."
        hide screen bld1
        with d5
        her "Херфа я хофу фофлахафафить фофефофа Фамлфора..." #Misspelled on purpose.
        show screen bld1
        with d3
        m "Меня?"
        hide screen bld1
        with d3
        her "................"
        $ end_u_2_pic =  "images/yule_ball/37.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        stop music fadeout 1.0
        her ".................................................."
        call ctc 
        
        $ end_u_1_pic =  "images/yule_ball/41.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        $ renpy.play('sounds/Gulp.mp3') #Sound of Gulping down a liqui
        her "{size=+5}*Gulp!!!*{/size}"
        $ end_u_2_pic =  "images/yule_ball/42.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Gua-ha..."
        #her "Thank you, professor."
        her "Спасибо вам, [genie_name]."
        show screen bld1
        with d3
        with hpunch
        g4 "ВОТ ШЛЮХА!!!"
        g4 "Когда ты успела так развратиться!"
        #m "Now I want to fuck you... Dammit."
        hide screen bld1
        with d3
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "images/yule_ball/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Я также хотела поблагодарить своих родителей..."
        her "Так же я хотела поблагодарить моих сокурсников!"
        show screen bld1
        with d3
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Громкие возгласы и свист..."
        hide screen bld1
        with d3
        her "И конечно же, наших преподавателей..."
        $ end_u_2_pic =  "images/yule_ball/44.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        show screen bld1
        with d3
        ">Немного слабых аплодисментов..."
        hide screen bld1
        with d3
        call ctc 
        
        show screen blktone
        with d5
        
        mal "(Так это Гермиона Грейнджер снова и в этом году...)"
        fem "(... Почему же я не удивлена?)"
        mal2 "(Может быть, потому, что она этого заслуживает?)"
        mal "(Да! Перестань ненавидеть Гермиону!)"
        fem "(...Мне все равно.)"
        mal "(Кстати, когда Гермиона вышла на сцену...)"
        mal2 "(Да, что-то было у нее во рту. Я тоже обратил на это внимание.)"
        fem "(Бьюсь об заклад, это была чья-то сперма!)"
        mal "(ЧТО?!!)"
        mal2 "(Вытащи голову из сточной канавы, девочка!)"
        fem "(Почему нет?)"
        fem "(Все знают, что она спит с профессором Дамблдором!)"
        mal "(Нет, только давай без этих сплетен.)"
        mal2 "(Подожди, я хочу послушать. Расскажи подробнее.)"
        fem "(Что тут рассказать?)"
        fem "(Гермиона Грейнджер-шлюха. Она любит сосать члены....)"
        fem "(Да, она любит сосать члены, но еще больше любит сперму!)"
        mal "(....)"
        fem "(Она спермоманка! Она должна проглотить по полстакана спермы каждый день...)"
        fem "(Потому что, если она этого не сделает, у нее будет сексуальное влечение...)"
        mal2 "(.....)"
        fem "(И когда это случится, она не сможет себя контролировать и с радостью переспит с первым встречным.)"
        mal "(.............)"
        mal2 "(.....................)"
        fem "(Хм? Почему ты так на меня смотришь?)"
        mal "(Что? Я не смотрел.)"
        mal2 "(Да, продолжай рассказывать. У тебя хорошо получается!)"
        fem "(Хорошо в чем?!)"
        fem "(Погодите-ка, мальчики, и вам это нравится?)"
        mal "(Хех... Посмотри на ворону, зовущую ворона черным!)"
        fem "(Что вы имеете в виду?)"
        mal2 "(Ты краснеешь как сумасшедшая, девочка! И твои глаза бешено забегали!)"
        mal "(Да! Ты наслаждаешься этим так же, как и мы!)"
        fem "(?!!!)"
        fem "Вы мальчики, идиоты!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        mal "(Что? Что я сказал такого?)"
        mal2 "(Кто знает, бро? Сучки бывают сумасшедшими...)"
        mal "(Они действительно сумасшедшие...)"


        
        hide screen blktone
        with d5
        $ end_u_1_pic =  "images/yule_ball/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Спасибо всем за то, что помогли организовать сегодняшнее мероприятие."
        her "И спасибо, что снова выбрали меня своей королевой в этом году..."
        $ end_u_1_pic =  "images/yule_ball/45.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Какой приятный, но совершенно неожиданный сюрприз...!"
        her "И еще один момент..."
        $ end_u_2_pic =  "images/yule_ball/43.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "{size=+5}Вперед, Гриффиндор!{/size}"
        show screen bld1
        with d5
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Толпа взрывается с громкими аплодисментами и свистом, со случайным окриками..."
        hide screen bld1
        with d5
        call ctc 
        
        show screen blkfade
        with d7
        pause.7
        stop music fadeout 1.0
        m "Великолепная речь..."
        m "Очень возбуждающе... Я имею в виду вдохновляюще."
        $ tiara = True #Tiara is displayed.
        call her_head("Благодарю вас, сэр.","soft","glanceL",cheeks="blush") 
        m "Глотание спермы перед всей школой?"
        g9 "Очень приятно."
        call her_head("........................................................","crooked_smile","worriedCl",cheeks="blush") 
        
        call play_music("playful_tension") # SEX THEME.
        
        $ end_u_2_pic =  "images/yule_ball/02.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        with d3
        show screen bld1 
        with d3
        m "Хорошо, девочка. Давай хоть сейчас поговорим..." 
        call her_head("....................","upset","base") 
        m "Мне нужно тебе кое-что сказать..."
        m "Не уверен, с чего начать..."
        m "........................................"
        m "Ну, во-первых, я... --"
        call her_head("Сэр, думаю, я точно знаю, что вы собираетесь сказать.","open","base") 
        m "Ты?"
        call her_head("Конечно.","open","base") 
        call her_head("Одного быстрого минета недостаточно, чтобы вернуть мой долг, я права?","base","glance",cheeks="blush") 
        m "Что? Нет, это не то, что я--"
        call her_head("Все в порядке, сэр. Правда.","base","glance",cheeks="blush") 
        call her_head("Позвольте мне немного стянуть трусики...","soft","glanceL",cheeks="blush") 
        g4 "Будь ты проклята! Ты позволишь мне закончить?!"
        call her_head("Конечно, сэр...","base","glance",cheeks="blush") 
        m "А?"
        call her_head("Просто убедитесь, что не испортите мое платье, хорошо?","open_tongue","concerned",cheeks="blush") 
        g4 "*Low growl!*"
        g4 "Иди сюда, шлюха!"
        g4 "Предположим, я могу трахнуть тебя в последний раз!"
        call her_head("(В последний раз?)","upset","base") 
        call ctc 
        
        show screen blkfade 
        with d7
        
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        $ her_head_ypos = her_head_only
        call her_head("{size=+5}Ахх!!!{/size}","open","surprised",cheeks="blush",tears="soft") 
        g4 "О, да!"
        
        $ end_u_2_pic =  "images/yule_ball/46.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        hide screen bld1
        with d7
        call ctc 
        
        her "Ах-ах..."
        m "Хм? Твоя киска..."
        m "Она мокрая, девочка."
        $ end_u_1_pic =  "images/yule_ball/47.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах...{image=textheart} Так и есть, сэр?"
        her "Наверное, это было до..."
        m "До...?"
        m "Ты имеешь в виду, когда ты чуть не подавилась моим членом?"
        her "Ах...{image=textheart} Да, сэр..."
        m "Ты кончила?"
        $ end_u_2_pic =  "images/yule_ball/48.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Малость..."
        m "Ну, тогда ты просто прелесть, не так ли?"
        her "Ах......"
        m "Разве не так, шлюха?!"
        her "Ах... Как скажите, сэр."
        m "Да, ты прелестная шлюха!"
        $ end_u_1_pic =  "images/yule_ball/49.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "............."
        m "Сжимаешь мой член своей узенькой киской!"
        her "......................"
        m "Хм...?"
        m "Чего молчишь?"
        $ end_u_2_pic =  "images/yule_ball/51.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "О... Я просто боюсь, что кто-нибудь--"
        m "Я думаю, это потому, что ты хочешь, чтобы тебя отшлепали!"
        her "Что?!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        
        $ end_u_2_pic =  "images/yule_ball/52.png" #<---- SCREEN
        #show screen end_u_2                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN
        her "EEeeeeeeeegh!"
        m "Тихо, шлюха! Кто-нибудь услышит!"
        $ end_u_1_pic =  "images/yule_ball/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, Я--"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/54.png" #<---- SCREEN
        #show screen end_u_1                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN

        her "{size=+7}EEghh!!!{/size}"
        m "Тихо, я сказал!"
        m "Или ты хочешь быть пойманной? На члене своего директора?"
        m "Ты, мисс Королева осеннего бала?"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/55.png" #<---- SCREEN
        her "Да..."
        m "Да, тебе это нравится не так ли?!"
        $ end_u_2_pic =  "images/yule_ball/56.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her ".............."
        g4 "Отвечай, шлюха!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "images/yule_ball/55.png" #<---- SCREEN
        her "Да, сэр! Мне это нравится!!!"
        $ end_u_1_pic =  "images/yule_ball/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Отшлепайте меня сильнее, сэр! Я заслужила это!"
        m "Вот это хватка!"
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/55.png" #<---- SCREEN
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/55.png" #<---- SCREEN
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/58.png" #<---- SCREEN
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/58.png" #<---- SCREEN
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "images/yule_ball/59.png" #<---- SCREEN
        call ctc 
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "images/yule_ball/59.png" #<---- SCREEN
        call ctc 
        
        her "{size=+7}Aaaaaah............................{/size}"


        show screen blktone
        with d3
        sna "Внимание, бездари!"
        sna "\"Осенний Бал В Хогвартсе\". Главный танец вот-вот начнется..."
        hide screen blktone 
        with d3
        
        $ end_u_2_pic =  "images/yule_ball/60.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        her "Танец! Я же совсем забыла!!!"
        $ end_u_2_pic =  "images/yule_ball/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, простите, но вам придется меня отпустить..."
        g4 "Ах... Твоя киска-это нечто!"
        her "Сэр... Ах... Я серьезно."
        her "Как королева, я должна возглавлять танцы."
        g4 "Да... Вот так, просто вот так... О, да."
        $ end_u_1_pic =  "images/yule_ball/62.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, вы вообще слушаете?"
        m "О, я тебя прекрасно слышу. И позволь мне сделать тебе встречное предложение."
        $ end_u_2_pic =  "images/yule_ball/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр?"
        m "Вместо того, чтобы отпустить тебя..."
        m "Я засуну свой член тебе в попку."
        m "А? Как насчет этого?"
        her "Что? Н-но..."
        m "Я думаю, что это отличная мысль!"
        her "Сэр, нет! Я--"
        m "Секундочку, секундочку..."
        show screen blkfade
        with d7
        m "Позволь я сперва вытащу свой член из твоей киски..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        call her_head("Ах...","open","surprised",cheeks="blush",tears="soft") 
        call her_head("Сэр, нет. Вы должны выслушать мен--","open_tongue","concerned",cheeks="blush") 
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        # INSERTION
        call her_head("{size=+7}!!!!!!!!!!!!!!!!!{/size}","scream","surprised",cheeks="blush",tears="soft") 
        call her_head("Мой...{w} Мой...{w} Мой...") 
        m "Заткнись, девчонка! Ты слишком много болтаешь."
        with hpunch
        call her_head("{size=+7}Мой анус!!!!!!!!!!!!!{/size}","scream","surprised",cheeks="blush",tears="soft") 
        g4 "Черт возьми, девочка. Я сказал, будь потише."
        
        $ end_u_2_pic =  "images/yule_ball/63.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        hide screen blkfade 
        with d9
        her "{size=+7}Я не могу! Мне все равно, больно!!!{/size}"
        g4 "Может, тебе все равно, но мне не все равно, шлюха!"
        $ end_u_1_pic =  "images/yule_ball/64.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}У вас такой огромный член!{/size}"
        g4 "Нас застукают из-за тебя, тупая шлюха!"
        m "Может, это поможет тебе заткнуться..." 
        
        # Fishhooking.
        $ end_u_2_pic =  "images/yule_ball/65.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!............"
        g4 "Все правильно, шлюха. Молчи!"
        $ end_u_1_pic =  "images/yule_ball/66.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah... Blah..."
        g4 "Твоя анальная дырочка... Она такая чертовски тугая..."
        $ end_u_2_pic =  "images/yule_ball/67.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... вздор... ах..."
        g4 "Ты пускаешь слюни но мою руку, грязная шлюха!"
        her "Ах... вздор-взвдор... ах... взд-ах..."
        
        show screen blktone
        with d5
        stop music fadeout 1.0
        sna "Что ж, мы собираемся начинать..."
        sna "Разбейтесь на пары прямо сейчас..."
        sna "Нет! Пары, это когда парень-девушка, тупая милюзга. Как вы думаете, что сейчас? Уроки? Лабораторное задание?"

        hide screen blktone
        with d5
        $ end_u_1_pic =  "images/yule_ball/69.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with fade                                                                    #<---- SCREEN
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        m "Не переживай, что пропустишь свой танец, шлюха."
        m "Мы немного потанцуем сами по себе..."
        her "Ах..."
        m "Да. В этом году королева бала исполняет сложный пируэт с членом вставленным глубоко в ее узенькую попку!"
        $ end_u_2_pic =  "images/yule_ball/69.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... я, я ахх..."
        m "Вы что-то сказали, ваше Величество?"
        her "Ах... Я королева осеннего бала... ах..."
        m "Ну конечно, ты!"
        m "Но ты еще и шлюха!"
        $ end_u_1_pic =  "images/yule_ball/68.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Я шлюха..."
        $ end_u_2_pic =  "images/yule_ball/70.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}Я шлюха!!!{/size}"
        $ end_u_1_pic =  "images/yule_ball/71.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}Я шлююююююююха!!!{/size}"
        g4 "Да, ты такая!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        $ end_u_1_pic =  "images/yule_ball/72.png" #<---- SCREEN
        with hpunch
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Да, ты такая!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Да, ты такая!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "images/yule_ball/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5} Я кончаю!!!{/size}"
        
        with hpunch
        g4 "Argh! Мой член!"
        $ end_u_1_pic =  "images/yule_ball/74.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}Я КОНЧАЮ! Я шлюха!{/size}"
        g4 "Я больше не могу сдерживаться!"
        her "{size=+10}Я КОНЧАЮ!{/size}"
        
        
        g4 "Мой член застрял в твоей попке, шлюха!"
        her "{size=+10}Я шлюююха!!!{/size}"
        g4 "Я сказал, расслабься немного, черт возьми!"
        $ end_u_2_pic =  "images/yule_ball/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}Я не могу! Я кончаю!!!{/size}"
        g4 "Отлично! Пусть будет по-твоему. Тогда я пальчиком по массирую твою киску."
        $ end_u_1_pic =  "images/yule_ball/75.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "А?"
        # POP
        
        show screen blkfade
        with d7
        g4 "Не могу вытащить!"
        g4 "Расслабь свой чертов анус, девочка!..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        call her_head("...........","angry","ahegao",cheeks="blush",tears="messy") 
        m "Вот..."
        
     
    #    $ renpy.play('sounds/gltch.mp3')
    #    with hpunch
    #    with kissiris
        
    #    # INSERTION
    #    show screen h_head2                                                             # HERMIONE
    #    $ h_body = "characters/hermione/face/body_175.png" # HERMIONE
    #    her "{size=+7}!!!!!!!!!!!!!!!!!{/size}"

        
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $ end_u_1_pic =  "images/yule_ball/77.png" #<---- SCREEN
        hide screen blkfade
        with d5
        # INSERTION
        her "{size=+10}АААААААХ!!{/size}"
        her "Моя киска, снова..."
        g4 "Да, шлюха!"
        $ end_u_2_pic =  "images/yule_ball/79.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Я опять кончаю!"
        her "Что со мной происходит, сэр?!"

        m "Расслабься, девочка, я знаю, что делаю!"
        m "Это нормально для шлюхи."
        $ end_u_1_pic =  "images/yule_ball/78.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Нет! Я сойду с ума!!!{/size}"
        g4 "Не сойдешь. Все будет в порядке."
        g4 "Наслаждайся ощущениями, пока я продолжаю тереть твою киску!"
        her "{size=+5}Ах!!!{/size}"
        
        $ end_u_2_pic =  "images/yule_ball/81.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}О!!!{/size}"
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Да, это так!"
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Верно!"
        g4 "О... Я думаю, что сам скоро..."
        g4 "Argh!"
        $ d_flag_01 = False #Came into pussy
        $ d_flag_02 = False #Came into asshole
        
        $ menu_x = 0.5 #Menu is moved to the left side.

                    
        menu:
            "-Кончить в киску Гермионе-":
                $ d_flag_01 = True #Came into pussy
                g4 "Думаешь, твоя киска готова к этому, шлюха?!"
                her "Сэр?!"
                g4 "Возьми все!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                $ end_u_2_pic =  "images/yule_ball/86.png" #<---- SCREEN
                with hpunch
                her "{size=+5}Ах! Ааааах!!{/size}"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                
               
                her "{size=+5}Ах! Я чувствую это! Это так горячо!{/size}"
                g4 "Argh! Да!"
                $ end_u_1_pic =  "images/yule_ball/87.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                
                
                
                
                her "{size=+5}Она заполняет меня! Она заполняет меня!!!{/size}"
                g4 "Да! Шлюха! Я накачаю до краев твое британское влагалище своей спермой!"
                
              
                
                $ end_u_2_pic =  "images/yule_ball/88.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                #her "Professor! My dress!"
                her "[genie_name]! Мое платье!"
                g4 "Что?"
                her "Будьте аккуратны, не запачкайте мне платье!"
                g4 "Заткнись со своим платьем, шлюха! Ты портишь такой момент!"
                $ end_u_1_pic =  "images/yule_ball/87.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Простите меня! Ваша шлюха просит прощения!!!!{/size}"
                g4 "Да! Так намного лучше!"
                g4 "О......."
        
            "-Кончить в попку Гермионе-":
                $ d_flag_02 = True #Came into asshole.
                g4 "Твоя задница должна быть готова к этому, шлюха!"
                her "Что?!"
                $ renpy.play('sounds/gltch.mp3')
                
                pause.5
                her "Ах..."
                
                #Pop
                
                #INSERTION
                $ renpy.play('sounds/boing.mp3') #Sound of # POP!
                with hpunch
                with kissiris
                $ end_u_1_pic =  "images/yule_ball/82.png" #<---- SCREEN
                show screen end_u_1                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+10}Ахх!!!{/size}"
                her "{size=+5}Все опять в моей попе!{/size}"
                $ end_u_2_pic =  "images/yule_ball/81.png" #<---- SCREEN
                show screen end_u_2                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Нет, сэр, пожалуйста! Не кончайте мне в анус!{/size}"
                her "{size=+5}Нет, я умру!!!{/size}"
                g4 "Ты не умрешь, глупая девчонка."
                g4 "Это будет сумасшедший оргазм. Может быть, даже отключишься на некоторое время, но не более..."
                her "Нет, сэр, пожалуйста... Я боюсь..."
                g4 "Возьми все, шлюха!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                
                $ end_u_1_pic =  "images/yule_ball/82.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Ах! Я чувствую это!!!{/size}"
                g4 "Argh! Да!"
                $ end_u_2_pic =  "images/yule_ball/83.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Это заполняет меня! Она заполняет меня!!!{/size}"
                g4 "Да! Шлюха! Я накачаю тебя своей спермой!"
                $ end_u_1_pic =  "images/yule_ball/84.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                #her "Professor! My dress!"
                her "[genie_name]! Мое платье!"
                g4 "Что?"
                her "Будьте аккуратны, не запачкайте мне платье!"
                g4 "Заткнись со своим платьем, шлюха! Ты портишь такой момент!"
                $ end_u_2_pic =  "images/yule_ball/85.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Простите меня! Ваша шлюха очень сожалеет!!!!{/size}"
                g4 "Да! Так намного лучше!"
        
                
        $ her_head_ypos = her_head_tits
        call ctc 
        
        show screen blkfade
        with d9
        stop music fadeout 1.0
        call her_head("Ах...","silly","ahegao",cheeks="blush",tears="mascara_soft") 
        call her_head("Я едва... могу... стоять...") 
        g4 "Я знаю, что ты имеешь в виду, девочка."
        g4 "Это была наша самая интенсивная ебля!"
        call her_head("Да... Я никогда не знала, что могла...","silly","ahegao",cheeks="blush",tears="mascara_soft") 
        call her_head("...оргазм такой сильный...") 
    #    her "But I must, go... The dance..."
    #    m "Go then..."
        call her_head("Сэр... Так, что вы хотели обсудить со мной..?","soft","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Да... Знаешь? Я написал тебе небольшое письмо по этому поводу..."
        call her_head("Письмо?","open","concerned",cheeks="blush",tears="mascara_soft") 
        m "Да... Оно должно объяснить некоторые моменты..."
        call her_head("О... Хорошо...","silly","ahegao",cheeks="blush",tears="mascara_soft") 
        m "Просто прочти его завтра утром..."
        m "Или когда угодно..."
        m "Или вообще не читай, мне все равно..."
        g4 "............."
        call her_head("Сэр...?","base","worried",cheeks="blush",tears="mascara") 
        m "Прекрати так смотреть! Ты заставляешь меня чувствовать себя неловко..."
        m "Я написал тебе письмо, и что с того?"
        call her_head("Я думаю, что это так мило.............","base","worried",cheeks="blush",tears="mascara") 
        g4 "Я сказал, хватит так на меня пялиться, девочка. Я думал, ты опаздываешь на танцы или куда то еще!"
        call her_head("ТАНЦЫ!","open","wide",cheeks="blush",tears="mascara") 
        call her_head("Простите, мне нужно идти!") 
        call her_head("Увидимся позже, сэр!") 
        
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "......................"
        m "Нет, не увидимся......."
        m "Прощай... Гермиона..."
        pause.7
        ">..............{w}..................{w}...................."
    
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        
        if d_flag_01: #Came into pussy
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "images/yule_ball/89.png" #<---- SCREEN
        else:
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "images/yule_ball/90.png" #<---- SCREEN
            
        ">Ты ненадолго задержишься..."
        ">Смотришь, как Гермиона участвует в главном танце..."
        hide screen blkfade
        with d7
        call ctc 
        
        ">Без сомнения, она устала и измучена, но она хорошо скрывает это..."
        show screen bld1
        with d5
        m "(Хм... Эта девочка действительно сильная...)"
        m "(Во всех смыслах этого слова...)"
        hide screen bld1
        with d5
        if d_flag_01: #Came into pussy
            ">Ты замечаешь крошечный поток блестящей жидкости, стекающей по ее ляшкам, незаметный для всех..."
        elif d_flag_02: #Came into asshole.
            ">Ты заметил, что она сжимает ягодицы время от времени."
            ">Вероятно, делает все возможное, чтобы сдержать внутри все, что ты спустил ей в ее анус всего минуту назад..."
        show screen bld1
        with d5
        m "................................................."
        m "..............."
        m "(Я лучше пойду...)"
        hide screen bld1
        with d5
        call ctc 
    
    
    #FINAL SCENE. GENIE IS LEAVING.
    
    
    
    show screen blkfade
    with d7
    pause 1
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Окраина Хогвартса{/color}{/size}"

    #Night interface.
    $ interface_color = "gray"
    
    $ end_u_1_pic =  "images/yule_ball/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    hide screen blkfade 
    with d7
    
    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    call ctc 
    
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRESS.
    m "......."
    pause.5
    
    $ end_u_3_pic =  "images/yule_ball/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    
    
    m "Ну, теперь мне действительно пора уходить..."
    
    $ end_u_4_pic =  "images/yule_ball/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    
    m "До свидания мир дикой магии..."
    m "Прощай моя шлю--......"
    m "Прощай, Гермиона..."
    m "............"
    m "......"
    
    $ renpy.play('sounds/magic4.ogg')
    with hpunch
    $ end_u_3_pic =  "images/yule_ball/174.png" #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    $ end_u_4_pic =  "images/yule_ball/175.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    call ctc 
    
    show screen blktone
    with d7
    
    show screen blktone8
    with d7
#    $ end_u_4_pic =  "title/title2.jpg" #<---- SCREEN
#    show screen end_u_3                                           #<---- SCREEN
#    with fade                                                                     #<---- SCREEN
    
    
#    show screen blkfade 
#    with d9
    pause .5
    
    
    ## FINAL CREDITS ###
    stop music fadeout 1.0
    if public_whore_ending: # PUBLIC WHORE ENDING
        centered "{size=+7}{color=#cbcbcb}Поздравляем с завершением игры!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}Это концовка \"02\" из \"02\".{/color}{/size}"
    else: # YOUR PERSONAL WHORE
        centered "{size=+7}{color=#cbcbcb}Поздравляем с завершением игры!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}Это концовка \"01\" из \"02\".{/color}{/size}"
        
    hide screen blktone8
    with d7
    
    play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 # ORANGE RANGE THEME.
    
    
    #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
    #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
    #scene image "08_ending/e05.png" with Dissolve(2)
    # show akaani with d5
    #$ dermo = "genie_attack"
    #$ dermo = "snape_attack_guard"
    $ dermo = "ch_sna defend"
    
    show screen credits_chibi
    centered "{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n
    {color=#e5e297}-\{Руссификация Silver mod\}-{/color}\n   {size=+5}{color=#cbcbcb}REd Machine Translators Team(REM TT):{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}wasya2009 from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Copycat from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}RuGamerPro from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}lilpeep from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Heresy from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Wentseeking from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}palad1n_ from - {/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Satna from - {/color}{/size}\n\n
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"
    

    
    
    #nvl clear


    #$ dermo = "ch_hem run_f"
#    $ dermo = "jerking_off_03_ani"
#    show screen credits_chibi
   
  
    $ xder = 160
    $ yder = 160
    $ dermo = "jerking_off_03_ani"
    show screen uni_cr
    hide screen credits_chibi
   
    
    
    
    centered "{cps=40}{size=+5}{color=#e5e297}-\{Sound Effects\}-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n
              
    {size=+5}{color=#e5e297}-\{Music provided by\}-{/color}{/size}\n    {color=#cbcbcb}http://incompetech.com/{/color}\n\n
    
    
    
    
    {size=+5}{color=#e5e297}-\{MUSIC\}-{/color}{/size}\n

              

    {color=#e5e297}\"(Orchestral) Playful Tension\" {/color}{color=#cbcbcb}by Shadow16nh.{/color}\n
    {color=#e5e297}\"Prologue\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Shanghai Honey\"{/color} {color=#cbcbcb}by orange range.{/color}\n
    {color=#e5e297}\"Introducing Colin\"{/color} {color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Neville's Waltz\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"The Quidditch Match\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Anguish\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Awkward Meeting\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Brittle Rille\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Chipper Doodle v2\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Dark Fog\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Despair\" {/color}{color=#cbcbcb}by erenik.{/color}\n
    {color=#e5e297}\"Game Over Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Boss Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Hitman\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Music for Manatees\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Plaint\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Under-the-Radar\" {/color}{color=#cbcbcb}by  PhobyAk.{/color}{/cps}"
 
    
    $ xder = 670
    $ yder = 410
    $ dermo = "ch_hem run_f"
    #$ dermo = "no_shirt_dance_ani"
    #nvl clear

    centered "{cps=40}{size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n{color=#cbcbcb}
    {size=+5}Dahr{/size}{/color}\n{color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n
    {color=#cbcbcb}{size=+5}Xaljio{/size}{/color}\n{color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n
    {color=#cbcbcb}{size=+5}Lyk.D9 (a.k.a. Silentchill){/size}{/color}\n {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar. {/color}\n\n
    {color=#cbcbcb}{size=+5}Bookfisher{/size}{/color}\n{color=#e5e297}For everything.\n\n
    {color=#cbcbcb}{size=+5}The fate (universe or higher power){/size}{/color}\n{color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.\n\n\n
              
    {color=#cbcbcb}{size=-1}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.\n\n\n
              
    {/color}{/size}{/cps}"

    hide screen uni_cr
    
    #nvl clear

    centered "{cps=70}{color=#cbcbcb}Это не коммерческая видеоигра. Весь проект был самостоятельно основан исключительно через\nhttp://www.patreon.com/ и\nby \"Hentai United\" подписчиками.{/color}\n\n\n
    
    {size=-1}{color=#e5e297}-People who supported development of this game with extraordinary amount of money-{/size}\n
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n
              
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/size}\n
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n
    
                        
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/size}\n
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, 
Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/size}\n\n{/cps}"
         
         
    #nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}"
    
    #nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n
              
              
              
    
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n
              
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}"
              
              
              
              
              
              
    pause 1
    call ctc 
    
    show screen blkfade
    with d9
    stop music fadeout 3.0
    ">..............{w}..................{w}...................."
    pause.5
    centered "{size=+7}{color=#cbcbcb}На следующее утро...{/color}{/size}"
    
    #Set Daytime.
    $ daytime = True
    $ interface_color = "gold"
    
    $ h_request_wear_hat = False
    $ hermione_wear_hat = False
    $ h_hair_style = "A"
    
    call h_outfit_OBJ(None) #Updates uniform.
    call reset_hermione_main 
    
    hide screen end_u_1                                           #<---- SCREEN
    hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    hide screen blktone
    hide screen blktone8
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_near_fire
    hide screen chair_left
    hide screen candlefire
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    
    $ show_weather()
    show screen weather
    
    show screen main_room
    show screen chair_right
    show screen fireplace

    hide screen genie
    hide screen owl
    hide screen owl_02
    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.

    
    show screen chair_right
    show screen dumbledore

    hide screen blkback
    hide screen blkfade
    with d9
    
    
    if public_whore_ending: # PUBLIC WHORE ENDING
    
        call play_sound("door") #Sound of a door opening.
        call sna_chibi("stand","door","base") 
        pause.8
        
        call sna_walk("door","mid",2) 
        pause.8
       
        call bld 
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
        dum_[1]"Доброе утро, Северус."                                                                                     # SNAPE
        call sna_main(".......................................","snape_09",xpos="base",ypos="base") 
        hide screen s_head2              
        dum_[1]"У меня есть самая необычная история, которой я хочу поделиться с тобой, мой старый друг."                                                                                               # SNAPE
        sna "......................................" 
        dum_[1]"Но прежде чем я это сделаю..."                                                                                               # SNAPE
        sna "........................................"
        dum_[2] "Эм... Северус?"                                                                                              # SNAPE
        sna "........................................."                                                                                               # SNAPE
        call sna_main("Кто рулит?","snape_06") 
        dum_[2] "Прошу прощения?"                                                                                                # SNAPE
        call sna_main("Кто рулит?",snape_26) 
        dum_[2] "...рулит чем?"                                                                                               # SNAPE
        sna "А...?"    
        dum_[2] "А?"                                                                                             # SNAPE
        call sna_main("Aka-a....?","snape_27") 
        dum_[2] "В этом нет никакого смысла, Северус."                                                                                             # SNAPE
        call sna_main("А, черт возьми...................","snape_29") 
        pause.5
        call ctc 
        
        stop music fadeout 1.0
        
        hide screen snape_main
        hide screen bld1
        show screen blkfade
        with d7
        pause.1
        
    
    else: # PERSONAL WHORE ENDING 
    
        call play_sound("door") #Sound of a door opening.
        call her_chibi("stand","door","base") 
        pause.8
        
        call her_walk("door","mid",3) 
        pause.8
        
        call bld 
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        
        call her_main("Сэр, если это о вчерашнем...","upset","closed",xpos="right",ypos="base") 
        her "Сэр, вы хотели меня видеть?"
        dum_[1]"Доброе утро, Мисс Грейнджер."
        call her_main("Не то, чтобы мне это понравилось или что-то в этом духе...","annoyed","annoyed") 
        dum_[1]"Мисс Грейнджер, я нашел это письмо на своем столе..."
        dum_[1]"Оно адресовано вам..."
        call her_main("Письмо, сэр?","soft","base") 
        call her_main("О, конечно! Которое вы написали для меня, сэр.","grin","worriedCl",emote="05") 
        dum_[1]"Это письмо не от меня, мисс Грейнджер."
        call her_main("Не от вас?","annoyed","suspicious") 
        call her_main("А, понятно...","grin","worriedCl",emote="05") 
        call her_main("Не надо стесняться этого, сэр. Все в порядке.") 
        dum_[1]"*акхм*... вот оно."
        call her_main("Спасибо, сэр.","base","base") 
        call her_main("Так посмотрим....","annoyed","down") 
        hide screen hermione_main
        with d3
        stop music fadeout 7.0
        pause.1
        
        $ letter_text = "{size=-7}Кому: Гермионе Грейнджер\n\n{/size}{size=-4}Дорогая [word_01]. \nЯ не тот, кто ты думаешь Я... Даже не человек, так сказать. Уже несколько месяцев я выдавал себя за человека, известного тебе как профессор Дамблдор. Но пришло время мне вернуться [word_02]. К тому времени, как ты получишь это письмо, меня уже не будет. Мы больше никогда с тобой не увидимся, но я обещаю тебе, что буду хранить воспоминания, об этом коротком моменте пребывания в твоем странном мире. \n\nПрощай, моя маленькая [word_03]. {size=-3}\n\n-[word_04]-{/size}"
        
        label last_letter:
        show screen letter
        call bld 
        call ctc 
        
        menu:
            "-Закончить чтение-":
                pass    
            "-Еще-":
                jump last_letter
                
        hide screen letter

        call her_main(".............................................................................................................................................................","disgust","shocked",cheeks="blush") 
        dum_[1]"Я предполагаю, что автор этого письма некое существо-Джинн?"
        dum_[1]"Тот, кто выдавал себя за меня, последние несколько месяцев?"
        call her_main(".............................................................................................................................................................","disgust","shocked",cheeks="blush") 
        dum_[1]"Ну, теперь, когда я вернулся..."
        dum_[1]"Я конечно же положу конец всей этой \"продаже очков, за неприличные услуги\"."
        call her_main("","scream","angry",emote="01") 
        pause.1
        with hpunch
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        her "{size=+7}Что?!!{/size}"
        call her_main("Тогда как я смогу заработать какие-то очки?","disgust","glance") 
        dum_[1]"Так же, как и всегда, мисс Грейнджер."
        call her_main("Да...?","open","annoyed",cheeks="blush") 
        dum_[1]"Упорным трудом."
        call her_main("Ну это же просто глупо!","angry","angry",cheeks="blush") 
        dum_[2] "Мисс Грейнджер, не могли бы вы попридержать свой язык, когда--"
        ### TITS ###
        hide screen hermione_main
        $ hermione_wear_bra = False
        call h_action("lift_top") 
        call her_main("","annoyed","annoyed",xpos="mid",trans="fade") 
        stop music
        call ctc 
        
        dum_[3] "{size=+4}!!!{/size}"
        call her_main("Или вы предпочитаете увидеть мою киску, сэр?","scream","angry",emote="01") 
        call her_main("","annoyed","angry") 
        
        $ hermione_wear_panties = False
        call set_hermione_action("lift_skirt") 
        call ctc 
        
        with hpunch
        dum_[5] "{size=+7}КХТ!!!{/size}"
        her "Я готова на все, чтобы получить эти очки, сэр!"
        call h_action("") 
        with hpunch
        call her_main("И я имею в виду {size=+9}ВСЕ, ЧТО УГОДНО!!!{/size}","scream","angry",emote="01") 
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.2
        
        call her_walk_desk_blkfade 
        
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause.7
        
        dum_[4] "О, боже... {image=textheart} "
        pause 1
        
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    centered "{size=+7}{color=#cbcbcb}-\{Спасибо за игру!\}-{/color}{/size}\n\n
              {size=+1}{color=#cbcbcb}-AKABUR 2014-{/color}{/size}"
    
    pause 2
     

    $ persistent.game_complete = True # Turns TRUE after you beat the game. Unlocks the gallery.
    
    # SILVER Items
    
    # gift item invintory
    $ persistent.gift_item_inv = []
    $ persistent.gift_item_inv = gift_item_inv
    
    # outfit invintory 
    #$ persistent.outfit_inventory = []
    #$ persistent.outfit_inventory = outfit_inventory
    
    # books
    #$ persistent.book_progress = []
    #$ persistent.book_progress = book_progress
    #$ persistent.book_done = []
    #$ persistent.book_done = book_done
    #$ persistent.books = []
    #$ persistent.books = books
    
    
    if public_whore_ending:
        $ persistent.ending_02 = True # Unlocked ending 01.
    else:
        $ persistent.ending_01 = True # Unlocked ending 01.
        
    $ persistent.gold = 0
    $ persistent.gold = persistent.gold + gold
        
    ### THE SKIRT ###
    if gave_miniskirt: #Turns True when Hermione has the miniskirt.
        $ persistent.haveskirt = True # Makes sure you only need to buy the skirt once. Checked at the +new game screen.
   
    
           
    ### SACRED SCROLLS ###
    $ persistent.ss_ = sscroll_
        
        
    $ renpy.full_restart()
        
        
