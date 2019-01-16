

### HERMIONE PERSONAL FAVOUR 4 ###

### BUTT MOLESTER ###

label hg_pf_ButtMolester:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(Я хочу немного помять ее задницу.){/size}"

    if hg_pf_ButtMolester_OBJ.points < 1:
        menu:
            "\"(Да, сделаем это!)\"":
                pass
            "\"(В другой раз.)\"":
                jump silver_requests

    if hg_maid_OBJ.purchased:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Конечно!)\"":
                m "[hermione_name], прежде чем я скажу свою просьбу, я хотел бы чтобы ты переоделась в..."
                call her_main("В кого?","open","worriedL")
                m "Горничную."
                if whoring >= 5:
                    call her_main("Горничную?","base","squint")
                    m "Да, во французскую горничную."
                    call her_main("...","base","baseL")
                    call her_main("Ну, если вы настаиваете...","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_maid_OBJ)
                    pass
                else:
                    jump too_much
            "\"(в другой раз.)\"":
                pass

    hide screen hermione_main
    with d3

    if whoring > 8 and not cho_known:
        jump cho_intro

    #First time event
    if whoring >= 0 and whoring <= 5:

        $ new_request_05_heart = 1
        $ hg_pf_ButtMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Подойди ближе, дитя. Позволь мне немного потрогать твою попку."
        if whoring < 3:
            call her_main("Мою--","soft","surprised")
            call her_main("Мою попу?!","shock","shocked")
            jump too_much

        if hg_pf_ButtMolester_OBJ.points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            call her_head("[genie_name]?!","mad","wide",cheeks="blush",xpos="base",ypos="base")
            m "Расслабься, [hermione_name]. Это будут самые легкие 15 очков в твоей жизни, я обещаю."
            call her_head("Но....","angry","angry")
            m "Все что я сделаю это сожму несколько раз и все..."
            call her_head("Это так непристойно, [genie_name]................","annoyed","angryL",cheeks="blush")
            m "Никто ведь не обязан знать как ты получила эти очки..."
            call her_head("(Эти 15 очков и правда могут нам помочь...)","disgust","down_raised",cheeks="blush")
            call her_head("(Проклятье.....!)","angry","worriedCl",cheeks="blush")
        else:
            call her_head("Опять.....?","annoyed","angryL",cheeks="blush",xpos="base",ypos="base")

        call her_walk_desk_blkfade
        hide screen genie

        call her_head("..................","annoyed","angryL",cheeks="blush")
        call her_head("Хотите чтобы я повернулась, [genie_name]?","annoyed","angryL",cheeks="blush")
        call play_music("playful_tension") # SEX THEME.

        menu:
            m "Хмм..."

            #Event A
            "\"Да, повернись. [hermione_name].\"":
                call her_head("Как скажете, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head(".............","annoyed","angryL",cheeks="blush")
                call her_head("...........................","annoyed","angryL",cheeks="blush")
                call her_head("[genie_name], я хотела бы покончить с этим как можно скорее...","annoyed","angryL",cheeks="blush")
                m "Не торопи меня, [hermione_name]... Позволь насладиться моментом..."
                call her_head(".............................","annoyed","angryL",cheeks="blush")

                menu:
                    m "Хмм..."
                    "-Сжать ее булочки-":
                        pass
                    "-Шлепнуть-":
                        call slap_her #Calls slapping sound and visual.

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]?!!","scream","wide",cheeks="blush")

                        menu:
                            "\"Ладно, ладно... я не мог сопротивляться искушению....\"":
                                call her_head(".......................","annoyed","angryL",cheeks="blush")
                                pass
                            "-Шлепнуть еще раз-":
                                call slap_her #Calls slapping sound and visual.

                                call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                                call her_head("[genie_name], что вы делаете?!","angry","worriedCl",cheeks="blush")
                                call her_head("вы обещали что только потрогаете!","angry","worriedCl",cheeks="blush")

                                menu:
                                    "\"Ладно, ладно... я не смог сопротивляться искушению....\"":
                                        call her_head(".......................","annoyed","angryL",cheeks="blush")
                                        pass
                                    "-Шлепнуть снова-":
                                        call slap_her #Calls slapping sound and visual.

                                        call her_head("Ауч! Мне больно!","angry","worriedCl",cheeks="blush")
                                        call her_head("Это так унизительно!","angry","angry",cheeks="blush")
                                        call her_head("Вы обещали только трогать...","angry","angry",cheeks="blush")
                                        g4 "Стой спокойно, [hermione_name]!"
                                        call her_head("Вы переходите границы, [genie_name]!","angry","worriedCl",cheeks="blush")
                                        call her_head("Нисколько очков не стоят такого унижения!","scream","angry",cheeks="blush",emote="01")
                                        call her_head("Вы злоупотребляете своим положением, [genie_name]!","scream","angry",cheeks="blush",emote="01")
                                        g4 "Что?"
                                        call her_head("Я ухожу!","angry","worriedCl",cheeks="blush")

                                        menu:
                                            g4 "Тсс..."
                                            "\"Я... мне очень жаль...\"":
                                                call her_head("Просто не делайте так больше, [genie_name]...","annoyed","angryL",cheeks="blush")
                                                #pass
                                            "\"Ты не получишь очков за это!\"":
                                                $ mad += 20
                                                call her_head("Ха! Идите к черту, [genie_name]!","angry","angry",cheeks="blush")
                                                ### Takes place aftre you refuse to pay her the points.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                with d3

                                                call her_walk("desk","leave",3,redux_pause=1)

                                                g4 "Тсс! (Маленькая избалованная девочка!)"

                                                $ hg_pf_ButtMolester_OBJ.points += 1

                                                if daytime:
                                                    call play_music("day_theme")
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    call play_music("night_theme")
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu

                                            "\"За это я вычту с тебя очки!\"":
                                                $ mad += 30
                                                call her_head("Вы серьезно?!","scream","wide",cheeks="blush")
                                                $ gryffindor -=10
                                                g4 "Минус десять очков \"Гриффиндору\"!"
                                                g4 "Все! Дело сделано!"
                                                call her_head("Аррр...........","angry","angry",cheeks="blush")
                                                call her_head("........................","angry","angry",cheeks="blush")
                                                call her_head("Это не справедливо...","angry","suspicious",cheeks="blush",tears="messy")
                                                m "Что? Чего еще ты ждала устраивая мне истерику?"
                                                call her_head("Я ненавижу вас, [genie_name]! Ненавижу!","scream","worriedCl",cheeks="blush",tears="messy")

                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie

                                                call her_walk("desk","leave",2,action="run")

                                                m ".............."
                                                menu:
                                                    "\"Сожалеть...\"":
                                                        m "Черт... Чувствую себя как кусок дерьма..."
                                                        g9 "Но кто мог устоять и не отшлепать ее?"
                                                    "\"Считать себя правым.\"":
                                                        g4 "Она вынудила меня сделать это, несносная девка!"
                                                        m "Маленькая язва..."
                                                        g9 "Держу пари, на самом деле она наслаждалась этим, просто не хочет признавать этого..."

                                                $ hg_pf_ButtMolester_OBJ.points += 1

                                                if daytime:
                                                    call play_music("day_theme")
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    call play_music("night_theme")
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu

                #You apologized.
                call ctc
                show screen groping_02
                with d7
                call her_head("?!!!!!!","mad","wide",cheeks="blush")
                m "Что это, [hermione_name]?"
                call her_head("Ничего, [genie_name]...","angry","worriedCl",cheeks="blush")
                call her_head("Просто... ","angry","worriedCl",cheeks="blush")
                call her_head("Не могу поверить что это происходит на самом деле...","angry","worriedCl",cheeks="blush")
                call her_head("Это так... унизительно...","angry","worriedCl",cheeks="blush")
                m "Расслабься, [hermione_name]. Не похоже чтобы тебе не нравилось..."
                call her_head("Что? Конечно нет! Это извращение...","angry","worriedCl",cheeks="blush")
                call her_head("Я приношу эту жертву только ради своего факультета...","angry","worriedCl",cheeks="blush")
                m "Верно, сконцентрируйся на этом..."
                call her_head("....................","angry","angry",cheeks="blush")
                call bld
                call ctc
                call her_head("Но, [genie_name]...","open","baseL",cheeks="blush")
                call her_head("Почему {size=+7}Вы{/size} делаете это?","open","baseL",cheeks="blush")

                menu:
                    m "Хмм..."
                    "\"У меня есть свои причины...\"":
                        call her_head("Ох...","disgust","down_raised",cheeks="blush")
                        call her_head("Хмм...","annoyed","angryL",cheeks="blush")
                    "\"Во имя науки, естественно!\"":
                        call her_head("Серьезно?!","soft","wide")
                        call her_head("И что же вы изучаете?","soft","wide")
                        m "Да, конечно, я изучаю... Ээ..."
                        m "Думаю ты не поймешь, я разрабатываю совершенно новый тип волшебства..."
                        call her_head("Понятно...","soft","wide")
                        call her_head("Ладно, если это для исследований, то я рада помочь...","annoyed","angryL")
                    "-Просто сжать ее плотные ягодицы-":
                        show screen blktone8
                        with d3
                        ">Ты сжимаешь ягодицы Гермионы."
                        hide screen blktone8
                        with d3

                        call her_head("....................","open","baseL",cheeks="blush")
                        call her_head("(Я просто потерплю, как всегда.....?)","disgust","down_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты продолжаешь мять попку Гермионы..."
                ">Ты проводишь руками по внутренней стороне ее бедер..."
                hide screen blktone8
                with d3

                call her_head("................","angry","worriedCl",cheeks="blush")

                label connection_of_rapes:
                menu:
                    "-Проникнуть в трусики-":
                        show screen blktone8
                        with d3
                        ">Ты медленно просовываешь руку под ткань трусиков девочки..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... Что вы делаете...?","mad","wide",cheeks="blush")
                        m "Все в порядке, просто думай об очках, которые получит твой факультет..."
                        call her_head(".............","disgust","down_raised",cheeks="blush")

                        menu:
                            "-Протолкнуть один из пальцев в ее киску-":
                                call blkfade

                                ">Ты помещаешь палец аккурат на девичью щелку..."
                                call her_head("[genie_name]? Нет! Почему вы это делаете...?","mad","wide",cheeks="blush")
                                ">Гермиона пытается отстраниться от тебя..."

                                menu:
                                    "-Протолкнуть палец вглубь ее киски!-":
                                        ">Ты проталкиваешь палец в ее узкую киску..."
                                        ">Там очень тесно и горячо..."
                                        ">Правда довольно сухо... Не похоже чтобы это приносило ей какое-то удовольствие..."
                                        jump screams_of_rapings
                                    "-Позволить уйти...-":
                                        pass

                            "-Прикоснуться к ее анусу-":
                                call blkfade

                                ">Ты помещаешь один палец к анусу девочки..."
                                call her_head("[genie_name]? Нет! Что вы себе позволяете?!","mad","wide",cheeks="blush")
                                ">Гермиона пытается отстранится от тебя..."

                                menu:
                                    "-Проникнуть в задницу-":
                                        ">Ты проталкиваешь палец вглубь ее узенького ануса..."
                                        with hpunch
                                        call her_head("?!!","angry","wide")
                                        ">Внутри очень тесно и тепло..."
                                        jump screams_of_rapings
                                    "-Позволить девочке уйти...-":
                                        pass

                            "-Больше не испытывать удачу. Отпустить девочку-":
                                pass

                    "-Довольно на сегодня.-":
                        pass

            #Event B
            "\"Нет. Просто стой, [hermione_name].\"":
                call her_head("Как скажете, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], Поторопитесь, пожалуйста, вдруг кто-нибудь зайдет...","soft","baseL",cheeks="blush")
                m "В чем проблема, [hermione_name]?"
                m "Ты ведь знаешь, что делаешь это ради своего факультета."
                call her_head("Да, я знаю.","annoyed","angryL",cheeks="blush")
                call her_head("Но я бы не хотела, чтобы все знали...","annoyed","angryL",cheeks="blush")
                call her_head("Поэтому, пожалуйста, сделайте все по-быстрее...","annoyed","angryL",cheeks="blush")
                call her_head("Пожалуйста...","open","baseL",cheeks="blush")
                m "Ну, если ты настаиваешь..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "Что?"
                call her_head("Ничего, [genie_name]. Просто у вас холодные руки...","open","baseL",cheeks="blush")
                call bld

                show screen blktone8
                with d3
                ">Ты растираешь ладони о ноги Гермионы..."
                hide screen blktone8
                with d3

                call her_head(".........................","annoyed","angryL",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты хорошенько сжимаешь ее ягодицы..."
                hide screen blktone8
                with d3

                call her_head(".................","angry","worriedCl",cheeks="blush")
                m "Не отводи свой взгляд, [hermione_name]. Я хочу, чтобы ты смотрела в мои глаза."
                call her_head("Я не хочу, [genie_name]...","angry","worriedCl",cheeks="blush")

                menu:
                    m "..."
                    "\"Хорошо. Просто стой .\"":
                        call her_head("Спасибо, [genie_name]...","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты слегка сжимаешь ее ягодицы..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты продолжаешь наслаждаться ее упругой задницей в своих руках..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты шлепаешь Гермиону по заднице."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                    "\"Открой глаза, если не хочешь потерять свои очки!\"":
                        $ mad += 7
                        call her_head("Ах! {size=-5}(Ты старый извращ--{/size}","angry","worriedCl",cheeks="blush")
                        m "Ты что-то сказала, [hermione_name]?"
                        call her_head("Нет, ничего, [genie_name].","angry","angry")

                        show screen blktone8
                        with d3
                        ">Ты слегка сжимаешь ее ягодицы..."
                        ">Гермиона смотрит тебе в глаза, как договаривались..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","angry")
                        call her_head("...............................","annoyed","angryL",cheeks="blush")
                        m "Что я тебе говорил?"
                        call her_head("Да, я помню...","angry","worriedCl",cheeks="blush")
                        call her_head(".................................","angry","angry")
                        call her_head("...................................","annoyed","angryL",cheeks="blush")
                        call her_head("..................................................","annoyed","angryL",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты продолжаешь наслаждаться ощущением мягкой упругой попки в своих руках..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","angry")
                        jump connection_of_rapes

    #Second Event
    elif whoring >= 6 and whoring <= 15:

        $ new_request_05_heart = 2
        $ hg_pf_ButtMolester_OBJ.hearts_level = 2 #Event hearts level (0-3)

        m "Подойди ко мне, [hermione_name]. Я хочу немного помять твою попу."
        call her_head("Ну, как скажите...","open","baseL",cheeks="blush",xpos="base",ypos="base")

        call her_walk_desk_blkfade
        hide screen genie

        call her_head("Вы хотите, чтобы я повернулась, [genie_name]?","base","baseL",cheeks="blush")
        call play_music("playful_tension") # SEX THEME.

        menu:
            m "Хмм..."
            "\"Да, повернись, [hermione_name].\"":
                call her_head("Как скажете, [genie_name]...","base","baseL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head(".............","base","ahegao_raised",cheeks="blush")

                menu:
                    m "Хм..."
                    "-Сжать ее булочки-":
                        pass
                    "-Шлепнуть по попке-":
                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]....?","base","baseL",cheeks="blush")

                        menu:
                            "\"Ладно, ладно... я не смог удержаться....\"":
                                call her_head("Все в порядке...","base","baseL",cheeks="blush")
                                #pass
                            "-Шлепнуть снова-":
                                call slap_her

                                call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                                call her_head("[genie_name], почему вы меня шлепаете?!","base","baseL",cheeks="blush")
                                call her_head("Вы обещали что будете только щупать!","base","baseL",cheeks="blush")

                                menu:
                                    "\"Ладно, ладно... я не смог удержаться....\"":
                                        call her_head("Ох, ничего страшного...","base","baseL",cheeks="blush")
                                        #pass
                                    "-Шлепнуть еще разок-":
                                        call slap_her

                                        call her_head("[genie_name], не так сильно, пожалуйста...","silly","ahegao_raised",cheeks="blush")
                                        call her_head("Вдруг нас услышат?","silly","ahegao_raised",cheeks="blush")
                                        m "Хорошо, хорошо... продолжу мять твои ягодицы..."
                                        call her_head("................","base","baseL",cheeks="blush")

                call ctc
                show screen groping_02
                with d7

                call her_head("...................","base","baseL",cheeks="blush")
                m "Ты сегодня довольно немногословна, [hermione_name]."
                call her_head("Эммм... Я...?","base","baseL",cheeks="blush")

                if whoring <= 13:
                    call her_head("Ну, вы меня знаете, [genie_name]...","base","ahegao_raised",cheeks="blush")
                    call her_head("Я просто рада внести свой вклад в победу \"Гриффиндора\"....","base","ahegao_raised",cheeks="blush")

                call her_head("Я не возражаю если вы продолжите...","base","ahegao_raised",cheeks="blush")
                call her_head("(...щупать меня...)","base","glance",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты продолжаешь играть с попкой Гермионы..."
                ">Твоя рука продолжает скользить по внутренней части ее бедра..."
                hide screen blktone8
                with d3

                call her_head("................","base","baseL",cheeks="blush")

                label connection_of_rapes_02:
                menu:
                    "-Запустить руки в трусики-":
                        show screen blktone8
                        with d3
                        ">Ты медленно запускаешь руку под трусики девочки..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... Зачем вы...?","open","baseL",cheeks="blush")

                        if whoring <= 13:
                            m "Все в порядке, просто сконцентрируйся на очках, которые ты получишь..."
                        else:
                            m "Все хорошо, расслабься и получай удовольствие"

                        call her_head("Ох...как скажете...","open","baseL",cheeks="blush")

                        menu:
                            "-Протолкнуть один из пальцев в ее киску-":
                                call blkfade

                                ">Твоя рука проникает вниз, и ты трогаешь ее маленькую щель..."
                                call her_head("[genie_name]?","base","baseL",cheeks="blush")

                                menu:
                                    "-Протолкнуть палец в киску!-":
                                        ">Ты проталкиваешь палец вглубь узкой киски..."
                                        ">В ней очень тесно и горячо..."
                                        ">И довольно влажно...  похоже ей это очень даже нравится..."
                                        jump screams_of_pleasure
                                    "-Позволить ей уйти...-":
                                        pass

                            "-Потрогать ее анус-":
                                call blkfade

                                ">Ты помещаешь один из своих пальцев прямо на узенький анус девочки..."
                                call her_head("[genie_name]? Что вы пытаетесь сделать?","base","baseL",cheeks="blush")

                                menu:
                                    "-Протолкнуть пальчик в попку-":
                                        ">Ты вставляешь свой палец в ее узенькую дырочку..."
                                        with hpunch
                                        call her_head("Ах... Ваш палец в моей...","silly","worried",cheeks="blush",tears="soft")
                                        ">Внутри очень тесно и горячо..."
                                        jump screams_of_pleasure
                                    "-Позволить ей уйти...-":
                                        pass

                            "-Не испытывать удачу. Позволить девочке уйти-":
                                pass

                    "-Нет, на сегодня достаточно. Можешь уходить.-":
                        pass

            "\"Нет. Просто стой, [hermione_name].\"":
                call her_head("Как скажете, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], поторопитесь, пожалуйста, вдруг кто-нибудь зайдет...","soft","baseL",cheeks="blush")
                m "В чем проблема, [hermione_name]?"
                m "Ты же знаешь, что делаешь это ради своего факультета."
                call her_head("Да, я знаю.","annoyed","angryL",cheeks="blush")
                call her_head("Но я бы не хотела чтобы это знал кто-либо еще...","annoyed","angryL",cheeks="blush")
                call her_head("Поэтому, пожалуйста, сделайте все по-быстрее...","annoyed","angryL",cheeks="blush")
                call her_head("Пожалуйста...","open","baseL",cheeks="blush")
                m "Ну, если ты настаиваешь..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "Что?"
                call her_head("Ничего, [genie_name]. Просто у вас холодные руки...","open","baseL",cheeks="blush")
                call bld

                show screen blktone8
                with d3
                ">Ты растираешь руки о ножки Гермионы..."
                hide screen blktone8
                with d3

                call her_head(".........................","annoyed","angryL",cheeks="blush")

                show screen blktone8
                with d3
                ">Хорошенько сжать ее ягодички..."
                hide screen blktone8
                with d3

                call her_head(".................","angry","worriedCl",cheeks="blush")
                m "Не отводи взгляд, девочка. Я хочу смотреть в твои глаза."
                call her_head("Мне бы не хотелось, [genie_name]...","angry","worriedCl",cheeks="blush")

                menu:
                    m "..."
                    "\"Ладно. Просто стой и не двигайся.\"":
                        call her_head("Спасибо, [genie_name]...","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты массируешь ее попку..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты продолжаешь наслаждаться упругой попкой в своих руках..."
                        hide screen blktone8
                        with d3

                        show screen blktone8
                        with d3
                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                        ">Ты сжимаешь попку Гермионы в последний раз."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                    "\"Смотри мне в глаза, или не получишь очков!\"":
                        $ mad += 20
                        call her_head("Ррр! {size=-5}(Старый извращенец...--{/size}","angry","worriedCl",cheeks="blush")
                        m "Ты что-то сказала, [hermione_name]?"
                        call her_head("Нет, ничего, [genie_name].","angry","angry")

                        show screen blktone8
                        with d3
                        ">Ты слегка массируешь ее ягодицы..."
                        ">Гермиона смотрит тебе в глаза как ты и просил..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","angry")
                        call her_head("...............................","annoyed","angryL",cheeks="blush")
                        m "Что я тебе говорил?"
                        call her_head("Да, я помню...","angry","worriedCl",cheeks="blush")
                        call her_head(".................................","angry","angry")
                        call her_head("...................................","annoyed","angryL",cheeks="blush")
                        call her_head("..................................................","annoyed","angryL",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Ты продолжаешь наслаждаться ее упругой попкой..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","angry")
                        jump connection_of_rapes_02


    #Third Event
    elif whoring >= 16:

        $ new_request_05_heart = 3
        $ hg_pf_ButtMolester_OBJ.hearts_level = 3 #Event hearts level (0-3)

        hide screen bld1
        m "Подойди ближе, [hermione_name]. Я хочу пощупать твою попку."
        call her_head("Если я должна...","open","baseL",cheeks="blush",xpos="base",ypos="base")

        call her_walk_desk_blkfade
        hide screen genie

        call her_head("Вы хотите, чтобы я повернулась, [genie_name]?","base","baseL",cheeks="blush")
        call play_music("playful_tension") # SEX THEME.

        menu:
            m "Хмм..."
            "\"Да, повернись, [hermione_name].\"":
                call her_head("Как скажете, [genie_name]...","base","baseL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc
                call her_head(".............","base","ahegao_raised",cheeks="blush")

                menu:
                    m "Хмм..."
                    "-Сжать ее задницу-":
                        pass
                    "-Шлепнуть-":
                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]....?","base","baseL",cheeks="blush")

                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name], что вы делаете?!","silly","worried",cheeks="blush",tears="soft")
                        call her_head("Вы обещали только трогать!","silly","worried",cheeks="blush",tears="soft")
                        m "Ты хочешь чтобы я остановился, [hermione_name]?"

                        call slap_her

                        call her_head("Ахх!!","silly","ahegao_raised",cheeks="blush")
                        call her_head("...я-","disgust","down_raised",cheeks="blush")

                        call slap_her

                        call her_head("нет!!","scream","wide")
                        m "Тогда, что ты хочешь чтобы я сделал?"

                        call slap_her

                        call her_head("Продолжайте шлепать меня!!","silly","ahegao_raised",cheeks="blush")
                        m "Что ты говоришь, мне нужно шлепать?"

                        call slap_her

                        call her_head("Мою попку!!","silly","ahegao")
                        call her_head("Шлепайте мою распутную задницу!!","open_tongue","ahegao_raised",cheeks="blush")
                        m "Оо, ты должна просить лучше. Я не очень понял чего ты от меня хочешь..."

                        call slap_her

                        call her_head("Шлепайте мою похотливый зад сильнее!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                        m "Ты сегодня довольно шумная."

                        call slap_her

                        call her_head("Дааа!!","open_tongue","ahegao_raised",cheeks="blush")
                        call her_head("Сильнее!!","silly","ahegao")
                        m "А что, если кто-нибудь услышит?"

                        call slap_her

                        call her_head("Мне все равно!!","shock","wide",cheeks="blush")

                        call slap_her

                        call her_head("Дааа!!!","silly","ahegao_raised",cheeks="blush")

                        call slap_her

                        call her_head("Еще немного-","grin","ahegao")

                        call slap_her

                        call her_head("Я грязная девченка","silly","dead")

                        call slap_her

                        call her_head("Кон..кон..кончаю...","silly","ahegao")
                        call her_head("Я кончаю!!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                        ">Ты около минуты смотришь как девочка бьется в спазмах оргазма"
                        m "Ну чтож... продолжу щупать..."
                        call her_head("................","base","ahegao_raised")

                call ctc
                show screen groping_02
                with d7

                call her_head("-Ааа, неспаведлииииво-!!!","base","baseL",cheeks="blush")
                ">Ее голос срывается в писк когда ты продолжаешь тискать ее большую упругую задницу"
                m "Что? Что ты говоришь? Я тебя не расслышал, [hermione_name]."
                call her_head("Вы ублюдок!{image=textheart}","grin","ahegao_mad",cheeks="blush")
                ">Все тело Гермионы дрожит"
                m "Похоже, ты наслаждаешься."
                call her_head("Ну, вы меня знаете, [genie_name]...","base","ahegao_raised",cheeks="blush")
                call her_head("Я просто рада внести свой вклад","base","ahegao_raised",cheeks="blush")
                call her_head("Пожалуйста, я не против если вы продолжите...","base","ahegao_raised",cheeks="blush")
                call her_head("(...щупать меня...)","silly","dead")

                show screen blktone8
                with d3
                ">Ты продолжаешь щупать булочки Гермионы..."
                ">Твоя рука продолжает скользить по внутренней части ее бедра..."
                hide screen blktone8
                with d3

                call her_head("................","base","baseL",cheeks="blush")

                menu:
                    "-Двигать руками между ее ножек-":
                        show screen blktone8
                        with d3
                        ">Ты медленно кладешь руку к промежности девочки..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... Что вы делаете...?","base","ahegao_raised",cheeks="blush")
                        m "Что-то, что тебе понравится."
                        m "Расслабься и доверься мне."
                        call her_head("Ах, как скажете...","base","ahegao_raised",cheeks="blush")

                        menu:
                            "-Прикоснуться к киске-":
                                call blkfade

                                ">Ты помещаешь один палец прямо на щелку девочки..."
                                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush")

                                ">Ты проталкиваеш палец в ее узкую киску..."
                                ">Внутри горячо и тесно..."
                                ">И влажно...  Похоже Гермионе это очень даже нравится..."
                                call her_head("Ах... ваш палец внутри моей...","silly","ahegao")
                                call her_head("Ах... подождите--","angry","dead",cheeks="blush",tears="crying")
                                ">Ты начинаешь медленно двигать пальцем..."
                                call her_head("-Всего пятнадцать очков...-","shock","down_raised",cheeks="blush",tears="crying")
                                ">Ты немного ускоряешься..."
                                call her_head("{image=textheart}-Мой долг...-{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                                ">Ты начинаете тереть ее клитор..."
                                call her_head("!!{image=textheart}-Гриффиндор-{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                                m "Мы можем остановиться, если ты хочешь, конечно. "
                                call her_head("...","angry","dead",cheeks="blush",tears="crying")
                                m "Что??"
                                call her_head("...Продолжайте...","shock","down_raised",cheeks="blush",tears="crying")
                                m "Хмм?"
                                call her_head("Продолжайте теребить мою киску!!","scream","angry",cheeks="blush",tears="messy")
                                m "Хочешь чтобы я продолжал двигать пальцем в твоей вагине? Ты это хотела сказать?"
                                call her_head("Да, [genie_name]! {image=textheart} Трахайте мою киску своим пальцем!{image=textheart}","open_wide_tongue","ahegao",tears="messy")
                                ">Она шевелит бедрами и пытаеся насадиться на твой палец."
                                call her_head("Засуньте его поглубже в мою похотливую дырку!!{image=textheart}","silly","dead",tears="messy")
                                m "Хмм... я не думаю что мои пальцы годятся для такой задачи..."
                                ">Ты вытаскиваешь палец из хлюпающего влагалища девочки."
                                call her_head("Чего?!! Нет, вы не може-","scream","worriedCl",cheeks="blush",tears="crying")
                                ">...Ты вытаскиваешь дилдо из ящика своего стола."
                                call her_head("О, боже, да!!","grin","dead",cheeks="blush",tears="messy")
                                m "Кажется, это подойдет лучше чем палец, да?"
                                call her_head("Ахх!{image=textheart}","silly","dead",tears="messy")
                                m "Ты слишком развратная шлюшка чтобы удовлетвориться пальцами, верно?"
                                call her_head("ДА!ДАДА!!!","scream","angry",cheeks="blush",tears="messy")
                                call her_head("Совершенно верно!","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("Не останавливайтесь!","silly","ahegao",tears="messy")
                                ">Она насаживается на дилдо в твоих руках с такой силой, что кажется сейчас вырвет его из рук."
                                call her_head("Неостанавливайтесьнеостанавливайтесь-","grin","dead",cheeks="blush",tears="messy")
                                call her_head("Пожалуйстапожалуйстапожалуйста-","scream","worriedCl",cheeks="blush",tears="messy")
                                m "Тебе нравится, [hermione_name]?"
                                call her_head("Да! Мне очень нравится как вы шлепаете меня!","grin","dead",cheeks="blush",tears="messy")
                                call her_head("Я люблю когда вы меня трогаете!","scream","worriedCl",cheeks="blush",tears="crying")
                                call her_head("Я люблю когда вы играете с моими узкими дырками!","grin","ahegao_mad",cheeks="blush",tears="messy")
                                call her_head("Огосподигосподи","scream","surprised",cheeks="blush",tears="messy")
                                ">Гермиона пытается кричать от накрывшего ее оргазма, но от недостатка воздуха может только стонать."
                                call her_head("Оооооох...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                                jump ending_of_screams_of_pleasure

                            "-Потрогать анус -":
                                call blkfade

                                ">Вы прикладываешь большой палец к узенькому анусу девочки..."
                                call her_head("[genie_name]? Что вы хоти...-","open","baseL",cheeks="blush")

                                ">Ты проталкиваешь большой палец вглубь тесного ануса..."
                                with hpunch
                                call her_head("Ах... Ваш палец в моем...","silly","ahegao")
                                ">Внутри очень тепло и тесно..."
                                call her_head("Ах... Подож...-","angry","dead",cheeks="blush",tears="crying")
                                ">Ты медленно начинаешь двигать пальцем"
                                call her_head("-Всего пятнадцать очков...-","shock","down_raised",cheeks="blush",tears="crying")
                                ">Ты немного увеличиваете скорость"
                                call her_head("{image=textheart}-Мой долг-{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                                ">Ты вращаешь палец, двигая в ней."
                                call her_head("!!{image=textheart}-перед Гриффиндором...-{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                                m "Мы можем остановиться прямо сейчас, если ты хочешь этого."
                                call her_head("...","angry","dead",cheeks="blush",tears="crying")
                                m "Что?"
                                call her_head("...Нет, продолжайте...","shock","down_raised",cheeks="blush",tears="crying")
                                m "Хмм?"
                                call her_head("Продолжайте шевелить пальцем в моей попке!!","scream","angry",cheeks="blush",tears="messy")
                                ">Ты вытаскиваешь свой палец из тесного ануса девочки..."
                                call her_head("Ч-чтоо?!","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("Почему вы пере-","scream","angry",cheeks="blush",tears="messy")
                                ">...и заменяете его двумя пальцами"
                                call her_head("Ааааах!","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("У-ублюдок!{image=textheart}","scream","worriedCl",cheeks="blush",tears="messy")
                                call her_head("В-вы извращенный ублюдок!{image=textheart}{image=textheart}","grin","dead",cheeks="blush",tears="messy")
                                m "Тебе нравится это, [hermione_name]?"
                                call her_head("Дааа!!!","angry","dead",cheeks="blush",tears="crying")
                                m "Ты любишь это?"
                                call her_head("О, Господи, да!!!","silly","ahegao",tears="messy")
                                m "Скажи мне как тебе это нравится!"

                                call slap_her

                                call her_head("Аааах!!{image=textheart}{image=textheart}{image=textheart}","scream","surprised",cheeks="blush",tears="messy")
                                m "Я задал тебе вопрос."

                                call slap_her

                                call her_head("Когда вы двигаете в моей заднице!","scream","worriedCl",cheeks="blush",tears="messy")
                                call her_head("Я люблю когда вы трахаете мою задницу своими пальцами!","grin","dead",cheeks="blush",tears="messy")
                                m "Что еще ты любишь?"

                                call slap_her

                                call her_head("Когда вы шлепаете мою распутную попку!","scream","worriedCl",cheeks="blush",tears="messy")

                                call slap_her

                                call her_head("С-снова! я ко...","scream","surprised",cheeks="blush",tears="messy")
                                m "Ты снова хочешь кончить?"

                                call slap_her

                                call her_head("Да!","scream","suspicious",cheeks="blush",tears="messy")
                                m "Ты кончаешь от того что я шлепал тебя по заднице?"

                                call slap_her

                                call her_head("Да!!","scream","worriedCl",cheeks="blush",tears="messy")
                                m "Ты кончаешь от того что я трахаю пальцами твой похотливый узенький анус?"

                                call slap_her

                                call her_head("Дааа!!!{image=textheart}","scream","surprised",cheeks="blush",tears="messy")
                                ">Тело Гермионы начинает дико конвульсировать."
                                ">Ты хватаешь Гермиону за волосы свободной рукой чтобы прижать ее к столу, а другой рукой отчаянно двигаешь пальцами в ее большой упругой заднице"
                                call her_head("огосподигосподи","scream","surprised",cheeks="blush",tears="messy")
                                m "От чего ты кончаешь, маленькая шлюха?"
                                call her_head("!!!!","mad","wide",cheeks="blush",tears="messy")
                                m "Что доставляет тебе такое удовольствие?!"
                                call her_head("Моя задница!!!{image=textheart}","open_wide_tongue","ahegao",tears="messy")
                                ">С последним спазмом Гермиона валится на стол без сил, ее тело все еще дергается в конвульсиях, а бедра продолжают двигаться."
                                jump ending_of_screams_of_pleasure

                    "-Нет. Довольно на сегодня.-":
                        pass

            "\"Нет. Просто стой здесь, [hermione_name].\"":
                call her_head("Ах, как скажете, [genie_name]...","soft","base",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], Пожалуйста, поторопитесь...","soft","baseL",cheeks="blush")
                m "Какие-то проблемы, [hermione_name]?"

                if daytime:
                    call her_head("Сейчас начнутся занятия.","annoyed","angryL",cheeks="blush")
                else:
                    call her_head("Я не хочу чтобы кто-то заметил что меня нет на месте.","annoyed","angryL",cheeks="blush")

                m "Но тебе ведь это нравится?"
                call her_head("Я бы не стала так говорить...","annoyed","wink",cheeks="blush")

                call her_head("Мы можем просто начать, пожалуйста...?","angry","worriedCl",cheeks="blush",emote="05")
                m "Раз уж ты так вежливо просишь..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "Что?"
                call her_head("Ничего, [genie_name].","base","ahegao_raised",cheeks="blush")
                m "Ох, это вовсе не звучало как ничего."
                call her_head("...","base","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты двигаешь ладонями вверх и вниз по ножкам Гермионы..."
                hide screen blktone8
                with d3

                call her_head(".........................","base","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">Хорошенько сжать задницу..."
                hide screen blktone8
                with d3

                call her_head(".................","base","glance")
                m "Не отводи взгляд девочка, я хочу чтобы ты смотрела в мои глаза."
                call her_head("Это смущает, [genie_name]...","angry","down_raised")
                m "..."
                call her_head("...Ладно, [genie_name]...","base","ahegao_raised",cheeks="blush")
                m "Ты так молчалива."
                call her_head("....................","base","closed")
                m "Ни слова..."

                show screen blktone8
                with d3
                ">Ты наслаждаешься ощущением от упругой попки..."
                hide screen blktone8
                with d3

                m "Поскольку мои руки трогают..."
                m "Твои бедра..."

                show screen blktone8
                with d3
                ">Твои руки двигаются от попки к внутренней стороне бедер"
                hide screen blktone8
                with d3

                m "Твоя большая, упругая задница..."

                show screen blktone8
                with d3
                ">Ты массируешь ее ягодицы..."
                hide screen blktone8
                with d3

                call her_head(".....................","grin","ahegao")
                m "Твоя талия..."

                show screen blktone8
                with d3
                ">Одна рука остановилась прямо над клитором девочки."
                hide screen blktone8
                with d3

                call her_head(".....................","silly","dead")
                m "Есть ли что-то, чего ты хочешь?"
                call her_head(".....................","annoyed","wink",cheeks="blush")
                call her_head("...Я... {size=-5}... Я хочу чтобы вы потрогали меня пальцем...{/size}","disgust","down_raised",cheeks="blush")
                m "Ты что-то сказала, [hermione_name]?"
                call her_head("...Нет, ничего, [genie_name]...","open","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты массируешь ягодицы девочки одной рукой, в то время как другая рука опускается к промежности, задевая клитор..."
                ">Гермиона смотрит в твои глаза, как ей было велено..."
                hide screen blktone8
                with d3

                m "Не нужно лгать мне."
                call her_head("Я... я сказала, что хочу, чтобы вы потрогами меня пальцами!","shock","worriedCl")

                show screen blktone8
                with d3
                ">Ты быстро погружаешь два пальца в истекающую соками киску."
                hide screen blktone8
                with d3

                call her_head("!!!{image=textheart}{image=textheart}","grin","ahegao")

                show screen blktone8
                with d3
                ">Ты начинаешь двигать пальцами в ней, прежде, чем она успевает сказать, что-то еще."
                hide screen blktone8
                with d3

                call her_head("...................................","disgust","down_raised",cheeks="blush")
                m "Разве я сказал что ты можешь отвести взгляд?"
                call her_head("..................................................","base","ahegao_raised",cheeks="blush",tears="soft")
                m "Хорошая девочка"

                show screen blktone8
                with d3
                ">Ее бедра двигаются в такт движению твоих пальцев"
                hide screen blktone8
                with d3

                m "Тебе нравится?"
                m "Тебе нравится как я трахаю твою киску?"
                call her_head("Я обожаю это!{image=textheart} Я люблю ваши пальцы в моей мокрой похотливой киске!!{image=textheart}","silly","ahegao",tears="crying")
                m "Ну, я думаю мы можем сделать и лучше."

                show screen blktone8
                with d3
                ">Другой рукой ты начинаешь ласкать анус девочки и проникать в него пальцем."
                hide screen blktone8
                with d3

                call her_head("!!!","scream","surprised",cheeks="blush",tears="messy")
                call her_head("Моя киска и моя попка!","grin","dead",cheeks="blush",tears="messy")

                show screen blktone8
                with d3
                ">Тебе даже не приходится двигать их, она сама насаживается на твои пальцы."
                hide screen blktone8
                with d3

                call her_head("Да! трахайте мою киску и попку!{image=textheart}{image=textheart}","silly","dead",tears="messy")
                m "Нет, мы сможем сделать еще лучше."

                show screen blktone8
                with d3
                ">Ты вставляешь еще один палец в ее попку."
                hide screen blktone8
                with d3

                call her_head("Оооялюблюэто","grin","ahegao",tears="messy")
                m "Что ты любишь, [hermione_name]?"
                call her_head("Ах!!{image=textheart} Я люблю ваши похотливые пальцы в моем влагалище и анусе!{image=textheart}","shock","wide",tears="messy")

                show screen blktone8
                with d3
                ">Она стала двигаться еще быстрее."
                hide screen blktone8
                with d3

                m "Ты кончаешь, [hermione_name]?"
                call her_head("Да!!","scream","surprised",cheeks="blush",tears="messy")
                call her_head("Я кончаю!!","scream","worriedCl",cheeks="blush",tears="messy")
                call her_head("Я кончаю от того что вы трахаете меня своими пальцами!!","grin","dead",cheeks="blush",tears="messy")
                m "Смотри на меня!"
                m "Покажи мне свое кончающее лицо!"
                m "Я хочу видеть на что ты готова ради пятнадцати очков."
                call her_head("Аааааах!!!","scream","surprised",cheeks="blush",tears="messy")
                jump ending_of_screams_of_pleasure

    label ending_of_screams_of_pleasure:
    call blkfade

    stop music fadeout 1.0
    ">Ты отпускаешь ее..."
    m "Сейчас."

    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    call her_chibi("stand","mid","base")
    show screen genie

    $ menu_x = 0.5 #Menu is moved to the left side.
    $ menu_y = 0.5 #Menu is moved to the left side.

    call hide_blkfade

    if whoring <= 13:
        $ gryffindor +=15
        m "Пятнадцать очков \"Гриффиндору\"!"
    else:
        m "Хорошая работа, [hermione_name]."

    call her_main("..................","grin","glance",cheeks="blush",tears="mascara",xpos="base",ypos="base")
    her "Спасибо [genie_name]..."

    if daytime:
        her "Если вы не возражаете, я пойду, мои занятия вот-вот начнутся."
    else:
        her "Я должна идти, уже довольно поздно..."

    hide screen bld1
    hide screen hermione_main
    with d3

    if whoring >= 3 and whoring <= 5: #First level. Not happy.

        call her_walk("mid","door",2)

        call her_head("...........................","disgust","down_raised",cheeks="blush")

        pause.5
        call her_chibi("leave","door","base")

    else:

        call her_walk("mid","leave",2)

    if whoring < 6: #Adds points till 6.
        $ whoring +=1

    $ hg_pf_ButtMolester_OBJ.points += 1

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
