

### Make Out With A Girl ###

##(Level 05) (45 pt.) (MAKE OUT WITH A GIRL). (Available during daytime only).
label hg_pr_KissAGirl: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_KissAGirl_OBJ.points < 1:
        m "{size=-4}(Предложить поцеловаться со своей одноклассницей?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro.
    if hg_pr_KissAGirl_OBJ.points == 0:
        m "Ты когда-нибудь целовалась с девочкой, [hermione_name]?"
        call her_main("?!","normal","frown",xpos="right",ypos="base")

        if whoring < 12 or hg_pr_FlashClassmate_OBJ.points < 2: # Counts how many times you sent Hermione to flash a classmate.
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Я не... лесбиянка, [genie_name].","open","base")
        m "Глупая девчонка... Тебе не нужно быть лесбиянкой, чтобы целовать девочек."
        m "Я имею в виду, что я делаю это, и я не лесбиянка."
        call her_main("...............","angry","angry")
        her "[genie_name]--"
        m "Никаких, \"[genie_name]ов\"! Это твоя задача на сегодня!"
        m "Найди какую-нибудь милашку и \"чмокни\" ее!"
        call her_main("[genie_name], но я--","open","worried")
        m "Иди, [hermione_name]."
        call her_main("[genie_name]!......","normal","frown")
        m "Я сказал, свободна."
        call her_main("*Хм!*...","annoyed","frown")

    #Second time event.
    else:
        m "[hermione_name], я дам тебе сегодня, сорок пять очков!"
        m "Интересно?"

        if whoring >= 12 and whoring < 15: # LEVEL 05 FIRST EVENT.
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Смотря, за что...","normal","base",xpos="right",ypos="base")
            her "Придется ли мне снова делать что-то развратное?"
            m "\"развратное\"??! Когда это я--?"
            call her_main("Серьезно, [genie_name]?","open","angryCl")
            m "Ладно, ладно... Я хочу, чтоб ты поцеловалась со своей одноклассницей."
            call her_main("Ох, это все?","angry","angry") # :(
            m "Да... Довольно простое задание, не так ли?"
            m "И ты конечно получишь сорок пять очков."
            call her_main(".............","normal","frown")
            m "Так... Ты готова к этому?"
            call her_main("Я посмотрю, что можно сделать, [genie_name]...","annoyed","angryL")
            m "Отлично. Увидимся после занятий."
            call her_main("................","annoyed","annoyed")

        elif whoring >= 15 and whoring < 18: # LEVEL 06. Event level 02.
            call her_main("Я полагаю...","annoyed","ahegao",xpos="right",ypos="base")
            m "Отлично. Все что тебе нужно сделать, это поцеловаться с другой девочкой."
            call her_main("Понятно...","annoyed","down")
            m "Готова для этой задачи, [hermione_name]?"
            call her_main("Я полагаю...","annoyed","worriedL")
            m "Отлично. Увидимся после занятий."

        elif whoring >= 18: # LEVEL 07+ Event level 03.
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Конечно, почему нет?","base","base",xpos="right",ypos="base")
            m "Отлично."
            m "Я хочу, чтобы ты поцеловала другую девочку."
            call her_main("Хорошо.","soft","baseL")
            call her_main("Я знаю пару девушек, которые жаждут внимания и не прочь устроить небольшое шоу.","smile","glance")
            m "Отлично. Жду тебя после занятий."

    $ hg_pr_KissAGirl_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_KissAGirl_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld


    #First time event.
    if whoring >= 12 and whoring < 15: # LEVEL 05

        #Event A
        if one_out_of_three == 1:
            stop music fadeout 1.0
            m "[hermione_name]..."
            m "Удалось ли тебе выполнить поручение?"
            show screen blktone
            call her_main("Я...","open","worried",xpos="right",ypos="base")
            m "Я просил тебя, поцеловаться с другой девочкой..."
            m "Ты сделала это?"
            call her_main("Я...","open","worriedL")
            her "Я пыталась, [genie_name]. Я правда пыталась."
            m "И?"
            call her_main("Ну...","annoyed","worriedL")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            her "Мне было стыдно и неловко..."
            m "Так ты это сделала или нет?"
            call her_main("...Нет, [genie_name]...","annoyed","angryL")
            her "Все, что я сделала, это выставила себя полной дурой...."
            call her_main("На глазах у всего класса...","angry","angry")
            m "Расскажи, что случилось, [hermione_name]."
            call her_main("Нет, не буду, [genie_name].","annoyed","angryL")
            her "Ни за что на свете!"
            call her_main("Почему я должна выполнять такие дурацкие задачи?!","shock","worriedCl")
            her "В чем смысл всего этого?"
            call her_main("Я ненавижу это!","scream","angryCl")
            call her_main("...............","annoyed","angryL")
            her "................."
            m ".............."
            m "Ты не получишь очков, понятно?"
            call her_main("Мне все равно...","scream","angryCl")
            $ mad +=25

            $ hg_pr_KissAGirl_OBJ.inProgress = False
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        #Event A
        elif one_out_of_three == 2:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила поручение?"
            show screen blktone
            call her_main("Да, [genie_name]...","open","closed",xpos="right",ypos="base")
            m "Хорошо. Расскажи мне в деталях."
            call her_main("Ну, я поцеловала девочку. Как вы и велели, [genie_name].","annoyed","suspicious")
            m "Я полагаю, это было неловко, да?"
            call her_main("Очень, [genie_name].","annoyed","angryL") # :( D: :D::D:D:D::D::D::D::DDD:DD
            m "Ты наслаждалась этим хотя бы?"
            call her_main("*Humph!*...","annoyed","annoyed")
            m "Так ты поцеловала девочку, и тебе понравилось?"
            call her_main("Да...","disgust","glance")
            m "С языком?"
            call her_main("Да...","disgust","glance")
            her "Это был настоящий поцелуй взасос, если вам интересно."
            her "Могу ли я получить очки?"
            call her_main("Пожалуйста, [genie_name]...","annoyed","angryL")
            m "Что ж, хорошо..."

        #Event C
        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила поручение?"
            show screen blktone
            call her_main("Да, [genie_name].","open","closed",xpos="right",ypos="base")
            m "Хорошо. Расскажи мне."
            call her_main("Это было замечательно, [genie_name].","open","closed")
            m "Отлично. Расскажи."
            call her_main("Что бы вы хотели узнать, [genie_name]?","open","angryCl")
            m "Все! Была ли девочка симпатичной?"
            m "Она ответила на твой поцелуй?"
            call her_main("Она была симпатичной, [genie_name].","open","suspicious")
            her "И она ответила на мой поцелуй..."
            call her_main("...........","annoyed","closed")
            call her_main("Что-нибудь еще, [genie_name]?","open","suspicious")
            m "...."
            m "Почему ты такая сложная?, [hermione_name]?"
            call her_main("Со всем уважением, [genie_name]...","open","angryCl")
            her "Вы сказали мне поцеловаться с другой девушкой, и я..."
            call her_main("Теперь, не могли бы вы быть так любезны заплатить мне?","normal","base")
            m "......................"

            menu:
                "\"Ладно. Вот твои очки, девочка.\"":
                    pass
                "\"Мне не нравится твой тон, [hermione_name].\"":
                    call her_main("Ну, это печально, [genie_name].","open","angryCl")
                    m "Конечно..."
                    m "Поэтому никаких очков, наглая маленькая ведьма."
                    stop music fadeout 1.0
                    call her_main("Что?","normal","base")
                    call her_main("[genie_name], вы не можете этого сделать!","open","worried")
                    m "Уходи."
                    call her_main("Н-но--","open","worriedL")
                    call her_main("[genie_name], пожалуйста!","open","worried")
                    her "Эта девочка из \"Пуффендуя\" и--"
                    m "Слишком поздно, [hermione_name]."
                    m "Свободна."
                    call her_main("......","angry","base",tears="soft")
                    $ mad +=25

                    $ hg_pr_KissAGirl_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).


    elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.

        #Event A
        if one_out_of_three == 1:
            m "[hermione_name], ты выполнила поручение?"
            show screen blktone
            call her_main("Да, [genie_name]...","open","closed",xpos="right",ypos="base")
            m "Ну, не стой просто так. Рассказывай давай."
            call her_main("Эм, хорошо...","open","base")
            her "Эта девочка из \"Когтеврана\"..."
            call her_main("Я думаю, что она, возможно, была из младших классов, но я не спрашивала...","soft","baseL")
            her "Мы разговорились о мальчиках..."
            call her_main("И она сказала мне, что никогда не целовалась...","open","closed")
            her "И она обеспокоена тем, что плохо целуется..."
            call her_main("Поэтому я просто предложила свою помощь...","base","base")
            call play_music("playful_tension") # SEX THEME.
            her "Затем мы закрылись в одной туалетной кабинке..."
            call her_main("Практиковались...","base","base")
            call her_main("Она быстро уловила смысл... Я думаю, она может быть очень хороша в этом, с некоторой практикой...","open","base")
            call her_main("Кроме того, она была довольно очаровательна...","base","base")
            call her_main("Она называла меня \"[hermione_name]\"...","smile","baseL")
            m "Хм..."
            m "Я не помню, чтобы посылал тебя с заданием втягивать маленьких детей, [hermione_name]."
            call her_main("\"Маленьких детей\"? [genie_name], пожалуйста...","smile","glance")
            her "Вы должны были видеть эту девушку..."
            her "Миниатюрная? Может быть... Но точно не \"ребенок\"."
            call her_main("И я уверяю вас, что она была какой угодно, но не смущенной.","smile","angry")
            her "На самом деле, под конец нашей \"практики\", она стала даже немного несносной..."
            call her_main("У меня даже появилось чувство, что она просто воспользовалась мной...","open","base")
            m "Oх... Ну, в таком случае..."
            call her_main("","base","base")

        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name]. Ты выполнила свое задание?"
            show screen blktone
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Да, [genie_name].","open","closed",xpos="right",ypos="base")
            m "Расскажи, как все прошло."
            call her_main("Что ж... Эм...","open","base")
            her "Есть одна девушка, которая любит девочек...."
            her "Я подумала, что она будет идеальным кандидатом для моей задачи..."
            her "Поэтому сказала ей, что я хотела бы поцеловать ее..."
            call her_main("Она сказала, что мы должны пойти в туалет для девочек...","open","down")
            her "Но я просто поцеловала ее прямо в коридоре..."
            call her_main("И она поцеловала меня в ответ, но...","open","base")
            call her_main("Это было странно и очень быстро...","angry","down_raised")
            her "Как она поцеловала меня..."
            call her_main("Она сделала это как мальчик, [genie_name]...","angry","base")
            call her_main("Агрессивно, но уверенно...","angry","down_raised")
            call her_main("Естественно, рядом мгновенно образовалась небольшая толпа...","upset","closed")
            call her_main("В основном конечно мальчики...","open","base",cheeks="blush")
            call her_main("Некоторые из них даже подбадривали нас...","open","worriedCl",cheeks="blush")
            call her_main(".....","base","suspicious")
            her "Кстати, девушка, которую я поцеловала, [genie_name]..."
            m "Хм...?"
            call her_main("Она одна из тех непопулярных детей...","open","closed")
            her "Я знаю, что другие студенты иногда смеются над ней..."
            call her_main("Но сегодня все изменилось...","base","suspicious")
            her "Я в одиночку вывела эту девушку из социального изгоя..."
            call her_main("В \"лесбиянку, которая целовалась с Гермионой Грейнджер\"!","smile","angry")
            m "Воу... Ты прямо герой..."
            call her_main("Я полагаю, да, [genie_name]...","base","glance")
            her "Я изменила жизнь этой бедной девушки..."
            m "Ты меня растрогала..."

        #Event C
        elif one_out_of_three == 3:
            show screen blktone
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("[genie_name]?","open","closed",xpos="right",ypos="base")
            m "Да, [hermione_name]?"
            call her_main("Могу я задать вам вопрос, [genie_name]?","open","base")
            m "Конечно."
            call her_main("Эм...","annoyed","angryL")
            call her_main("Почему мальчики так любят смотреть, как девочки целуются друг с другом, [genie_name]?","disgust","glance")
            menu:
                m "..."
                "\"Кто знает? Странные мальчики.\"":
                    call her_main("Да, так и есть, не так ли...?","angry","down_raised")
                    m "Да, да..."
                    m "И именно поэтому молодые девочки, такие как ты...."
                    m "Часто интересуются гораздо более старшими джентльменами..."
                    call her_main("??!","angry","base")
                    call her_main("Это не то, что я имела в виду, [genie_name]...","annoyed","annoyed")
                "\"Ты не поймешь, девочка.\"":
                    call her_main("Эм...","upset","closed")
                    call her_main("А что насчет вас, [genie_name]?","angry","base")
                    her "Вам это нравилось, когда вы были мальчиком?"
                    m "Ты имеешь в виду, любил ли я наблюдать за двумя целующими девочками?"
                    m "Ну, конечно."
                    m "Я все еще это делаю..."
                    call her_main("Ох...","upset","closed")
                "\"Целующиеся девочки? Где?!!\"":
                    call her_main("Тск!......................","angry","angry",emote="01") # :(
            call her_main("Ну, я спрашиваю у вас это, [genie_name], потому что...","open","down")
            call her_main("...Это своего рода становится новой тенденцией в нашей школе...","angry","base")
            her "Некоторые девушки хотят сделать это, чтобы привлечь внимание мальчика, которого они любят..."
            m "Ты одна из тех девушек, [hermione_name]?"
            call her_main("Я полагаю...","angry","down_raised")
            call her_main("Я имею в виду, только из-за услуги, которую вы у меня купили, [genie_name]...","upset","closed")
            m "Хорошо... Расскажи больше."
            call her_main("Ну, как вы знаете, я довольно популярна...","smile","happyCl",emote="06")
            call her_main("Поэтому все, что мне нужно было сделать, это просто упомянуть, что я не возражаю сделать это...","base","happyCl")
            her "И было около шести девушек, которые встали вокруг меня..."
            call her_main("Я конечно выбрала девушку из \"Гриффиндора\"...","base","base")
            call her_main("И мы провели небольшое шоу прямо посреди класса...","open","base")
            m "Хорошо... С языком и все такое?"
            call her_main("Да, [genie_name].","annoyed","worriedL")
            m "Отличная работа."
            call her_main("","base","base")

    elif whoring >= 18: # LEVEL 07+

        #Event A
        if one_out_of_three == 1: #Snowballing
            label snowballing:
                pass
            m "[hermione_name]..."
            show screen blktone
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Добрый день, [genie_name].","open","closed",xpos="right",ypos="base")
            m "Ты выполнила поручение, девочка?"
            call her_main("Да, [genie_name].","soft","base")
            m "Я весь во внимании..."
            call her_main("Ну, я поцеловала эту надоедливую блондинку из \"Слизерина\"...","annoyed","suspicious")
            m "Хм... \"надоедливую\", да?"
            m "Потому что она из \"Слизерина\"."
            call her_main("Именно так, [genie_name].","open","closed")
            m "Хм..."
            m "Тебе не кажется, что это немного предвзято с твоей стороны?"
            m "Или я должен сказать, что ты в настоящее время \"факулист\"?"
            call her_main("...\"факулист\", [genie_name]?","annoyed","annoyed")
            m "Ну, ты знаешь... Это как \"сексист\" или \"эгоист\"..."
            m "Ты просто вставляешь \"ист\" и после этого оно, автоматически становится плохим словом..."
            call her_main("Слова \"факулист\" - не существует, [genie_name]...","soft","baseL")
            m "Не существует? Тогда подожди..."
            call her_main(".............?","annoyed","annoyed")
            m "\"Факультофобия\"...?"
            m "Нет, подожди, я понял!"
            m "\"Факультофоб\"!"
            call her_main("Прекратите, [genie_name]. Я не имею отношения к этим странным словам...","normal","frown")
            her "\"Слизеринцы\" злые и надменные. Никто не любит их, и это факт!"
            m "Ладно, неважно. Вернемся тогда к твоим \"лобзаниям\"."
            call her_main("...............","annoyed","worriedL")
            her "Как я и говорила..."
            call her_main("Я поцеловала девушку из \"Слизерина\"...","open","base")
            call her_main("Обычно, я бы никогда этого не сделала...","annoyed","angryL")
            her "В любом случае, не с кем из этого подлого факультета..."
            call her_main("Но она подошла ко мне первой и практически умоляла меня сделать это с ней...","annoyed","annoyed")
            call her_main("И она...","annoyed","angryL")
            her "Честно говоря..."
            call her_main("Она была довольно привлекательной....","annoyed","annoyed")
            call her_main("Для того, кто из \"Слизерина\"...","upset","closed")
            call her_main("Я не спрашивала ее, зачем она так отчаянно хотела этого....","open","closed")
            her "Вероятно, она просто пыталась повысить свою популярность за мой счет..."
            her "Или также может быть, что кто-то из школьного персонала купил эту услугу у нее..."
            call her_main("Так же, как вы покупаете мои услуги, [genie_name]...","open","annoyed",cheeks="blush")
            m "(Снейп?)"
            call her_main("Если это так, я уверена, что это был профессор Снейп...","angry","angry")
            m "Что? Он бы никогда..."
            call her_main("Вы должны действительно расследовать деятельность профессора Снейпа, [genie_name]...","annoyed","angryL")
            m "Конечно..."
            m "Пока мы говорим, я занесу его в свой \"список плохих мальчиков\"..."
            call her_main("..........","disgust","glance")
            m "Что случилось потом, [hermione_name]?"
            call her_main("Ох, точно...","open","down")
            her "Ну, мы целовались какое-то время..."
            her "Она была очень... страстной."
            call her_main("Так что я думаю, это было довольно зрелищно...","angry","wink")
            her "Мальчики подбадривали и свистели..."
            call her_main("Поэтому, мы решили немного \"поиграть в снежки\"...","base","down")
            m "Прости, что вы решили?"
            call her_main("\"Поиграть в снежки\", [genie_name].","angry","wink")
            call her_main("Это когда одна девушка плюет в рот другой девушке...","base","glance")
            her "Мы называем это \"игра в снежки\"..."
            her "Мальчики действительно сходят с ума от этого по какой-то причине..."
            m "Могу себе представить..."
            call her_main("Так она плюнула мне в рот...","open","closed")
            her "А потом я плюнула в ее..."
            call her_main("Хотя я бы скорее плюнула ей в лицо!","angry","angry",cheeks="blush")
            call her_main("Потом она вернула мою слюну...","annoyed","angryL")
            call her_main("И мне пришлось бороться с желанием ударить ее самодовольное лицо за это...","angry","angry",cheeks="blush")
            call her_main("Но я не думала, что мальчики оценят это...","upset","closed")
            m "Ну, ты была бы удивлена..."
            call her_main("В любом случае, после этого мы целовались еще немного...","base","down")
            her "А потом перерыв закончился..."
            call her_main("И нам пришлось бежать в класс...","angry","wink")
            m "*Вздох...* Беззаботные и невинные школьные годы..."
            m "Домашние задания... Классы..."
            m "Одноклассницы, \"игра в снежки\" во дворе..."
            m "Прекрасно, [hermione_name]."
            call her_main("","grin","baseL")

        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, [genie_name].","open","closed",xpos="right",ypos="base")
            call her_main("Только... эм...","grin","baseL")
            m "Что?"
            call her_main("Ну... У меня есть подруга...","base","base")
            her "Ее имя Джинни Уизли..."
            call her_main("И... эм...","base","baseL",cheeks="blush")
            her "Я не уверена, как это сказать..."
            m "Просто скажи, [hermione_name]."
            call her_main("Ну, мы решили пропустить урок зельеварения вместе...","open","base")
            her "И вместо него подготовиться к тесту по Гербологии..."
            her "Итак, я и Джинни, мы..."
            her "И мы поговорили о мальчиках..."
            m "Серьезно..."
            call play_music("playful_tension") # SEX THEME.
            call her_main("А потом я поцеловала ее...","open","baseL",cheeks="blush")
            call her_main("И Джинни ответила на мой поцелуй с такой страстью...","base","glance")
            her "Что в итоге, мы делали больше, чем просто целовались..."

            #if not kissed_ginny:
            #    call nar(>Your curiosity about Ginny grows!)
            #$ kissed_ginny = True

            g9 "А потом у вас была драка подушками в нижнем белье?"
            call her_main("Эм... Нет...","open","squint",cheeks="blush")
            m "Что вы тогда делали?"
            call her_main("Я вам не скажу, [genie_name].","base","baseL",cheeks="blush") # :)
            her "Вы послали меня, чтобы я поцеловала девушку..."
            her "И именно это я и сделала."
            call her_main("Остальное останется в тайне.","angry","wink")
            m "Это жестоко, маленькая ведьма."
            call her_main("Мои очки, пожалуйста.","smile","glance") # :)
            m "Ладно..."

        #Event C #Removed
        elif one_out_of_three == 3: ### EVENT (C) Only takes place once
            if lazy_aka_not_yet:
                jump snowballing #Removed "Pass"
            else:
                jump snowballing

            $ lazy_aka_not_yet = False #Makes sure this event only takes place once.
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила поручение?"
            show screen blktone
            with d3
            call her_main("Да, [genie_name].","base","base",xpos="right",ypos="base")
            m "Великолепно. Расскажи мне все."
            show screen blktone
            with d3
            call her_main("Конечно.","smile","glance")
            her "Я решила пойти по другому методу..."
            stop music
            call her_main("Я подумала, что еслиииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииииии","open","base",xpos=500)
            m "Что?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            her "Если бы я моглааааааааааааааааааааа"
            pause
            pause
            pause
            with hpunch
            g4 "{size=+5}Черт подери!!!{/size}"
            g4 "{size=+5}АКАБУР?!!!{/size}"
            a4 "А...? Что?!! Что ты хочешь от меня?"
            a4 "Дата релиза не установлена! Хватит меня спрашивать!"
            g4 "О чем ты говоришь?"
            a5 "Я имею в виду, я не сплю..."
            a7 "*Зевок*..."
            a5 "................"
            m "Так Гермиона теперь будет заикаться? Да?"
            pause
            pause
            g4 "Ты все еще здесь?"
            a1 "Я не сплю..."
            a5 "Просто прикрыл глаза..."
            g4 "Черт, чувак."
            g4 "Просто иди поспи немного, пока все не испортил."
            m "Иди поспи и закончи это дерьмо."
            a1 "Я не могу..."
            a1 "Я хочу, чтобы эта игра была выпущена как можно скорее..."
            a1 "Нет, не так. Я хочу, чтобы ее выпустили как можно скорее..."
            a1 "Люди доверяют мне... и..."
            a7 "*зевок*..."
            a1 "И...."
            pause
            pause
            m "Акабур?"
            m "Чувак?"
            pause
            pause
            m "*Вздох*...Ну, мы могли бы пропустить это событие, я полагаю."
            m "Только один раз..."
            m "И у Гермионы уровень \"развращения\"  действительно повысился..."
            m "Таким образом, нет никакой потребности в..."
            aa "Хррр....хрр....."
            aa "Хрр.... Лола? нет... Убери свои сиськи, я сказал... Хрррр....."
            aa "Хрррр.... И не называй меня так.... Хрр...."
            m "*Вздох...* Это просто печально..."

    $ gryffindor +=45
    m "\"Гриффиндор\" получает 45 очко!"
    her "Спасибо, [genie_name]."

    $ hg_pr_KissAGirl_OBJ.points += 1
    $ hg_pr_KissAGirl_OBJ.inProgress = False

    if hg_pr_KissAGirl_OBJ.points >= 2:
        $ hg_pr_KissAGirl_OBJ.complete = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
