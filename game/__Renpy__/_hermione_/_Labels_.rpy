label __init_variables:
    if not hasattr(renpy.store,'hg_pf_TalkToMe_OBJ'): #important!
        $ hg_pf_TalkToMe_OBJ = personal_favor(
            imagination_level = 0,
            menu_text = "Поговори со мной",
            start_label = "hg_pf_TalkToMe",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_NicePanties_OBJ'): #important!
        $ hg_pf_NicePanties_OBJ = personal_favor(
            imagination_level = 0,
            menu_text = "Красивые трусики",
            start_label = "hg_pf_NicePanties"
        )

    if not hasattr(renpy.store,'hg_pf_BreastMolester_OBJ'): #important!
        $ hg_pf_BreastMolester_OBJ = personal_favor(
            imagination_level = 2,
            menu_text = "Пощупать грудь",
            start_label = "hg_pf_BreastMolester",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_ButtMolester_OBJ'): #important!
        $ hg_pf_ButtMolester_OBJ = personal_favor(
            imagination_level = 2,
            menu_text = "Пощупать попку",
            start_label = "hg_pf_ButtMolester",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_ShowThemToMe_OBJ'): #important!
        $ hg_pf_ShowThemToMe_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Покажи их мне!",
            start_label = "hg_pf_ShowThemToMe",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_DanceForMe_OBJ'): #important!
        $ hg_pf_DanceForMe_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Потанцуй для меня!",
            start_label = "hg_pf_DanceForMe",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_ShowMeYourAss_OBJ'): #important!
        $ hg_pf_ShowMeYourAss_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Покажи мне свою попку!",
            start_label = "hg_pf_ShowMeYourAss",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_LetMeTouchThem_OBJ'): #important!
        $ hg_pf_LetMeTouchThem_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Помацать сиськи!",
            start_label = "hg_pf_LetMeTouchThem",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_TouchYourself_OBJ'): #important!
        $ hg_pf_TouchYourself_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Потрогай себя!",
            start_label = "hg_pf_TouchYourself",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_TouchMe_OBJ'): #important!
        $ hg_pf_TouchMe_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Потрогай меня!",
            start_label = "hg_pf_TouchMe",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_TitJob_OBJ'): #important!
        $ hg_pf_TitJob_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Трахнуть твою грудь!",
            start_label = "hg_pf_TitJob",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_SuckIt_OBJ'): #important!
        $ hg_pf_SuckIt_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Соси!",
            start_label = "hg_pf_SuckIt",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_LetsHaveSex_OBJ'): #important!
        $ hg_pf_LetsHaveSex_OBJ = personal_favor(
            imagination_level = 5,
            menu_text = "Давай займемся сексом!",
            start_label = "hg_pf_LetsHaveSex",
            costume_event = True
        )

    if not hasattr(renpy.store,'hg_pf_TimeForAnal_OBJ'): #important!
        $ hg_pf_TimeForAnal_OBJ = personal_favor(
            imagination_level = 5,
            menu_text = "Время для анала!",
            start_label = "hg_pf_TimeForAnal",
            costume_event = True
        )


    $ hg_pf_list = []
    $ hg_pf_list.append(hg_pf_TalkToMe_OBJ)
    $ hg_pf_list.append(hg_pf_NicePanties_OBJ)
    $ hg_pf_list.append(hg_pf_BreastMolester_OBJ)
    $ hg_pf_list.append(hg_pf_ButtMolester_OBJ)
    $ hg_pf_list.append(hg_pf_ShowThemToMe_OBJ)
    $ hg_pf_list.append(hg_pf_DanceForMe_OBJ)
    $ hg_pf_list.append(hg_pf_ShowMeYourAss_OBJ)
    $ hg_pf_list.append(hg_pf_LetMeTouchThem_OBJ)
    $ hg_pf_list.append(hg_pf_TouchMe_OBJ)
    $ hg_pf_list.append(hg_pf_TitJob_OBJ)
    $ hg_pf_list.append(hg_pf_TouchYourself_OBJ)
    $ hg_pf_list.append(hg_pf_SuckIt_OBJ)
    $ hg_pf_list.append(hg_pf_LetsHaveSex_OBJ)
    $ hg_pf_list.append(hg_pf_TimeForAnal_OBJ)



    if not hasattr(renpy.store,'hg_pr_FlirtClassmate_OBJ'): #important!
        $ hg_pr_FlirtClassmate_OBJ = public_request()
    $ hg_pr_FlirtClassmate_OBJ.imagination_level = 0
    $ hg_pr_FlirtClassmate_OBJ.menu_text = "Пофлиртуй с одноклассником"
    $ hg_pr_FlirtClassmate_OBJ.start_label = "hg_pr_FlirtClassmate"
    $ hg_pr_FlirtClassmate_OBJ.complete_label = "hg_pr_FlirtClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_FlirtTeacher_OBJ'): #important!
        $ hg_pr_FlirtTeacher_OBJ = public_request()
    $ hg_pr_FlirtTeacher_OBJ.imagination_level = 2
    $ hg_pr_FlirtTeacher_OBJ.menu_text = "Пофлиртуй с учителем"
    $ hg_pr_FlirtTeacher_OBJ.start_label = "hg_pr_FlirtTeacher"
    $ hg_pr_FlirtTeacher_OBJ.complete_label = "hg_pr_FlirtTeacher_complete"

    if not hasattr(renpy.store,'hg_pr_ClassmateTouchYou_OBJ'): #important!
        $ hg_pr_ClassmateTouchYou_OBJ = public_request()
    $ hg_pr_ClassmateTouchYou_OBJ.imagination_level = 3
    $ hg_pr_ClassmateTouchYou_OBJ.menu_text = "Пусть одноклассник пристает к тебе"
    $ hg_pr_ClassmateTouchYou_OBJ.start_label = "hg_pr_ClassmateTouchYou"
    $ hg_pr_ClassmateTouchYou_OBJ.complete_label = "hg_pr_ClassmateTouchYou_complete"

    if not hasattr(renpy.store,'hg_pr_FlashClassmate_OBJ'): #important!
        $ hg_pr_FlashClassmate_OBJ = public_request()
    $ hg_pr_FlashClassmate_OBJ.imagination_level = 3
    $ hg_pr_FlashClassmate_OBJ.menu_text = "Покажи свои сиськи однокласснику"
    $ hg_pr_FlashClassmate_OBJ.start_label = "hg_pr_FlashClassmate"
    $ hg_pr_FlashClassmate_OBJ.complete_label = "hg_pr_FlashClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_KissAGirl_OBJ'): #important!
        $ hg_pr_KissAGirl_OBJ = public_request()
    $ hg_pr_KissAGirl_OBJ.imagination_level = 4
    $ hg_pr_KissAGirl_OBJ.menu_text = "Поцелуй девушку"
    $ hg_pr_KissAGirl_OBJ.start_label = "hg_pr_KissAGirl"
    $ hg_pr_KissAGirl_OBJ.complete_label = "hg_pr_KissAGirl_complete"

    if not hasattr(renpy.store,'hg_pr_HandjobClassmate_OBJ'): #important!
        $ hg_pr_HandjobClassmate_OBJ = public_request()
    $ hg_pr_HandjobClassmate_OBJ.imagination_level = 4
    $ hg_pr_HandjobClassmate_OBJ.menu_text = "Подрочи однокласснику"
    $ hg_pr_HandjobClassmate_OBJ.start_label = "hg_pr_HandjobClassmate"
    $ hg_pr_HandjobClassmate_OBJ.complete_label = "hg_pr_HandjobClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_BlowjobClassmate_OBJ'): #important!
        $ hg_pr_BlowjobClassmate_OBJ = public_request()
    $ hg_pr_BlowjobClassmate_OBJ.imagination_level = 5
    $ hg_pr_BlowjobClassmate_OBJ.menu_text = "Отсоси однокласснику"
    $ hg_pr_BlowjobClassmate_OBJ.start_label = "hg_pr_BlowjobClassmate"
    $ hg_pr_BlowjobClassmate_OBJ.complete_label = "hg_pr_BlowjobClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_SexWithClassmate_OBJ'): #important!
        $ hg_pr_SexWithClassmate_OBJ = public_request()
    $ hg_pr_SexWithClassmate_OBJ.imagination_level = 5
    $ hg_pr_SexWithClassmate_OBJ.menu_text = "Займись сексом с одноклассником"
    $ hg_pr_SexWithClassmate_OBJ.start_label = "hg_pr_SexWithClassmate"
    $ hg_pr_SexWithClassmate_OBJ.complete_label = "hg_pr_SexWithClassmate_complete"


    $ hg_pr_list = []
    $ hg_pr_list.append(hg_pr_FlirtClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_FlirtTeacher_OBJ)
    $ hg_pr_list.append(hg_pr_ClassmateTouchYou_OBJ)
    $ hg_pr_list.append(hg_pr_FlashClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_KissAGirl_OBJ)
    $ hg_pr_list.append(hg_pr_HandjobClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_BlowjobClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_SexWithClassmate_OBJ)



    if not hasattr(renpy.store,'hg_ps_PantyThief_OBJ'): #important!
        $ hg_ps_PantyThief_OBJ = public_shaming()
    $ hg_ps_PantyThief_OBJ.menu_text = "Без трусиков"
    $ hg_ps_PantyThief_OBJ.start_label = "hg_ps_PantyThief"
    $ hg_ps_PantyThief_OBJ.complete_label = "hg_ps_PantyThief_complete"

    if not hasattr(renpy.store,'hg_ps_WalkOfShame_OBJ'): #important!
        $ hg_ps_WalkOfShame_OBJ = public_shaming()
    $ hg_ps_WalkOfShame_OBJ.menu_text = "Прогулка позора"
    $ hg_ps_WalkOfShame_OBJ.start_label = "hg_ps_WalkOfShame"
    $ hg_ps_WalkOfShame_OBJ.complete_label = "hg_ps_WalkOfShame_complete"

    if not hasattr(renpy.store,'hg_ps_WearMyCum_OBJ'): #important!
        $ hg_ps_WearMyCum_OBJ = public_shaming()
    $ hg_ps_WearMyCum_OBJ.menu_text = "Носи мою сперму"
    $ hg_ps_WearMyCum_OBJ.start_label = "hg_ps_WearMyCum"
    $ hg_ps_WearMyCum_OBJ.complete_label = "hg_ps_WearMyCum_complete"

    if not hasattr(renpy.store,'hg_ps_HiddenBlowjob_OBJ'): #important!
        $ hg_ps_HiddenBlowjob_OBJ = public_shaming()
    $ hg_ps_HiddenBlowjob_OBJ.menu_text = "Скрытый минет"
    $ hg_ps_HiddenBlowjob_OBJ.start_label = "hg_ps_HiddenBlowjob"
    $ hg_ps_HiddenBlowjob_OBJ.complete_label = "hg_ps_HiddenBlowjob_complete"

    if not hasattr(renpy.store,'hg_ps_LeashWalk_OBJ'): #important!
        $ hg_ps_LeashWalk_OBJ = public_shaming()
    $ hg_ps_LeashWalk_OBJ.menu_text = "Время для прогулки (поводок)"
    $ hg_ps_LeashWalk_OBJ.start_label = "hg_ps_LeashWalk"
    $ hg_ps_LeashWalk_OBJ.complete_label = "hg_ps_LeashWalk_complete"

    if not hasattr(renpy.store,'hg_ps_Buttplug_OBJ'): #important!
        $ hg_ps_Buttplug_OBJ = public_shaming()
    $ hg_ps_Buttplug_OBJ.menu_text = "Походи с анальной пробкой"
    $ hg_ps_Buttplug_OBJ.start_label = "hg_ps_Buttplug"
    $ hg_ps_Buttplug_OBJ.complete_label = "hg_ps_Buttplug_complete"


    $ hg_ps_list = []
    $ hg_ps_list.append(hg_ps_PantyThief_OBJ)
    #$ hg_ps_list.append(hg_ps_WalkOfShame_OBJ)
    $ hg_ps_list.append(hg_ps_Buttplug_OBJ)
    $ hg_ps_list.append(hg_ps_WearMyCum_OBJ)
    #$ hg_ps_list.append(hg_ps_HiddenBlowjob_OBJ)
    #$ hg_ps_list.append(hg_ps_LeashWalk_OBJ)

    return


label silver_requests:
    if slytherin > gryffindor or slytherin == gryffindor:
        show screen hermione_main

        label silver_requests_root:
        menu:
            "-Личные услуги-":
                label not_now_pf:
                python:
                    pf_menu = []
                    for i in hg_pf_list:
                        if i.imagination_level > imagination:
                            pf_menu.append(("{color=#858585}-Смутное представление-{/color}","vague"))
                        else:
                            pf_menu.append((i.getMenuText(),i.start_label))
                    pf_menu.append(("-Неважно-", "nvm"))
                    result = renpy.display_menu(pf_menu)
                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call vague_idea
                    jump not_now_pf
                else:
                    $ renpy.jump(result)

            "{color=#858585}-Публичные услуги-{/color}" if not daytime:
                show screen blktone
                with d3
                ">Публичные услуги доступны только в дневное время."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Публичные услуги-" if daytime:
                if lock_public_favors:
                    her "Ээ... [genie_name]..."
                    her "Я не против продолжать оказывать Вам услуги..."
                    her "Но только до тех пор, пока мы держим их в секрете..."
                    jump silver_requests_root
                else:
                    label not_now_pr:
                    python:
                        pr_menu = []
                        for i in hg_pr_list:
                            if i.imagination_level > imagination:
                                pr_menu.append(("{color=#858585}-Смутное представление-{/color}","vague"))
                            else:
                                pr_menu.append((i.getMenuText(),i.start_label))
                        pr_menu.append(("-Неважно-", "nvm"))
                        result = renpy.display_menu(pr_menu)
                    if result == "nvm":
                        jump silver_requests_root
                    elif result == "vague":
                        call vague_idea
                        jump not_now_pr
                    else:
                        $ renpy.jump(result)

            "{color=#858585}-Публичный Позор-{/color}" if not daytime:
                show screen blktone
                with d3
                ">События Публичного Позора, доступны только в дневное время."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Публичный Позор-"if daytime:
                label not_now_ps:
                python:
                    ps_menu = []
                    for i in hg_ps_list:
                        ps_menu.append((i.getMenuText(),i.start_label))
                    ps_menu.append(("-Неважно-", "nvm"))
                    result = renpy.display_menu(ps_menu)
                if result == "nvm":
                    jump silver_requests_root
                else:
                    $ renpy.jump(result)

            "-Отмена-":
                jump day_time_requests

    else:
        show screen hermione_main
        with d3
        her "Гриффиндор лидирует. Мне не нужно этого делать."
        jump day_time_requests


label end_hg_pf: #Hides screens. Hermione walks out. Resets Hermione.
    hide screen hermione_main
    show screen blkfade
    with d3

    hide screen chair_left
    hide screen desk
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen bld1
    hide screen blktone

    if hermione_xpos_name == "desk":
        call her_chibi("stand","desk","base")
    else:
        call her_chibi("stand","mid","base")

    call gen_chibi("hide")
    show screen genie
    call hide_blkfade

    if hermione_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    else:
        call her_walk("mid","leave",2)

    call reset_hermione_main

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


label hg_pr_transition_block:

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3

    if hermione_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    elif hermione_xpos_name == "mid":
        call her_walk("mid","leave",2)
    else:
        call her_chibi("leave")

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

label could_not_flirt: #Sent here when choose "Favour failed! No points for you!" (Hermione is leaving without getting any points).

    show screen blkfade #Should be active anyways.

    hide screen hermione_main
    hide screen hermione_main_ass

    hide screen chair_left
    hide screen desk
    hide screen hermione_04 #Stands with tits out.
    hide screen groping_naked_tits
    hide screen genie_and_tits_01
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    if hermione_xpos_name == "desk":
        call her_chibi("stand","desk","base")
    else:
        call her_chibi("stand","mid","base")
    show screen genie

    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with fade

    if hermione_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    else:
        call her_walk("mid","leave",2)

    if daytime:
        call play_music("day_theme")
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme")
        $ hermione_sleeping = True
        jump night_main_menu



### MUSIC BLOCK ###
label music_block:
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    return

### YOU LUCK IMAGINATION ###
label vague_idea:

    call nar(">Тебе не хватает воображения для идеи такого калибра.")

    return

### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
    call her_head("Нет! Что вы наделали?!!","angry","worriedCl",cheeks="blush",tears="soft_blink")
    ">Гермиона неожиданно сильно толкается..."
    with hpunch
    call her_head("Зачем вы делаете это со мной, [genie_name]...?","angry","worriedCl",cheeks="blush",tears="soft_blink")
    call her_head("Я никогда не соглашалась, чтобы... чтобы...","angry","worriedCl",cheeks="blush",tears="crying_blink")
    call her_head("Вы... вы...","angry","worriedCl",cheeks="blush",tears="crying_blink")
    with hpunch
    call her_head("{size=+7}ВЫ ИЗНАСИЛОВАЛИ МЕНЯ!{/size}","scream","worriedCl",cheeks="blush",tears="messy")
    g4 "Что? Не смеши, [hermione_name]! Я не делал ничего подобного!"
    call her_head("Да вы это сделали! Да вы это сделали!","scream","worriedCl",cheeks="blush",tears="messy")
    g4 "Я этого не делал!"
    call her_head("Нет, вы, [genie_name]!","scream","worriedCl",cheeks="blush",tears="messy")
    call her_head("Теперь, вы дадите мне 20--","angry","angry",cheeks="blush",tears="down")
    call her_head("Нет, 100 очков факультету или я пожалуюсь в Министерство Магии!","angry","angry",cheeks="blush",tears="down")
    menu:
        m "(Ах, дерьмо...)"
        "\"Ладно, ладно... 100 очков твои...\"":
            $ gryffindor +=100
            m "Сто очков \"Гриффиндору\" !"
            m "Вот, это уже сделано..."
            m "А теперь успокойся, [hermione_name]?"
            call her_head("Нет, не буду!","scream","worriedCl",cheeks="blush",tears="messy")
            call her_head("Меня только что изнасиловали!","scream","worriedCl",cheeks="blush",tears="messy")
            g4 "Да, брось [hermione_name], Я тебя не насиловал! Все, что я сделал, это--"
            with hpunch
            call her_head("{size=+7}Вы изнасиловали меня!!!{/size}","scream","worriedCl",cheeks="blush",tears="messy")
            g4 "О, Великие Пески Пустыни, ты бы потише об изнасилованиях?!"
            g4  "Кто-нибудь тебя может услышать!"
            call her_head("Хорошо! Я хочу, чтобы все услышали!","scream","worriedCl",cheeks="blush",tears="messy")
            m "Зачем тебе это? Я же уже, тебе заплатил!"
            call her_head("О... правда...","angry","base",cheeks="blush",tears="mascara")
            call her_head("Но я ненавижу вас! Я ненавижу вас [genie_name]!","scream","angryCl",cheeks="blush",tears="mascara")
            $ mad +=30

        "\"Ты, не докажешь, [hermione_name]!\"":
            call her_head("Нет, это не так! Я собираюсь это сделать!","scream","worriedCl",cheeks="blush",tears="messy")
            g4 "Во что бы то ни стало, вперед..."
            g4 "Не было никакого изнасилования!"
            call her_head("Я ненавижу вас, [genie_name]!","scream","worriedCl",cheeks="blush",tears="messy")
            $ mad +=50


    hide screen bld1
    hide screen ctc
    hide screen hermione_main
    show screen genie
    hide screen groping_01
    hide screen groping_02
    hide screen blkfade
    hide screen blktone8
    with d3

    call her_walk("mid","door",2)

    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        call her_head("...........................","disgust","down_raised",cheeks="blush")


    call her_chibi("leave","door","base")

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

### SCREAM OF PLEASURES ###
label screams_of_pleasure:
    call her_head("Ах....","silly","glance",cheeks="blush")
    call her_head("Это внутри меня...")
    call her_head("Нет, [genie_name], Вы должны остановиться...","base","glance",cheeks="blush")
    m "Почему? Тебе не нравится?"
    call her_head("Неважно, нравится мне это или нет, [genie_name].")
    call her_head("Вы знаете, почему я это делаю...")
    call her_head("И это неправильно, позволить вам сделать это со мной, за жалкие 15 очков...")
    ">Гермиона отстраняется от тебя..."
    m "Хех... Я вижу..."
    m "Хорошо, в таком случае....."
    jump ending_of_screams_of_pleasure


label Day_Request_Block:

    if hg_pr_SexWithClassmate_AltFlag:#Hermione does not show up. This sends to label where she shows up next morning.
        call hg_pr_SexWithClassmate_Alt

    return

label Night_Request_Block:
    ###JOBS###
    if current_job == 1:
        jump maid_responses

    if current_job == 2:
        jump barmaid_responses

    if current_job == 3:
        jump gryffindor_cheer_responses

    if current_job == 4:
        jump slytherin_cheer_responses

    if cat_ears_potion_return:
        jump potion_scene_1_1_2

    if transparency < 1 and transparent_quest:
        jump potion_scene_4_2

    if addicted == True:
        jump potion_scene_3_1_2


    if hg_pf_TheGamble_Flag and hg_pf_TheGamble_FlagC or hg_pf_TheGamble_FlagA:
        jump hg_pf_TheGamble_complete

    python:
        for i in hg_pr_list: #Call any public request event if it's in progress
            if i.inProgress:
                renpy.jump(i.complete_label)
        for i in hg_ps_list: #Call any public shaming event if it's in progress
            if i.inProgress:
                renpy.jump(i.complete_label)

    #Astoria Intro
    if day >= 25 and whoring >= 9:
        jump astoria_intro_branches

    jump night_resume

label her_walk_desk_blkfade:

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("mid","desk",2,loiter=False, redux_pause = 2)
    call blkfade

    return

#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!","shock","wide",xpos="mid",trans="fade")
    her "Как вы можете просить о таком?!"
    call her_main("Я думаю, мне лучше уйти.","angry","worriedCl",emote="05")

    $ mad += 7

    jump end_hg_pf

label very_no:
    stop music fadeout 2.0
    call her_main("Категорически нет!","annoyed","angryL",xpos="mid",trans="fade")
    her "Я покажу вам, что мою честь и честь Гриффиндора нельзя купить!"
    call her_main("Я ухожу немедленно.","scream","angryCl")

    $ mad += 7

    jump end_hg_pf


init python:
    class silver_request(object):
        menu_text = ""
        start_label = ""
        complete_label = ""
        points = 0


    class personal_favor(silver_request):
        hearts_level = 0
        imagination_level = 0
        costume_event = False
        progress_hint = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/heart_0"+str(self.hearts_level)+".png"
            ret_str = "Услуга: \""+self.menu_text+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            if self.costume_event:
               ret_str += "  {image=interface/clothes.png}"
            return ret_str

    class public_request(silver_request):
        imagination_level = 0
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            return "Услуга: \""+self.menu_text+"\" {image="+menu_image+"}"

    class public_shaming(silver_request):
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            return "Событие: "+self.menu_text+" {image="+menu_image+"}"
