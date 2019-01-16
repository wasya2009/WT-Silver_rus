

### Hermione Masturbates ###

label hg_pf_TouchYourself: #LV.4 (Whoring = 8 - 10)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TouchYourself_OBJ.points == 0:
        m "{size=-4}(Должен ли я попросить ее мастурбировать?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests

    $ current_payout = 40 #Used when haggling about price of the favor.

    #First time event.
    if hg_pf_TouchYourself_OBJ.points == 0:
        m "[hermione_name]..."
        call her_main("Да, [genie_name]?","base","base")
        m "Ты когда-нибудь мастурбировала себе?"
        if whoring < 8:
            jump too_much

        $ hg_pf_TouchYourself_OBJ.hearts_level = 1

        call her_main("Что?","upset","wink")
        m "Мастурбировала?"
        call her_main("[genie_name]!","scream","worriedCl")
        m "Это простой вопрос [hermione_name]..."
        call her_main("......","normal","worriedCl")
        call her_main("{size=-5}Да...{/size}","angry","worriedCl",emote="05")
        m "А? Что?"
        call her_main("Я сказала, что да!!!","scream","worriedCl")
        m "Хмммм, я не верю тебе..."
        call her_main("Что? Почему я должна вам врать?","annoyed","worriedL")
        m "Я не уверен..."
        m "Но не волнуйся, я уверен, что небольшая демонстрация устранит любые сомнения..."
        call her_main("...{p}И сколько принесет мне эта демонстрация?","annoyed","suspicious")

        menu:
            "\"Ты получишь 20 очков.\"":
                $ current_payout = 20
                call her_main("......","annoyed","angryL")
                call her_main("Хорошо, полагаю, я могу.","open","down")
                call her_main("Но вы лучше держите себя в руках...","open","down")
                m "Слово Ведьмака."
                call her_main("...","annoyed","suspicious")
            "\"Ты получишь 40 очков.\"":
                $ current_payout = 40
                call her_main(".....","base","base")
                call her_main("40...?","soft","baseL")
                her "Это поможет \"Гриффиндору\" вернуться на лидирующую позицию..."
                m "Это значит \"да\"?"
                call her_main("Да, [genie_name].","base","squint")
                m "Прекрасно!"
            "\"Ты получишь 80 очков!\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ current_payout = 80 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("80 очков?!","scream","wide_stare")
                m "Этого достаточно?"
                call her_main("Конечно [genie_name]!","smile","happyCl")
                call her_main("Если это для Гриффиндора 80 очков, то я не против показать вам немного этого...","smile","happyCl",emote="06")

        call play_music("playful_tension") # SEX THEME.
        call her_main("...........","upset","wink",xpos="mid",ypos="base",trans="fade")
        call her_main("Вы хотите, чтобы я ... начала?","upset","wink")
        m "Может, сначала снимешь рубашку..."
        call her_main("...","angry","worriedCl",emote="05")
        call her_main("Вы хотите, чтобы я разделась для вас, и...","angry","worriedCl",emote="05")
        m "Я дам 10 дополнительных очков \"Гриффиндору\"."
        $ current_payout += 10
        call her_main("Хорошо... {p}но я оставляю свою юбку...","upset","wink")
        hide screen bld1
        with d3

        call set_hermione_action("lift_top")
        pause.5

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("...........","upset","wink")
        m "Мммм, вот и все, [hermione_name]..."

        call her_main("(Не могу поверить, что собираюсь это сделать...)","normal","worriedCl")


        call set_hermione_action("covering_top")
        call ctc

        call play_music("playful_tension") # SEX THEME.
        call nar(">Гермиона начинает медленно мастурбировать.")
        g9 "Хорошо..."
        call her_main("........","upset","wink")
        m "............."
        call her_main(".............","normal","worriedCl")
        call her_main("Эм... [genie_name]?")
        m "Да, что такое?"
        call her_main("Как долго мне это делать?","open","base")
        m "Пока ты не кончишь [hermione_name]..."

        if daytime:
            call her_main("Что? Мои занятия вот-вот начнутся [genie_name]...","upset","wink")
        else:
            call her_main("Что? уже довольно поздно [genie_name]...","upset","wink")

        call her_main("Я не уверена, смогу ли я закончить... вовремя.","upset","wink")
        m "Тебе нужны очки или нет?"
        call her_main("Нужны, [genie_name]! Простите...","open","down")
        call her_main("Я тогда просто продолжу...","disgust","down_raised")
        m "(Хм, мне, возможно, придется немного помочь ей.)"

        #MAIN FAVOUR MENU
        label TouchYourself_menu:
        menu:
            m "..."
            "\"Вот именно шлюха, продолжай.\"":
                call her_main("[genie_name]!!!","angry","angry")
                call her_main("Как вы смеете!")
                m "Что?"
                call her_main("Я не думаю, что такие слова подходят.","upset","wink")
                m "А мастурбировать перед директором?"
                call her_main("Ну... это другое.","open","down")
                call her_main("Я делаю это ради чести \"Гриффиндора\"...")
                call her_main("Чтобы помочь моему--")
                call nar(">Ты заметил, как она начинает ускоряться.")
                $ hermione_dribble = True
                call her_main("Ах...{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
                call her_main("Мои одноклассники выигрывают кубок...","angry","wink")
                m "Ты уверена, что это единственная причина, шлюха?"
                call her_main("Я не знаю--","normal","worriedCl")
                call her_main("Ах-a{image=textheart}...","open","worriedCl")
                call her_main("Я не знаю, что вы имеете в виду, [genie_name]...","angry","down_raised")
                m "Мне кажется, что тебе это слишком нравится..."
                call her_main("Нет, [genie_name]!","open","worriedCl")
                m "Правда?"
                call her_main("......................","normal","worriedCl")
                m "Тогда почему твоя киска такая мокрая, шлюха?"
                call ctc

                call her_main("Ах...{image=textheart}","open","worriedCl")
                m "Ха! Просто признайся, тебе нравится, когда тебя называют шлюхой!"
                call her_main("Нет!","normal","worriedCl")
                call her_main("Aхa...{image=textheart}","open","worriedCl")
                call her_main("Я просто думаю о том, как все будут счастливы, когда мы победим!","shock","worriedCl")
                m "А что делать, если они узнают, как ты заработала очки?"
                call her_main("Что?!","shock","wide")
                m "Тогда не только твои одноклассники будут унижать тебя..."
                call her_main("...","soft","squintL")
                m "Это будет и вся школа."
                call her_main("Ах...{image=textheart}","silly","dead")
                m "Маленькая. Мисс. Шлюха."
                call her_main("Ах...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
                call her_main("[genie_name], пожалуйста... никому не говорите...","angry","wink")
                call nar(">Гермиона держит руками свои бедра...")
                call her_main("Они не должны узнать...","angry","base")
                call her_main("Если бы Гарри и Рон узнали...","angry","down_raised")
                call her_main("Я... aх...{image=textheart}","soft","ahegao")
                m "Что ты [hermione_name]?"
                call her_main("Я...","open","worriedCl")
                call her_main("Я...{image=textheart}","shock","worriedCl")
                call her_main("Я...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")

            "\"Трогай свои сиськи\"" if hg_pf_TouchYourself_OBJ.points > 0:
                call her_main("Мои сиськи...","open","down")
                call set_hermione_action("covering_top")

                call her_main("Я не уверена, должна ли я--","clench","down_raised")
                m "Я дам дополнительно 10 очков \"Гриффиндору\"..."
                $ current_payout += 10
                call her_main("...","soft","squintL")
                call her_main("......","soft","squintL")
                call set_hermione_action("lift_breasts")

                call her_main("Ах...{image=textheart}","open","baseL")
                m "Так... Разве вот так не лучше?"
                $ hermione_dribble = True
                call her_main("Aх... д-да...{image=textheart}","grin","ahegao")
                call h_action("covering_top")
                call her_main("Мммм...","smile","happyCl")
                m "Вот и все..."
                call h_action("lift_breasts")
                call her_main("[genie_name], вы не возражаете...","base","ahegao_raised")
                m "Что [hermione_name]?"
                call her_main("Могли бы вы... называть меня...","open","ahegao_raised",cheeks="blush")
                m "Например?"
                call set_hermione_action("covering_top")

                call her_main("...{p}{size=-5}Шлюхой...{/size}{p}Только если вы хотите...","base","ahegao_raised",cheeks="blush")
                m "Ты маленькая шлюха..."
                call her_main("Aх...{image=textheart}{image=textheart}","grin","ahegao")
                m "Что подумают твои родители, если увидят это?"
                call her_main("Я-{image=textheart}","base","ahegao_raised",cheeks="blush")
                call set_hermione_action("lift_breasts")

                call her_main("Aх...{image=textheart} я не знаю...","base","ahegao_raised",cheeks="blush")
                call her_main("Если быть честной [genie_name]... Я не думаю, что это меня волнует...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")
                m "Правда?"
                call set_hermione_action("covering_top")

                call her_main("Правда...{image=textheart}","silly","ahegao_raised",cheeks="blush")
                m "Ты можешь остановиться?"
                call her_main("Aх...{image=textheart}","open_tongue","ahegao_raised",cheeks="blush")
                call set_hermione_action("lift_breasts")

                call her_main("Может быть....","open_tongue","ahegao_raised",cheeks="blush")
                call her_main("Я не уверена...","open","baseL",cheeks="blush")
                call set_hermione_action("covering_top")

                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")

            "\"Сними юбку\"" if hg_pf_TouchYourself_OBJ.points > 0:
                call her_main("Простите?","soft","wide")
                m "Ты слышала, что я сказал, [hermione_name]..."
                call her_main("........","annoyed","angryL",cheeks="blush")
                call her_main("............","disgust","down_raised",cheeks="blush")
                call her_main("*Вздох!*..............","open","ahegao_raised",cheeks="blush")
                call her_main("Ну, я могу...")
                call nar(">Гермиона прекращает мастурбировать и медленно снимает юбку.")

                $ hermione_wear_bottom = False
                call set_hermione_action("covering")

                call her_main("...","open","down")
                m "Все не так уж и плохо, не так ли?"
                call her_main("Нет, я думаю нет...","upset","wink")
                m "Ну, тогда продолжай..."
                call her_main("...","normal","worriedCl")
                call her_main("Хорошо...","base","ahegao_raised",cheeks="blush")
                m "Хорошо... Просто продолжай играть со своей похотливой маленькой киской!"
                call her_main("[genie_name]!","mad","angry",cheeks="blush")
                m "Что?"
                $ hermione_dribble = True
                call her_main("Она не {size=-5}похотливая...{/size}","annoyed","angryL",cheeks="blush")
                m "Ты уверена? Там где я сижу, она выглядит красиво и мокро."
                call her_main("Aх...{image=textheart}","base","ahegao_raised",cheeks="blush")
                call her_main("Это просто пот [genie_name]...","open","baseL",cheeks="blush")
                m "Что ты говоришь..."
                call her_main("...............","base","ahegao_raised",cheeks="blush")
                m "{size=-5}Шлюха.{/size}"
                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")
                call her_main("Сэр... пожалуйста...","open","baseL",cheeks="blush")
                call set_hermione_action("pinch")

                call nar(">Гермиона начинает нежно мастурбировать.")
                m "Очень хорошо..."
                call her_main("...{image=textheart}","silly","ahegao_raised",cheeks="blush")
                call her_main("Ах...{image=textheart}","open_tongue","ahegao_raised",cheeks="blush")
                m "Вот так шлюха. Попробуй засунуть глубже...."
                call her_main("...","open_tongue","ahegao_raised",cheeks="blush")
                call set_hermione_action("covering")

                call her_main("Мммм...{image=textheart}","scream","worriedCl",cheeks="blush")


        if hg_pf_TouchYourself_OBJ.points == 0: #HERMIONE DOESN'T CUM
                call her_main("Aх...","shock","baseL",cheeks="blush",tears="soft")
                m "Ты уже скоро [hermione_name]?"
                call her_main("П-почти...","clench","worried",cheeks="blush",tears="soft")
                call her_main("Мне нужно чуть больше времени...")
                m "Ну, тебе лучше поторопиться..."
                call her_main("Aх... я знаю, [genie_name].","mad","worriedCl",tears="soft_blink")
                call her_main("...........","shock","baseL",cheeks="blush",tears="soft")
                m "Все в порядке?"
                call her_main("................","shock","down_raised",cheeks="blush",tears="crying")
                m "Почему ты молчишь? [hermione_name]?"
                call her_main("......","clench","worried",cheeks="blush",tears="soft")
                call her_main("[genie_name]... Не думаю, что смогу...")
                m "Что?"
                call her_main("...закончить...","angry","dead",cheeks="blush",tears="crying")

                menu:
                    "-Наказать-":
                        m "Ну тогда я думаю \"Слизерин\" выйграет кубок в этом году."
                        call her_main("Н-но--","scream","wide")
                        m "Ну, [hermione_name], уговор срывается."
                        call her_main("Серьезно?","open","worriedCl")
                        call her_main("Но я пыталась [genie_name]...","shock","worriedCl")
                        m "Постарайся..."
                        call nar(">Гермиона начинает яростно мастурбировать")
                        call her_main("*Плачет!* Я не могу...","shock","down_raised",cheeks="blush",tears="crying")
                        m "Тогда, 0 очков \"Гриффиндору\"..."
                        call her_main("{size=-5}После этого...{/size} Серьезно [genie_name]?","clench","worried",cheeks="blush",tears="soft")
                        call her_main("После того, как я стояла здесь и...","scream","angry",cheeks="blush",tears="messy")
                        call her_main("..........","angry","suspicious",cheeks="blush",tears="messy")
                        call nar(">Гермиона вытирает слезы с глаз.")
                        call her_main("Я больше не собираюсь продавать вам ни одной услуги., [genie_name]!","angry","angry",cheeks="blush")

                        $ mad += 15
                        jump end_touch_yourself

                    "-Простить-":
                        m "Все в порядке, [hermione_name]."
                        call her_main("Правда?","open","surprised",cheeks="blush",tears="messy")
                        m "Уверен, ты просто немного перенервничала.."
                        call her_main("Спасибо [genie_name].","clench","worried",cheeks="blush",tears="soft")
                        call her_main("Я обещаю постараться в следующий раз.","scream","worriedCl",cheeks="blush",tears="messy")

        else: #HERMIONE CUMS
            $ hg_pf_TouchYourself_OBJ.hearts_level = 2
            call her_main("A-хa... {image=textheart}ах...","open","worriedCl")
            call her_main("Aх... {image=textheart}-аха...","open","worriedCl")
            m "..."
            call her_main("Aх-aх...","open","worriedCl")
            m "......................"
            call her_main("Aх... ах...{image=textheart}","open","worriedCl")
            call her_main("Aх... [genie_name]?","soft","squintL")
            m "Что такое?"
            call her_main("Aх... вам.... нравится?","open","worriedCl")
            m "Нравится ли мне смотреть, как ты мастурбируешь свою распутную маленькую киску?"
            m "Очень, [hermione_name]. А что?"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","normal","worriedCl")
            call her_main("Aх... Вы молчите...","open","worriedCl")
            m "Тебе нужна поддержка?"
            call her_main("Aх... да... пожалуйста....{image=textheart}","open","worriedCl")
            m "Tch... Ты противная шлюха!"
            call her_main("Да [genie_name], aх...{image=textheart}","grin","ahegao_mad",cheeks="blush")
            call her_main("Пожалуйста... aх... еще...{image=textheart}","grin","angry",cheeks="blush")
            g4 "Ты должна быть наказана за то, что ты такая шлюха!"
            call her_main("Да, [genie_name]... накажите меня...","open","ahegao_raised",cheeks="blush")
            call her_main("Сделайте меня своей маленькой шлюхой....","open","ahegao_raised",cheeks="blush")
            call her_main("Я сейчас... aх... {image=textheart}сделаю кое-что... aх...{image=textheart}","silly","dead")
            m "Что [hermione_name]?"
            call her_main("Ах-a...{image=textheart} дааа...","silly","ahegao_raised",cheeks="blush")
            m "Кончаешь?"
            $ hermione_squirt = True
            call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","silly","dead",cheeks="blush")

            call cum_block

            $ hermione_squirt = False
            call her_main("Aх...{image=textheart}...{image=textheart}","grin","ahegao")
            call her_main("Aх... aх...{image=textheart}","silly","ahegao")
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
            call her_main("*Тяжелое дыхание*","open_wide_tongue","ahegao")
            call her_main("[genie_name]...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
            call her_main(".............","soft","ahegao")
            call nar(">Гермиона берет минутку, чтобы привести себя в порядок.")
            m "Ты себя хорошо чувствуешь?"
            call her_main("Да, [genie_name]... мне нужно еще немного времени...","shock","baseL",cheeks="blush",tears="soft")
            m "Хорошо."
            call her_main("Ах... {image=textheart}","silly","worried",cheeks="blush",tears="soft")

    #Second time event.
    elif hg_pf_TouchYourself_OBJ.points == 1: # SECOND EVENT
        m "[hermione_name]..."
        call her_main("Да, [genie_name]?","base","base")
        m "Ты возбуждена?"
        call her_main("Может немного, [genie_name].","base","glance")
        m "A, хорошо, возможно, мы можем это исправить..."
        call her_main("[genie_name]...","open","worriedCl")
        m "[hermione_name], я бы хотел купить у тебя одну услугу."
        call her_main("Конечно, [genie_name].","base","down")
        g9 "Я хочу что бы ты поиграла со своей распутной маленькой киской!"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
        call her_main(".............","soft","ahegao")
        call her_main("Хорошо...","base","down")

        call her_main("","base","glance",xpos="mid",ypos="base",trans="fade")
        call set_hermione_action("lift_top")
        pause.5

        call her_main("...........","upset","wink")
        m "Мммм, вот так [hermione_name]..."

        call her_main("(Не могу поверить, что собираюсь это сделать... снова...)","angry","down_raised")
        call set_hermione_action("covering_top")
        call ctc

        call play_music("playful_tension") # SEX THEME.
        call nar(">Гермиона начинает медленно мастурбировать.")
        g9 "Отлично..."
        call her_main("........","grin","ahegao")


        jump TouchYourself_menu


    #Third time event.
    elif hg_pf_TouchYourself_OBJ.points >= 2:
        $ hg_pf_TouchYourself_OBJ.hearts_level = 3 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base")
        m "Ты не против сегодня ублажать себя передо мной?"
        if whoring <= 16:
            call her_main("Пока вы начисляете очки...","grin","baseL")
            m "Ну, начинай. Время, чтоб заработать очки."
        else:
            call her_main("Я уже это делала сегодня...","grin","baseL")
            m "Тогда, еще раз на удачу!"
            call her_main("Если вы настаиваете...{image=textheart}","open","baseL",cheeks="blush")

        call her_main("","base","glance",xpos="mid",ypos="base",trans="fade")
        call set_hermione_action("lift_top")
        pause.5

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("(Я не могу поверить, что я делаю это... снова...)","base","baseL",cheeks="blush")
        m "Теперь юбка."

        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("...","base","glance")
        call set_hermione_action("covering")

        stop music fadeout 3.0
        call her_main("Вам нравится, когда я делаю это, [genie_name]?","grin","baseL")
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        m "Да, да, нравится..."
        m "Попробуй немного глубже."
        call her_main("Хорошо [genie_name]...","base","happyCl")
        $ hermione_dribble = True
        call her_main("Aх... aх...{image=textheart}","open","worriedCl")
        call her_main("Aх... [genie_name]...{image=textheart}","open","worriedCl")

        menu:
            m "..."
            "\"О чем ты думаешь?\"":
                call her_main("А?","open","worriedCl",cheeks="blush")
                call her_main("Oх, эм... ни о чем...","upset","worriedCl",cheeks="blush")
                m "[hermione_name]..."
                call her_main("[genie_name], пожалуйста, это слишком неловко...","disgust","down_raised",cheeks="blush")
                g4 "Ну, теперь я должен это услышать."
                call her_main("Хорошо... но вы обещайте, что никому не расскажете!","open","baseL",cheeks="blush")
                m "Слово Ведьмака."
                call her_main("......","annoyed","annoyed")
                m "[hermione_name]..."
                call her_main("Хорошо. Если вы хотите знать... Я помню, как я поправила профессора Снейпа по ингредиентам Hiccoughing (икающего) зелья .","open","down")
                m "....."
                call her_main("Ах...{image=textheart}","soft","ahegao")
                call set_hermione_action("pinch")

                call her_main("Это было... ах... {image=textheart} перед всем классом.")
                call set_hermione_action("covering")

                call her_main("Он отказывался отвечать мне на любые вопросы в течение недели, после того случая.","base","down")
                call her_main("Но это стоило того...","soft","squintL")
                call her_main("Этот взгляд на его лице, когда он понял, что ошибается...{image=textheart}","soft","ahegao")
                call set_hermione_action("pinch")

                call her_main("А-aх...{image=textheart}")
                call set_hermione_action("covering")

                call her_main("Это было так хорошо!{image=textheart}","grin","dead")
                m "Хорошо, думаю, этого достаточно..."
                call her_main("Это было слишком?","angry","wink")
                m "Давай просто вернемся к делу?"
                call her_main(".................","soft","ahegao")
                call nar(">Гермиона продолжает засовывать в себя пальчики.","start")
                call nar(">Она отлично справляется с этим.","end")
                m "Да, да... мне нравится."

            "\"Ты действительно бесстыжая шлюха, не так ли?\"":
                call her_main("Да...","soft","ahegao")
                call set_hermione_action("pinch")

                call her_main("Ах... {image=textheart}","silly","dead")
                call her_main("Я не знаю, сколько времени я провожу с вами...{image=textheart}","angry","wink")
                call her_main("Или, если я всегда буду такой...{image=textheart}","angry","down_raised")
                call her_main("Но... {image=textheart} aх... {image=textheart} я шлюха [genie_name]...{image=textheart}","soft","ahegao")
                call her_main("Бесстыжая шлюха...","grin","dead")
                call her_main("Меня радует то...{image=textheart} aх...","soft","ahegao")
                call her_main("Что сделает директора счастливыми...","grin","dead")
                m "Oх, да..."
                call her_main("Вот так [genie_name]...","base","down")
                call her_main("Наслаждайтесь, пока я стою здесь....","silly","dead")
                call her_main("Aх...{image=textheart}","open_wide_tongue","ahegao")
                call her_main("Я мастурбирую свою киску...","silly","ahegao")
                call her_main("Aх... aх...{image=textheart}","grin","ahegao")
                call her_main("Aх... Вам.... нравится [genie_name]?","shock","worriedCl")
                call her_main("Смотреть на меня... Aх...{image=textheart} как я унижаю себя?","silly","dead")
                m "Очень, [hermione_name]. Просто продолжай..."
                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","dead")

            "\"Играй со своими сиськами!\"":
                call her_main("Хм?","soft","ahegao")
                call her_main("Хорошо... если вы настаиваете...","open","baseL",cheeks="blush")
                call set_hermione_action("pinch")

                call her_main("Ах...{image=textheart}","angry","wink")
                m "Теперь подними их."
                call her_main("[genie_name]...","open","squint",cheeks="blush")
                m "Сделай это, [hermione_name]."
                call her_main("...","open","baseL",cheeks="blush")
                call set_hermione_action("lift_breasts_naked")

                call her_main("Мммм...","grin","ahegao_mad",cheeks="blush")
                m "Вот и все..."
                call nar(">Ты с возбуждением смотришь на грудь Гермионы...")
                call her_main("Ах...","silly","dead")
                m "Так тебе нравится играть со своими сиськами, [hermione_name]?"
                call her_main("Да, [genie_name]... aх...{image=textheart}","soft","ahegao")
                call her_main("Я не знаю почему...","base","baseL",cheeks="blush")
                call set_hermione_action("pinch")

                call her_main("Но, я люблю их...{image=textheart}{image=textheart}","base","down")
                m "Ты грязная шлюха!"
                call her_main("Aх...{image=textheart} Ах-a...{image=textheart}","open_wide_tongue","ahegao")
                call her_main("Я...")
                call her_main("Грязная шлюха... Aх...{image=textheart}","silly","dead")
                m "Ты позорище, [hermione_name]!"
                call her_main("Aх-aх...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")

        m "Почему бы тебе не подойти поближе?"
        call her_main("...","base","down")

        call her_walk_desk_blkfade

        ">Гермиона медленно подошла к твоему столу и стоит перед тобой."

        show screen desk
        show screen chair_left
        hide screen genie
        $ genie_chibi_xpos = -217
        $ genie_chibi_ypos = 13
        $ g_c_u_pic = "images/animation/grope_e_01.png"
        show screen g_c_u

        hide screen blktone
        hide screen bld1
        call hide_blkfade
        call ctc

        call set_hermione_action("lift_breasts_naked")
        call her_main("..............","base","ahegao_raised",cheeks="blush")

        menu:
            m "..."
            "-Схватить сиськи-":
                call nar(">Ты протягиваешь руки вперед и хватаешь ее за упругую грудь.")
                $ g_c_u_pic = "groping_naked_tits_ani"
                call set_hermione_action("fingering")

                call her_main("[genie_name]!","shock","worriedCl")
                call her_main("Это не было частью сделки!","open","worriedCl")
                call her_main("Я не думаю, что мы должны...","annoyed","angryL",cheeks="blush")
                m "Не волнуйся [hermione_name], ты можешь продолжать играть с собой."
                m "Это надо, чтобы быстрее закончить."
                call her_main("Aх...{image=textheart} ну, главное, чтобы все закончилось быстрее...","open","ahegao_raised",cheeks="blush")
                call her_main("Я полагаю, что могу... aх{image=textheart} позволить вам...","base","baseL",cheeks="blush")
                call nar(">Ты пару раз сжимаешь сиськи Гермионы...")
                m "Просто признайся, что тебе это нравится."
                call her_main("Aх... ладно...{image=textheart}","open","worriedCl",cheeks="blush")
                call her_main("{size=-5}Мне нравится это...{/size}","soft","ahegao")
                m "Что, [hermione_name]?"
                call her_main(".......")
                call her_main("Я люблю...","grin","dead")
                call her_main("Стоять здесь... мастурбировать...","base","down")
                call her_main("Aх... пока вы трогаете мои...{image=textheart}","grin","ahegao_mad",cheeks="blush")
                m "Хех... Отлично."
                call her_main("Aх...{image=textheart}","open","ahegao_raised",cheeks="blush")
                call her_main("Иногда мне хочется провести здесь весь день....","grin","angry",cheeks="blush")
                m "Мммм"
                call nar(">Ты продолжаешь массировать ее грудь...")
                call her_main(".......")
                call her_main("[genie_name]... Я знаю, что я много хочу...","base","baseL",cheeks="blush")
                call her_main("Ах...{image=textheart}","base","down")
                call her_main("Но не могли бы вы прикоснуться... там...","open","squint",cheeks="blush")
                m "Чего [hermione_name]?"
                call her_main("Пожалуйста, дотроньтесь...","open","ahegao_raised",cheeks="blush")
                m "Еще раз, громче."
                call her_main("Aх...{image=textheart} {size=+5}пожалуйста, дотроньтесь до моей пизды!{/size}","grin","ahegao_mad",cheeks="blush")
                $ g_c_u_pic = "groping_06"
                call nar(">Ты быстро засовываншь два пальца в ее мокрую киску.")
                call h_action("lift_breasts_naked")
                call her_main("{image=textheart}{image=textheart}{size=+5}!!!{/size}{image=textheart}{image=textheart}","silly","ahegao")

            "-Засунуть пальцы-":
                $ g_c_u_pic = "groping_06"
                call nar(">Ты начинаешь гладить ноги Гермионы...")
                call her_main("!!!","open","worriedCl")
                call nar(">И медленно двигаешь руками к ее киске...")
                call her_main(".................","silly","dead")
                m "Вот так [hermione_name]..."
                call her_main("{size=-7}[genie_name]...{/size}","soft","ahegao")
                m "Тсс. Просто играй с сиськами."
                call her_main("...Ладно, [genie_name]...","base","ahegao_raised",cheeks="blush")
                m "Хорошая девочка."
                call her_main("....................","base","closed")
                m "Будь тихой..."
                call nar(">Ты наслаждаешься ощущением, нежно поглаживая внутреннюю часть ее бедер...")
                m "Когда мои руки исследуют тебя"
                m "Твои бедра..."
                call nar(">Ты начинаешь подниматься выше по ее бедрам, двигаясь все ближе к ее мокрой киске")
                m "Твоя большая, упругая попка"
                call nar(">Ты нежно сжимаешь ее задницу...")
                call her_main(".....................","grin","ahegao")
                m "Твой лобок..."
                call nar(">Ты кладешь руку чуть выше клитора и начинаешь гладить.")
                call her_main(".....................{size=-8}[genie_name]...{/size}","silly","dead")
                m "Что такое, [hermione_name]?"
                call her_main(".....................","annoyed","wink",cheeks="blush")
                call her_main("...Я... {size=-5}...Я хочу вас... Засуньте в меня...{/size}","disgust","down_raised",cheeks="blush")
                m "Тебе придется говорить громче, если ты ждешь, что я тебя услышу..."
                call her_main("Я... aх...{image=textheart} хочу...","open","ahegao_raised",cheeks="blush")
                call nar(">Ты стремительно вонзаешь два пальца в ее промокшую пизденку.")
                call her_main("!!!{image=textheart}{image=textheart}","grin","ahegao")
                call nar(">Ты начинаешь двигать пальцами внутри нее, прежде чем она успевает ахнуть")
                call her_main("{size=+10}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}","silly","dead")
                m "Вот и все [hermione_name]. Наслаждайся."
                call her_main("..................................................","base","ahegao_raised",cheeks="blush")
                m "Тебе нравится?"
                m "Тебе нравится, когда мои пальцы в твоей пизде?"
                call her_main("Мне нравится!{image=textheart} Мне нравятся ваши пальцы в моей тугой, влажной киске!!{image=textheart}","silly","ahegao")
                m "Ну, я думаю, мы можем сделать лучше."
                call nar(">Другой рукой ты начинаешь тереть ладонью ее клитор.")
                call her_main("{size=+10}!!!{/size}","open","ahegao_raised",cheeks="blush")


        call nar(">Тебе даже не приходиться шевелить руками, она почти все делает сама.")
        call her_main("Ах...{image=textheart} пожалуйста...{image=textheart} не останавливайтесь...{image=textheart}","silly","dead","blush")
        call her_main("Вставьте еще один! {image=textheart}{image=textheart}","silly","ahegao","blush")
        g9 "Как пожелаешь!"
        call nar(">Ты засовываешь еще один палец в ее киску!")
        call her_main("Ах... да... {image=textheart}мне нравится, мне нравится!","grin","ahegao","blush")
        m "Что ты любишь, [hermione_name]?"
        call her_main("Ах!!{image=textheart} Я люблю, когда ваши пальцы находятся во мне [genie_name]!{image=textheart}","open_wide_tongue","ahegao","blush")
        call nar(">Ее движения становятся все более неистовыми")
        m "Ты кончаешь, [hermione_name]?"
        call her_main("Ах...{image=textheart} да!!","grin","ahegao")
        call her_main("Я кончаю [genie_name]!!{image=textheart}","grin","dead")
        call her_main("Я кончаю от ваших гребанных пальцев!!{image=textheart}{image=textheart}","grin","ahegao_mad",cheeks="blush")
        m "Покажи сиськи [hermione_name]!"
        m "Я хочу, чтобы ты кончила, играясь с ними."
        $ hermione_squirt = True
        call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","silly","dead",cheeks="blush")

        call cum_block

        $ hermione_squirt = False
        call her_main("Aх...{image=textheart}...{image=textheart}","grin","ahegao")
        call her_main("Aх... aх...{image=textheart}","silly","ahegao")
        call her_main("...........","silly","ahegao")
        call her_main("........................","silly","ahegao")
        call nar(">Ты отпускаешь ее...")
        $ g_c_u_pic = "images/animation/grope_e_01.png"
        m "Это было для тебя [hermione_name]."


    label end_touch_yourself:
    hide screen hermione_main
    call blkfade
    ">Гермиона быстро надевает свою одежду."

    call h_action("none") #Resets clothes.

    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base")
    pause.1

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    pause.5

    if whoring < 19:
        call her_main("Что насчет моих очков?","scream","surprised",cheeks="blush",tears="messy",xpos="right",ypos="base")
        m "Да, да, [hermione_name]. [current_payout] очков \"Гриффиндору\"."
        $ gryffindor +=current_payout

    call her_main("Спасибо, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if whoring < 14: #Adds points till 14.
        $ whoring +=1

    $ hg_pf_TouchYourself_OBJ.points += 1

    if hg_pf_TouchYourself_OBJ.points == 1:
        $ new_request_16_heart = 1
        $ hg_pf_TouchYourself_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_TouchYourself_OBJ.points == 2:
        $ new_request_16_heart = 2
        $ hg_pf_TouchYourself_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_TouchYourself_OBJ.points == 3:
        $ new_request_16_heart = 3
        $ hg_pf_TouchYourself_OBJ.hearts_level = 3 #Event hearts level (0-3)


    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
