

label hg_pf_TitJob: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TitJob_OBJ.points == 0:
        m "{size=-4}(Должен ли я попросить ее поработать сиськами?){/size}"
    else:
        g9 "{size=-4}(Я чувствую, как ложу член между ее сисек!){/size}"

    if hg_pf_TitJob_OBJ.points < 1:
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    if hg_powerGirl_OBJ.purchased:
        m "\"(Должен ли я попросить ее переодеться?)\""
        menu:
            "\"(Да, давай!)\"":
                m "[hermione_name], прежде чем я попрошу об услуге, ты должна переодеться."
                call her_main("Во что?","open","worriedL")
                m "В Super Girl."
                if whoring >= 18:
                    call her_main("Типо, в супергероя?","annoyed","annoyed")
                    m "Что-то не так?"
                    call her_main("...","upset","wink")
                    call her_main("Нет, я имею в виду, если это сохранит мою форму чистой...","annoyed","worriedL")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_powerGirl_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Нет, не сейчас.)\"":
                pass

    $ current_payout = 45 #Used when haggling about price of th favor.

    call bld

    #First Event.
    if hg_pf_TitJob_OBJ.points == 0:
        m "[hermione_name]."
        call her_main("Да, [genie_name]?","base","base",xpos="right",ypos="base")
        m "Ты когда-нибудь давала играть со своими сиськами?"

        if whoring < 15:
            jump too_much

        call her_main("Играть с сиськами?","annoyed","annoyed")
        m "Это когда ты оборачиваешь своими сиськами член, а затем трясешь ими, вверх и вниз...."
        call her_main("[genie_name]!","angry","angry")
        m "Так ты когда-нибудь делала это?"
        call her_main("......","disgust","glance")
        call her_main("{size=-7}Нет...{/size}","angry","worriedCl",emote="05")
        m "Хммм? Что?"
        call her_main("Нет!!!","scream","worriedCl")
        m "Ну, сегодня тебя удача не обошла стороной!"
        call her_main("Удача? Вы это называете *Удача*?","disgust","glance")
        m "Ведь вы не каждый день узнаете, что-то новое."
        call her_main("Я учусь в школе! Это моя работа-узнавать, что-то новое!","scream","angryCl")
        m "По крайней мере, это то, что ты сможешь использовать в жизни."
        call her_main("......","disgust","glance")
        call her_main("{size=-7}Я хочу 100 очков...{/size}","angry","worriedCl",emote="05")
        m "Громче [hermione_name]."
        call her_main("Я хочу 100 очков!","scream","worriedCl")

        label back_to_titjob_choices:
        menu:
            m "..."
            "\"Я дам тебе 15 очков и обещаю не кончать на тебя.\"":
                $ mad +=7
                call her_main("Вы ожидаете то, что я потрясу сиськами за 15 очков?!","annoyed","angryL")
                her "Я не знаю, что обо мне вы думаете, но я не собираюсь это делать за 15 очков!"
                call her_main("(Кроме того, я не против, если вы кончите...)","annoyed","angryL")
                jump back_to_titjob_choices
            "\"Я дам тебе 45 очков.\"":
                if mad > 7: #You could spam points into infinity with the choice above.
                    $ mad = 7
                call her_main(".....","annoyed","angryL")
                call her_main("45 очков...?","open","down")
                her "Это поможет \"Гриффиндору\" вернуться в лидеры..."
                m "Это значит \"да\"?"
                call her_main("Да, да, [genie_name].","annoyed","annoyed")
                m "Отлично!"
            "\"Я дам тебе 100 очков.\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 очков?!","scream","wide_stare")
                her "Это намного быстрее продвинет \"Гриффиндор\" в лидеры!"
                m "Так что, да?"
                call her_main("Конечно!","smile","happyCl")
                call her_main("За 100 очков я сделаю вашу жизнь - незабываемой!","smile","happyCl",emote="06")

        # GENIE STANDS WITH HIS COCK OUT
        hide screen hermione_main
        hide screen bld1
        call blkfade

        call play_music("playful_tension") #HERMIONE
        hide screen genie
        show screen chair_left
        show screen desk
        call her_chibi("stand","mid","base")
        call gen_chibi("hold_dick","desk","base")
        call hide_blkfade
        call ctc

        show screen bld1
        call her_main("...........","open","base")
        call her_main("(Он такой большой...)","base","down")
        m "Возьми его [hermione_name]."
        call her_main("Хорошо...","angry","worriedCl",emote="05")
        call her_main("","annoyed","annoyed")
        pause.2

        #First and Second Event.
        label titjob_round_2:

        #Hermione removes her top.
        $ hermione_wear_bra = False
        call set_hermione_action("lift_top")
        pause.5

        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update")
        pause.5

        hide screen hermione_main
        hide screen bld1
        call blkfade
                                                                                                                                                                                       #HERMIONE
        hide screen genie
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide")
        call gen_chibi("titjob","mid","base")

        if hermione_costume:
            call h_action("lift_top")
        else:
            call h_action("lift_breasts")

        if use_cgs:
            $ ccg_folder = "herm_boob"
            $ ccg1 = 5
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            show screen ccg
            with d3

        call nar(">Гермиона неуклюже обертывает сиськи вокруг члена...")
        m "Это только начало. Теперь вверх и вниз..."
        call her_head("Хорошо...","angry","worriedCl",emote="05",xpos="base",ypos="high")
        hide screen bld1
        call hide_blkfade
        call ctc

        call play_music("playful_tension") # SEX THEME.
        call bld
        g9 "мммм..."
        $ ccg1 = 6
        if hg_pf_TitJob_OBJ.points == 0:
            call her_head("...","base","base")
            call her_head("У меня получается... ? Вам хорошо?","base","squint")
            m "Хорошо?"
            m "Это великолепно."
            call her_head("Ох...","base","squint")
            call her_head("......")
            call her_head("Спасибо [genie_name]","base","baseL")

        call her_head("[genie_name]...?","soft","base")
        m "Что такое?"
        $ ccg1 = 7
        call her_head("Обещайте, что вы не кончите мне на... лицо.","upset","wink")

        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Обещаю...\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                $ ccg1 = 6
                call her_head("Спасибо, [genie_name].","base","squint")
            "\"Хммм... Посмотрим...\"":
                $ ccg1 = 8
                call her_head("Пффф.","annoyed","annoyed")
                call her_head("Хотя бы не на волосы...","normal","worriedCl")

        $ ccg1 = 5
        call her_head("........","open","base")
        m "............."
        call her_head(".............","normal","worriedCl")
        call her_head("Эм... [genie_name]?")
        m "Да, что такое?"
        call her_head("Вы уже?","open","base")
        m "Чего уже?"
        $ ccg1 = 7
        if daytime:
            call her_head("Ну, уроки вот-вот начнутся...","upset","wink")
        else:
            call her_head("Ну, я пообещала Джинни, что мы пойдем гулять...","upset","wink")
            call her_head("Она очень расстроена тем, что я так много времени провожу здесь...")


        #if not hanging_out_with_ginny:
        #    m "(Isn't Ginny that hot redhead?!)"
        #    call nar(>Your curiosity about Ginny grows!)
        #$ hanging_out_with_ginny = True

        m "Тебе нужны очки или нет?"
        $ ccg1 = 6
        call her_head("Нужны, [genie_name]! Простите...","grin","worriedCl")
        call her_head("Я продолжу...")
        m "Ну, ты можешь сделать это немного быстрее..."
        call her_head("Правда? Что я могу сделать [genie_name]?","base","baseL")

        menu:
            m "..."
            "\"Скажи, как сильно ты любишь свои сиськи.\"":
                $ ccg1 = 5
                call her_head("Что?","upset","wink")
                $ ccg1 = 6
                call her_head("Мою грудь?")
                m "Ты знаешь, как хорошо они себя чувствуют..."
                m "Взгляды, которые ты получаешь из-за них."
                call her_head("Ох, тогда...","base","base")
                call her_head("Был случай один раз в библиотеке...","smile","baseL")
                call her_head("Там было пусто, если не считать мальчика-первокурсника, сидящего напротив меня...")
                m "Хех. Хорошо... Продолжай."
                call her_head("Тут так жарко, по этому сниму жилет...","base","squint")
                m "Да, жарковато..."
                call her_head("Он пытался обмануть меня, но я сказала ему, что он может продолжать смотреть на них...","base","baseL")
                call her_head("Поэтому я начала расстегивать пуговицы... Сначало медленно, но он это заметил.","base","glance")
                m "Мммм, маленькая шлюшка."
                $ ccg1 = 9
                call her_head("На третьей пуговице, он не мог отвести от меня взгляд.","base","down")
                call her_head("Когда я расстегнула четвертую пуговицу, он убрал руки под стол...")
                m "Серьезно?"
                call her_head("Серьезно... Я слышала, как он...","base","ahegao_raised")
                $ ccg1 = 10
                call her_head("Когда я расстегнула пятую пуговицу, он почти увидел мои соски...","open","baseL")
                g9 "Тебе не было стыдно?"
                $ ccg1 = 5
                call her_head("[genie_name]! Я просто пыталась освежиться...","base","down")
                m "Я шучу, продолжай."
                call her_head(".....","base","glance")
                $ ccg1 = 9
                call her_head("После шестой пуговицы, он почти все уже увидел...")
                call her_head("Он увидел мои обнаженные сиськи...","base","suspicious")
                call her_head("И он продолжал смотреть на них... Он даже не пытался скрыть, то что он делал под столом")
                call her_head("Когда я расстегнула последнюю пуговицу, то для него это было финалом...")
                $ ccg1 = 10
                call her_head("Он выстрелил своей спермой под стол, прикрывая ногами!","silly","ahegao")
                g4 "!!!"
                call her_head("Давайте [genie_name] покройте меня всю! Я хочу чтоб ваша сперма была на моих сиськах!","grin","ahegao")
                with hpunch
                g4 "{size=-4}(Еще немного! Куда мне кончить?){/size}"

            "\"Высунь язык и наклони голову вниз!\"":
                $ ccg1 = 5
                call her_head("Что?","base","base")
                m "Сделай это, шлюха."
                $ ccg1 = 11
                call her_head("Вот так?","open_wide_tongue","squintL")
                m "Да, хорошо. Наклони голову."
                call her_head(".....................","open_wide_tongue","base")
                m "Да... Хорошо..."
                call her_head("...........","open_wide_tongue","base")
                call her_head("...........")
                $ ccg1 = 9
                call her_head("Я не могу держать рот открытым так долго, [genie_name]. Я начну пускать слюни...","open","base")
                m "Но я хочу чтоб ты это делала... эти прекрасные сиськи."
                call her_head("Что? Вы думаете, они прекрасны?","open","base")
                m "Такие прекрасные, как любой смертный, [hermione_name]!"
                $ ccg1 = 11
                call her_head(".......","base","ahegao_raised")
                m "Теперь засунь его обратно и попытайся расположить его как можно ближе к кончику моего члена, как ты можешь"
                call her_head("............","normal","worriedCl")
                call her_head("А-ха.....","open_wide_tongue","base")
                m "Хорошо, [hermione_name]."
                call her_head("..............","open_wide_tongue","base")
                m "Да, продолжай дрочить мой член."
                ">Когда Гермиона тянет сиськи вниз, ты, пытаясь коснуться ее влажного языка, тянешься вверх."
                call her_head("..................","open_wide_tongue","base")
                g4 "Ох, хорошо..."
                call her_head(".................","open_wide_tongue","base")
                ">Ты снова дотронулся до языка."
                m "Попробуй его, шлюха!"
                call her_head(".....................","open_wide_tongue","angryCl")
                m "Да, ты сисястая шлюха!"
                call her_head("......................","open_wide_tongue","angry")
                m "Я хочу кончить в этот маленький развратный ротик..."
                call her_head("................","open_wide_tongue","angry")
                g4 "{size=-4}(Еще не много! Куда мне кончить?){/size}"

        menu:
            m "..."
            "-Кончить в ротик-":
                $ mad += 3
                g4 "Я уже скоро, [hermione_name]! Будь готова!"
                $ ccg1 = 13
                call her_head("Что? Уже?!","shock","wide")
                g4 "{size=+5}Да, твои сиськи такие великолепные!!!{/size}"
                g4 "{size=+5}Ты маленькая шлюха!!!{/size}"
                hide screen bld1
                call blkfade

                call her_head("Нет, [genie_name], подождите, не на ли--","angry","base")
                g4 "{size=+5}Открой широко, шлюха!!{/size}"
                call her_head("Не в мой ро-","scream","wide")
                $ ccg1 = 12
                ">Ты хватаешь за затылок Гермиону и заставляешь ее засунуть член в рот..."
                call her_head("!!!!!!!","shock","worriedCl")
                ">Ощущение ее теплого рта и извивающегося языка переполняет тебя, и ты начинаешь кончать, как сумасшедший"

                call cum_block

                g4 "{size=+5}АХ! ДА!!! Возьми его, шлюха!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("titjob_cum_in_mouth","mid","base")
                hide screen bld1
                call hide_blkfade
                stop music fadeout 1.0
                call ctc

                call bld
                call her_head(".......................","full_cum","down",cheeks="blush")
                m "Мммммм, это было здорово...."
                call her_head(".......................","full_cum","down",cheeks="blush")
                m "Как ты себя чувствуешь?"
                call her_head(".......................","full_cum","down",cheeks="blush")
                m "[hermione_name]?"

                call play_music("chipper_doodle") # HERMIONE'S THEME.

                hide screen bld1
                call gen_chibi("titjob_pause","mid","base")
                pause.5

                show screen bld1
                $ ccg1 = 15
                call nar(">Гермиона открывает рот, ты начинаешь дико кончать в ее рот и на сиськи.")
                call her_head("*Тьфу*","open_wide_tongue_cum","angry")

                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                $ ccg1 = 16
                call her_head("Зачем вы кончили мне в рот!","angry","worriedCl",emote="05")
                m "Ты же сказала не кончать на лицо."
                pause.5
                hide screen bld1
                call blkfade
                $ ccg1 = 17
                ">Гермиона выпускает твой все еще пульсирующий член."
                pause.5

                call gen_chibi("hold_dick","desk","base")
                call her_chibi("stand","mid","base")
                call hide_blkfade
                pause.5

                show screen bld1
                call her_main("Ухх... Вы так много кончили! Мне пришлось проглотить большую часть.","angry","worriedCl",emote="05",xpos="right",ypos="base")
                m "Это твоя вина, что ты так хорошо справляешься..."
                call her_main("Я не хочу этого слышать...","angry","worriedCl",emote="05")
                if daytime:
                    call her_main("Мои занятия скоро начнутся и я вся в вашей сперме...","angry","worriedCl",emote="05")
                else:
                    call her_main("В это время в общей комнате \"Гриффиндора\" будет полно народу...","angry","worriedCl",emote="05")
                    call her_main("И теперь мне придется пойти туда, пахнущей и грязной...")
                    call her_main("Может быть, если я просто побегу в постель, меня никто не заметит...","angry","base")

                m "Ты могла проглотить..."
                m "Тогда бы не испачкалась твоя форма."
                call her_main("Проглотить все?","angry","down_raised")
                call her_main("Я не думаю, что у меня достаточно места в животе...")
                call her_main("Мы закончили [genie_name]?","annoyed","closed")
                call blkfade
                hide screen ccg
                with d3
                $ aftersperm = True

                jump done_with_titjob

            "-Кончить на сиськи-":
                with hpunch
                g4 "АХ!"
                call blkfade
                $ ccg1 = 13
                call her_head("ЧТО?!","shock","wide")
                g4 "Держи, шлюха!"

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide")
                $ ccg1 = 18
                call gen_chibi("titjob_cum_on_tits","mid","base")
                hide screen bld1
                call hide_blkfade
                call ctc

                call bld
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True
                call her_head(".......................","angry","wide")
                m "Да... это было..."
                call her_head("..........","soft","base",tears="soft")
                m "Ну, я думаю, что на этом все..."
                her ".........."
                hide screen bld1
                call blkfade

                call gen_chibi("hold_dick","desk","base")
                call her_chibi("stand","mid","base")
                pause 1
                call hide_blkfade
                pause.5

                call her_main("","annoyed","baseL",xpos="right",ypos="base")
                call ctc
                $ ccg1 = 17
                if daytime:
                    call her_main("[genie_name]! Как вы могли так кончить?!","scream","worriedCl")
                    call her_main("Как будто вы вылили ведро спермы на мою грудь!","annoyed","angryL")
                    call her_main("Мои занятия вот-вот начнутся, а я не могу ходить в таком виде!","open","down")
                    m "Конечно можешь, просто вытрись не много..."
                    m "Никто даже не заметит... может, кроме запаха..."
                    call her_main("...Я хотела бы получить очки.","annoyed","annoyed")
                else:
                    call her_main("Как может один человек кончить так много!","annoyed","angryL")
                    her "Как я могу вернуться в комнату отдыха \"Гриффиндора\" в таком виде?!"
                    m "Конечно можешь, просто вытрись не много."
                    m "Это не похоже на первый раз, когда ты легла спать, пахнующий спермой."
                    call her_main("...Я хотела бы получить очки.","annoyed","annoyed")

                call blkfade
                hide screen ccg
                with d3
                $ uni_sperm = False
                $ aftersperm = True

                jump done_with_titjob

    #Second Event.
    elif hg_pf_TitJob_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("Да, [genie_name]?","base","base",xpos="right",ypos="base")
        m "Как ты относишься к тому, чтоб обернуть мой член своими сиськами?"
        call her_main("Опять?","upset","closed")
        m "Ладно, ладно."
        m "Как ты относишься к тому, чтоб обхватить мой член своими сиськами еще разок?"
        call her_main("Хорошо, [genie_name].","base","glance")
        m "Тебе нравится, когда я называю их прекрасными, не так ли?"
        call her_main(".............","base","down")
        g9 "Тебе ничего говорить не надо, просто обхвати сиськами мой член."
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","worriedCl")
        call her_main("Да [genie_name]","grin","baseL")
        stop music fadeout 4.0

        jump titjob_round_2

    #Third Event.
    elif hg_pf_TitJob_OBJ.points >= 2:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="right",ypos="base")
        m "Ты не возражаешь, чтобы обхватить мой член своими сиськами?"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised")
        if whoring < 21:
            call her_main("Пока вы платите...","soft","squintL")
            m "Хорошо, тогда, подойди сюда, время, чтоб заработать еще немного очков."
        else:
            call her_main("Конечно нет [genie_name]...","open","baseL")
            m "Ну, тогда иди сюда."
            call her_main("","base","glance")
            pause.1

        jump start_titfuck


label start_titfuck:

        #Hermione removes her top.
        $ hermione_wear_bra = False
        call set_hermione_action("lift_top","skip_update")
        pause.5

        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update")
        pause.5

        hide screen bld1
        call blkfade
        pause.8

        hide screen genie
        show screen chair_left
        show screen desk
        call her_chibi("hide")
        call gen_chibi("titjob","mid","base")

        ">Гермиона обхватывает твой член своими большими сиськами..."

        if use_cgs:
            $ ccg_folder = "herm_boob"
            $ ccg1 = 6
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            show screen ccg
            with d3

        call h_action("lift_breasts","skip_update")

        stop music fadeout 3.0
        $ ccg1 = 20
        call her_head("Вам нравится, когда я так делаю, [genie_name]?","grin","baseL",xpos="base",ypos="high")
        ">Гермиона начинает быстро дрочить твой член своими сиськами."
        g9 "Конечно, да! Отлично!"
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        call hide_blkfade
        call ctc

        show screen bld1
        call her_head("...","base","glance")
        m "Да, да, мне нравится..."
        m "Хм... У тебя хорошо получается."
        $ ccg1 = 21
        call her_head("Спасибо, [genie_name].","base","happyCl")
        call her_head("Я думаю, это меньшее, что я вам делаю...")
        m "Хм..."

        menu:
            m "..."
            "\"Что ты думаешь о моем члене?\"":
                $ ccg1 = 22
                call her_head("А?","open","base")
                call her_head("О вашем члене?","angry","worriedCl",emote="05")
                m "Что ты думаешь о-"
                $ ccg1 = 23
                call her_head("Он великолепен....","upset","closed")
                m "Продолжай..."
                call her_head("Если у меня идеальные сиськи...","soft","ahegao")
                call nar(">Она сжимает сиськи вокруг твоего члена.")
                $ ccg1 = 22
                call her_head("То это идеальный член","grin","dead")
                m "Идеальный?"
                call her_head("Идеальный.","base","down")
                call her_head("Идеальный размер...","soft","down")
                call her_head("Идеальная форма...")
                $ ccg1 = 24
                call nar("Гермиона наклоняет голову и облизывает кончик члена.")
                call her_head("...","open_tongue","ahegao")
                $ ccg1 = 23
                call her_head("Безупречный вкус...","soft","ahegao")
                m "..."
                $ ccg1 = 25
                call her_head("Я думаю, что ваш идеальный член должен быть общим. ","scream","angryCl")
                m "Ну, я бы не стал заходить так далеко--"
                call her_head("Слушайте меня, [genie_name]!","soft","ahegao")
                call her_head("Я думаю, что вашему идеальному члену должны поклоняться, как части школьной программы!")
                $ ccg1 = 24
                call her_head("Девушки будут обязаны прийти и погреться в его славе!")
                m "Ладно, думаю, я достаточно услышал."
                $ ccg1 = 21
                call her_head("Слишком?","angry","wink")
                m "Да, немного."
                call her_head("Простите [genie_name], я не много увлеклась...","angry","worriedCl",emote="05")
                m "Ничего страшного. Просто продолжай массировать его своими большими сиськами."
                call her_head(".................","soft","ahegao")

                call nar(">Гермиона продолжает массировать твой член.","start")
                $ ccg1 = 25
                call nar(">Она плюет на него, чтобы смазать.","end")
                $ ccg1 = 21
                m "Да, да... Вот так, шлюха."

            "\"Назови себя большой сисястой шлюхой!\"":
                $ ccg1 = 22
                call her_head("Простите?","open","base")
                $ ccg1 = 23
                call her_head("Ох... Я большая сисястая шлюха!","soft","ahegao")
                m "Хорошо. Рад, что мы узнали это."
                m "Теперь, я хочу, чтоб ты сказала..."

                menu:
                    m "..."
                    "\"Скажи, что ты бестыжая спермоглотка!\"":
                        $ ccg1 = 22
                        call her_head("Конечно.","base","down")
                        $ ccg1 = 24
                        call her_head("Я бестыжая спермоглотка .","soft","ahegao")
                        $ ccg1 = 21
                        call her_head("Грязная шлюха, которая обожает вкус спермы...","grin","dead")
                        m "Да! Хорошо!"
                    "\"Скажи, что ты любишь быть обконченной!\"":
                        $ ccg1 = 24
                        call her_head("Я люблю быть обконченной!","soft","ahegao")
                        call her_head("горячей...")
                        call her_head("липкой...")
                        call her_head("вонючей...")
                        call her_head("спермой...")
                        $ ccg1 = 23
                        call her_head("...................................","grin","dead")
                        $ ccg1 = 21
                        call her_head("Как вам, [genie_name]?","angry","wink")
                        m "Превосходно."

            "\"Это было здорово. Ты практиковалась?\"":
                $ ccg1 = 22
                call her_head("Хм?","base","happyCl")
                $ ccg1 = 21
                call her_head("Вроде... Ну, не с другим...","angry","wink")
                m "А как тогда?"
                $ ccg1 = 22
                call her_head("Ну, я говорила с Джинни...","grin","baseL")
                m "Это твоя подруга?"
                call her_head("Да. Я попросила советов у нее...","base","baseL")
                $ ccg1 = 21
                call her_head("Она сказала, что лучше практиковаться...","base","squint")
                m "С кем?"
                $ ccg1 = 22
                call her_head("С ней же","smile","baseL")
                $ ccg1 = 23
                call her_head("Ну... на ней... на ее руке.","angry","wink")
                m "Ты обхватывала ее руку своими сиськами?"
                $ ccg1 = 25
                call her_head("Я практиковалась!","grin","worriedCl",emote="05")
                $ ccg1 = 22
                call her_head("Она дала еще пару советов...")
                $ ccg1 = 23
                call her_head("Какое у вас чувство после этого?","base","down")
                m "Ммммм... Это было здорово."
                call her_head("Правда?","angry","wink")
                $ ccg1 = 21
                call her_head("Джинни тоже, вроде, понравилось...","base","ahegao_raised")
                g4 "Ей понравилось?"
                $ ccg1 = 22
                call her_head("Конечно!","base","happyCl")
                $ ccg1 = 23
                call her_head("Кто же не хочет почувствовать мои идеальные сиськи...","base","closed")
                call her_head("Хотя, ей даже очень понравилось...","open","down")
                $ ccg1 = 22
                call her_head("Слишком сильно...","soft","squintL")
                m "Как так?"
                call her_head("Ну...","soft","squintL")
                call her_head("Она начала играть...")
                $ ccg1 = 23
                call her_head("Играть с собой...","grin","ahegao")
                with hpunch
                with kissiris
                g4 "Да, продолжай, шлюха"
                call her_head("Поскольку, я \"практиковалась\" на ее руке, она могла...","open","baseL")
                $ ccg1 = 24
                call her_head("Кончить...","soft","ahegao")
                g4 "[hermione_name], ты маленькая шлюха!"
                $ ccg1 = 23
                call her_head("Но, это была просто практика!","grin","worriedCl",emote="05")
                call her_head("Эм... я имею в виду...","angry","wink")
                $ ccg1 = 21
                call her_head("И... Мне понравилось тоже...","angry","down_raised")
                m "Да, да... ты не совсем шлюха..."
                m "Ммммм, почему бы тебе не плюнуть на него..."
                m "О да..."
                $ ccg1 = 24
                call her_head("...............","base","down")

        m "Да... Продолжай."
        $ ccg1 = 23
        call her_head("..............","angry","wink")
        m "Я хочу чтоб ты сказала..."

        menu:
            m "..."
            "{size=-4}\"Я люблю дразнить своего отца моими большими сиськами.\"{/size}":
                $ ccg1 = 25
                call her_head("Я не буду!","angry","down_raised")
                m "Я знаю. Просто скажи."
                $ ccg1 = 22
                call her_head("Моего отца? Это грубо, [genie_name]! Как вы могли предложить такое, пиз-","soft","ahegao")
                m "Давай... Скажи это."
                call her_head("...........","angry","wink")
                call her_head("Ну...","open","down")
                $ ccg1 = 21
                call her_head("Иногда, когда я обнимаю его...")
                call her_head(".......")
                m "Давай [hermione_name]..."
                $ ccg1 = 22
                call her_head("Я прижимаю свои сиськи к нему...","soft","ahegao")
                m "Как ты думаешь, ему это нравится?"
                call her_head("Конечно нет...","annoyed","base")
                call her_head("Я думаю...","soft","squintL")
                $ ccg1 = 23
                call her_head("Он пытается прикрыть свой стоящий член...","base","closed")
                call her_head("Он даже говорит, что я слишком старая для обьятий...","annoyed","closed")
                call her_head("Но я не забываю обнимать его каждый вечер перед сном...")
                call her_head("Чтоб он думал обо мне...","base","down")
                call her_head("И как хорошо я это чувствую...","grin","dead")
                $ ccg1 = 24
                call her_head("Давлю на него...","soft","ahegao")
                m "Вот так, шлюха."
                $ ccg1 = 22
                call her_head("А потом я поцеловала его в лоб...","soft","squintL")
                $ ccg1 = 23
                call her_head("Сделав так, чтоб он увидел мои сиськи...","grin","worriedCl",emote="05")
                call her_head("{image=textheart}{image=textheart}{image=textheart}")
                $ ccg1 = 25
                call her_head("Но все это, конечно, не так!","open","base")
                $ ccg1 = 22
                call her_head("Ничего не было! Это было только для вас.")
                m "Верно..."
            "{size=-4}\"Я люблю дразнить одноклассников своими сиськами.\"{/size}":
                $ ccg1 = 23
                call her_head("Я люблю дразнить моих одноклассников моими идеальными сиськами...","soft","ahegao")
                m "Конечно..."
                call her_head("Обожаю ревнивые взгляды других девочек...","base","down")
                m "Я уверен, что они завидуют..."
                $ ccg1 = 21
                call her_head("Я люблю дразнить Рона и Гарри во время завтрака...","base","glance")
                $ ccg1 = 22
                call her_head("Иногда, я хожу только с одной застегнутой пуговицей...","base","suspicious")
                $ ccg1 = 23
                call her_head("В других случаях, я одеваю жилет, а под ним у меня ничего нет...")
                m "И как ты себя чувствуешь..."
                call her_head("Хорошо...","silly","dead")
                call her_head("Однажды, когда я возвращалась из вашего кабинета ночью, я едва прикрывала их. ...","angry","wink")
                call her_head("И я завернула за угол...","soft","ahegao")
                $ ccg1 = 24
                call her_head("И какой-то мальчик врезался своей головой в мою грудь...","grin","ahegao")
                m "Головой в твою грудь?"
                call her_head("Я видела его макушку...","grin","dead")
                m "Что он сделал?"
                call her_head("Он попытался уйти...")
                m "Попытался?"
                $ ccg1 = 22
                call her_head("Ну, я держала его там...","base","glance")
                call her_head("Немного...","base","down")
                $ ccg1 = 23
                call her_head("Что бы сказать ему, что все в порядке...","base","suspicious")
                m "Ты маленькая шлюха."
                $ ccg1 = 22
                call her_head("Я думаю. Хотя, возможно, я сломала его...","base","down")
                $ ccg1 = 21
                call her_head("Когда я его отпустила, он ничего не сказал. Он просто медленно ушел.","soft","ahegao")
                m "Я знаю куда он пошел..."
                $ ccg1 = 23
                call her_head("И я тоже...","soft","ahegao")

        #CUMMING
        m "Хм..."
        m "Я люблю твои развратные сиськи!"
        $ ccg1 = 22
        call her_head("Спасибо [genie_name].","soft","ahegao")
        $ ccg1 = 23
        call her_head("Мне потрясти ими?")
        call nar(">Гермиона прижалась к тебе и начинает трясти их еще быстрее...")
        m "О да!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Скоро кончу. Только куда?){/size}"

        menu:
            m "..."
            "\"(В рот).\"":
                g4 "Возьми его, шлюха"
                hide screen bld1
                call blkfade

                ">Ты хватаешь Гермиону за затылок, наклоняя ее вниз"
                $ ccg1 = 25
                call her_head("Что вы-","angry","wink")
                ">Ты засовываешь свой член в ее влажный ротик."

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"


                call play_music("chipper_doodle") # HERMIONE'S THEME.

                $ ccg1 = 26
                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("titjob_cum_in_mouth")
                call hide_blkfade
                call ctc

                call bld
                g4 "Ах! Шлюха!"
                call her_head("{image=textheart}{image=textheart}{image=textheart}","full_cum","dead")
                g4 "Ах! Ты жирная шлюха! Проглоти все!"
                call her_head("......","full_cum","dead")
                m "............"
                m "Хорошо, думаю, я закончил..."
                call her_head("..............","full_cum","dead")
                call her_head("........","full_cum","dead")
                call her_head("...","full_cum","dead")
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                $ ccg1 = 27
                call her_head("*GULP*","cum","worriedCl") #play noise here
                hide screen bld1
                call ctc
                call blkfade

                pause.5
                ">Гермиона высовывает твой член."
                pause 1
                $ ccg1 = 28
                call gen_chibi("stand","desk","base")
                call her_chibi("stand","mid","base")

                call h_action("none","skip_update")

                call hide_blkfade
                pause.5

                show screen bld1
                call her_main("","soft","glance",xpos="right",ypos="base")
                call ctc
                $ ccg1 = 29
                if daytime:
                    call her_main("Ну, думаю, мне лучше уйти... мои занятия вот-вот начнутся.","base","base")
                else:
                    call her_main("Ну, думаю, мне лучше уйти... Уже довольно поздно.","base","base")
                m "Так, теперь ты не против глотать?"
                call her_main("Что?","open","down")
                call her_main("Ох. Я полагаю...","grin","baseL")
                call her_main("Я имею в виду, что это не так уж и плохо, и это значит, что мне не нужно приводить себя в порядок.","base","happyCl")
                m "Хм... Ты уверена, что не хочешь, чтобы люди видели твои сиськи, покрытые спермой..."
                call her_main("Что? Гулять по школе покрытой спермой [genie_name]?","angry","wink")
                m "Глотая ты будешь держать свою одежду в чистоте."

                if whoring < 21:
                    call her_main("Со всем уважением [genie_name]...","upset","closed")
                    call her_main("Я не планирую получить репутацию, любящей сперму, шлюхи...","angry","wink")
                    call her_main("Не как те \"Слизеринские\" девочки...")
                else:
                    call her_main("Хм...","soft","squintL")
                    call her_main("Может быть, если вы вежливо попросите...","soft","squintL")
                call her_main("На этом все [genie_name]?","annoyed","closed")

                call blkfade
                hide screen ccg
                jump done_with_titjob


            "\"(На сиськи).\"":
                g4 "Лови все на сиськи!"
                with hpunch
                g4 "АХ!"
                hide screen bld1
                call blkfade
                $ ccg1 = 25
                call her_head("Что? Уже?!","shock","wide")
                g4 "Да, я сейчас кончу на твои сиськи!"

                call cum_block

                g4 "{size=+5}АХ! ДА!!!{/size}"
                $ ccg1 = 30
                call her_head("!!!!!!!!!!!","shock","wide")

                call gen_chibi("titjob_cum_on_tits")
                call hide_blkfade
                call ctc

                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                show screen bld1
                $ ccg1 = 31
                call her_head(".......................","angry","wide")
                m "Ахх... Я чувствую себя намного лучше..."
                hide screen bld1
                call ctc
                call blkfade
                $ ccg1 = 32
                call gen_chibi("stand","desk","base")
                call her_chibi("stand","mid","base")

                call h_action("none","skip_update")

                call hide_blkfade
                pause.5

                show screen bld1
                call her_main("","upset","closed",xpos="right",ypos="base")
                call ctc
                $ ccg1 = 33
                her ".........."
                m "Ну, я думаю, что на этом все..."

                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ ccg1 = 35
                call her_main("[genie_name]!","annoyed","angryL")
                m "Что?"
                call her_main("Вы покрыли мою грудь спермой, [genie_name]...","angry","worriedCl")
                $ ccg1 = 34
                call her_main("Ее очень много...","open","baseL")
                m "Это твоя вина, [hermione_name]!"
                call her_main("Моя вина?","angry","base")
                m "Да! Это все твои идеальные сиськи...."
                m "Они слишком хороши..."
                $ ccg1 = 36
                call her_main("Ох...","shock","wide")
                her "Ну, я полагаю, что это не так уж и плохо..."
                $ ccg1 = 37
                call her_main("Я просто сотру все и, надеюсь, что никто не заметит...","upset","closed")
                m "Ты можешь вылизать их."
                call her_main("Вы хотите, чтобы я слизывала вашу сперму со своих сисек?","soft","ahegao")
                call her_main("Я так не думаю, [genie_name]...","soft","ahegao")
                her "{size=-5}Может быть в следующий раз...{/size}"
                call her_main("Это все [genie_name]?","angry","wink")

                call blkfade
                hide screen ccg
                $ aftersperm = True

                jump done_with_titjob

label done_with_titjob:

    $ gryffindor += current_payout #35
    hide screen ccg
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    hide screen hermione_main

    call h_action("none")

    call gen_chibi("hide")
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base")
    pause.1
    call hide_blkfade
    pause.5

    call bld
    m "Да, [hermione_name]. [current_payout] очков \"Гриффиндору\"."
    $ gryffindor +=current_payout

    call her_main("Спасибо, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if whoring < 18:
        $ whoring +=1

    $ hg_pf_TitJob_OBJ.points += 1

    if hg_pf_TitJob_OBJ.points <= 3:
        $ hg_pf_TitJob_OBJ.hearts_level = hg_pf_TitJob_OBJ.points

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    $ custom_outfit_old = temp_outfit

    jump end_hg_pf #Resets screens. Hermione walks out. Resets Hermione.
