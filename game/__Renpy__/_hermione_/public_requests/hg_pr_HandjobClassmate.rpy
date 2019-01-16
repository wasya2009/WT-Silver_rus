

### Give Classmate A Handjob ###

##(Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label hg_pr_HandjobClassmate: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main
    with d3

    $ current_payout = 55 #Used when haggling about price of the favour.

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_HandjobClassmate_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтоб она подрочила одному из своих одноклассников?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro
    if hg_pr_HandjobClassmate_OBJ.points == 0:

        if whoring < 15 or hg_pr_KissAGirl_OBJ.points < 2:
            m "[hermione_name], я хочу, чтобы ты сегодня сделала что-то необычное..."
            call her_main("...?","normal","frown",xpos="right",ypos="base")
            m "Я хочу, чтобы ты подрочила своему однокласснику."
            jump too_much

        m "[hermione_name], я хочу, чтобы ты сегодня сделала что-то новенькое..."
        call her_main("...........","soft","base",xpos="right",ypos="base")
        m "Я хочу, чтобы ты занялась сексом с одним из твоих одноклассников."
        stop music
        with hpunch
        call her_main("{size=+5}Что?!!{/size}","shock","wide")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Теперь вы сделали это, [genie_name]! Вы пересекли черту!","angry","angry")
        her "Я знаю, что в прошлом я продала вам, пару довольно сомнительных услуг..."
        with vpunch
        call her_main("{size=+5}Но ЭТО?!{/size}","scream","angry",emote="01")
        her "Я не могу поверить, что вы просите одну из своих учениц, за... за..."
        call her_main("Все кончено, [genie_name]!","angry","angry",emote="01")
        m "Хорошо, хорошо, ты можешь успокоиться?"
        call her_main("Я точно не успокоюсь, [genie_name]! Это за гранью приемлемого!","scream","angryCl")
        m "Хорошо, ладно, возможно, на этот раз я действительно немного перегнул палку..."
        call her_main("Немного [genie_name]?! Немного?!!","angry","angry")
        m "Да, я извиняюсь..."
        call her_main(".........","annoyed","annoyed")
        m "Как насчет того, чтобы попробовать что-то меньшее... увлекательное?"
        call her_main("............","upset","closed")
        m "Я готов дать \"Гриффиндору\" пятьдесят пять очков."
        m "Все, что я попрошу взамен..."
        call her_main("..........?","angry","angry",cheeks="blush")
        m "...так это выйти и подрочить какому-нибудь счастливчику..."
        call her_main("!!!......","angry","angry")
        m "Ой, да брось... Всего лишь разок."
        call her_main("...","disgust","glance")
        m "Пятьдесят пять очков..."
        call her_main("..............","annoyed","angryL")
        call her_main("Я рада, что вы одумались, [genie_name].","annoyed","annoyed")
        m "Ох, конечно. Спасибо за заботу."
        m "Это значит, что ты согласна?"
        call her_main("Я готова попробовать...","annoyed","angryL")
        m "Великолепно... Увидимся позже."

    #Second time event.
    else:

        #First level.
        if whoring >= 15 and whoring < 18:
            m "Сегодняшней услугой, будет..."
            call her_main(".........","angry","base",xpos="right",ypos="base")
            m "Ублажение ручкой любого парня! На твой выбор!"
            call her_main("...Опять?","angry","down_raised")
            m "Конечно, почему бы и нет?"
            m "И еще пятьдесят пять очков \"Гриффиндору\"."
            call her_main("..........","annoyed","worriedL")
            m "Так... ты не против, [hermione_name]?"
            call her_main("Я посмотрю, что смогу сделать...","annoyed","angryL")
            m "Великолепно!"

        #Second level.
        elif whoring >= 18 and whoring < 21:
            m "Готова пойти и заняться сексом с одноклассником?"
            stop music fadeout 1.0
            call her_main("Что?","scream","wide_stare",xpos="right",ypos="base")
            call her_main("Конечно нет! Я никогда--","scream","angryCl")
            m "Тогда, как насчет подрочить?"
            call her_main("...............","annoyed","angryL")
            m "Да ладно тебе. Ты уже делала это раньше."
            call her_main("Хм..........","annoyed","annoyed")
            her "Пятьдесят пять очков?"
            m "Естественно."
            call her_main("Что ж, хорошо... я посмотрю, что смогу сделать...","angry","down_raised")

        #Third level.
        elif whoring >= 21:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Что ты думаешь о том, чтобы подарить очередному однокласснику оргазм с помощью своих ручек?"
            call her_main("Я не против, [genie_name].","annoyed","down",xpos="right",ypos="base")
            m "Серьезно?"
            call her_main("Да... Я имею в виду, это просто мастурбация...","grin","baseL")
            m "Отлично. Удачи, тогда!"
            m "И сообщи мне, как обычно обо всем после занятий."
            call her_main("Конечно, [genie_name].","base","happyCl")

    $ hg_pr_HandjobClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_HandjobClassmate_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First level.
    if whoring >= 15 and whoring < 18:

        #Event A
        if one_out_of_three == 1:
            m "[hermione_name], как прошло?"
            show screen blktone
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Довольно ужасно... конечно...","annoyed","frown",xpos="right",ypos="base")
            m "Просто скажи мне, что случилось, [hermione_name]..."
            call her_main("Я выставила себя полной дурой, вот что случилось, [genie_name].","disgust","glance")
            her "....."
            m "..."
            call her_main("..........","annoyed","worriedL")
            call her_main("Я не хочу об этом говорить...","annoyed","angryL")
            her "Вы сказали мне пойти и потрогать пенис мальчика, и я сделала это, [genie_name]."
            call her_main("Пожалуйста, просто начислите мне очки, [genie_name]...","open","base")
            m "Я не сказал \"идти и трогать пенис мальчика\", [hermione_name]."
            m "Я сказал тебе, чтобы ты подрочила своему однокласснику."
            call her_main("Ну, да... я про это и имела в виду...","annoyed","annoyed")
            m "Он кончил?"
            call her_main("[genie_name]?","open","base")
            m "Его \"пи-пи\" выстрелила в тебя белой жидкостью, [hermione_name]?"
            call her_main("Ну...","annoyed","worriedL")
            call her_main("Нет...","normal","worriedCl")

            menu:
                "\"Ну, тогда это не считается.\"":
                    stop music fadeout 4.0
                    call her_main("Что?","angry","wide",xpos="right",ypos="base")
                    her "Но, [genie_name], я..."
                    m "Если ты не заставила его кончить, то это не мастурбация. Точка."
                    call her_main("Но... Но, что это тогда было... ?","angry","base")
                    m "Откуда мне это знать? Массаж члена?"
                    call her_main("Пфф...","angry","down_raised")
                    her "Но я действительно старалась изо всех сил..."
                    m "Нет дрочки - нет очков, [hermione_name]."
                    call her_main(".....","angry","base")
                    m "Ты можешь идти, [hermione_name]."
                    call her_main(".........","annoyed","angryL")
                    $ mad +=9

                    $ hg_pr_HandjobClassmate_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

                "\"Ты получишь только половину очков.\"":
                    $ current_payout = 27 #Used when haggling about price of th favour.
                    call her_main("Ох...?","open","base",xpos="right",ypos="base")
                    m "В чем проблема, [hermione_name]?"
                    call her_main("Не в чем [genie_name]... Это справедливо, я полагаю...","angry","down_raised")
                    m "Конечно!"

                "\"Ты попробовала. Вот твои очки.\"":
                    call her_main("Правда?","angry","base",xpos="right",ypos="base")
                    call her_main("Спасибо, [genie_name]!","open","down")
                    call her_main("Обещаю, в следующий раз постараюсь!","base","base")
                    call her_main("Эм... В смысле, если вы попросите подобную услугу в будущем...","upset","wink")

        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name], как все прошло?"
            show screen blktone
            call her_main("Хорошо, [genie_name]...","open","base",xpos="right",ypos="base")
            call play_music("playful_tension") # SEX THEME.
            her "Я спросила у мальчика из \"Гриффиндора\" сделать \"это\" с ним..."
            call her_main("К моему удивлению, он охотно согласился.","open","base",cheeks="blush")
            m "Поразительно..."
            call her_main("Поэтому мы спрятались за одним из тех огромных гобеленов в восточном крыле...","open","closed")
            call her_main("И я... дрочила ему, пока он не кончил...","annoyed","angryL")
            her "........."
            call her_main("И я попросила его держать все в секрете, но...","angry","base")
            m "В чем дело, [hermione_name]?"
            m "Сомневаешься в честности своих собратьев \"Гриффиндорцев\"?"
            call her_main("Конечно нет, [genie_name].","upset","closed")
            call her_main("...........................","angry","down_raised")
            call her_main("Однако... Выполнение такого рода услуг может нанести серьезный ущерб моей репутации....","angry","base")
            m "Это твой новый способ попросить прибавки, [hermione_name]?"
            m "Пятьдесят пять очков - это максимум за эту услугу."
            call her_main("Oх... Конечно...","angry","down_raised")
            m "Конечно, если ты еще не изменила свое мнение о сексе со своим одноклассником?"
            call her_main("Что?","shock","wide")
            call her_main("[genie_name], я не проститутка!","angry","down_raised")
            m "Что ж, в таком случае..."

        #Event C
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            m "[hermione_name], как прошло?"

            $ aftersperm = True #Shows stains on Hermione's uniform.
            $ uni_sperm = True  #Universal sperm.
            $ u_sperm = "characters/hermione/face/auto_08.png"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("Ужасно, [genie_name]. Просто ужасно...","scream","worriedCl",xpos="right",ypos="base")
            m "У тебя что-то... в волосах..."
            call her_main("Где?","open","base")
            call her_main("O нет! Я думала, что все вытерла...","open","baseL",cheeks="blush")
            show screen ctc
            pause
            show screen blkfade
            with d3
            pause.5
            $ uni_sperm = False  #Universal sperm.
            call her_main("","upset","closed")
            hide screen blkfade
            with d3
            pause
            hide screen ctc
            m "Хм... Итак, я полагаю, что ты выполнила свое задание?"
            call her_main("Да, [genie_name]...","annoyed","angryL")
            m "Тогда в чем проблема?"
            call her_main("..........","annoyed","worriedL")
            call her_main("Все мальчики-придурки! Вот в чем проблема, [genie_name]!","scream","angryCl")
            call her_main("Я хорошо подрочила этому мальчику...","open","down")
            her "И знаете, как он меня отблагодарил?"
            call her_main("Он заляпал меня в своей сперме...","scream","angry",emote="01")
            call her_main("И я знаю, что он сделал это нарочно!","scream","angryCl")
            call her_main("Противный, \"Когтевранец\"...","annoyed","worriedL")
            m "А я бы сказал, что работа выполнена на отлично!"

    #Second level.
    elif whoring >= 18 and whoring < 21:

        #Event A
        if one_out_of_three == 1:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            with d3
            call her_main("Эм...","open","base",xpos="right",ypos="base")
            her "Еще нет, [genie_name]..."
            m "\"Еще нет\"?"
            call her_main("Да... Позвольте мне объяснить, [genie_name]...","annoyed","worriedL")
            call her_main("Хм... Ну...","open","base")
            her "Я дрочила этому мальчику в одном из пустых классов..."
            her "И этот мерзкий призрак Пивз вошел в..."
            call her_main("Или, скорее, вылетел на нас...","annoyed","worriedL")
            call her_main("И как только он понял, что я делаю с мальчиком...","open","base")
            her "Он начал кричать непристойности на нас..."
            her "В общем, нам пришлось быстро уйти..."
            m "Понятно..."
            call her_main("Это еще не все, [genie_name]...","annoyed","angryL")
            m "Продолжай..."
            call her_main("Ну, я вроде как обещала мальчику...","open","down")
            her "Я обещала встретиться с ним после занятий и..."
            call her_main("...и закончить начатое...","annoyed","annoyed")
            m "Понятно..."
            m "Ты встретилась с ним?"
            call her_main("Нет, [genie_name]. Еще нет...","angry","base")
            her "Я собираюсь встретиться с ним, как только я закончу с вами, [genie_name]."
            m "Хм..."
            call her_main("Поэтому, если вы можете начислить очки прямо сейчас...","angry","down_raised")
            her "Я сразу пойду к тому мальчику..."
            call her_main("И подрочу ему, как полагается...","open","baseL",cheeks="blush")

            menu:
                "\"Нет. Ты провалила задание, [hermione_name].\"":
                    stop music fadeout 3.0
                    call her_main("Н-но...","open","base",cheeks="blush")
                    call her_main("Но я дала ему слово...","angry","wide")
                    her "Я поклялась именем Годрика Гриффиндора..."
                    call her_main("И теперь мне придется дрочить ему, несмотря ни на что...","angry","down_raised")
                    m "Ну, я не заставлял тебя давать ему это обещание, не так ли?"
                    call her_main("......","angry","base")
                    call her_main("Это просто несправедливо!","scream","worriedCl")
                    $ mad +=20

                    $ hg_pr_HandjobClassmate_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

                "\"Хорошо, я думаю, что могу доверять тебе.\"":
                    call her_main("Спасибо, [genie_name].","base","base")
                    her "Я знала, что вы поймете."
                    m "Просто убедись, что закончишь с ним должным образом."
                    call her_main("Конечно, [genie_name]. Я подарю ему лучший фап в его жизни, обещаю!","base","happyCl")

        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            call her_main("Да, [genie_name]...","open","closed",xpos="right",ypos="base")
            call her_main("Хотя я все еще не уверена, как я отношусь ко всему этому...","annoyed","worriedL")
            m "Твои личные чувства меня не интересуют, [hermione_name]."
            m "Расскажи мне, как все прошло."
            call her_main("Ну, особо нечего рассказывать, [genie_name]...","open","base")
            call play_music("playful_tension") # SEX THEME.
            her "Сегодня я снова подрочила своему однокласснику..."
            call her_main("Я, Гермиона Грейнджер...","open","down")
            call her_main("Бесплатно дрочила мальчику в туалете...","angry","down_raised")
            m "Подожди. Что ты имеешь в виду под \"бесплатно\"?"
            call her_main("Oх, конечно... Вы мне за это даете очки...","angry","base")
            her "Но об этом никто не знает..."
            her "И для всех остальных это больше похоже на блудницу, которая делает это для удовольствия..."
            call her_main("Они могут подумать, что я шлюха...","open","down")
            call her_main("..............","clench","down_raised")
            call her_main("Вы думаете, что я шлюха, [genie_name]?","open","squint",cheeks="blush")

            menu:
                "\"Что? Конечно нет, [hermione_name]!\"":
                    call her_main("..............","base","baseL",cheeks="blush")
                    call her_main("Вы правы, [genie_name]...","base","down")
                    her "Я делаю это ради чести \"Гриффиндора\"."
                    call her_main("Я не получаю удовольствия от этого...","soft","ahegao")
                    call her_main("Но, если бы получала...","annoyed","angryL")
                    her "Это будет означать, что я действительно шлюха..."
                    call her_main("А я не...","angry","down_raised")
                    her "......"
                    her "Я не шлюха..."

                "\"Шлюха? Нет... Еще нет.\"":
                    call her_main("\"Еще нет\"??!","angry","base")
                    call her_main("..........","angry","down_raised")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Ну, конечно!","scream","wide_stare")
                    call her_main("Вы, как обычно, правы [genie_name]!","soft","base")
                    m "А?"
                    call her_main("Я сделала несколько... непристойных вещей...","open","base")
                    her "Но это ничего не значит!"
                    call her_main("...........","annoyed","angryL")

                "\"Да, именно так бы я о тебе и думаю.\"":
                    call her_main("Я боялась, что вы это скажете, [genie_name]...","mad","worriedCl",tears="soft_blink")
                    her "Но вы ошибаетесь, [genie_name]."
                    call her_main("Вы должны понимать, что я не испытываю никакого удовольствия от этого...","angry","base",tears="soft")
                    call her_main("Я просто делаю то, что нужно сделать...","normal","baseL",tears="soft")
                    $ mad = 10

            call her_main("[genie_name], я могу получить очки?","soft","baseL")
            m "Получить? Но ты не рассказала мне, как все прошло?"
            her "Нет?"
            call her_main("[genie_name], я подрочила сегодня одному однокласснику...","open","base",cheeks="blush")
            her "Я дрочила его член, пока он не кончил..."
            call her_main("Не это ли вы мне сказали сделать?","disgust","glance")
            m "Это именно то, что я сказал тебе сделать, [hermione_name]."
            call her_main("Тогда, я хотела бы получить очки.","annoyed","closed")
            m "........"
            m "Ладно..."

        #Event C
        elif one_out_of_three == 3:
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, [genie_name]. Выполнила.","open","closed",xpos="right",ypos="base")
            m "Отлично. Расскажи мне подробности."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Ну, сегодня был довольно напряженный день...","open","base")
            her "И мне нужно было наверстать упущенное в учебе..."
            her "Поэтому как обычно, у меня действительно не было времени, чтобы правильно все спланировать..."
            her "Я подошла к первому попавшемуся мальчику, которого увидела..."
            call her_main("И спросила, не хочет ли он, чтобы я сняла его напряжение..","annoyed","angryL")
            her "Через несколько минут я уже дрочила его твердый член в туалете..."
            m "Как результативно с твоей стороны..."
            call her_main("Спасибо, [genie_name].","annoyed","annoyed")
            call her_main("Итак, как я уже говорила...","annoyed","angryL")
            her "Я дрочила его член, пока он не кончил..."
            call her_main("Но после этого он сказал : \"Хорошая работа, шлюха\" и ушел...","disgust","glance")
            call her_main("Так мерзко с его стороны...","annoyed","angryL")
            call her_main("Я чувствовала себя дешевкой... и использованной","upset","closed")
            her "Но становится только хуже..."
            her "......."
            call her_main("Я думаю, что на каком-то уровне это также заставило меня чувствовать себя...","angry","down_raised")
            her "Все эти услуги, которые я продаю вам в последнее время, [genie_name]..."
            call her_main("...начинают влиять на меня.","angry","base")
            her "[genie_name], что со мной происходит?"

            menu:
                "\"Это ерунда. Хватит думать об этом!\"":
                    call her_main(".......","open","squint",cheeks="blush")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Вы, наверное, правы, [genie_name]. Как всегда...","base","baseL",cheeks="blush")
                    her "Это не должно ничего значить..."

                "\"Это естественная реакция...\"":
                    call her_main("Это естественно?","open","squint",cheeks="blush")
                    m "Конечно."
                    m "Ты девочка, а он мальчик..."
                    m "Когда ты возбуждаешься, тебе хорошо..."
                    call her_main("Хм...","base","baseL",cheeks="blush")
                    m "А если бы ты подрочила парню с совершенным безразличием к этому..."
                    m "...это было бы... неестественно."
                    call her_main("Я думаю вы правы, [genie_name].","open","squint",cheeks="blush")
                    call her_main("Как всегда.","base","baseL",cheeks="blush") # :)

                "\"Да! Все идет по плану!\"":
                    call her_main("Что?","angry","wide")
                    m "Что?"
                    call her_main("[genie_name], вы только что сказали \"все идет по плану\"?","angry","angry",cheeks="blush")
                    m "Я?"
                    m "Ох, да, конечно."
                    m "Гарантируя, что \"Гриффиндор\" получит кубок факультетов в этом году."
                    m "Таков план, и благодаря твоей тяжелой работе, [hermione_name]..."
                    m "Все идет согласно пик-... В смысле, плана..."
                    call her_main("Хм...","upset","closed")
                    $ mad += 11

    #Third level.
    elif whoring >= 21:

        #Event A
        if one_out_of_three == 1:
            if sucked_off_ron: #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
                jump blowjob_ron

            else:
                $ sucked_off_ron = True #Makes sure this event is not repeated twice.
                stop music fadeout 1.0

                # HERMIONE HAS CUM ON HAIR.
                #$ aftersperm = True #Shows stains on Hermione's uniform.
                $ uni_sperm = True  #Universal sperm.
                $ u_sperm = "characters/hermione/face/auto_08.png"

                show screen blktone
                call her_main("[genie_name]...","open","worried",xpos="right",ypos="base")
                m "[hermione_name]..."
                call her_main("Я сделала сегодня плохую вещь, [genie_name]...","open","worriedL")
                m "Что? Расскажи..."
                call play_music("playful_tension") # SEX THEME.
                her "Да, я сделала плохую вещь... очень плохую вещь..."
                call her_main("Очень плохую и дурацкую вещь...","annoyed","frown")
                her "..."
                m "...................."
                her "......................"
                call her_main("Я дрочила брату моей лучшей подруги...","angry","base",tears="soft")
                m "Интересно..."
                call her_main("Поначалу, это казалось отличной идеей....","angry","base",tears="soft")
                her "Да и Рон был \'за\', руками и ногами..."
                call her_main("Но если Джинни узнает об этом... она...","shock","baseL",cheeks="blush",tears="soft")
                call her_main("Она, наверняка, убьет меня, [genie_name]...","angry","base",tears="soft")
                m "Подрочила, да? Ты уверена, что это все, что ты сделала?"
                call her_main("[genie_name]?","angry","base",tears="soft")
                m "В твоих волосах что-то есть..."
                call her_main("Что? Но я все глотала... эээ...","soft","base",tears="soft")
                call her_main("Я имела в виду...","clench","worried",cheeks="blush",tears="soft")
                call her_main("*Вздох*","shock","baseL",cheeks="blush",tears="soft")
                her "...Я отсосала ему., [genie_name]."
                her "Я не планировала... но..."
                call her_main("Рон всегда так добр ко мне...","clench","worried",cheeks="blush",tears="soft")
                call her_main("И я хотела отблагодарить его....*Всхлип!*","shock","down_raised",cheeks="blush",tears="crying")
                call her_main("А теперь Джинни убьет меня! *Всхлип!*","angry","base",tears="soft")
                her "Она убьет меня, [genie_name]!"
                call her_main("И если она этого не сделает, я, вероятно, все равно умру от стыда.","shock","down_raised",cheeks="blush",tears="crying")
                her "Нет, нет, нет... Как я буду смотреть ей в глаза...?"
                m "Успокойся, [hermione_name]."
                m "Уверяю тебя, это не то, о чем мальчик хотел бы похвастаться своей сестре."
                call her_main("Нет?","clench","worried",cheeks="blush",tears="soft")
                m "Не будь глупой, [hermione_name]."
                call her_main("Хм...","normal","baseL",tears="soft")
                call her_main("Вы, наверное, правы, [genie_name]...","soft","base",tears="soft")
                her "И я заставила Рона дать мне слово, что он сохранит все в секрете..."
                call her_main("Так что, я думаю, я должна просто довериться ему...","open","worriedL")
                call her_main("..........","soft","baseL")
                her "..."
                call her_main("Вы заплатите за это, [genie_name]?","base","base")
                m "Конечно."

        #Event B
        elif one_out_of_three == 2: ### (WANK DURING CLASS)
            label blowjob_ron: #Sent here if sucked off Ron already.
                pass

            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            call her_main("Да, [genie_name].","base","base",xpos="right",ypos="base")
            call her_main("Но, эм...","open","worried")
            m "...?"
            call her_main("Ну, я не просто дрочила одному из своих одноклассников...","open","base")
            her "Я.............."
            call her_main("...............","clench","down_raised")
            m "Давай выкладывай, [hermione_name]. Неопределенность убивает меня."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Я делала это во время занятий...","open","down")
            m "Впечатляюще..."
            call her_main("Сэр, вы не понимаете. Позвольте мне все объяснить.","angry","down_raised")
            hide screen blktone
            with d3
            her "Я даже не знаю, что случилось со мной."
            show screen dual_hand_job
            with d5

            call her_main("Я старалась вести себя настолько естественно, насколько могла...")
            her "Но у меня внезапно возникло, невероятно, приятное желание сделать это во время занятий профессора Снейпа."
            her "Я даже не могла делать заметки..."
            her "Мои руки были заняты членами."
            m "Ты одновременно дрочила двум мальчикам?!"
            call her_main("Да, Сэр.","angry","wink")
            call her_main("И, я думаю, что им очень понравилось...","base","down")
            her "Потому что они не просто кончили."
            her "Их члены просто взорвались."
            m "Тебе понравилось, не так ли?"
            call her_main("Если быть честной, то... Да.","grin","dead")
            call her_main("Это было захватывающе.","smile","angry")
            call her_main("Боже, столько всего произошло.  Мои руки были похожи на свечу, с них, как будто, капал горячий воск.","grin","dead")
            call her_main("Я не знала, как мне идти через весь класс со спермой на руках.","angry","down_raised")
            her "Поэтому я решила вытереть их изнутри своих бедер, чтобы не было пятен на моей одежде."
            call her_main("Каждый раз, когда я ходила, я чувствовала запах спермы между ног.","silly","ahegao")
            m "Это довольно интересная история, мисс Грейнджер."
            hide screen dual_hand_job
            with d5

            show screen blktone
            call her_main("Я определенно хочу их одновременно.","silly","dead")
            m "..."
            call her_main("Да, два огромных члена взрываются и пачкают меня всю своей спермой.","silly","ahegao")
            m "........"
            call her_main(".......","silly","ahegao")
            m "Эм....."
            call her_main("Ох, боже, простите [genie_name], я не о том думаю.","angry","wide")
            m "Да... конечно, хорошо."
            call her_main("","base","base")

        #Event C
        elif one_out_of_three == 3: ### (Wanked off 5 boys)
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            with d3
            call her_main("Да, [genie_name]...","base","suspicious",xpos="right",ypos="base")
            her "Не раз..."
            m "Не раз?"
            call her_main("Пять, [genie_name]...","base","glance")
            her "Я немного увлеклась, я полагаю..."
            m "Что ты имеешь в виду под \"пять\", [hermione_name]?"
            call her_main("Я дрочила сегодня пяти мальчикам , [genie_name].","base","suspicious")
            m "Очень внушительно, [hermione_name]."
            call her_main("Спасибо, [genie_name].","base","glance")
            m "Ты же не ожидаешь, что я умножу твои очки на пять или более раз, не так ли?"
            call her_main("Конечно нет, [genie_name].","base","baseL",cheeks="blush")
            m "Чем это объясняется?"
            call her_main("Это просто случилось...","open","squint",cheeks="blush")
            her "Я дрочила мальчику..."
            her "И один мальчик застукал нас..."
            her "Он позвал своих друзей..."
            call her_main("А после еще одному...","base","glance")
            m "И ты, в конечном итоге, дрочила пять членов..."
            call her_main("...Да.","soft","ahegao")
            m "Молодец, мисс Грейнджер."
            call her_main("","base","glance")

    $ gryffindor += current_payout #55
    m "\"Гриффиндор\" получает [current_payout] очков!"
    her "Спасибо, [genie_name]."

    $ uni_sperm = False  #Universal sperm.
    $ aftersperm = False #Shows stains on Hermione's uniform.

    $ hg_pr_HandjobClassmate_OBJ.points += 1
    $ hg_pr_HandjobClassmate_OBJ.inProgress = False

    if hg_pr_HandjobClassmate_OBJ.points >= 2:
        $ hg_pr_HandjobClassmate_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
