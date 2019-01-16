###COLLAR SCENES
label start_collar_event:
    hide screen wardrobe
    "Ты уверен, что хочешь начать этот эвент?"
    menu:
        "Да!":
            $ collar = 5
        "Нет!":
            pass
    call screen wardrobe


label collar_scene:

    call play_sound("door") #Sound of a door opening.

    call her_walk("door","mid",1.5)
    pause.2

    call nar(">Гермиона врывается в кабинет и плачет")

    show screen bld1
    call her_main("[genie_name], я шлюха?","angry","base",tears="soft",xpos="right",ypos="base")
    m "О чем ты говоришь ?"
    call her_main("Сьюзен Боунс говорит всем в школе, что я шлюха!","open","angryCl")
    m "Почему эта мисс Бомба называет тебя шлюхой?"
    call her_main("Потому что она узнала, что мы делаем! Она всем говорит, что я ваша шлюха!","soft","base",tears="soft")
    call her_main("Моя репутация разрушена! Что подумают люди, когда узнают, что я делаю с девяностолетним профессором?","mad","worriedCl",tears="soft_blink")
    call her_main("Я буду известна как шлюха до конца своей жизни!","scream","worriedCl")
    her "Я никогда не смогу найти хорошую работу..."
    her "Мои друзья возненавидят меня..."
    call her_main("Пожалуйста, вы же не думаете, что я шлюха, не так ли [genie_name]?","open","base")

    menu:
        "-Ты шлюха-" if lock_public_favors == True:
            jump slut_scene
        "-Ты блядь-" if lock_public_favors == False:
            jump whore_scene
        "-Нет, ты рабыня-":
            jump slave_scene
        "-Конечно нет, ты хорошая девочка-":
            jump good_girl_scene

label slut_scene: #Locked to her being your slut

    m "Конечно ты шлюха."
    call her_main("!!!","angry","base",tears="soft")
    m "Ты приходишь сюда почти каждый день и делаешь ужасные вещи. Нормальная девушка не дает директору трахать ее в жопу."
    call her_main("Я так и знала... Как я смогу это пережить?","mad","worried",tears="soft")
    m "Никак. Тебе придется принять это..."
    call her_main("Что?","angry","base",tears="soft")
    m "От такой репутации шлюхи ты никуда не денешься. Даже если я уйду, ты просто найдешь себе другой член."
    call her_main("Сэр... пожалуйста.","angry","worriedCl",emote="05")
    m "Не делай вид, что ты этого еще не знаешь. Ты знаешь, что в глубине души ты грязная шлюха."
    call her_main("Нет!","scream","worriedCl")
    m "Соси мой член."
    call her_main("...Что?","open","base")
    m "Я сказал соси... мой... член, шлюха."
    call her_main("...","annoyed","worriedL")
    hide screen hermione_main
    with d3

    call her_walk_desk_blkfade #Hides her_main, her_chibi, screen-tones, calls blkfade.

    ">Гермиона подходит и становится на колени перед тобой, тем временем ты достаешь свой член."

    call play_music("playful_tension") #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ hermione_SC.chibi.xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_SC.chibi.ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    $ h_c_u_pic = "hand_ani"
    show screen chair_left
    show screen h_c_u

    hide screen hermione_blink #Hermione stands still.
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call bld
    $ hermione_main_zorder = 8
    m "Хорошая маленькая шлюшка. Теперь, если ты хочешь пососать мой член, я ожидаю, что ты красиво об этом попросишь."
    call her_main("Что? Мне и так плохо, просто дайте мне пососать \nваш член.","upset","wink")
    hide screen hermione_main
    m "Шлюхи выпрашивают член. И поскольку ты шлюха, я жду, что ты будешь умолять меня об этом."
    call her_main("...","normal","worriedCl")
    hide screen hermione_main
    call her_main("Пожалуйста [genie_name], дайте мне отсосать ваш член.","open","base")
    hide screen hermione_main
    m "Хммм, этого было недостаточно. Попробуй еще разок, чуть лучше."
    call her_main("Пожалуйста [genie_name], пожалуйста, позвольте мне сосать\nваш большой прекрасный член.","scream","worriedCl")
    hide screen hermione_main
    m "Хорошая девочка."

    menu:
        "-Трахать горло-":
            m "Вот твоя награда, шлюха!"
            ">Ты хватаешь ее за затылок и засовываешь член глубоко в горло."
            show screen g_c_u
            hide screen h_c_u
            with d3
            call her_main("!!!","shock","wide")
            hide screen hermione_main
            ">Ты чувствуешь, как она прижимается к твоим ногам."
            m "Так, [hermione_name] хорошие шлюхи знают, как заглотить. Просто расслабь горло."
            call her_main("eeettsss hhooooo hhhhggggg!","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "Давай [hermione_name] хорошая шлюха."
            call her_main("...","open_wide_tongue","angryCl")
            hide screen hermione_main
            ">Гермиона расслабила свое горло."
            m "Ахх! У тебя такое тугое горло. Ты грязная шлюха?"
            call her_main("*Slurp!* *Gltch!* *Gulp!*","open_wide_tongue","base")
            hide screen hermione_main
            m "Я задал тебе вопрос, шлюха."
            call her_main("ааааааа    фуууууааааааа","open_wide_tongue","angry")
            hide screen hermione_main
            ">Ты начинаешь быстрее трахать ее горло."
            m "Что такое [hermione_name]? Я не слышу, пока ты сосешь мой член. Попробуй говорить громче."
            call her_main("ааааааааааа фууууууууууааааааааааааа!","shock","wide")
            hide screen hermione_main
            ">Вибрация в ее горле тебе очень нравится."
            m "Еще раз, чтобы я тебя услышал."
            ">Ты высовываешь свой член из ее рта."
            show screen h_c_u
            hide screen g_c_u
            with d3
            call her_main("{size=+10}Я шлюха!{/size}","scream","worriedCl")
            hide screen hermione_main
            m "Да."
            ">Ты обратно засунул член в ее рот."
            show screen g_c_u
            hide screen h_c_u
            with d3
        "-Соси-":
            m "Ну если ты настаиваешь [hermione_name]."
            ">Гермиона берет в рот твой член."
            show screen g_c_u
            hide screen h_c_u
            with d3
            m "Видишь, разве ты не чувствуешь себя лучше, когда у тебя во рту член?"
            call her_main("Ммммммм","open_tongue","glance")
            hide screen hermione_main
            m "Признайся, тебе это нравится."
            call her_main("*Slurp!* *Gulp!* *Slurp!*","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "Ты любишь, когда тебя используют как игрушку."
            call her_main("*Gulp!* *Gobble!* *Gobble!*","open_wide_tongue","angryCl")
            hide screen hermione_main
            m "Ты будешь расстроена, если люди узнают кто ты."
            call her_main("*Gulp!* *Gobble!* *Slurp!*","open_tongue","glance")
            hide screen hermione_main
            m "Но в глубине души ты просто рада, что тебе не нужно вести себя как, хорошая девочка."
            call her_main("*Slurp!* *Gobble!*","open_wide_tongue","angryCl")
            hide screen hermione_main
            m "Не так ли?"
            call her_main("...","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "Я задал тебе вопрос, шлюха."
            show screen h_c_u
            hide screen g_c_u
            with d3
            ">Она вытаскивает твой член изо рта."
            call her_main("...Да. Я шлюха.","normal","worriedCl")
            hide screen hermione_main
            m "Рад слышать, что ты наконец признаешь это. А теперь, обратно в рот."
            call her_main("Да [genie_name]","smile","glance")
            hide screen hermione_main
            ">Гермиона берет член обратно в рот с новым рвением."
            show screen g_c_u
            hide screen h_c_u
            with d3

    m "Ах, Я уже близко, девочка."
    m "Готовься."
    ">Гермиона сосредотачиваться на кончике члена, облизывая его."
    m "Сейчас кончу!"
    ">Ты вытаскиваешь из ее рта член и начинаешь дрочить его."
    $ g_c_u_pic = "cum_on_face_ani"
    $ u_sperm = "characters/hermione/face/auto_07.png"
    $ uni_sperm = True
    m "Вот твоя награда, ебанная спермоглотка!"
    ">Ты кончил ей на лицо."
    ">Одна капля спермы попала ей прямо в ноздрю."
    m "Кто шлюха?"
    $ g_c_u_pic = "cum_on_face_blink_ani"
    call her_main("Я...","grin","baseL")
    hide screen hermione_main
    m "Хорошо, теперь, когда мы это узнали, у меня есть для тебя подарок."
    call her_main("Подарок? Какой?","base","down")
    hide screen hermione_main
    m "Это прекрасное ожерелье, чтобы помочь вспомнить, кто ты."

    #sQuest "slave" collar reward
    call give_reward(">Ты даришь ей ошейник \"whore\".\n ошейник \"whore\" добавлен в твой гардероб.")

    call her_main("Это не ожерелье, это - ошейник \nс надписью whore! Я не могу носить его!","angry","wide")
    hide screen hermione_main
    m "Ты можешь носить его."
    m "Ты-МОЯ шлюха, и ты хорошо запомнишь это. А теперь надень и убирайся из моего кабинета."
    call her_main("...Ладно","angry","down_raised")
    hide screen hermione_main
    ">Она застегивает ошейник вокруг шеи."

    $ h_neckwear = "neck_slut_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 2
    call update_her_uniform

    call her_main("Можно мне хотя бы полотенце или еще что-нибудь, чтобы \nочистить свое лицо?","angry","base")
    hide screen hermione_main
    m "Зачем? Все уже знают, какая ты шлюха, возвращайся в свою комнату со спермой на лице."
    call her_main("Вы серьезно?!","upset","closed")
    hide screen hermione_main
    m "Да, и если ты когда-нибудь захочешь отсосать мой член снова, ты будешь делать то, что я скажу."
    call her_main("...Да, [genie_name].","open","closed")
    hide screen hermione_main
    m "Что ж, иди."
    call her_main("Спокойной ночи [genie_name].","base","glance")
    hide screen hermione_main
    m "Спокойной ночи. {w}Шлюха."
    call her_main("...","base","down")
    show screen genie
    hide screen chair_left
    hide screen hermione_main
    hide screen chair_left
    hide screen g_c_u
    hide screen h_c_u
    hide screen ctc
    hide screen bld1
    $ hermione_main_zorder = 5
    $ display_h_tears = False

    jump end_hg_pf #Hides screens, calls her_walk, resets and ends day.
    #she then comes back in the evening with a story about some people abusing her and some congratulating her

label whore_scene: #(locked behind the public whoring flag)

    #sex scene where she begs genie to cum inside her
    #genie yells at her and makes her admit she is a whore
    #he cums inside her
    #she then comes back later that night after Ginny makes the quidditch team use her

    m "Ты не шлюха [hermione_name]."
    call her_main("Спасибо вам, сэ-","mad","worried",tears="soft")
    m "Ты хуже шлюхи, ты блядь."
    call her_main("Что? Какая разница?","angry","base")
    m "Шлюха-это та, кто любит секс. Блять-это те, кто зависим от него."
    m "Тебе все равно, где ты его получишь! Пока кто-то трахает тебя, тебе все равно кто он."
    call her_main("Я-Я-Я-","open","worriedCl")
    m "Ты даже трахалась со своими лучшими друзьями, не так ли?"
    m "Уверен, что ты умоляла их сделать это."
    m "Посмотри, кем ты стала, не более чем школьная игрушка, готовая дать каждому."
    call her_main("Сэр, пожалуйста, вы слишком грубы...","shock","worriedCl")
    m "О, эта маленькая шлюшка расстраивается? Не волнуйся, я заставлю тебя чувствовать себя лучше.."
    her "Как?"
    m "Иди сюда и нагнись."
    call her_main("Вы серьезно? Что вы только что сказали?","angry","base")
    m "Да, теперь будь хорошей блядбю и нагнись над моим столом, и я дам тебе то, что ты хочешь."
    call her_main("...","angry","down_raised")

    call her_walk_desk_blkfade
                                                                                                                                                                                  #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "pause_sex"
    show screen chair_left
    show screen g_c_u
    call hide_blkfade

    $ hermione_main_zorder = 8

    ">Гермиона тихо подходит к твоему столу и наклоняется."
    m "Посмотрим, какая ты хорошая маленькая шлюха. Теперь, если ты попросишь красиво, я трахну тебя."
    call her_main("...","angry","down_raised")
    hide screen hermione_main
    call her_main("Пожалуйста [genie_name].","open","down")
    hide screen hermione_main
    m "Что, пожалуйста?"
    call her_main("Пожалуйста, трахните меня...","mad","worried",tears="soft")
    hide screen hermione_main
    m "Я не уверен, что я достаточно услышал. Тебе нужно сказать громче."
    call her_main("{size=+5}Пожалуйста, трахните мою пизду{/size}","scream","wide")
    hide screen hermione_main
    m "Да, ты красиво попросила!"
    $ g_c_u_pic = "sex_ani"
    ">Ты крепко сжал ее бедра и вонзаешь свой член в ее киску."
    m "Ах, ты все еще такая тугая."
    m "Я думал, что ты растянешься после того, как ты перетрахала всех парней."
    call her_main("[genie_name]...","open","worriedCl")
    hide screen hermione_main
    m "Не строй из себя невинность [hermione_name]. Я знаю, чем ты занимаешься в комнатах после наступления темноты.."
    m "Просто признайся, кто ты."
    call her_main("{size=-5}Я блядь.{/size}","grin","ahegao")
    hide screen hermione_main
    m "Что? Я не слышу тебя."
    call her_main("Я блядь.","silly","ahegao")
    hide screen hermione_main
    m "Отлично, теперь умоляй меня."
    call her_main("Умолять вас, о чем?","silly","dead")
    hide screen hermione_main
    m "Умоляй меня кончить в твою киску, блядь."
    call her_main("Пожалуйста, заполните мою киску своей спермой.","grin","dead")
    hide screen hermione_main
    m "Хорошая маленькая блядь, кому еще ты это говорила?"
    m "Это только мне так говоришь или любому встречному мальчику?"
    call her_main("...","angry","wink")
    hide screen hermione_main
    m "Скажи мне, девочка."
    call her_main("Я прошу кончить внутрь каждого мальчика, который меня трахает!","shock","worriedCl")
    hide screen hermione_main
    m "Какая ебанная блядь."
    call her_main("Я-я кончаю.","open","surprised",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Пожалуй, я могу присоединиться к тебе."
    ">Ты увеличиваешь темп."
    m "Вот твоя сперма, блядь. Ты ее заслужила."
    ">Ты начинаешь кончать в ее киску."
    $ g_c_u_pic = "sex_cum_in_ani"
    call her_main("!!!","scream","surprised",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Вот так, возьми все, шлюха."
    call her_main("...","grin","dead",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Может ты как-то отблагодаришь меня?"
    call her_main("...Спасибо [genie_name].","base","concerned",cheeks="blush",tears="soft")
    hide screen hermione_main
    m "За что спасибо?"
    call her_main("Спасибо за то, что... кончили в мою киску.","grin","dead",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Всегда пожалуйста, девочка. Хорошая блядь всегда должна быть благодарна."
    call her_main("Да [genie_name].","grin","closed",cheeks="blush",tears="mascara")
    hide screen hermione_main
    call blkfade

    show screen genie
    hide screen chair_left
    hide screen g_c_u
    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d3
    $ hermione_main_zorder = 5
    ">Гермиона встает на ноги"
    m "Ну так как ты поблагодарила, у меня появился подарок для тебя."
    call her_main("Подарок?","open","concerned",cheeks="blush",tears="mascara")
    m "Да, это прекрасное украшение в память о твоем самопринятии."

    #sQuest "whore" collar reward
    call give_reward(">Ты подарил ошейник \"whore\".\n Ошейник \"whore\" добавлен в твой гардероб.")

    call her_main("Ошейник? С надписью whore?","open","squint",cheeks="blush")
    call her_main("Как это может быть украшением?","open","annoyed",cheeks="blush")
    m "Ну, я ожидаю, что ты будешь носить постоянно, как к примеру кольцо, поэтому я думаю, что оно выглядит как украшение."
    call her_main("Вы ждете, что я буду носить его постоянно и не только в вашем кабинете?","scream","angry",cheeks="blush",tears="messy")
    m "Конечно. Я же знаю, какая ты блядь, это для того, чтобы все остальные узнали."
    call her_main("Что обо мне подумают люди?","scream","worriedCl",cheeks="blush",tears="messy")
    m "Они подумают правду, что ты бестыжая блядь."
    call her_main("...Пфф","angry","suspicious",cheeks="blush")
    m "Ну, что бы ты ни думала, я ожидаю, что ты наденешь его, а затем уйдешь из моего кабинета."
    call her_main("...Ладно","shock","down_raised",cheeks="blush",tears="crying")
    ">Она надевает ошейник вокруг шеи и застегивает его."

    $ h_neckwear = "neck_whore_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 3
    call update_her_uniform

    call her_main("Спокойной ночи [genie_name].","angry","dead",cheeks="blush",tears="crying")
    m "Спокойной ночи, блядь."
    hide screen hermione_main
    with d3

    $ display_h_tears = False
    jump end_hg_pf

    #m "Also, come see me tonight after everyone has seen the new you. I want to hear what they say."
    #call her_main("...yes [genie_name].","angry","suspicious",cheeks="blush",tears="messy")


label slave_scene:

    m "Не будь глупой [hermione_name], ты не шлюха."
    call her_main("Спасиб-","base","base")
    m "Ты рабыня."
    call her_main("Кто я?","upset","wink")
    m "Ты рабыня Мисс Грейнджер. В частности, моя рабыня."
    call her_main("О чем вы вообще говорите? Я вам не рабыня.","angry","angry")
    m "Ты уверена? Ты приходишь сюда всякий раз, когда я зову, желая делать все, что скажу."
    m "Просто умоляла сделать что-нибудь, чтобы угодить мне."
    m "Когда в последний раз ты мне отказывала?"
    call her_main("Ну, я...","annoyed","worriedL")
    m "Именно, ты стала моей рабыней и даже не осознала этого."
    call her_main("То, что я забочусь о своем факультете, не значит, что-","angry","worriedCl",emote="05")
    m "Пожалуйста, когда ты последний раз получала за это очки?"
    m "Ты просто хочешь порадовать меня. Эти моменты-оправдание, которое внушаешь себе, поэтому не признаешься, кто ты есть."
    m "Теперь будь хорошей девочкой и нагнись над столом."
    call her_main("...","angry","base")

    call her_walk_desk_blkfade

    hide screen genie
    $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "pause_sex"
    show screen chair_left
    show screen g_c_u
    hide screen hermione_blink #Hermione stands still.
    call hide_blkfade

    $ hermione_main_zorder = 8
    ">Гермиона подходит к столу, наклоняется, а затем поднимает юбку."
    call her_main("Да [genie_name].","angry","down_raised")
    hide screen hermione_main
    m "Правильно, маленькая рабыня."
    m "А теперь попроси меня хорошенько трахнуть твою маленькую попку."
    call her_main("Пожалуйста, [genie_name], трахните мою маленькую попку.","open","closed")
    hide screen hermione_main
    m "Хорошая девочка."
    ">Ты по яйца засовываешь свой член в ее задницу."
    $ g_c_u_pic = "sex_ani"
    m "Ты очень тугая, наслаждаешься этим?"
    call her_main("Да [genie_name], я люблю это.","base","ahegao_raised")
    hide screen hermione_main
    m "Хорошо, убедись, что держишься крепко."
    ">Ты набираешь скорость и начинаешь трахать ее задницу не на шутку."
    m "Теперь расскажи мне, девочка. Кому ты принадлежишь?"
    call her_main("Вам.","open","down")
    hide screen hermione_main
    m "Хорошо, и кто я такой?"
    call her_main("Профессор Дамблдор.","grin","baseL")
    hide screen hermione_main

    call slap_her

    "Ты пару раз шлепаешь ее по заднице."
    m "Это не правильный ответ. Кем я являюсь для тебя [hermione_name]? Для тебя я твой хозяин."
    m "Ты поняла?"
    call her_main("Да.","angry","base",tears="soft")
    hide screen hermione_main

    call slap_her

    "Ты очень сильно шлепаешь по ее заднице, оставляя ярко-красный след."
    m "Что да?"
    call her_main("Да, хозяин.","angry","base",tears="soft")

    $ genie_name = "Хозяин"

    hide screen hermione_main
    m "Хорошо, ты быстро учишься."
    m "Теперь, если я твой хозяин, то кто ты?"
    call her_main("{size=-7}Рабыня{/size}","soft","base",tears="soft")
    m "Не расслышал."
    call her_main("Рабыня.","mad","worried",tears="soft")

    $ hermione_name = "Рабыня"

    hide screen hermione_main

    call slap_her

    ">Ты опять шлепаешь по ее заднице."
    m "Ты не просто обычная [hermione_name]."
    call her_main("Нет?","annoyed","annoyed")
    hide screen hermione_main
    m "Нет, конечно нет."
    m "Ты моя личная рабыня."
    call her_main("Я думаю, что собираюсь кончить хозяин.","angry","down_raised")
    hide screen hermione_main

    call slap_her

    ">Ты шлепаешь по левой ягодице."
    m "Ты кончишь, когда я позволю тебе, и ни секундой раньше."
    call her_main("Пожалуйста, хозяин, можно мне кончить?","angry","wide")
    hide screen hermione_main
    m "Нет, пока я не кончу."
    call her_main("Пожалуйста, поторопитесь.","open","worriedCl")
    hide screen hermione_main
    m "Ну приложи тогда усилий, девочка. Если ты хочешь, чтобы я кончил, то тебе лучше постараться."
    ">Гермиона начинает двигаться на встречу тебе, от этого ты получаешь массу удовольствия."
    m "Вот так, девочка. Я скоро кончу..."
    ">Ты хватаешь ее за бедра и насаживаешь на свой пульсирующий член."
    m "АХХ"
    $ g_c_u_pic = "sex_cum_in_ani"
    ">Ты кончаешь в ее тугую дырочку."
    call her_main("Я кончаю!","scream","wide")
    hide screen hermione_main
    ">Ты по-прежнему кончаешь в ее попу."
    call her_main("Спасибо, сэр.","soft","ahegao")
    hide screen hermione_main

    call slap_her

    ">Шлепок!"
    m "Что? Ты не назвала меня хозяином."
    call her_main("Спасибо, хозяин. Спасибо, хозяин.","grin","dead")
    hide screen hermione_main
    m "Вот так, девочка."
    ">Гермиона закрывает глаза, из-за оргазма."
    m "На колени, девочка."
    call her_main("Ч-ч-что? Зачем?","angry","base")
    hide screen hermione_main
    m "Потому что я так сказал. Теперь встань со стола и на колени."
    call her_main("Да, хозяин.","angry","down_raised")
    hide screen hermione_main
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ hermione_SC.chibi.xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_SC.chibi.ypos = 10
    $ h_c_u_pic = "hand_ani"
    hide screen g_c_u
    show screen h_c_u
    ">Гермиона встает из-за стола и становится перед тобой на колени."
    m "Скажи мне, кто ты."
    call her_main("Рабыня, хозяин.","base","down")
    hide screen hermione_main
    m "Хороший ответ. И потому, я сделаю тебе подарок."

    #sQuest "slave" collar reward
    call give_reward(">Ты подарил ей ошейник с надписью \"slave\".\n ошейник с надписью\"slave\" добавлен в твой гардероб.")

    call her_main("Что это?","base","glance")
    hide screen hermione_main
    m "Это ошейник, чтобы все знали, что ты моя собственность, моя рабыня."
    call her_main("Я должна носить его постоянно?","base","suspicious")
    hide screen hermione_main
    m "Да, должна."
    call her_main("...","angry","down_raised")
    pause       ###new
    call her_main("Да, хозяин...","angry","wink")
    hide screen hermione_main
    ">Она затягивает ошейник вокруг шеи."

    $ h_neckwear = "neck_slut_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 1
    call update_her_uniform

    m "Этот взгляд тебе идет, девочка."
    call her_main("Спасибо, хозяин. Получу ли я, какие-нибудь очки \nсегодня?","base","down")
    hide screen hermione_main
    m "Хахаха, конечно нет. Рабам не платят, девочка, вот что отличает их от остальных."
    call her_main("Я полагаю, вы правы.","base","glance")
    hide screen hermione_main
    show screen blkfade
    with d3                                                                                                                                                                                 #HERMIONE
    show screen genie
    hide screen chair_left
    hide screen g_c_u
    hide screen h_c_u
    show screen hermione_blink #Hermione stands still.
    $ hermione_SC.chibi.xpos = 400
    call hide_blkfade

    $ hermione_main_zorder = 5
    hide screen hermione_main
    with d3

    $ display_h_tears = False
    jump end_hg_pf


label good_girl_scene:

    m "Конечно, ты не шлюха, Мисс Грейнджер.."
    m "Ты просто делаешь все возможное, чтобы помочь своим друзьям."
    call her_main("*всхлип* Серьезно [genie_name]?","open","worriedCl")
    m "Серьезно. Ты бы не сделала ничего из этого если система очков была бы справедливой?"
    call her_main("*всхлип* Я думаю, нет...","angry","base")
    m "Я уверен, как только Мисс Боунс узнает для чего ты это делаешь, то она поймет."
    call her_main("Вы действительно так думаете [genie_name]?","angry","down_raised")
    m "Я знаю, ты хорошая девочка, мисс Грейнджер."
    call her_main("Спасибо [genie_name].","base","base")
    m "Как только Гриффиндор выиграет Кубок, никто даже не вспомнит, что они говорили, они будут благодарны тебе."
    call her_main("Да, вы правы [genie_name]. Полагаю, я просто слишком остро отреагировала.","base","happyCl")
    m "Не беспокойся об этом."
    call her_main("Прежде чем я уйду...","grin","baseL")
    call her_main("Вы не хотите купить у меня услугу?","smile","glance")
    m "Конечно, что бы ты хотела сделать?"
    call her_main("Ну, я могу показать свои сиськи.","base","down")
    call her_main("За 50 очков, конечно...","angry","wink")
    m "Справедливо."
    call her_main("Спасибо [genie_name].","base","glance")
    ">Гермиона медленно поднимает топик."

    call set_hermione_action("lift_top")
    call ctc

    call her_main("Вам нравится [genie_name]","annoyed","base")
    m "Конечно, они прекрасны."
    call her_main("Спасибо [genie_name], вы всегда такой добрый..","base","closed")
    ">Она опускает свой топик."

    call set_hermione_action("none")
    pause.5

    m "50 очков Гриффиндору."
    $ gryffindor += 50
    call her_main("Спасибо [genie_name]. Доброй ночи.","smile","angry")
    m "Тебе тоже [hermione_name]."
    hide screen hermione_main
    with d3

    $ display_h_tears = False
    $ collar = 4

    jump end_hg_pf
