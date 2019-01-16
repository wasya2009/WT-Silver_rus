

label hg_pf_LetsHaveSex: #LV.7 (Whoring = 18 - 20)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Должен ли я попросить ее заняться сексом со мной?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    if hg_laraCroft_OBJ.purchased and hg_pf_SuckIt_OBJ.points >= 1:
        m "\"(Попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, пойди и переоденься."
                call her_main("Во что?","open","worriedL")
                m "Я хочу, что бы ты переоделась в Лару Крофт"
                if whoring >= 22:
                    call her_main("Кого?","open","base")
                    m "Она персонаж из одной видео игры."
                    call her_main("...","annoyed","down")
                    call her_main("Хорошо, пойду переоденусь.","annoyed","base")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_laraCroft_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Не сейчас.)\"":
                pass

    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_ani"

    call bld

    if whoring < 18:
        m "[hermione_name]..."
        m "Почему бы тебе не подойти ко мне, я не много порву твою киску..."
        g9 "Своим членом!"
        jump too_much

    #First Event.
    if hg_pf_LetsHaveSex_OBJ.points == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base")
        m "Я хочу купить у тебя услугу.."
        call her_main(".......?","base","base")
        m "Как бы сказать это правильно...?"
        call her_main("Это секс, [genie_name]?","base","suspicious")
        m "Ну, да. Как ты...?"

        call her_main("Это не сложно было понять...","base","glance")
        m "Ты не против?"
        call her_main("Конечно я против, [genie_name]!","upset","closed")
        her "Я не проститутка!"
        m "Но ты все равно это сделаешь?"
        call her_main("\"Гриффиндор\" опять отстает...","open","closed")
        her "У меня есть выбор...?"
        m "Вот и отлично!"

        label your_ass:
        hide screen hermione_main
        call blkfade

        stop music fadeout 1.0
        call gen_chibi("hide")
        call her_chibi("hide")

        call her_head(".............","upset","closed")
        call her_head("!!!!!!!!!!!!!!!","angry","wide")
        m "Расслабься, [hermione_name]. Я пока просто снял твои трусы."
        call her_head("..............","angry","angry")
        m "Ты готова?"
        call her_head("Нет...","annoyed","annoyed")
        m "Хорошая девочка."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ах....{image=textheart}","scream","wide")

        call gen_chibi("hide")
        call her_chibi("hide")
        hide screen genie
        show screen chair_left
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","normal","worriedCl")
            show screen ccg

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc


        call play_music("playful_tension") # SEX THEME.

        #FUCKING
        g4 "Твоя киска... Такая тугая."
        call her_head("................","normal","worriedCl")
        m "Ты в порядке?"
        call her_head("А-ах... Он такой большой...","angry","base",tears="soft")
        call her_head("Вы разорвете меня на части, [genie_name]!")
        m "Глупость! Мой член обычного размера."
        m "Я не виноват, что ты такая узенькая..."
        call her_head("......................","normal","worriedCl")

        menu:
            "\"Тебе должно быть стыдно!\"":
                #$ ccg2 = 20
                call her_head("Мне не стыдно, [genie_name]!","normal","worriedCl")
                call her_head("Я делаю это ради своего факультета!")
                call her_head("Помочь моим--")
                call her_head("Ах-ах-а...","open","worriedCl")
                call her_head("Мои одноклассники зависят от меня... ах-а...")
                m "Ты уверена, что это единственная причина?"
                call her_head("Я не знаю--","normal","worriedCl")
                call her_head("Ах-а...","open","worriedCl")
                call her_head("Я не понимаю, что вы имеете в виду, [genie_name].","angry","down_raised")
                m "Мне кажется, тебе это очень нравится..."
                #$ ccg2 = 21
                call her_head("Нет, [genie_name]!","angry","down_raised")
                m "Серьезно?"
                call her_head("......................","normal","worriedCl")
                m "Тогда почему твоя киска такая влажная?"
                call her_head("....................А-ха.{image=textheart}","open","worriedCl")
                m "Признайся, тебе нравится трахаться со мной [genie_name]!"
                #$ ccg2 = 25
                call her_head("Нет!","normal","worriedCl")
                m "Упрямая девочка..."
                call her_head("Ах-а...{image=textheart}","open","worriedCl")
            "\"Так... Что нового в твоей жизни?\"":
                #$ ccg2 = 14
                call her_head("...[genie_name]?","open","base")
                m "Я просто пытаюсь вести вежливый разговор."
                #$ ccg2 = 17
                call her_head("Ах-ах... Но...","open","base")
                m "Какие-нибудь новости от родителей?"
                call her_head("От родителей?","angry","worriedCl",emote="05")
                call her_head("[genie_name], пожалуйста, я не могу говорить...","open","worriedCl")
                m "Почему нет? Наслаждаешься?"
                call her_head("Нет... ах...{image=textheart}","open","worriedCl")
                m "Я думаю, да."
                call her_head("Я делаю это только ради очков, [genie_name]...","open","worriedCl")
                m "Ох, понятно..."
                m "Значит, ты как проститутка."
                call her_head("Что?","angry","base")
                m "Я плачу тебе за секс со мной. Как бы ты это назвала?"
                call her_head("...........","angry","down_raised")
                #$ ccg2 = 19
                call her_head("Я не проститутка...","open","worriedCl")
                call her_head("Почему вы так грубы со мной, [genie_name]?","angry","base",tears="soft")
                m "Я думал, что тебе это нравится."
                call her_head("Нет!","mad","worried",tears="soft")
                m "Серьезно? Тогда, почему твоя киска влажная?"
                call her_head("Не из-за этого!","angry","down_raised")
                m "Ну если ты так говоришь..."
                #$ ccg2 = 20
                call her_head("А-ах...{image=textheart}","open","worriedCl")
                call her_head("Я... ах...{image=textheart} не проститутка...","shock","worriedCl")
            "\"......................................................\"":
                #$ ccg2 = 14
                call her_head("А-хa... aх...","open","worriedCl")
                m "*Тяжелый вздох!*"
                call her_head("Aх... хa-aхa...","open","worriedCl")
                m "Ох..."
                call her_head("Aх-aх...","open","worriedCl")
                m "......................"
                call her_head("Aх... aх...","open","worriedCl")
                call her_head("Aх... [genie_name]?","open","base")
                m "Что такое?"
                #$ ccg2 = 17
                call her_head("Aх... Вам... Нравится?","open","worriedCl")
                m "Нравится ли мне сверлить твою супер-узенькую киску?"
                m "Очень, [hermione_name]. А что?"
                call her_head(".....................","normal","worriedCl")
                call her_head("Aх... Вы просто притихли...","open","worriedCl")
                m "Просто наслаждаюсь моментом, [hermione_name]."
                m "А что насчет тебя? Ты в порядке?"
                call her_head("Aх... да...","open","worriedCl")
                call her_head("Правда, немного больно, aх...","open","base")
                call her_head("Ваш член такой большой... aх...","open","worriedCl")
                m "Хм..."
                m "Мне остановиться?"
                #$ ccg2 = 20
                call her_head("Нет, [genie_name]... Вам не надо...","open","base")
                call her_head("Пожалуйста, не обращайте на меня внимания... Наслаждайтесь моментом.","normal","worriedCl")
                call her_head("Я попробую... Ах... Привыкнуть в конце концов... Ах...")
                m "Ну, как скажешь, [hermione_name]."
                #$ ccg2 = 21
                call her_head("Aх-a...{image=textheart}","open","worriedCl")
                m "Да, так хорошо!"

        call her_head("Aх-aх...{image=textheart}","open","worriedCl")

        if daytime:
            m "Пойдешь после на занятия?"
        else:
            m "Пойдешь после спать?"
        #$ ccg2 = 22

        call her_head("Да, aх...{image=textheart}","open","worriedCl")
        call her_head("Если я смогу ходить...")
        g4 "Ght! {image=textheart} Да, ты всегда говоришь правильные вещи, [hermione_name]!"
        call her_head("Aх...{image=textheart} aх...{image=textheart}{image=textheart}","shock","worriedCl")
        with hpunch
        #$ ccg2 = 24
        call her_head("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}","scream","wide")
        m "А? Ты в порядке?"
        call nar(">У Гермионы дрожат ноги...")
        m "[hermione_name]?"
        #$ ccg2 = 28
        call her_head("{image=textheart}{image=textheart}{image=textheart}Я думаю, что я кончила, [genie_name]!{image=textheart}{image=textheart}{image=textheart}","scream","wide")
        g9 "Tch... Ты мерзкая шлюха!"
        #$ ccg2 = 29
        call her_head("AAХ! Я не могу сдерживаться!","silly","dead")
        g4 "Ты должна быть наказана за то, что такая шлюха!"
        call nar(">Ты схватил Гермиону за задницу и начал трахать ее очень быстро!")
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        #$ ccg2 = 30
        call her_head("НЕТ! ОСТАНОВИТЕСЬ! ПОЖАЛУЙСТА!","scream","wide")
        g4 "Кто тебе разрешил кончать, шлюха? Это и есть твое наказание!"
        call her_head("[genie_name], нет, aх-a!{image=textheart}","open","worriedCl")
        #$ ccg2 = 31
        call her_head("Aх-a...{image=textheart}Я сойду с ума!{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
        g4 "{size=+7}Ах!{/size}"
        hide screen bld1
        with d3
        call ctc

        #$ ccg2 = 32
        call her_head("Нет...{image=textheart} aх...{image=textheart}","silly","ahegao")
        #$ ccg2 = 33
        call her_head("Я думаю, что сейчас...{image=textheart} потеряю сознание...{image=textheart}")
        g4 "АХ! ТЫ ШЛЮХА!"

        menu:
            "-Кончить на гермиону-":
                with hpunch
                g4 "{size=+7}Ах!!!{/size}"
                call cum_block
                g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_out_ani")
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"
                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 42
                call her_head("Aх...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                hide screen bld1
                call ctc

                call set_u_ani("sex_cum_out_blink_ani")
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Это было очень классно..."
                #$ ccg2 = 28
                call her_head("*Тяжелые вздохи*","open_wide_tongue","ahegao")
                m "Ты в порядке?"
                call her_head("Aх... да...","silly","dead")
                #$ ccg2 = 29
                call her_head("Мои ноги дрожат...")
                hide screen bld1
                with d3
                call ctc
                call blkfade

                hide screen ccg
                $ face_on_cg = False
                call h_update_hair

                if daytime:
                    call her_head("Но я думаю, что дойду до класса...","silly","dead",xpos="base",ypos="base")
                else:
                    call her_head("Но я думаю, что дойду до кровати...","silly","dead",xpos="base",ypos="base")

                m "Хорошо."
                m "Тебе понравилось [genie_name]?"
                call her_head("[genie_name], я сделала это ради своего факультета.","grin","ahegao")
                m "Серьезно? До сих пор для факультета?"
                call her_head("Могу я получить... очки?","open","worriedCl")

            "-Кончить в Гермиону-":
                with hpunch
                g4 "{size=+7}Aх!!!{/size}"
                call cum_block
                g4 "{size=+15}AХ!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_in_ani")
                $ g_c_u_pic = "sex_cum_in_ani"
                $ ccg3 = "s1"
                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 41
                call her_head("Aх...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                hide screen bld1
                with d3
                call ctc
                $ g_c_u_pic = "images/animation/23_cum_19.png"
                #$ ccg2 = 40
                call her_head("Вы кончили в меня...","silly","dead")
                g9 "Я знаю."
                hide screen bld1
                with d3
                call ctc
                call blkfade

                hide screen ccg
                $ face_on_cg = False
                call h_update_hair

                call her_head("Но...","silly","dead",xpos="base",ypos="base")
                m "Что?"
                call her_head("Что делать, если я забеременею?","shock","worriedCl")
                m "Нет, все будет хорошо...."
                call her_head("Откуда вы знаете, [genie_name]?","shock","worriedCl")
                m "Мы ведьмаки-бесплодны."
                call her_head("Ведьмаки?","open","worriedCl")
                m "Конечно... Ты ведьма, я ведьмак, все верно?"
                m "А все знают, что ведьмаки бесплодны..."
                call her_head("[genie_name], но в этом же нет смысла...","angry","base")
                call her_head("Ладно, могу я получить свои очки...?")

    #Second time event.
    elif hg_pf_LetsHaveSex_OBJ.points == 1:
        m "[hermione_name], ты постоянно влажная при встрече со мной?"
        call her_main("[genie_name]!","scream","angryCl")
        m "Просто скажи \"Да\" и иди ко мне, [hermione_name]."
        call her_main("...........","open","base")
        call her_main("Да....","angry","down_raised")
        hide screen hermione_main
        jump your_ass

    #Third time event.
    elif hg_pf_LetsHaveSex_OBJ.points >= 2:
        m "[hermione_name]..."
        m "Прошлой ночью мне приснился сон..."
        g9 "Ты лежала на моем столе, и я трахал твою киску, как сумасшедший..."
        if whoring >= 24:
            call her_main("Во сне, [genie_name]...","soft","ahegao",xpos="right",ypos="base")
        else:
            call her_main("Во сне, [genie_name]...","upset","closed",xpos="right",ypos="base")
        if whoring <= 23:
            call her_main("А вконце этого сна, я получила 65 очков?","angry","angry")
            g9 "Да, получила, [hermione_name]."
        else:
            call her_main("Вы кончили в меня?","smile","baseL")
            g9 "Я не уверен [hermione_name], хочешь узнать?"
        call her_main("...............................","disgust","glance")
        her "Давайте я просто сниму трусики..."
        stop music fadeout 1.0
        hide screen hermione_main
        call blkfade

        # SEX
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ааааххх....{image=textheart}","scream","wide")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie

        call gen_chibi("hide")
        call her_chibi("hide")
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","worriedCl")
            show screen ccg

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        call play_music("playful_tension") # SEX THEME.


        call her_head("Aх...{image=textheart}","open","worriedCl")
        m "Твоя киска стала какой-то просторной..."
        #$ ccg2 = 4
        call her_head("Имеет ли это значение...{image=textheart} aх...?{image=textheart}","open","worriedCl")
        #$ ccg2 = 5
        call her_head("Это все из-за вас [genie_name]...{image=textheart}","shock","worriedCl")
        #$ ccg2 = 6
        call her_head("Вы разрываете мою маленькую узенькую киску своим громадным пенисом...{image=textheart}","silly","ahegao")
        g4 "Ах, ты шлюха!"
        #$ ccg2 = 10
        call her_head("Aх...{image=textheart}{image=textheart}","silly","ahegao")
        m "Да! Тебе нравится, когда я трахаю тебя?"
        call her_head("Да, [genie_name]...","base","glance")
        menu:
            g4 "..."
            "\"Быть милым, но страстным.\"":
                m "Да, тебе это нравится?"
                #$ ccg2 = 14
                call her_head("Да, [genie_name]... aх...{image=textheart}","open","closed")
                m "Хорошая девочка!"
                m "Просто расслабляйся!"
                call her_head("Да... aх...{image=textheart}","open","closed")
                m "Весь процесс..."
                call her_head("Aх...{image=textheart}{image=textheart}","open","worriedCl")
                m "Да, моя маленькая принцесса..."
                #$ ccg2 = 15
                call her_head("Что?","angry","wide")
                call her_head("Нет, пожалуйста, не называйте меня так... aх...{image=textheart}","angry","down_raised")
                call her_head("Мой папа называл меня своей маленькой принцессой, когда я была маленькой...")
                m "Ну, верно, а сейчас я твой папа!"
                #$ ccg2 = 16
                call her_head("Aх...{image=textheart} ах-aх...{image=textheart}{image=textheart}","soft","ahegao")
                m "И ты моя маленькая принцесса-шлюха!"
                #$ ccg2 = 17
                call her_head("Aх...{image=textheart} aх...{image=textheart}{image=textheart}{image=textheart}","grin","dead")
            "\"Быть грубым!\"":
                m "Да шлюха!"
                m "Я уверен, что ты наслаждаешься каждым подобным моментом!"
                call nar(">Ты набираешь темп.")
                #$ ccg2 = 17
                call her_head("Aх...{image=textheart} [genie_name]...","open","worriedCl")
                m "Ты развратная шлюха!"
                call her_head("Aх...{image=textheart} aх-a...{image=textheart}","shock","worriedCl")
                m "Ты позорище, [hermione_name]!"
                #$ ccg2 = 18
                call her_head("Aх-aх...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
                m "Твои родители отправили тебя сюда учиться, а не трахаться с учителями, ты, конченная пизда!"
                #$ ccg2 = 19
                call her_head("Aх-a...{image=textheart} Но я только это и делаю--","shock","worriedCl")
                m "Всем плевать, зачем ты это делаешь, хуесоска!"
                m "Посмотри, кем ты стала!"
                m "Прыгаешь с голым задом на члене своего профессора!"
                #$ ccg2 = 20
                call her_head("Aх...{image=textheart} Нет...{image=textheart} хватит говорить...{image=textheart} aх...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
                call nar(">Ты набираете темп еще быстрее.","start")
                $ g_c_u_pic = "sex2_ani"
                call nar(">Комната наполняется ритмичным звуком шлепков...","end")
                m "Ты позволила приставать к тебе... Ты сосешь мой член..."
                m "Кто ты после этого?!"
                #$ ccg2 = 21
                call her_head("................","grin","dead")
                call her_head("Aх...{image=textheart} aх....{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
                call her_head(".......................","angry","down_raised")
                call her_head("{size=-5}Я шлюха...{/size}")
                m "Да! Это именно то, что я хотел услышать!"

        #$ ccg2 = 22
        call her_head("Aх... aх... aх...","angry","down_raised")
        call her_head("[genie_name], думаю, вы могли бы... aх...")
        m "Что?"
        call her_head("Не могли бы вы отшлепать меня... aх...?","silly","worried",cheeks="blush",tears="soft")
        g4 "С превиликим удовольствием!"

        call slap_her

        #$ ccg2 = 24
        call her_head("Aa-a-aх!{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
        m "Тебе понравилось, да?"

        call slap_her

        #$ ccg2 = 28
        call her_head("Aх..!{image=textheart} Да!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        m "И еще раз!"

        call slap_her

        #$ ccg2 = 29
        call her_head("Aхх! Да!","silly","worried",cheeks="blush",tears="soft")
        call nar(">Ты заметил, что каждый раз, когда ты шлепаешь девочку по попке, ее киска крепко сжимает твой член на секунду...","start")
        ">Тебе очень нравятся эти ощущения..."
        ">Ты делаешь серию шлепков по заднице Гермионы."
        call nar(">Каждый из них приходил с вздохом возбуждения от девочки.","end")
        #$ ccg2 = 30

        call slap_her
        call slap_her
        call slap_her
        call slap_her
        call slap_her

        #$ ccg2 = 31
        call her_head("Aaх!!!{image=textheart}{image=textheart}{image=textheart} БОЛЬНО!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        #$ ccg2 = 32
        call her_head("БОЛЬНО...{image=textheart}{image=textheart}{image=textheart} БОЛЬНО...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
        m "Хм?"
        m "Почему твои ноги дрожат, [hermione_name]?"
        m "Ты кончила?"
        #$ ccg2 = 33
        call her_head("Да...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
        m "Что ж, думаю, тогда и я последую твоему примеру."
        call her_head("..............","silly","dead")
        call nar(">Ты начинаешь трахать Гермиону с большей скоростью!")
        #$ ccg2 = 34
        call her_head("Aх! Нет! Я не могу так...{image=textheart} Я...{image=textheart} aх...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
        m "Заткнись, шлюха!"
        g4 "Ах!"

        menu:
            "-Кончить в нее-":
                with hpunch
                g4 "{size=+7}Ах, Держи!!!{/size}"
                call cum_block
                g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
                $ ccg3 = "s1"
                $ g_c_u_pic = "sex_cum_in_ani"
                call cum_block
                call ctc
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 33
                call her_head("!!!","silly","dead")
                #$ ccg2 = 38
                call her_head("AХ! ВЫ НАПОЛНЯЕТЕ МЕНЯ!{image=textheart}{image=textheart}{image=textheart}")
                g4 "Я еще не закончил, сука!"
                g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
                call cum_block
                call her_head("AХ! МОЙ ЖИВОТ!","shock","baseL",cheeks="blush",tears="soft")
                g4 "{size=+5}ШЛЮХА!{/size}"

                hide screen bld1
                with d3
                call ctc



                $ g_c_u_pic = "images/animation/23_cum_19.png"

                #$ ccg2 = 40
                m "Ну, это было здорово..."
                call her_head("Aх...{image=textheart}","silly","dead")
                m "С тобой все в порядке, шлюха? Эм, я имею в виду, [hermione_name]."
                call her_head("Да... Я...","silly","dead")
                #$ ccg2 = 41
                call her_head("Я чувствую себя такой сытой...","open_wide_tongue","ahegao")
                call her_head("!!!","scream","wide")
                call her_head("Вы же кончили в меня, [genie_name]!")
                m "Я знаю."
                call her_head("Вы не должны были...","open","worriedCl")
                m "Разве тебе не понравилось?"
                call her_head("....Может быть.","grin","dead")
                #$ ccg2 = 42
                call her_head("Я думаю, что успела кончить несколько раз...","soft","ahegao")
                call blkfade

                $ face_on_cg = False
                call h_update_hair

                call her_head("Может вы правы, [genie_name], и мне не стоит об этом так беспокоиться.","angry","wink",xpos="base",ypos="base")
                if whoring <= 23:
                    call her_head("Могу ли я получить очки?")

            "-Кончить на нее-":
                with hpunch
                g4 "{size=+7}Ах!!!{/size}"
                call cum_block
                g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 30
                call her_head("Aх...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "{size=+5}Ты шлюха! Держи!{/size}"
                call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft")
                hide screen bld1
                with d3
                call ctc


                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Это было довольно здорово..."
                #$ ccg2 = 31
                call her_head("Aх...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
                m "Ты в порядке, шлюха?"
                call her_head("Да... Я...","silly","dead")
                m "Разве тебе не понравилось?"
                #$ ccg2 = 29
                call her_head("....Я думаю...","grin","dead")
                call ctc
                call blkfade

                $ face_on_cg = False
                call h_update_hair

                call her_head("Я думаю, что несколько раз кончила, [genie_name]...","soft","ahegao",xpos="base",ypos="base")
                if whoring <= 23:
                    call her_head("Могу я получить очки?","angry","wink")
                $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    #Fourth time event.
    elif hg_pf_LetsHaveSex_OBJ.points >= 3:
        m "[hermione_name]..."
        m "У меня к тебе просьба...."
        call her_main("Заняться сексом? {size=-2}Пожалуйста, пусть это будет секс...{/size}","smile","baseL")
        m "Ты, кажется, готова."
        call her_main(".......","base","glance")
        call her_main("Ну, я, возможно, воплощу некоторые планы...","base","down")
        her "Но я не могу сказать вам..."
        m "Пока ты нагибаешься у моего стола, мне все равно...."
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down")
        stop music fadeout 1.0
        hide screen hermione_main
        call blkfade
        # SEX

        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ааааххх....{image=textheart}","scream","wide") #HERMIONE
        hide screen genie

        $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u

        call her_chibi("hide")
        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        call play_music("playful_tension") # SEX THEME.
        show screen bld1
        with d3

        call her_head("Aх...{image=textheart}","open","worriedCl")
        m "У тебя мокрая киска..."
        call her_head("Это, из-за...{image=textheart} aх...{image=textheart}","open","worriedCl")
        call her_head("Это все из-за вас [genie_name]...{image=textheart}","shock","worriedCl")

        if daytime:
            call her_head("Я... с нетерпением ждала этого, все утро...{image=textheart}","silly","ahegao")
        else:
            call her_head("Я... с нетерпением ждала этого, весь день...{image=textheart}","silly","ahegao")

        g4 "Ах, шлюха!"
        call her_head("Aх...{image=textheart}{image=textheart}","silly","ahegao")
        m "Да! Тебе нравится, когда я трахаю тебя?"
        call her_head("Да, [genie_name]...","base","glance")

        call play_sound("knocking")
        call nar(">Ты слышишь стук в дверь.")

        menu:
            "\"Кто там?\"":
                m "(Кто будет стучать в такое время?)"
                lun "Это Полумна Лавгуд, сэр."
                m "{size=-3}Кто это, [hermione_name]?{/size}"
                call her_head("Сумасшедшая блондинка... aх...{image=textheart}... с красивой грудью...","open","closed")
                m "Войди!"
            "-Сказать, чтоб ушла-":
                m "Прогнать-!"
                call her_head("Нет [genie_name]... пусть она...","open","worriedCl")
                m "Ты хочешь этого?!"
                call her_head("Aх...{image=textheart} да...{image=textheart}","shock","worriedCl")
                m "Ты такая маленькая шлюха, [hermione_name]!"
                call her_head("Aх-aх...{image=textheart} пусть она зайдет... пожалуйста...","shock","worriedCl")
                m "Ты это сама попросила!"
                call her_head("Aх-a...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
                m "Войди!"

        ">Дверь открывается и входит Полумна Лавгуд."
        call play_sound("door") #Sound of a door opening.
        call luna_init
        $ luna_chibi("stand", 540, 250)
        $ changeLuna(1, 1, 4, 1)
        lun "Здравствуйте профессор!"
        #Stop sex
        m "....."
        call her_head("......","shock","worriedCl")

        lun "Я хотела поговорить с вами о школьной форме."
        m "Форме?"
        lun "Да, у меня есть некоторые идеи, которые нуждаются в изменениях, и я хотела бы, чтобы вы меня выслушали."
        m "{size=-3}Что здесь происходит, [hermione_name]?{/size}"

        call her_head("Возможно, я дала ей сыворотку внушаемости...","silly","ahegao")
        m "{size=-3}Сыворотку внушаемости?{/size}"
        lun "С кем вы разговариваете, сэр?"
        m "Ох, эм.... ни с кем, просто игнорируй меня..."
        lun "Хорошо, тогда я проигнорирую вас..."
        call her_head("Возможно, я предложила ей прийти сюда...","silly","ahegao")
        call her_head("И она не сможет увидеть меня...","silly","ahegao")
        lun "Как я уже говорила, сэр, школьная форма просто не может оставаться такой, какая она есть."

        show screen blktone
        with d3
        ">Ты набираешь темп."
        $ g_c_u_pic = "sex2_ani"
        ">Комната наполняется ритмичным звуком шлепков..."
        call her_head("Aх... aх... aх...","angry","down_raised")
        m "{size=-3}Просто, я все правильно понимаю?{/size}"
        m "{size=-3}Ты накачала свою одноклассницу...{/size}"
        m "{size=-3}Чтобы она приходила сюда и смотрела, как ты занимаешься сексом с директором.{/size}"
        call her_head("Aх... да...{image=textheart}{image=textheart}{image=textheart}")
        lun "Форма девочек слишком скромная!"
        m "Скромная?"
        lun "Действительно! Мисс Грейнджер-единственный ученик, который правильно одевается."
        call her_head("Ах...","silly","worried",cheeks="blush",tears="soft")
        m "{size=-3}Что еще ты с ней сделала?{/size}"
        call her_head("Я, возможно, сказала ей... aх...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        call her_head("Действовать как самая развратная шлюха, которую она себе представит...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        m "{size=-3}Примерно как ты?{/size}"
        call her_head("Даа...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        lun "Сэр, пожалуйста, обратите внимание..."
        m "Извините, мисс Лавгуд."
        lun "Спасибо. Как я уже говорила, я думаю, что вам нужно принять несколько новых политик в отношении школьной формы для девочек."
        lun "Каждый должен стремиться достичь того же уровня совершенства, что и мисс Грейнджер."
        call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        lun "Я придумала несколько правил, которые помогут в этом, и я хотела бы, чтобы вы их применили."
        m "Давай посмотрим..."
        lun "правило номер один: рубашки должны раскрывать как минимум 3 дюйма декольте."
        call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        lun "Правило номер два: никакой юбки длиной более 5 дюймов."
        call her_head("{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        lun "Правило номер три: никаких бюстгальтеров в любое время."
        call her_head("{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        lun "И, наконец, правило номер четыре: никаких трусиков в любое время."
        call her_head("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")

        m "Почему твои ноги дрожат, [hermione_name]?"
        m "Ты кончила? От того, что на тебя смотрела твоя одноклассница?"
        call her_head("Да...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
        m "Ну, я последую твоему примеру."
        call her_head("..............","silly","dead")
        call nar(">Ты начинаешь трахать Гермиону более решительно!")
        call her_head("Aх! Нет! Я не могу...{image=textheart} не перед...{image=textheart} aх...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
        m "Заткнись шлюха!"
        lun "Да, сэр."
        g4 "Ах!"
        with hpunch
        g4 "{size=+7}Ах!!!{/size}"
        call cum_block
        g4 "{size=+15}АХ!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_out_ani"
        call cum_block
        call ctc

        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_08.png"
        call her_head("Aх...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
        g4 "{size=+5}Ты шлюха! Держи!{/size}"
        call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft")
        hide screen bld1
        with d3
        call ctc


        $ g_c_u_pic = "sex_cum_out_blink_ani"
        m "Это было здорово..."
        call her_head("Aх...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        m "Ты в порядке, шлюха?"
        call her_head("Да... Я...","silly","dead")
        m "Разве тебе не понравилось?"
        call her_head("....Я думаю...","grin","dead")
        call ctc

        call blkfade
        call her_head("Я думаю, что кончила несколько раз, [genie_name]...","soft","ahegao")
        m "Вы двое-лучшие в классе."
        call her_head("Да, сэр...","grin","dead")
        call her_head("Давай Полумна пойдем.","grin","dead")
        lun "Гермиона! Как ты здесь оказалась?"
        lun "И в чем это ты?"
        call her_head("Это не имеет значения...","soft","ahegao")
        call her_head("{size=-7}Ты сможешь слизать это позже...{/size}","soft","ahegao")

    $ face_on_cg = False
    call h_update_hair

    hide screen ccg
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    if not daytime:
        show screen candlefire

    call her_chibi("stand","desk","base")
    call gen_chibi("hide")
    show screen genie
    pause.1
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    pause.5

    call bld
    stop music fadeout 4.0
    if whoring < 24:
        m "Да, [hermione_name]. 65 очков \"Гриффиндору\"."
        $ gryffindor +=65
    call her_main("Спасибо, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if whoring < 21: #Adds points till 21.
        $ whoring +=1

    if hg_pf_LetsHaveSex_OBJ.points == 0:
        $ new_request_29_heart = 1
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points == 1:
        $ new_request_29_heart = 2
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points >= 2:
        $ new_request_29_heart = 3
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 3 #Event hearts level (0-3)

    $ hg_pf_LetsHaveSex_OBJ.points += 1

    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
