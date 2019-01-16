

### Flash A Classmate ###

##(Level 04) (35 pt.) (Flash your tits to a boy). (Available during daytime only).
label hg_pr_FlashClassmate: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_FlashClassmate_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтобы показала сиськи однокласснику?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro.
    if hg_pr_FlashClassmate_OBJ.points == 0:
        m "[hermione_name]..."
        m "Я хотел бы наградить \"Гриффиндор\" 25 очками."
        call her_main("Серьезно?","base","base",xpos="right",ypos="base")
        her "Спасибо, [genie_name]!"
        m "Да, но сначало, ты должна помочь мне в этом..."
        her "Конечно, [genie_name]! Что угодно!"
        m "Мне нужно, чтоб ты пошла и показала кому-нибудь свои сиськи..."
        stop music fadeout 1.0
        call her_main("...?","open","base")
        m "Покажи свою грудь каким-нибудь мальчикам..."
        call her_main("?!!","shock","wide")

        if whoring < 9 or hg_pr_ClassmateTouchYou_OBJ.points < 2:
            jump too_much

        her "[genie_name]!"
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Это совершенно новый уровень наглости, неуместен даже для вас, [genie_name]!","angry","angry")
        her "Как вы можете просить свою ученицу выполнить подобное задание?"
        m "Понятно..."
        m "Я думаю, что вместо твоего, я буду присуждать эти очки какому-то другому факультету ..."
        m "Возможно, \"Слизерину\"?"
        call her_main("................","disgust","glance")
        m "Но, знаешь, я никого не заставляю...."
        call her_main("[genie_name]...","annoyed","angryL")
        her "Судьба моего факультета очень важна для меня, но..."
        m "Это правда?"
        m "Почему бы тебе, не доказать это мне?"
        m "Да. Покажи мне, насколько это важно для тебя, [hermione_name]."
        call her_main("Но это неуместно...","angry","angry")
        m "Действительно ли мы в должны обсуждать, что уместно, а что нет в данный момент?"
        call her_main("..................","annoyed","angryL")
        m "Я бы сказал, что корабль давно ушел..."
        call her_main("..............","disgust","glance")
        m "Все, что я прошу, это показать сиськи какому-то мальчику..."
        call her_main("Но почему? Почему я должна делать подобные вещи, [genie_name]?","annoyed","angryL")
        m "Минута твоего времени и 25 очков твои..."
        m "Отличная сделка, не находишь?"
        her "Я полагаю..."
        her "Хорошо, я посмотрю, что смогу сделать..."

    #Second time event.
    else:
        if whoring >= 9 and whoring < 12: # LEVEL 04 FIRST EVENT.
            m "Я думаю, тебе нужно еще раз показать свои сиськи, [hermione_name]."
            call her_main("Вы имеете в виду, вам, [genie_name]?","upset","wink",xpos="right",ypos="base")
            m "Нет, своему однокласснику..."
            call her_main("Oх...","angry","base")
            m "Да, сделай это, а после расскажешь мне..."
            call her_main("Вы за это заплатите?","annoyed","angryL")
            m "Конечно, ты получишь за это очки, [hermione_name]. Don't be silly."
            m "Тридцать пять очков. Обычная стоимость..."
            call her_main(".................","annoyed","angryL")
            call her_main("Ну хорошо... Я посмотрю, что смогу сделать, [genie_name]...","disgust","glance")

        elif whoring >= 12 and whoring < 15: # LEVEL 05
            m "[hermione_name]. У меня есть для тебя задание."
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Как ты думаешь, откуда у женщин грудь?"
            call her_main("...Что вы имеете в виду, [genie_name]?","upset","wink",xpos="right",ypos="base")
            m "Хорошо, позволь мне перефразировать..."
            m "Назови основную функцию женских молочных желез?"
            call her_main("Oх...","soft","base")
            call her_main("Производство молока?","annoyed","suspicious")
            m "Хорошо. Для чего еще женщины используют свои сиськи?"
            call her_main("Хм...","soft","baseL")
            call her_main("...чтобы привлечь мужчин?","annoyed","suspicious")
            m "Да. Давай сосредоточимся на этом."
            m "Мне нужно, чтобы ты вышла из кабинета..."
            m "Нашла счастливчика..."
            m "И показала ему свою грудь..."
            call her_main("{size=-3}(Почему-то, я была уверена, к чему идет этот разговор...){/size}","disgust","glance")
            m "Что, [hermione_name]?"
            call her_main("Я сказала, что лучше пойду, [genie_name].","annoyed","angryL")
            her "Мои занятия вот-вот начнутся..."
            m "Тридцать пять очков будут ждать тебя здесь по возвращении, [hermione_name]."
            call her_main("..............","annoyed","annoyed")

        elif whoring >= 15: # LEVEL 06+
            m "[hermione_name] мне нужно, чтобы ты вышла из кабинета и показала сиськи одному из своих одноклассников."
            call her_main("Я сделаю все возможное [genie_name].","open","closed",xpos="right",ypos="base")
            m "Правда? Просто так? Никаких жалоб или чего-либо еще?"
            call her_main("Я получу за это очки, не так ли?","base","glance")
            m "Конечно."
            call her_main("Для чего мне жаловаться на такую простую задачу, как эта?","open","closed")
            her "Тридцать пять очков-это справедливая цена за несколько секунд волнения... грр..."
            call her_main("...Я имею в виду, смущения.","base","happyCl")
            m "{size=-3}(Она уже так сильно изменилась?){/size}"
            g9 "{size=-3}(Я так хорош в этой тренировке, что становится жутковато!){/size}"
            call her_main("Занятия начинаются... Мне лучше сейчас уйти.","base","base")
            her "Увидимся вечером, [genie_name]."

    $ hg_pr_FlashClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_FlashClassmate_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First time event.
    if whoring >= 9 and whoring < 12:

        #Event A
        if one_out_of_three == 1:
                call her_main("Добрый вечер, [genie_name]...","open","base",xpos="right",ypos="base")
                m "[hermione_name]..."
                m "Итак, как все прошло?"
                call her_main("Эм... На самом деле, не слишком хорошо...","angry","worriedCl",emote="05")
                her "................................"
                m "Просто скажи мне, что случилось, [hermione_name]."
                call her_main("Дело в том, [genie_name]...","open","base")
                her "Что ничего не произошло..."
                call her_main("Я просто не смогла заставить себя сделать это...","open","down")
                m "Понятно..."
                m "Ну, я не могу просто так давать тебе очки, [hermione_name]."
                call her_main("Конечно, [genie_name]... Я понимаю...","open","closed")
                call her_main("В следующий раз постараюсь... Я обещаю...","annoyed","worriedL")
                m "Тогда я пока отложу эти тридцать пять очков в сторону..."
                call her_main("Спасибо, [genie_name]...","annoyed","worriedL")
                her "..."
                her "Мне лучше сейчас уйти."

                $ hg_pr_FlashClassmate_OBJ.inProgress = False
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name], ты выполнила свое задание?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Эм... Вроде...","annoyed","worriedL",xpos="right",ypos="base")
            m "Вроде?"
            call her_main("Да... эм...","open","base")
            her "Ну, я решила постараться и показать их мальчику из \"Пуффендуя\"..."
            call her_main("Я ждала нужного момента...","open","down")
            her "Я волновалась, что что-то пойдет не так..."
            call her_main("И, конечно, все прошло не так, как должно...","annoyed","angryL")
            call her_main("Когда я попыталась показать себя мальчику...","open","base")
            her "Я подняла жилетку...."
            her "Затем я попыталась снять свою рубашку..."
            her "И одна из моих грудей запуталась в ткани и была подтянута вместе с рубашкой..."
            call her_main("Так что только одна из моих грудей была обнажена, а я отчаянно пыталась освободить другую.","scream","worriedCl")
            her "Другие ученики начали обращать на меня внимание..."
            her "Так что мне пришлось быстро поправить рубашку и одеться..."
            her "И момент был упущен..."
            call her_main("............","normal","worriedCl")
            m "Хм..."
            m "А как насчет мальчика? Он видел твои сиськи или нет?"
            call her_main("Ну, я думаю, он, возможно, видел одну из них...","open","base")
            her "Но от того, как он смотрел на меня..."
            her "Я сомневаюсь, что он понял, что это было для него."
            call her_main("......................","annoyed","worriedL")
            call her_main("Простите, [genie_name]...","open","base")
            m "Все в порядке..."
            m "Я не ожидал, что ты в совершенстве справишься с этим в начале своей тренировки..."
            call her_main("(Моей тренировки?)","angry","base")

        #Event C
        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            with d3
            $ sc34CG(3, 5)
            call her_main("Да, [genie_name].","annoyed","worriedL",xpos="base",ypos="base")
            m "Хорошо. Расскажи."
            $ sc34CG(3, 4)
            call her_main("Эм... Я мало чего могу рассказать...","open","base")
            call her_main("Я провела первую половину дня в библиотеке...")
            call her_main("В это время она обычно пуста...")
            call her_main("Помимо меня там был только один студент...")
            $ sc34CG(3, 6)
            call her_main("Мальчик из \"Когтеврана\"...","upset","closed")
            call her_main("Поэтому я помахала ему и когда он посмотрел на меня...")
            $ sc34CG(3, 7)
            call her_main("Я быстро расстегнула рубашку...","angry","base")
            m "Хорошая работа."
            m "Как он отреагировал на вид твоих обнаженных сисек?"
            $ sc34CG(3, 8)
            call her_main("Я не уверена...","angry","down_raised")
            $ sc34CG(3, 9)
            call her_main("Он выглядел довольно шокированным...","angry","base")
            $ sc34CG(3, 10)
            call her_main("После того, как я показала ему свою грудь, мне стало слишком стыдно...","angry","down_raised")
            $ sc34CG(3, 11)
            call her_main("Поэтому я собрала свои книги и ушла...","angry","base")
            $ sc34CG(3, 6)
            m "Понятно..."
            hide screen sccg
            show screen blktone
            call her_main(xpos="right",ypos="base",trans="fade")

    #Second level event.
    elif whoring >= 12 and whoring < 15:

        #Event A
        if one_out_of_three == 1:
            stop music fadeout 1.0
            show screen blktone
            m "[hermione_name]. Ты выполнила свое задание?"
            call her_main("Да, [genie_name].","upset","wink",xpos="right",ypos="base")
            call her_main(".............","angry","down_raised")
            m "Что ж. Как все прошло?"
            call her_main("................","angry","down_raised")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Просто для справки, [genie_name]...","annoyed","angryL")
            m "Хм?"
            call her_main("Я думаю, что заставлять своих учеников делать такие вещи...","scream","angryCl")
            call her_main("Это очень низко для такого волшебника, как вы...","upset","closed")
            m "\"Заставляю\"? Никто тебя ни чего не заставляет делать, [hermione_name]."
            m "Ты пришла ко мне, помнишь?"
            call her_main("..........","open","base")
            m "Ты умоляла меня купить сексуальную услугу у тебя."
            call her_main("...Я....","annoyed","worriedL")
            call her_main("Я не говорила \"сексуальную\"...","open","base")
            m "Тем не менее, ты можешь прекратить продавать мне эти услуги в любой момент, [hermione_name]."
            call her_main("Я...","annoyed","angryL")
            m "И все же ты продолжаешь возвращаться..."
            call her_main("............................","angry","down_raised")
            m "Я думаю, что ты на самом деле принимаешь какую-то извращенную форму удовольствия от этого."
            call her_main("Что?","angry","angry")
            m "Позор тебе, [hermione_name]. Позор."
            call her_main("[genie_name], я никогда...!","angry","angry")
            m "Хватит об этом. Ты выполнила свою задачу или нет?"
            call her_main("Да, выполнила...","upset","closed")
            m "И?"
            call her_main("И это все, что я хотела сказать...","open","down")
            call her_main("........","upset","closed")
            m ".........."
            her "........"
            m "Ох, в любом случае. Просто возьми свои очки и иди."
            call her_main("Спасибо, [genie_name].","upset","closed")

        #Event B
        elif one_out_of_three == 2:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            show screen blktone
            call her_main("Добрый вечер, [genie_name]...","normal","worriedCl",xpos="right",ypos="base")
            m "Ты выполнила задание?"
            call her_main("Да, [genie_name]...","open","base")
            call her_main("..........","normal","worriedCl")
            m "................"
            her "..............."
            m "Ну?"
            call her_main("Могу я, пожалуйста, получить очки?","open","base")
            m "Не раньше, чем ты расскажешь мне, что именно ты сделала сегодня."
            call her_main("....................","normal","worriedCl")
            call her_main("Мне действительно это нужно, [genie_name]?","open","base")
            m "Когда ты так говоришь..."
            m "Ты только усиливаешь мое любопытство. Ты же знаешь это, верно?"
            call her_main("Пф...","angry","base")
            call her_main("Ну... Эм...","angry","down_raised")
            her "Ну, ладно..."
            call her_main("Я показала свои сиськи мальчику из \"Слизерина\" в коридоре...","scream","worriedCl")
            her "Но я стояла слишком близко к нему..."
            call her_main("....","normal","worriedCl")
            her "...."
            call her_main("Ну, он схватил одну из моих сисек, [genie_name]...","open","base")
            her "Крепко ее сжал и не отпускал..."
            call her_main("Он заставил меня пообещать встретиться с ним после уроков...","angry","base")
            her "И дать ему..."
            call her_main("\"Поиграть с моими сиськами\"...","open","worriedCl")
            call her_main("Видите, вот почему я ненавижу мальчиков из \"Слизерина\", [genie_name]...","angry","down_raised")
            her "У них нет ни капли чести..."
            her "..."
            m "Ты сдержала свое обещание?"
            call her_main("Нет, еще нет...","angry","base")
            her "Я планирую встретиться с этим гнусным мальчиком после того, как мы закончим здесь, [genie_name]."
            m "Понятно..."
            m "Ну, тогда я не должен заставлять его ждать, не так ли?"

        #Event C
        elif one_out_of_three == 3:
            m "[hermione_name], ты выполнила задание?"
            show screen blktone
            call her_main("Да [genie_name]...","open","base",xpos="right",ypos="base")
            m "Я слушаю..."
            call her_main("Ну...","open","base")
            her "Мне пришлось провести большую часть дня в школьной библиотеке..."
            her "Так что у меня действительно не было времени, чтобы выполнить вашу задачу должным образом, [genie_name]..."
            m "Хм...?"
            call play_music("playful_tension") # SEX THEME.
            her "Вместо этого я просто подошла к окну библиотеки и..."
            call her_main("...Я задрала рубашку и прижалась голой грудью к стеклу...","angry","down_raised")
            her "Я стояла так несколько секунд..."
            her "Чтобы хоть кто-то увидел меня со стороны..."
            call her_main("Я надеюсь, что это все еще считается, [genie_name]...","angry","base")
            m "Хм..."
            m "Как думаешь, сколько студентов видели тебя за стеклом?"
            call her_main("Я не уверена, [genie_name]... Парочка, может быть...?","angry","down_raised")
            m "\"Может быть\"?"
            call her_main("Я точно не знаю, [genie_name]...","open","worriedCl",cheeks="blush")
            her "Честно говоря, я держала глаза закрытыми..."
            m "Откуда ты знаешь, что кто-то видел тебя тогда, [hermione_name]?"
            call her_main("Я слышала чей-то крик: \"Смотри! Там, в окне!\".","angry","suspicious",cheeks="blush")
            her "Когда я это услышала, я начала прикрываться и быстро ушла..."
            call her_main("....","angry","base")
            m "Хм..."
            m "Ну, хорошо... Я думаю, это засчитывается..."

    #Third level event.
    elif whoring >= 15:

        #Event A
        if one_out_of_three == 1:
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да [genie_name]...","base","base",xpos="right",ypos="base")
            m "Я слушаю..."
            hide screen hermione_main
            with d3
            $ sc34CG(3, 5)
            call her_main("Ну... Мне пришлось провести большую часть дня в школьной библиотеке...","upset","wink",xpos="base",ypos="base")
            call her_main("Так что у меня действительно не было времени, чтобы выполнить вашу задачу должным образом, [genie_name]...")
            m "Хм...?"
            $ sc34CG(3, 6)
            call her_main("Вместо этого я убедилась, что вокруг нет учителей...","angry","base")
            call play_music("playful_tension") # SEX THEME.
            $ sc34CG(3, 7)
            call her_main("Задрала рубашку...")
            call her_main("А потом я просто сидела там какое-то время...","open","base")
            $ sc34CG(3, 12)
            call her_main("Пытаясь сделать несколько заданий...","open","down")
            her "Я не думаю, что вокруг было много людей..."
            call her_main("Или, по крайней мере, я надеюсь...","angry","down_raised")
            $ sc34CG(3, 13)
            call her_main("Но они определенно видели мою грудь, [genie_name]...","angry","base")
            $ sc34CG(3, 7)
            call her_main("В конце концов, несколько первокурсников точно заметили...","angry","down_raised")
            $ sc34CG(3, 10)
            call her_main("Мне пришлось довольно быстро уйти после этого...","angry","base")
            m "Хм..."
            m "Как думаешь, сколько людей тебя увидели, [hermione_name]?"
            $ sc34CG(3, 9)
            call her_main("Трудно сказать, [genie_name]...","open","base")
            call her_main("Две дюжины мальчиков или около того, я полагаю...")
            $ sc34CG(3, 12)
            call her_main("Несколько девушек, а также...","annoyed","worriedL")
            $ sc34CG(3, 11)
            call her_main("Думаю, школьный библиотекарь тоже меня видел...")
            m "Хм... Отличная работа."
            hide screen sccg
            show screen blktone
            call her_main(xpos="right",ypos="base",trans="fade")

        #Event B
        elif one_out_of_three == 2:
            stop music fadeout 1.0
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, [genie_name].","base","base",xpos="right",ypos="base")
            m "Тогда расскажи мне все об этом."
            call her_main("Эм... Хорошо...","open","base")
            her "Я показывала сиськи мальчику из \"Гриффиндора\" в общей комнате..."
            call her_main("Когда Джинни застукала нас...","open","base")
            m "Это другой мальчик?"
            call her_main("Мальчик? Нет, Джинни-женское имя, [genie_name].","soft","baseL")
            m "....."
            call her_main("Джинни Уизли, [genie_name].","open","base")
            m "Хорошо, ладно, продолжай..."
            call her_main("Эм...","soft","baseL")
            her "......."
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("*Хихикает*","grin","worriedCl",emote="05")
            m "Хм...?"
            call her_main("Она схватила меня за грудь...","smile","baseL")
            her "И начала их сжимать..."
            her "Затем она начала страстно целовала ее ..."
            m "............"
            call her_main("Целовала и сосала сосочки...","smile","angry")
            call her_main("Я ничего не могла с собой поделать, я начала стонать...","base","glance")
            m ".............."
            call her_main("А потом парень достал свой пульсирующий член...","base","suspicious")
            her "И разбрызгал свою горячую сперму на меня и Джинни!"
            call her_main("А потом мы с Джинни слизывали его горячую сперму с наших тел...","smile","angry")
            m ".............."
            m "Ты это выдумала, [hermione_name]?"
            call her_main("...Может быть.","grin","worriedCl",emote="05")
            call her_main("Я просто думала, что вы хотели бы услышать что-то подобное, [genie_name]...","base","glance")
            m "То, что я хотел бы услышать, [hermione_name], это правду."
            call her_main("Даже если это невероятно скучно, [genie_name]?","open","closed")
            m "Скучно или нет..."
            m "Я только хочу знать, что на самом деле произошло..."
            m "Держи свои фантазии при себе, [hermione_name]."
            call her_main("Как пожелаете, [genie_name].","annoyed","ahegao")
            her "Моя подруга Джинни проходила мимо, когда я показывала сиськи этому парню."
            her "Но она пообещала, что никому не расскажет."
            call her_main("И это все, что произошло, [genie_name]...","soft","base")
            m "Понятно..."

            #if not flashing_tits_with_ginny:
            #    call nar(>Your curiosity about Ginny grows!)
            #$ flashing_tits_with_ginny = True

            m "Все-таки, это мне нравится больше, чем выдуманные рассказы..."

        #Event C
        elif one_out_of_three == 3:
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Да, [genie_name]...","base","base",xpos="right",ypos="base")
            m "Хорошо, расскажи мне, как все прошло."
            call her_main("Ну, давайте посмотрим...","annoyed","worriedL")
            her "Сначала я показала их мальчику из \"Когтеврана\"..."
            call her_main("Старшекласснику из \"Пуффендуя\"...","open","base")
            call her_main("Потом был еще один мальчик из \"Когтеврана\".","base","base")
            m "???"
            call her_main("После этого я показала сиськи небольшой группе из \"Гриффиндора\"...","angry","worriedCl",emote="05")
            call her_main("Нет, подождите...  мальчики из \"Гриффиндора\" были после другого мальчика...","annoyed","worriedL")
            m "Так скольким мальчикам ты показала свои сиськи, [hermione_name]?"
            call her_main("Приблизительно полудюжина или больше?","angry","base")
            call her_main("В моем расписание было окно...","angry","wink")
            her "Так что я решила заработать дополнительные очки от вашего поручения, [genie_name]."
            m "Это не поручение, [hermione_name]..."
            m "И нет ни каких дополнительных очков..."
            call her_main("Oх...?","open","base")
            m "Ты все так же получишь обычную оговоренную стоимость, [hermione_name], и это все."
            call her_main("Oх... Понятно...","annoyed","worriedL")
            m "Но, [hermione_name]..."
            call her_main("Да, [genie_name]?","open","base")
            g9 "Это была отличная работа."
            call her_main("Спасибо, [genie_name].","base","glance")

    $ gryffindor +=35
    m "\"Гриффиндор\" получает 35 очков!"
    her "Спасибо, [genie_name]."

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3

    call her_walk("mid","door",2)
    pause.3

    show screen blktone
    if one_out_of_three == 2 and whoring >= 12 and whoring <= 14: #Event level 02.
        call her_head("\"Слизерин\"...","upset","closed",xpos="base",ypos="base")

    if one_out_of_three == 3 and whoring >= 12 and whoring <= 14: #Event level 02.
        call her_head("(Я не могу поверить, что я сделала это...)","upset","closed",xpos="base",ypos="base")
        call her_head("(Что если Гарри или Рон видели меня такой?)","angry","wide")
        call her_head("(Стоя там...)")
        call her_head("(Прижимающейся грудью к окну...)")
        call her_head("(Я, наверное, просто умру со стыда...)","angry","down_raised")
        call her_head("(Нет. Защита чести \"Гриффиндора\" -это моя цель номер один.)","upset","closed")
        call her_head("(Мы должны получить Кубок в этом году, не важно, какой ценой...)")
        call her_head("(........)","angry","down_raised")

    if whoring >= 15 and one_out_of_three == 1:
        call her_head(".........................","grin","dead",xpos="base",ypos="base")

    call hide_blktone

    $ hg_pr_FlashClassmate_OBJ.points += 1
    $ hg_pr_FlashClassmate_OBJ.inProgress = False

    if hg_pr_FlashClassmate_OBJ.points >= 2:
        $ hg_pr_FlashClassmate_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
