

### Let Classmate Molest Her ###

##(Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label hg_pr_ClassmateTouchYou:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_ClassmateTouchYou_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтобы она пошла и дала облапать себя своему однокласснику?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro.
    if hg_pr_ClassmateTouchYou_OBJ.points == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="right",ypos="base")
        m "Тебе нравятся мальчики твоего возраста, не так ли?"
        call her_main("...?","normal","base")
        m "Может быть один из твоих одноклассников?"
        call her_main("Ну...","open","worriedL")
        her "Это обязательно обсуждать с вами, [genie_name]?"
        call her_main("Мне немного неловко...","annoyed","worriedL")
        m "Конечно, я все понимаю. Мне не нужно знать подробности..."
        m "Но вот, что ты должна сделать сегодня, [hermione_name]."
        m "Иди и порази парня, который тебе нравится. Того, которого ты считаешь, \"просто мечтой\"..."
        call her_main(".......?","open","base")
        m "И пусть он тебя облапает..."

        if whoring < 6 or hg_pr_FlirtTeacher_OBJ.points < 2: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much

        call her_main("Позволить ему... лапать меня, [genie_name]?","open","base")
        m "Да, лапать. Как мальчики прикасаются к девочкам."
        m "Сколько тебе лет, [hermione_name]? Ты выглядишь достаточно взрослой..."
        m "Разве ты не пробовала \"разговаривать\" с родителями?"
        call her_main("\"разговаривать\", [genie_name]?","angry","worriedCl",emote="05")
        m "Да, \"разговаривать\"! О том, чем мальчики отличаются от девочек...?"
        m "© У мальчиков есть \"пенисы\", у девочек есть \"вагины\", и девочки любят \"пенисы\" запихивать себе в рот, не так ли?"
        call her_main("!!!","normal","base")
        call her_main("Какой сумасшедший родитель будет о таком говорить со своим ребенком?","angry","angry")
        m "Акабур бы стал."
        call her_main("Прошу прощения, [genie_name]?","annoyed","suspicious")
        m "*Кхем!* Я сказал, ответственный и заботливый!"
        m "Ну, в любом случае. Это твоя задача на сегодня, [hermione_name]."
        m "Найди способ, убедить одного из своих одноклассников немного облапать тебя..."
        call her_main("..........","annoyed","angryL")
        m "Ты красивая девочка, это не должно быть слишком сложно."
        her "....................."
        call her_main("Сколько очков я получу за выполнение, [genie_name]?","disgust","glance")
        m "Хм... двадцать пять..."
        call her_main("Двадцать пять очков...","annoyed","angryL")
        her "...."
        call her_main("Ну, так тому и быть...","disgust","glance")
        m "Отлично..."
        call her_main("Я, тогда пойду. Занятия вот-вот начнутся...","angry","angry")

    #Second time event.
    else:
        if whoring >= 6 and whoring < 9: # LEVEL 03
            m "[hermione_name]?"
            call her_main("[genie_name]?","base","base",xpos="right",ypos="base")
            m "Как насчет того, чтобы позволить одному из твоих одноклассников снова по приставать к тебе?"
            call her_main("........","upset","closed")
            m "Двадцать пять очков, [hermione_name]."
            call her_main("[genie_name], это...","annoyed","angryL")
            call her_main("Я не понимаю, почему я должна так поступать...","annoyed","annoyed")
            m "Чтобы помочь своему факультету?"
            call her_main("Это не то, что я имела в виду...","disgust","glance")
            call her_main("Ничего страшного...","annoyed","angryL")
            her "Занятия скоро начнутся, мне пора идти..."
            m "Будешь ли ты это делать?"
            call her_main("Я не знаю... Возможно...","disgust","glance")

        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "[hermione_name], мне нужно, чтобы ты пошла и заставила одного из своих одноклассников полапать тебя..."
            call her_main("Я поняла, [genie_name]...","base","base",xpos="right",ypos="base")
            m "Тогда иди."
            her "..........."

        elif whoring >= 12: # LEVEL 05+
            m "[hermione_name], мне нужно, чтоб ты..."
            m "Найди парня и заставь его потрогать себя!"
            call her_main("Вы имеете в виду...","base","base",xpos="right",ypos="base")
            call her_main("В сексуальном смысле, [genie_name]?","angry","wink")
            m "Что? Нет, просто дай ему залезть тебе под форму, и все..."
            call her_main("Oх...","grin","worriedCl",emote="05")
            call her_main("Интересно, кто же это будет на этот раз...","grin","baseL")
            call her_main("А если, больше одного мальчика, это не проблема, не так ли, [genie_name]?","angry","base")
            m "Проблема? Конечно нет!"
            m "Это очень даже приветствуется."
            call her_main("Отлично. Тогда увидимся после занятий, [genie_name]. Как обычно.","angry","wink")
            m "Да. Удачи."

    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_ClassmateTouchYou_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First time event.
    call her_main("Добрый вечер, [genie_name].","base","base",xpos="right",ypos="base")
    m "[hermione_name]..."
    m "Ты выполнила поставленную задачу?"
    her "Я сделала, как вы просили [genie_name]..."

    menu:
        "\"Отлично. Вот тебе твои очки.\"":
            pass
        "\"Расскажи мне, как это было.\"":
            hide screen hermione_main
            with d3
            m "Давай, расскажи мне, как это было."
            show screen blktone

            if whoring >= 6 and whoring < 9: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                call her_main("......","annoyed","angryL")
                call her_main("Ну... Эм...","soft","baseL")
                m "Говори же, [hermione_name]."
                m "Скольким повезло на этот раз или что?"

                #Event A
                if one_out_of_three == 1:
                    her "Я все сделала, [genie_name]..."
                    m "Так..? Давай рассказывай подробности."
                    her "Ну, я не так и много смогу вам сказать..."
                    call her_main("Я сказала одному парню, что он может прикоснуться ко мне, если захочет....","open","base")
                    call her_main("Сначала он подумал, что я шучу...","annoyed","worriedL")
                    call her_main("Было так неловко...","normal","worriedCl")
                    m "Так, он лапал тебя?"
                    call play_music("playful_tension") # SEX THEME.
                    call her_main("Да...","normal","worriedCl")
                    m "Ну, где он тебя трогал, [hermione_name]?"
                    call her_main("Эм... Мои ноги...","annoyed","worriedL")
                    her "И... вспомнила, грудь немного..."
                    m "Это все?"
                    call her_main("Да, [genie_name]...","open","base")
                    call her_main("Уже довольно поздно... Думаю, мне пора уйти...","normal","worriedCl")
                    call her_main("Простите, [genie_name]...","angry","worriedCl",emote="05")
                    m "Не о чем сожалеть, [hermione_name]."
                    m "Ты молодец."

                #Event B
                elif one_out_of_three == 2:
                    stop music fadeout 3.0
                    call her_main("Я это сделала, [genie_name].","annoyed","angryL")
                    her "Но все это было очень неловко и стыдно..."
                    m "В этом и состоит весь смысл, [hermione_name]."
                    m "Скажи мне, где тебя лапали..."
                    call play_music("playful_tension") # SEX THEME.
                    her "Эм..."
                    call her_main("Ну, он залез по юбку...","angry","base")
                    her "Тогда, я позволила потереть мою..."
                    call her_main("...мою киску через трусики, [genie_name].","angry","down_raised")
                    m "Очень хорошо. Что случилось после?"
                    call her_main("Затем он начал трогать себя [genie_name]...","open","worriedCl")
                    her "И поэтому я решила уйти...."
                    m "Ох..."
                    call her_main(".............","normal","worriedCl")

                #Event C
                elif one_out_of_three == 3:
                    her "Я это сделала, [genie_name]..."
                    call play_music("playful_tension") # SEX THEME.
                    call her_main("Я привела парня из \"Пуффендуя\" в пустой класс и сказала ему, что он может полапать меня, если захочет.","open","base")
                    her "Потому что я не против..."
                    call her_main("...........","annoyed","worriedL")
                    m "И?"
                    call her_main("Ну, он легонько прикоснулся ко мне...","open","base")
                    call her_main("......","normal","worriedCl")
                    m "Не заставляй меня клещами доставать из тебя каждое слово, [hermione_name]!"
                    m "Что случилось позже?"
                    call her_main("Ну...","open","down")
                    stop music fadeout 1.0
                    her "Думаю, его больше интересовало, чтобы {size=+5}я{/size} потрогала у {size=+5}него{/size}..."
                    call her_main("Он попросил меня, назвать его \"маменькин сынок\"...","upset","wink")
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("И мне пришлось успокаивать его, от того что у него не встал, его очень маленький пенис...","open","base")
                    call her_main("Он просто повторял *всхлип!*...","angry","base",tears="soft")
                    call her_main("Почему со мной такое произошло?","angry","base",tears="soft")
                    her "*всхлип!* Я не могла больше оставаться в его компании, поэтому просто убежала."
                    m "Мне жаль это слышать..."
                    call her_main("Это было действительно ужасно, [genie_name]...","angry","base",tears="soft")
                    m "Ну, ну, не плачь..."
                    call her_main("*всхлип!*","normal","baseL",tears="soft")
                    m "Десять дополнительных очков заставят тебя успокоится?"
                    call her_main("А? Это было бы очень мило [genie_name].","soft","base",tears="soft")
                    m "Конечно... Десять дополнительных очков \"Гриффиндору\"."
                    call her_main("Спасибо [genie_name]...","clench","worried",cheeks="blush",tears="soft")
                    m "И остальные очки за выполненную услугу..."

            elif whoring >= 9 and whoring <= 11: # LEVEL 04

                #Event A
                if one_out_of_three == 1:
                    call her_main("Ну... я мало, что могу рассказать...","open","closed")
                    her "Я нашла одного мальчика из \"Когтеврана\"..."
                    her "Привела его в один из пустых классов в восточном крыле..."
                    her "Он думал, что я хочу поцеловаться с ним...."
                    her "Но я сказала ему, что хочу, чтобы он лапал меня...."
                    call her_main("...так он и делал.","normal","worriedCl")
                    m "Ох..."
                    m "Молодец, [hermione_name]."
                    call her_main("Я получу очки?","upset","wink")
                    m "Минуту, [hermione_name]. Я хочу тебе задать вопрос."
                    call her_main("???","open","base")
                    m "Тебе понравилось?"
                    m "Тебе было хорошо, когда мальчик тебя лапал?"
                    call her_main("Oх...","open","closed")
                    her "Ну, он был довольно красив, и я полагаю..."
                    call her_main("Я не ненавижу, если вы это имеете в виду, [genie_name]...","upset","closed")
                    m "Понятно..."

                #Event B
                elif one_out_of_three == 2:
                    call her_main("Ну...","open","closed")
                    her "Я не уверена, имеет ли это значение, но..."
                    her "Во время урока гербологии..."
                    call her_main("Я позволила одному мальчику засунуть руку мне под юбку...","upset","wink")
                    her "И поэтому пока профессор Спраут объясняла различия между \"мандрагорой\" и \"мандрогорой\"..."
                    call her_main("Которые я, конечно же, знала...","open","suspicious")
                    call her_main("Я позволила своему однокласснику массировать мои ягодицы...","upset","wink")
                    her "И это все..."
                    m "Хм..."
                    menu:
                        "\"Ты можешь сделать больше, [hermione_name].\"":
                            call her_main("Да, я знаю, [genie_name]. Простите.","open","base")
                            m "Просто по лучше постарайся в следующий раз."
                            her "Хорошо, [genie_name]."
                        "\"Похвально, что ты делаешь это в классе.\"":
                            call her_main("Спасибо, [genie_name].","base","happyCl")
                            m "Ты заслужила свои очки."

                #Event C
                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main(".................","annoyed","angryL")
                    m "???"
                    call play_music("playful_tension") # SEX THEME.
                    call her_main("Я не хочу об этом говорить, [genie_name]...","annoyed","angryL")
                    m "Что случилось, [hermione_name]. Рассказывай."
                    call her_main(".................","annoyed","annoyed")
                    call her_main("Но... это так стыдно...","open","base")
                    call her_main("Мне действительно нужно рассказывать, [genie_name]?","normal","worriedCl")
                    m "Да, я люблю постыдные вещи!"
                    call her_main(".................","annoyed","angryL")
                    her "Ладно..."
                    her "Я подошла к парню, которого всегда считала привлекательным..."
                    her "Сумела набраться смелости и попросила пойти за мной..."
                    call her_main("В обычных условиях я бы не смогла...","open","base")
                    her "Но дело в том, что я делала это как задачу, порученную мне кем-то другим..."
                    her "Это мне немного упростило..."
                    m "Рад помочь, [hermione_name]."
                    call her_main("Я привела его в библиотеку...","open","down")
                    her "Мы нашли уединенное место за одной из книжных полок..."
                    her "И я сказала ему, что он может полапать меня, где он захочет..."
                    her "И...."
                    call her_main("..........","clench","down_raised")
                    m "Что?"
                    call her_main(".....................","normal","worriedCl")
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("Он начал прикасаться к моим... ступням, [genie_name].","scream","worriedCl")
                    m "Что?"
                    m "К твоим \"ступням\"? Это так, теперь молодежь называет сиськи?"
                    call her_main("Хотелось бы, [genie_name]...","disgust","glance")
                    her "Он попросил меня снять туфли..."
                    her "Затем он..."
                    call her_main("Он начал нюхать мои пальцы, [genie_name]!","angry","base",tears="soft")
                    call her_main("Я чувствовала себя так...","angry","base",tears="soft")
                    m "Так он не трогал твои сиськи или попку?"
                    call her_main("Нет, [genie_name]... *всхлип!*","shock","down_raised",cheeks="blush",tears="crying")
                    m "Хорошо, тогда что случилось?"
                    call her_main("Ничего! Я не вынесла такого унижения... Я просто убежала...","angry","dead",cheeks="blush",tears="crying")
                    her "Я даже оставила свои туфли и должна вернуться за ними..."
                    call her_main("*всхлип!*............","angry","suspicious",cheeks="blush",tears="messy")
                    m "Хм..."
                    m "Ну, к тебе приставали..."
                    m "Хотя и в довольно необычной манере..."
                    call her_main("*Всхлип!* Я хотела, чтобы он просто прикоснулся к моей груди, как мальчик, [genie_name]... *Всхлип!*","angry","suspicious",cheeks="blush",tears="messy")
                    m "Ну, ну, не плачь..."
                    m "Вот тебе твои очки..."

            elif whoring >= 12: # LEVEL 05+

                #Event A
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    call her_main("......","annoyed","worriedL")
                    call her_main("Ну...","open","base")
                    her "Во время сегодняшнего урока зельеварения..."
                    her "Я написала записку на листке бумаги..."
                    her "Я собиралась дать ее своему однокласснику в лаборатории, тогда..."
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Профессор Снейп вырвал ее у меня из рук....","annoyed","angryL")
                    call her_main("Затем он прочитал ее вслух перед всем классом...","annoyed","annoyed")
                    m "Что было написано в записке?"
                    call her_main("Ну...","open","down")
                    her "Он прочитал: \"Можешь потрогать мою задницу, если хочешь. Профессор Снейп не увидит.\""
                    call her_main("Все смеялись...","angry","down_raised")
                    her "Мне было так стыдно, что я хотела умереть..."
                    call her_main("Я ненавижу профессора Снейпа, [genie_name]...","angry","angry")
                    m "Что было после?"
                    call her_main("Ничего...","open","down")

                    call play_music("playful_tension") # SEX THEME.
                    hide screen hermione_main
                    with d3
                    $ sc34CG(2, 19, 6, 5)

                    call her_main("Но когда занятия закончились...",xpos="base",ypos="base")
                    call her_main("Эти два противных на вид мальчика из \"Слизерина\" загнали меня в угол...")
                    call her_main("Вообще-то, они не хотели меня обидеть...")
                    call her_main("Поэтому мы просто ждали, пока все покинут класс...")
                    $ sc34CG(2, 16, 6, 9)
                    call ctc

                    call her_main("И тогда, они начали лапать меня...","angry","base")
                    $ sc34CG(2, 17, 6, 9)
                    call her_main("Они трогали меня везде, [genie_name]...")
                    m "\"Везде\", да?"
                    call her_main("Да... Везде, [genie_name]...","soft","ahegao")
                    call her_main("Их руки были под юбкой, под рубашкой...","base","glance")
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("А потом я начала тяжело дышать....")
                    call her_main("Так, что один из них просто зажал рукой мне рот...","soft","ahegao")
                    her "А их руки были... Большими..."
                    $ sc34CG(2, 17, 6, 9)
                    call her_main("У меня закружилась голова...")
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("Это было очень волнующе, [genie_name].","base","glance")
                    m "Очень хорошо, [hermione_name]. Очень хорошо."

                    hide screen sccg
                    call her_main(xpos="right",ypos="base",trans="fade")

                #Event B
                if one_out_of_three == 2:
                    call her_main("Вообще-то, сегодня со мной произошло кое-что неожиданное, [genie_name]...","base","base")
                    her "Сразу после урока защиты от темных искусств..."
                    her "Лохматый мальчик из \"Пуффендуя \" подошел ко мне..."
                    call play_music("playful_tension") # SEX THEME.
                    call her_main("Он сказал, что ему рассказали, о том, что я позволяю лапать себя...","angry","wink")
                    call her_main("Обычно я бы все отрицала...","base","glance")
                    her "Но я решила не упускать эту возможность..."
                    call her_main("Я отвела мальчика в тихое место и позволила ему лапать себя...","base","ahegao_raised")
                    her "Я позволила ему, гладить мои бедра..."
                    her "Трогать мою грудь..."
                    call her_main("Все как всегда...","base","glance")
                    m "Отлично, [hermione_name]."

                #Event C
                if one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main("Ну...","upset","wink")
                    her "Я все сделала, [genie_name]..."
                    her "Но... это своего рода... эм..."
                    call her_main("Ну, это переросло во что-то другое...","base","ahegao_raised")
                    call play_music("playful_tension") # SEX THEME.
                    m "Хм?"
                    call her_main("эм...","upset","wink")
                    her "Нас вроде как... застукали, пока я позволяла этому парню трогать мою грудь..."
                    m "Застукали? Один из учителей?"
                    call her_main("Нет, [genie_name]...","base","base")
                    call her_main("Девочка этого мальчика...","smile","baseL")
                    m "Интересно..."
                    call her_main("Сначала она была в ярости...","angry","base")
                    call her_main("Но, потом...","angry","wink")
                    call her_main("Эм... Она тоже начала трогать мою грудь...","base","down")
                    call her_main("Почти так же, как и ее парень минуту назад...","smile","angry")
                    her "Затем она повернулась к нему и сказала..."
                    call her_main("\"Я люблю тебя, и я хочу делиться всем с тобой...\"","open","closed")
                    her "\"...И это включает всех твоих шлюх.\""
                    call her_main("Я конечно проигнорировала, что меня называют шлюхой...","angry","base")
                    call her_main("Но это был такой милый и романтический момент...","base","base")
                    her "Вы не согласны, [genie_name]?"
                    m "Полностью..."
                    m "Кажется, что настоящая любовь {size=+5}Все-таки{/size} существует."
                    m "А что случилось потом?"
                    call her_main("Эм... Ну, они, конечно, поцеловались...","grin","worriedCl",emote="05")
                    call her_main("И затем они начали опять меня трогать...","upset","wink")
                    call her_main("А после они уже начали друг друга трогать...","annoyed","worriedL")
                    her "И снова целовались..."
                    her "Я вдруг почувствовала себя третьей лишней, поэтому я просто тихонько ушла..."
                    m "Понятно..."

    $ gryffindor +=25
    m "\"Гриффиндор\" получает 25 очков!"
    her "Спасибо, [genie_name]."

    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.

    $ hg_pr_ClassmateTouchYou_OBJ.points += 1
    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = False

    if hg_pr_ClassmateTouchYou_OBJ.points >= 2:
        $ hg_pr_ClassmateTouchYou_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
