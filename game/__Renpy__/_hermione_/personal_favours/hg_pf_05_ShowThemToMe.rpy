

### HERMIONE PERSONAL FAVOUR 5 ###

### LOOK AT HER TITS! ###

label hg_pf_ShowThemToMe: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_ShowThemToMe_OBJ.points == 0:
        m "{size=-4}(Я хочу посмотреть на твои сиськи.){/size}"
    else:
        m "{size=-4}(Я хочу посмотреть на твои сиськи еще раз.){/size}"

    if hg_pf_ShowThemToMe_OBJ.points < 1:
        menu:
            "\"(Да, давай сделаем это!)\"":
                pass
            "\"(Нет не сейчас.)\"":
                jump silver_requests

    if whoring < 6:
        jump too_much

    if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased or hg_powerGirl_OBJ.purchased:
        m "\"(Должен ли я попросить ее переодеться?)\""
        menu:
            "\"(Да, давай.)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, я хочу, чтобы ты переоделась.."
                if whoring < 15:
                    jump too_much
                call her_main("Во что?","open","worriedL")
                menu:
                    "-В Cheerleaderшу-" if hg_gryffCheer_OBJ.purchased:
                        her "Ладно, пойду переоденусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_gryffCheer_OBJ)
                        pass
                    "-В Слизеринскую Cheerleaderшу-" if hg_slythCheer_OBJ.purchased:
                        her "Ладно, пойду переоденусь."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_slythCheer_OBJ)
                        pass
                    "-В *Power girl*-" if hg_powerGirl_OBJ.purchased:
                        call her_main("В этот нелепый костюм?","scream","angryCl")
                        m "Все не так уж и плохо. У него есть хороший плащ."
                        call her_main("...","angry","worriedCl",emote="05")
                        call her_main("Ладно, пойду переоденусь.","normal","worriedCl")
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_powerGirl_OBJ)
                        pass
                call her_main("","","",xpos="mid")
                call ctc
                m "Очень хорошо."
            "\"(Не сейчас.)\"":
                pass

    hide screen hermione_main
    with d3

    $ current_payout = 25 #Used when haggling about price of th favor.

    #First time event
    if hg_pf_ShowThemToMe_OBJ.points == 0 and whoring <= 11:
        m "[hermione_name]?"
        call her_main("Да, [genie_name]...","normal","base",xpos="mid",ypos="base")
        m "Сколько хочешь очков за то, чтоб я увидел твои сиськи?"
        stop music fadeout 1.0
        call her_main("Сколько вы дадите...?","open","base")
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        call her_main("[genie_name]!","scream","angryCl")
        m "Хм... Я думал твоему факультету не помешают лишние баллы..."
        m "Я думаю, что ошибся..."
        call her_main(".........?","open","base")
        m "Пожалуйста, не обращай на меня внимания..."
        m "Все, что я хочу сделать, это помочь тебе..."
        call her_main(".............","annoyed","worriedL")
        call her_main("200 очков, [genie_name].","normal","worriedCl")
        m "Так, если я дам тебе 200 очков, [hermione_name]..."
        m "Ты оголишь свои сиськи для меня?"
        call her_main("[genie_name]! Не надо быть таким вульгарным!","angry","angry")
        her "Думаю, мне лучше уйти...."

        menu:
            "\"Подожди. 200 очков твои. Покажи мне!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                call her_main("Правда?","open","base")
                m "Ну?"
                call her_main("......................................","annoyed","worriedL")
                her "Вы должны пообещать мне, что трогать не будете, [genie_name]."
                m "Конечно, конечно..."
                call her_main("Я делаю это только ради победы моего факультета, [genie_name]!","scream","worriedCl")

            "\"Я дам тебе 5 очков, чтоб посмотреть на твои сиськи.\"":
                call her_main("Пять?!","scream","wide_stare")
                call her_main("[genie_name], я не собираюсь выставлять себя за жалкие пять очков!","angry","angry",emote="01")
                m "Хорошо, твои сиськи точно не стоят 200, [hermione_name]!"
                call her_main("(Они не стоят?)","annoyed","down")
                call her_main("Ну, может быть 100?","annoyed","angryL")

                menu:
                    "\"Прекрасно. 100 очков! Оголи их уже.":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "Так тому и быть... За сто очков..."
                    "\"25 очков, это мое последнее предложение!\"":
                        $ current_payout = 25 #Used when haggling about price of th favor.
                        her "..............."
                        her "Хорошо, пусть будет так..."

            "\"Ладно, уходи, неважно...\"":
                $mad = +12
                her "Tsk!"
                call music_block
                jump could_not_flirt


        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d5

        call h_action("lift_top")

        call play_music("playful_tension") # SEX THEME.

        call her_chibi("lift_top","mid","base")
        call ctc

        call bld
        m "Хм..."
        call her_head("{size=-5}(Моя грудь полностью обнажена...){/size}","disgust","down_raised",cheeks="blush")
        m "Подойди поближе [hermione_name], дай рассмотреть получше..."
        call her_head("............","annoyed","angryL",cheeks="blush")

        call her_chibi("stand","mid","base")
        pause.2

        call her_walk_desk_blkfade

        ">Гермиона медленно подходит к твоему столу."
        ">С каждым шагом ее сиськи немного подпрыгивают..."

        hide screen genie
        show screen genie_and_tits_01
        call hide_blkfade
        call ctc

        call bld
        call her_head("............","soft","baseL",cheeks="blush")
        m "Очень хорошо..."
        call her_head(".....","annoyed","angryL",cheeks="blush")

        hide screen bld1
        show screen blktone
        call her_main("","annoyed","annoyed",trans="fade",xpos="mid",ypos="base")
        call ctc
        her "...................................."

    #Second event
    else:
        hide screen hermione_main
        with d3

        if whoring >= 6 and whoring <= 8:
            m "[hermione_name]?"
            call her_head("Да, [genie_name]?","annoyed","angryL")
            m "Я хочу посмотреть на твои сиськи."
            call her_head("............","annoyed","angryL",cheeks="blush")
            call her_head("Вы обещаете не трогать, [genie_name]?","annoyed","angryL",cheeks="blush")
            m "Конечно."
            hide screen bld1
            hide screen blktone
            hide screen hermione_main
            with d3
            pause.2

            call her_chibi("lift_top","mid","base")
            call ctc

            call bld
            m "Хм..."
            m "Подойди поближе [hermione_name], дай рассмотреть их вблизи..."

            hide screen bld1
            call her_chibi("stand","mid","base")
            pause.2

            call her_walk_desk_blkfade

            ">Гермиона медленно подходит к твоему столу."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            call hide_blkfade
            call ctc

            call bld
            m "Очень хорошо..."
            call play_music("playful_tension") # SEX THEME.
            call h_action("lift_top")

            hide screen bld1
            show screen blktone
            call her_main("","annoyed","annoyed",xpos="mid",trans="fade")
            call ctc

            her "...................................."

        elif whoring >= 9:
            m "Я хочу посмотреть на твои сиськи, [hermione_name]."
            if whoring >= 17:
                call her_head("Конечно [genie_name]","base","ahegao_raised",cheeks="blush")
            else:
                call her_head("Вы будете только смотреть, [genie_name]?","angry","worriedCl",cheeks="blush")
                m "Конечно..."
            hide screen hermione_main
            call hide_blktone
            pause.2

            call her_chibi("lift_top","mid","base")
            call ctc

            call bld
            m "Хм..."
            m "Подойди поближе [hermione_name], дай рассмотреть получше..."

            hide screen bld1
            call her_chibi("stand","mid","base")
            pause.2

            call her_walk_desk_blkfade

            ">Гермиона медленно подходит к твоему столу."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            hide screen bld1
            call hide_blkfade
            call ctc

            call bld
            m "Очень хорошо..."

            call h_action("lift_top")
            hide screen bld1
            show screen blktone
            call her_main("","base","closed",xpos="mid",trans="fade")
            call ctc

            her "...................................."
            call play_music("playful_tension") # SEX THEME.

    menu:
        "\"Нарушить свое обещание. Схватить за сиськи!\"":

            #First Time Event.

            #Event Fails
            if whoring >= 6 and whoring <= 8:
                hide screen hermione_main
                call blkfade

                ">Ты протягиваешь руку и вцепляешься пальцами в грудь..."
                call her_head("[genie_name], что вы делаете?","mad","wide",cheeks="blush",xpos="base",ypos="high")

                #Start Groping
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                call hide_blkfade
                call ctc

                call bld
                m "Расслабься, [hermione_name]. Стой спокойно!"
                m "Ох... Какая красивая у тебя грудь..."
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("Нет, [genie_name], пожалуйста! Вы не должны этого делать...","shock","worriedCl")
                m "Это не займет много времени, постой спокойно."
                call her_head("[genie_name], я не соглашалась на это!","angry","angry",cheeks="blush")
                with hpunch
                call her_head("Вы должны отпустить меня!!!","scream","angry",cheeks="blush",emote="01")

                call blkfade
                ">Гермиона отошла от тебя, поспешно прикрываясь."
                call h_action("none")
                call her_head("Думаю, мне лучше уйти....","angry","worriedCl",cheeks="blush",xpos="base",ypos="base")

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call bld
                m "Уходи, [hermione_name], тогда я тебе не заплачу за это..."
                call her_head("Но я показала вам свои...","angry","worriedCl",cheeks="blush")
                call her_head("И вы трогали...","angry","angry",cheeks="blush")
                call her_head("И я ничего не получу?","scream","angry",cheeks="blush",emote="01")
                m "Уходи, [hermione_name]..."
                call her_head("Грр..................","angry","worriedCl",cheeks="blush")
                call her_head("{size=-5}(Гори в аду, бесчестный старик---{/size}","angry","worriedCl",cheeks="blush")
                $ mad += 22
                call music_block
                jump could_not_flirt

            #Event Succeeds
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade

                ">Ты протягиваешь руку и вцепляешься пальцами в грудь..."
                call her_head("[genie_name], что вы делаете?","mad","wide",cheeks="blush",xpos="base",ypos="high")

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade
                show screen groping_naked_tits
                with fade
                call ctc

                call bld
                m "Расслабься, [hermione_name]. Стой спокойно!"
                call her_head("Я не соглашалась на это, [genie_name]...","annoyed","angryL",cheeks="blush")
                call her_head("Я не думаю, что вы должны...","annoyed","angryL",cheeks="blush")
                m "Тебе не нравится...?"
                call her_head("Что?","disgust","down_raised",cheeks="blush")
                m "Разве тебе не нравится, как я сжимаю и тяну твои сиськи?"
                call her_head("...............","disgust","down_raised",cheeks="blush")
                m "Признайся, тебе это немного нравится..."
                call her_head("{size=-5}(Так странно видеть мою грудь в чужих руках...){/size}","disgust","down_raised",cheeks="blush")
                call her_head("[genie_name], я позволяю вам это делать со мной, чтобы помочь моему факультету, не более того!","shock","worriedCl")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("Пожалуйста, отпустите меня!","annoyed","angryL",cheeks="blush")
                show screen blkfade
                with d5
                ">Гермиона внезапно отталкивается от тебя и накрывается."
                call h_action("none")
                call her_head("Вы обещали не трогать, [genie_name]...","annoyed","angryL",cheeks="blush",xpos="base",ypos="base")
                m "Трудно было устоять..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call bld
                call her_head(".............","soft","baseL",cheeks="blush")
                call her_head("Могу ли я тогда, получить заработанные очки, пожалуйста?","angry","worriedCl",cheeks="blush",emote="05")
                m "Конечно..."
                $ mad += 9

            #Event Also Succeeds
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade

                ">Ты протягиваешь руку и вцепляешься пальцами в грудь..."
                call her_head("[genie_name], что вы делаете?","mad","wide",cheeks="blush",xpos="base",ypos="high")

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade
                show screen groping_naked_tits
                with fade
                call ctc

                call bld
                m "Расслабься, [hermione_name]. Стой спокойно!"
                call her_head("Но...","disgust","down_raised",cheeks="blush")
                call her_head("ах...{image=textheart}","shock","worriedCl")
                call her_head("Я не соглашалась на это....","disgust","down_raised",cheeks="blush")
                m "Но тебе это нравится, не так ли?"

                if whoring >= 17:
                    call her_head("Мне нравится [genie_name]!{image=textheart}","open","baseL",cheeks="blush")
                else:
                    call her_head("Я так не думаю, [genie_name]!{image=textheart}","shock","worriedCl")

                call blktone
                ">Ты сжимаешь ее сиськи..."
                call hide_blktone

                if whoring >= 17:
                    call her_head("[genie_name], вы обещали не трогать...","base","baseL",cheeks="blush")
                    m "Знаю, знаю... но трудно было устоять..."
                    call her_head(".................","base","ahegao_raised",cheeks="blush")
                else:
                    call her_head("[genie_name], вы обещали меня не лапать...","angry","worriedCl",cheeks="blush")
                    m "Знаю, знаю... но трудно было устоять..."
                    call her_head(".................","angry","angry",cheeks="blush")

                call her_head("....................ах...{image=textheart}","base","ahegao_raised",cheeks="blush")
                call her_head("[genie_name], вы должны остановиться...","base","ahegao_raised",cheeks="blush")
                m "Еще немного..."

                show screen blktone8
                with d3
                ">Ты продолжаешь массировать грудь девушки..."
                hide screen blktone8
                with d3

                call her_head("[genie_name]... пожалуйста, остановитесь...","open","ahegao_raised",cheeks="blush")
                m "Почему? Потому что тебе это нравится?"
                call her_head("Нет, это не так...","base","baseL",cheeks="blush")
                call her_head("Я имею ввиду...","open","baseL",cheeks="blush")

                show screen blktone8
                with d3
                ">Ты тянешь сиськи в противоположных направлениях, а затем ударяешь их друг об друга..."
                hide screen blktone8
                with d3

                call her_head("Ах...{image=textheart} [genie_name], мне правда надо идти...","base","ahegao_raised",cheeks="blush")
                if daytime:
                    call her_head("Скоро... занятия вот-вот начнутся...","open","baseL",cheeks="blush")
                else:
                    call her_head("Уже поздно...","open","baseL",cheeks="blush")

                m "Ну, хорошо..."
                call blkfade

                ">Ты отпустил грудь девушки..."
                ">Гермиона прикрывается..."

                call h_action("none")
                call play_music("chipper_doodle") # HERMIONE'S THEME.

                if whoring >= 17:
                    call her_head("Пожалуйста, не подумайте, что я забыла, что вы нарушили свое обещание, [genie_name].","base","baseL",cheeks="blush",xpos="base",ypos="base")
                else:
                    call her_head("Пожалуйста, не подумайте, что я забыла, что вы нарушили свое обещание, [genie_name].","annoyed","angryL",cheeks="blush",xpos="base",ypos="base")

                m "Правда..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call bld

                if whoring >= 17:
                    call her_head("Спасибо [genie_name].","open","baseL",cheeks="blush")
                else:
                    call her_head("Могу я получить очки?","base","ahegao_raised",cheeks="blush")
                    $ mad +=7


        "\"Сдержать обещание. Просто смотреть.\"":
            ">Ты долго смотришь на сиськи Гермионы..."

            #First time event.
            if whoring >= 6 and whoring <= 8:
                call ctc

                menu:
                    "-Кивнуть головой-":
                        ">Ты смотришь на сиськи девушки, а потом киваешь..."
                        her "......................"
                    "-Покачать головой-":
                        $ mad += 3
                        ">Ты долго смотришь на сиськи девушки, а потом покачал головой..."
                        her ".....................?"

            #Second time event.
            elif whoring >= 9 and whoring <= 11:
                call ctc

                menu:
                    "\"У тебя хорошие сиськи.\"":
                        call her_main("","annoyed","closed")
                        pause
                        her "Спасибо--"
                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                        call her_main("...........","annoyed","base")
                        call her_main("Вы неуместны, [genie_name].","annoyed","annoyed")
                    "\"Хм. Я видел лучше.\"":
                        $ mad += 7
                        her "Tsk..."
                        her "Мы закончили?"

            #Third time event.
            elif whoring >= 12:
                call ctc

                menu:
                    "\"У тебя большие сиськи, [hermione_name].\"":
                        call her_main("Вы правда так думаете [genie_name]?","annoyed","base")
                        call her_main("Я рада, что они вам понравились, [genie_name]...","base","closed")
                    "\"Я думаю, твои сиськи в порядке...\"":
                        call her_main("А?","annoyed","base")
                        her "Это означает то, что вам не нравится, [genie_name]?"
                        call her_main("Простите меня...","disgust","down_raised")

            call blktone
            ">Ты продолжаешь смотреть на ее грудь..."
            call hide_blktone
            call ctc

            m "Ладно, можешь прикрыться, [hermione_name]..."
            her "............."
            pause.2

            call set_hermione_action("none")
            pause.5

            call blkfade

            ">Гермиона прикрывается..."

            #End Admiring
            hide screen hermione_main
            hide screen chair_left
            hide screen genie_and_tits_01
            hide screen blktone
            hide screen bld1

        "\"Начать дрочить.\"":

            #First Time Event.
            if whoring >= 6 and whoring <= 8:
                $ mad += 2
                hide screen hermione_main
                with d3
                ">Ты хватаешь свой член и начинаешь дрочить..."
                call blkfade

                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("[genie_name]?!!","angry","wide")
                m "Стой спокойно, [hermione_name]..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade
                call ctc

                call bld
                call nar(">Ты голодным взглядом смотришь на грудь Гермионы...")
                call her_head("[genie_name], что вы...?","shock","worriedCl")
                call nar(">Ты продолжаешь дрочить...")
                call her_head("[genie_name], нет...","disgust","down_raised",cheeks="blush")
                call her_head("Вы должны... убрать его...","disgust","down_raised",cheeks="blush")
                m "Хватит ныть [hermione_name]. Я ведь не трогаю тебя, не так ли?"
                call her_head("Но...","angry","worriedCl",cheeks="blush")
                call her_head("Но я не соглашалась на это!","angry","angry",cheeks="blush")
                call her_head("Я...","angry","worriedCl",cheeks="blush")
                call her_head("Думаю, мне лучше уйти!","angry","worriedCl",cheeks="blush")

                menu:
                    "\"Уйдешь сейчас и не получишь очков!\"":

                        call her_head("{size=+5}Что{/size}? Вы издеваетесь, [genie_name]?","scream","wide",cheeks="blush")
                        call her_head("Я показала вам свои...","scream","wide",cheeks="blush")
                        call her_head("..........","annoyed","angryL",cheeks="blush")
                        call her_head("Я больше не собираюсь продавать вам ни одной услуги, [genie_name]!","angry","angry",cheeks="blush")
                        call blkfade

                        ">Гермиона отстраняется от тебя и прикрывается..."
                        g4 "Не смей оставлять меня в таком состоянии, [hermione_name]!"

                        call h_action("none")
                        call her_head("Я больше никогда не войду в ваш кабинет, [genie_name]!","angry","suspicious",cheeks="blush",xpos="base",ypos="base")

                        g4 "Подожди. Просто скажи еще чего-нибудь грязного! Я почти!"
                        call her_head("Вы ужасный человек, [genie_name]...","angry","suspicious",cheeks="blush",tears="messy")

                        $ mad += 30

                        call music_block
                        jump could_not_flirt

                    "\"Хорошо, хорошо. На сегодня достаточно.\"":
                        $ mad +=9
                        pass

                    "-Начать дрочить еще быстрее-":
                        $ mad += 35

                        ">Ты начинаешь яростно дрочить свой член!"
                        call her_head("Нет, [genie_name], остановитесь!","scream","angry",cheeks="blush",emote="01")
                        ">Ты дрочишь еще быстрее!"
                        call her_head("[genie_name], думаю, я сейчас уйду....","annoyed","angryL",cheeks="blush")
                        g4 "Нет, подожди, я почти!"
                        call blkfade

                        call her_head("Фууу! [genie_name]!","angry","suspicious",cheeks="blush")
                        call her_head("Я ухожу!","angry","suspicious",cheeks="blush")
                        call h_action("none")

                        call music_block
                        jump could_not_flirt

            #Second Event.
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade

                ">Ты берешь свой член и начинаешь дрочить..."

                call her_head("[genie_name]?","angry","wide")
                ">Ты голодным взглядом смотришь на грудь Гермионы..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade
                call ctc

                call bld
                call her_head("[genie_name], я не соглашалась на это....","shock","worriedCl")
                m "На что ты жалуешься, [hermione_name]?"
                m "Я же не трогаю тебя..."
                call her_head("Да, но вы... трогаете себя, [genie_name].","shock","worriedCl")
                call nar(">Ты набираешь темп...")
                m "Просто стой, [hermione_name]."
                m "Скоро все закончится."
                call her_head("..................","shock","worriedCl")
                call her_head("(Он такой большой...)","disgust","down_raised",cheeks="blush")
                m "Да... Да, мне нравятся они..."
                m "Да, твои голые сиськи..."
                call her_head("..............","disgust","down_raised",cheeks="blush")
                call her_head("Ну, пусть будет так...","open","baseL",cheeks="blush")
                call her_head("Можете продолжать трогать себя, [genie_name]...","open","baseL",cheeks="blush")
                call her_head("Но пообещайте мне, что не будете...","soft","baseL",cheeks="blush")
                call her_head("Не надо... Эмм...","open","baseL",cheeks="blush")
                call her_head("Не разрядитесь...","annoyed","angryL",cheeks="blush")
                call her_head("Не в мою сторону, [genie_name]...","angry","angry")
                m "Ладно, посмотрим..."
                m "Ох, ты маленькая шлюшка. Ты противная маленькая шлюха!"
                call her_head(".......................","angry","worriedCl",cheeks="blush")
                call nar(">Ты начинаешь дрочить еще сильнее...")
                g4 "Да, я знаю, ты хочешь этого! Да!"
                call her_head("................","angry","worriedCl",cheeks="blush")
                call blkfade

                ">Ты собираешься кончить..."

                menu:
                    "-Остановиться-":
                        g4 "Ох, хорошо..."
                        g4 "Я лучше остановлюсь сейчас..."
                        call her_head("...............","angry","worriedCl",cheeks="blush")
                        ">Гермиона прикрывается..."
                        call h_action("none")
                    "-Кончить-":
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        g4 "Ах! Ты шлюха!"
                        call her_head("Профф-- ??","scream","wide",cheeks="blush")
                        call cum_block
                        g4 "Ах! Да!"
                        hide screen bld1
                        with d1
                        $ no_blinking = True #When True - blinking animation is not displayed.
                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade
                        with d3
                        call ctc

                        call bld
                        $ sperm_on_tits = True
                        call her_head("[genie_name], нет, вы же обещали!","scream","angry",cheeks="blush",emote="01")
                        g4 "О, это замечательно, да...."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3
                        call her_head("[genie_name], как вы могли...?","angry","suspicious",cheeks="blush")
                        m "Ох, это было прекрасно..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised")
                        call ctc
                        her "Но моя форма..."
                        her "Все испорчено..."
                        m "Не волнуйся, я дам твоему факультету очки, [hermione_name]."
                        m "Ты молодец."
                        her "................"
                        her "Мне нужно привести себя в порядок..."

                        hide screen hermione_main
                        call blkfade

                        call h_action("none")
                        $ sperm_on_tits = False

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        show screen genie

                        call hide_blkfade
                        call her_main("","angry","angry")
                        call ctc
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        her "Как вы могли поступить так со мной, [genie_name]?!"
                        her "Вы же мне обещали!"
                        hide screen hermione_main
                        with d3
                        $ mad += 45


            #Event three.
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade

                ">Ты берешь свой член и начинаешь дрочить..."
                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush")
                ">Ты голодным взгдядом смотришь на грудь Гермионы..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade
                call ctc

                call bld
                if whoring >= 17:
                    call her_head("Ах...","base","ahegao_raised",cheeks="blush")
                    call her_head("Он такой большой...","open","baseL",cheeks="blush")
                    call her_head("Вы просто не могли сдержаться, не так ли [genie_name]?","base","baseL",cheeks="blush")
                    call her_head("..................","base","ahegao_raised",cheeks="blush")
                    m "Да... Да, они нравятся мне..."
                    m "Да, твои сиськи..."
                    call her_head("..............","base","ahegao_raised",cheeks="blush")
                    call her_head("ну, пусть будет так...","open","baseL",cheeks="blush")
                    call her_head("Но пообещайте мне, что не будете...","soft","baseL",cheeks="blush")
                    call her_head("Не... хм...","open","baseL",cheeks="blush")
                    call her_head("Не кончайте на меня, [genie_name]...","base","ahegao_raised",cheeks="blush")
                    m "Ладно, возможно..."
                    m "Ох, ты маленькая шлюшка. Ты противная маленькая шлюха!"
                    call her_head(".......................","base","ahegao_raised",cheeks="blush")
                    call nar(">Ты начинаешь дрочить еще быстрее...")
                    g4 "Да, я знаю, что ты хочешь этого! Да!"
                    call her_head("................","base","ahegao_raised",cheeks="blush")
                    # SAME AS PREVIOUS EVENT^^^

                else:
                    call her_head("[genie_name], на самом деле я не соглашалась на это...","shock","worriedCl")
                    m "На что ты жалуешься, [hermione_name]?"
                    m "Я же не трогаю тебя..."
                    call her_head("Да, но вы... трогаете себя, [genie_name].","shock","worriedCl")
                    #">You pick up the pace..."
                    m "Стой спокойно, [hermione_name]."
                    m "Скоро все закончится."
                    call her_head("..................","shock","worriedCl")
                    m "Да... да, мне нравятся они..."
                    m "Да, твои сиськи..."
                    call her_head("..............","disgust","down_raised",cheeks="blush")
                    call her_head("Что ж, пусть будет так...","open","baseL",cheeks="blush")
                    call her_head("Но пообещайте мне, что не будете...","soft","baseL",cheeks="blush")
                    call her_head("Не... эм...","open","baseL",cheeks="blush")
                    call her_head("Не разрядитесь...","annoyed","angryL",cheeks="blush")
                    call her_head("Не в мою сторону, [genie_name]...","annoyed","angryL",cheeks="blush")
                    m "Ладно, возможно..."
                    m "Ох, ты маленькая шлюшка. Ты противная маленькая шлюха!"
                    call her_head(".......................","disgust","down_raised",cheeks="blush")
                    call nar(">Ты начинаешь дрочить еще быстрее...")
                    g4 "Да, я знаю, что ты хочешь этого! Да!"
                    call her_head("................","disgust","down_raised",cheeks="blush")
                    # SAME AS PREVIOUS EVENT^^^


                call blkfade

                menu:
                    g4 "Ах! (Я собираюсь кончить!)"
                    "-Сдержаться-":
                        g4 "Ох, хорошо..."
                        g4 "Я лучше остановлюсь..."
                        call her_head("...............","disgust","down_raised",cheeks="blush")
                        call her_head("Хм... Я читала, что это плохо, [genie_name]...","disgust","down_raised",cheeks="blush")
                        m "А?"
                        call her_head("Это плохо для вашего здоровья, не разряжаться...","shock","worriedCl")
                        call her_head("Эм...","disgust","down_raised",cheeks="blush")
                        call her_head("Если вы хотите вы можете--","base","baseL",cheeks="blush")
                        g4 "Ах! Ты шлюха!"
                        call her_head("???","mad","wide",cheeks="blush")

                        call cum_block

                        g4 "Ах! ДА!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade
                        call ctc

                        call bld
                        call her_head("[genie_name], я не имела ввиду, что вы можете спустить свою... сперму на меня, [genie_name]...","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Ох, это было великолепно..."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3

                        call her_head("Ну, что сделано, то сделано...","base","baseL",cheeks="blush")
                        m "Ох, это было потрясающе..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base")
                        call ctc

                        her "Но моя форма испорчена..."
                        m "Не волнуйся, я дам твоему факультету очки, [hermione_name]."
                        m "Ты молодец!"
                        call her_main("Спасибо [genie_name].","base","closed")
                        call her_main("А теперь мне нужно привести себя в порядок...","annoyed","closed")
                        call ctc

                        hide screen hermione_main
                        call blkfade

                        $ sperm_on_tits = False
                        $ aftersperm = True
                        call h_action("none")

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        show screen genie
                        call hide_blkfade

                        call her_main("","base","base")
                        call ctc
                        her "Ну, пока этого достаточно...."
                        hide screen hermione_main

                    "-Кончить-":
                        g4 "Ах! Ты шлюха!"
                        call her_head("???","mad","wide",cheeks="blush")

                        call cum_block

                        g4 "Ах! ДА!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        call hide_blkfade
                        call ctc

                        call bld
                        call her_head("ах...{image=textheart} здесь так жарко...{image=textheart}","shock","worriedCl")
                        call her_head("[genie_name], вы же обещали...","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Ох, это замечательно, да...."

                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3
                        call her_head("Ну... что сделано, то сделано...","angry","worriedCl",cheeks="blush")
                        m "О, это было потрясающе..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base")
                        call ctc

                        her "Но моя форма испорчена..."
                        m "Не волнуйся, я уверен, что никто не заметит."
                        m "Ты молодец."
                        call her_main("Спасибо [genie_name].","base","closed")
                        call her_main("А теперь мне нужно привести себя в порядок...","annoyed","closed")
                        call ctc

                        hide screen hermione_main
                        call blkfade

                        $ sperm_on_tits = False
                        call h_action("none") #This reloads all her clothing!

                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        call hide_blkfade

                        call her_main("","base","base")
                        call ctc

                        her "Ну, пока этого достаточно..."
                        hide screen hermione_main


    call blkfade

    $ sperm_on_tits = False
    call h_action("none") #This reloads all her clothing!

    hide screen jerking_off_01
    hide screen chair_left
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    hide screen groping_01
    hide screen groping_02

    call her_chibi("stand","desk","base")
    show screen genie
    call hide_blkfade
    pause.5

    call bld
    if whoring <= 16:
        $ gryffindor +=current_payout
        m " \"Гриффиндор\" получает [current_payout] очков!"

    stop music fadeout 10.0

    if whoring <= 16:
        call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    else:
        call her_main("..................","base","happyCl",xpos="base",ypos="base")

    her "Спасибо, [genie_name]..."

    if daytime:
        her "Теперь, если вы не возражаете, мне лучше уйти. Мои занятия вот-вот начнутся."
    else:
        her "Мне лучше уйти. Уже довольно поздно..."

    if whoring >= 6 and whoring <= 8:
        $ new_request_08_heart = 1
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 9 and whoring <= 11:
        $ new_request_08_heart = 2
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 12:
        $ new_request_08_heart = 3
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 3 #Event hearts level (0-3)


    hide screen bld1
    hide screen hermione_main
    with d3

    #Door reaction.
    if whoring >= 6:

        call her_walk("desk","door",3)

        if whoring >= 6 and whoring <= 8:
            call her_head("(Как унизительно... Кем я стала...?)","disgust","down_raised",cheeks="blush")

        elif whoring >= 9 and whoring <= 11:
            call her_head("........................","disgust","down_raised",cheeks="blush")

        elif whoring >= 12:
            call her_head("{size=-5}(Это было так унизительно...){/size}","base","ahegao_raised",cheeks="blush")
            call her_head("{size=-5}(Нет, Гермиона, ты глупая девчонка!){/size}","angry","angry",cheeks="blush")
            call her_head("{size=-5}(Мы делаем это, для победы нашего факультета!){/size}","angry","angry",cheeks="blush")
            call her_head(".................................","base","ahegao_raised",cheeks="blush")

        elif whoring >= 17 and aftersperm:
            call her_head("{size=-5}(Это было так волнующе...){/size}","base","ahegao_raised",cheeks="blush")
            call her_head("{size=-5}(Интересно, кто-нибудь заметит что на моей форме!){/size}","open","ahegao_raised",cheeks="blush")
            call her_head("{size=-5}(Что обо мне подумают люди?){/size}","open","ahegao_raised",cheeks="blush")
            call her_head(".................................","base","ahegao_raised",cheeks="blush")

        pause.5
        call her_chibi("leave","door","base")

    else:
        call her_walk("desk","leave",3)

    $ aftersperm = False #Shows cum stains on Hermione's uniform.

    if whoring < 9: #Adds points till 9.
        $ whoring +=1

    $ hg_pf_ShowThemToMe_OBJ.points += 1

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
