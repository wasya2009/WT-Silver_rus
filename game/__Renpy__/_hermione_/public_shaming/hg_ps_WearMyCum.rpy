

### Wear My Cum ###

label hg_ps_WearMyCum: #Walk around school covered in genies cum
    hide screen hermione_main
    with d3

    m "{size=-4}(Попросить ее ходить со спермой на лице?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Да, сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump silver_requests

    m "[hermione_name]?"
    call her_main("Да, [genie_name].",xpos="right",ypos="base")

    call play_music("playful_tension") # SEX THEME.
    m "Сегодня у меня будет к тебе просьба."
    call her_main("Какая?","base","base")
    m "Я хочу чтобы ты отправилась в свой класс."
    call her_main("Конечно...","base","base")
    m "После того как я кончу на тебя...."

    if whoring < 10:
        jump too_much
    elif whoring < 15:
        jump hg_ps_WearMyCum_Scene_1
    elif whoring < 20:
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 2
    else:
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 3







label hg_ps_WearMyCum_Scene_1:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Что?!!","shock","wide")
    call her_main("Вы серьезно","angry","angry")
    call her_main("Вам мало кончать на меня наедине!","annoyed","annoyed")
    call her_main("А теперь хотите при всех?","angry","annoyed",emote="01")
    call her_main("Я думаю мне лучше уйти...","annoyed","angry")
    m "Подожди, подожди, подожди."
    m "А что, если никто не сможет это увидеть?"
    call her_main("Я полагаю, что это будет не страшно...","annoyed","annoyed")
    call her_main("Но в чем смысл, если они этого не видят?","annoyed","worriedL")
    m "Ты будешь знать что она там."
    call her_main("Хмммм...","annoyed","angryL") #Haggle here
    call her_main("Сколько я получу?","annoyed","suspicious")
    m "30 очков."
    call her_main("30! Я ожидаю как минимум 70 за такой грязный поступок!","scream","worriedCl")
    m "40."
    call her_main("60!","scream","angryCl")
    m "50 очков, окончательное предложение."
    call her_main("Хорошо, я сделаю это.","annoyed","worriedL")
    m "Правда?"
    call her_main("Пока никто не видит, я не вижу в этом большой проблемы.","annoyed","angryL")
    m "Отлично. По рукам?"
    call her_main("...","base","down")

    #Start jerk off chibis
    hide screen hermione_main
    call blkfade

    call her_chibi("hide")
    call gen_chibi("handjob","desk","base")

    show screen chair_left
    hide screen desk
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call her_head("Почему вы заставляете меня делать это?, [genie_name]?","angry","base")
    m "Что ты имеешь в виду?"
    call her_head("Почему вы заставляете меня дразнить вас...","angry","down_raised")
    call her_head("Чтобы кончить на меня...","soft","ahegao")
    call her_head("И заставляете ходить так по школе?","open","worriedCl")
    m "Я не заставляю тебя этого делать."
    m "Я просто попросил тебя, сделать это."
    call her_head("Но если я этого не сделаю, Гриффиндор потеряет Кубок.","shock","worriedCl")
    m "И?"
    call her_head("Гарри и Рон будут так расстроены...","angry","worried")
    m "Так вот почему ты это делаешь? Для этих двух мальчиков?"
    call her_head("Как бы... Я не уверена, что они были бы слишком расстроены, хотя","annoyed","worriedL")
    m "Ты уверена, может быть тебе это нравится?"
    call her_head("Что?","upset","wink")
    m "Приходишь когда я зову тебя."
    m "Делаешь все, что я тебе говорю."
    m "Делаешь все эти грязные веши перед своими сверстниками, потому, что я тебе это говорю."
    call her_head("...","disgust","down_raised")
    m "Знаешь что я скажу, я сделаю все интереснее."
    m "Я кончу на тебя, и ты будешь ходить так на всех уроках, и Гриффиндор получит 50 очков."
    call her_head("Что в этом интересного?","disgust","glance")
    m "Я позволю тебе выбрать куда я кончу."
    call nar(">Она берет твой член в руку.")
    call her_head("Вы позволите мне выбрать?","smile","baseL")
    m "Куда угодно, главное на тебя. Это может быть даже твоя обувь."
    call her_head("Хорошо...","base","squint")
    m "Решай быстрее [hermione_name], твои уроки скоро начнутся."
    call nar(">Она начинает дрочить твой член с новой силой.")
    m "Итак, куда мне кончить?"
    call her_head("Я не уверена.","upset","wink")
    call her_head("Я пытаюсь подумать о том, где ее никто не увидит.","upset","wink")
    m "Тебе нужно думать быстрее!"
    call her_head("Почему?","angry","wink")
    g9 "Потому, что я собираюсь кончать!"
    call her_head("Уже? Куда же мне-","angry","wide")

    menu:
        "-Промолчать-": # Cum under shirt
            $ cum_location = 1
            call nar(">Гермиона быстро поднимает рубашку...","start")
            call nar(">Своим членом ты чувствуешь ее невероятно мягкие груди которые трутся об кончик твоего члена, пока ты кончаешь!","end")
            g4 "{size=+5}АРГХ! ДА!!!{/size}"

            hide screen hermione_main
            hide screen bld1
            call gen_chibi("cumming_under_shirt")
            call cum_block
            pause.5

            call her_head("!!!!!!!!!!!","shock","wide")

            $ aftersperm = True

            call her_main("Ну, это не такая плохая идея...","upset","wink")
            m "Я думаю ни кто не заметит."
            call her_main("Лучше не надо.","angry","angry")

        "\"Не останавливайся, [hermione_name]!\"": # Cum on skirt
            $ cum_location = 2

            call nar(">Гермиона продолжает дрочить твой член, ее взгляд следит за твоим членом.")
            g4 "Приготовься шлюха, я сейчас кончу!!"
            call her_head("Подождите, куда я должна-","angry","worried")
            g9 "{size=+5}АРГХ! ДА!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.

            hide screen hermione_main
            hide screen bld1
            call gen_chibi("cumming_on_shirt")
            call cum_block
            pause.5

            $ u_sperm = "characters/hermione/face/auto_11.png"
            $ uni_sperm = True

            call her_main("!!!!!!!!!!!","shock","wide")
            m "Вот так, получай шлюха."
            call her_main("...","annoyed","down")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause")
            call ctc

            call her_main("Это все [genie_name].","annoyed","ahegao")
            m "Может хочешь поцеловать его на удачу?"
            call her_main("Я так не думаю.","annoyed","angryL")
            m "Тогда это все [hermione_name]."

        "\"Направь его на лицо!\"":
            $ cum_location = 3

            call nar(">Гермиона наклоняется и подставляет лицо к члену.")
            m "Приготовься шлюха, Уже совсем близко!"
            call her_head("...","scream","wide_stare")
            g9 "{size=+5}АРГХ! Да!!!{/size}"
            call her_head("Я не...","clench","down_raised")

            call nar(">В последний момент Гермиона отворачивается от члена.","start")
            call nar(">Ты кончаешь ей на голову, покрывая ее волосы своей спермой","end")

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt")
            call cum_block
            pause.5

            $ u_sperm = "characters/hermione/face/auto_12.png"
            $ uni_sperm = True

            call her_main("!!!!!!!!!!!","shock","wide")
            m "Да... Я теперь чувствую себя намного лучше..."
            call her_main("..............","normal","worriedCl")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause")
            call ctc

            call her_main("Как вы могли!","scream","worriedCl")
            m "Как я мог?"
            call her_main("Вы сказали, что хотите кончить мне на лицо!","scream","angryCl")
            m "Ну да."
            call her_main("Зачем вы мне это сказали!","mad","worriedCl",tears="soft_blink")
            call her_main("Если бы я не увернулась в последнюю секунду, то все мое лицо было бы в сперме!","angry","base",tears="soft")
            m "Ты меня не слушала."
            call her_main("Что?","angry","worried")
            m "Я сказал, что моя сперма должна быть на тебе."
            m "Я никогда не говорил, где."
            call her_main("Вы имеете в виду, я не должна была...","annoyed","worriedL")
            m "Вот именно."

    hide screen hermione_main
    call blkfade

    ">Ты убрал свой член обратно в мантию."

    call gen_chibi("hide")
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    call hide_blkfade


    m "Ох, и одна последняя вещь, прежде чем отправишься в класс."
    call her_main("Да...","annoyed","annoyed",xpos="right",ypos="base")
    m "Если ты вернешься сюда после уроков без следов спермы на себе, Слизерин получит 200 очков."
    call her_main("{size=+10}200! Это не справедливо!{/size}","shock","wide")
    m "Это будет несправедливо, если ты ее смоешь."
    call her_main("...","angry","angry")

    jump end_hg_pf




label hg_ps_WearMyCum_Scene_2:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Снова?","shock","wide")
    call her_main("Вы можете быть серьезнее!","angry","angry")
    call her_main("Я уже позволяла вам делать это со мной один раз, разве этого не достаточно?","annoyed","annoyed")
    m "Достаточно будет когда я это скажу."
    m "Кроме того, в прошлый раз ты не особо была против!"
    call her_main("Ну я не против...","annoyed","base")
    call her_main("В этот раз она также будет спрятана?","annoyed","worriedL")
    m "Это по желанию."
    call her_main("Хммм...","annoyed","angryL") #Haggle here
    call her_main("Сколько я получу на этот раз?","annoyed","suspicious")
    m "20 очков."
    call her_main("20! В прошлый раз мы договорились на 50!","scream","worriedCl")
    m "40."
    call her_main("70!","scream","angryCl")
    m "50 очков, окончательное предложение."
    call her_main("80 и я не буду прятать ее от других.","base","glance")
    m "Правда?"
    call her_main("Пока она не слишком очевидна.","base","down")
    m "По рукам."
    call her_main("...","base","down")

    #Start jerk off chibis
    hide screen hermione_main
    call blkfade

    call her_chibi("hide")
    call gen_chibi("handjob","desk","base")

    show screen chair_left
    hide screen desk
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call her_head("Почему вы просите меня сделать это? [genie_name]?","angry","base")
    m "Снова вопросы?"
    m "Позволь мне задать встречный вопрос."
    call her_head("Ладно...","angry","down_raised")
    m "Почему ты мне дрочишь [hermione_name]?"
    call her_head("Потому что вы меня попросили...","soft","ahegao")
    m "И это единственная причина?"
    call her_head("Нет...","open","worriedCl")
    m "Ты уверена?"
    m "Тогда какие еще у тебя причины?"
    call her_head("Если я этого не сделаю, Гриффиндор потеряет лидерство.","shock","worriedCl")
    m "Ты снова врешь?"
    call her_head("Это не ложь...","angry","worried")
    m "Что тебе важнее, выйграть Кубок Хогвартса или сделать меня счастливым?"
    call her_head("Может... А я не могу выбрать оба варианта?","annoyed","worriedL")
    m "Можешь..."
    call her_head("Хорошо","base","squint")
    m "Но я хочу, чтобы ты была честной."
    m "Так что я собираюсь дать тебе выбор."
    m "Ты можешь остановиться прямо сейчас, и уйти, и я дам тебе 80 очков. Тем не менее, я буду очень расстроен."
    call her_head("Или?","open","base")
    m "Или, ты можешь продолжить, и потом ходить с моей спермой по школе, но ты не получишь очки."
    call her_head("НЕ ПОЛУЧУ ОЧКОВ?","scream","worriedCl")
    m "Ни одного. Но ты сделаешь меня очень счастливым."
    call her_head("Может вы просто заплатите мне за то, что я буду ходить в вашей сперме?","angry","worriedCl",emote="05")
    m "Нет."
    call nar(">Ты чувствуешь, как ее руки сжались вокруг твоего члена.")
    call her_head("Вы заставляете меня выбирать? Между 80-ю очками за просто так.","annoyed","annoyed")
    call her_head("Или без очков, но я буду ходить с вашей спермой на себе.","angry","annoyed",emote="01")
    m "Все верно [hermione_name]."
    call her_head("{size=-5}Хорошо...{/size}","disgust","down_raised")
    m "Поторопись [hermione_name], скоро начнутся уроки, тебе нужно принять решение."
    call nar(">Она начинает дрочить твой член с новой силой.")
    call her_head("...","annoyed","suspicious")
    call her_head("Надеюсь вы это оцените.","annoyed","angryL")
    m "Ох, я это очень ценю!"
    call her_head("Правда?","open","base")
    g9 "Сейчас ты узнаешь как сильно я это ценю!"
    call her_head("Что, уже? Куда я должна-","angry","wide")

    menu:
        "-Промолчать-": # Legs
            $ cum_location = 4

            call nar(">Гермионо дрочит твой член, она стыдливо отводит взгляд изредка смотря на член.")
            g4 "Приготовься шлюха, я сейчас кончу!"
            call her_head("Подождите, куда я должна-","angry","worried")
            g9 "{size=+5}АХ! ДА!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt")
            call cum_block
            pause.5

            $ u_sperm = "characters/hermione/face/auto_13.png"
            $ uni_sperm = True

            call her_main("!!!!!!!!!!!","shock","wide")

            m "Отлично, все на твоих сочных бедрах."
            call her_main("...","annoyed","down")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause")
            call ctc

            call her_main("Это все [genie_name].","annoyed","ahegao")
            m "Может хочешь поцеловать его на удачу?"
            call her_main("...{p}...","base","ahegao_raised")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("handjob_kiss")
            $ renpy.play('sounds/kiss.mp3')
            with kissiris
            call ctc

            call gen_chibi("cumming_on_shirt_pause")
            m "Хорошая девочка."

        "\"Просто продолжай [hermione_name]!\"": # Cum on shirt front
            $ cum_location = 5

            call nar(">Гермионо дрочит твой член, ее взгляд сосредоточен на нем.")
            g4 "Приготовься шлюха, я сейчас кончу!"
            call her_head("...","angry","worried")
            g9 "{size=+5}Ах! ДА!!! ПРЯМО НА ТВОИ СИСЬКИ!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt")
            call cum_block
            pause.5

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True

            call her_main("!!!!!!!!!!!","shock","wide")
            m "Вот и все , это все для тебя шлюха."
            call her_main("...","annoyed","down")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause")
            call ctc

            call her_main("Это все?","annoyed","ahegao")
            m "Все!"
            call her_main("Я думаю мне уже нужно идти...","annoyed","down")

        "\"Подставь свое лицо, шлюха!\"":
            $ cum_location = 6

            call nar(">Гермиона наклоняется и выставляет лицо перед членом.")
            m "Приготовься шлюха, я сейчас кончу!"
            call her_head("...","scream","wide_stare")
            g9 "{size=+5}АХ! ДА!!!{/size}"
            call her_head("...","clench","down_raised")
            call nar(">Ты кончаешь на ее лицо, полностью заливая спермой.")

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            hide screen bld1
            call gen_chibi("cumming_on_shirt")
            call cum_block
            pause.5

            $ u_sperm = "characters/hermione/face/auto_07.png"
            $ uni_sperm = True

            call her_main("!!!!!!!!!!!","shock","wide")
            m "Да... Я чувствую себя намного лучше..."
            call her_main("..............","normal","worriedCl")

            hide screen hermione_main
            hide screen bld1
            with d3
            call gen_chibi("cumming_on_shirt_pause")
            call ctc

            call her_main("Как вы могли!","scream","worriedCl")
            m "Что я мог?"
            call her_main("Вы кончили мне на лицо","scream","angryCl")
            m "Ну да."
            call her_main("Почему вы попросили меня сделать это!","mad","worriedCl",tears="soft_blink")
            call her_main("Я полностью покрыта вашей спермой!","angry","base",tears="soft")
            m "Ты меня не слушала."
            call her_main("...","angry","worried")
            m "Я сказал, что моя сперма должна быть на тебе."
            m "Я не говорил где."
            call her_main("Вы сказали мне сделать это, хотя...","annoyed","worriedL")

    hide screen hermione_main
    call blkfade

    ">Ты заправляешь свой член обратно в свою мантию."

    call gen_chibi("hide")
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    call hide_blkfade

    m "О, и последнее, прежде чем отправиться в класс."
    call her_main("Да...","soft","ahegao",xpos="right",ypos="base")
    m "Если ты вернешься после занятий без следов спермы, я буду очень расстроен."
    call her_main("Да [genie_name].","base","ahegao_raised")
    m "Повеселись. Передавай привет своим друзьям от меня."
    call her_main("...","base","closed")

    jump end_hg_pf


label hg_ps_WearMyCum_Scene_3:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Вы серьезно?","shock","wide")
    call her_main("Я могу?","grin","ahegao")
    m "Что ж-"
    call her_main("Я хочу спросить вас, я увижу ваше довольное лицо, как в прошлый раз, [genie_name].","smile","happyCl",emote="06")
    call her_main("Я даже сделаю это бесплатно, если это сделает вас счастливее!","base","ahegao_raised")
    m "Правда?"
    m "Тогда начинай!"
    #Start jerk off chibis
    hide screen hermione_main
    hide screen bld1
    with d3
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3

    hide screen genie
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "handjob_ani"
    show screen chair_left
    show screen g_c_u
    show screen desk_02
    hide screen blktone
    hide screen hermione_walk_01
    hide screen blkfade
    $ hermione_head_ypos = 235
    m "О боже, ты хороша в этом, [hermione_name]!"
    call her_head("Спасибо... Я думала о том, о чем вы спрашивали меня в прошлый раз...","soft","ahegao")
    m "Прошлый раз?"
    call her_head("О том, почему я делаю это... продаю вам эти услуги.","upset","closed")
    call her_head("В начале это было ради очков для \"Грифиндора\", чтобы выиграть Кубок факультетов...","angry","wink")
    call her_head("Но в последнее время...","base","down")
    call her_head("...Это было больше, чем... теперь я делаю это, чтобы сделать вас счастливым, [genie_name].","base","glance")
    call her_head("Потому, что делает вас счастливым, то делает и меня...","base","suspicious")
    m "Это здорово... но что бы действительно сделать меня счастливым сейчас, сосредоточься немного больше на задаче в своих руках..."
    call her_head("Ой! Конечно, [genie_name]...","open","worriedCl")
    call her_head("Может хотите немного больше?","open","closed")
    m "Это помогло бы..."
    call her_head("Вообщем... Вообщем я тут думала обо всем этом. Я так сильно хотела придти к вам и попросить, чтобы вы снова обкончали меня!","base","down")
    call her_head("Я стала такой шлюхой [genie_name], я больше не о чем не могу думать... Сидеть в классе вся покрытая вашей {image=textheart}спермой{image=textheart}","grin","ahegao")
    call her_head("Я фантазирую как она впитывается в мою одежду и что я никогда не смогу отмыть ее. Я фантазирую как вы постоянно кончаете на меня. Таким образом, все узнают, кто я.","grin","dead")
    call her_head("Нет, я не шлюха... я Спермошлюха...","soft","ahegao")
    call her_head("Ваша {image=textheart}спермо{image=textheart}шлюха...","silly","ahegao")
    g9 "Отлично, шлюха!"
    g4 "СЕЙЧАС КОНЧУ!!!"
    call her_head("Залейте меня всю [genie_name]...","open_wide_tongue","ahegao")
    menu:
        "\"На грудь!\"": # Cum on shirt front
            $ cum_location = 7
            call her_head("Пожалуйста, залейте мои сиськи своей липкой спермой! Пожалуйста пожайлуста, [genie_name]!","grin","ahegao")
            ">Гермиона продолжает дрочить твой член, ее взгляд, сосредоточен на нем."
            g4 "Готовься шлюха, я кончаю!"
            call her_head("...","silly","dead")
            ">Гермиона наклоняется вперед, выставляя сиськи перед твоим членом."
            g9 "{size=+5}АХ! ДА!!! Прямо между твоими СИСЬКАМИ!{/size}"
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
            $ uni_sperm = True
            call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down")
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            m "Я закончил, это все для тебя шлюха."
            call her_main("......","soft","ahegao")
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("Она такая теплая..{image=textheart}","grin","dead")
            m "Отлично."
            call her_main("Если вы закончили я думаю, мне пора в класс...","base","down")

        "\"Подставляй свое лицо, шлюха!\"":
            $ cum_location = 8
            ">Гермиона наклоняется вниз и выставляет свое лицо перед твоим членом."
            m "Готовься шлюха, я кончаю!"
            call her_head("Пожалуйста, дайте ее мне! Мне это очень нужно, [genie_name]!","grin","ahegao")
            g9 "{size=+5}АХ! ДА!!!{/size}"
            call her_head("...","open_wide_tongue","ahegao")
            ">Ты кончаешь на ее лицо, заливая ее своей спермой."
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
            $ uni_sperm = True
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            call her_main("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
            m "Да... Я чувствую себя, куда лучше..."
            call her_main("Я тоже...","normal","worriedCl")
    show screen hermione_stand
    hide screen chair_left
    hide screen desk_02
    show screen genie
    hide screen g_c_u
    $ her_head_ypos = her_head_tits
    hide screen blkfade
    with d5
    ">Ты убираешь свой член в мантию."
    m "Я буду ждать тебя после уроков. Как и прежде, если ты вернешься чистой, я буду очень разочарован."
    call her_main("Конечно, [genie_name]...","soft","ahegao")
    call her_main("(Я не могу дождаться когда меня увидят в таком виде...)","grin","dead")

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 500 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_blink #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3

    jump end_hg_pf



label hg_ps_WearMyCum_complete: #Hermione returns from her day of wearing your cum
    $ hg_ps_WearMyCum_OBJ.inProgress = False
    $ hg_ps_WearMyCum_OBJ.complete = True
    if cum_location <= 3:
        jump hg_ps_WearMyCum_complete_1
    else:
        jump hg_ps_WearMyCum_complete_2


label hg_ps_WearMyCum_complete_1:

    call play_sound("door")
    call her_walk("door","mid",2)

    if cum_location == 1: #Cum under shirt
        $ aftersperm = True
        call her_main("...Я сделала это, [genie_name].","base","squint",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой весь день.","base","baseL")

        menu:
            "\"50 очков Гриффиндору!\"":
                $ gryffindor += 50
                call her_main("Спасибо, [genie_name], это все?","soft","base")
                m "Да, [hermione_name], теперь можешь идти. "
            "\"Расскажи, как ты провела день.\"":
                call her_main("Это был довольно нормальный день, у меня были уроки зельеварения и затем преобразования.","open","closed")
                m "Как ты думаешь, тебя кто нибудь заметил?"
                call her_main("Думаю да, [genie_name]. Джинни Уизли спросила меня об этом на занятиях преобразования.","soft","base")
                m "И что ты сказала ей?"
                call her_main("Я просто сказала, что пролила на себя зелье, на прошлом уроке.","open","base")
                m "Очень хитро. 50 очков Гриффиндору."
                $ gryffindor += 50
                call her_main("Спасибо [genie_name], если это все, я пойду, мне пора спать.","soft","base")
                m "Хорошо, спокойной ночи, [hermione_name]."
                call her_main("Спокойной ночи, [genie_name].","base","base")

    elif cum_location == 2: #Cum on skirt
        $ u_sperm = "characters/hermione/face/auto_11.png"
        $ uni_sperm = True

        call her_main("...Я сделала это [genie_name].","normal","worriedCl",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой весь день.","angry","worriedCl",emote="05")

        menu:
            "\"50 очков Гриффиндору!\"":
                $ gryffindor += 50
                call her_main("Спасибо [genie_name], это все?","annoyed","worriedL")
                m "Да [hermione_name], теперь можешь идти. "
            "\"Расскажи как ты провела день.\"":
                $ sc34CG(1, 10, 2)
                call her_main("Это был довольно нормальный день, у меня были уроки зельеварения и затем преобразования.","annoyed","worriedL",xpos="base",ypos="base")
                m "Как ты думаешь, тебя кто нибудь заметил?"
                call her_main("Я думаю несколько студентов заметили, [genie_name]. Я слышала как они шепчутся, когда я проходила мимо.","grin","worriedCl")
                m "И что ты чувствуешь?"
                call her_main("Возбуждение. Я просто хочу, чтобы они понимали, почему я это делаю.","base","down")
                m "Все ясно, 50 очков Гриффиндору."
                $ gryffindor += 50
                call her_main("Ах, точно очки, спасибо [genie_name]. Если это все, я пойду, мне пора спать.","open","down")
                m "Хорошо, спокойной ночи, [hermione_name]."
                call her_main("Спокойной ночи, [genie_name].","annoyed","closed")

    else: #Cum on hair
        $ u_sperm = "characters/hermione/face/auto_12.png"
        $ uni_sperm = True

        call her_main("...Я сделала это [genie_name].","upset","dead",tears="mascara",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой {p}весь день.","upset","worriedCl",tears="mascara_soft_blink")

        menu:
            "\"50 очков Гриффиндору!\"":
                $ gryffindor += 50
                $ mad += 5
                call her_main("...","annoyed","annoyed",tears="mascara_soft")
                m "И так [hermione_name], теперь можешь идти."
                call her_main("Мммммммм...","angry","annoyed",emote="01",tears="mascara")
            "\"Расскажи, как ты провела день.\"":
                $ mad += 10
                $ sc34CG(1, 8, 8)
                call her_main("Мой день...","normal","worriedCl",tears="mascara_soft_blink",xpos="base",ypos="base")
                call her_main("Это был самый ужасный день в моей жизни!","scream","worriedCl",tears="mascara_soft_blink")
                call her_main("Мне никогда не было так стыдно!","angry","worriedCl",emote="05",tears="mascara_soft_blink")
                m "Тебя кто-то обидел из твоих друзей?"
                call her_main("Нет! Это было ужасно!","scream","angryCl",tears="mascara_soft_blink")
                call her_main("Я думала, что буду изгоем, сидеть одна и со мной не будут разговаривать Джинни и Полумна..","annoyed","worriedL",tears="mascara_soft_blink")
                call her_main("Но они полностью игнорировали то, что я была покрыта спермой!","annoyed","angryL",tears="mascara_soft_blink")
                call her_main("Они вели себя, как будто ничего не случилось.","mad","worriedCl",tears="mascara_soft_blink")
                call her_main("Я даже пыталась спровоцировать Джинни, я спросила ее как мои волосы сегодня!","angry","base",tears="mascara_soft")
                m "И какова была ее реакция?"
                call her_main("Она сказала, что мне идет!","upset","worriedCl",tears="mascara_soft_blink")
                m "Может они уже привыкли, к твоему внешнему виду."
                call her_main("В этом и проблема! Они считают что такая распущенность, для меня норма!","angry","worried",tears="mascara_soft")
                m "А разве это не так?"
                call her_main("...","upset","worriedCl",tears="mascara_soft_blink")
                call her_main("Спокойной ночи, [genie_name].","normal","worriedCl",tears="mascara_soft_blink")

    hide screen sccg
    show screen blkfade
    with fade
    jump end_hg_pf


label hg_ps_WearMyCum_complete_2:

    call play_sound("door")
    call her_walk("door","mid",2)

    if cum_location == 4: #Cum on legs
        $ u_sperm = "characters/hermione/face/auto_13.png"
        $ uni_sperm = True

        call her_main("...Я сделала это, [genie_name].","base","squint",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой.","base","baseL")

        menu:
            "\"Хорошая работа!\"":
                call her_main("Спасибо [genie_name], это все?","soft","base")
                m "Да, [hermione_name], теперь можешь идти. "
            "\"Расскажи как ты провела день.\"":
                call her_main("Это был довольно нормальный день, ну... за исключением Полумны...","open","closed")
                m "Полумна?"
                call her_main("Полумны Лавгуд, сэр..","soft","base")
                m "Что произошло с мисс Лавгуд?"
                call her_main("Она пыталась намекнуть мне, что Корнуэльский эльф сделал мне подарок.","annoyed","angryL")
                m "А Корнуэльский эльф сделал тебе подарок?"
                call her_main("Я понимала, о чем она говорит. Корнуэльские эльфы - противные небольшие существа, которые никогда не делают ничего хорошего.","disgust","glance")
                m "Хорошо, что произошло потом?"
                call her_main("Ну, я спросила ее, о чем она говорит, а она провела пальцем по моей ноге, зачерпнув немного вашей спермы!","smile","glance")
                m "Правда?"
                call her_main("Это еще не все. Затем она его облизала!","open_tongue","glance")
                m "Я тебе не верю.."
                call her_main("Я была в таком же шоке как и вы.","open","closed")
                m "Невероятно ты сделала меня счастливым."
                call her_main("Спасибо, [genie_name]. Если это все, я пойду, мне пора спать.","open","down")
                m "Очень хорошо, спокойной ночи, [hermione_name]."
                call her_main("Спокойной ночи, [genie_name].","annoyed","closed")

    elif cum_location == 5: #Cum on shirt
        $ u_sperm = "characters/hermione/face/auto_06.png"
        $ uni_sperm = True

        call her_main("...Я сделала это, [genie_name].","normal","worriedCl",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой весь день.","angry","worriedCl",emote="05")

        menu:
            "\"Хорошая работа!\"":
                call her_main("Спасибо [genie_name], Это все?","annoyed","worriedL")
                m "Да [hermione_name], теперь можешь идти. "
            "\"Расскажи, как ты провела день.\"":
                $ sc34CG(1, 14, 7)
                call her_main("Это был довольно нормальный день, у меня был урок защиты от темных искусств, а затем Гербология.","annoyed","worriedL",xpos="base",ypos="base")
                m "Как ты думаешь, тебя кто-нибудь заметил?"
                call her_main("Я думаю большинство людей меня видели, [genie_name]. Хотя я и не уверена, что они поняли, что это сперма.","grin","worriedCl")
                m "И что ты чувствуешь?"
                call her_main("Возбуждение. Я вижу их лица в тот момент, когда они понимают, что это...","base","down")
                m "Значит ты не против, чтобы они знали?"
                call her_main("Думаю нет... Главное что это нравится вам.","open","down")
                m "Очень хорошо, спокойной ночи, [hermione_name]."
                call her_main("Спокойной ночи, [genie_name].","annoyed","closed")

    else: #Cum on face
        $ u_sperm = "characters/hermione/face/auto_07.png"
        $ uni_sperm = True

        call her_main("...Я сделала это, [genie_name].","annoyed","dead",tears="mascara",xpos="right",ypos="base")
        call her_main("Я ходила с вашей спермой {p}весь день.","annoyed","dead",tears="mascara")

        menu:
            "\"Хорошая работа!\"":
                call her_main("...","annoyed","dead",tears="mascara")
                m "Да, [hermione_name], теперь можешь идти."
                call her_main("Вы ведь довольны мной","open","annoyed",tears="mascara")
                m "Да, я доволен."
                call her_main("Хорошо.","annoyed","closed",tears="mascara")
            "\"Расскажи как ты провела день.\"":
                $ sc34CG(1, 16, 6)
                call her_main("Мой день...","normal","worriedCl",tears="mascara",xpos="base",ypos="base")
                call her_main("Все было совершенно нормально.","scream","worriedCl",tears="mascara")
                m "В самом деле? Ничего странного не произошло?"
                call her_main("Нет. Все относились ко мне так, как я этого заслуживаю.","scream","angryCl",tears="mascara")
                m "И как это?"
                call her_main("Как к шлюхе.","annoyed","worriedL",tears="mascara")
                call her_main("Парни домогались до меня.","annoyed","angryL",tears="mascara")
                call her_main("Ставили меня раком.","mad","worriedCl",tears="soft_blink",tears="mascara")
                call her_main("Профессор Снейп заставил меня выйти к доске, перед всем классом, во время урока защиты от темных искусств.","angry","base",tears="mascara_soft")
                m "Что он заставил тебя делать?"
                call her_main("Нечего я просто стояла там весь урок.","upset","worriedCl",tears="mascara_soft_blink")
                m "Твои друзья ничего не сказали?"
                call her_main("Ничего.","angry","worried",tears="mascara_soft")
                call her_main("...","upset","worriedCl",tears="mascara_soft_blink")
                call her_main("Я{p} сделала вас счастливым?","open","annoyed",tears="mascara_soft")
                m "Да."
                call her_main("Спокойной ночи, [genie_name].","normal","worriedCl",tears="mascara_soft")

    hide screen sccg
    show screen blkfade
    with fade
    jump end_hg_pf


label hg_ps_WearMyCum_complete_3:
    if cum_location == 7: #Cleavage
        $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
        $ uni_sperm = True
        ">Гермиона заходит в кабинет, ее рубашка все еще покрыта спермой."
        call her_main("... Я сделала это, [genie_name].","open","suspicious")
        call her_main("Я ходила с вашей спермой весь день...","grin","worriedCl",emote="05")
        menu:
            "\"Хорошая работа!\"":
                call her_main("Спасибо [hermione_name], это все?","base","base")
                m "Да, [hermione_name], теперь можешь идти. "
            "\"Расскажи как ты провела день.\"":
                $ sc34CG(1, 17, 7)
                call her_main("Это было довольно неприятно, [genie_name]...","annoyed","angryL")
                m "Неприятно?"
                call her_main("Да! Я провела весь день, пахнущая вашей вкусной спермой, но не имея возможности попробовать ее!","open","baseL")
                call her_main("Это как смотреть на стакан воды в пустыне...","soft","ahegao")
                m "Кто-нибудь тебя заметил?"
                call her_main("Я не могу сказать [genie_name]... Я была слишком отвлечена запахом...","angry","wink")
                m "Очень хорошо, спокойной ночи [hermione_name]."
                call her_main("Спокойной ночи [genie_name].","grin","dead")
    else: #Cum on face
        $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
        $ uni_sperm = True
        ">Гермиона возвращается в твой кабинет."
        call her_main("Я сделала это, [genie_name].","open","suspicious")
        call her_main("Я ходила с вашей спермой весь день.","base","base")
        menu:
            "\"Хорошая работа!\"":
                call her_main("Спасибо, [genie_name]. Это все?","soft","squintL")
                m "Да, [hermione_name], теперь можешь идти."
                call her_main("Умываться?","open","baseL")
                m "Только, если ты хочешь..."
                call her_main("Спасибо [genie_name]!","grin","ahegao")
            "\"Расскажи как ты провела день.\"":
                $ sc34CG(1, 17, 6)
                call her_main("Мой день...","soft","squintL")
                call her_main("Самый обычный день [genie_name]. Ну для меня он обычный.","soft","ahegao")
                call her_main("Меня снова зажимали парни, и ласкали меня.","grin","dead")
                call her_main("Сьюзан Боунс даже сказала, что ей нравится, как я выгляжу в своей рубашке.","base","down")
                m "И что ты чувствовала?"
                call her_main("Возбуждение, я почти кончила, когда Плакса Миртл начала кричать всем о сперме, на моей рубашке.","silly","dead")
                m "В самом деле?"
                call her_main("Конечно, это сделало меня еще счастливее, зная, что это обрадует вас.","base","down")
                m "Молодец..."
                call her_main("...{image=textheart}","grin","ahegao")
                call her_main("Спасибо, [genie_name]. И, спокойной ночи.","open","baseL")
                m "Спокойной ночи, [hermione_name]."
    hide screen sccg
    with fade
    jump end_hg_pf

    return
