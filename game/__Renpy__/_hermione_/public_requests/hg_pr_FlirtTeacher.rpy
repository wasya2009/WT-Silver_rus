

### Flirt With Teacher ###

##(Level 02) (15 pt.) (Flirt with teachers). (Available during daytime only).
label hg_pr_FlirtTeacher:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_FlirtTeacher_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтоб пофлиртовала со своим учителем?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    m "[hermione_name], я хочу, чтобы ты пофлиртовала со своим учителем."

    if whoring < 3 or hg_pr_FlirtClassmate_OBJ.points < 2:
        jump too_much

    #Intro
    if hg_pr_FlirtTeacher_OBJ.points == 0 and whoring < 9:
        call her_main("Я сделаю все возможное, [genie_name]!","base","base",xpos="right",ypos="base")
        call her_main("Я рада, что вы, наконец, решили действовать, [genie_name]!","open","base")
        m "А?"
        call her_main("Вы, наконец, готовы расследовать темные делишки учителей, которые покупают услуги у студентов, не так ли?","normal","frown")
        call her_main("Для меня честь быть приманкой, в этом благородном деле.","open","closed")
        m "Эм... Да, это именно то, о чем я прошу."
        call her_main("Великолепно! Можете на меня рассчитывать, [genie_name]!","normal","frown")

    #Second time event.
    else:
        call her_main("Я позже, предоставлю вам подробный отчет, [genie_name].","normal","frown",xpos="right",ypos="base")
        m "Я буду ждать..."

    her "Ну, я лучше пойду. Занятия вот-вот начнутся..."

    $ hg_pr_FlirtTeacher_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_FlirtTeacher_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First level.
    call her_main("Добрый день, [genie_name].","base","base",xpos="right",ypos="base")
    m "[hermione_name]..."
    m "Ты выполнила мое задание?"
    her "Да [genie_name]..."

    menu:
        "\"Отлично, вот твои очки.\"":
            pass
        "\"Расскажи о деталях.\"":
            hide screen hermione_main
            with d3
            m "Скажи мне, со сколькими учителями ты флиртовала, [hermione_name]?"
            m "По подробнее."
            show screen blktone
            with d3

            #First level.
            if  whoring >= 3 and whoring < 6:

                #Event A
                if one_out_of_three == 1: ### Flitwick
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Я пыталась флиртовать с профессором Флитвиком....","open","worriedL",xpos="right",ypos="base")
                    call her_main("Но это не сработало...","annoyed","frown")
                    call her_main("..............................","annoyed","angryL")
                    m "Как интересно..."
                    m "Это все, что у тебя есть для меня, [hermione_name]?"
                    call her_main("Д-да...","open","worried")
                    her "Но [genie_name], я знаю \"грязные\" факты о профессоре Флитвике!"
                    her "Всем известно, что из-за своего роста..."
                    call her_main("Он иногда... эм...","soft","baseL")
                    call her_main("Он любит смотреть под юбки девочкам, [genie_name]!","annoyed","worriedL")
                    m "Как, и все?"
                    call her_main("Что?","open","base")
                    m "Я сказал: как мы все порицаем это и, должны быть, возмущены таким человеком, как профессор Флик-Флик."
                    call her_main("Эм... Его зовут \"Профессор Флитвик\", [genie_name].","normal","frown")
                    m "Верно. Внесем его в мой \"список непослушных мальчиков\", как я и говорил."
                    call her_main("......................","annoyed","suspicious")
                    m "Что ж, мне неприятно это признавать, но ты не выполнила задание, [hermione_name]."
                    call her_main("................................","annoyed","angryL")

                    menu:
                        "\"Ладно, держи свои очки.\"":
                            call her_main("Серьезно?","angry","worried")
                            call her_main("Спасибо огромное [genie_name]!","smile","happyCl")
                        "\"Ты не получишь очков!\"":

                            call her_main("Но [genie_name], я сделала все возможное!","angry","worried")
                            call her_main("Вы не можите нарушать свое обещание [genie_name]!","mad","worried",tears="soft")
                            m "......................."
                            stop music fadeout 1.0
                            call her_main("Так не подобает директору школы!","scream","worriedCl")
                            m "Уходи, [hermione_name]."
                            call her_main("Пф!","angry","angry",emote="01")
                            $ mad += 18
                            call music_block

                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt

                #Event B
                elif one_out_of_three == 2: ### Snape
                    call her_main("..................","soft","baseL",xpos="right",ypos="base")
                    her "............................"
                    m "[hermione_name]?"
                    call her_main("Да, [genie_name]... Простите... Я просто...","open","worried")
                    call her_main("............","soft","baseL")
                    m "Ты сделала то, о чем я тебя просил?"
                    call her_main("Я пыталась, [genie_name]. Я правда...","open","base")
                    m "С кем ты пыталась флиртовать?"
                    call her_main(".........","soft","baseL")
                    call her_main("С профессором Снейпом, [genie_name].","annoyed","angryL")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    m "Северус? Интересно..."
                    m "Как все прошло?"
                    call her_main("Это было ужасно [genie_name]...","normal","frown")
                    her "Простите, но я действительно ненавижу профессора Снейпа, [genie_name]!"
                    m "Я уверен, что эти чувства взаимны..."
                    m "Скажи мне, что случилось."
                    call her_main("Ничего не произошло, [genie_name]. Он просто смеялся надо мной...","annoyed","frown")
                    call her_main("У меня не так много женского обаяния, но я старалась быть хорошей...","annoyed","worriedL")
                    call her_main("А он просто начал смеяться мне в лицо!","scream","angryCl")
                    call her_main("...Очень страшно видеть, как Профессор Снейп смеется...","angry","worriedCl",emote="05")
                    her "........"
                    her "Я ужасно заигрываю, простите меня [genie_name]..."
                    call her_main("Но я знаю, что Профессор Снейп тоже проворачивает \"грязные\" делишки!","angry","angry")
                    her "Если бы вы отправили к нему кого-то другого, результат был бы другим, я знаю!"
                    m "Кого-то другого?"
                    call her_main("Да! Кого-то с большим опытом в этом...","upset","wink")
                    her "Эту..."
                    her "Эту, эм..."
                    m "Шлюху?"
                    call her_main("Да, я полагаю...","disgust","glance")
                    m "Не сдавайся, [hermione_name]. Мы сделаем из тебя шлю--"
                    m "Я имею в виду женщину!"
                    call her_main("...................","annoyed","annoyed")

                    menu:
                        "\"Вот твои очки, [hermione_name].\"":
                            pass
                        "\"...На этот раз ты не получишь очков\"":
                            call her_main("Но я сделала все возможное...","annoyed","angryL")
                            call her_main("И теперь я чувствую себя униженной...","angry","worriedCl",emote="05")
                            call her_main("Но я понимаю и не буду спорить с вашим решением...","normal","worriedCl")
                            call music_block

                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt

                #Event C
                elif one_out_of_three == 3: ### Filch
                    stop music fadeout 1.0
                    call her_main("Я пыталась флиртовать с мистером Филчем, [genie_name]...","open","worriedL",xpos="right",ypos="base")
                    m "Понятно. {size=-5}(Не понимаю, кто это.){/size}"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Да, я знаю, что технически мистер Филч не учитель....","open","worried")
                    m "А?"
                    call her_main("Но он работает в школе...","base","base")
                    her "И мы неплохо поладили!"
                    her "Он был удивительно мил."
                    her "Но я не думаю, что он \"грязный\", [genie_name].(Filtch - мистер Филч. Filth - грязь."                 
                    m "Ага... мистер Фил{size=+7}ьм{/size} исключен из списка."
                    call her_main("Его зовут \"Мистер Филч\", [genie_name]...","normal","frown")
                    m "А я что сказал?"

            #Second Level.
            elif whoring >= 6 and whoring < 9:

                #Event A
                if one_out_of_three == 1: ### Slughorn
                    stop music fadeout 1.0
                    call her_main("Ну, профессор Слизнорт пригласил меня на свое...","open","worriedL",xpos="right",ypos="base")
                    her "Довольно неприятное чаепитие..."
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Было много девочек...","open","closed")
                    her "Но все они были намного моложе, чем я..."
                    call her_main("Почти каждая была первокурсницей...","annoyed","suspicious")
                    call her_main("Мы пили чай и ели пирожные...","open","closed")
                    her "Все было довольно безобидно..."
                    m "Ты флиртовала с кем-то или нет?"
                    her "Да..."
                    call her_main("Или, по крайней мере, я пыталась...","annoyed","suspicious")
                    her "Профессор Слизнорт, похоже, больше интересуется гораздо более молоденькими девушками..."
                    m "Ты будто его ревнуешь, [hermione_name]."
                    call her_main("Что?!","angry","wide")
                    call her_main("Это абсурд!","annoyed","angryL")
                    m "Вот твои очки..."
                    her "...................."

                #Event B
                elif one_out_of_three == 2: ### Lockhart
                    $ autograph = True #This unlocks the Lockheart tattoo in the wardrobe now.
                    $ h_request_wear_tattoos = True
                    $ hermione_wear_tattoos = True
                    $ hermione_tattoos_list.append("thigh/signature") #LOCKHEART TATTOO

                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("У меня был замечательный день, [genie_name]!","smile","happyCl",emote="06",xpos="right",ypos="base")
                    m "Рассказывай, [hermione_name]..."
                    call her_main("У меня сегодня был урок с профессором Локхартом...","grin","baseL")
                    her "[genie_name] Локонс такой очаровательный и умный и..."
                    call her_main("И прекрасный...","base","ahegao_raised")
                    m "Пожалуйста, избавь меня от подобных подробностей, [hermione_name]."
                    call her_main("[genie_name] Локонс даже любезно дал мне свой автограф...","smile","happyCl",emote="06")
                    m "Как любезно с его стороны."
                    call her_main("Да, не могу дождаться, чтобы показать его девочкам!","grin","baseL")
                    m "Хм... Могу я увидеть его?"
                    call her_main("[genie_name]?","base","base")
                    m "Автограф, [hermione_name]. Могу я увидеть?"
                    call her_main("Ну... Эм... Он в довольно интимной зоне, [genie_name].","upset","wink")
                    m "Что? Ну, следовательно, у профессора Лохона есть какие-то \"грязные\" делишки!"
                    call her_main("Это профессор Локонс, [genie_name]...","annoyed","angryL")
                    her "И... Эм..."
                    her "Ну, не {size=+5}настолько{/size} интимном..."
                    m "Покажи мне!"
                    call her_main("Нет, [genie_name]! Это было бы неуместно!","disgust","glance")

                    menu:
                        "{size=-3}\"Локонс вылетит из школы в ближайшее время!\"{/size}":
                            call her_main("Из-за меня?","scream","wide_stare")
                            call her_main("[genie_name], пожалуйста!","mad","worried",tears="soft")
                            m "Покажи мне!"
                            call her_main("Нет, это унизительно!","scream","worriedCl")

                            menu:
                                "\"Ладно. Держи свои очки.\"":
                                    call her_main("Спасибо за понимание, [genie_name].","base","happyCl")
                                "\"Покажи мне или ничего не получишь!\"":
                                    call her_main("Что?!","scream","wide_stare")
                                    call her_main("...............","annoyed","down")
                                    call her_main("..................","annoyed","worriedL")
                                    call her_main("Ну, хорошо, но только, чтобы очистить имя своего кумира ...","angry","angry")
                                    pause.5

                                    call her_main("Здесь....","disgust","down_raised",cheeks="blush",xpos="mid",ypos="base",trans="fade")

                                    call set_hermione_action("lift_skirt")
                                    pause.5

                                    m "Хм..."
                                    call her_main("","angry","annoyed",emote="01",xpos="right",ypos="base")
                                    call ctc

                                    call her_main("Как видите, профессор Локонс - не что иное, как воплощение всего чистого и мужественного!","annoyed","annoyed")
                                    pause
                                    m "Неужели?"
                                    her "Вы не должны беспокоиться о профессоре Локонсе, [genie_name]."
                                    her "Он не из тех \"пошлых\" учителей."
                                    m "Ах, да какое мне дело..."
                                    call her_main("............?","angry","annoyed",emote="01")

                                    call set_hermione_action("none")

                                    call her_main("","angry","angry")
                                    call ctc
                                    $ mad += 18

                        "\"Ладно. Держи свои очки.\"":
                            call her_main("Спасибо, [genie_name].","base","happyCl")

                #Event C
                elif one_out_of_three == 3: ### Filch
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Ну, я довольно долго флиртовала с мистером Филчем.","soft","base",xpos="right",ypos="base")
                    call her_main("Какой начитанный и исключительно воспитанный господин мистер Филч.","open","closed")
                    m "........"
                    call her_main("Но я не думаю, что кто-то знает его таким...","soft","baseL")
                    her "Не думаю, что кто-то знает мистера Филча, как я."
                    call her_main("Я чувствую, что он действительно открылся мне, [genie_name].","base","base")
                    m "Хорошо..."
                    m "Этот мистер Фли{size=+7}нт{/size}--"
                    call her_main("Его зовут мистер Филч, [genie_name].","open","angryCl")
                    m "Да, неважно... Он что, преподает здесь?"
                    her "Мистер Филч? Учитель? Нет, [genie_name]..."
                    call her_main("Он смотритель...","base","base")
                    m "Смотритель...?"
                    m "Хочешь сказать, он уборщик?"
                    call her_main("Ну...","open","worriedL")
                    m "[hermione_name], я не посылал тебя очаровывать школьных уборщиков!"
                    call her_main("Но мистер Филч является-частью школьного персонала, [genie_name]!","open","base")

                    menu:
                        "\"Просто забирай свои очки и уходи!\"":
                            call her_main(".........................","normal","base")
                        "\"Услуга провалена! Ты не получишь очков!\"":
                            $ mad +=15
                            call her_main("Но [genie_name]?","normal","frown")
                            m "Уходи, [hermione_name]."
                            call her_main(".........................................","angry","angry")

                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt

            #Third level.
            elif whoring >= 9:

                #Event A
                if one_out_of_three == 1: ### Filch
                    stop music fadeout 1.0
                    call her_main(".............................","normal","worriedCl",xpos="right",ypos="base")
                    her "....................................."
                    m "[hermione_name]?"
                    call her_main("[genie_name], я.....","angry","worriedCl",emote="05")
                    m "Что такое? Что случилось?"
                    call her_main("Ну...","annoyed","worriedL")
                    her "Это мистер Филч, [genie_name]..."
                    m "Дворник?"
                    call her_main("Я немного флиртовала с ним...","open","base")
                    her "И это было поначалу здорово..."
                    call her_main(".......................","annoyed","worriedL")
                    m "................?"
                    call her_main("И тогда...","open","base")
                    call her_main("Я не уверена, что должна...","annoyed","worriedL")
                    m "[hermione_name], если ты не собираешься говорить, ты можешь уйти."
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Он показал мне свою \"штуку\", [genie_name]!","scream","worriedCl")
                    m "Его что?"
                    call her_main("Его... достоинство, [genie_name].","angry","worriedCl",emote="05")
                    g9 "Так держать, мужик-уборщик!"
                    call her_main("Что?!","scream","wide_stare")
                    m "*Кхем* Я имею в виду, это возмутительно!"
                    call her_main("Да... Мерзкая кривая штука, вся в венах...","angry","base",tears="soft")
                    m "Избавь меня от этих ужасных подробностей, [hermione_name]."
                    call her_main("Зачем он сделал такое?","mad","worriedCl",tears="soft_blink")
                    her "Секунду назад, мы просто разговаривали, а потом..."
                    m "Чтож, твоя, такая благородная жертва, не останется незамеченной, [hermione_name]!"
                    m "Пятнадцать очков \"Грифф--"
                    call her_main("Профессор, пожалуйста подождите.","soft","base",tears="soft")
                    m "А?"
                    call her_main("Ну, разве вы не собираетесь что-то сделать по этому поводу?","open","base")
                    m "Ну..."
                    call her_main("Что, если я не первая жертва..?","angry","angry")
                    her "Какой-нибудь несчастный первокурсник может получить травму на всю жизнь!"
                    m "Действительно может?"
                    call her_main("Это значит, что вы примете меры, [genie_name]?","open","base")
                    m "Эм... Да, конечно..."
                    m "Запишу его в свой \"список\"..."
                    m "\"Позаботиться о дворнике и его жутко кривом члене.\"..."
                    m "Да, завтра же, в первую очередь."
                    call her_main("Спасибо [genie_name].","open","closed")
                    call her_main("Могу я получить свои очки?","smile","happyCl")

                #Event B
                elif one_out_of_three == 2: ### Snape
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Профессор Снейп!","angry","angry",emote="01",xpos="right",ypos="base")
                    m "Эм... Ага, я, почти уверен, что я Дамблдор, вроде как..."
                    call her_main("[genie_name], пожалуйста, вам нужно выслушать меня!","open","base")
                    m "Да, да, [hermione_name], я слушаю."
                    call her_main("Я нашла подтверждение тому, что профессор Снейп коррумпирован и занимается \"грязными\" делами, [genie_name]!","open","angryCl")
                    m "Расскажи мне, что случилось."

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade

                    call her_head("Ну, сегодня во время занятий...","open","base",xpos="base",ypos="base")
                    call her_head("Я делала все возможное, чтобы привлечь внимание профессора Снейпа...","open","baseL")
                    call her_head("Я смотрела на него \"влюбленным взглядом\"...","open","down")
                    call her_head("И я следила за его промежностью...","soft","baseL")
                    m "Ты..."
                    m "Смотрела на его промежность?"
                    call her_head("Да... Я имею в виду, когда вы смотрите туда и хотите кое-что от него...","open","angryCl")
                    m "Откуда ты все это знаешь?"
                    call her_head("Из женского журнала...","open","worriedL")
                    call her_head("Ну, в любом случае, это сработало, [genie_name].","normal","frown")

                    hide screen blkfade
                    show screen snape_groping
                    with fade
                    call ctc

                    call her_head("Как только занятие закончилось, профессор Снейп схватил меня за ягодицы, [genie_name]!","angry","angry")
                    m "Дьявол!"
                    m "Однако, тебе понравилось?"
                    call her_head("[genie_name], я делаю это--","scream","angryCl")
                    m "\"Во имя чести \"Гриффиндора\" и все такое. Да, помню я."
                    call ctc

                    hide screen snape_groping
                    with fade

                    m "Держи свои очки."
                    show screen blktone
                    call her_main("","disgust","glance",xpos="right",ypos="base")

                #Event C
                elif one_out_of_three == 3: ### Lockhart
                    stop music fadeout 1.0
                    call her_main("Профессор Локонс!","annoyed","frown",xpos="right",ypos="base")
                    m "Понял! Добавляем его в \"список непослушных\"!"
                    call her_main("Нет, [genie_name], дело не в этом...","open","worried")
                    call her_main("или...","annoyed","angryL")
                    her "Я не уверена..."
                    call her_main("Я его обожаю...","open","worried")
                    call her_main("Но он...","soft","baseL")
                    her "Он просто..."
                    call her_main("Но, как это возможно?","mad","worriedCl",tears="soft_blink")
                    her "Не могу в это поверить..."
                    hide screen hermione_main
                    with d3
                    call play_music("playful_tension") # SEX THEME.
                    m "{size=-4}(Ах! Ожидание убивает меня!){/size}"
                    m "{size=-4}(Он заставил ее отсосать ему?){/size}"
                    m "{size=-4}(Он изнасиловал ее?){/size}"
                    g4 "Что произошло, [hermione_name]? Рассказывай!"
                    call her_main("А?","open","base")
                    m "Что сделал профессор Локонс?"
                    call her_main("Эм... Ничего, [genie_name]...","soft","baseL")
                    m "Ничего?!"
                    call her_main("Да. Я, конечно, загнала его в угол сегодня...","open","worried")
                    call her_main("И еще старалась выглядеть доступной для него...","open","base")
                    m "Серьезно?"
                    call her_main("Да... Не знаю, что на меня нашло, [genie_name]...","angry","worriedCl",emote="05")
                    m "Чем все закончилось, [hermione_name]?"
                    call her_main("Сначала выслушайте меня [genie_name], пожалуйста!","scream","worriedCl")
                    m "Мои извинения. Пожалуйста, продолжай."
                    call her_main("Ну, я всегда знала, что мистер Локонс был настоящим джентльменом и...","open","base")
                    her "И... и я просто хотела очистить его имя от всех этих подозрений раз и навсегда..."
                    call her_main("...............","annoyed","worriedL")
                    her "Ну, мистер Локонс не отверг меня..."
                    m "Ты меня убиваешь [hermione_name]!"
                    m "Он не отверг тебя, но и не изнасиловал..."
                    m "Тогда что произошло?"
                    call her_main(".............","normal","worriedCl")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Я заставила его плакать, [genie_name]...","angry","worriedCl",emote="05")
                    m "..............подожди.......что?"
                    call her_main("Он посмотрел на меня растерянным взглядом, а потом зарыдал...","angry","worried")
                    her "Он выглядел так, будто искренне боялся меня, [genie_name]."
                    call her_main("Я думаю...","annoyed","worriedL")
                    her "Думаю, мистер Локонс боится женщин..."
                    m "Боится женщин?"
                    m "Что это значит?"
                    call her_main("Что он любит мальчиков, [genie_name]?","angry","worriedCl",emote="05")
                    m "Oх..."
                    call her_main("............","upset","wink")
                    m "..........."
                    m "Держу пари, это был травмирующий опыт для тебя, [hermione_name]."
                    call her_main("Был, [genie_name]...","open","base")
                    m "Я, надеюсь, эти очки поднимут тебе настроение."

    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    her "Спасибо, [genie_name]."

    $ hg_pr_FlirtTeacher_OBJ.points += 1
    $ hg_pr_FlirtTeacher_OBJ.inProgress = False

    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1
    if whoring >= 5 and hg_pr_FlirtTeacher_OBJ.points >= 2:
        $ hg_pr_FlirtTeacher_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
