#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_top:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_top
    #Luna
    if active_girl == "luna":
        jump equip_lun_top
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_top
    #Susan
    if active_girl == "susan":
        jump equip_sus_top


### Equip Hermione's Top ###

label equip_her_top:    

    if top_choice == h_top and top_color_choice == h_top_color:
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

            "-Забудь-":
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

            ### Uniform ###

            #Uniform Top Vest and Tie #Done
            if top_choice == "uni_top_1":
                m "Можешь надеть свою школьную рубашку? С жилетом и галстуком." 
                if whoring < 8:
                    call her_main("Конечно, [genie_name].","soft","baseL") 
                    call her_main("Дайте мне минуту.","base","base") 
                elif whoring < 14:
                    call her_main("Ладно, [genie_name].","smile","happyCl") 
                    call her_main("Секунду.","base","glance") 
                elif whoring < 20:
                    call her_main("Вы серьезно, [genie_name]?","angry","wink") 
                    call her_main("Моя школьная одежда?","angry","base") 
                    call her_main("Вы даже не хотите, чтобы я сняла галстук?","disgust","glance") 
                    m "Нет, [hermione_name]. Не сегодня."
                    call her_main("(Что он хочет?)","annoyed","suspicious") 
                    call her_main("(Может быть, это тест какой-то...)","disgust","down_raised") 
                    call her_main("Хорошо, один момент.","annoyed","annoyed") 
                else: #20+
                    call her_main("Это старье?","angry","wide") 
                    call her_main("Это какая-то глупая шутка, [genie_name]?","angry","angry") 
                    m "..."
                    m "(Я не знаю.)"
                    call her_main("Это неприемлимо!","scream","worriedCl") 
                    call her_main("В ней даже не видно моего тела!","angry","down_raised") 
                    m "(...)"
                    call her_main("Вы оскорбляете чувства моих сисек, [genie_name]!!!","soft","base",tears="soft") 
                    g4 "*Вздох* {w=0.9}Я никогда этого не делаю, [hermione_name]!"
                    if one_of_ten == 1:
                        g4 "Твоя грудь изумительна!"
                    if one_of_ten == 2:
                        g4 "Твоя грудь великолепна!"
                    if one_of_ten == 3:
                        g4 "Твоя грудь поразительна!"
                    if one_of_ten == 4:
                        g4 "Твоя грудь потрясающая!"
                    if one_of_ten == 5:
                        g4 "Твоя грудь впечатляет!"
                    if one_of_ten == 6:
                        g4 "Твоя грудь нереальная!"
                    if one_of_ten == 7:
                        g4 "Твоя грудь очень славная!"
                    if one_of_ten == 8:
                        g4 "Твоя грудь удивительная!"
                    if one_of_ten == 9:
                        g4 "Твоя грудь очень милая!"
                    if one_of_ten == 10:
                        g4 "Твоя грудь просто сумасшедшая!"
                    call her_main("И все же вы хотите, чтобы я носила это тряпье!","annoyed","annoyed") 
                    m "Ты собираешься это носить или нет?"
                    call her_main("Хммм... Ладно, дайте мне минутку.","annoyed","baseL") 
                    
            #Uniform Top Tie only #Done
            elif top_choice == "uni_top_2":
                m "Можешь надеть свою школьную рубашку? Без джемпера." 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("Хорошо, [genie_name].","base","glance") 
                        call her_main("Однако я считаю неуместным, чтобы студент Хогвартса не носил надлежащую школьную одежду...","open","closed") 
                        call her_main("(И, конечно, половина факультета Слизерина даже не думает завязывать свои туфли...)","annoyed","angryL") 
                        call her_main("В конце концов, вы директор. Вы создаете правила.","open","closed") 
                        call her_main("Я сейчас переоденусь, [genie_name].","base","base") 
                    elif whoring < 11:
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("Один момент.","base","base") 
                    elif whoring < 17:
                        call her_main("Конечно, [genie_name].","grin","baseL") 
                        call her_main("Я переоденусь тут, если вы не возражаете.","base","glance") 
                        #g4 "(Baby I don't mind at all!)"
                        #g9 "(Show me those titties!)"
                        # $ wardrobe_strip = True 
                    else: #17+
                        call her_main("Просто моя школьная рубашка и мой галстук?","soft","base") 
                        m "Да, [hermione_name]."
                        call her_main("Вы хотите, чтобы я подвязала рубашку на груди?","open","baseL") 
                        m "Нет, надень ее как нужно."
                        call her_main("Как нужно, [genie_name]?","angry","wink") 
                        m "Знаешь... пуговицы и все."
                        call her_main("(Я даже забыла, что у этой рубашки были пуговицы...)","annoyed","down") 
                        call her_main("Нельзя ли мне расстегнуть пуговицы, [genie_name]?","soft","baseL") 
                        m "Я не испугаюсь, [hermione_name]."
                        call her_main("(Это смешно, что я ношу свою рубашку.)","annoyed","ahegao") 
                        call her_main("Ладно, я сделаю это.","base","baseL") 
                else:
                    call her_main("Извините, [genie_name].","base","base") 
                    call her_main("Но это против школьных правил!","open","closed") 
                    call her_main("Я отказываюсь, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 2."
                    jump return_to_wardrobe
                    
            #Uniform Top No Tie #Done
            elif top_choice == "uni_top_3":
                m "Можешь надеть свою школьную рубашку? Но без джемпера и галстука." 
                if whoring >= 5: #Gets removed at level 11.
                    call her_main("Вам виднее, [genie_name].","annoyed","annoyed") 
                    call her_main("Не могу поверить, что я готова снять свой галстук Гриффиндора для вас...","angry","angry") 
                    m "Это просто галстук, девочка!"
                    call her_main("Нет, это не...","scream","worriedCl") 
                    call her_main("...","annoyed","worriedL") 
                    call her_main("Ладно, дайте мне минутку","annoyed","base") 
                else:
                    call her_main("Нет, спасибо, [genie_name].","open","worriedL") 
                    call her_main("Никакое количество очков не убедит меня снять мой драгоценный галстук Гриффиндора!","open","closed") 
                    call her_main("Это самый ценный предмет одежды, который у меня есть!","soft","baseL") 
                    m "(Может, для тебя это и так...)"
                    g9 "(Но для меня это твои трусики!!!)"
                    call her_main("В конце концов, мой галстук представляет мою принадлежность и приверженность факультету Гриффиндора.","soft","base") 
                    m "..."
                    call her_main("Каждый студент Гриффиндора знает это...","open","down") 
                    m "(Черт, она снова начинает рассказывать про свой факультет!)"
                    call her_main("...когда Годрик Гриффиндор, величайший из четырех основателей Хогвартса, выбирал цвета красный и золотой, для своего факультета, он...","open","closed") 
                    m "(Я не понимаю ни слова из того, что она говорит, {w=0.9}но она так мило это делает!)"
                    call her_main("...золотая грива льва, которая также является нашим символом...","smile","happyCl") 
                    m "(Может мне просто вздрочнуть пока она разговаривает?)"
                    m "(Наверное, сейчас не время. {w=0.9}Пожалуйста, скажи мне, что ты уже закончила.)"
                    call her_main("...что можно прочитать в \"Историях о Хогвартсе\", которую вы, [genie_name], конечно же много раз читали...","open","closed") 
                    m "(...)"
                    call her_main("...для ученика Хогвартса также важно...","soft","baseL") 
                    g4 "Хватит, девочка!"
                    m "Оставь галстук."
                    g4 "(И прекрати говорить!)"
                    call her_main("Очень мудро, [genie_name].","soft","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Cleavage #Done
            elif top_choice == "uni_top_4":
                m "Можешь надеть свою школьную рубашку? Только рубашку..." 
                g9 "И расстегни несколько пуговиц..." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("(Надеюсь, что никто не будет на это глазеть...)","annoyed","down") 
                        call her_main("Ладно, [genie_name]. {w=0.9}Я сделаю это.","open","suspicious") 
                    elif whoring < 20:
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Я сделаю это.","base","glance") 
                        m "Да, сделай это, [hermione_name]."
                        g4 "(И покажи мне свои сиськи.)"
                    else: #20+
                        call her_main("(Пуговиц?...)","base","suspicious") 
                        call her_main("(Оу, он действительно так думает.)","base","down") 
                        call her_main("Разве я не могу подвязать рубашку на груди, чтобы было легче снимать ее?","open","closed") 
                        m "Это твой выбор, [hermione_name]"
                        call her_main("Да.","soft","baseL") 
                        call her_main("Мне нравится показывать их людям!","grin","wink",cheeks="blush") 
                        g4 "Ты безнадежная шлюха!"
                        call her_main("...","base","glance") 
                        m "Надевай свою рубашку как надо, пока что."
                        m "Если тебе повезет и я передумаю, я дам тебе знать."
                        call her_main("Хорошо, [genie_name]. {w=0.9}Дайте мне минутку.","soft","baseL") 
                else:
                    if whoring >=2:
                        call her_main("Показывать себя...","open","suspicious") 
                        call her_main("Развратной?","angry","angry") 
                        call her_main("[genie_name], при всем моем уважении,...","open","closed") 
                        call her_main("Я не собираюсь ходить по школе как... {w=0.9}блудница!","angry","angry",emote="01") 
                        call her_main("(Что он думает обо мне? Что я из Слизерина?)","annoyed","angryL") 
                        m "Это может значительно повысить уверенность женщины, если она будет показывать свои..."
                        call her_main("Я чувствую себя очень уверенно, [genie_name].","open","closed") 
                        call her_main("Я против.","annoyed","suspicious") 
                    else:
                        call her_main("Уууупс....","angry","down_raised") 
                        call her_main("Я уронила свою палочку.","open","down") 
                        call her_main("Извините, [genie_name]. {w=0.9}Позвольте мне поднять ее.","open","baseL",cheeks="blush") 
                        hide screen hermione_main
                        with d3
                        ">Ты ходишь по очень тонкому льду!"
                        call her_main("Что вы хотели от меня, [genie_name]?","soft","baseL") 
                        m "(Может, сейчас не лучшее время.)"
                        m "Не бери в голову, девочка."
                        call her_main("Хорошо, [genie_name].","base","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    
            #Uniform Crop-Top #Done
            elif top_choice == "uni_top_5":
                m "Можешь надеть свою школьную рубашку? Я хочу, что бы она была расстегнута и подвязана на груди." 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("Я даже не знаю, хорошая ли это идея, [genie_name]...","open","closed") 
                        call her_main("Все будут смотреть на мою грудь...","annoyed","down") 
                        g9 "Было бы странно, если бы они этого не делали!"
                        call her_main("Хм... Ладно. {w=0.9}Я это сделаю.","soft","angry") 
                    elif whoring < 20:
                        call her_main("Подвязать рубашку на груди?.","open","suspicious") 
                        m "Да, если ты можешь это сделать."
                        call her_main("Конечно, [genie_name].","grin","angry",cheeks="blush") 
                        call her_main("Я сделаю это тут, если вы не против.","base","glance") 
                        #m "{w=0.5}.{w=0.5}.{w=0.5}.{w=1.0}!"
                        # $ wardrobe_strip = True 
                    else: #20+
                        call her_main("Конечно, [genie_name].","soft","baseL") #soft, baseL
                        call her_main("Я люблю носить свою рубашку так, это очень удобно!","smile","happyCl",emote="06") 
                        call her_main("Я могу легко развязать ее каждый раз, когда мальчики из Слизерина идут мимо меня!","soft","ahegao") 
                        call her_main("Или, конечно же, девушки из Слизерина! Я не говорю, что я против!","smile","happyCl") 
                        m "А как насчет учеников других факультетов?"
                        call her_main("Они тоже, конечно!","open","baseL",cheeks="blush") 
                        call her_main("(Но не так сильно, теперь, когда я думаю об этом.)","annoyed","ahegao") 
                        call her_main("Позвольте я подвяжу свою рубашку для вас!","grin","baseL") 
                        # $ wardrobe_strip = True 
                else:
                    call her_main("Это просто смешно!","angry","angry") 
                    call her_main("Я не собираюсь ходить по школе в таком виде!","annoyed","suspicious") 
                    call her_main("Я против!","open","worriedL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
                    
            #Uniform Top Vest with Cleavage #Done
            elif top_choice == "uni_top_6":
                m "Можешь надеть свой жилет? А под него рубашку, но только не вздумай ее застегивать."
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Ладно, почему нет.","soft","baseL") 
                        call her_main("Дайте мне переодеться.","base","base") 
                    elif whoring < 20:
                        call her_main("Просто жилетка?","annoyed","down") 
                        call her_main("(По-крайней мере я могу показать свое декольте.)","annoyed","ahegao") 
                        call her_main("Хорошо, [genie_name]. Я сделаю это.","base","glance") 
                    else: #20+
                        call her_main("Моя жилетка, [genie_name]?","angry","wink") 
                        call her_main("У вас нет ничего более стильного?","annoyed","ahegao") 
                        call her_main("Кроме того, красный и желтый не очень меня устраивает.","open","closed") 
                        m "Носи это, или заставлю тебя скрыть и свои сиськи!"
                        call her_main("(Это было бы ужасно!)","shock","wide") 
                        call her_main("Да, [genie_name]. Я сделаю это.","soft","baseL") 
                else:
                    if whoring < 5:
                        call her_main("Просто жилетка?","base","base") 
                        call her_main("Без галстука Гриффиндора?!","shock","wide") 
                        call her_main("Почему я должна делать это? Я отказываюсь, [genie_name]!","angry","base") 
                    else:
                        call her_main("Извините, [genie_name].","open","closed") 
                        call her_main("Но я не буду ходить по школе в...","angry","angry") 
                        call her_main("Я не буду показывать свою грудь, [genie_name]!","open","closed") 
                        call her_main("Я отказываюсь!","annoyed","baseL") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                   
                    
            #Uniform Top Cheer #Done
            elif top_choice == "uni_top_cheer" or top_choice == "uni_top_cheer_skimpy":
                if top_color_choice == "green" or top_color_choice == "blue" or top_color_choice == "yellow":
                    m "Можешь надеть эту юбку болельщицы?" 
                    if whoring >= 11:
                        if whoring < 14:
                            if top_color_choice == "green":
                                call her_main("Но [genie_name], она же для Слизерина!","angry","wink") 
                            if top_color_choice == "blue":
                                call her_main("Но [genie_name], она же для Когтеврана!","angry","wink") 
                            if top_color_choice == "yellow":
                                call her_main("Но [genie_name], она же для Пуффендуя!","angry","wink") 
                            m "И?"
                            call her_main("Я из Гриффиндора!","annoyed","annoyed") 
                            if top_color_choice == "green":
                                call her_main("(Я выше этого!)","disgust","down_raised") 
                            call her_main("Я не могу надеть это.","open","worriedCl") 
                            m "Почему?"
                            call her_main("Я повторяюсь. Я из Гриффиндора!","annoyed","ahegao") 
                            m "(...)"
                            g9 "(У меня есть идея!)"
                            g4 "[hermione_name], я совсем забыл сказать!"
                            m "Будучи лучшим учеником Гриффиндора, ты была выбрана для того, чтобы поменяться с другим студентом из другого факультета!"
                            m "Это прекрасный способ сблизить все четыре факультета!"
                            call her_main("Но... факультеты Хогвартса должны конкурировать друг с другом! Особенно в спортивной деятельности, такой как квиддич!","disgust","glance") 
                            g4 "Бред какой-то! Все, что делается, вызывает ненавистные и нездоровые отношения между учащимися!"
                            if top_color_choice == "green":
                                m "Особенно Гриффиндор и Слизерин!"
                                m "Я имею ввиду, тебе нравится когда они называют тебя грязнокровкой каждый день?"
                                call her_main("Нет, [genie_name].","angry","wink") 
                                m "Или когда они называют тебя блудницей..."
                                g4 "Или шлюхой!"
                                g9 "Или сучкой!"
                                g4 "Или... шлюхой!"
                                g4 "Или..."
                                call her_main("Я вас поняла, [genie_name]!!!","scream","worriedCl",cheeks="blush") 
                            m "Я даю тебе возможность улучшить твои отношения с ними!"
                            m "Теперь ты собираешься надеть ее для меня или нет?..."
                            call her_main("(...)","annoyed","angryL") 
                            call her_main("Ладно, [genie_name]... Дайте мне надеть ее.","annoyed","annoyed") 
                        elif whoring < 20:
                            call her_main("Ладно, [genie_name].","soft","ahegao") 
                            call her_main("(Как унизительно носить ее, находясь в Гриффиндоре.)","disgust","narrow") 
                            call her_main("Дайте мне минутку.","soft","baseL") 
                        else: #20+
                            if top_color_choice == "green":
                                call her_main("Конечно я надену ее!","smile","angry") 
                                call her_main("Дайте ее мне!","smile","happyCl") 
                                call her_main("(Я буду поддержкой для них в следующей игре!)","soft","baseL",cheeks="blush") 
                                call her_main("(Если они выиграют, мне не придется долго носить эту форму!)","base","glance") 
                                call her_main("Вухууу! Вперед Слизерин!","smile","happyCl") 
                            else:
                                call her_main("Если мне действительно нужно....","annoyed","annoyed") 
                                call her_main("Дайте мне минуту.","soft","baseL") 
                    else:
                        if top_color_choice == "green":
                            call her_main("В зеленый?","shock","wide") 
                        if top_color_choice == "blue":
                            call her_main("В синий?","shock","wide") 
                        if top_color_choice == "yellow":
                            call her_main("В желтый?","shock","wide") 
                        call her_main("Вы серьезно, [genie_name]?","angry","angry") 
                        call her_main("Вы уверены, что выбрали для меня тот цвет?","annoyed","suspicious") 
                        if top_color_choice == "green":
                            m "(Что-то подсказывает мне, что она не хочет носить зеленые вещи.)"
                            m "(У нее аллергия на кузнечиков или что-то еще?)"
                        else:
                            m "(Могу поклясться, что я выбрал хороший цвет для нее...)"
                        m "Забудь об этом, девочка."
                        call her_main("Я постараюсь!","annoyed","annoyed") 
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    if top_choice == "uni_top_cheer":

                        m "Можешь надеть костюм болельщицы? Только верх."
                        if whoring >= 5:
                            if whoring < 11:
                                call her_main("Конечно, [genie_name]!","soft","baseL",cheeks="blush") 
                                call her_main("Дайте мне минуту.","base","base") 
                            elif whoring < 20:
                                call her_main("Хорошо, [genie_name]!","soft","base") 
                                call her_main("Дайте я переоденусь.","base","glance") 
                            else: #20+
                                call her_main("Что это? Это для мальчиков?","angry","wide") 
                                call her_main("Вы украли это у талисмана Гриффиндора, [genie_name]?","angry","angry") 
                                call her_main("Вы хотите что бы я и львиную голову одела?","open","worriedL") 
                                m "(Львиная голова? У них есть такие вещи здесь?)"
                                call her_main("Вы же не серьезно, [genie_name]?!","open","worriedCl") 
                                m "Надень это или я заставлю тебя полностью раздеться!"
                                call her_main("...","shock","wide") 
                                call her_main("(Он действительно думает, что заставит меня это сделать?)","angry","wink") 
                                call her_main("{size=-5}(Как здорово!){/size}","smile","happyCl") 
                                call her_main("Я буду носить это, если мне придется...","open","closed") 
                                call her_main("{size=-5}Надеть?{/size}","angry","wink") 
                                m "Да."
                                call her_main("Хм... Как хотите.","angry","angry") 
                        else:
                            call her_main("Я не знаю, [genie_name].","annoyed","down") 
                            call her_main("Я не похожа на болельщицу!","angry","wink") 
                            call her_main("Хотя мне нравится идея, поддержать свой факультет в квиддиче...","open","closed") 
                            call her_main("Мой приоритет заключается в том, чтобы выиграть кубок этом году!","open","baseL") 
                            call her_main("Я против, [genie_name].","soft","base") 
                            if cheats_active or game_difficulty <= 2:
                                ">Попробуй еще раз на уровне разврата 5."
                            jump return_to_wardrobe

                    if top_choice == "uni_top_cheer_skimpy":
                        m "Можешь надеть костюм болельщицы с вырезом?"
                        if whoring >= 8: 
                            g9 "Вырез!" 
                            if whoring < 14:
                                call her_main("Конечно, [genie_name]!","soft","baseL",cheeks="blush") 
                                call her_main("Дайте мне минуту.","base","base") 
                            elif whoring < 23:
                                call her_main("Ладно, [genie_name]!","soft","base") 
                                call her_main("Дайте мне надеть его.","base","glance") 
                            else: #23+
                                call her_main("Гриффиндорский?","annoyed","suspicious") 
                                call her_main("Но Гриффиндор даже не побеждает!","angry","wink") 
                                call her_main("Гриффиндор даже не пытается победить!","open","worriedL") 
                                call her_main("(Они такие трудные...)","annoyed","ahegao") 
                                call her_main("Неужели мне это нужно?","angry","wink") 
                                m "Да, [hermione_name]. Надень его."
                                call her_main("Хорошо, если я должна... Позвольте мне переодеться.","annoyed","annoyed") 
                        else:
                            if whoring < 3: 
                                g9 "Вырезы..." 
                                m "Девочка, что ты делаешь?" 
                                ">Ты видишь, что Гермиона смотрит на одежду." 
                                call her_main("(Это школьная форма Гриффиндора по квидичу, да, но...)","annoyed","down") 
                                call her_main("(В ней так много дыр...)","disgust","down_raised") 
                                call her_main("(Может быть...!)","soft","wide") 
                                call her_main("[genie_name], у вас проблемы с крысами?","open","closed") 
                                m "Проблемы с крысами?"
                                call her_main("Да, крысы! Они повсюду в Хогвартсе.","open","worried") 
                                call her_main("И я не говорю о животных-крысах.","disgust","glance") 
                                m "(Люди здесь держат крыс в качестве своих питомцев?)"
                                call her_main("Вы должны поговорить с мистером Филчем. Он обязательно скажет, что с этим делать!","open","closed") 
                                call her_main("И выбросите это, здесь столько дыр...","annoyed","annoyed") 
                            else: 
                                g9 "Вырезы!" 
                                call her_main("Вырезы?","shock","wide") 
                                call her_main("Вы сошли с ума, [genie_name]?","scream","worriedCl") 
                                call her_main("Я не собираюсь ходить так, как эти... Слизеринцы!","angry","worried") 
                                m "Но это форма Гриффиндора!"
                                call her_main("Это не имеет никакого отношения к этому!","angry","angry") 
                                call her_main("(Глупые неряхи... всегда отвлекают нашу команду своими сиськами...)","annoyed","annoyed") 
                                call her_main("(Эти сиськи постоянно мелькают перед глазами наших игроков...!)","annoyed","angryL") 
                                call her_main("(Я ненавижу их, я никогда не упаду так низко!)","angry","angry") 
                                call her_main("Я не собираюсь надевать это, [genie_name]!","annoyed","annoyed") 
                            if cheats_active or game_difficulty <= 2:
                                ">Попробуй еще раз на уровне разврата 8."
                            jump return_to_wardrobe

        
            ### Muggle ###

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover":
                m "Можешь надеть свитер который я купил тебе?" 
                if whoring >= 0:
                    if whoring < 5:
                        call her_main("[genie_name], это же свитер!","angry","wink") 
                        m "И что...?"
                        call her_main("Одежда маглов!","disgust","down_raised",cheeks="blush") 
                        call her_main("Одежда маглов запрещена правилами школы...","open","closed") 
                        m "Правильная школьная форма... Да, да, слышал это уже сто раз..."
                        call her_main("(...)","annoyed","annoyed") #very upset, annoyed
                        m "Я разрешаю тебе носить это. В конце концов, я же директор."
                        g9 "(Я могу делать это дерьмо?!)"
                        call her_main("Ладно... Дайте мне его...","annoyed","angryL") 
                    elif whoring < 11:
                        call her_main("Ладно, [genie_name].","soft","baseL") 
                        call her_main("(Мне очень нравится цвет...)","base","down") 
                        call her_main("(Я, наверное, буду выглядеть очень мило!)","base","happyCl") 
                        call her_main("Дайте мне его, [genie_name].","base","base") 
                    else: #11+
                        call her_main("Конечно, [genie_name].","smile","glance") 
                        call her_main("Я надену его.","base","glance") 
                else:
                    pass

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover_sexy":
                m "Можешь надеть свитер, который я купил тебе?" 
                if whoring >= 2:
                    if whoring < 11:
                        call her_main("Хорошо, [genie_name]. Просто дайте мне...","soft","baseL") 
                        m "Одну секунду... Я почти закончил..."
                        call her_main("Закончил, [genie_name]? Что вы делаете с...","open","suspicious") 
                        m "Тссс! Молчи, девочка ... Я должен прочитать инструкцию."
                        g4 "(Так... Мне просто нужно потянуть сюда и толкнуть туда...)"
                        ">В ткани магически появилось отверстие в форме сердца!"
                        g9 "(Да, готово!)"
                        m "Девочка, теперь можешь надеть его."
                        call her_main("(Что он сделал с этим свитером?)","annoyed","suspicious") 
                        call her_main("(Он не похож на тот...)","annoyed","down") 
                        call her_main("Ладно, [genie_name]. Дайте мне надеть его.","soft","baseL") 
                    elif whoring < 20:
                        call her_main("Вы никогда не говорили, что в нем есть отверстие.","open","down") 
                        call her_main("(Прямо над моими огромными...)","disgust","down_raised") 
                        m "Это не моя вина, что ты никогда не замечала этого..."
                        call her_main("Я действительно чувствую, что он наполнен магией!","base","glance") 
                        call her_main("Возможно, чтобы увидеть это, нужна определенная степень... сексуального сознания...","soft","baseL",cheeks="blush") 
                        m "О да! Я думаю, что что-то подобное упоминалось в руководстве!"
                        call her_main("(...)","disgust","glance") 
                        call her_main("Ладно, дайте мне минутку что бы надеть его.","soft","ahegao") 
                    else: #20+
                        call her_main("Ладно, [genie_name].","smile","happyCl") 
                        call her_main("Дайте секунду.","base","glance") 
                else:
                    call her_main("Извините, [genie_name].","base","base") 
                    call her_main("Но такая одежда запрещена правилами Хогвартса!","open","closed") 
                    call her_main("Я против, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 2."
                    jump return_to_wardrobe

            #Muggle Sweater #Done
            elif top_choice == "normal_sweater":
                m "Можешь надеть ту кофту, что я купил тебе?" 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("[genie_name], но это же кофта!","angry","wink") 
                        m "...И что?"
                        call her_main("Одежда маглов!","disgust","down_raised",cheeks="blush") 
                        call her_main("Одежда маглов запрещена правилами школы...","open","closed") 
                        m "Правильная школьная одежда... Да, да, слышал это уже сто раз..."
                        call her_main("(...)","annoyed","annoyed") 
                        m "Я разрешаю тебе надеть ее, в конце-концов я же директор."
                        g9 "(Я могу делать это дерьмо?!)"
                        call her_main("Ладно, дайте мне ее...","annoyed","angryL") 
                    elif whoring < 20:
                        call her_main("Хорошо, [genie_name].","soft","baseL") 
                        call her_main("(Она очень похожа на один из моих старых свитеров...)","annoyed","down") 
                        call her_main("Дайте мне минуту.","base","base") 
                    else: #20+
                        call her_main("Конечно, [genie_name].","smile","glance") 
                        call her_main("Я надену ее.","base","glance") 
                else:
                    call her_main("Извините, [genie_name].","base","base") 
                    call her_main("Но подобная одежда запрещена правилами школы!","open","closed") 
                    call her_main("Я против, [genie_name].","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 2."
                    jump return_to_wardrobe

            #Muggle Waitress Top #Kinda done
            elif top_choice == "normal_waitress_top":
                m "Можешь надеть этот верх?" 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Ладно, [genie_name].","open","closed") 
                        call her_main("Дайте мне надеть его, пока я не передумала...","annoyed","annoyed") 
                    else: #11+
                        call her_main("Ладно, [genie_name].","soft","ahegao") 
                        call her_main("Дайте мне переодеться.","base","glance") 
                else:
                    if whoring < 2:
                        call her_main("Извините, [genie_name].","base","base") 
                        call her_main("Но такая одежда запрещена правилами Хогвартса!","open","closed") 
                        call her_main("Я против, [genie_name].","normal","base") 
                    else: #2-7
                        call her_main("Извините, [genie_name].","open","closed") 
                        call her_main("Но даже не думайте, что я буду носить такое в школе!","angry","angry") 
                        call her_main("Нет, спасибо.","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 8."
                    jump return_to_wardrobe
                    

            ### Wicked ###

            #Leather Jacket #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves" or top_choice == "wicked_leather_jacket_sleeveless" or top_choice == "wicked_leather_jacket_sleeves":
                m "Можешь надеть эту кожаную куртку?"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("Вы должны знать, [genie_name].","open","closed") 
                        call her_main("Я не против носить это в вашем кабинете.","open","worriedL") 
                        call her_main("(Или вообще ничего не носить.)","annoyed","annoyed") 
                        call her_main("Но носить что-то подобное в классе...","angry","angry") 
                        call her_main("Вы должны это понимать, [genie_name]!","annoyed","angry") 
                    elif whoring < 23:
                        call her_main("Ладно, [genie_name].","open","closed") 
                        call her_main("Это правда неплохая куртка.","annoyed","down") 
                        call her_main("Я надену ее.","base","base") 
                    else: #23+
                        call her_main("Конечно, [genie_name]!","smile","happyCl") 
                        call her_main("Мне нравится эта куртка!","smile","glance") 
                        call her_main("(Может, я буду носить ее иногда...)","soft","ahegao") 
                        call her_main("(Я хочу показать мальчикам мой новый бюстгальтер ...)","grin","baseL") 
                        call her_main("Дайте мне надеть ее.","base","glance") 
                else:
                    if whoring < 5: 
                        call her_main("[genie_name]?!","shock","wide") 
                        call her_main("Как вы можете предлагать что-то подобное одному из своих учеников!","angry","wink") 
                        call her_main("Это какая-то глупая шутка?","shock","worriedCl") 
                        m "Ладно, прости [hermione_name]. Это была просто шутка."
                        call her_main("Она не особо забавная, [genie_name].","annoyed","suspicious") 
                        g4 "(Какая ханжа.... Я потратил целое состояние на эту куртку!)"
                        m "(Интересно, я еще смогу вернуть за нее свои деньги...)"
                    elif whoring < 11: 
                        call her_main("Я не могу поверить, что вы просили меня об этом, [genie_name]","angry","angry") 
                        call her_main("Кожаная куртка? Для меня?","angry","worried") 
                        call her_main("Даже Слизерин не будет носить что-то подобное!","open","closed") 
                        call her_main("Я катергорически против!","annoyed","annoyed") 
                    else:
                        call her_main("Нет, [genie_name].","open","closed") 
                        call her_main("Даже учитывая все вещи, что я для вас делала...","open","worriedL") 
                        call her_main("Я не буду ходить в этом по школьным коридорам.","annoyed","annoyed") 
                        call her_main("Я против.","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe

            #Leather Jacket Open #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves_open" or top_choice == "wicked_leather_jacket_sleeveless_open" or top_choice == "wicked_leather_jacket_sleeves_open": 
                m "Можешь надеть эту кожаную куртку?"
                g9 "Но не застегивай ее!"
                if whoring >= 11: 
                    g9 "Твоим прелестям нужно дышать!"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("Вы должны знать, [genie_name].","open","closed") 
                        call her_main("Я не против носить это в вашем кабинете.","open","worriedL") 
                        call her_main("(Или вообще, ничего не носить.)","annoyed","annoyed") 
                        call her_main("Но носить что-то подобное в классе...","angry","angry") 
                        call her_main("(Я ни в коем случае не хожу в расстегнутой куртке вне вашего кабинета.)","annoyed","ahegao") 
                        call her_main("Вы должны это понимать, [genie_name]!","angry","angry") 
                    elif whoring < 23:
                        call her_main("Ладно, [genie_name].","open","closed") 
                        call her_main("Это правда неплохая куртка.","annoyed","down") 
                        call her_main("Просто... вы полагаете, что я постоянно буду ходить в расстегнутом виде?","angry","wink") 
                        m "Именно, [hermione_name]."
                        call her_main("С бюстгальтером под ним?","disgust","narrow") 
                        g9 "Еще бы!"
                        call her_main("(Я не верю что соглашаюсь на такое...)","angry","angry") 
                        call her_main("Ладно, [genie_name]. Я буду носить ее расстегнутой.","annoyed","annoyed") 
                    else: #23+
                        call her_main("Конечно, [genie_name].","soft","baseL") 
                        call her_main("Должна ли я носить бюстгальтер под ней, или вы хотите, чтобы я действительно показывала их?!","smile","glance") 
                        m "Хм..."
                        call her_main("Я шучу!","smile","happyCl") 
                        call her_main("Другие учителя не позволили бы это, что очень печально.","annoyed","down") 
                        call her_main("(Разве что профессер Снейп...)","annoyed","ahegao") 
                        call her_main("Давайте мне эту куртку.","base","glance") 
                else:
                    if whoring < 5:
                        call her_main("[genie_name]?!","shock","wide") 
                        call her_main("Как вы можете предлагать подобное своему ученику?!","angry","wink") 
                        call her_main("Это какая то шутка!","shock","worriedCl") 
                        m "Эм, извини, [hermione_name]. Это была шутка."
                        call her_main("Не самая смешная, [genie_name].","annoyed","suspicious") 
                        g4 "(Какая ханжа... Я потратил целое состояние на эту куртку!)"
                        m "(Интересно, могу ли я еще вернуть свои деньги...)"
                    elif whoring < 11: 
                        call her_main("Я не могу поверить что вы спрашиваете меня об этом, [genie_name]","angry","angry") 
                        call her_main("Кожаная куртка... для меня?","angry","worried") 
                        call her_main("Даже Слизерин не позволяет себе подобное!","open","closed") 
                        call her_main("Я категорически против!","annoyed","annoyed") 
                    else:
                        call her_main("Нет, [genie_name].","open","closed") 
                        call her_main("Даже после всего, что я для вас сделала...","open","worriedL") 
                        call her_main("Я не буду носить это в школе.","annoyed","annoyed") 
                        call her_main("Я отказываюсь!","normal","base") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe

            #Rocker Top #Done
            elif top_choice == "wicked_rocker_top":
                if whoring < 5: 
                    m "Можешь надеть этот топ..."
                else: 
                    m "Можешь надеть этот топ для меня?"

                if whoring >= 20: 
                    if whoring < 23: 
                        call her_main("Конечно, почему нет.","open","closed") 
                        m "Правда?"
                        call her_main("Да, это просто обычный топ..","soft","baseL") 
                        m "(...)"
                        m "(Я сошел с ума?)"
                        call her_main("Дайте мне минуту переодеться.","base","glance") 
                    else: #23+
                        call her_main("Конечно, [genie_name].","soft","ahegao") 
                        call her_main("Мне нравится, насколько он подчеркивает мою грудь!","smile","glance") 
                        call her_main("Я правда люблю это!","smile","happyCl") 
                        call her_main("Дайте мне минуту.","base","glance") 
                else:
                    if whoring < 5: 
                        call her_main("А...а....","shock","worriedCl") #Add screen shake and sneeze sound.
                        call her_main("Апчхуй..!","angry","worriedCl",cheeks="blush",emote="05") #Add screen shake and sneeze sound.
                        ">Гермиона чихнула."
                        call her_main("Охх...","silly","ahegao") 
                        call her_main("Мне ужасно жаль, [genie_name]...","angry","wink") 
                        call her_main("Спасибо...","base","happyCl") 
                        ">Гермиона хватает одежду."
                        g4 "(Подожди!...)"
                        ">Гермиона снова чихает."
                        m "(О, это просто отлично...)"
                        call her_main("Простите, сэр. Вы о чем-то меня спрашивали?","soft","baseL") 
                        m "Ничего, девочка..."
                    elif whoring < 11: 
                        call her_main("Что?... Что это?!","shock","wide") 
                        call her_main("Волшебный... Секс?!","scream","angry",emote="01") 
                        call her_main("Что это значит?","angry","angry") 
                        m "Это то, что популярно сегодня у детей!"
                        call her_main("Это, безусловно, не так!","annoyed","annoyed") 
                        m "Как скажешь..."
                        call her_main("Держите эту оскорбительную... вещь при себе, [genie_name].","scream","angryCl") 
                        call her_main("Я не надену его!","angry","worried") 
                    else: #11-19
                        call her_main("Нет, [genie_name]!","open","closed") 
                        call her_main("Я не буду носить его, находясь в школе!","open","worriedL") 
                        call her_main("О чем вы думаете!","angry","angry") 
                        call her_main("Я против!","annoyed","annoyed") 
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 20."
                    jump return_to_wardrobe
                    
            
            #Misc #Doesn't have texts yet.
            elif top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green":
                if whoring >= 11:
                    pass
                else:
                    ">Она пока не будет носить этот верх."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
            elif top_choice == "top_ripped_tie_striped":
                if whoring >= 11:
                    pass
                else:
                    ">Она пока не будет носить этот верх."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
            elif top_choice == "top_tie_striped":
                if whoring >= 11:
                    pass
                else:
                    ">Она пока не будет носить этот верх."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe
            elif top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green"):
                if whoring >= 17:
                    pass
                else:
                    ">Она пока не будет носить этот верх."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 17."
                    jump return_to_wardrobe
            elif top_choice == "top_fishnets":
                if whoring >= 20:
                    pass
                else:
                    ">Она пока не будет носить этот верх."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_top(top_choice,top_color_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if top_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">Она пока не будет носить этот верх."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Попробуй еще раз на уровне разврата "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice == "uni_top_2" and whoring < 2: #no vest
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if top_choice == "uni_top_3" and whoring < 5: #no tie
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_4" and whoring < 8: #cleavage
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_5" and whoring < 11: #crop top
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_6" and whoring < 8: #vest w/cleavage
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe

            if top_choice == "uni_top_cheer":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">Она пока не будет носить этот верх."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 5:
                        ">Она пока не будет носить этот верх."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 5."
                        jump return_to_wardrobe

            if top_choice == "uni_top_cheer_skimpy":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">Она пока не будет носить этот верх."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 8:
                        ">Она пока не будет носить этот верх."
                        if cheats_active or game_difficulty <= 2:
                            ">Попробуй еще раз на уровне разврата 8."
                        jump return_to_wardrobe

            #Muggle
            if top_choice == "normal_pullover" and whoring < 2:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if top_choice == "normal_pullover_sexy" and whoring < 2:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if top_choice == "normal_sweater" and whoring < 2:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 2."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 8:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 8."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 11:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe

            #Wicked
            if top_choice == "wicked_leather_jacket_short_sleeves" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_short_sleeves_open" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless_open" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves_open" and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "wicked_rocker_top" and whoring < 20:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 20."
                jump return_to_wardrobe

            #Misc
            if top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green" and whoring < 11:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if top_choice == "top_ripped_tie_striped" and whoring < 11:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if top_choice == "top_tie_striped" and whoring < 11:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 11."
                jump return_to_wardrobe
            if top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green") and whoring < 17:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 17."
                jump return_to_wardrobe
            if top_choice == "top_fishnets" and whoring < 20:
                ">Она пока не будет носить этот верх."
                if cheats_active or game_difficulty <= 2:
                    ">Попробуй еще раз на уровне разврата 20."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_h_top(top_choice,top_color_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe

            


### Equip Astoria's Top ###
label equip_ast_top: 
    call set_ast_top(top_choice) 
        
    hide screen wardrobe
    call screen wardrobe
        
### Equip Susan's Top ###
label equip_sus_top:
    call set_sus_top(top_choice) 

    hide screen wardrobe
    call screen wardrobe
        
        



