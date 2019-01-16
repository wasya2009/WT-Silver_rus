

### Flirt With Classmate ###

##(Level 01) (5 pt.) (Flirt with classmates). (Available during daytime only).
label hg_pr_FlirtClassmate:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_FlirtClassmate_OBJ.points < 1:
        m "{size=-4}(Попросить ее флиртовать с парнями из  \"Слизерина\"?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    m "[hermione_name]?"
    call her_main("Да?","soft","baseL",xpos="right",ypos="base")

    #Intro.
    if hg_pr_FlirtClassmate_OBJ.points == 0 and whoring < 6: ### LEVEL 01 and LEVEL 02

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "Как ты относишься к мальчикам из \"Слизерина\"?"
        call her_main("Я их ненавижу, [genie_name].","angry","angry")
        m "Что ж, очень жаль. Потому что я хочу, чтобы ты подружилась с некоторыми из них."
        call her_main("Если я должна...","soft","baseL")
        her "Да, я думаю, что смогу быть вежливой с ними в течение одного дня."
        m "Да, и когда я говорю \"подружиться с ними...\""
        m "Я имею в виду, что нужно с ними флиртовать..."
        call her_main("Флиртовать?!","shock","wide")
        call her_main("[genie_name]!","angry","angry")
        call her_main("Я даже не собираюсь спрашивать, почему вас это интересует, [genie_name]...","annoyed","suspicious")
        call her_main("Но почему \"Слизерин\"?","open","worried")
        her "Если вам нужно, чтобы я кокетничила с ними, я думаю, что смогу это сделать..."
        her "Но, пожалуйста, можно мне другой факультет?"
        call her_main("Может быть\"Гриффиндор\"?","upset","wink")
        m "Я лишь пытаюсь защитить твою репутацию, [hermione_name]."
        call her_main("[genie_name]?","soft","base")
        m "Ценишь ли ты мнение о себе от студентов \"Слизерина\"?"
        call her_main("Мне наплевать на мнение этих неандертальцев.","scream","angryCl")
        m "Как насчет студентов \"Гриффиндора\"?"
        call her_main("Их мнение очень значит для меня--","annoyed","worriedL")
        call her_main("Oх, я поняла...","base","base")
        m "Точно... Я просто забочусь о тебе. [hermione_name]."
        her "Эм... Спасибо [genie_name]..."

    #Second time event.
    else:

        if whoring < 3:
            m "Я хочу чтоб у тебя появились друзья из \"Слизерина\"."
            her "Вы хотите чтоб я снова флиртовала с мальчиками из \"Слизерина\" [genie_name]?"
            m "Это именно то, что мне нужно, [hermione_name]."
            call her_main("Правда я должна делать это [genie_name]?","open","base")
            m "Мы уже проходили через это, [hermione_name]."
            m "Идти к мальчикам \"Слизерина\" в твоих интересах."
            call her_main("Да, я знаю, [genie_name].","open","angryCl")
            her "Но почему я должна делать это вообще?"
            m "Никто тебя не заставляет, [hermione_name]..."
            call her_main("Вам не нужно напоминать мне об этом, [genie_name]...","angry","angry")
            call her_main("Хорошо, если так надо... [genie_name]...","normal","frown")

        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ##
            m "Я хочу, чтобы ты пофлиртовала с мальчиками из  \"Слизерина\"."
            her "Посмотрю, что можно сделать, [genie_name]."
            m "Отлично. Я жду твой отчет после занятий.."

    her "Ну, я лучше пойду. Занятия вот-вот начинутся..."

    $ hg_pr_FlirtClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_FlirtClassmate_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First time event.
    call her_main("Добрый день, [genie_name].","base","base",xpos="right",ypos="base")
    m "[hermione_name]..."
    m "Ты выполнила мое задание?"
    her "Я сделала, как вы просили, [genie_name]..."

    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Расскажи мне в деталях.\"":
            hide screen hermione_main
            with d3
            m "Со сколькими парнями ты флиртовала, [hermione_name]?"
            m "Расскажи подробнее."
            call blktone

            #First Level.
            if whoring >= 0 and whoring < 3:

                #Event A
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    call her_main("Ну...","open","worriedL",xpos="right",ypos="base")
                    her "Там был один первокурсник..."
                    her "........."
                    m "Я слушаю..."
                    her "Ну... Я подошла к нему и сказала: \"Привет, красавчик!\"."
                    m "И?"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Он показал мне язык и убежал, [genie_name].","normal","frown")
                    m "Ты пыталась заманить его леденцом?"
                    call her_main("Я, нет, [genie_name]...","open","worriedL")
                    her "Эта мысль не приходила мне в голову, но--"
                    m "Это была шутка, [hermione_name]."
                    call her_main("[genie_name]?","normal","frown")
                    m "Я отправил тебя туда не для того, чтобы преследовать маленьких детей!"
                    call her_main(".............","annoyed","frown")
                    m "Я говорил тебе флиртовать с мальчиками. {size=+5}Твоего возраста{/size}!"
                    call her_main("Я хотела сначала, но...","normal","frown")
                    call her_main("Наверное, я испугалась...","annoyed","angryL")
                    her "Я сильно презираю  \"Слизеринцев\", чтобы флиртовать с ними, [genie_name]!"
                    call her_main("Я должна была бы бороться со своим рвотным рефлексом!","angry","angry")
                    menu:
                        "\"Ладно. Просто постарайся в следующий раз.\"":
                            call her_main("Спасибо, [genie_name].","base","base")
                            her "Я буду, обещаю!"
                        "\"Задание провалено. Очков не получишь!\"":
                            stop music fadeout 1.0
                            call her_main("Я поняла...","normal","frown")
                            m "Убирайся с глаз моих..."
                            call her_main("Да, [genie_name]... Простите, [genie_name]...","annoyed","frown")

                            $ hg_pr_FlirtClassmate_OBJ.inProgress = False
                            jump could_not_flirt

                #Event B
                elif one_out_of_three == 2:
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Ну, я пыталась со старшеклассником...","open","worriedL",xpos="right",ypos="base")
                    m "Он оценил это?"
                    call her_main("Он назвал меня \"Гриффиндорской шлюхой\", [genie_name]!","angry","angry",emote="01")
                    m "Понятно..."
                    m "Что ты тогда сделала?"
                    call her_main("Ну, это был не правильный способ обратиться к ученику \"Хогвартса\"...","open","angryCl")
                    her "Поэтому я сказал, что донесу о нем."
                    m "По-настоящему захватывающая история..."
                    m "Что-нибудь еще?"
                    call her_main("Да, в библиотеке был еще один студент...","annoyed","frown")
                    her "Очевидно, он пытался исправить какую-то ошибку..."
                    her "Поэтому, я предложила свою помощь..."
                    m "И?"
                    call her_main("Он назвал меня \"Главной шлюхой Гриффиндора\", [genie_name]...","angry","angry",emote="01")
                    m "Ты угрожала донести на него об этом?"
                    call her_main("Конечно, [genie_name].","open","angryCl")
                    m "*Вздох*"
                    m "Что-нибудь еще?"
                    call her_main("Ну, был еще один случай, но результат был почти таким же...","annoyed","frown")
                    m "\"Гриффиндорская шлюха\"?"
                    call her_main(".........Да, [genie_name].","disgust","glance")
                    m "Ты все делаешь неправильно, [hermione_name]."
                    call her_main("Простите, [genie_name]. Я думала, что это будет легко...","annoyed","angryL")
                    menu:
                        "\"Ну, по крайней мере, ты пытаешься.\"":
                            call her_main("Очевидно, флирт-не моя сильная сторона...","angry","worriedCl",emote="05")
                        "\"Задание провалено. Очков не получишь!\"":
                            stop music fadeout 1.0
                            call her_main("Вы не собираетесь заплатить мне, [genie_name]?","open","worried")
                            $ mad +=15
                            call her_main("Но вы обещали!","angry","base",tears="soft")
                            call her_main("................","mad","worriedCl",tears="soft_blink")

                            $ hg_pr_FlirtClassmate_OBJ.inProgress = False
                            jump could_not_flirt

                #Event C
                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main("Ну, команда \"Слизерин\" по квиддичу сегодня тренировалась на стадионе...","open","worriedL",xpos="right",ypos="base")
                    her "Я думала, что смогу пробраться на трибуны и подбодрить их..."
                    call her_main("Но...","annoyed","angryL")
                    m "Да?"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Все эти \"Слизеринские\" шлюхи уже были там, [genie_name].","angry","angry")
                    her "Они кричали и подбадривали..."
                    call her_main("И одна из них даже выставила себя неподобающим образом перед игроками, [genie_name]...","angry","angry")
                    her "Я не могу поверить, что наша школа допускает такое поведение..."
                    m "Так... чем закончилась эта увлекательная драма?"
                    call her_main("Я просто ушла [genie_name]...","annoyed","angryL")
                    menu:
                        m "Хм..."
                        "\"Хорошо, вот твои очки.\"":
                            call her_main("Спасибо, [genie_name]...","open","closed")

                        "\"Задание провалено. Очков не получишь!\"":
                            stop music fadeout 1.0
                            call her_main("В любом случае, я не чувствую, что их заслужила...","annoyed","angryL")

                            $ hg_pr_FlirtClassmate_OBJ.inProgress = False
                            jump could_not_flirt

            #Second Level.
            elif whoring >= 3 and whoring < 6:

                #Event A
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    call her_main("Ну, был один парень в библиотеке...","open","worriedL",xpos="right",ypos="base")
                    her "Очевидно, он не мог решить какое-то задание, поэтому я предложила свою помощь..."
                    m "И?"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("К моему удивлению, он согласился...","smile","happyCl")
                    her "Он дал мне закончить задание за него..."
                    call her_main("Пока я работала, он сделал несколько неуместных комментариев, но я просто улыбнулась в ответ...","angry","worriedCl",emote="05")
                    m "Так, по сути, он был тем, кто флиртовал..."
                    call her_main("Ну... да.","grin","worriedCl",emote="05")
                    call her_main("Но, несмотря на мое здравомыслие, я поощряла его неподобающее поведение...","base","base")
                    m "Молча?"
                    her "Да, [genie_name]..."
                    her "Я имею в виду, это действительно что-то, верно?"
                    m "Эх..."
                    m "Что еще у тебя есть для меня?"
                    call her_main("Точно...","annoyed","angryL")
                    her "Позже, в коридоре два других парня похвалили мою внешность в очень вульгарной манере..."
                    call her_main("Но я просто улыбнулась...","angry","worriedCl",emote="05")
                    m "Ты снова делала не то..."
                    m "Это не то, что я приказал тебе сделать, [hermione_name]."
                    call her_main("Я знаю, [genie_name]!","angry","worriedCl",emote="05")
                    call her_main("Но я действительно очень занята. Между \"ДПМ\" встречами и занятиями...","annoyed","angryL")
                    her "У меня почти нет времени--"
                    m "Это все, что у тебя есть для меня?"
                    call her_main("Нет, [genie_name].","annoyed","angryL")
                    her "По дороге сюда я столкнулась с Драко Малфоем, [genie_name]."
                    m "Не может быть!!! (Понятия не имею, кто это...)"
                    her "Я заставила себя быть с ним дружелюбной..."
                    call her_main("Мы закончили наш разговор довольно прилично.","base","happyCl")
                    m "Понятно... этот \"темный\" парень... (прим.Drako - Драко, Dark-Ох - темный)"
                    m "Он вообще смотрел на твои ноги?"
                    call her_main("Что?","open","base")
                    m "Он пялился на твои ноги или нет, [hermione_name]?"
                    call her_main("Эм... Возможно...","upset","wink")
                    m "Что на счет сисек?"
                    call her_main("[genie_name]!!!","angry","angry")
                    m "Ладно. Получай свои очки. Продолжай в том же духе."
                    call her_main("","annoyed","worriedL")

                #Event B
                elif one_out_of_three == 2:
                    stop music fadeout 1.0
                    call her_main("Ну...","open","worriedL",xpos="right",ypos="base")
                    her "Сегодня утром я флиртовала с одним парнем..."
                    call her_main("Через пару минут уже с другим парнем...","soft","baseL")
                    call her_main("А потом случилось что-то странное...","angry","worried")
                    call play_music("playful_tension") # SEX THEME.
                    her "Этот злобный парень из \"Слизерина\" подошел ко мне и пригласил на свидание..."
                    call her_main("Я сначала сказала \"нет\", но в итоге мы пошли гулять вместе.","soft","baseL")
                    m "Тебе понравилось, [hermione_name]?"
                    call her_main("Я думаю, да, [genie_name]... К моему собственному удивлению...","open","base")
                    call her_main("В нем было какое-то \"наплевательское\" отношение...","base","base")
                    call her_main("Он был таким уверенным и спокойным...","base","happyCl")
                    call her_main("Я конечно все еще ненавижу \"Слизеринцев\"!","angry","worriedCl",emote="05")
                    call her_main("Но...","annoyed","down")
                    her "Может быть, кто-то из студентов попал туда по ошибке?"
                    call her_main("Может \"сортировочная шляпа\" совершила... ошибку?","open","worriedL")
                    menu:
                        "\"Просто возьми свои очки и иди!\"":
                            call her_main("................","normal","frown")
                        "\"Всемогущая шляпа никогда не ошибается!\"":
                            call her_main("Да, конечно... Всем известно...","soft","baseL")
                        "\"Ты действительно так думаешь?\"":
                            call her_main("Oх, забудьте, [genie_name].","soft","baseL")
                            her "Всем известно, что \"Сортировочная шляпа\" никогда не ошибается."

                #Event C
                elif one_out_of_three == 3:
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Пять мальчиков, [genie_name]!","smile","happyCl",xpos="right",ypos="base")
                    m "Серьезно?"
                    call her_main("Да!","base","happyCl")
                    call her_main("Один парень, сегодня утром.","base","happyCl")
                    her "Потом еще два, сразу после первого."
                    her "А потом еще один."
                    call her_main("И после этого, у меня был удивительно приятный разговор еще с одним.","grin","baseL")
                    call her_main("Он оказался весьма умным и неплохо воспитанным.","base","happyCl")
                    her "............................"
                    her "................"
                    call her_main("Но мое мнение о \"Слизерине\" останется прежним, [genie_name].","angry","worriedCl",emote="05")
                    m "Я не прошу тебя менять его, [hermione_name]."
                    her "Я делаю это, чтобы помочь своему факультету!"
                    call her_main("Гордому факультету \"Гриффиндор\"!","scream","worriedCl")
                    m "Хорошо, хорошо. Успокойся, [hermione_name]."
                    call her_main("","base","happyCl")

            #Third Level.
            elif whoring >= 6:

                #Event A
                if one_out_of_three == 1:
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    $ sc34CG(2, 7, 1, 1)
                    call her_main("Одиннадцать мальчиков, [genie_name]!","smile","happyCl",xpos="right",ypos="base")
                    m "Одиннадцать? Серьезно? Твой личный рекорд, [hermione_name]."
                    call her_main("Да.","base","happyCl")
                    call her_main("Давайте пересчитаем...","grin","baseL")
                    her "Сперва два красавчика..."
                    call her_main("Затем я обменялась несколькими, довольно, неуместными фразами с другим парнем.","smile","glance")
                    call her_main("После этого был еще один парень...","grin","baseL")
                    call her_main("Потом другие трое парней...","annoyed","down")
                    call her_main("Затем еще один...","base","happyCl")
                    call her_main("И, наконец, последний парень, который проводил меня до вашей башни, [genie_name]...","smile","happyCl")
                    m "Значит, одиннадцать?"
                    m "Те мальчики из \"Слизерина\" начинают тебе нравится?"
                    $ sc34CG(2, 7, 1, 2)
                    call her_main("Я полагаю, да...","base","happyCl")
                    call her_main("Ну, не все из них были добры ко мне поначалу...","annoyed","down")
                    call her_main("Но, я использую один трюк, чтобы \"приручить\" их.","smile","glance")
                    m "Трюк?"
                    $ sc34CG(2, 6, 1, 1)
                    call her_main("Да... Всякий раз, когда мальчики из \"Слизерина\" обзывают меня...","base","happyCl")
                    her "Я просто улыбаюсь."
                    m "Хм..."
                    m "Так, например, если кто-то назовет тебя \"шлюхой\", ты просто улыбнешься?"
                    call her_main("Да, [genie_name]...","angry","worriedCl",emote="05")
                    m "Да, я уверен, что ты приручишь их."
                    m "Прекрасная работа, [hermione_name]."
                    call her_main("","grin","baseL")
                    hide screen sccg
                    with d3

                #Event B
                elif one_out_of_three == 2:
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Два свидания, семь приятных разговоров...","smile","happyCl",xpos="right",ypos="base")
                    call her_main("И я даже позволила одному парню поцеловать меня...","grin","baseL")
                    m "Весьма внушительно, [hermione_name]."
                    call her_main("Я так тоже думаю, [genie_name]. Спасибо.","base","happyCl")
                    call her_main("А еще там был маленький первокурсник...","smile","happyCl")
                    her "Я пыталась флиртовать и с ним, но в итоге мы просто болтали..."
                    her "Он называл меня \"мисс Гермиона\"..."
                    her "Это так очаровательно..."
                    m "Ну, я не посылал тебя приставать к детям, [hermione_name]."
                    call her_main("Я не приставала--","disgust","glance")
                    call her_main("[genie_name]! Семь раз флиртовала и два свидания - стоят этих очков, не так ли?","angry","worriedCl",emote="05")
                    m "Oх, абсолютно."
                    call her_main("Тогда, можно их получить...","scream","angryCl")
                    call her_main("","normal","worriedCl")

                #Event C
                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main("[genie_name], простите, но...","normal","worriedCl",xpos="right",ypos="base")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Я ненавижу этих \"Слизеринских\" ублюдков, [genie_name]!","angry","angry")
                    m "Скажи мне, что случилось."
                    call her_main("Я не хочу говорить об этом...","annoyed","angryL")
                    m "Скажи мне, что случилось, [hermione_name]!"
                    call her_main("Я не хочу говорить об этом, [genie_name].","angry","angry",emote="01")
                    call her_main("Пожалуйста, не заставляйте меня...","annoyed","angryL")
                    menu:
                        "\"Ладно. Не буду.\"":
                            call her_main("Спасибо, [genie_name].","normal","worriedCl")
                            m "Сегодня тебе не повезо с флиртом?"
                            call her_main("Oх, совсем наоборот, [genie_name].","angry","worriedCl",emote="05")
                            call play_music("playful_tension") # SEX THEME.
                            her "Сегодня один из мальчиков отвел меня в комнату отдыха \"Слизерина\"..."
                            call her_main("Их там было как минимум двенадцать...","normal","base")
                            call her_main("Все мальчики знали, кто я такая...","open","angryCl")
                            her "Сначала я была в центре их внимания..."
                            call her_main("И чувствовала себя как-то замечательно...","base","ahegao_raised")
                            call play_music("chipper_doodle") # HERMIONE'S THEME.
                            call her_main("А потом на меня накинулась кучка этих \"Слизеринских\" шлюх...","disgust","glance")
                            m "И?"
                            call her_main("Ну, они делали и говорили всякое такое...","annoyed","angryL")
                            her "В любом случае, мне пришлось уйти..."
                            m "Понятно..."
                            m "Я думаю, что ты заслуживаешь свои очки в любом случае, [hermione_name]."
                            call her_main("","base","happyCl")

                        "\"Скажи мне или потеряешь очки!\"":
                            $ mad +=10
                            call her_main("[genie_name], пожалуйста, я не хочу обсуждать это с вами, [genie_name].","disgust","glance")
                            m "Никто тебя не заставляет, [hermione_name]."
                            m "Ты можешь идти."
                            call her_main("{size=-4}(Упрямый старик!){/size}","angry","angry")

                            $ hg_pr_FlirtClassmate_OBJ.inProgress = False
                            jump could_not_flirt

    $ gryffindor +=5
    m "\"Гриффиндор\" получает 5 очков!"
    her "Спасибо, [genie_name]."

    $ hg_pr_FlirtClassmate_OBJ.points += 1
    $ hg_pr_FlirtClassmate_OBJ.inProgress = False

    if whoring <= 2:
        $ whoring +=1
    if whoring >= 2 and hg_pr_FlirtClassmate_OBJ.points >= 2:
        $ hg_pr_FlirtClassmate_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
