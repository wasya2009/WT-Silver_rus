

### Panty Thief ###

################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label hg_ps_PantyThief: #(Whoring = 3 - 5)
    hide screen hermione_main
    with d3
    m "{size=-4}(Попросить ее снять трусики и отдать их мне?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump silver_requests
    m "[hermione_name]?"
    call her_main("Я слушаю, [genie_name].",xpos="right",ypos="base")
    m "Мне нужны твои трусики..."

    if whoring <=2:
        jump too_much

    if hg_ps_PantyThief_OBJ.points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_heart = 1 #Event hearts level (0-3)
        $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)

        call her_main("Ч-что?","open","worried")
        her "Мои... трусики...?"
        her "[genie_name], это..."
        m "Это услуга, которую я хочу купить у тебя сегодня, [hermione_name]..."
        m "Если тебя это не интересует, то можешь больше не приходить."
        her "Нет, мне интересно. Я... это..."
        her "Вам нужны трусики...."
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("...трусики, [genie_name]?","angry","angry")
        m "Да..."
        call her_main("Можно спросить, что вы собираетесь с ними делать...?","disgust","glance")
        m "Эм... Я веду исследование..."
        her "Но это вроде неуместно, не так ли?"
        m "Но разве тебе не противно, что некоторые девушки из \"Слизерин\"..."
        m "Продают услуги за очки, [hermione_name]?"
        call her_main("Я дам их вам!","angry","angry")
        call her_main("(Те \"Слизеринские\" блудницы не имеют достоинства.)","annoyed","angryL")
        m "Что ж, тогда давай!"
        call her_main("А?","disgust","glance")
        m "Победи в их игре!"
        call her_main("Что?","open","base")
        m "Да! Не просто вернуть \"Гриффиндор\" в лидеры..."
        m "Но сделай это, победив в их собственной игре!"
        call her_main("[genie_name]...","open","worried")
        m "Будучи директором, я не могу выбирать любимчиков. Но ты знаешь, как я поддерживаю \"Гриффиндор\"..."
        m "Хотел бы я просто дать тебе очки, но это испортило бы систему..."
        hide screen hermione_main
        with d3
        call nar(">Внезапно Гермиона протягивает тебе руку...","start")
        call nar(">Ты видишь, что она сжимает трусики в кулаке...","end")
        #">Her panties? You can't help but wonder when she managed to take them off..."
        m "??!"
        call nar(">Ты взял трусики Гермионы...")
        call her_main("Возьмите их, [genie_name]...","mad","worried",tears="soft")
        m "Что? Когда ты?"
        her "Ваша речь была такой трогательной...."
        her "Вы так правы, [genie_name]! Я выиграю в их собственной игре!"
        her "Мои занятия вот-вот начнутся, так что я должна идти..."
        call her_main("...........","normal","baseL",tears="soft")
        call her_main("...Надеюсь, никто не заметит, что на мне сегодня нет нижнего белья...","annoyed","worriedL")
        call her_main("Oх, и я вернусь сегодня вечером, чтобы забрать их, [genie_name].","open","base")
        m "Конечно. Твои трусики будут прямо здесь, на моем столе, ждать тебя..."
        call her_main(".............","angry","worriedCl",emote="05")
        jump hg_ps_PantyThief_ends

    else: #<========================================================================================== FIRST EVENT!
        if hg_ps_PantyThief_OBJ.points >= 1:
            her "Опять, [genie_name]?"
            m "Да, опять..."
        her "Вот..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            call nar(">Гермиона вытаскивает трусики из кармана...")
            m "Что?"
            call her_main("Да, у меня было предчувствие, что вы можете попросить их сегодня, [genie_name].","base","base")
            m "Предчувствие?"
            call her_main("Ну, если быть абсолютно честной, я просто не хочу больше их носить...","grin","baseL")
        else:
            hide screen hermione_main
            with d3
            call nar(">Гермиона снимает трусики и передает их тебе...")
        call nar(">Ты взял трусики Гермионы.")
        call her_main("Занятия вот-вот начнутся, так что мне лучше идти...","soft","base")

    label hg_ps_PantyThief_ends:

    $ hg_ps_PantyThief_OBJ.inProgress = True #True when Hermione has no panties on.

    hide screen blktone

    call her_walk("mid","leave",2)

    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu

label hg_ps_PantyThief_soaked:### PANTIES SOAKED IN CUM ###
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        call her_main("Хм....?","annoyed","down",xpos="right",ypos="base")
        call her_main("[genie_name]? Что такое?","angry","angry")
        her "Что вы с ними сделали?"
        call her_main("Они покрыты чем-то склизким...","normal","frown")

        menu:
            "\"Эксперимент пошел не так\"":
                call her_main("Эксперимент пошел не так, [genie_name]?","open","base")
                m "Да... Или, может, мне лучше сказать..."
                g9 "\"Эксперимент прошел очень правильно\"? Хе-хе..."
                call her_main(".....................?","normal","frown")
                her "Какой эксперимент?"
                m "Какой? Oх..."
                m "Некоторые сверхсекретные исследования."
                m "Я не могу обсуждать это с учениками."
                call her_main("................................","angry","angry")
            "\"Ты подарила их мне!\"":
                her "Я точно не дарила, [genie_name]!"
                her ".........................."

        call her_main("Что ж, они потребуют серьезной очистки, прежде чем я смогу надеть их снова...","annoyed","down")
        m "Или ты можешь надеть их сейчас."
        call her_main("Что?","open","base")
        call her_main("Я бы не стала, [genie_name]...","soft","baseL")

        menu:
            "\"Надень их или не получишь очков!\"":
                $ mad +=7
                call her_main("Что?","scream","wide_stare")
                her "[genie_name], вы шутите, да?"
                m "Нет..."
                call her_main("Н-но...","open","base")
                call her_main("........................................","normal","worriedCl")
                call her_main("(Вы всегда делаете по-своему, [genie_name]?)","angry","angry")
                m "Что, [hermione_name]?"
                call her_main("Ничего, [genie_name].","scream","angryCl")
                her "Я надену свои трусики!"
                hide screen hermione_main
                call nar(">Гермиона нерешительно надевает трусики...","start")
                ">Малюсенький поток спермы свисает по одной из ее ног..."
                call nar(">Гермиона выглядит очень неуклюже...","end")
                call her_main("......................","angry","worriedCl",emote="05")
            "\"Ну, как хочешь....\"":
                pass

    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        call her_main("Мои трусики...","annoyed","down",xpos="right",ypos="base")
        call her_main("Что с ними случилось [genie_name]?","annoyed","down")

        menu:
            "\"Эксперимент пошел не так.\"":
                her "Хм..."
                her "Понятно..."
            "\"Ты подарила их мне!\"":
                her "Я? Oх, ну..."

        hide screen hermione_main
        call nar(">Гермиона недоуменно смотрит на свои, пропитанные спермой, трусики...")
        call her_main("Похоже, они потребуют серьезной очистки, прежде чем я смогу снова их надеть...","annoyed","down")
        m "Почему бы не надеть их сейчас?"
        call her_main("Хм....?","annoyed","suspicious")
        call her_main("Ну, я полагаю, я могла бы надеть их еще раз, прежде чем положить их в прачечную...","annoyed","down")
        hide screen hermione_main
        call nar(">Гермиона надевает трусики...")
        call her_main("(Забавное ощущение...)","angry","worriedCl",emote="05")
        call her_main("Это все, [genie_name]?","upset","wink")

    if whoring >= 9 and whoring <= 15: #LEVEL 04+ (THIRD EVENT)
        call her_main("Мои трусики...","annoyed","down",xpos="right",ypos="base")
        if hg_ps_PantyThief_SoakedPantiesFlag:
            her "Они снова покрыты чем-то склизким..."
        else:
            her "Они покрыты чем-то склизким..."
        her "И они странно пахнут..."
        call her_main("Хм... Этот запах...","annoyed","worriedL")
        her "Это как-то знакомо..."
        call her_main("Что именно вы с ними сделали, [genie_name]?","base","base")

        menu:
            "\"Эксперимент пошел не так\"":
                her "Эксперимент, да?"
                her "Действительно?"
                call her_main("Нет, не отвечайте... Думаю, я знаю...","smile","baseL")
            "\"Ты подарила их мне!\"":
                her "Я так не думаю, [genie_name]."
                her "Но ничего страшного, если вы не хотите мне говорить, [genie_name]..."
                her "Думаю, я точно знаю, что с ними случилось..."
            "\"Я кончил в них!\"":
                call her_main("Я так и знала...","smile","glance")
                her "От них разит спермой!"

        call her_main("Хм...","grin","baseL")
        her "Похоже, они потребуют серьезной очистки, прежде чем я смогу их надеть..."
        call her_main("Если только вы не хотите, чтобы я надела их сейчас, [genie_name]...?","smile","glance")

        menu:
            "\"Да! Надень их, [hermione_name]!\"":
                her "Ну, если вы настаиваете..."
            "\"Меня не волнует. Делай, что хочешь.\"":
                her "Почему бы не надеть их сейчас?"

        call her_main("Я делаю это только для того, чтобы дать шанс моему факультету выиграть Кубок в этом году...","base","happyCl")
        m "Верно..."
        hide screen hermione_main
        call nar(">Гермиона быстро надевает трусики, пропитанные спермой...")

    elif whoring > 15: ###New variant of the event
        call her_main("Мои трусики...","base","ahegao_raised",xpos="right",ypos="base")
        if hg_ps_PantyThief_OBJ.points >= 1:
            her "Вы опять кончили в мои трусики..."
        else:
            her "Вы опять кончили в мои трусики..."
        call her_main("Хм...","grin","baseL")
        her "Похоже, они потребуют серьезной очистки, прежде чем я смогу их надеть..."
        call her_main("Если только вы не хотите, чтобы я надела их сейчас, [genie_name]...?","smile","glance")

        menu:
            "\"Да! Надень их, [hermione_name]!\"":
                her "Да [genie_name]..."
                call her_main("Я делаю это только для того, чтобы дать шанс моему факультету выиграть Кубок в этом году.","smile","happyCl")
                call her_main("Мне совсем не нравится это ощущение...","base","ahegao_raised")
                m "Конечно..."
                hide screen hermione_main
                call nar(">Гермиона быстро надевает трусики, пропитанные спермой...")
                call her_main("...","soft","ahegao")
            "\"Почему бы тебе не почистить их сейчас?\"":
                $ cleaned_panties = True
                call her_main("Как почистить? У вас здесь нет раковины...","open","base")
                m "Ты права, тогда тебе придется использовать свой рот."
                call her_main("Мой рот?!","scream","wide_stare")
                m "В чем дело? Это не первый раз, когда ты попробуешь мою сперму."
                call her_main("Это немного по-другому! Я надевала эти трусики перед тем, как отдать их вам.","scream","angryCl")
                call her_main("Не говоря уже о том, что ваша сперма вся холодная и скользкая...","scream","worriedCl")
                m "Ну в таком случае верни их обратно."
                call her_main("Что? Разве я не могу просто надеть их?","angry","wink")
                m "Я боюсь, что нет, ты почистишь их сейчас или отдашь их обратно."
                call her_main("{size=-4}Ладно...{/size}","angry","down_raised")
                m "Что?"
                call her_main("Я сказала, что почищу их, хорошо?!","shock","worriedCl")
                m "Что ж..."
                call her_main("...","angry","down_raised")
                call nar(">Гермиона неохотно ложит свои, пропитанные спермой, трусики в рот.")
                call her_main("Мммммххх!","full","ahegao_intense")
                m "Вот и все, не так сложно, как ты думала, не так ли?"
                call her_main("...","full","narrow")
                m "Убедись, что они будут красивые и чистые..."
                call her_main("*gulp*","full_cum","down",cheeks="blush")
                m "Вот и все. Мне кажется, что они уже чистые."
                call her_main("*Ммммхххммм*","full_cum","dead")
                m "Что ж, ты можешь вытащить их из своего рта."
                call her_main("*Ахххх*","open_wide_tongue","ahegao")
                m "Они теперь чистые?"
                call her_main("*Да [genie_name]*","soft","ahegao")

    jump back_from_soaked

label hg_ps_PantyThief_complete: # WHORING LEVEL 02 <=================
    $ hg_ps_PantyThief_OBJ.complete = True

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.5

    call her_main("Добрый вечер, [genie_name]...","base","base",xpos="right",ypos="base")
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    menu:
        "\"Вот твои трусики.\"":
            if hg_ps_PantyThief_SoakedPantiesFlag:
                jump hg_ps_PantyThief_soaked
            else:
                her "Спасибо, [genie_name]."
                her "А мои очки?"
                m "Конечно."

        "\"Как прошел твой день, [hermione_name]?\"":
            if  whoring <= 5: #WHORING LVL 02. EVENT LEVEL: 01
                $ new_request_03_heart = 1 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)
                $ sc34CG(1, 10)
                call her_main("Oх...","soft","base",xpos="base",ypos="base")
                her "Вполне обычно на самом деле..."
                call her_main("Хотя... Я не могла не волноваться, что кто-то заметит...","soft","baseL")
                call her_main(".....","annoyed","worriedL")
                hide screen sccg
                call her_main("Могу я получить свои трусики?","open","base",xpos="right",ypos="base",trans="fade")
                m "Конечно..."
                hide screen hermione_main
                with d3
                call nar(">Ты отдаешь трусики Гермионе...")
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("А мои очки?","open","base")
                    m "Да, да..."

            elif whoring >= 6 and whoring <= 8: #WHORING LVL 03. EVENT LEVEL 02.
                $ new_request_03_heart = 2 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 2 #Event hearts level (0-3)
                $ sc34CG(1, 5)
                call her_main("Oх...","soft","base",xpos="base",ypos="base")
                her "На самом деле, это был вполне обычный день..."
                her "Я провела некоторое время со своими одноклассниками..."
                her "И после этого у нас была короткая встреча \"ДПМ\"..."
                call her_main("Я произнесла короткую речь о том, \"Почему нельзя продавать сексуальные услуги в обмен на очки факультета\"...","open","closed")
                call her_main("Я мне было неловко, потому что пришлось произнести речь без нижнего белья...","annoyed","angryL")
                hide screen sccg
                call her_main(xpos="right",ypos="base",trans="fade")

                menu:
                    "\"Ты лицемерка!\"":
                        $ mad +=5
                        call her_main("[genie_name]?","open","base")
                        m "Ты продала мне свои трусики..."
                        m "А через пару часов ты уже публично осудила именно такое поведение..."
                        #m "What would you call this?"
                        #call her_main("I know you are right, [genie_name]...","annoyed","angryL")
                        call her_main("(Но нам нужны очки...)","annoyed","angryL")
                        call her_main("Могу я получить очки?","disgust","glance")
                        m "А что насчет твоих трусиков?"
                        call her_main("Oх, и их тоже, конечно...","angry","worriedCl",emote="05")
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            pass
                    "\"Это для общего блага...\"":
                        her "Именно!"
                        her "Нам очень нужны эти очки..."
                        her "Это не моя вина, что система так коррумпирована..."
                        call her_main("Я останусь символом чести для моих сверстников, несмотря ни на что!","open","closed")
                        call her_main("Могу я получить свои трусики?","open","base")
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            her "И мои очки."

            elif whoring >= 9: #WHORING LVL 04. EVENT LEVEL 03.
                $ new_request_03_heart = 3 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 3 #Event hearts level (0-3)
                $ sc34CG(1, 11)
                call her_main("Как всегда, обычный день в Хогвартсе...","open","closed",xpos="base",ypos="base")
                her "Ничего не произошло..."
                call her_main("Хотя должна признаться...","annoyed","worriedL")
                her "Очень странно, я себя чувствовала свободнее без нижнего белья..."
                her "Хм..."
                hide screen sccg
                call her_main("Могу я получить трусики?","base","base",xpos="right",ypos="base",trans="fade")
                m "Конечно..."
                hide screen hermione_main
                with d3
                call nar(">Ты отдаешь трусики Гермионе...")
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("А мои очки?","base","base")
                    m "Да, да..."

    label back_from_soaked:
    if hg_ps_PantyThief_SoakedPantiesFlag and whoring >= 9 and whoring <= 15 :
        m "Ты можешь идти."
        call her_main("А мои очки?","scream","angryCl")
        m "Ты все еще хочешь очки после того, как я сделал тебе подарок?"
        her "Какой подарок?"
        m "Ты его носишь."
        her "Что, трусики, пропитанные спермой?"
        m "Если ты предпочитаешь очки, просто сними их"
        call her_main("Что ж... Я уже их ношу.","annoyed","worriedL")
        m "Тогда, скажи спасибо за подарок"
        call her_main("Спасибо, [genie_name]...","annoyed","suspicious")
        m "Ты можешь идти."
        her "Доброй ночи, [genie_name]."
    elif hg_ps_PantyThief_SoakedPantiesFlag and whoring > 15:
        $ hg_ps_PantyThief_OBJ.hearts_level = 4 #Event hearts level (0-4)
        m "Ты можешь идти."
        call her_main("Да, [genie_name]","angry","down_raised")
        m "Но, сначала скажи, спасибо. "
        call her_main("Спасибо, за что?","angry","wink")
        m "За мою сперму"
        call her_main("...","base","down")
        call her_main("Спасибо за вашу сперму [genie_name]...","grin","dead")
        m "Можешь идти."
        her "Доброй ночи, [genie_name]."
    else:
        $ gryffindor +=15
        m "Пятнадцать очков \"Гриффиндору\", [hermione_name]. Заслуженно."
        her "Спасибо, [genie_name]..."
        m "Ты можешь идти."
        her "Доброй ночи, [genie_name]."
        #m "Yes, good night..."

    if whoring <= 5:
        $ whoring +=1

    $ hg_ps_PantyThief_OBJ.points += 1
    $ hg_ps_PantyThief_OBJ.inProgress = False #False when favor is not in progress
    $ hg_ps_PantyThief_SoakedPantiesFlag = False #TRUE if you jerked off in panties

    hide screen hermione_main
    hide screen blkfade
    hide screen bld1
    hide screen blktone
    call her_chibi("stand","mid","base")
    show screen genie
    with d3

    call her_walk("mid","leave",2)

    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu
