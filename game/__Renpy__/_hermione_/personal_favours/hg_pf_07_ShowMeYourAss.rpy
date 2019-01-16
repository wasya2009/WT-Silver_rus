

label hg_pf_ShowMeYourAss: #LV.3 (Whoring = 9 - 11)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_ShowMeYourAss_OBJ.points == 0:
        m "{size=-4}(Я хочу посмотреть на твою попу.){/size}"
    else:
        m "{size=-4}(Я хочу посмотреть на твою попу еще раз.){/size}"

    if hg_pf_ShowMeYourAss_OBJ.points < 1:
        menu:
            "\"(Да, сделаем это!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    $ current_payout = 50 #Used when haggling about price of th favor.

    if hg_pf_ShowMeYourAss_OBJ.points == 0 and whoring < 15: # LEVEL 04 # FIRST TIME.

        call bld
        m "[hermione_name]?"
        call her_main("Да, [genie_name]...","normal","base")
        m "Сколько будет стоить, чтобы ты разделась и показала свою попу?"
        stop music fadeout 1.0
        if whoring < 9:
            call her_main("Раздеться и показать вам свою...?","angry","shocked")
            jump too_much
        else:
            $ current_payout = 50 #Used when haggling about price of the favor.
            call her_main("Раздеться и показать вам свою...?","open","base")

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("[genie_name]!","scream","angryCl")
        m "Давай без таких бурных эмоций..."
        m "Не то, чтобы я не видел всего этого раньше.."
        call her_main("......","open","base")
        call her_main(".............","annoyed","worriedL")
        call her_main("50 очков, [genie_name].","normal","worriedCl")
        m "Так, а если я дам тебе 50 очков, [hermione_name]..."
        m "Ты разденешься и покажешь мне свою попу?"
        call her_main("[genie_name]! Нет причин, быть таким вульгарным!","angry","angry")
        her "Я подумала, и... Я хочу 70 очков..."

        menu:
            "\"Ладно. 70 очков твои, показывай!\"":
                $ current_payout = 70 #Used when haggling about price of th favor.
                call her_main("Правда?","open","base")
                m "Ну?"
                call her_main("...","annoyed","worriedL")
                her "Вы должны пообещать мне, что не будете трогать, [genie_name]..."
                m "Конечно, конечно..."
                call her_main("И не должны прикасаться к себе!","scream","worriedCl")

            "\"Я дам тебе 50 очков, чтобы увидеть твою попу.\"":
                call her_main("Пятьдесят?","annoyed","frown")
                call her_main("Ну хорошо, тогда...","annoyed","angryL")
                call her_main("Но если вы захотите прикоснуться ко мне, то это будет стоить дополнительных очков...","annoyed","down")
                call her_main("...по крайней мере сто очков","annoyed","angryL")

                menu:
                    "\"Ладно. 100 очков, раздевайся!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        call her_main("(Я не думала, что он согласится на это...)","annoyed","worriedL")
                        call her_main("Н-ну, ладно...","normal","worriedCl")
                    "\"Тогда 50 очков\"":
                        her "Ну, пусть будет так."
                        call her_main("но лучше держите свои руки при себе...","annoyed","angryL")

            "\"Ладно, уходи. Мне все равно...\"":
                $ mad = +12
                her "Пф!"
                call music_block
                jump could_not_flirt


        m "Хорошо, хорошо..."
        g9 "Просто разденься уже!"

        hide screen bld1
        show screen blktone
        call her_main("...","annoyed","annoyed",xpos="mid",ypos="base")

        #Remove Top Animation
        call set_hermione_action("lift_top")
        pause.5
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")
        pause.2

        call her_main("{size=-5}(Не могу поверить, что собираюсь раздеться для него...){/size}","disgust","down_raised",cheeks="blush")
        m "Вот так, [hermione_name], теперь твоя юбка..."
        call her_main("............","annoyed","angryL",cheeks="blush")

        #Remove Skirt Animation
        call set_hermione_action("lift_skirt")
        pause.5
        call h_action("naked") #Removes all clothing.
        call set_hermione_action("none","skip_update")
        pause.2
        call ctc

        call her_main("............","soft","baseL",cheeks="blush")
        m "Очень хорошо..."
        call her_main(".....","annoyed","angryL",cheeks="blush")
        m "Теперь повернись..."
        call blkfade

        call her_main("","annoyed","annoyed")
        call ctc
        her "...................................."
        call her_chibi("stand","mid","base",flip=True)

        hide screen hermione_main
        with d3
        show screen hermione_ass
        with d3
        call ctc

        call hide_blkfade


    #Second and Third Event
    else: #Whoring 12+ or whoring (9+ and .points > 1)

        show screen bld1
        call her_main(xpos="right",ypos="base")
        pause.5

        if whoring < 12:
            m "[hermione_name]?"
            call her_main("Да, [genie_name]?","annoyed","angryL")
        m "Я хочу посмотреть на твою попу, [hermione_name]."

        if whoring < 12:
            call her_main("............","annoyed","angryL",cheeks="blush")
            call her_main("Обещайте, что вы не будете трогать, [genie_name]?","annoyed","angryL",cheeks="blush")
            m "Конечно."
        elif whoring < 15:
            call her_main("Вы только будете смотреть, [genie_name]?","angry","worriedCl",cheeks="blush")
            m "Конечно..."
        else:
            call her_main("Все для вас [genie_name]","base","ahegao_raised",cheeks="blush")
        call ctc


        #Remove Top Animation
        call set_hermione_action("lift_top")
        pause.5
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")
        pause.2


        m "Хм..."
        m "Вот и все [hermione_name], теперь юбка..."


        #Remove Skirt Animation
        call set_hermione_action("lift_skirt")
        pause.5
        call h_action("naked") #Removes all clothing.
        call set_hermione_action("none","skip_update")
        pause.2
        call ctc


        m "Очень хорошо..."

        if whoring < 15:
            call her_main(".....","annoyed","angryL",cheeks="blush")
        else:
            call her_main("............","soft","baseL",cheeks="blush")

        m "Теперь повернись..."
        call blkfade

        call her_main("","","")
        pause.5

        call her_chibi("stand","mid","base",flip=True)
        hide screen hermione_main
        with d3
        show screen hermione_ass
        with d3
        call ctc

        show screen blktone
        call hide_blkfade

        if whoring < 15:
            call her_head("....................................","annoyed","annoyed")
        else:
            call her_head("....................................","base","closed")
            call play_music("playful_tension") # SEX THEME.
        call ctc


    menu:
        "\"Схватить за задницу!\"":

            hide screen hermione_ass
            call blkfade

            ">Ты подходишь к Гермионе, протягиваешь руку, и своими большими пальцами хватаешь ее за задницу..."
            call her_head("[genie_name], что вы делаете?","mad","wide",cheeks="blush")

            hide screen genie
            hide screen desk
            show screen chair_left
            show screen desk
            call gen_chibi("groping","mid","base")
            hide screen blktone
            call hide_blkfade
            call ctc

            m "Расслабься, [hermione_name]. Стой спокойно!"

            show screen blktone
            show screen hermione_ass
            with fade
            call ctc

            #FIRST EVENT. HERMIONE OUTRAGED.
            if whoring < 12 and current_payout < 100:

                m "Ох... У тебя хорошая задница..."
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("Нет, [genie_name], пожалуйста! Вы не должны этого делать...","shock","worriedCl")
                m "Это не займет много времени, просто стой и смотри вперед."
                call her_head("[genie_name], я не соглашалась на это!","angry","angry",cheeks="blush")
                with hpunch
                call her_head("Вы должны отпустить меня!!!","scream","angry",cheeks="blush",emote="01")
                call blkfade

                ">Гермиона отстраняется от тебя и прикрывается."

                call h_action("none")

                call her_head("Думаю, мне лучше уйти...","angry","worriedCl",cheeks="blush")
                hide screen chair_left #Genie's chair.
                hide screen desk
                call gen_chibi("hide")
                call her_chibi("stand","mid","base")
                show screen genie
                hide screen hermione_ass
                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call bld
                m "Уходи, [hermione_name]. Ты заработала свои очки.'"
                call her_main("Пффф...","angry","worriedCl",cheeks="blush",xpos="right",ypos="base")
                call her_main("Вы бы смогли по больше рассмотреть, если бы могли просто держать руки при себе...","angry","angry",cheeks="blush")
                m "Это все [hermione_name]..."
                call her_main("......","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(Я думаю, позволить ему схватить меня, все-таки не так уж и плохо...{/size}","angry","worriedCl",cheeks="blush")

                $ mad += 7

            #SECOND EVENT. A BIT ANGRY.
            elif whoring < 15:

                if current_payout < 100:
                    $ mad += 3
                    call her_head("Я не соглашалась на это, [genie_name]...","annoyed","angryL",cheeks="blush")
                else:
                    call her_head("Я знаю, что согласилась на это [genie_name]...","annoyed","angryL",cheeks="blush")
                    call her_head("Но как директор этой школы...","annoyed","angryL",cheeks="blush")
                call her_head("Я не знаю, если вы должны...","annoyed","angryL",cheeks="blush")
                m "Тебе нравится...?"
                call her_head("Что?","disgust","down_raised",cheeks="blush")
                m "Тебе нравится как я сжимаю твою задницу?"
                call her_head("...............","disgust","down_raised",cheeks="blush")
                m "Признайся, тебе немного это нравится..."
                m "Может быть чуть-чуть..."
                call her_head("{size=-5}(Так странно позволять ему лапать меня...){/size}","disgust","down_raised",cheeks="blush")
                call her_head("[genie_name], я позволяю вам делать это со мной, чтобы помочь моему факультету!","shock","worriedCl")
                call her_head("Не имеет значения, насколько это приятно...","shock","worriedCl")
                m "Так ты признаешься, что тебе нравится."
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("Пожалуйста, отпустите меня!","annoyed","angryL",cheeks="blush")
                call blkfade

                ">Гермиона внезапно отстраняется от тебя и прикрывается."

                call h_action("none")

                if current_payout < 100:
                    call her_head("Вы обещали не трогать меня, [genie_name]...","annoyed","angryL",cheeks="blush")
                    m "Трудно было устоять..."
                else:
                    call her_head("Несмотря на то, что я позволила вам схватить меня, [genie_name]...","annoyed","angryL",cheeks="blush")
                    call her_head("Вам не нужно быть таким грубым...","annoyed","angryL",cheeks="blush")
                    m "Прости, было трудно устоять..."
                    call her_head("..........","base","closed")

                hide screen chair_left #Genie's chair.
                hide screen desk
                call gen_chibi("hide")
                call her_chibi("stand","mid","base")
                show screen genie
                hide screen hermione_ass
                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                show screen bld1
                if current_payout < 100:
                    call her_main("Ну... если вы хотели прикоснуться, вы должны заплатить мне больше.","soft","baseL",cheeks="blush",xpos="right",ypos="base")
                    call her_main("Кстати, могу я получить очки?","angry","worriedCl",cheeks="blush",emote="05")
                else:
                    call her_main("Я бы хотела получить сейчас очки [genie_name].","angry","worriedCl",cheeks="blush",emote="05",xpos="right",ypos="base")
                m "Конечно..."

            #THIRD EVENT. ENJOYS A LITTLE.
            elif whoring >= 15:

                call her_head("Но...","disgust","down_raised",cheeks="blush")
                call her_head("Ах...{image=textheart}","shock","worriedCl")

                if current_payout < 100:
                    call her_head("Я не соглашалась на это...","disgust","down_raised",cheeks="blush")
                else:
                    call her_head("Пожалуйста [genie_name], не так грубо...{image=textheart}","shock","worriedCl")

                m "Но тебе это нравится, не так ли?"

                if whoring >= 18:
                    call her_head("Мне нравится [genie_name]!{image=textheart}","open","baseL",cheeks="blush")
                else:
                    call her_head("Может быть... [genie_name]{image=textheart}","shock","worriedCl")

                call nar(">Ты пару раз сжимаешь ее задницу...")

                if whoring >= 18 or current_payout == 100:
                    if current_payout < 100:
                        call her_head("[genie_name], вы обещали не трогать...","base","baseL",cheeks="blush")
                        m "Я знаю, знаю... но признайся, ты хотела, чтобы я..."
                        call her_head(".................{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised",cheeks="blush")
                    else:
                        call her_head("[genie_name], пожалуйста...{image=textheart}","base","baseL",cheeks="blush")
                else:
                    call her_head("[genie_name], вы обещали не трогать...","angry","worriedCl",cheeks="blush")
                    m "Я знаю, знаю... но признайся, ты хотела, чтобы я..."
                    call her_head("Ах{image=textheart}... конечно нет [genie_name]{image=textheart}","angry","angry",cheeks="blush")

                call her_head("Мммм.......................{image=textheart}","base","ahegao_raised",cheeks="blush")
                call her_head("[genie_name], вы должны остановиться...","base","ahegao_raised",cheeks="blush")
                m "Еще немного..."

                call nar(">Ты продолжаешь щупать ее задницу...")

                call her_head("[genie_name]... пожалуйста, остановитесь...","open","ahegao_raised",cheeks="blush")
                m "Почему? Потому что тебе это нравится?"
                call her_head("Нет, это не так....","base","baseL",cheeks="blush")
                call her_head("Я имею в виду...","open","baseL",cheeks="blush")

                call nar(">Ты разводишь булочки в разные стороны, а затем ударяешь их друг об друга...")

                call her_head("Ах...{image=textheart} [genie_name], мне правда нужно идти... до того как я-","base","ahegao_raised",cheeks="blush")

                if daytime:
                    call her_head("Опоздаю в класс... Занятия вот-вот начнутся...","open","baseL",cheeks="blush")
                else:
                    call her_head("Поздно лягу... Сейчас становится очень... поздно...","open","baseL",cheeks="blush")

                m "Что ж, хорошо..."
                call blkfade

                ">Ты отпустил задницу девушки..."
                ">Гермиона прикрывается..."

                call h_action("none")

                call play_music("chipper_doodle") # HERMIONE'S THEME.

                if current_payout < 100:
                    if whoring >= 18:
                        call her_head("Пожалуйста, не думайте, что я забыла, что вы нарушили свое обещание, [genie_name].","base","baseL",cheeks="blush")
                        call her_head("Я жду, что бы вы загладили свою вину, позже...","base","baseL",cheeks="blush")
                    else:
                        call her_head("Пожалуйста, не думайте, что я забыла, что вы нарушили свое обещание, [genie_name].","annoyed","angryL",cheeks="blush")
                    m "Хорошо..."

            call ctc

            hide screen hermione_main
            call blkfade

        "\"Держать руки при себе, только смотреть.\"":

            call nar(">Ты долго смотришь на голую задницу Гермионы...")
            call ctc

            #First Event
            if whoring >= 9 and whoring < 15:

                menu:
                    "-\"У тебя фантастическая задница\"-":
                        m "Ты должна носить более короткие юбки, чтобы показать немного свою..."
                        call her_head(".....................","base","closed")
                    "-\"У тебя посредственная задница...\"-":
                        ">Ты некоторое время с разочарованием смотришь на ее задницу..."
                        call her_head(".....................","annoyed","frown")
                        $ mad +=3

            #Second Event
            elif whoring >= 15 and whoring < 18:

                menu:
                    "\"У тебя хорошая аккуратная попочка.\"":
                        call her_head("","annoyed","closed")
                        call ctc
                        call her_head("Спасибо [genie_name].","base","closed")
                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                        call her_head("(Может быть, в следующий раз он потрогает ее...)","annoyed","annoyed")

                    "\"Хм... Я видел и лучше.\"":
                        $ mad += 9
                        her "Пф..."
                        her "Хорошо, в этом случае мы закончили?"

            #Third Event
            elif whoring >= 18:

                menu:
                    "\"У тебя потрясающая попка, [hermione_name].\"":
                        call her_head("Вы правда так думаете [genie_name]?","annoyed","base")
                        call her_head("Я рада, что вам она понравилось, [genie_name]...","base","closed")
                    "\"У тебя хорошая задница... Я предполагаю...\"":
                        call her_head("А?","annoyed","base")
                        call her_head("Это значит, что вам не понравилась, [genie_name]?","annoyed","base")
                        call her_head("Простите... Я постараюсь работать эффективнее над ней.","disgust","down_raised")


            call nar(">Ты смотришь на ее задницу еще некоторое время...")
            call ctc

            m "Хорошо, теперь можешь одеваться [hermione_name]..."

            if whoring < 15 or mad > 1:
                call her_head(".............","annoyed","base")
            else:
                call her_head(".............","base","closed")

            call ctc

            hide screen hermione_main
            call blkfade



        "\"Начать дрочить.\"":

            hide screen hermione_ass
            call blkfade

            ">Ты достаешь свой член и начинаешь дрочить..."

            hide screen chair_left #Genie's chair.
            show screen chair_left #Genie's chair.
            hide screen desk
            show screen desk
            call gen_chibi("jerking_off","mid","base")
            hide screen bld1
            hide screen blktone
            call hide_blkfade
            call play_music("chipper_doodle")
            call ctc

            #First Event.
            if whoring >= 9 and whoring < 15:
                $ mad += 2

                show screen blktone
                show screen hermione_ass
                call her_head("Наслаждайтесь видом [genie_name]","angry","wide")
                m "Да [hermione_name]. Стой спокойно и дай мне посмотреть еще немного..."

                call nar(">Ты голодным взглядом пялишься на задницу Гермионы...")
                call her_head("[genie_name], как долго мне еще здесь стоять?","shock","worriedCl")
                call nar(">Ты продолжаешь дрочить...")
                m "Не долго..."
                call her_head("[genie_name]...","disgust","down_raised",cheeks="blush")
                call her_head("Вы не... трогаете себя...?","disgust","down_raised",cheeks="blush")
                m "Ах... конечно нет [hermione_name], ты знаешь, что я никогда не сделаю... такую вещь..."
                call her_head("Хммм.....","angry","worriedCl",cheeks="blush")
                call her_head("Ну, если вы не трогаете свою штуку...","angry","angry",cheeks="blush")
                call her_head("Я надеюсь, что вы примете правильное решение...'","angry","worriedCl",cheeks="blush")
                call her_head("Ой, нет... {size=-5}сперма...{/size} на мне...","angry","worriedCl",cheeks="blush")

                menu:
                    "\"Конечно нет\"":
                        call her_head("Хорошо.","scream","wide",cheeks="blush")
                        call her_head("Я имею в виду, как я разделась и показала вам...","scream","wide",cheeks="blush")
                        call her_head("..........","annoyed","angryL",cheeks="blush")
                        call her_head("Не, {size=-5}кончайте{/size} на меня - это наименьшее, что вы могли бы сделать...","angry","angry",cheeks="blush")

                        call nar(">Гермиона начинает смотреть на тебя краем глаза...")

                        call her_head("Вы готовы...","angry","suspicious",cheeks="blush")
                        g4 "Почти готов [hermione_name]!"
                        call her_head("Сделайте это, [genie_name]... кончите на меня...","angry","suspicious",cheeks="blush",tears="messy")

                    "-Начать дрочить еще сильнее-":
                        call nar(">Ты начинаешь яростно дрочить свой член!")
                        call her_head("...","scream","angry",cheeks="blush",emote="01")
                        call nar(">Ты дрочишь еще быстрее!")
                        call her_head("Вы собираетесь кончить...","annoyed","angryL",cheeks="blush")
                        g4 "Почти, шлюха!"
                        call her_head("Давайте я встану...","angry","suspicious",cheeks="blush")
                        call her_head("Пока вы кончаете на меня!","angry","suspicious",cheeks="blush")

            #Second Event.
            elif whoring >= 15 and whoring < 18:

                show screen blktone
                show screen hermione_ass
                call her_head("Вы наслаждаетесь видом [genie_name]?","angry","wide")
                m "Я безмерно наслаждаюсь"
                call her_head("[genie_name], вы... трогаете себя...","shock","worriedCl")
                m "Не вини меня [hermione_name]..."
                call her_head("Ну, а кого я должна винить, [genie_name]?","shock","worriedCl")
                call nar(">Ты набираешь темп...")
                m "Вини себя [hermione_name]..."
                m "Или, скорее, вини свою идеальную маленькую попку!"
                call her_head("..................","shock","worriedCl")
                call her_head("(Его член такой большой...)","disgust","down_raised",cheeks="blush")
                m "Да... Да, нравится это..."
                m "Попробуй потрясти немного..."
                call her_head("..............","disgust","down_raised",cheeks="blush")
                call her_head("Ну, если так и надо...","open","baseL",cheeks="blush")
                call her_head("Вы можете продолжать прикасаться к себе, [genie_name]...","open","baseL",cheeks="blush")
                call her_head("Но вы должны пообещать мне не...","soft","baseL",cheeks="blush")
                call her_head("Не... эм...","open","baseL",cheeks="blush")
                call her_head("Не кончать...","annoyed","angryL",cheeks="blush")
                call her_head("Не кончать на меня, [genie_name]...","angry","angry")
                m "Ты уверена..."
                m "Я уверен, что ты бы хотела, чтоб твоя задница была в моей сперме!"
                call her_head(".......................","angry","worriedCl",cheeks="blush")
                call nar(">Ты начинаешь дрочить еще сильнее...")
                g4 "Да, я знаю, что ты хочешь этого! Да!"
                call her_head("................","angry","worriedCl",cheeks="blush")

                call nar(">Ты собираешься кончить...")

            #Third Event.
            elif whoring >= 18:

                show screen blktone
                show screen hermione_ass
                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush")

                if whoring >= 21:
                    call her_head("А...","base","ahegao_raised",cheeks="blush")
                    call nar(">Гермиона оглядывается и видит, как ты дрочишь свой член.")
                    call her_head("Он такой большой...","open","baseL",cheeks="blush")
                    call her_head("Вы просто не смогли воздержаться, не так ли [genie_name]?","base","baseL",cheeks="blush")
                    call her_head("..................","base","ahegao_raised",cheeks="blush")
                    m "Да... Да, мне нравится твоя..."
                    m "Да, потряси своей задницей [hermione_name]..."
                    call her_head("..............","base","ahegao_raised",cheeks="blush")
                    call her_head("Ну, пусть будет так...","open","baseL",cheeks="blush")
                    call her_head("Но пообещайте мне, что не будете...","soft","baseL",cheeks="blush")
                    call her_head("Не... эм...","open","baseL",cheeks="blush")
                    call her_head("Не кончать... на меня, [genie_name]...","base","ahegao_raised",cheeks="blush")
                    m "Ладно, все равно..."
                    m "Ах ты маленькая потаскушка. Ты противная маленькая шлюха!"
                    call her_head(".......................","base","ahegao_raised",cheeks="blush")
                    ">Ты начинаешь дрочить еще сильнее..."
                    g4 "Да, я знаю, что ты хочешь этого! Да!"
                    call her_head("................","base","ahegao_raised",cheeks="blush")

                else:
                    call her_head("[genie_name], на самом деле я никогда не соглашалась на это...","shock","worriedCl")
                    m "На что ты жалуешься, [hermione_name]?"
                    m "Я даже не трогаю твою задницу...."
                    call her_head("Да, но вы... трогаете себя, [genie_name].","shock","worriedCl")
                    m "Стой спокойно, толстожопая сучка."
                    m "Скоро все закончится."
                    call her_head("..................","shock","worriedCl")
                    m "Да... Да, мне нравится твоя..."
                    m "Да, твоя голая задница..."
                    call her_head("..............","disgust","down_raised",cheeks="blush")
                    call her_head("Ну, пусть будет так...","open","baseL",cheeks="blush")
                    call her_head("Но пообещайте мне, что не будете...","soft","baseL",cheeks="blush")
                    call her_head("Не... эм...","open","baseL",cheeks="blush")
                    call her_head("Не кончите...","annoyed","angryL",cheeks="blush")
                    call her_head("Не кончите на меня, [genie_name]...","annoyed","angryL",cheeks="blush")
                    m "Ладно, все равно..."
                    m "Ах, ты маленькая шлюха. Ты противная маленькая шлюха!"
                    call her_head(".......................","disgust","down_raised",cheeks="blush")
                    call nar(">Ты начинаешь дрочить еще сильнее...")
                    g4 "Да, я знаю, что ты хочешь этого! Да!"
                    call her_head("................","disgust","down_raised",cheeks="blush")


            ### GENIE STARTS CUMMING ###

            #First and second event.
            if whoring < 18:
                menu:
                    "-Кончить на пол-":

                        hide screen blktone
                        call blkfade

                        g4 "Ах! Ты жирная шлюха!"
                        call her_head("Профф-- ??","scream","wide",cheeks="blush")

                        call cum_block

                        g4 "Ах! ДА!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        call hide_blkfade
                        call ctc

                        show screen bld1
                        call her_head("[genie_name]!","scream","angry",cheeks="blush",emote="01")
                        g4 "Ох, так даже лучше...."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3

                        call her_head("[genie_name], вы так много...","angry","suspicious",cheeks="blush")

                        hide screen hermione_ass
                        call gen_chibi("stand","desk","base")
                        call her_chibi("stand","mid","base")
                        hide screen bld1
                        hide screen blktone
                        with fade
                        call ctc

                        call bld
                        m "Ох, это было потрясающе..."

                        call her_main("","disgust","down_raised",xpos="right",ypos="base")
                        pause.5

                        her "Пол..."
                        her "Он покрыт...."
                        m "Все благодаря твоей заднице, [hermione_name]."
                        her "................"
                        call her_main("Мне нужно одеться...","open","closed")
                        call ctc

                        hide screen hermione_main
                        call blkfade

                    "-Кончить на ее попку-":

                        hide screen blktone
                        call blkfade

                        g4 "Ах! Ты жирная шлюха!"
                        call her_head("Профф-- ??","scream","wide",cheeks="blush")
                        call cum_block

                        g4 "Ах! ДА!"

                        hide screen bld1
                        call gen_chibi("cumming","on_girl","base")
                        hide screen bld1
                        call hide_blkfade
                        call ctc

                        show screen bld1
                        with d3
                        $ hermione_ass_cum = True
                        call her_head("[genie_name], нет, вы обещали!","scream","angry",cheeks="blush",emote="01")
                        g4 " Ох, как хорошо..."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        call ctc


                        hide screen hermione_ass
                        call gen_chibi("stand","desk","base")
                        call her_chibi("stand","mid","base")
                        hide screen bld1
                        hide screen blktone
                        with fade
                        call ctc

                        call bld
                        m "Ох, это потрясающе..."
                        call her_main("","disgust","down_raised",xpos="right",ypos="base")
                        pause.5

                        if whoring < 15:
                            call her_main("Как вы могли так поступить со мной, [genie_name]?!","scream","angry")
                            call her_main("Теперь моя попка, вся покрыта вашей спермой!","angry","angry")
                        else:
                            call her_main("[genie_name], как вы могли...?","angry","suspicious",cheeks="blush")
                            call her_main("Моя попа...","disgust","down")
                            call her_main("Она вся в....","disgust","down_raised")

                        m "Не волнуйся, я дам твоему факультету очки, [hermione_name]."
                        m "Ты молодец."
                        her "................"
                        call ctc

                        hide screen hermione_main
                        call blkfade

                        if whoring < 15:
                            $ mad += 20
                        else:
                            $ mad += 10


            #Third Event.
            else: #18+

                menu:
                    g4 "Ах! (Я собираюсь кончить!)"

                    "-Воздержаться-":
                        g4 "Ох, хорошо..."
                        g4 "Мне лучше остановиться..."
                        call her_head("...............","disgust","down_raised",cheeks="blush")
                        call her_head("Эм... Я имела в виду, что бы вы не кончали на меня...","disgust","down_raised",cheeks="blush")
                        m "А?"
                        call her_head("Но я не возражаю, если вы...","shock","worriedCl")
                        call her_head("Кончите...","disgust","down_raised",cheeks="blush")
                        call her_head("На мою попку--","base","baseL",cheeks="blush")
                        g4 "Ах! Ты шлюшка!"
                        call her_head("???","mad","wide",cheeks="blush")

                        call cum_block

                        g4 "Ах! ДА!"

                        $ hermione_ass_cum = True
                        call gen_chibi("cumming","on_girl","base")
                        hide screen hermione_ass
                        hide screen bld1
                        hide screen blktone
                        hide screen blkfade
                        call ctc

                        show screen blktone
                        show screen hermione_ass
                        with fade

                        call her_head("Вот и все [genie_name], кончили... на меня...","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Ох, так хорошо..."
                        $ no_blinking = False #When True - blinking animation is not displayed.

                        call her_head("ах{image=textheart} ладно, что сделано, то сделано...","base","baseL",cheeks="blush")

                    "-Кончить-":
                        g4 "Ах! Ты жирная шлюха!"
                        call her_head("???","mad","wide",cheeks="blush")

                        call cum_block

                        g4 "Ах! ДА!"

                        $ hermione_ass_cum = True
                        hide screen hermione_ass
                        call gen_chibi("cumming","on_girl","base")
                        hide screen bld1
                        hide screen blktone
                        hide screen blkfade
                        call ctc

                        show screen blktone
                        show screen hermione_ass
                        with fade

                        call her_head("Ах...{image=textheart} она такая горячая...{image=textheart}","shock","worriedCl")
                        call her_head("Ее так много...{image=textheart}","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Ох, так хорошо..."
                        call her_head("Ах...{image=textheart}","angry","worriedCl",cheeks="blush",emote="05")

                        call her_head("Ну, что сделано, то сделано...","angry","worriedCl",cheeks="blush")

                hide screen hermione_ass
                call gen_chibi("stand","desk","base")
                call her_chibi("stand","mid","base")
                hide screen blktone
                with fade
                pause.5

                call bld
                m "Ах, это было потрясающе..."
                call her_main("","disgust","down_raised",xpos="right",ypos="base")
                pause.5
                her "Моя задница вся покрыта..."
                m "Не волнуйся, она по-прежнему выглядит великолепно, [hermione_name]."
                m "Может быть, даже еще лучше..."
                call her_main("Спасибо [genie_name].","base","closed")
                call her_main("Мне нужно привести себя в порядок...","annoyed","closed")
                call ctc

                hide screen hermione_main
                call blkfade



    $ hermione_ass_cum = False

    call h_action("none") #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01
    hide screen groping_01
    hide screen groping_02

    call her_chibi("stand","desk","base")

    hide screen chair_left
    show screen genie
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main("","","",trans="fade",xpos="right",ypos="base")

    if whoring < 18:
        if whoring < 15:
            call her_main("Могу я получить очки?","base","ahegao_raised",cheeks="blush")
            if current_payout < 100:
                $ mad +=7

        $ gryffindor +=current_payout
        m " \"Гриффиндор\" получает [current_payout] очков!"
        stop music fadeout 10.0

        call her_main("..................","annoyed","worriedL")
        her "Спасибо [genie_name]..."

    else:
        call her_main("..................","base","happyCl")


    if daytime:
        her "Теперь, если вы не возражаете, мне лучше уйти, мои занятия вот-вот начнутся."
    else:
        her "Мне лучше сейчас уйти. Уже довольно поздно..."

    $ new_request_08_heart = 1
    $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 1 #Event hearts level (0-3)

    if whoring >= 9 and whoring < 12:
        $ new_request_08_heart = 1
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 12 and whoring < 15:
        $ new_request_08_heart = 2
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 15:
        $ new_request_08_heart = 3
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 3 #Event hearts level (0-3)

    if whoring < 12:
        $ whoring +=1

    $ hg_pf_ShowMeYourAss_OBJ.points += 1

    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("desk","door",2.5)

    #First event.
    if whoring >= 9 and whoring < 12:
        call her_head("(Как это унизительно... почему я согласилась на это...?)","disgust","down_raised",cheeks="blush")

    #Second event.
    elif whoring >= 12 and whoring < 15:
        call her_head("........................","disgust","down_raised",cheeks="blush")

    #Third event.
    elif whoring >= 12:
        call her_head("{size=-5}(Это было так волнующе...){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-5}(Нет, Гермиона, ты глупая девчонка!){/size}","angry","angry",cheeks="blush")
        call her_head("{size=-5}(Мне так стыдно! Хорошие девочки не ублажают своих директоров!){/size}","angry","angry",cheeks="blush")
        call her_head(".................................","base","ahegao_raised",cheeks="blush")
    elif whoring >= 18 and aftersperm:
        call her_head("{size=-5}(Это было так волнующе...){/size}","base","ahegao_raised",cheeks="blush")
        call her_head("{size=-5}(Интересно, что он попросит меня сделать в следующий раз...?){/size}","open","ahegao_raised",cheeks="blush")

    $ aftersperm = False #Shows cum stains on Hermione's uniform.

    call her_chibi("leave","door","base")

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
