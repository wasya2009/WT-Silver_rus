#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_bottom:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_bottom
    #Luna
    if active_girl == "luna":
        jump equip_lun_bottom
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_bottom
    #Susan
    if active_girl == "susan":
        jump equip_sus_bottom


### Equip Bottom ###

label equip_her_bottom:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

    if skirt_choice == h_skirt and bottom_color_choice == h_skirt_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    if hermione_action == "hands_behind" or hermione_action == "covering" or hermione_action == "fingering" or hermione_action == "covering_top" or hermione_action == "pinch" or hermione_action == "hands_cuffed" or hermione_action == "milk_breasts":

        $ wardrobe_active = 1
        hide screen hermione_main
        with d3
        ">Гермиона в настоящее время позирует... обнаженной.\nХочешь, чтобы она оделась?"
        menu:
            "-Заставить ее одеться.-":
                call h_action("none") 
                hide screen hermione_main

            "-nvm-":
                show screen hermione_main
                with d3
                jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            ### Uniform Skirts ###

            #Uniform Skirt Very Long #Done
            if skirt_choice == "uni_skirt_1":
                m "Можешь надеть свою школьную юбку? Самую длинную." 
                if whoring < 8:
                    call her_main("Конечно, [genie_name].","soft","baseL") 
                    call her_main("Дайте минутку.","base","base") 
                elif whoring < 11:
                    call her_main("Ладно...Конечно, почему нет.","base","down") 
                    call her_main("Один момент.","base","base") 
                elif whoring < 20:
                    call her_main("Вы серьезно, [genie_name]?","disgust","down_raised") 
                    call her_main("Это выглядит довольно просто...","open","closed") 
                    call her_main("Я бы предпочла надеть немного короче!","angry","wink") 
                    m "Нет, [hermione_name]. Надень длинную ..."
                    call her_main("Хм...Ладно.","disgust","down_raised") 
                    call her_main("Дайте мне минутку.","annoyed","annoyed") 
                else: #20+
                    call her_main("Вы серьезно?","angry","wink") 
                    call her_main("Это выглядит так убого!","annoyed","ahegao") 
                    call her_main("Это смешно, в Хогвартсе никто не носит такие юбки!","disgust","narrow") 
                    m "Нет, [hermione_name]. Тебе нужно надеть это..."
                    call her_main("Хорошо, дайте минутку...","disgust","glance") 
                    
            #Uniform Skirt Long #Done
            elif skirt_choice == "uni_skirt_2":
                m "Можешь надеть свою школьную юбку? Длинную." 
                if whoring >= 5:
                    if whoring < 8:
                        call her_main("...","annoyed","annoyed") 
                        call her_main("Ладно.","open","closed") 
                        call her_main("Дайте мне минутку.","base","base") 
                    elif whoring < 11:
                        call her_main("Конечно, почему нет.","base","down") 
                        call her_main("Секунду.","base","base") 
                    elif whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Один момент.","base","glance") 
                    else: #20+
                        call her_main("...это старье?","annoyed","angryL") 
                        m "Да, а есть проблема?"
                        call her_main("...","annoyed","ahegao") 
                        call her_main("Думаю, что нет...","annoyed","down") 
                        call her_main("Просто... это, так обыденно!","annoyed","angryL") 
                else:
                    call her_main("Я извиняюсь, [genie_name].","base","base") 
                    call her_main("Но это против правил Хогвартса!","open","closed") 
                    call her_main("Я вынуждена отказаться, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Medium Length #Done
            elif skirt_choice == "uni_skirt_3":
                m "Можешь надеть свою школьную юбку? Среднюю." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Ладно...хорошо, почему нет.","base","down") 
                        call her_main("Дайте секунду.","base","base") 
                    elif whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Одну минуту.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(По-крайней мере, она достаточно коротка...)","annoyed","ahegao") 
                        call her_main("Ладно, [genie_name].","soft","baseL") 
                        call her_main("Дайте минутку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Я извиняюсь, [genie_name].","base","base") 
                        call her_main("Но это против правил Хогвартса!","open","closed") 
                        call her_main("Я вынуждена отказаться, [genie_name].","normal","base") 
                    else:
                        call her_main("Это слишком коротко, [genie_name]!","open","closed") 
                        call her_main("Я отказываюсь!","annoyed","suspicious") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Short #Done
            elif skirt_choice == "uni_skirt_4":
                m "Можешь надеть свою школьную юбку? Короткую."
                if whoring >= 14:
                    if whoring < 20:
                        call her_main("Хорошо, почему нет.","soft","baseL") 
                        call her_main("Одну минуту.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(По-крайней мере она достаточно коротка...)","annoyed","ahegao") 
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Секундочку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Извините, [genie_name].","base","base") 
                        call her_main("Но это против правил Хогвартса!","open","closed") 
                        call her_main("Я вынуждена отказаться, [genie_name].","normal","base") 
                    else:
                        call her_main("Она такая короткая!, [genie_name]!","open","closed") 
                        call her_main("Я вынуждена отказаться!","annoyed","suspicious") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 14."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Shortest #Done
            elif skirt_choice == "uni_skirt_5":
                m "Можешь надеть свою школьную юбку? Самую короткую что у тебя есть."  
                if whoring >= 17:
                    if whoring < 23:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Одну минутку.","base","glance") 
                    else: #23+
                        call her_main("(Что за старье?)","annoyed","down") 
                        call her_main("Могу ли я носить что-то немного короче?","open","baseL",cheeks="blush") 
                        m "Я не думаю, что у нас есть что-нибудь по-короче."
                        call her_main("Думаю, это просто нужно сделать ...","open","ahegao_raised",cheeks="blush") 
                        call her_main("Секунду.","base","ahegao_raised",cheeks="blush") 
                else:
                    if whoring < 5:
                        call her_main("Извините, [genie_name].","base","base") 
                        call her_main("Но это против правил Хогвартса!","open","closed") 
                        call her_main("Я вынуждена отказаться, [genie_name].","normal","base") 
                    else:
                        call her_main("Какая... какая короткая!","shock","wide") 
                        call her_main("Это какая-то ваша очередная глупая шутка?, [genie_name]?","angry","worried") 
                        call her_main("Нет, не говорите мне.","open","closed") 
                        call her_main("Я даже не хочу знать ...","annoyed","worriedL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Gryffindor #Done
            elif skirt_choice == "uni_skirt_cheer_gryff":
                m "Можешь надеть униформу болельщицы?"
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Конечно, [genie_name]!","soft","baseL",cheeks="blush") 
                        call her_main("Один момент","base","base") 
                    else:
                        call her_main("Ладно, [genie_name]!","soft","base") 
                        call her_main("Дайте мне минутку.","base","glance") 
                else:
                    call her_main("Я даже не знаю, [genie_name].","annoyed","down") 
                    call her_main("Я не похожа на болельщицу!","angry","wink") 
                    call her_main("Хотя мне нравится идея поддерживать свой факультет в квиддиче...","open","closed") 
                    call her_main("Мой приоритет заключается в том, чтобы получить кубок этом году!","open","baseL") 
                    call her_main("Я отказываюсь, [genie_name].","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Slytherin #Done
            elif skirt_choice == "uni_skirt_cheer" or skirt_choice == "uni_skirt_cheer_skimpy":
                if bottom_color_choice == "green" or bottom_color_choice == "blue" or bottom_color_choice == "yellow":
                    m "Можешь надеть эту униформу болельщицы?" 
                    if whoring >= 11:
                        if whoring < 14:
                            if bottom_color_choice == "green":
                                call her_main("Но [genie_name], она же для Слизерина!","angry","wink") 
                            if bottom_color_choice == "blue":
                                call her_main("Но [genie_name], она же для Когтеврана!","angry","wink") 
                            if bottom_color_choice == "yellow":
                                call her_main("Но [genie_name], она же для Пуффендуя!","angry","wink") 
                            m "И?"
                            call her_main("Я из Гриффиндора!","annoyed","annoyed") 
                            if bottom_color_choice == "green":
                                call her_main("(Я выше этого.)","disgust","down_raised") 
                            call her_main("Я не могу это надеть!","open","worriedCl") 
                            m "Почему нет?"
                            call her_main("Я снова вам повторяю...Я из Гриффиндора!","annoyed","ahegao") 
                            m "(...)"
                            g9 "(У меня есть идея!)"
                            g4 "[hermione_name], Я совсем забыл сказать!"
                            m "Будучи лучшим учеником Гриффиндора, ты была выбрана для того, чтобы поменяться со студентом из другого факультета!"
                            m "Это прекрасный способ сблизить все четыре факультета!"
                            call her_main("Но ... факультеты Хогвартса должны конкурировать друг с другом! Особенно в спортивной деятельности, такой как квиддич!","disgust","glance") 
                            g4 "Бред какой-то! Все, что делается, вызывает ненавистные и нездоровые отношения между учащимися!"
                            if bottom_color_choice == "green":
                                m "Особенно Гриффиндор и Слизерин!"
                                m "Я имею в ввиду, тебе нравится когда они называют тебя грязнокровкой, каждый день?"
                                call her_main("Нет, [genie_name].","angry","wink") 
                                m "Или когда они называют тебя блудницей..."
                                g4 "Или шлюхой!"
                                g9 "Или сучкой!"
                                g4 "Или...шлюхой!"
                                g4 "Или..."
                                call her_main("Я вас поняла, [genie_name]!!!","scream","worriedCl",cheeks="blush") 
                            m "Я даю тебе возможность улучшить твои отношения с ними!"
                            m "Теперь ты собираешься надеть ее для меня или нет? ..."
                            call her_main("(...)","annoyed","angryL") 
                            call her_main("Ладно, [genie_name]... Дайте мне надеть ее.","annoyed","annoyed") 
                        elif whoring < 20:
                            call her_main("Хорошо, [genie_name].","soft","ahegao") 
                            call her_main("(Как унизительно носить ее, находясь в Гриффиндоре.)","disgust","narrow") 
                            call her_main("Дайте мне минуту.","soft","baseL") 
                        else: #20+
                            if bottom_color_choice == "green":
                                call her_main("Конечно я надену ее!","smile","angry") 
                                call her_main("Дайте мне ее!","smile","happyCl") 
                                call her_main("(Я буду поддерживать их в следующей игре!)","soft","baseL",cheeks="blush") 
                                call her_main("(Если они выиграют, мне не придется долго носить эту форму!)","base","glance") 
                                call her_main("Вухууу! Вперед Слизерин!","smile","happyCl") 
                            else:
                                call her_main("Если мне действительно нужно...","annoyed","annoyed") 
                                call her_main("Дайте мне минуту.","soft","baseL") 
                    else:
                        if bottom_color_choice == "green":
                            call her_main("В зеленый?","shock","wide") 
                        if bottom_color_choice == "blue":
                            call her_main("В синий?","shock","wide") 
                        if bottom_color_choice == "yellow":
                            call her_main("В желтый?","shock","wide") 
                        call her_main("Вы серьезно?, [genie_name]?","angry","angry") 
                        call her_main("Вы уверены, что выбрали для меня тот цвет?","annoyed","suspicious") 
                        if bottom_color_choice == "green":
                            m "(Что-то подсказывает мне, что она не хочет носить зеленые вещи.)"
                            m "(У нее аллергия на кузнечиков или что-то еще?)"
                        else:
                            m "(Мог бы поклясться, что я выбрал хороший цвет для нее...)"
                        m "Забудь об этом, девочка."
                        call her_main("Я постараюсь!","annoyed","annoyed") 
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    m "Можешь надеть юбку болельщицы?"
                    if whoring >= 5:
                        if whoring < 11:
                            call her_main("Конечно, [genie_name]!","soft","baseL",cheeks="blush") 
                            call her_main("Дайте минутку.","base","base") 
                        else:
                            call her_main("Ладно, [genie_name]!","soft","base") 
                            call her_main("Дайте мне надеть ее.","base","glance") 
                    else:
                        call her_main("Я не знаю, [genie_name].","annoyed","down") 
                        call her_main("Я не похожа на болельщицу!","angry","wink") 
                        call her_main("Хотя мне нравится идея поддержать мой факультет в квиддиче...","open","closed") 
                        call her_main("Мой приоритет заключается в том, чтобы защитить кубок этом году!","open","baseL") 
                        call her_main("Я против, [genie_name].","soft","base") 
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 5."
                        jump return_to_wardrobe
                    
                    
            ### Uniform Skirts Low ###

            #Uniform Skirt Low Very Long #Done
            elif skirt_choice == "uni_skirt_1_low":
                m "Можешь надеть свою школьную юбку? Самую длинную. Но немного приспусти ее." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Ладно...хорошо, почему нет.","base","down") 
                        call her_main("Дайте минуту.","base","base") 
                    elif whoring < 20:
                        call her_main("Вы серьезно, [genie_name]?","disgust","down_raised") 
                        call her_main("Это звучит довольно просто...","open","closed") 
                        call her_main("Я не прочь носить что-нибудь по-короче.","angry","wink") 
                        m "Нет, [hermione_name]. Надень это..."
                        call her_main("Хм...Ладно.","disgust","down_raised") 
                        call her_main("Дайте мне сделать это.","annoyed","annoyed") 
                    else: #20+
                        call her_main("Вы серьезно?","angry","wink") 
                        call her_main("Это таааак странно.","annoyed","ahegao") 
                        call her_main("В Хогвартсе уже такое никто не носит.","disgust","narrow") 
                        m "Нет, [hermione_name]. Тебе нужно надеть это"
                        call her_main("Ладно...Я сделаю это.","disgust","glance") 
                else:
                    if whoring < 5:
                        call her_main("Приспустить юбку?!","shock","wide") 
                        call her_main("Я не буду делать этого, [genie_name].","angry","angry") 
                        call her_main("Как вы можете просить такое?","angry","worriedCl") 
                        call her_main("(Мерзкий старик...)","annoyed","annoyed") 
                    else:
                        call her_main("Нет, [genie_name].","open","closed") 
                        call her_main("Я не опущу юбку для вас, [genie_name].","annoyed","annoyed") 
                        call her_main("Так вы будете видеть мои трусики...","disgust","down_raised") 
                        m "Будто в этом есть что-то плохое..., [hermione_name]."
                        call her_main("Я отказываюсь!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Medium Length #Done
            elif skirt_choice == "uni_skirt_2_low":
                m "Можешь надеть свою школьную юбку? Средней длины. Но немного приспусти ее."
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("Ладно...почему нет.","base","down") 
                        call her_main("Минуту.","base","base") 
                    elif whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Один момент.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(По крайней мере она достаточно коротка.)","annoyed","ahegao") 
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне сделать это.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Приспустить свою юбку?!","shock","wide") 
                        call her_main("Я не собираюсь делать это для вас, [genie_name].","angry","angry") 
                        call her_main("Как вы могли, даже предположить такое?","angry","worriedCl") 
                        call her_main("(Грязный старик...)","annoyed","annoyed") 
                    else:
                        call her_main("Нет, [genie_name].","open","closed") 
                        call her_main("Я не буду делать это для вас, [genie_name].","annoyed","annoyed") 
                        call her_main("Мои трусики будут видны!","disgust","down_raised") 
                        m "Будто в этом есть что-то плохое..., [hermione_name]."
                        call her_main("Кроме того, длина, которую вы предложили, слишком короткая!","open","closed") 
                        call her_main("Я против!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Short #Done
            elif skirt_choice == "uni_skirt_3_low":
                m "Можешь надеть свою школьную юбку? Короткую. Но немного приспусти ее."
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне сделать это.","base","glance") 
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") 
                        call her_main("(По крайней мере, это достаточно коротко...)","annoyed","ahegao") 
                        call her_main("Ладно, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне минутку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Приспустить мою юбку вниз?!","shock","wide") 
                        call her_main("Я не собираюсь делать это для вас, [genie_name].","angry","angry") 
                        call her_main("Как вы могли об этом подумать?!","angry","worriedCl") 
                        call her_main("(Старый извращенец...)","annoyed","annoyed") 
                    else:
                        call her_main("Нет, [genie_name].","open","closed") 
                        call her_main("Я не буду спускать свою юбку, [genie_name].","annoyed","annoyed") 
                        call her_main("Вы будете видеть мои трусики...","disgust","down_raised") 
                        m "Будто в этом есть что-то плохое..., [hermione_name]."
                        call her_main("Кроме того, длина, которую вы предложили, слишком короткая!","open","closed") 
                        call her_main("Я против!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Shortest (Micro Skirt) #Not implemented.
            elif skirt_choice == "uni_skirt_4_low":
                m "Можешь надеть эту юбку для меня?" 
                ">Ты передаешь ей микро-юбку." 
                if whoring >= 20:
                   call her_main("","base","base") 
                else:
                    call her_main("","base","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 20."
                    jump return_to_wardrobe


            ### Skirts ###
                    
            #Belted Mini Skirt #Done
            elif skirt_choice == "skirt_belted_mini":
                m "Хочешь носить юбку, которую я купил?" 
                if whoring >= 8: 
                    if whoring < 14:
                        call her_main("(Она такая короткая!)","disgust","down_raised") 
                        call her_main("(...)","annoyed","angryL") 
                        call her_main("Ладно, [genie_name]...Я надену это.","open","closed") 
                        m "Правда?"
                        call her_main("Дайте мне эту юбку, пока я не передумала.","annoyed","annoyed") 
                    elif whoring < 23:
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне надеть это.","base","glance") 
                    else: #23+
                        call her_main("Ладно, [genie_name].","smile","happyCl") 
                        call her_main("Дайте мне это!","open_tongue","ahegao_raised",cheeks="blush") 
                        g4 "(!!!)"
                        call her_main("Я имею в виду юбку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Извините, [genie_name].","base","base") 
                        call her_main("Но это не соответствует правилам Хогвартса","open","closed") 
                        call her_main("Я против, [genie_name].","normal","base") 
                    else: 
                        call her_main("Безоговорочное нет, [genie_name]!","scream","worriedCl") 
                        call her_main("Я не буду носить юбку такой длины!","angry","angry") 
                        call her_main("(О чем он вообще думает?...)","angry","worried") 
                        call her_main("Я против.","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Belted Micro Skirt #Done
            elif skirt_choice == "skirt_belted_micro":
                m "Хочешь носить юбку, которую я купил?"
                if whoring >= 17: 
                    if whoring < 23: 
                        call her_main("(Она такая короткая!)","disgust","down_raised") 
                        call her_main("(Каждый сможет увидеть мою попу в этом ...)","soft","ahegao") 
                        call her_main("(...)","annoyed","angryL") 
                        call her_main("Я надену ее!.","open","closed") 
                        m "Правда??"
                        call her_main("Конечно... Она достаточно короткая.","soft","baseL") 
                        call her_main("Или вы скажете, что это слишком неуместно носить в этой школе?","base","glance") 
                        g4 "Шшшшшш... Ты получаешь мое одобрение."
                        call her_main("Спасибо, [genie_name].","soft","baseL") 
                    else: #23+
                        call her_main("Ладно, [genie_name].","smile","happyCl") 
                        call her_main("Дайте мне это!","open_tongue","ahegao_raised",cheeks="blush") 
                        g4 "(!!!)"
                        call her_main("Я имею в виду юбку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("Извините, [genie_name].","base","base") 
                        call her_main("Но это против правил Хогвартса","open","closed") 
                        call her_main("Я отказываюсь, [genie_name].","normal","base") 
                    else: 
                        call her_main("Категорически нет, [genie_name]!","scream","worriedCl") 
                        call her_main("Я не буду носить короткую юбку!","angry","angry") 
                        call her_main("(О чем он думает?...)","angry","worried") 
                        call her_main("Я против.","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe


            ### Pants ###
                    
            #Pants Jeans Long #Done
            elif skirt_choice == "pants_jeans_long":
                m "Можешь надеть эти брюки для меня?" 
                if whoring >= 2: 
                    if whoring < 5:
                        call her_main("[genie_name], но ведь это джинсы!","angry","wink") 
                        m "...ну?"
                        call her_main("Одежда маглов!","disgust","down_raised",cheeks="blush") 
                        call her_main("Девочки в Хогвартсе должны носить юбки!","open","closed") 
                        call her_main("Всегда! Без исключений!","annoyed","worriedL") 
                        m "Кажется это попахивает сексизмом, тебе не кажется?"
                        call her_main("Я... э-э...","angry","wink") 
                        call her_main("(Черт,... он прав...)","disgust","down_raised") 
                        call her_main("(Хм... может поносить их... Они не выглядят слишком плохо...)","clench","down_raised") 
                        m "(...)"
                        g4 "(Как смешно..! Как она может называть эти одеяла вокруг своих бедер юбками ..)"
                        g9 "(По крайней мере, я получаю неплохой ракурс на ее попку в этих штанах!)"
                        call her_main("Хорошо, [genie_name].","annoyed","ahegao") 
                        call her_main("Я надену их.","soft","base") 
                    elif whoring < 8:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне минуту.","base","base") 
                    else:
                        call her_main("Но они такие длинные, [genie_name]!","annoyed","ahegao") 
                        call her_main("Я даже не смогу показать свои ноги в них!","annoyed","angry") 
                        call her_main("(Хотя они заставляют мою попку выглядеть потрясающе...)","disgust","down_raised") 
                        call her_main("(Теперь, когда я думаю об этом...)","annoyed","ahegao") 
                        call her_main("Отлично, я их надену.","base","glance") 
                else:
                    call her_main("Простите, [genie_name].","soft","baseL") 
                    call her_main("Но брюки не являются частью школьной одежды.","open","closed") 
                    call her_main("К тому же, мне более комфортно в моей юбке.","open","suspicious") 
                    call her_main("Я против.","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 2."
                    jump return_to_wardrobe
                    
            #Pants Jeans Short #Done
            elif skirt_choice == "pants_jeans_short":
                m "Можешь надеть эти короткие джинсы для меня?" 
                if whoring >= 11:
                    if whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Дайте мне их.","base","base") 
                    else: #20+
                        call her_main("Ладно, [genie_name].","soft","baseL") 
                        call her_main("(Они такие тугие...у меня едва получится втиснуться в них...)","soft","ahegao") 
                        call her_main("Дайте мне минутку.","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("Извините, [genie_name].","soft","baseL") 
                        call her_main("Но брюки не являются частью школьной одежды.","open","closed") 
                        call her_main("К тому же, мне более комфортно в моей юбке.","open","suspicious") 
                        call her_main("Я против.","normal","base") 
                    elif whoring < 5: 
                        call her_main("...Что это?","annoyed","suspicious") 
                        m "брюки..?"
                        call her_main("...","annoyed","annoyed") 
                        call her_main("Это не брюки!","angry","worriedCl") 
                        m "А что же это?"
                        call her_main("Нижнее белье!","shock","wide") 
                        m "Так ты не будешь это носить?"
                        call her_main("НЕТ!","scream","worriedCl") 
                        call her_main("...","angry","angry") 
                    else: 
                        call her_main("Извините, [genie_name].","soft","baseL") 
                        call her_main("Но я не думаю что мне можно носить это в школе.","open","closed") 
                        call her_main("(Они выглядят очень хорошо, хотя...)","base","down") 
                        call her_main("(Может как-нибудь потом...)","base","baseL") 
                        call her_main("Я откажусь.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
                    
            #Pants Retro Shorts #Done
            elif skirt_choice == "pants_retro_shorts":
                m "Можешь надеть эти ретро брюки для меня?" 
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("(Эти брюки выглядят такими короткими...)","disgust","down_raised") 
                        call her_main("(Моя попа будет как на ладони в них..)","open_tongue","ahegao_raised",cheeks="blush") 
                        call her_main("Ладно, [genie_name].","smile","happyCl") 
                        call her_main("Я надену их.","base","glance") 
                    else: #20+
                        call her_main("Ладно, [genie_name].","soft","baseL") 
                        call her_main("Готова поспорить, вам нравится, как моя попка в них выглядит.","smile","glance") 
                        g9 "Ты чертовски права!"
                        call her_main("Рада слышать, [genie_name].","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("Извините, [genie_name].","soft","baseL") 
                        call her_main("Но брюки не являются частью школьной одежды.","open","closed") 
                        call her_main("К тому же, мне более комфортно в моей юбке.","open","suspicious") 
                        call her_main("Я против!","normal","base") 
                    elif whoring < 11: 
                        call her_main("Нет, [genie_name].","open","worriedCl") 
                        call her_main("Я не собираюсь носить это в школе!","angry","worried") 
                        call her_main("(О чем он думает?!)","annoyed","angryL") 
                    else: 
                        call her_main("Извините, [genie_name].","soft","baseL") 
                        call her_main("Но я не думаю что такое можно носить в школе...","open","closed") 
                        call her_main("(Они выглядят очень хорошо, хотя..)","base","down") 
                        call her_main("(Может как-нибудь потом...)","base","baseL") 
                        call her_main("Я откажусь.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe
                    
            #Pants Rocker Shorts #Done
            elif skirt_choice == "pants_rocker":
                m "Можешь надеть эти брюки для меня?" 
                if whoring >= 20: 
                    if whoring < 23:
                        call her_main("(Эти брюки такие короткие...)","disgust","down_raised") 
                        call her_main("(Я такая извращенка...)","open_tongue","ahegao_raised",cheeks="blush") 
                        call her_main("Ладно, [genie_name].","smile","happyCl") 
                        call her_main("Я надену их.","base","glance") 
                    else:
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Готова поспорить, вам нравится, как моя попка в них выглядит.","smile","glance") 
                        g9 "Ты чертовски права!"
                        call her_main("Рада слышать, [genie_name].","base","glance") 
                else:
                    if whoring < 2: 
                        call her_main("Я извиняюсь, [genie_name].","soft","baseL") 
                        call her_main("Но брюки не являются частью школьной одежды.","open","closed") 
                        call her_main("К тому же, мне более комфортно в моей юбке.","open","suspicious") 
                        call her_main("Я откажусь.","normal","base") 
                    elif whoring < 5: 
                        call her_main("Что?!...","angry","angry") 
                        call her_main("Что?!...Что это такое?","angry","angry",emote="01") 
                        m "Я просто сказал, что это..."
                        call her_main("[genie_name]!","shock","wide") 
                        call her_main("Вы не можете просто так давать нижнее белье своим ученикам!","angry","worried") 
                        m "Нижнее белье?"
                        call her_main("Да, нижнее белье!","open","worriedCl") 
                        call her_main("Как еще вы можете это назвать?","annoyed","annoyed") 
                        m "Это прекрасные джинсовые шорты!"
                        m "Не нужно бояться...Просто надень их!"
                        call her_main("Нет, я не сделаю этого!","scream","worriedCl") 
                        call her_main("(Нет на миллион лет!)","angry","angry") 
                    elif whoring < 11: 
                        call her_main("Извините, [genie_name].","open","worriedCl") 
                        call her_main("Но брюки не являются частью школьной одежды!","angry","worried") 
                        call her_main("(О чем он вообще думает?...)","annoyed","angryL") 
                    else: 
                        call her_main("Извините, [genie_name].","soft","baseL") 
                        call her_main("Но брюки не являются частью школьной одежды!","open","closed") 
                        call her_main("(Они выглядят неплохо,хотя...)","base","down") 
                        call her_main("(Может как-нибудь потом...)","base","baseL") 
                        call her_main("Я откажусь.","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
            else:
                pass

            hide screen hermione_main
            with d3

            pause.5

            call set_h_bottom(skirt_choice,bottom_color_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if skirt_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">Она пока не будет носить that skirt just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Попробуй еще раз на уровне разврата "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if skirt_choice == "uni_skirt_2" and whoring < 5: #no vest
                ">Она пока не будет носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3" and whoring < 8: #no tie
                ">Она пока не будет носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_4" and whoring < 14: #cleavage
                ">Она пока не будет носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 14."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_5" and whoring < 17: #crop top
                ">Она пока не будет носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer" and whoring < 5:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">Она пока не будет носить эту юбку."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">Она пока не будет носить эту юбку."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer_skimpy" and whoring < 8:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">Она пока не будет носить эту юбку."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">Она пока не будет носить эту юбку."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe


            #Uniform Low
            if skirt_choice == "uni_skirt_1_low" and whoring < 8:
                ">Она пока не будет носить этот костюм."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_2_low" and whoring < 11:
                ">Она пока не будет носить этот костюм."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3_low" and whoring < 17:
                ">Она пока не будет носить этот костюм."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            #if skirt_choice == "uni_skirt_4_low" and whoring < 20:
            #    ">Она пока не будет носить that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Попробуй еще раз на уровне разврата 20."
            #    jump return_to_wardrobe

            #Skirts
            if skirt_choice == "skirt_belted_mini" and whoring < 8:
                ">Она пока не будет носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if skirt_choice == "skirt_belted_micro" and whoring < 17:
                ">Она пока не будет носить носить эту юбку."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe

            #Pants
            if skirt_choice == "pants_jeans_long" and whoring < 2:
                ">Она пока не будет носить эти брюки."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if skirt_choice == "pants_jeans_short" and whoring < 11:
                ">Она пока не будет носить эти брюки."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_retro_shorts" and whoring < 17:
                ">Она пока не будет носить эти брюки."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if skirt_choice == "pants_rocker" and whoring < 20:
                ">Она пока не будет носить эти брюки."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 20."
                jump return_to_wardrobe



            else:
                pass

            $ wardrobe_active = 1
            call set_h_bottom(skirt_choice,bottom_color_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe



### Equip Astoria's Bottom ###
label equip_ast_bottom: 
    call set_ast_bottom(skirt_choice) 
        
    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Bottom ###
label equip_sus_bottom:
    call set_sus_bottom(skirt_choice) 

    hide screen wardrobe
    call screen wardrobe

