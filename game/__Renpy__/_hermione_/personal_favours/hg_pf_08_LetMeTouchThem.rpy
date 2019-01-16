

label hg_pf_LetMeTouchThem: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_LetMeTouchThem_OBJ.points == 0:
        m "{size=-4}(Мне нравится играть с этими сиськами.){/size}"
    else:
        m "{size=-4}(Мне снова хочется поиграть с этими сиськами..){/size}"

    if hg_pf_LetMeTouchThem_OBJ.points < 1:
        menu:
            "\"(Да, давай сделаем это!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    if hg_christmas_OBJ.purchased:
        m "\"(Должен ли я попросить ее переодеться?)\""
        menu:
            "\"(Да, давай сделаем это!)\"":
                m "[hermione_name], прежде чем я попрошу об одолжении, я хочу, чтобы ты переоделась."
                call her_main("В чего?","open","worriedL")
                m "В мой Рождественский подарок."
                if whoring >= 14:
                    call her_main("Ваш подарок?","grin","baseL")
                    m "Да, я был хорошим мальчиком в этом году?!"
                    call her_main("...","base","glance")
                    call her_main("Прекрасно, дайте мне время завернуться.","base","down")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_christmas_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Не сейчас.)\"":
                pass

    $ current_payout = 35 #Used when haggling about price of th favor.

    if hg_pf_LetMeTouchThem_OBJ.points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.

        call bld
        m "[hermione_name]."
        call her_main("Да, [genie_name]?","base","base",xpos="base",ypos="base")

        if whoring < 9:
            m "Иди сюда и дай мне потрогать твои сиськи!" #Bit of flavour text, lol.
            jump too_much

        m "Как насчет того, чтобы продать мне еще одну услугу?"
        call her_main("Хмм... Хорошо...","open","base")
        her "Что это будет, [genie_name]?"
        m "Ну, как насчет того, чтобы подойти поближе ко мне и обнажить свою грудь...?"
        call her_main("!!!","open","base")
        m "Я хочу хорошо их сжать."
        call her_main("[genie_name]! Вам не кажется, что это слишком?","disgust","glance")
        m "Ты думаешь?"
        her "Я не одна из тех \"Слизеринских\" шлюх, вы же знаете..."
        m "Я знаю... Ты из \"Грифомана\"... или как там..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        call her_main("И если мне не понравится, я не буду продавать вам эту услугу, [genie_name]!","annoyed","worriedL")
        m "Конечно..."
        call her_main("...................","annoyed","angryL")
        m "Я дам тебе 35 очков."
        call her_main(".......................","disgust","glance")
        her "Все, что вы будете делать, это только смотреть, [genie_name]?"
        m "Хорошо, но я больше люблю трогать на самом деле..."
        her "...................................."


    else: #Not first time.

        if whoring >= 9 and whoring < 15: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.

            call bld
            m "[hermione_name]..."
            call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
            m "Мне хочется немного поиграть с твоими сиськами..."
            call her_main("[genie_name]... я бы предпочла сама это, если бы вы не сделали такого предложения...","annoyed","annoyed")
            m "Почему? Слишком трудно сопротивляться?"
            her "Ничего подобного, [genie_name]."
            m "Я дам тебе 35 очков..."
            call her_main("..................","annoyed","angryL")
            her "Хорошо, хорошо... Вы можете немного прикоснуться к ним..."

        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.

            call bld
            m "[hermione_name]..."
            call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
            m "Мне хочется немного поиграть с твоими сиськами..."
            call her_main("Конечно [genie_name]...","base","ahegao_raised")

    call her_walk_desk_blkfade
    hide screen genie

    show screen genie_and_tits_01
    with d1
    call hide_blkfade
    stop music fadeout 1.0
    call ctc

    call play_music("playful_tension") # SEX THEME.

    $ hermione_wear_bra = False
    show screen blktone
    call h_action("lift_top")
    call her_main("","","",xpos="mid",ypos="base")
    call ctc

    menu:
        m "..."
        "-Схватить их-":

            label no_smacking_tits:
                pass
            hide screen hermione_main
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            hide screen bld1
            hide screen blktone
            with fade
            call ctc


            #First event. (HERMIONE IS UNWILLING).
            if whoring >= 9 and whoring < 15:

                show screen blktone
                call her_main("..............................","angry","down_raised")
                m "У тебя хорошие сиськи, [hermione_name]..."
                call her_main("....................................","angry","down_raised")
                m "Тебе нравится, когда я их сжимаю?"
                call her_main("Простите меня, [genie_name], но вы снова путаете меня с этими блудницами...","upset","closed")
                call her_main("Я только позволяю вам нежно трогать, потому что вы платите за это...","upset","closed")
                call her_main("Не потому, что мне это нравится...","upset","closed")
                m "Я вижу..."
                m "Так ты тогда больше похожа на проститутку..."
                call her_main("[genie_name]!","angry","wide")
                m "Проституткам платят за секс с мужчинами..."
                call her_main("Я никогда не буду делать нечто подобное!","upset","closed")

                call nar(">Ты сильно сжимаешь одну из сисек девушки и сжимаешь другую несколько раз потянув в сторону.")

                call her_main("Ах...","open","worriedCl")
                m "Наслаждаешься, [hermione_name]?"

                if whoring >= 9 and whoring < 12:
                    call her_main("[genie_name], я делаю это только--","upset","closed")

                    call nar(">Ты сильно сжимаешь обе сиськи...")

                    call her_main("Ах...","shock","worriedCl")
                    m "Скажи мне, что тебе это нравится, [hermione_name]!"
                    call her_main("[genie_name], я позволяю делать это со мной, только потому--","open","worriedCl")
                    m "Я знаю, знаю..."
                    m "Ты начинаешь звучать как заезженная пластинка."
                    call her_main("....","annoyed","annoyed")
                    call blkfade

                    ">Ты отпустил сиськи девушки..."

                else: #12+
                    call her_main("Ах...","open","down")

                    call nar(">Ты сжимаешь ее сиськи еще несколько раз, затем начинаешь дергать их...")

                    call her_main("Ах... [genie_name]...","open","base")
                    m "Что? Тебе это нравится?"
                    call her_main("Нет... я...","open","base")
                    m "Не ври своему директору, [hermione_name]!"

                    call nar(">Ты сжимаешь ее сиськи еще раз...")

                    call her_main("Ах...","open","down")
                    call her_main("Я не вру, [genie_name]...","open","down")
                    call her_main("Почему мне это должно нравится?","open","base")
                    m "Я не знаю [hermione_name]. Ты скажи мне."

                    call nar(">Ты продолжаешь массировать ее грудь...")

                    call her_main("Ах... Я...","open","base")
                    m "Да, что ты?"
                    call her_main("Это... ничего, [genie_name]...","angry","base")
                    m "Ох, я думаю, что это что-то."
                    m "Я думаю, тебе нравится, как я сжимаю их."
                    call her_main("[genie_name], пожалуйста...","angry","down_raised")

                    if daytime:
                        call her_main("Занятия вот-вот начнутся...","angry","down_raised")
                    else:
                        call her_main("Становится поздно...","angry","down_raised")

                    call her_main("Могу я идти, [genie_name]? Пожалуйста?","angry","base")

                    m "Конечно, иди..."
                    pause 2
                    call her_main("...............","angry","down_raised")
                    pause.2

                    call her_main("[genie_name], вы все еще ... держите меня...","angry","base")
                    m "Ох, точно... моя вина...."
                    call blkfade

                    ">Ты отпускаешь грудь Гермионы..."

            #Third Event.
            elif whoring >= 15:

                show screen blktone
                call her_main("Ах...","soft","ahegao")
                m "Сегодня ты более чувствительна, не так ли?"
                call her_main("Я полагаю...","base","glance")
                call her_main("Ах...","open","worriedCl")
                m "Тебе нравится, когда я сжимаю их вот так?"
                call her_main("Я думаю, [genie_name]... Ах...","base","glance")
                m "Хех..."
                m "Что если я ущипну твои соски?"
                call her_main("!!!","angry","base")
                call her_main("Ах! [genie_name]...","open","worriedCl")
                m "А что, если я сделаю так?"
                call nar(">Ты хватаешь девушку за ее твердые соски и начинаешь тянуть...")
                call her_main("Ах... Ах... Ах... [genie_name]...","shock","worriedCl")
                m "Что, если я потяну еще сильнее?"
                with hpunch

                call her_main("Ах... [genie_name], пожалуйста...","scream","wide")
                call nar(">Гермиона сжимает край вашего стола, чтоб не сделать шаг к вам...")
                m "Хорошая девочка..."
                call her_main("*Тяжело дышет*","grin","dead")
                m "Тебе понравилось?"
                call her_main("Ты делаешь мне больно, [genie_name]...","shock","baseL",cheeks="blush",tears="soft")
                m "Но тебе это нравится?"

                if whoring < 18:
                    call her_main("Ах... Да, [genie_name]... Я не знаю почему, но я делаю...","clench","worried",cheeks="blush",tears="soft")
                else:
                    call her_main("Ах... Да, [genie_name]... Мне нравится...","silly","worried",cheeks="blush",tears="soft")

                m "Хорошая девочка..."
                call nar(">Ты отпускаешь ее соски...")
                call her_main("Ах...","silly","worried",cheeks="blush",tears="soft")

                show screen bld1
                call hide_blktone

                m "Это все на сегодня, [hermione_name]..."
                call her_main("Ах...?","shock","baseL",cheeks="blush",tears="soft")
                m "Что такое? Ты выглядишь разочарованной."
                m "Я заплачу тебе, конечно,..."
                call her_main("Это не так, [genie_name]...","angry","suspicious",cheeks="blush")
                call her_main("Это...","angry","suspicious",cheeks="blush")

                if daytime:
                    call her_main("Просто у меня все еще осталось время, прежде чем я уйду на занятия и...","shock","baseL",cheeks="blush",tears="soft")
                else:
                    call her_main("У нас еще есть время, не так ли?","shock","baseL",cheeks="blush",tears="soft")

                call her_main("Эм...","angry","suspicious",cheeks="blush")
                call her_main("...................","angry","suspicious",cheeks="blush")
                m "Ты хочешь, чтобы я сделал тебе больно, не так ли?"

                if whoring < 18:
                    call her_main("Я не \"хочу\"... ","shock","baseL",cheeks="blush",tears="soft")
                    call her_main("Но если вы настаиваете [genie_name]...","silly","worried",cheeks="blush",tears="soft")
                    m "Хорошо, я настаиваю... видимо."
                else:
                    call her_main("Да, пожалуйста, [genie_name]!","shock","baseL",cheeks="blush",tears="soft")
                    call her_main("Я даже позволю вам сделать это бесплатно...","shock","baseL",cheeks="blush",tears="soft")
                    m "Ну, в таком случае..."

                call her_main("Ах...","silly","worried",cheeks="blush",tears="soft")
                call ctc
                call blkfade

                ">Ты проводишь еще немного времени с грудью Гермионы..."

        "-Шлепнуть их-":

            show screen blktone
            call nar(">Ты шлепаешь по сиськам Гермионы!")
            call slap_her

            #First Event (HERMIONE IS UNWILLING).
            if whoring >= 9 and whoring <= 11:

                $ mad += 20
                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ай! Больно! *ВСХЛИП!*","angry","worried",cheeks="blush")
                m "Тебе понравилось?"
                call her_main("Думаете мне... это \"понравилось\", [genie_name]..?","annoyed","annoyed")
                call her_main("Какая девушка в здравом уме хотела бы, чтобы так с ней обращались?")
                stop music fadeout 1.0

                hide screen blktone
                show screen bld1
                call set_hermione_action("none")
                pause.5

                call her_main("Вы злой и сумасшедший старик!","angry","worried",cheeks="blush",tears="soft")
                hide screen hermione_main
                call blkfade

                m "............"
                call play_sound("door")
                m "Хорошо, тогда у меня нет очков для \"Гриффиндра\"..."

                jump could_not_flirt #Favor failed! #Needs Blkfade!

            #Second Event.
            elif whoring >= 12 and whoring < 15:

                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ай!","angry","worried",cheeks="blush")
                call her_main("[genie_name], что вы делаете?")
                m "Не знаю... Мне это казалось хорошей идеей..."
                m "Тебе понравилось?"
                call her_main("...Конечно, нет, [genie_name].","annoyed","closed")
                m "Давай, тогда попробуем это снова."
                call her_main("Что?","annoyed","base")

                call slap_her

                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ай! Перестаньте, мне больно!")
                m "Признай, что тебе это нравится."
                call her_main("Но мне не...","disgust","down_raised")
                call her_main("Если вы планируете делать это со мной, [genie_name]...")
                call her_main("...тогда, я думаю, уйду.","annoyed","annoyed")
                m "Ладно, ладно..."

                jump no_smacking_tits #Jumps to usual tits molesting scene.

            #Third Event.
            elif whoring >= 15:

                call her_main("Ах!!!","scream","wide",cheeks="blush")
                call her_main("[genie_name], зачем вы это сделали?","grin","glance",cheeks="blush")
                m "Не знаю... Мне казалось, идея хорошая..."
                m "Тебе понравилось?"
                call her_main("..........","annoyed","base")
                call her_main("Я не извращенка...")
                call nar(">Ты еще раз шлепаешь Гермиону!")

                call slap_her

                call her_main("А-ах!!!","silly","down",cheeks="blush")
                m "Скажи мне, что тебе нравится!"
                her "[genie_name]... я..."
                call nar(">Ты делаешь серию шлепков!")

                call slap_her

                call slap_her

                call slap_her

                call nar(">Сиськи Гермионы очень высоко подпрыгивают, она полностью вышла из-под контроля")
                call her_main("А-ах!!! Ах!!! А-а-аха!!!","silly","ahegao",cheeks="blush",tears="soft")
                m "Тебе это нравится. Признай это."
                call her_main("...........","base","dead",cheeks="blush",tears="soft")
                call nar(">Ты ударяешь по ее сиськам еще раз.")

                call slap_her

                call slap_her

                call slap_her

                call her_main("А-ах! Да! Мне нравится, мне нравится! А-ах...","silly","ahegao",cheeks="blush",tears="soft")
                call her_main("...значит ли это, что я извращенка, [genie_name]?","angry","worried",cheeks="blush",tears="soft")
                m "Что?"
                m "Хватит нести чушь, [hermione_name]."
                m "Это совершенно естественно для девочки, когда наслаждаешься шлепками по сиськам."
                her "......"
                her "Вы уверены, [genie_name]?"
                m "Да. Поверь мне, я знаю."
                call nar(">Ты еще раз шлепнул по сиськам!")

                call slap_her

                call her_main("А-ах... Да... Спасибо, [genie_name].","silly","ahegao",cheeks="blush",tears="soft")
                m "Хорошо... Достаточно со шлепками..."

                jump no_smacking_tits #Jumps to usual tits molesting scene.


    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    call h_action("none") #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01
    hide screen groping_01
    hide screen groping_02
    hide screen groping_naked_tits

    call her_chibi("stand","desk","base")

    hide screen chair_left
    show screen genie
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main("","","",trans="fade",xpos="mid",ypos="base")

    stop music fadeout 1.0

    if whoring <= 17:
        m "Да, [hermione_name]. 35 очков \"Гриффиндору\"."
        $ gryffindor +=35

    call her_main("Спасибо, [genie_name]...","soft","baseL")

    if whoring < 12:
        $ whoring +=1

    $ hg_pf_LetMeTouchThem_OBJ.points +=1

    if whoring >= 9 and whoring < 12:
        $ new_request_12_heart = 1
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 12 and whoring < 15:
        $ new_request_12_heart = 2
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 15:
        $ new_request_12_heart = 3
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 3 #Event hearts level (0-3)


    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("desk","leave",2.5)

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    $ custom_outfit_old = temp_outfit

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme")
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme")
        $ hermione_sleeping = True
        jump night_main_menu
