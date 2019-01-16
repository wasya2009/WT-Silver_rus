

### Wear A Buttplug ###

label hg_ps_Buttplug:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    $ current_payout = 55 #Used when haggling about price of the favour.

    if hg_ps_Buttplug_OBJ.points < 1:
        m "{size=-4}(Сказать ей, чтобы она походила с анальной пробкой по школе?){/size}"
        menu:
            "\"(Да, давай сделаем это!)\"":
                pass
            "\"(Не сейчас.)\"":
                jump silver_requests
    else:
        m "{size=-4}(Я намереваюсь снова ее заставить ходить по школе с анальной пробкой!){/size}"

    m "{size=-4}(Но какой размер?){/size}"
    menu:
        "-Маленькая, обычная-":
            $ buttplug_size = 1
        "-Средняя, магическая-" if hg_ps_Buttplug_OBJ.points >= 1:
            $ buttplug_size = 2
        "-Огромная, магическая-" if buttplug_2_worn == True and whoring > 23:
            $ buttplug_size = 3

    #First event.
    if hg_ps_Buttplug_OBJ.points == 0 and buttplug_size == 1:
        m "[hermione_name], я хочу, чтобы ты сегодня сделала что-то необычное..."
        call her_main("...........","soft","base",xpos="right",ypos="base")
        call nar(">Ты вытаскиваешь анальную пробку огромного размера из-под своего стола и ставишь перед ней.")
        if whoring <=10:
            m "Я хочу, чтобы ты походила с анальной пробкой по школе."
            jump too_much

        $ buttplug_1_worn = True

        call her_main("И что это? Хвост какого-то животного?","open","suspicious")
        m "Не совсем, это анальная пробка. Я хочу, чтобы ты носила ее в себе, пока будешь на уроках."
        stop music
        with hpunch
        call her_main("{size=+5}Что?!!{/size}","shock","wide")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Вы ожидаете, что я вставлю эту огромную штуку в...","angry","angry")
        her "А потом выставлю себя на показ перед школой!"
        m "Она похожа на поддельный хвост, никто не догадается, что это на самом деле."
        call her_main("{size=+5}Не в этом дело!{/size}","scream","angryCl")
        her "Я не собираюсь вставлять эту нелепую штуку в свою задницу!"
        call her_main("На этом точка, [genie_name]!","angry","angry",emote="01")
        m "Хорошо, хорошо, успокойся..."
        call her_main("Я определенно не стану, [genie_name]! Это полный абсурд!","scream","angryCl")
        m "Ладно, ладно, может, я недооценил его размер..."
        call her_main("Думаете, [genie_name]?! Я бы хотела посмотреть, как вы пытаетесь-","angry","angry")
        m "Хорошо, хорошо..."
        call her_main(".........","annoyed","annoyed")
        m "Как насчет того, чтобы попробовать немного меньший..."
        call her_main("............","upset","closed")
        m "Я готов пожертвовать \"Гриффиндору\" пятьдесят пять очков."
        m "И все, что я прошу..."
        call her_main("..........?","annoyed","suspicious")
        call nar(">Ты вытаскиваешь небольшую анальную пробку из стола.")
        m "...Это то, что ты будешь носить в классе..."
        call her_main("!!!......","angry","angry")
        m "Ох, да ладно... Малое дитя."
        call her_main("...","disgust","glance")
        m "Пятьдесят пять очков факультету..."
        call her_main("..............","annoyed","angryL")
        call her_main("Хорошо.","annoyed","annoyed")
        m "Чудесно."
        m "Ты вставишь ее сейчас?"
        call her_main("........","annoyed","angryL")
        call her_main("Я вставлю ее в женском туалете [genie_name]","annoyed","angryL")
        m "Хммм... тогда увидимся вечером."

    #Second Event.
    elif buttplug_2_worn == False and buttplug_size == 2:
        m "[hermione_name], я хочу, чтобы ты сегодня испытала что-то необычное..."
        call her_main("...........","soft","base",xpos="right",ypos="base")
        call nar(">Ты вытаскиваешь анальную пробку среднего размера из своего стола и ставишь перед ней.")
        if whoring <=15:
            m "Я хочу, чтобы ты походила с анальной пробкой по школе"
            jump too_much

        $ buttplug_2_worn = True

        call her_main("И что же это такое?","open","suspicious")
        m "Ты не можешь сказать, что это анальная пробка? Сейчас они не должны быть в новинку для тебя."
        call her_main("...","annoyed","annoyed")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Почему к ней прикреплен такой большой хвост...","annoyed","angry")
        her "Вы же не думаете, что я буду носить это в школе!"
        m "Если ты не хочешь, чтобы я покупал у тебя услуги..."
        call her_main("Но ведь он такой длинный! Все смогут его увидеть!","normal","worriedCl")
        m "В этом и суть, [hermione_name]..."
        call her_main("...........","angry","worriedCl",emote="05")
        call her_main("Я хочу 100 очков.","annoyed","angry")

        menu:
            "\"Отлично, но я рассчитываю, что ты вставишь его сейчас.\"":
                $ current_payout = 100
                call her_main("Что? Сейчас?!","angry","worriedCl")
                call her_main("Перед вами?","angry","wink")
                m "100 очков [hermione_name]..."
                call her_main("Угх... Хорошо...","angry","down_raised")
                call her_main("Но я не повернусь!","annoyed","annoyed")
                m "Это больше тебе подходит..."
                ">Ты передаешь ей анальную пробку."
                call her_main("{size=-7}Такая большая...{/size}","clench","down_raised")
                ">Гермиона поднимает юбку и прижимает ее к своей дырочке."
                call her_main("Угхх... она такая большая...","shock","worriedCl")
                call her_main("Она не войдет!","open","worriedCl")
                m "Ну, тогда попробуй плюнуть на нее."
                call her_main(".........","angry","down_raised")
                ">Она плюет на кончик, а затем повторяет попытку."
                call her_main("Это не работает, она все ровно боль-","angry","base")
                stop music

                call set_h_buttplug("plug_b_on") #Updates clothing and body.

                with hpunch
                call her_main("{size=+5}!!!!{/size}","shock","wide")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main(".............","angry","base")
                call her_main("...","angry","down_raised")
                call her_main("Уу.... Ах, я... Лучше тогда.... Пойду в... Класс...","angry","wink")
                m "Увидимся вечером [hermione_name]."

            "\"Ты получаешь 70 очков.\"":
                $ current_payout = 70
                call her_main("Хмммпф...","annoyed","angryL")
                call her_main("Хорошо, тогда, не рассчитывайте, что я покажу вам ее!","angry","angry")
                m "Ты получишь 70 очков, если будешь носишь ее в классе."
                ">Ты передаешь ей анальную пробку."
                call her_main("Это все [genie_name]?.","annoyed","annoyed")
                m "Да [hermione_name], увидимся вечером."
                call her_main("{size=-5}(Дешевый ублюдок..){/size}","annoyed","angryL")


    else: # <================================================================================ NOT FIRST TIME
        if whoring <= 15 and buttplug_size == 1: # LEVEL 06 FIRST EVENT.
            $ buttplug_1_worn = True

            m "Я хочу купить услугу..."
            call her_main(".........","angry","base",xpos="right",ypos="base")
            m "Вставь свою любимую анальную пробку!"
            call her_main("...Снова?","angry","down_raised")
            m "Конечно, почему нет?"
            m "И еще пятьдесят пять очков факультету \"Гриффиндор\" конечно же."
            call her_main("..........","annoyed","worriedL")
            m "Итак... Ты с этим согласна, [hermione_name]?"
            call her_main("Думаю, да...","annoyed","angryL")
            ">Ты передаешь ей анальную пробку."
            m "Чудесно! Увидимся после занятий."

        elif whoring <= 20 and buttplug_size == 1: # LEVEL 07
            $ buttplug_1_worn = True

            ">Ты достаешь большую анальную пробку."
            m "Готова попробывать этого дракона?"
            stop music fadeout 1.0
            call her_main("Что?","scream","wide_stare",xpos="right",ypos="base")
            call her_main("Конечно нет! Эта штука порвет меня--","scream","angryCl")
            ">Ты достаешь маленькую анальную пробку."
            m "Тогда как насчет этой?"
            call her_main("Ох, хорошо!","smile","happyCl",emote="06")
            m "Ты так просто согласилась?"
            call her_main("Ну, за пятьдесят пять очков безумие отказываться.","base","closed")
            call her_main("Плюс в том, что ее носить не так уж и плохо...","open","baseL")
            ">Ты передаешь ей анальную пробку."
            m "Почему бы тебе не вставить ее сейчас."
            call her_main("Вы хотите, чтобы я ее сейчас вставила? Перед вами!","scream","wide_stare")
            m "Я не вижу в этом ничего плохого."
            call her_main("Ну... Это избавляет меня от необходимости посещать ванную для девочек перед занятием...","annoyed","down")
            call her_main("Хорошо, тогда, я сделаю это... Но я хочу дополнительные пять очков!","smile","baseL")
            m "Хорошо."
            $ current_payout += 5
            call her_main("Ну... Приступим.","smile","baseL")
            ">Гермиона медленно задирает юбку."

            call set_h_buttplug("plug_a_on") #Updates clothing and body.

            call her_main("{image=textheart}ах{image=textheart}...","grin","ahegao")
            call her_main("Я лучше пойду в класс...","soft","squintL")
            m "Увидимся вечером [hermione_name]."
            call her_main("{size=-5}({image=textheart}это так приятно{image=textheart}){/size}","grin","ahegao")

        elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+
            $ buttplug_1_worn = True

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Что ты думаешь о ношении анальной п-?"
            call her_main("Я сделаю это.","grin","baseL",xpos="right",ypos="base")
            m "А ты нетерпеливая."
            call her_main("Ну... Я думаю о количестве очков и... Я вроде как полюбила это чувство...","open","down")
            m "Замечательно. Тогда давай веселиться!"
            ">Ты передаешь ей анальную пробку."
            ">Гермиона оборачивается поднимая юбку, давая тебе отличный вид, пока она вставляет ее."

            call set_h_buttplug("plug_a_on") #Updates clothing and body.

            call her_main("{image=textheart}ах{image=textheart}...","grin","ahegao")
            call her_main("Так и сделаю, [genie_name]. Спасибо вам.","base","happyCl")

        elif whoring <= 19 and buttplug_size == 2: # LEVEL 06 FIRST EVENT.
            $ buttplug_2_worn = True

            m "Сегодня моей любезной просьбой будет..."
            call her_main(".........","angry","base",xpos="right",ypos="base")
            m "Ношение на занятиях твоей любимой магической анальной пробки!"
            call her_main("...Снова?","angry","down_raised")
            m "Почему нет? Это будут самые легкие пятьдесят пять очков, которые ты когда-либо зарабатывала!"
            call her_main("..........","annoyed","worriedL")
            m "У тебя проблемы с этим, [hermione_name]?"
            call her_main("Я полагаю, нет...","annoyed","angryL")
            ">Ты передаешь ей магическую анальную пробку."
            m "Чудесно! Увидимся снова после занятий."

        elif whoring <= 23 and buttplug_size == 2: # LEVEL 07
            if buttplug_2_question == False:
                $ buttplug_2_question = True
                ">Ты достаешь анальную пробку."
                m "Готова снова попробовать?"
                call her_main("Ох, я думаю да...","soft","squintL",xpos="right",ypos="base")
                call her_main("Но ничего, если я сначала кое-что спрошу?","open","down")
                m "Что такое [hermione_name]"
                call her_main("Вы не боитесь того, что нас поймают?","annoyed","base")
                m "А должен?"
                call her_main("Ну, просто то, что вы заставляет меня носить подобное, привлекает много внимания...","open","worriedL")
                call her_main("А что если кто-то поймет, что это вы заставляете меня делать все это...","open","worried")
                m "И кто станет подозревать великого Альбиса Дамблдорфа?"
                call her_main("...Я полагаю никто...","annoyed","worriedL")
                m "Тогда не беспокойся об этом. Если кто-нибудь спросит, просто скажи им, что ты проходишь период эксгибиционизма."
                m "Говоря об этом..."
                ">Ты передаешь ей анальную пробку."
                call her_main("Ох... хорошо...","base","down")
                ">Гермиона приподнимает юбку и осторожно, не торопясь, вставляет ее."

                call set_h_buttplug("plug_b_on") #Updates clothing and body.

                call her_main("{image=textheart}{image=textheart}{image=textheart}Ах{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao")
                call her_main("Я лучше... сейчас пойду... в класс...","open","baseL")
                m "Увидимся вечером [hermione_name]."
                call her_main("{size=-5}({image=textheart}она... такая... большая...{image=textheart}){/size}","grin","ahegao")
            else:
                ">Ты достаешь анальную пробку."
                m "Готова снова попробовать?"
                call her_main("Ох, наверно...","open","down",xpos="right",ypos="base")
                call her_main("Но если вы заплатите мне дополнительные 5 очков, я вставлю ее прямо здесь...","soft","squintL")
                menu:
                    "\"Отличное предложение\"":
                        $ current_payout += 5
                        call her_main("Спасибо вам [genie_name], вы не пожалеете об этом...","open","baseL")
                    "\"Пятьдесят пять - это все, что я могу дать.\"":
                        m "Еще немного и люди станут подозревать."
                        call her_main("Хмммм, я думаю вы правы...","annoyed","angryL")
                        call her_main("Но в качестве подарка я все равно сделаю это...","base","down")
                        call her_main("Вы хотя бы оцените...","base","suspicious")
                        m "Будь уверена, я оценю."
                ">Ты передаешь ей анальную пробку."
                call her_main("Ну... Начнем...","base","down")
                ">Гермиона оборачивается, приподнимает юбку и осторожно, не торопясь, вставляет ее."

                call set_h_buttplug("plug_b_on") #Updates clothing and body.

                call her_main("{image=textheart}{image=textheart}{image=textheart}ах{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao")
                call her_main("Я лучше... сейчас пойду... в класс...","soft","squintL")
                m "Увидимся вечером [hermione_name]."
                call her_main("{size=-5}({image=textheart}это... так... хорошо...{image=textheart}){/size}","grin","ahegao")

        elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Что ты думаешь о ношении анальной п-?"
            call her_main("Я сделаю это.","grin","baseL",xpos="right",ypos="base")
            m "А ты нетерпеливая. Я даже не договорил..."
            call her_main("Ох... можно мне большую... с длинным хвостом...","open","down")
            call her_main("Пожалуйста...","soft","squintL")
            m "Ну, раз ты так хорошо попросила..."
            ">Ты передаешь ей анальную пробку."
            ">Гермиона оборачивается поднимая юбку, давая тебе отличный вид, пока она вставляет ее."

            call set_h_buttplug("plug_b_on") #Updates clothing and body.

            call her_main("{image=textheart}ах{image=textheart}...","grin","ahegao")
            call her_main("Спасибо вам [genie_name]!","open","baseL")
            call her_main("{size=-5}({image=textheart}Это так хорошо... Возможно, мне придется купить себе такую же...{image=textheart}){/size}","grin","ahegao")

        elif buttplug_size == 3 and not buttplug_3_worn: # Large buttplug first time
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Что ты думаешь о ношении анальной п-?"
            call her_main("Я сделаю это.","grin","baseL",xpos="right",ypos="base")
            m "А ты нетерпиливая. Я даже не договорил..."
            call her_main("Ох... можно мне большую... с длинным хвостом...","open","down")
            call her_main("Пожалуйста...","soft","squintL")
            m "Чтож, раз ты настаиваешь..."
            ">Ты передаешь ей анальную пробку."
            call her_main("!!!","angry","down_raised")
            call her_main("Это не та, которую я имела в виду [genie_name]...","angry","down_raised")
            m "Разве ты просила не большую?"
            call her_main("Я просила-","grin","ahegao")
            m "Ну вот {b}эту{/b} большую."
            call her_main("Я не знала, что у вас есть настолько большая!","open","baseL")
            call her_main("Я даже не думаю, что она войдет...","grin","ahegao")
            m "Никогда не говори никогда!"
            call her_main("Вы же не серьезно!","grin","ahegao")
            call her_main("Это абсурд!","grin","ahegao")
            m "Ты говорила то же самое о маленькой."
            call her_main("Это было другое...","grin","ahegao")
            m "Я уверен в тебе! Кроме того, ты была очень хороша, когда брала мой член в задницу!"
            call her_main("[genie_name]!","grin","ahegao")
            m "Да ладно..."
            call her_main("Она слишком большая, сэр! Даже ваш член не был таким {p}{b}толстым{/b}...","grin","ahegao")
            m "Ничего, небольшой плевок все решит!"
            call her_main("Я думаю плевка недостаточно, [genie_name]. Если у вас нет никакой {i}смазки{/i} в распоряжении, не думаю, что позволю этой штуке приблизиться к себе.","grin","ahegao")
            if gift_item_inv[12] >= 1:# anal lubricant
                $ buttplug_3_worn = True
                call play_music("playful_tension") # SEX THEME.
                m "Ну, так уж получилось, что у меня есть решение твоей проблемы."
                call her_main("Какое?","grin","ahegao")
                m "Вот."
                ">Ты передаешь Гермионе банку анальной смазки."
                $ gift_item_inv[12] -= 1
                call her_main("!!!","grin","ahegao")
                call her_main("Я же не серьезно [genie_name]!","grin","ahegao")
                m "Так, так. Никому не нравятся лгуньи."
                call her_main("Я ничего не обещала! Кроме того, я не ожидала, что у вас окажется банка смазки.","grin","ahegao")
                m "Я купил его как раз для такого случая..."
                call her_main("...","grin","ahegao")
                call her_main("Угх... хорошо. Я {b}попробую{/b} вставить ее.","grin","ahegao")
                call her_main("Но ничего не обещаю!","grin","ahegao")
                m "Это все что я прошу."
                ">Ты передаешь Гермионе огромную анальную пробку."
                call her_main("Я все еще думаю, что это не сработает...","grin","ahegao")
                ">Гермиона медленно покрывает большую анальную пробку смазкой. "
                call her_main("Едва хватает чтобы намазать ее...","grin","ahegao")
                call her_main("(Эта штука ни за что не поместится.)","grin","ahegao")
                ">Гермиона медленно вставляет смазаную анальную пробку в анус."
                call her_main("Я говорю вам [genie_name], она не собирается-","grin","ahegao")
                call her_main("{size=+10}!!!{/size}","grin","ahegao")
                call her_main("{size=+10}Она входит!{/size}","grin","ahegao")
                m "Правда?"
                call her_main("{size=+5}Угх...{/size}","grin","ahegao")
                call her_main("{size=+5}Она входит внутрь меня....{/size}","grin","ahegao")
                call her_main("{size=+5}И расстягивает меня изнутри... [genie_name].{/size}","grin","ahegao")
                call her_main("Ах...","grin","ahegao")
                call her_main("Это...{p}Это...","grin","ahegao")
                $ hermione_dribble = True
                call her_main("{size=+5}Невероятно!{/size}","grin","ahegao")
                ">Ты слышишь хлюпающие звуки, как анальная пробка движется внутри Гермионы."

                call set_h_buttplug("plug_c_on") #Updates clothing and body.

                call her_main(".............","grin","ahegao")
                m "Ты в порядке [hermione_name]?"
                call her_main("..........................","grin","ahegao")
                call her_main("Ах... д-да..","grin","ahegao")
                m "Чудесно! Тогда увидимся после занятий."
                call her_main(".............","grin","ahegao")
                ">Гермиона медленно выходит из твоего кабинета, едва способная нормально ходить."
                pass
            else:
                m "Боюсь, нет..."
                call her_main("Ну, тогда думаю, мне лучше пойти на занятия.","grin","ahegao")
                call her_main("{size=-2}Если {size=-2}только {size=-2}у {size=-2}вас {size=-2}нет {size=-2}поменьше.{/size}{image=textheart}","grin","ahegao")
                m "Так уж получилось, что есть."
                ">Ты передаешь ей анальную пробку."
                ">Гермиона оборачивается поднимая юбку, давая тебе отличный вид, пока она вставляет ее."

                call set_h_buttplug("plug_b_on") #Updates clothing and body.

                call her_main("{image=textheart}Ах{image=textheart}...","grin","ahegao")
                call her_main("Спасибо вам [genie_name]!","open","baseL")
                call her_main("{size=-5}({image=textheart}Это так приятно... Я думаю, стоит купить себе такую же...{image=textheart}){/size}","grin","ahegao")
                m "(Нужно посмотреть, есть ли у ребят Уизли что-нибудь, что может помочь...)"

        elif buttplug_size == 3: # Large buttplug repeat
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Как ты относишься к тому, чтобы надеть еще одну анальную пробку сегодня на урок?"
            call her_main("...","grin","baseL",xpos="right",ypos="base")
            call her_main("Какую?","grin","baseL")
            m "Как насчет снова большой?"
            call her_main("Правда?","open","down")
            call her_main("Еще раз?","soft","squintL")
            m "Кажется, тебе понравилсь ее носить в прошлый раз..."
            call her_main("...","open","down")
            call her_main("{size=-5}хорошо, тогда...{/size}","open","down")
            ">Ты передаешь ей анальную пробку."
            ">Гермиона оборачивается поднимая юбку, давая тебе отличный вид, пока она вставляет ее."
            ">Ты видишь магического червя, который проникает внутрь ее нетерпеливой дырочки."

            call set_h_buttplug("plug_c_on") #Updates clothing and body.

            call her_main("{image=textheart}Ах{image=textheart}Ах...","grin","ahegao")
            call her_main("Спасибо вам [genie_name]!","open","baseL")
            call her_main("{size=-5}({image=textheart}это так приятно... Я должна купить для себя такую же...{image=textheart}){/size}","grin","ahegao")

    $ hg_ps_Buttplug_OBJ.inProgress = True

    jump hg_pr_transition_block





label hg_ps_Buttplug_complete:

    call play_sound("door")
    call her_walk("door","mid",2)
    pause.5

    if whoring <= 15 and buttplug_size == 1: # LEVEL 06
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], как все прошло?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            $ sc34CG(1, 8)
            call her_main("Конечно же... это было ужасно...","annoyed","frown",xpos="base",ypos="base")
            m "Просто расскажи мне, что произошло, [hermione_name]..."
            call her_main("Мне никогда не было так неудобно в моей жизни, [genie_name]!","disgust","glance")
            call her_main("Я целый день не могла ни на чем сосредоточиться!","annoyed","annoyed")
            m "Почему?"
            call her_main("Каждый раз, когда я садилась в классе, она шевелилась внутри меня...","annoyed","angryL")
            her "Поэтому, естественно, мне пришлось приспособиться к тому, как сидеть, [genie_name]..."
            $ sc34CG(1, 9)
            call her_main("Но стало только хуже...","annoyed","angryL")
            m "Как думаешь, кто-то заметил ее у тебя?"
            call her_main("Понятия не имею...","annoyed","annoyed")
            $ sc34CG(1, 10)
            call her_main("Я сама едва могла думать... Не говоря уже о других.","annoyed","annoyed")
            m "Тебе было приятно?"
            call her_main("Приятно?","open","base")
            $ sc34CG(1, 12)
            call her_main("Если вам нравиться... Весь день дразнить мою задницу...","annoyed","down")
            call her_main("Тогда да, полагаю было...","annoyed","ahegao")
            $ sc34CG(1, 13)
            call her_main("А еще... такая невнимательность во время занятий может серьезно навредить моим оценкам....","angry","base")
            m "Я бы не беспокоился об этом. Только подумай о Гриффиндоре!"
            hide screen sccg
            call her_main("Говоря об этом...","annoyed","annoyed",xpos="right",ypos="base",trans="fade")
            m "Ах, да, совершенно верно."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], как все прошло?"
            show screen blktone
            call her_main("Все хорошо, [genie_name]...","open","base",xpos="right",ypos="base")
            call play_music("playful_tension") # SEX THEME.
            her "Вряд ли кто-нибудь заметил, что я ее ношу..."
            call her_main("...За исключением нескольких девушек из Когтеврана...","open","base",cheeks="blush")
            m "Что случилось?"
            call her_main("Я шла по коридору, направляясь на урок зельеварения...","open","closed")
            call her_main("И вдруг порыв ветра поднял мою юбку....","upset","wink")
            m "Порыв ветра? В помещении?"
            call her_main("Должно быть, он подул из окна...","soft","baseL")
            call her_main("Во всяком случае, три девушки, идущие позади меня, возможно... видели ее.","open","down")
            m "Они что-нибудь сказали тебе?"
            call her_main("Нет... Но я слышала, как они потом хихикали...","clench","down_raised")
            m "Ну, это похоже, на хорошо выполненную работу..."

        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            m "[hermione_name], как все прошло?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("Ужасно, [genie_name]. Просо ужасно...","scream","worriedCl",xpos="right",ypos="base")
            m "Что случилось?"
            call her_main("Случилась Плакса Миртл!","normal","worriedCl")
            m "Плакса Миртл?"
            call her_main("Эта надоедливая маленькая","annoyed","angryL")
            call her_main("Эта пробка сделала меня такой расстроенной, что на перемене я пошла в туалет для девочек...","annoyed","angryL")
            call her_main("Облегчиться...","annoyed","worriedL")
            call her_main("Когда вдруг этот надоедливый призрак высунул голову в дверь!","scream","angryCl")
            call her_main("Как будто, она плохо видит меня...","open","down")
            call her_main("Затем она начала кричать \'Гермиона носит анальную пробку\' на весь туалет!","scream","angry",emote="01")
            call her_main("К счастью, кабинки были пусты! Представьте, если бы в них кто-нибудь был!","annoyed","annoyed")
            m "Что ж, похоже, ты заработала свои очки."

    elif whoring <= 20 and buttplug_size == 1: # LEVEL 07
        if one_out_of_three == 1: ### EVENT (A)
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила свою задачу?"
            show screen blktone
            call her_main("Конечно.","open","base",xpos="right",ypos="base")
            m "Кто-нибудь заметил?"
            call her_main("Да... Ну, я должна была...","base","down")
            call her_main("Показать кое-кому...","base","glance")
            her "Я была в библиотеке и получая книги, я увидела Полумну..."
            her "Она читала за столом..."
            call her_main("Поэтому я решила подойти к ней и поговорить...","grin","baseL")
            call her_main("Она говорила о чем-то бессмысленном...","base","baseL")
            her "И я подумала, что если она это увидит..."
            her "Никто ей не поверит..."
            m "Хорошо..."
            call her_main("Так что я притворилась, будто уронила перо....","grin","baseL")
            m "Продолжай..."
            call her_main("Потом я обернулась перед ней....","base","down")
            her "И наклонилась..."
            her "...держа колени прямо..."
            call her_main("...давая ей отличный обзор...","base","ahegao_raised")
            m "Представляю..."
            m "Она что-нибудь сказала?"
            call her_main("Нет, [genie_name]...","soft","squintL")
            her "Но когда я обернулась, она не смотрела мне в глаза...."
            m "Хм..."
            call her_main("Я никогда не видела, чтобы кто-нибудь так краснел...","base","glance")
            m "Ну, похоже, ты заработала свои очки, даже больше."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            $ sc34CG(1, 9, 1)
            call her_main("Выполнила, [genie_name]...","open","closed",xpos="base",ypos="base")
            call her_main("Хотя я все еще не уверена, как относиться ко всему этому...","annoyed","worriedL")
            $ sc34CG(1, 11, 1)
            call her_main("Это начинает влиять на мои оценки....","annoyed","worriedL")
            call her_main("Я даже не могу сказать, каким зельям нас сегодня учили...","open","base")
            call play_music("playful_tension") # SEX THEME.
            call her_main("Я, Гермиона Грейнджер...","open","down")
            $ sc34CG(1, 12, 1)
            call her_main("Не училась в классе...","angry","down_raised")
            m "Ну, ты могла бы попробовать снять напряжение между уроками."
            $ sc34CG(1, 13, 1)
            call her_main("Ох, я пробовала... Но это не работает...","angry","base")
            her "Это просто делает следующее занятие сложнее..."
            $ sc34CG(1, 12, 1)
            call her_main("Сегодня, после зельеварения, я пошла в свою комнату, чтобы... успокоиться...","open","baseL")
            call her_main("Но на Травологии мне было еще хуже...","open","down")
            $ sc34CG(1, 11, 1)
            call her_main("Я была вынуждена трогать себя посреди класса на уроке...","clench","down_raised")
            call her_main("Как вы думаете, кто-нибудь заметил, [genie_name]?","open","squint",cheeks="blush")
            $ sc34CG(1, 9, 1)

            menu:
                "\"Что? Конечно нет, [hermione_name]!\"":
                    $ sc34CG(1, 8, 2)
                    call her_main("..............","base","baseL",cheeks="blush")
                    call her_main("Вы правы, [genie_name]...","base","down")
                    her "Я была очень осторожной..."
                    $ sc34CG(1, 12, 3)
                    call her_main("Очень тихой...","soft","ahegao")
                    call her_main("Едва издавала звуки...","grin","baseL")
                    hide screen sccg
                    call her_main("[genie_name], могу ли я получить очки, пожалуйста?","base","glance",xpos="right",ypos="base",trans="fade")
                    her "......"
                "\"Конечно, они заметили!\"":
                    $ sc34CG(1, 13, 2)
                    m "Ты искренне веришь, что никто не заметил, как ты трогаешь себя?"
                    call her_main("Я боялась, что вы скажите это, [genie_name]...","mad","worriedCl",tears="soft_blink")
                    m "Тебя окружали люди!"
                    call her_main("........","mad","worriedCl",tears="soft_blink")
                    hide screen sccg
                    call her_main("[genie_name], могу я сейчас получить очки, пожалуйста?","angry","base",tears="soft",xpos="right",ypos="base",trans="fade")
            m "Безусловно."

        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            $ sc34CG(1, 11)
            call her_main("Да, [genie_name]. Я выполнила.","open","closed",xpos="base",ypos="base")
            m "Отлично. Рассказывай подробности."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Ну, тут особо нечего рассказывать...","open","base")
            $ sc34CG(1, 12)
            her "Я посещала занятия..."
            her "Пыталась делать заметки."
            her "В целом, это был довольно обычный день..."
            $ sc34CG(1, 13)
            call her_main("Такой же обычный, на сколько и пробка в моей заднице.","annoyed","angryL")
            m "И никто не заметил?"
            call her_main("Думаю нет, [genie_name].","annoyed","annoyed")
            $ sc34CG(1, 11)
            m "Ну, я полагаю, что-нибудь интересное, не может происходить каждый день."
            hide screen sccg
            call her_main("...","annoyed","baseL",xpos="right",ypos="base",trans="fade")


    elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, я выполнила, [genie_name].","base","base",xpos="right",ypos="base")
            m "Ну? Как прошел твой день?"
            call her_main("Замечательно, [genie_name]...","base","ahegao_raised")
            m "Продолжай..."
            call play_music("playful_tension") # SEX THEME.
            $ sc34CG(1, 14, 1)
            call her_main("Ну, я придумала, как справиться с этой штукой, находящейся во мне весь день...","soft","squintL",xpos="base",ypos="base")
            m "Правда? И как же?"
            call her_main("До сих пор я подходила к этому неправильно...","open","baseL")
            call her_main("Я просто пыталась игнорировать это...","open","closed")
            her "И старалась слушать на уроках..."
            call her_main("Но это все, не работало...","upset","wink")
            call her_main("Я просто, слишком правильная...","base","down")
            $ sc34CG(1, 15, 2)
            call her_main("Поэтому я подумала, что мне просто нужно сосредоточиться на ней...","base","ahegao_raised")
            $ sc34CG(1, 16, 3)
            call her_main("Не обращать внимание на все остальное...","base","down")
            $ sc34CG(1, 17, 2)
            call her_main("...Принять это...","grin","dead")
            m "И как ты это сделала?"
            call her_main("Ну, если я ерзаю на стуле, пока я сижу в классе, этого почти достаточно...","base","glance")
            $ sc34CG(1, 16, 3)
            call her_main("Но когда я сижу на краю стула, пока ерзаю...","base","suspicious")
            $ sc34CG(1, 17, 2)
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "Так ты научилась доставлять себе удовольствие на занятиях."
            call her_main("Научилась, [genie_name].","base","down")
            her "Хотя я волнуюсь, что это действительно начнет влиять на мои оценки..."
            m "Ну, я уверен, что пропуск одного занятия в день ты сможешь наверстать."
            $ sc34CG(1, 15, 2)
            call her_main("Только одного?","angry","wink")
            m "Ты хочешь сказать, что провела все свои занятия, ублажая себя?"
            $ sc34CG(1, 17, 2)
            call her_main("..........","soft","ahegao")
            hide screen sccg
            call her_main(xpos="right",ypos="base",trans="fade")
            m "Хорошая работа, [hermione_name]."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, я выполнила, [genie_name].","base","base",xpos="right",ypos="base")
            call her_main("Но, эмм...","open","worried")
            m "...?"
            call her_main("Ну, я, возможно, получила немного больше внимания, чем ожидала...","disgust","down_raised")
            call her_main("...............","clench","down_raised")
            m "Расскажи мне, что случилось, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Возможно, меня сфотографировали несколько раз...","open","down")
            m "Фото..."
            call her_main("Ну, я была в библиотеке, занималась своими уроками...","annoyed","closed")
            her "Когда я пошла, чтобы получить копию книги Зигмунда Баджа о зельях."
            call her_main("Она была на нижней полке, мне пришлось встать на колени, чтобы добраться до нее...","annoyed","base")
            call her_main("Как вдруг я услышала вспышку фотоаппарата!","annoyed","angryL")
            her "Я обернулсь и увидела Колина Криви...."
            her "С огромной улыбкой на лице!"
            m "Ты позволила сделать фотографию с собой?!"
            call her_main("Я не позволяла себя фотографировать! Это было без моего согласия!","scream","angry",emote="01")
            call her_main("Я даже заставила его пообещать никому не показывать фото....","open","down")
            her "...в обмен мне пришлось позволить ему сделать еще несколько...."
            her "Но он утверждал, что больше никому не покажет...."
            m "И ты поверила ему?"
            call her_main("Конечно, [genie_name], он с Гриффиндора.","annoyed","closed")
            call her_main("Хотя эта мысль приходила мне в голову.","open","down")
            call her_main("Что если он распространит фотографии по всей школе.","clench","down_raised")
            call her_main("Представьте, что все смотрят на мои фото...","open","baseL")
            her "Все бы узнали, что я ношу..."
            call her_main("Каждый раз, когда кто-то бы видел меня, думал о том, вставлена ли эта штука в меня...","base","down")
            m "Это довольно продуманно."
            call her_main("Да, но я определенно не хочу, чтобы это произошло....","base","suspicious")
            m "Я уверен, что не хочешь..."
            call her_main("","base","glance")
            m "Это звучит как хорошо проделанная работа, [hermione_name]."

        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, я выполнила, [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Кто-нибудь заметил?"
            her "Может, несколько третьекурсников..."
            m "Хорошо, продолжай."
            call her_main("Это было на лестнице...","base","glance")
            her "Возможно, я немного увлеклась собой..."
            m "Что случилось, [hermione_name]?"
            call her_main("Ну, когда я шла в класс Прорицания, я оказалась перед группой студентов третьего курса...","base","suspicious")
            call her_main("И видя, как они шли позади меня на лестнице, они, возможно, заметили... Ее.","base","glance")
            m "Так ты намеренно показала ее группе мальчиков? Ты же не ожидаешь, что я дам тебе дополнительные очки за это?"
            call her_main("Конечно нет, [genie_name].","base","baseL",cheeks="blush")
            m "Тогда зачем это делать?"
            call her_main("Ну, это произошло как-то само...","open","squint",cheeks="blush")
            call her_main("Плюс выражение их лиц, когда они это заметили...","grin","dead")
            call her_main("Они едва смогли скрыть их...","soft","ahegao")
            m "Так тебе нравится, когда на тебя смотрят?"
            call her_main("Ну...","open","baseL")
            m "Молодец, [hermione_name]."
            call her_main("","base","down")

    elif whoring <= 19 and buttplug_size == 2: # LEVEL 06
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], ну как?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("Это было ужасно... просто ужас...","annoyed","frown",xpos="right",ypos="base")
            m "Что произошло, [hermione_name]..."
            call her_main("Это был противный профессор Снейп, [genie_name]!","annoyed","angryL")
            call her_main("Я никогда в жизни не была так смущена!","annoyed","annoyed")
            m "Что он сделал?"
            call her_main("Ну, в классе зельеварения я исправила его, когда показала, как правильно раздавить Дремоносный боб...","annoyed","angryL")
            her "Поэтому он заставил меня встать перед ним и показать ему как \'правильно\' ..."
            call her_main("И что еще хуже, он заставил меня сделать это перед классом....","annoyed","annoyed")
            m "Думаешь, кто-нибудь увидел?"
            call her_main("Все увидели!","disgust","down_raised")
            call her_main("Я даже едва смогла раздавить Боб, мои ноги так сильно дрожали...","clench","down_raised")
            m "Ну, похоже, ты заработала свои очки."
            call her_main(".......","annoyed","down")

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], как все прошло?"
            show screen blktone
            call her_main("Хорошо, [genie_name]...","open","base",xpos="right",ypos="base")
            call play_music("playful_tension") # SEX THEME.
            her "Каждый из второгодок \"Пуффендуя\" сделал мне комплимент..."
            call her_main("...они сказали, что она выглядит мило...","grin","baseL")
            m "Что-нибудь еще?"
            call her_main("Ну, увидев, как они любезны...","base","down")
            call her_main("Я немного задрала юбку для них....","soft","squintL")
            m "Ты показала им ее?"
            call her_main("Они были так добры ко мне...","open","baseL")
            call her_main("И они смогли увидеть большую часть...","base","down")
            m "Они что-нибудь сказали тебе?"
            call her_main("Нет... Но взгляды на их лицах...","base","glance")
            m "Хорошо, это звучит как хорошо выполненная работа..."

        elif one_out_of_three == 3: ### EVENT (C) cat swatting it
            label buttplug_magic_show:
                pass
            $ buttplug_magic_known = True
            m "[hermione_name], как все прошло?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("Что вы наделали?!","scream","worriedCl",xpos="right",ypos="base")
            m "Что случилось?"
            call her_main("Почему вы не сказали мне, что эта \'штука\' проклята!","normal","worriedCl")
            m "Проклята?"
            call her_main("Она вибрирует!","annoyed","angryL")
            m "Правда? Как?"
            call her_main("Когда ее дернуть...","annoyed","angryL")
            m "Разве твоя юбка не должна была ее прикрыть?"
            call her_main("Я думаю, что она живая...","annoyed","worriedL")
            call her_main("Все, что я знаю, это когда мой кот Живоглот дернул за нее, она завелась! !","scream","angryCl")
            m "Насколько все плохо?"
            call her_main("Это было абсурдно! Я едва могла стоять...","open","worriedCl")
            call her_main("Но потом Живоглот подумал, что это какая-то игра... Он не оставил ее в покое...","shock","worriedCl")
            call her_main("Вибрации были настолько интенсивными, что мои колени не выдержали, и я рухнула на кровать!","angry","down_raised")
            call her_main("Затем он просто играл с ней часами...","angry","wink")
            m "Ты все еще готова носить ее в будущем?"
            call her_main("Наверное... Теперь, когда я знаю, как это работает.","upset","closed")
            call her_main("Я просто должна держать ее подальше от Живоглота...","angry","down_raised")
            call her_main("{size=-6}или нет...{/size}","soft","ahegao")
            m "Хорошая работа, [hermione_name]."

    elif whoring <= 23 and buttplug_size == 2: # LEVEL 07
        if one_out_of_three == 1: ### EVENT (A) luna plays with it in the library
            if not buttplug_magic_known:
                jump buttplug_magic_show
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], повеселилась?"
            show screen blktone
            call her_main("Можно сказать и так.","base","down",xpos="right",ypos="base")
            m "Произошло что-нибудь интересное?"
            call her_main("Да... Ну, было...","base","down")
            call her_main("Кое-кто...","base","worriedCl")
            call her_main("Трогал ее...","base","glance")
            m "Хмммм..."
            call her_main("Это снова была Полумна Лавгуд.","grin","baseL")
            call her_main("Мы закончили тем, что сидели рядом друг с другом в классе.","soft","baseL")
            her "Мы обсуждали школу, одежду..."
            m "Да, выкладывай..."
            call her_main("Она сказала, что думает, что мой хвост милый...","grin","baseL")
            m "Продолжай..."
            call her_main("Потом она вежливо спросила, можно ли к нему прикоснуться...","base","down")
            call her_main("Я не смогла отказать...","open","baseL")
            call her_main("И я... разрешила ей провести остаток урока... дергая за него...","soft","squintL")
            m "Понятно..."
            m "Поняла ли она, что происходит?"
            call her_main("Возможно... это чувство такое приятное, что было трудно сдержаться.","soft","ahegao")
            her "Но я думаю, что это заставило ее захотеть больше играть с ним..."
            m "Хм..."
            call her_main("Я думаю, это был лучший урок...","grin","dead")
            m "Ну, похоже, ты заработала свои очки, и даже с лихвой."

        elif one_out_of_three == 2: ### EVENT (B)
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Я выполнила, [genie_name].","open","closed",xpos="right",ypos="base")
            call her_main("Только... Эм...","grin","baseL")
            m "Что на это раз, [hermione_name]?"
            call her_main("Ну... Вы знаете мою подругу...","base","base")
            her "Джинни Уизли..."
            call her_main("Я рассказала ей про хвост....","base","baseL",cheeks="blush")
            her "И как он работает..."
            m "Рассказывай, [hermione_name]."
            call her_main("Ну, мы решили пропустить урок Травологии...","open","baseL")
            call play_music("playful_tension") # SEX THEME.
            call her_main("И потом она вроде как схватила за него...","grin","ahegao")
            call her_main("И просто дергала его так активно...","grin","dead")
            her "После этого я была не в себе..."
            g9 "И ты вернула должок?"
            if touched_by_boy == True:
                call her_main("Эрр... возможно...","open","squint",cheeks="blush")
                m "Что ты сделала?"
                call her_main("Я не хочу говорить слишком много, [genie_name].","base","baseL",cheeks="blush") # :)
                her "Но после того, как она увидела, что она делает со мной..."
                her "Она настояла, чтобы я ее отпустила...."
                call her_main("Это все, что я скажу...","base","down") # :)
                m "Хмммм, ну ты заработала свои очки, [hermione_name], даже если ты не рассказываешь о произошедшем..."
            else:
                call her_main("...Нет.","open","down")
                m "Почему нет?"
                call her_main("Ну, я не против позволить ей дотрагиваться до хвоста, [genie_name].","annoyed","base") # :)
                her "И все остальное..."
                m "Очень хорошо, [hermione_name]..."

        elif one_out_of_three == 3: ### EVENT (C) called a slut by slytherin
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, [genie_name]. Я выполнила.","annoyed","angryL",xpos="right",ypos="base")
            m "Восхитительно. Расскажи мне больше."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Ну, тут особо нечего рассказывать...","open","down")
            her "Я посещала занятия..."
            her "Готовилась к предстоящему экзамену по зельям..."
            call her_main("Это был обычный день, за исключением группы этих мерзких \"Слизеринцев\"...","annoyed","angryL")
            call her_main("Я занималась своими делами по дороге на занятия, после услышала, как они назвали меня \"Анальной шлюхой\".","angry","down_raised")
            m "Ты ответила им что-нибудь?"
            call her_main("И опуститься до их уровня...","annoyed","angryL")
            m "Ну, я полагаю, это к лучшему."


    elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+
        if one_out_of_three == 1: ### EVENT (A) groped by first years
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], как прошел день?"
            show screen blktone
            call her_main("Ужасно, на меня напала группа бешеных студентов, [genie_name].","scream","angryCl",xpos="right",ypos="base")
            m "Напала? Сколько их было?"
            call her_main("Шесть первокурсников, [genie_name]...","annoyed","angry")
            m "На тебя напали первокурсники?"
            call play_music("playful_tension") # SEX THEME.
            call her_main("Возможно, я немного преувеличила...","open","worriedL")
            m "Так что произошло?"
            call her_main("Ну, я сидела в библиотеке, занимаясь своими делами...","annoyed","angryL")
            call her_main("Как вдруг, из ни откуда появилась группа первокурсников и начала задавать вопросы...","angry","worriedCl")
            call her_main("\"Он пушистый\"...","annoyed","angryL")
            call her_main("\"Почему ты носишь его\"...","angry","down_raised")
            call her_main("\"Это приятно\"...","base","down")
            call her_main("\"Можно нам потрогать\"...","base","down")
            call her_main("\"Можешь повилять им\"...","angry","wink")
            m "И что ты сделала?"
            call her_main("Ну, я заставила их пообещать молчать об этом...","upset","closed")
            call her_main("Но в обмен я должна была позволить им потрогать...","open","down")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "И ты позволила группе невинных первокурсников прикоснуться к своей анальной пробке?..."
            call her_main("Это звучит зловеще, когда вы так говорите.","annoyed","angryL")
            her "Все, что я сделала, это отвела их в уединенную часть библиотеки и позволила потрогать мой хвост..."
            m "Ну, тогда все в порядке..."
            call her_main(".......","base","down")
            m "Ты наслаждалась этим?"
            call her_main("..........","angry","base")
            call her_main("Искренне, [genie_name].... Это был самый приятный опыт в моей жизни...","grin","dead")
            call her_main("Все их руки прикасались к нему...","soft","ahegao")
            call her_main("По очереди...","grin","ahegao")
            call her_main("Все это время он вибрировал...","base","down")
            call her_main("Я чуть не потеряла сознание.","silly","dead")
            call her_main("Я даже пыталась их остановить....","silly","ahegao")
            call her_main("Но они продолжали...","grin","ahegao")
            m "Хорошая работа, [hermione_name]."

        elif one_out_of_three == 2: ### EVENT (B) glory hole with astoria
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], ты выполнила свою задачу?"
            show screen blktone
            call her_main("Да, я выполнила, [genie_name]...","base","base",xpos="right",ypos="base")
            call her_main("Вы знаете, что в женском туалете между кабинками есть дырки?","soft","base")
            m "Я не знал, но какое это имеет отношение к твоей анальной пробке?"
            call her_main("Ну, я заметила, что отверстия такого же диаметра, как и хвост...","grin","baseL")
            call her_main("...............","grin","worriedCl")
            m "Продолжай, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Я смогла вставить его...","base","down")
            m "Что?"
            call her_main("Ну, я была в кабинке, заканчивала...","base","baseL")
            her "Когда девушка зашла в другую кабинку."
            call her_main("Я не уверена, но думаю, она могла быть из \"Слизерина\"...","upset","wink")
            call her_main("Поэтому я решила прижаться ягодицами к стене и просунуть хвост!","smile","baseL")
            m "Она прикасалась к нему?"
            call her_main("Не сразу...","base","baseL")
            call her_main("Но после того, как я немного пошевелила им, она в конце концов решилась...","grin","baseL")
            call her_main("Сначала ей было любопытно, но в итоге она начала играться с ним...","open","baseL")
            call her_main("Гладила его... Трясла его... Я даже думаю, возможно, она лизнула его...","soft","ahegao")
            her "...Представьте себе... Слизеринка, облизывающая что-то, что было внутри меня..."
            her "Это было невероятно... Я едва могла стоять, пока это происходило..."
            m "Ты выяснила, кто это был?"
            call her_main("Выяснила, [genie_name].","open","worried")
            call her_main("Это было за обедом, в Большом зале.","open","closed")
            call her_main("По пути, чтобы присесть, я шла мимо столов Слизерина...","open","closed")
            call her_main("Когда я увидел эту маленькую... мегеру, Асторию Гринграсс.","base","suspicious")
            her "Она не могла отвести от него глаз..."
            call her_main("Представьте себе... Астория Гринграсс... чистокровка, лизала мой...","grin","ahegao")
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao")
            m "Похоже, ты заработала сегодня свои очки, [hermione_name]."
            call her_main("...{size=-7}(Я бы сделала это за бесплатно...){/size}","base","down")

        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, выполнила, [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Произошло что-нибудь интересное?"
            her "Вы знаете близняшек Патил, [genie_name]?"
            m "Нет, но продолжай."
            call her_main("Они шли по коридору позади меня...","base","glance")
            her "Клянусь, я слышала, как они шептались друг с другом..."
            call her_main("И я подумала, что могу дать им тему для разговора...","base","suspicious")
            call her_main("Поэтому я остановилась, выпрямила колени и наклонилась, насколько смогла...","base","glance")
            m "Ты разоблачила себя, просто так?"
            call her_main(".......","base","baseL",cheeks="blush")
            m "Очень хорошо, [hermione_name]!"

    elif buttplug_size == 3:
        if one_out_of_three == 1: #Groped by first years again...
            m "[hermione_name], как прошел твой день?"
            show screen blktone
            call her_main("Ужасно, меня атаковала группа бешеных учеников, [genie_name].","scream","angryCl",xpos="right",ypos="base")
            m "Атоковала? Сколько их было?"
            call her_main("Шесть первокурсников, [genie_name]...","annoyed","angry")
            m "Ты была атакована первокурсниками?"
            call play_music("playful_tension") # SEX THEME.
            call her_main("Возможно, я немного преувеличила...","open","worriedL")
            m "Так, что же произошло?"
            call her_main("Ну, я сидела в библиотеке, занимаясь своими делами...","annoyed","angryL")
            call her_main("Как вдруг, из ниоткуда появилась группа первокурсников и начала задавать вопросы...","angry","worriedCl")
            call her_main("\"Он пушистый\"...","annoyed","angryL")
            call her_main("\"Почему ты носишь его\"...","angry","down_raised")
            call her_main("\"Это приятно\"...","base","down")
            call her_main("\"Можно нам потрогать\"...","base","down")
            call her_main("\"Можешь повилять им\"...","angry","wink")
            m "И что ты сделала?"
            call her_main("Ну, я заставила их пообещать молчать об этом...","upset","closed")
            call her_main("Но в обмен я должна была позволить им потрогать его...","open","down")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "И ты позволила группе невинных первокурсников прикоснуться к твоей анальной пробке..."
            call her_main("Это звучит зловеще, когда вы так говорите...","annoyed","angryL")
            her "Все, что я сделала, это отвела их в уединенную часть библиотеки и позволила потрогать мой хвост..."
            m "Ну, тогда все в порядке..."
            call her_main(".......","base","down")
            m "Ты наслаждалась этим?"
            call her_main("..........","angry","base")
            call her_main("Искренне, [genie_name].... Это был самый приятный опыт в моей жизни...","grin","dead")
            call her_main("Все их руки прикасались к нему...","soft","ahegao")
            call her_main("По очереди...","grin","ahegao")
            call her_main("Все это время он вибрировал...","base","down")
            call her_main("Я чуть не потеряла сознание.","silly","dead")
            call her_main("Я даже попыталась их остановить...","silly","ahegao")
            call her_main("Но они просто продолжали...","grin","ahegao")
            m "Хорошая работа, [hermione_name]."

        elif one_out_of_three == 2: ### Speech in McGonagall's class
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, выполнила, [genie_name]...","base","base",xpos="right",ypos="base")
            call her_main("Вы знаете, что в женском туалете между кабинками есть дырки?","soft","base")
            m "Я не знал, но какое это имеет отношение к твоей анальной пробке?"
            call her_main("Ну, я заметила, что отверстия такого же диаметра, как и хвост...","grin","baseL")
            call her_main("...............","grin","worriedCl")
            m "Продолжай, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Я смогла вставить его...","base","down")
            m "Что?"
            call her_main("Ну, я была в кабинке, заканчивала...","base","baseL")
            her "Когда девушка зашла в другую кабинку."
            call her_main("Я не уверена, но думаю, она могла быть из \"Слизерина\"...","upset","wink")
            call her_main("Поэтому я решила просунуть свой хвост!","smile","baseL")
            m "Она прикасалась к нему?"
            call her_main("Не сразу...","base","baseL")
            call her_main("Но после того, как я немного пошевелила им, она в конце концов решилась...","grin","baseL")
            call her_main("Сначала ей было любопытно, но в итоге она начала играться с ним...","open","baseL")
            call her_main("Гладила его... трясла... Я даже думаю, возможно, она лизнула его...","soft","ahegao")
            her "...Представьте себе... Слизеринка, облизывающий что-то, что было во мне..."
            her "Это было невероятно... Я едва могла стоять, пока это происходило..."
            m "Ты выяснила, кто это был?"
            call her_main("Выяснила, [genie_name].","open","worried")
            call her_main("Это было за обедом, в Большом зале.","open","closed")
            call her_main("По пути, к своему столику, я шла мимо столов Слизерина...","open","closed")
            call her_main("Когда я увидела эту маленькую... мегеру, Асторию Гринграсс.","base","suspicious")
            her "Она не могла отвести от него глаз..."
            call her_main("Представьте себе... Астория Гринграсс... чистокровка, лизала мой...","grin","ahegao")
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao")
            m "Похоже, сегодня ты заработала свои очки, [hermione_name]."
            call her_main("...{size=-7}(Я бы сделала это и бесплатно...){/size}","base","down")

        elif one_out_of_three == 3: ### Sits down in hall with it showing
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], ты выполнила свое задание?"
            show screen blktone
            call her_main("Да, выполнила, [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Что-нибудь интересное произошло сегодня?"
            her "Вы знаете Близняшек Патил, [genie_name]?"
            m "Нет, но продолжай."
            call her_main("Они шли по коридору позади меня...","base","glance")
            her "Клянусь, я слышала, как они шептались друг с другом..."
            call her_main("И я подумала, что могу дать им тему для разговора...","base","suspicious")
            call her_main("Поэтому я остановилась, выпрямила колени и наклонилась, насколько смогла...","base","glance")
            m "Ты разоблачила себя, просто так?"
            call her_main(".......","base","baseL",cheeks="blush")
            m "Очень хорошо, [hermione_name]!"

    $ gryffindor += current_payout #55
    m "\"Гриффиндор\" получает [current_payout] очков!"
    her "Спасибо, [genie_name]."

    $ hg_ps_Buttplug_OBJ.points += 1
    $ hg_ps_Buttplug_OBJ.complete = True
    $ hg_ps_Buttplug_OBJ.inProgress = False

    call set_h_buttplug("remove")

    jump hg_pr_transition_block
