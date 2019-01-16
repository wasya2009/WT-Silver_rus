#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

### Change Hair Style ###
### Change Hair Color ###


label change_hair:

    #Hermione
    if active_girl == "hermione":
        jump change_her_hair
    #Luna
    if active_girl == "luna":
        jump change_lun_hair
    #Astoria
    if active_girl == "astoria":
        jump change_ast_hair
    #Susan
    if active_girl == "susan":
        jump change_sus_hair


### Change Hermione's Hair Color ###

label change_her_hair:

    #if hair_color_choice == h_hair_color:
    #    $ wardrobe_active = 1
    #    #">She's already wearing that!" #Remove line. Just for testing.
    #    jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 


            #Change Hair-Style
            if hair_style_choice == "A" and h_hair_style != "A":
                m "[hermione_name]..."
                m "Можешь сделать обычную прическу?"
                call her_main("Конечно, [genie_name].","soft","base") 
                call her_main("Дайте мне время.","base","base") 

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) 
                call compliment_her_hair_style 

                if hair_color_choice != h_hair_color:
                    m "Я хочу, чтобы ты сделала кое-что еще, [hermione_name]..."
                    call her_main("Конечно, [genie_name].","base","base") 

            if hair_style_choice == "B" and h_hair_style != "B":
                m "[hermione_name]..."
                m "Можешь завязать свои волосы для меня?"
                call her_main("Конечно, [genie_name].","soft","base") 
                call her_main("Дайте мне немного времени","base","base") 

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) 
                call compliment_her_hair_style 

                if hair_color_choice != h_hair_color:
                    m "Я хочу, чтобы ты сделала кое-что еще, [hermione_name]..."
                    call her_main("Конечно, [genie_name].","base","base") 

            if hair_style_choice == "E" and h_hair_style != "E":
                m "[hermione_name]..."
                m "Можешь сделать свою прическу короче?"
                call her_main("Конечно, [genie_name].","soft","base") 
                call her_main("Дайте мне время изменить ее.","base","base") 

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) 

                if hair_color_choice != h_hair_color:
                    m "Я хочу, чтобы ты сделала кое-что еще, [hermione_name]..."
                    call her_main("Конечно, [genie_name].","base","base") 

            #Change Hair-Color
            if hair_color_choice == h_hair_color:
                jump return_to_wardrobe
            else:
                if hair_style_choice != h_hair_style:
                    m "[hermione_name]..."

            #Brown #Done
            if hair_color_choice == "1":
                m "Я хочу, чтобы ты перекрасилась в коричневый цвет." 
                if whoring < 5:
                    call her_main("С удовольствием, [genie_name].","open","closed") 
                    call her_main("(Я ненавижу когда люди пялятся на меня...)","annoyed","ahegao") 
                    call her_main("Я пойду и изменю его.","base","baseL") 
                elif whoring < 11:
                    call her_main("Конечно, [genie_name].","open","base") 
                    call her_main("Дайте мне время сделать это.","base","base") 
                elif whoring < 20:
                    call her_main("Конечно, [genie_name].","soft","baseL") 
                    call her_main("Дайте мне время сделать это.","base","glance") 
                else: #20+
                    call her_main("Коричневый, [genie_name]?","upset","wink") 
                    call her_main("(Но мне нравилось выделяться своими волосами)","annoyed","down") 
                    call her_main("Хорошо, [genie_name]... {w=0.9}Дайте мне минуту.","base","baseL") 
                    
            #Blonde #Done
            elif hair_color_choice == "2":
                m "Можешь перекрасить свои волосы в светлый цвет?" 
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Светлый?...","upset","wink") 
                        call her_main("(это выглядит достаточно порядочно... {w=0.9}Наверное, нужно иногда пробовать что-то новое...)","annoyed","down") 
                        call her_main("Ладно, [genie_name]... {w=0.9}Дайте мне минуту.","base","base") 
                    elif whoring < 20:
                        call her_main("Светлый?","base","base") 
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Один момент.","base","glance") 
                    else: #20+
                        call her_main("Я почти не выгляжу как блондинка!","annoyed","down") 
                        call her_main("Есть что-то по-светлее?","angry","wink") 
                        m "Ты собираешься это делать или как?"
                        call her_main("Отлично... дайте мне секундочку.","annoyed","annoyed") 
                else:
                    call her_main("Нет, спасибо, [genie_name].","open","closed") 
                    call her_main("Мне нравятся мои волосы.","open","worriedL") 
                    call her_main("Я вынуждена отказаться!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe
                    
            #Red #Done
            elif hair_color_choice == "3":
                m "Можешь перекраситься в шатенку?" 
                if whoring >= 5:
                    if whoring < 11:
                        
                        call her_main("Рыжий, [genie_name]?","open","base") 
                        call her_main("Я буду выглядеть как Джинни...","base","down") 
                        m "Джинни?"
                        call her_main("Джинни Уизли, [genie_name].","open","closed") 
                        m "..."
                        call her_main("(...?)","angry","wink") 
                        m "Точно! Уизли!"
                        call her_main("Да, [genie_name].","open","suspicious") 
                        m "(Интересно, она горячая?)"
                        m "(Девчонка говорит, что она рыжая)"
                        g9 "(Очень интересно!)"
                        #if not mentioned_ginnys_hair:
                        #    call nar(>Your curiosity about Ginny grows!)
                        call her_main("Я перекрашусь, [genie_name].","open","baseL") 
                    elif whoring < 20:
                        call her_main("О, ничего себе, это выглядит красиво. Мне это и вправду нравится!","soft","base") 
                        call her_main("Теперь я буду похожа на Джинни...","smile","happyCl") 
                        call her_main("(Хотя она немного ниже меня, и ее волосы не такие кудрявые.)","annoyed","base") 
                        #if not mentioned_ginnys_hair:
                        #    call nar(>Your curiosity about Ginny grows!)
                        call her_main("(Интересно, будут ли учителя замечать, если мы пересядем в классе ...)","grin","ahegao") 
                        call her_main("(Есть только один способ выяснить!)","smile","glance") 
                        call her_main("Дайте мне минуту, я сделаю это.","base","glance") 
                    else: #20+
                        call her_main("Вы хотите, чтобы я была рыжей?","base","glance") 
                        call her_main("Вы знаете, что все говорят о рыжих, [genie_name].","smile","glance") 
                        call her_main("Позвольте мне перекраситься для вас.","soft","base") 
                        
                    #$ mentioned_ginnys_hair      = True
                    
                else:
                    call her_main("Нет, спасибо, [genie_name].","open","closed") 
                    call her_main("Мне и так нравятся мои волосы.","open","worriedL") 
                    call her_main("Я отказываюсь!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe
                    
            #Crimson #Done
            elif hair_color_choice == "4":
                m "Хочешь перекрасить свои волосы в малиновый?" 
                if whoring >= 8:
                    call her_main("Это действительно неплохой цвет, [genie_name].","soft","base") 
                    call her_main("Дайте мне минуту","base","base") 
                else:
                    call her_main("Это нелепо, вам не кажется?","angry","worriedCl") 
                    call her_main("(Я не покрашусь в малиновый, потому что буду выглядеть как блудница.)","annoyed","baseL") 
                    call her_main("Я вынуждена отказаться, [genie_name]!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Black #Done
            elif hair_color_choice == "5":
                m "Можешь перекраситься в брюнетку для меня?" 
                if whoring >= 8:
                    if whoring < 17:
                        call her_main("Черный, [genie_name]?","annoyed","down") 
                        call her_main("(Это выглядит хорошо.)","annoyed","baseL") 
                        call her_main("Я попробую! Дайте мне минуту.","soft","baseL") 
                    else: #17+
                        call her_main("Конечно, [genie_name]!","base","glance") 
                        call her_main("Мне нравится этот цвет!","smile","happyCl") 
                        call her_main("Дайте мне изменить себя.","base","glance") 
                else:
                    call her_main("Черный, [genie_name]?","open","suspicious") 
                    call her_main("Черный - это не совсем мой цвет","soft","baseL") 
                    call her_main("Я не думаю, что он подойдет мне, [genie_name].","open","closed") 
                    call her_main("Я вынуждена отказаться.","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Green #Done
            elif hair_color_choice == "6":
                m "Можешь снова покрасить свои волосы?"
                call her_main("Хорошо, [genie_name]. В какой цвет?","open","base") 
                g9 "Слизеринский зеленый!"
                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Конечно, почему нет","soft","baseL") #soft, baseL
                        call her_main("Зеленый цвет - это просто цвет, [genie_name]!","open","base") 
                        call her_main("Носить его на голове не значит, что я поддерживаю Слизерин!","open","closed") 
                        call her_main("(Это будет выглядеть ужасно подозрительно для Гриффиндора, хотя ...)","annoyed","worriedL") 
                        call her_main("Дайте мне минуту.","base","base") 
                    else: #17+
                        call her_main("Хорошо, [genie_name].","base","base") 
                        call her_main("Хочу открыть вам секрет.","soft","baseL") 
                        call her_main("Зеленый - мой любимый цвет.","base","glance") 
                        m "Правда? А как же рыжий?"
                        call her_main("Хм...нет, [genie_name].","annoyed","baseL")
                        call her_main("Рыжий цвет, такой агрессивный.","open","down") 
                        call her_main("Зеленый же мягкий и сладкий.","soft","baseL") 
                        call her_main("Это всегда напоминает мне природу, травяные поля летом, запах цветов повсюду...","open","baseL") 
                        call her_main("Мне это нравится!","smile","happyCl") 
                        call her_main("Дайте мне минуту.","base","glance") 
                else:
                    call her_main("Что?!","angry","angry") 
                    call her_main("Я не собираюсь ходить по школе как какой-то талисман Слизерина!","scream","angryCl") 
                    call her_main("Я категорически против!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
                    
            #Blue #Done
            elif hair_color_choice == "7":
                m "Не хочешь покрасить волосы синим цветом для меня?" 
                if whoring >= 11:
                    call her_main("Конечно, [genie_name].","soft","baseL") 
                    call her_main("Дайте мне минуту.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Я не буду красить свои волосы в синий для вас, [genie_name]!","open","angryCl") 
                        call her_main("Если вы хотите себе попугая, то просто купите его!","angry","angry") 
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                    else: #5-10
                        call her_main("Серьезно?, [genie_name]?","annoyed","suspicious") 
                        call her_main("Вы хотите что бы я выглядела как лесбиянка?","open","annoyed",cheeks="blush") 
                        call her_main("Я вынуждена отказаться!","annoyed","baseL") 
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                    
            #Purple #Done
            elif hair_color_choice == "8":
                m "Можешь перекраситься в пурпурный для меня?" 
                if whoring >= 11:
                    call her_main("Конечно, [genie_name].","soft","baseL") 
                    call her_main("Секунду.","base","glance") 
                else:
                    call her_main("Пурпурный?","angry","wink") 
                    call her_main("Мне нравится этот цвет, но...","soft","baseL") 
                    call her_main("Я не думаю что смогу носить его на голове...","annoyed","ahegao") 
                    call her_main("Я откажусь, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
                    
            #Pink #Done
            elif hair_color_choice == "9":
                m "Хочешь покрасить свои волосы в розовый для меня?" 
                if whoring >= 14:
                    call her_main("Конечно, [genie_name]!","smile","glance") 
                    call her_main("Я люблю розовый!!!","soft","baseL") 
                    call her_main("Хе-хе","smile","happyCl") 
                    call her_main("Секунду.","base","glance") 
                else:
                    call her_main("Перекрасить мои волосы...","angry","angry") #mad, angry
                    call her_main("Перекрасить в розовый?... {w=0.9}Розовый?!","angry","angry",emote="01") 
                    call her_main("Я не могу покраситься, [genie_name]!","scream","worriedCl") 
                    call her_main("(Что он думает, я что какой-то манекен?)","annoyed","angryL") 
                    call her_main("В любом случае это уродливый цвет.","open","closed") 
                    call her_main("Я отказываюсь!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 14."
                    jump return_to_wardrobe
                    
            #White #Done
            elif hair_color_choice == "10":
                m "Перекрась свои волосы в белый цвет." 
                if whoring >= 17:
                    call her_main("Ладно, [genie_name].","smile","baseL") 
                    call her_main("Дайте мне время.","base","glance") 
                else:
                    call her_main("Нет, [genie_name].","open","closed") 
                    call her_main("Я не буду ходить по школе как бабушка!","annoyed","annoyed") 
                    call her_main("Я против.","annoyed","baseL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_her_hair_color(hair_color_choice) 


            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_her_hair_style(hair_style_choice) 
            call her_main("","","",xpos="wardrobe") 

            if hair_color_choice == h_hair_color:
                call screen wardrobe

            if hair_color_choice == "2" and whoring <= 5:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if hair_color_choice == "3" and whoring <= 5:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if hair_color_choice == "4" and whoring <= 8:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if hair_color_choice == "5" and whoring <= 8:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe

            if hair_color_choice == "6" and whoring <= 11:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if hair_color_choice == "7" and whoring <= 11:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if hair_color_choice == "8" and whoring <= 11:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if hair_color_choice == "9" and whoring <= 14:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 14."
                jump return_to_wardrobe
            if hair_color_choice == "10" and whoring <= 17:
                ">Она пока не будет носить этот цвет."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_her_hair_color(hair_color_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe
#


label compliment_her_hair_style:
    if whoring < 5:
        call her_main("Как я выгляжу, [genie_name]?","soft","base") 
        m "Это действительно подходит тебе, [hermione_name]."
        call her_main("Спасибо, [genie_name].","base","baseL",cheeks="blush") 
    elif whoring < 11:
        call her_main("...","base","happyCl") 
        call her_main("Вам это нравится?, [genie_name]?","grin","wink",cheeks="blush") 
        m "Конечно же, [hermione_name]."
        call her_main("Спасибо.","base","base") 
    elif whoring < 20:
        call her_main("Как я выгляжу?","open","closed") 
        m "Ты очень милая, [hermione_name]!"
        call her_main("Рада слышать, [genie_name].","base","glance") 
    else: #20+
        if h_hair_style == "A":
            call her_main("Вам нравятся мои длинные волосы?, [genie_name]?","base","glance") 
            m "Да, [hermione_name]"
            call her_main("Я предпочитаю носить свои волосы так.","open","closed") 
            call her_main("Легко схватить и потянуть...","base","glance") 
            call her_main("Как поводок!","smile","angry") 
            g4 "Ты грязная извращенка!"
        else: 
            call her_main("Вам это нравится, [genie_name]?","base","glance") 
            call her_main("Это волосы заставляют меня выглядеть...","base","base") 
            call her_main("Развратной?","base","glance") 
            g4 "Ух! Ты можешь поспорить на свою прекрасную задницу!" 
            g9 "Почему бы тебе не подойти ближе, я обработаю твои волосы лосьоном!" 
            call her_main("[genie_name], вы должны знать, что я уже использовала довольно дорогой лосьон этим утром и ...","open","closed") 
            m "Я просто хочу облить их своей спермой, девочка ..."  
            call her_main("Ох-","soft","base") 
            call her_main("...","soft","baseL",cheeks="blush") 
            call her_main("(Хорошая идея.)","base","happyCl") 
            call her_main("Может как-нибудь потом, [genie_name].","smile","baseL") 

    return


label change_ast_hair:
    call set_ast_hair(hair_style_choice, hair_color_choice) 

    hide screen wardrobe
    call screen wardrobe

label change_sus_hair:
    call set_sus_hair(hair_style_choice, hair_color_choice) 

    hide screen wardrobe
    call screen wardrobe

