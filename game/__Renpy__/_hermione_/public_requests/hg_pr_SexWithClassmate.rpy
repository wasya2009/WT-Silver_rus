

### Have Sex With A Classmate ###

##(Level 08) (75 pt.) (FUCK A CLASSMATE). (Available during daytime only).
label hg_pr_SexWithClassmate: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_SexWithClassmate_OBJ.points < 1:
        m "{size=-4}(Попросить ее заняться сексом с одноклассником?){/size}"
        menu:
            "\"(Да, давай!)\"":
                pass
            "\"(Нет, не сейчас.)\"":
                jump silver_requests

    call bld

    #Intro.
    if hg_pr_SexWithClassmate_OBJ.points == 0:
        m "[hermione_name]..."
        m "Сегодня я хочу, чтобы ты занялась сексом с одноклассником по своему выбору."

        if whoring < 21 or hg_pr_BlowjobClassmate_OBJ.points < 2:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("..............","angry","angry",xpos="right",ypos="base")
        call her_main("У меня было чувство, что мы доберемся до этого рано или поздно...","disgust","glance")
        call her_main("Но...","annoyed","angryL")
        her "..................."
        m "Если ты это сделаешь, \"Гриффиндор\" получит 75 очков."
        call her_main("Ну, тогда я это сделаю, [genie_name].","annoyed","annoyed")
        m "Отлично. Увидимся после занятий."
        call her_main(".............","upset","closed")

    #Secont time event.
    else:
        m "[hermione_name]..."
        m "Я хочу, чтоб ты занялась сексом со своим одноклассником."
        call her_main("Опять, [genie_name]?","angry","base",xpos="right",ypos="base")
        m "Да. И ты получишь 75 очков."
        call her_main("Ну, хорошо...","annoyed","annoyed")

    $ hg_pr_SexWithClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_SexWithClassmate_complete:

    #Event A
    if one_out_of_three == 1: ### EVENT (A)

        if fucked_ron_and_har:
            jump returns_next_morning
        else:
            $ fucked_ron_and_har = True #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        m "....."
        m ".........."
        m "Она уже должна была быть здесь..."
        m "Хм..."
        $ hg_pr_SexWithClassmate_OBJ.points += 1
        $ hg_pr_SexWithClassmate_OBJ.inProgress = False
        $ hermione_sleeping = True
        $ hg_pr_SexWithClassmate_AltFlag = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.

        return
        # NEXT MORNING

    #Event B
    elif one_out_of_three == 2: ### EVENT (B)

        call play_sound("door") #Sound of a door opening.
        call her_walk("door","mid",2)
        call bld

        m "[hermione_name], ты сделала, что я сказал?"
        show screen blktone
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Да, [genie_name].","upset","closed",xpos="right",ypos="base")
        call her_main("В школьной библиотеке...","open","annoyed",cheeks="blush")
        her "Сначала, я волновалась, потому что мы шумели..."
        her "Но мальчик продержался всего одну минуту, [genie_name]."
        m "Не вини его, [hermione_name]."
        m "Ты, довольно, привлекательна, он, вероятно, был очень взволнован..."
        call her_main("Однако...","upset","closed")
        her "Пару раз он вошел в меня и начал кончать, взволнованы?"
        her "Как? Девочка... я чувствую разочарование..."
        m "Я вижу..."
        m "Что ты сделала потом?"
        m "Одела трусики и пошла по своим делам, как ни в чем не бывало?"
        call her_main("Мои трусики?","open","down")
        call her_main("Я их больше не ношу, [genie_name].","annoyed","angryL")
        m "Ох, правда?"
        call her_main("Да... Я не ношу их, потому что в них не удобно.","annoyed","annoyed")
        m "Хорошо тебе, [hermione_name]."

    #Event C
    elif one_out_of_three == 3:
        label returns_next_morning:
            pass

        call play_sound("door") #Sound of a door opening.
        call her_walk("door","mid",2)
        call bld

        m "[hermione_name], Ты выполнила мое задание?"
        call play_music("playful_tension") # SEX THEME.
        call her_main("Да, [genie_name].","upset","closed",xpos="right",ypos="base")
        call her_main("Я отвела одного из парней \"Когтеврана\" в женский туалет...","base","down")
        her "...И дала попользоваться мною, как он хочет."
        m "Молодец, [hermione_name]."
        call her_main(".....................","annoyed","angryL")
        m "Я сказал, что ты молодец, в чем дело?"
        call her_main("Эмм... ну...","open","baseL",cheeks="blush")
        her "Вы мне хорошо платите за выполнение таких заданий..."
        her "По этому, я не имею права жаловаться..."
        m "Хм...?"
        call her_main("Моя репутация начинает падать, и это беспокоит меня, [genie_name]...","open","base",cheeks="blush")
        m "Твоя репутация?"
        call her_main("Ну, да... эм...","open","baseL",cheeks="blush")
        m ".............."
        call her_main("Нет, извините, не обращайте внимания на то, что я сказала, [genie_name].","upset","closed")
        m "Хм..."

    $ gryffindor += 75 #75
    m "\"Гриффиндор\" получает 75 очков!"
    her "Спасибо, [genie_name]."

    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False

    jump hg_pr_transition_block

    return


label hg_pr_SexWithClassmate_Alt: #Hermione does not show up. This is label where she shows up next morning.
    $ hg_pr_SexWithClassmate_AltFlag = False #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "[hermione_name], ты пропустила вчера нашу встречу."
    call her_main("Да, [genie_name], прошу прощения... *yawn*...","open","closed",xpos="right",ypos="base")
    m "Объяснишь?"
    call her_main("Конечно, [genie_name].","open","squint",cheeks="blush")
    call her_main("Это получилось неловко, хотя...","base","baseL",cheeks="blush")
    call her_main("Я провела ночь со своими друзьями...","open","squint",cheeks="blush")
    m "Девичник, да?"
    call her_main("Девичник?","angry","wink")
    call her_main("Нет, [genie_name]. Гарри и Рон - мальчики...","open","baseL",cheeks="blush")
    m "Хм..."
    call her_main("Мы лучшие друзья, уже долго...","base","baseL",cheeks="blush")
    call play_music("playful_tension") # SEX THEME.
    call her_main("Но прошлой ночью мальчики устроили со мной...","base","glance")
    call her_main("И я была совсем не против...","grin","dead")
    her "Они делали со мной все, что хотели..."
    her "И все, что я захотела, со мной, было сделано..."
    call her_main(".................","soft","ahegao")
    call her_main("Мне заплатят за это, [genie_name]?","angry","wink")

    $ gryffindor += 75 #75
    m "\"Гриффиндор\" получает 75 очков!"
    her "Спасибо, [genie_name]."

    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
