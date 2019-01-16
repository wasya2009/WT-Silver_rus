

label hg_pf_TouchMe: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TouchMe_OBJ.points == 0:
        m "{size=-4}(Должен ли я, попросить ее подрочить мне?){/size}"
    else:
        m "{size=-4}(Мне хочется чтоб она подрочила мне!){/size}"

    if hg_pf_TouchMe_OBJ.points < 1:
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    if hg_gryffCheer_OBJ.purchased:
        m "\"(Должен ли я попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, я хочу, чтобы ты переоделась.."
                call her_main("Во что?","open","worriedL")
                m "В болельщицу."
                if whoring >= 17:
                    call her_main("В болельщицу?","annoyed","annoyed")
                    m "В болельщицу Гриффиндора."
                    call her_main("...","upset","wink")
                    call her_main("Хорошо, по крайней мере, это Гриффиндор.","annoyed","worriedL")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_gryffCheer_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Не сейчас.)\"":
                pass

    $ current_payout = 45 #Used when haggling about price of th favor.

    call bld

    #First Event.
    if hg_pf_TouchMe_OBJ.points == 0:

        m "[hermione_name]."
        call her_main("Да, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "Ты знаешь, что такое \"дрочить\" ?"

        if whoring < 12:
            jump too_much

        call her_main("Что?","annoyed","annoyed")
        m "Я хочу, чтоб ты сделала это..."
        call her_main("[genie_name]!","angry","angry")
        m "Еще одна услуга. Ничего страшного, правда?"
        call her_main("......","disgust","glance")
        call her_main("{size=-7}Я хочу 100 очков за это...{/size}","angry","worriedCl",emote="05")
        m "А? Что?"
        call her_main("Я хочу 100 очков за это!!!","scream","worriedCl")
        m "100 очков, да?"
        m "И ты будешь мне дрочить?"
        call her_main("{size=-7}Да...{/size}","disgust","glance")
        m "Прости, я тебя не расслышал..."
        call her_main("Да, я сказала, да! Я буду вам дрочить, [genie_name]!","scream","worriedCl")

        $ new_request_16_heart = 1
        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        label back_to_handjob_choices:

        menu:
            m "..."
            "\"Ты получишь 15 очков.\"":
                $ mad +=7
                call her_main("За 15 очков, я могла бы позволить вам немного поприставать ко мне, но не более, [genie_name].","annoyed","angryL")
                her "Я не буду опускаться так низко, чтоб дрочить за 15 очков."
                her "Это оскорбительно, [genie_name]."
                jump back_to_handjob_choices

            "\"Ты получишь 45 очков.\"":
                if mad > 7: #You could spam points into infinity with the choice above.
                    $ mad = 7
                call her_main(".....","annoyed","angryL")
                call her_main("45 очков...?","open","down")
                her "Это может помочь \"Гриффиндору\" выйти в лидеры..."
                m "Это значит \"да\"?"
                call her_main("Да, это да, [genie_name].","annoyed","annoyed")
                m "Отлично!"

            "\"Ты получишь 100 очков.\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 очков?!","scream","wide_stare")
                her "Это очень хорошо поможет \"Гриффиндору\" выйти в лидеры!"
                m "Это значит \"да\"?"
                call her_main("Конечно!","smile","happyCl")
                call her_main("Если это принесет \"Гриффиндору\" 100 очков, я буду не против прикоснуться к... немного работы и все.","smile","happyCl",emote="06")


        call play_music("playful_tension") # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        show screen chair_left
        hide screen desk
        show screen desk
        call gen_chibi("jerking_off","on_girl","base")

        hide screen bld1
        hide screen blktone
        with fade
        call ctc

        show screen bld1
        call her_main("...........","open","base",xpos="right",ypos="base")
        m "Начинай как будешь готова, [hermione_name]."
        pause.5

        label event_01_round_02:
        hide screen hermione_main
        call blkfade

        ">Гермиона обхватывает твой член..."
        m "Хорошо. Погладь его."
        call her_head("Хорошо...","angry","worriedCl",emote="05")
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide")
        call gen_chibi("handjob","desk","base")
        hide screen bld1
        call hide_blkfade
        call ctc

        call play_music("playful_tension") # SEX THEME.
        call blktone
        g9 "Круто..."

        if hg_pf_TouchMe_OBJ.points == 0:
            call her_main("!!!","shock","wide",xpos="right",ypos="base")
            call her_main("Вы собираетесь закончить, [genie_name]?!")
            m "Закончить?"
            m "Не смеши [hermione_name], мы только начали."
            call her_main("Ох...","angry","worriedCl",emote="05")
            call her_main("......")
            call her_main("Но вы же предупредите меня, не так ли, [genie_name]?","upset","wink")
        else:
            call her_main("[genie_name]...?","angry","worriedCl",emote="05",xpos="right",ypos="base")
            m "О чем?"
            call her_main("Вы предупредите меня заранее... эм... когда вы...","angry","worriedCl",emote="05")

        $ d_flag_01 = False #If TRUE Genie promised to warn her.

        menu:
            m "..."
            "\"Конечно, я дам тебе знать, когда придет время.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                call her_main("Спасибо, [genie_name].","normal","worriedCl")
            "\"Я и сам не всегда знаю, когда...\"":
                call her_main("Серьезно? Но я думала...","open","base")
                call her_main("Ну, тогда ладно...","normal","worriedCl")

        call her_main("........","open","base")
        m "............."
        call her_main(".............","normal","worriedCl")
        call her_main("Эм... [genie_name]?")
        m "Да, что такое?"
        call her_main("Как долго это будет продолжаться?","open","base")
        m "Чего, продолжаться?"

        if daytime:
            call her_main("Ну, мои занятия вот-вот начнутся....","upset","wink")
        else:
            call her_main("Ну, у меня есть проекты, которые нужно закончить...","upset","wink")
            call her_main("Завтра их сдаем, и уже довольно поздно...")

        m "Тебе нужны очки или нет?"
        call her_main("Нужны, [genie_name]! Простите...","base","happyCl")
        call her_main("Тогда я продолжу его гладить...")
        m "Ну, есть кое-что, для ускорения процесса..."
        call her_main("Правда? И что это, [genie_name]?","base","base")

        menu:
            m "..."
            "\"Скажи мне, какая ты шлюха!\"":
                call her_main("Что?","angry","angry")
                call her_main("Но, я не...")
                m "Не всегда нужно говорить правду, [hermione_name]."
                m "Придумай что-нибудь."
                call her_main("Серьезно?","upset","wink")
                m "Конечно. Получай удовольствие."
                call her_main("В таком случае...","open","down")
                call her_main("Я... шлюха.")
                m "Хех... хорошо. Продолжай."
                call her_main("Я жирная шлюха...","open","down")
                m "Да, ты."
                call her_main("Я самая жирная шлюха в Англии!","annoyed","annoyed")
                call her_main("Я пытаюсь вести себя невинно, но на самом деле я всегда думаю только о члене!")
                m "Да, ты маленькая шлюшка!"
                call her_main("Да! Я шлюшка!","annoyed","angryL")
                call her_main("Я хочу ваш член.")
                m "Очень хорошо!"
                m "Но, как я уже сказал, тебе не обязательно быть честной."
                call her_main("Что?","shock","wide")
                call her_main("[genie_name], те вещи, которые я говорю-неправда!","upset","wink")
                g9 "Хех... Я знаю. Просто прикалываюсь."
                call her_main("[genie_name]!","disgust","glance")
                m "Ты отлично справляешься. Продолжай!"
                call her_main(".....","open","down")
                call her_main("Я люблю член...")
                call her_main("И я люблю...","clench","down_raised")
                call her_main("Сперму... да, сперму...")
                call her_main("Я люблю глотать ее...")
                call her_main("Я хочу, что б вы накормили ей меня, [genie_name]!","open_tongue","glance")
                g4 "!!!"
                call her_main("Или еще лучше, залейте меня спермой, [genie_name]!","smile","glance")
                with hpunch
                g4 "{size=-4}(Вот-вот кончу, стоит ли предупреждать?){/size}"

            "\"Высунь язык и посмотри на меня!\"":
                call her_main("Что?","base","base")
                m "Просто сделай это, шлюшка."
                call her_main("Вот так?","open_wide_tongue","squintL")
                m "Да, хорошо. Продолжай смотреть мне в глаза и дрочить."
                call her_main(".....................","open_wide_tongue","base")
                m "Да... отлично..."
                call her_main("...........","open_wide_tongue","base")
                call her_main("...........")
                call her_main("Я не могу держать рот открытым так долго, [genie_name]. Я начну пускать слюни...","open","base")
                m "Но я хочу, чтоб ты пускала слюни..."
                call her_main("Что? Но я буду выглядеть глупо!","open","base")
                m "Ради очков, [hermione_name]!"
                call her_main(".......","annoyed","worriedL")
                m "Разве ты не хочешь, чтоб я закончил это как можно быстрее?"
                call her_main("............","normal","worriedCl")
                call her_main("А-ха.....","open_wide_tongue","base")
                m "Хорошо, [hermione_name]."
                call her_main("..............","open_wide_tongue","base")
                m "Да, продолжай дрочить его."
                call her_main("..................","open_wide_tongue","base")
                g4 "Ох... Я хочу, чтоб мой член залез тебе в рот!"
                call her_main(".................","open_wide_tongue","angryCl")
                m "Нет, продолжай смотреть на меня!"
                call her_main(".....................","open_wide_tongue","base")
                m "Да, маленькая шлюшка!"
                call her_main("......................","open_wide_tongue","angry")
                m "Я хочу кончить в рот, да..."
                call her_main("................","open_wide_tongue","angry")
                with hpunch
                g4 "{size=-4}(Вот-вот кончу, стоит ли ее предупредить?){/size}"

            "\"Поцелуй мой член!\"":
                call her_main("Простите?","angry","angry")
                m "Ты поняла, просто маленький поцелуй."
                call her_main(".............","angry","angry")
                call her_main("...Губами?","shock","wide")
                m "Конечно... Это ускорит процесс."
                call her_main("*вздох!*..............","open","down")
                call her_main("Ну, я думаю, смогу...")
                call nar(">Гермиона нежно поцеловала головку.")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                pause 2

                call gen_chibi("handjob","desk","base")
                pause.5

                show screen blktone
                call her_main("Вам понравилось?","open","down")
                m "Не так уж и плохо, не так ли?"
                call her_main("Нет, я думаю нет...","upset","wink")
                m "Можешь ли повторить?"
                call her_main("Могла бы...","normal","worriedCl")
                m "Сделай это!"
                call her_main("Ну, хорошо...","open","base")
                call nar(">Гермиона еще раз поцеловала твою головку...")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                pause 3

                call nar(">На этот раз она целовала дольше...")
                pause.8

                call blkfade
                call gen_chibi("handjob","desk","base")
                call hide_blkfade
                pause.5

                call blktone
                m "Хорошо... Теперь поцелуй снова, подольше."
                call her_main("Вы имеете ввиду, чтоб я долго целовала... член, [genie_name]?","open","base")
                call her_main("Нет, я буду выглядеть глупо...","annoyed","worriedL")
                m "Это не глупо, [hermione_name]. Никто не смотрит."
                call her_main("Вы, [genie_name].","open","down")
                m "Но в этом весь смысл!"
                call her_main("......","annoyed","annoyed")
                m "Это заставит меня кончить в кратчайшие сроки!"
                call her_main("...............","annoyed","angryL")
                m "И тогда ты сможешь быстрее пойти делать свои уроки."
                call her_main(".............","disgust","glance")
                call her_main("Ну, тогда хорошо....","open","down")
                call nar(">Гермиона снова наклоняется...","start")
                call nar(">Она касается губами головки и дольше держит...","end")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                call ctc

                call blktone
                m "Очень хорошо..."
                m "Теперь прикоснись языком."
                call her_main("??!","open_tongue","")
                m "Это последнее, о чем я прошу тебя."
                her "............"
                call nar(">Ты чувствуешь кончик язычка Гермионы...")
                m "Да, мне нравится..."
                call nar(">Гермиона немного шевелит языком....")
                m "ДА... хорошо..."

                call blkfade
                hide screen hermione_main
                call gen_chibi("handjob","desk","base")
                hide screen blktone
                call hide_blkfade
                pause.8

                show screen blktone
                call her_main("Так, это сработало? Вы уже готовы... Кончать, [genie_name]?","open","down")
                g4 "{size=-4}(Удивительно! Я собираюсь кончить, стоит ли предупредить ее?){/size}"

        menu:
            m "..."
            "-Предупредить-":
                g4 "Вот-Вот, [hermione_name]! Тебе лучше быть на готове!"
                call her_main("Что? Так скоро?!","shock","wide")
                g4 "{size=+5}ДА, ты проделала огромную работу!!!{/size}"
                g4 "{size=+5}Ты маленькая шлюшка!!!{/size}"
                hide screen hermione_main
                call blkfade

                call her_head("Нет, [genie_name], подождите, я--","angry","base")
                g4 "{size=+5}Слишком поздно, маленькая шлюшка!{/size}"
                call her_head("*whimper*","angry","down_raised")
                ">Гермиона внезапно кладет ваш член под свою рубашку..."
                g4 "?!!"
                ">Ощущение ее теплой кожи дает о себе знать, ты начинаешь кончать, как сумасшедший."

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("cumming_under_shirt","desk","base")
                hide screen blktone
                call hide_blkfade
                stop music fadeout 1.0
                call ctc

                $ aftersperm = True
                call her_main(".......................","angry","wide")
                m "..........................."
                call her_main(".......................","angry","wide")
                m "....................?"
                call her_main(".......................","angry","down_raised")
                m "...Что сейчас за херня произошла?"

                call play_music("chipper_doodle") # HERMIONE'S THEME.

                show screen bld1
                call her_main("Я не знаю... я запаниковала...","angry","worriedCl",emote="05")

                if daytime:
                    call her_main("Мои занятия вот-вот начнутся, и я не хотела, чтобы вы испортили мою форму, [genie_name]...","angry","worriedCl",emote="05")
                    m "Ты пойдешь так на занятия?"
                    m "В этой одежде, пропитанной изнутри спермой?"
                    call her_main("А у меня есть выбор?","angry","down_raised")
                    call her_main("Я не могу просто пропустить урок...")
                else:
                    call her_main("В это время в общей комнате \"Гриффиндора\" полно людей...","angry","worriedCl",emote="05")
                    call her_main("Я не хочу возвращаться туда, покрытая... спермой, [genie_name].")
                    call her_main("Уже довольно поздно...","angry","base")
                    m "Так, ты пойдешь?"
                    m "В одежде , пропитанной спермой?"
                    call her_main("А какой у меня выбор?","angry","down_raised")

                call ctc
                call blkfade

                ">Гермиона отпускает твой пульсирующий член."

                call her_chibi("stand","mid","base")
                call gen_chibi("stand","desk","base")
                hide screen bld1
                call hide_blkfade
                pause.5

                call her_main("Эм... Ваша сперма, [genie_name]...","angry","down_raised")
                call her_main("Она повсюду под моей одеждой...","angry","base")
                m "Положи его в рот следующий раз."
                call her_main("Я... так не думаю, [genie_name].","annoyed","annoyed")
                call her_main("Мне действительно нужно идти. Могу ли я просто получить очки?")


            "-Кончить-":

                with hpunch
                g4 "АХ!"
                call blkfade

                call her_head("ЧТО?!","shock","wide")
                g4 "Держи!"

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("cumming_on_shirt","desk","base")
                hide screen blktone
                call hide_blkfade
                call ctc

                $ aftersperm = True

                show screen bld1
                call her_main(".......................","angry","wide")
                call gen_chibi("cumming_on_shirt_pause")
                m "Да... Теперь я чувствую себя намного лучше ..."
                pause.5

                $ g_c_u_pic = "images/animation/15_cum_21.png"
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                call her_main("","soft","base",tears="soft")
                pause.5
                her ".........."
                m "Ну, я думаю, что на этом все..."
                pause.2

                hide screen hermione_main
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide")
                call her_chibi("stand","desk","base")
                show screen genie
                hide screen bld1
                with fade
                pause.8

                show screen bld1
                call her_main("[genie_name]! Что вы сделали?!","scream","worriedCl")
                m "Что?"

                if d_flag_01: #If TRUE Genie promised to warn her.
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    $ mad += 11
                    call her_main("Вы обещали предупредить, [genie_name]!","angry","angry")
                    m "Ох, точно... Что-то я увлекся."
                    call her_main("А теперь моя форма испорчена.","annoyed","angryL")
                    her "...Я хотела бы получить очки."

                else:

                    if daytime:
                        call her_main("Моя форма испорчена!","annoyed","angryL")
                        call her_main("Мои занятия вот-вот начнутся, а я не могу ходить в таком виде!","open","down")
                        m "Конечно ты можешь, просто вытри..."
                        m "Никто даже и не заметит."
                        call her_main("...Я хотела бы получить очки.","annoyed","annoyed")
                    else:
                        call her_main("Моя форма испорчена!","annoyed","angryL")
                        her "Я должна идти в комнату отдыха \"Гриффиндора\" в таком виде?!"
                        m "Почему нет? Ты выглядишь горячо, [hermione_name]!"
                        call her_main("[genie_name]!!!","annoyed","annoyed")
                        m "Хорошо, хорошо. Просто сотри или еще что-нибудь придумай."
                        m "Никто даже не заметит."
                        call her_main("...Я хотела бы получить очки.","annoyed","annoyed")


    #Second Event.
    elif hg_pf_TouchMe_OBJ.points == 1:

        $ new_request_16_heart = 2
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("Да, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "Ты знаешь что такое \"дрочить\"?"
        call her_main("Вы уже спрашивали меня об этом, [genie_name].","disgust","glance")
        m "Ах, точно."
        m "Ну, я хочу, чтоб ты снова поигралась с моим членом."
        call her_main("[genie_name], вы опять ведете себя вульгарно...","upset","closed")
        m "Ладно, ладно."
        m "[hermione_name], я хотел бы купить у тебя еще одну услугу."
        call her_main("Конечно, [genie_name].","annoyed","angryL")
        g9 "Я хочу, чтоб ты поигралась с моим членом!"
        call her_main("..............","disgust","glance")
        m "Ох, давай. За честь \"Гриффиндора\"?"
        call her_main(".............","angry","angry")
        g9 "Играй с моим членом в честь \"Гриффиндора\", [hermione_name]!"
        call her_main("Прекратите говорить это, [genie_name]...","scream","angry",emote="01")
        m "Давай [hermione_name], я же не прошу тебя сделать это бесплатно."
        call her_main(".......","annoyed","angryL")
        stop music fadeout 4.0

        jump event_01_round_02 #Sets up handjob.


    #Third Event.
    elif hg_pf_TouchMe_OBJ.points >= 2:

        $ new_request_16_heart = 3
        $ hg_pf_TouchMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base")
        m "Ты не против подрочить мне еще раз?"

        if whoring <= 16:
            call her_main("Пока вы платите...","grin","baseL")
            m "Хорошо, тогда подойди сюда. Есть время, чтоб заработать немного очков."
        else:
            call her_main("Конечно нет [genie_name]...","grin","baseL")
            m "Что ж, тогда иди сюда."


        hide screen hermione_main
        hide screen bld1
        call blkfade

        stop music fadeout 3.0
        call her_head("Вам нравится, когда я делаю вот так, [genie_name]?","grin","baseL")
        g9 "Конечно, да! Очень хорошо!"
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide")
        call gen_chibi("handjob","desk","base")

        hide screen bld1
        call hide_blkfade
        call ctc

        call blktone
        m "Да, да, мне нравится..."
        m "Хм... Ты довольно хорошо это делаешь."
        call her_main("Спасибо, [genie_name].","base","happyCl",xpos="right",ypos="base")
        call her_main("Я подумала, чем лучше я сделаю, тем быстрее закончим.")
        m "Хм..."

        menu:
            m "..."
            "\"Что ты думаешь о моем члене?\"":
                call her_main("А?","open","base")
                call her_main("Ох...")
                call her_main("Я должна похвалить ваш пенис! Я совсем забыла.","angry","worriedCl",emote="05")
                m "Ну, тебе не обязательно--"
                call her_main("[genie_name], позвольте мне быть честной с вами...","upset","closed")
                m "Да?"
                call her_main("У вас самый большой пенис, который я когда-либо видела!","smile","angry")
                m "Ну, я полаг--"
                call her_main("Еще не все!","scream","angryCl")
                m "Прости."
                call her_main("Ваш член такой большой, что почти пугает меня!","angry","down_raised")
                g9 "Ах ты маленькая... Ты точно знаешь, что сказать..."
                call her_main("И я его хочу...","soft","ahegao")
                call her_main("Каждая женщина жаждет такого члена!")
                m "...Ты хороша!"
                call her_main("Есть еще!","scream","angryCl")
                m "Конечно..."
                call her_main("Я думаю, что ваш великолепный член является благословением для этого мира!","scream","angryCl")
                m "Ну, я бы не стал заходить так далеко--"
                call her_main("Слушайте меня, [genie_name]!","scream","angryCl")
                call her_main("Я думаю, что статуя, посвященная вашему великолепному пенису, будет установлена в каждом городе!")
                call her_main("Чтобы люди всего мира могли свободно поклоняться вашему пенису!")
                m "Ладно, я достаточно услышал."
                call her_main("Слишком?","angry","wink")
                m "Да, чуточку."
                call her_main("Простите...","angry","worriedCl",emote="05")
                m "Ничего страшного. Просто продолжай дрочить."
                call her_main(".................","soft","ahegao")
                call nar(">Гермиона продолжает дрочить.","start")
                call nar(">Она отлично справляется с этим.","end")
                m "Да, да... Мне нравится."

            "\"Назови себя шлюхой!\"":
                call her_main("Простите?","open","base")
                call her_main("Ох, точно! Я должна унижать себя, верно?","annoyed","suspicious")
                m "Ну, тебе не обязательно, но..."
                call her_main("Все в порядке, я не возражаю.","upset","closed")
                call her_main("Ну ладно! Я шлюха!","base","base")
                m "Хорошо. Рад, что ты это признала."
                m "Теперь я хочу, чтоб ты сказала..."

                menu:
                    m "..."
                    "\"Я никчемная шлюха!\"":
                        call her_main("Конечно.","angry","wink")
                        call her_main("Я никчемная шлюха.","soft","ahegao")
                        call her_main("Я грязная, маленькая шлюха.")
                        m "Да! Хорошо!"
                    "\"Я живу, чтоб сосать члены!\"":
                        call her_main("Эм...","angry","wink")
                        call her_main("Я живу, чтоб сосать пенисы, эм... я имела в виду члены...","base","base")
                        m "Правда? Ну почему бы тебе не пососать мой?"
                        call her_main("[genie_name], я просто повторяю за вами...","smile","angry")
                        m "Правда? Могла бы обмануть меня...."
                        call her_main("....................","angry","wink")
                        m ".................."
                    "\"Люблю глотать сперму!\"":
                        call her_main("Я люблю... эм... глотать сперму.","angry","wink")
                        m "Ты замешкалась."
                        call her_main("Да, я знаю....","angry","wink")
                        call her_main("Повтори...")
                        call her_main("Люблю глотать сперму!","soft","ahegao")
                        call her_main("Глотать сперму-это самое лучшее, что есть!")
                        call her_main("Я люблю это!")
                        call her_main("...................................","grin","dead")
                        call her_main("Как это было, [genie_name]?","angry","wink")
                        m "Прекрасно."

            "\"Это было здорово! Ты практиковалась?\"":
                call her_main("Хм?","base","happyCl")
                call her_main("Вроде... Ну, не очень...")
                call her_main("Я поговорила с девочками, и...","angry","wink")
                m "О дрочке?"
                call her_main("Среди всего прочего...","smile","happyCl",emote="06")
                m "Так, что, твои подружки, много знают об этом?"
                call her_main("Вообще-то, да. Я сама удивилась.","shock","wide")
                call her_main("В последнее время в нашей школе происходят всякие странные сексуальные вещи...","grin","baseL")
                call her_main("Не могу сказать, что одобряю их...")
                call her_main("Но они меня многому научили... tricks.","base","happyCl")
                m "Правда? Например?"
                call her_main("Ну, давайте посмотрим...","base","down")
                call her_main("Если я положу сюда руку...")
                call her_main("И сюда...")
                m "Ох, понятно... Это довольно приятно."
                call her_main("Сделать это?","angry","wink")
                call her_main("Джинни была права насчет этого...","grin","baseL")
                g4 "Что ты только что сказала?"
                call her_main("Джинни Уизли научила меня этому.","base","happyCl")
                m "Ох, хорошо..."

                #if not handjob_practice_with_ginny:
                #    call nar(>Your curiosity about Ginny grows!)
                #$ handjob_practice_with_ginny = True

                call her_main("Она сказала, что любой парень влюбится в меня, если я сделаю вот так...","base","down")
                call her_main("Можно еще сделать кольцо из пальцев...")
                call her_main("И потом я засуну туда палец...")
                m "Хм... Я ничего не чувствую..."
                call her_main("Правда?","angry","down_raised")
                call her_main("Хм...")
                call her_main("Ох! Точно!","base","down")
                call her_main("Палец должен быть здесь! Я глупая.")
                with hpunch
                with kissiris
                g4 "Ох!!! Великие пески пустыни, да!"
                call her_main("Правда? Вам хорошо?","smile","happyCl",emote="06")
                call her_main("Что будет если я придержу этот палец и нажму не много тут...","base","down")
                g4 "[hermione_name], ты убьешь меня!"
                call her_main("Серьезно? Серьезно?!","smile","happyCl",emote="06")
                call her_main("Это довольно весело!")
                call her_main("Эмм... Я имела в виду...","angry","wink")
                call her_main("Я делаю это для того, чтобы помочь моему факультету...")
                m "Да, да... \"Гриффиндору\" честь и все такое."
                m "Продолжай массировать это место..."
                m "О, да..."
                call her_main("...............","base","down")

        m "Да, продолжай."
        call her_main("..............","angry","wink")
        m "Теперь я хочу, чтобы ты сказала..."

        menu:
            m "..."
            "{size=-4}\"Я хочу, чтоб мой отец изнасиловал меня.\"{/size}":
                $ mad += 11
                call her_main("Я этого не хочу!","angry","angry")
                m "Я знаю. Просто скажи это."
                call her_main("Что отец насилует меня? Это отвратительно, [genie_name]!","angry","angry",emote="01")
                m "Это смешно."
                call her_main("...........","annoyed","annoyed")
                call her_main("Ну...","open","down")
                call her_main("Иногда, я фантазирую, об износиловании...")
                call her_main(".......")
                m "Понятно. И в твоих фантазиях..."
                m "Кто тебя насилует?"
                call her_main("Мой отец...?","angry","base")
                m "И тебе это нравится?"
                call her_main("Нет. Я плачу и умоляю его остановиться!","angry","down_raised")
                m "Хех... Круто."
                call her_main(".......","angry","down_raised")
                m "Ну, это было не так уж и сложно--"
                call her_main("Я кричу своей маме, но ее нет дома...","mad","worried",tears="soft")
                m "А?"
                call her_main("Мой папа ведет меня в комнату...","normal","worriedCl")
                call her_main("Он кидает меня на кровать!")
                call her_main("Я плачу \"Нет, папа, пожалуйста, я все еще девственница!\"","scream","worriedCl")
                call gen_chibi("handjob_pause")
                call her_main("Но он меня не слушает и срывает с меня трусики!","grin","dead")
                call her_main("Я умоляю его остановиться! Я кричу и кричу!","angry","base",tears="soft")
                m "Хм, [hermione_name]?"
                call her_main("Да?","angry","base",tears="soft")
                m "Ты больше не массируешь мой член..."
                call her_main("Ох, простите, [genie_name].","grin","worriedCl",emote="05")
                call her_main("Я запуталась...")
                call gen_chibi("handjob")
                call her_main("Но все, что я только что сказала, конечно, неправда!","open","base")
                call her_main("У меня никогда не было таких фантазий!")
                m "Верно."

            "{size=-4}\"Иногда мне становится одиноко и я даю моему псу трахнуть меня.\"{/size}":
                call her_main("Что?!","angry","wide")
                call her_main("Это отвратительно.","annoyed","suspicious")
                call her_main("Собаки - разносчики {size=+5}болезней{/size}, [genie_name].","open","closed")
                m "На самом деле, человеческие и собачьи {size=+5}болезни{/size} сильно отличаются..."
                m "Что означает, что они не смогут тебя заразить."
                call her_main("............","open","suspicious")
                m "Я слышал, кстати, что многим женщинам нравится быть \"связанными\" ."
                call her_main("В каком смысле - \"связанными\"?","normal","frown")
                m "Эм... Ну..."
                m "Не имеет значения."
                m "Просто скажи это!"
                call her_main("Ладно!","normal","base")
                call her_main("Иногда мне становится одиноко и я даю моему псу трахнуть меня.","open","suspicious")
                m "Звучит не очень..."
                call her_main("Потому что у нас даже собаки нет!","normal","frown")
                m "Ладно, неважно, продолжай массировать..."

            "{size=-4}\"-Ввести фразу-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt
                # the player to enter the name they've chosen.

                $ tmp_name = renpy.input("(Используйте клавиатуру для ввода фразы.)")

                $ tmp_name = tmp_name.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if tmp_name == "":
                    $ tmp_name="Я - шлюха."
                    call her_main("Хм...?","annoyed","worriedL")
                    call her_main("Я должна сказать \"Я - шлюха.\" как обычно?")
                if one_out_of_three == 1:
                    call her_main("Я не хочу говорить, что...","annoyed","worriedL")
                    m "Ой, просто скажи это, [hermione_name]."
                    call her_main("...........","annoyed","worriedL")
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "Хе-Хе..."
                elif one_out_of_three == 2:
                    call her_main("А?","annoyed","worriedL")
                    call her_main("Что это значит?")
                    m "Просто скажи."
                    call her_main("......","annoyed","worriedL")
                    m "Давай, это смешно."
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "Хе-хе..."
                elif one_out_of_three == 3:
                    call her_main("...........","annoyed","worriedL")
                    call her_main("Должна ли я это говорить?")
                    m "Просто скажи."
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "Хе-хе..."

        #CUMMING
        m "Хм..."
        m "Мне понравилось то, что ты делала ладонью!"
        call her_main("Вы заметили...?","angry","wink")
        call her_main("Мне продолжить?")
        call blkfade

        ">Гермиона прижимает ладошку к кончику твоего пульсирующего члена и начинает очень нежно тереть..."
        m "О да!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Вот-вот кончу. Предупредить ее?){/size}"

        menu:
            m "..."
            "\"(Да, я должен предупредить ее).\"":
                g4 "Я думаю, что уже--"
                if whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                ">Гермиона быстро поднимает рубашку..."
                ">И накрывает ею твой член..."
                ">Ощущение ее теплой кожи твоим членом провоцирует легкое головокружение ..."
                ">Гермиона переместила твой член немного выше, чем ты ожидал..."
                ">Ты чувствуешь ее, невероятно, мягкие сиськи своим членом..."

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"


                call play_music("chipper_doodle") # HERMIONE'S THEME.

                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("cumming_under_shirt")
                hide screen blktone
                call hide_blkfade
                call ctc

                $ aftersperm = True

                g4 "Ах! Ты шлюха!"
                show screen blktone
                call her_main("Да, [genie_name]! Сделайте это!","base","down")
                g4 "Ах! Ебанная шлюха!"
                call her_main("Ах! Такая горячая!","smile","glance")
                call her_main("Она повсюду! Так много!","soft","ahegao")
                call her_main("...[genie_name].")
                g4 "Ах!!!"
                m "............"
                m "Думаю, я закончил..."
                call her_main("Ах, хорошо...","angry","wink")
                call her_main("..............","base","down")
                call her_main("Вы так много накончали на меня сегодня, [genie_name]...","soft","ahegao")
                call ctc
                call blkfade

                ">Гермиона отпускает твой все еще пульсирующий член."

                hide screen chair_left
                hide screen desk
                call her_chibi("stand","desk","base")
                call gen_chibi("hide")
                show screen genie
                show screen bld1
                hide screen blkfade

                if daytime:
                    call her_main("Я думаю, сейчас мне лучше уйти... Мои занятия вот-вот начнутся.","base","base",xpos="right",ypos="base")
                else:
                    call her_main("Я думаю, сейчас мне лучше уйти... Уже поздно.","base","base",xpos="right",ypos="base")

                m "Ты пойдешь в таком виде?"
                call her_main("Что?","open","down")
                call her_main("Ох. Да, я буду в порядке...","grin","baseL")
                call her_main("Она может немного впитаться здесь и там, но я сомневаюсь, что кто-нибудь заметит.","base","happyCl")
                m "Хм... Ты могла бы положить его в свой рот и избежать этой неприятности..."
                call her_main("И проглотить, [genie_name]?","angry","wink")
                m "Зато одежда будет в чистоте."

                if whoring <= 15:
                    call her_main("Со всем уважением [genie_name]...","upset","closed")
                    call her_main("Но никак не за 45 очков...","angry","wink")
                    call her_main("Кстати, могу ли я получить свои очки?")
                else:
                    call her_main("Может в следующий раз...","angry","wink")
                    call her_main("Могу я получить свои очки?","angry","wink")

            "\"(В этом нет необходимости).\"":
                g4 "Держи, шлюха!"
                if whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                with hpunch
                g4 "АХ!"
                call blkfade

                call her_head("ЧТО?!","shock","wide")
                g4 "Держи!"

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"

                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("cumming_under_shirt")

                hide screen bld1
                call hide_blkfade
                call ctc

                $ aftersperm = True
                call her_head(".......................","angry","wide")
                call gen_chibi("cumming_on_shirt_pause")
                m "Да... Теперь я чувствую себя намного лучше ..."
                call ctc

                hide screen hermione_main
                with d3

                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                show screen bld1
                call her_main("","soft","base",tears="soft",xpos="right",ypos="base")
                call ctc
                her ".........."
                m "Ну, я думаю, что на этом все..."
                call blkfade

                call her_chibi("stand","desk","base")
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide")
                show screen genie
                call play_music("chipper_doodle") # HERMIONE'S THEME.

                hide screen blkfade
                call her_main("[genie_name]! Что вы сделали?","scream","worriedCl")

                m "Что?"
                call her_main("Вы все на меня выпустили, [genie_name]...","scream","worriedCl")
                call her_main("Как липко...","angry","down_raised")
                call her_main("[genie_name], вы должны были предупредить меня.","upset","closed")
                m "Это твоя вина, [hermione_name]!"
                call her_main("Моя вина?","angry","base")
                m "Да! Ты сделала все слишком хорошо..."
                m "Я забыл обо всем остальном..."
                call her_main("Ох...","angry","wink")
                her "Ну, что сделано, то сделано..."
                call her_main("Я просто сотру все и надеюсь, что никто не заметит...","grin","dead")
                call her_main("Могу ли я получить очки?","angry","wink")

    label done_with_handjob:

    call blkfade

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
    call her_main(trans="fade",xpos="right",ypos="base")

    m "Да, [hermione_name]. [current_payout] очков \"Гриффиндору\"."
    $ gryffindor +=current_payout

    call her_main("Спасибо, [genie_name]...","soft","baseL")

    $ hg_pf_TouchMe_OBJ.points += 1

    if whoring < 15:
        $ whoring +=1

    if whoring >= 12 and whoring < 15:
        $ new_request_16_heart = 1
        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

    if whoring >= 15 and whoring < 18:
        $ new_request_16_heart = 2
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("desk","leave",2.5)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

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


label hg_pf_TouchMe_KissSuck: #Jumps here after event #03 and if WHORING >= LEVEL 07 ### KISS SUCK! ###
    ">Гермиона стремительно кладет кончик члена себе на губы, словно хочет поцеловать его..."
    ">Это простое действие заставило твой член практически взорваться потоком спермы."

    call cum_block

    g4 "{size=+5}АХ! ДА!!!{/size}"
    call gen_chibi("handjob_kiss","desk","base")

    hide screen hermione_main
    hide screen bld1
    call hide_blkfade
    call ctc

    call bld
    call her_head("*Глоток!-Глоток!-Глоток!*")
    g4 "Ах! Ты маленькая шлюха!"
    g4 "Да, шлюха! Глотай все, без остатка!"
    her "*Глп!-Глп!-Глп!*"
    g4 "Ах... Да!"
    call nar(">Ты замечаешь, что Гермиона едва успевает заглатывать сперму.")
    her "*Глп!-Глп!-Глп!*"
    g4 "Ах..."
    g4 "Это прекрасно..."
    her "*Глп!-Глп!-Глп!*"
    m "Я думаю, что это все, [hermione_name]..."
    m "Ты можешь идти..."
    call blkfade

    hide screen chair_left
    hide screen desk
    call her_chibi("stand","desk","base")
    call gen_chibi("hide")
    show screen genie
    with d3

    call her_main("","full_cum","dead",xpos="mid",xpos="base")
    call ctc
    her "........................................."
    call her_main("Глп!!!","cum","worriedCl")
    call her_main("Гу-а-а...","open_wide_tongue","down_raised")

    hide screen blkfade
    call her_main(trans="fade",xpos="right",xpos="base")
    pause.5

    show screen bld1
    call her_main("Я все проглотила, [genie_name]!","grin","dead")
    m "Хорошая девочка..."
    call her_main("В какой-то момент я подумала, что задохнусь...","grin","dead")
    her "Ее было так много..."
    m "Что ж, дело сделано, и твоя форма не запачкалась."
    call her_main("Да! Я знаю! Так намного лучше!","base","down")

    if daytime:
        call her_main("Теперь я могу ходить на занятия, как будто ничего не случилось.","angry","wink")
    else:
        call her_main("Я могу пойти и провести некоторое время с ребятами в общей комнате, и никто не узнает...","base","down")

    m "Да... С полным желудком спермы..."
    call her_main("[genie_name]!","angry","base")
    her "...Могу я получить очки, пожалуйста, [genie_name]?"

    jump done_with_handjob
