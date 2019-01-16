

### CUM ADDICTION ###

label potion_scene_3_1_1: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], сегодня у меня есть особое зелье, которое я бы хотел, чтобы ты выпила."
    call her_main("Что оно сделает со мной?","normal","frown") 
    m "Как всегда, это должно остаться сюрпризом."
    call her_main("Вы же не собираетесь снова превратить меня в кошку, [genie_name]?","normal","frown") 
    call her_main("","normal","frown") 
    m "Конечно нет, а теперь можешь уже выпить это зелье?"
    call her_main("...","annoyed","angryL") 
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Гермиона начинает осторожно пить зелье.") 
    call her_main("","cum","worriedCl") 
    pause .5
    call her_chibi("stand","mid","base") 
    
    call her_main("Это не зелье! Это просто бутылка с вашей спермой!","scream","angryCl") 
    call her_main("Уххх, и такая холодная.","disgust","narrow") 
    m "Так что, это зелье на вкус как сперма?"
    call her_main("Конечно да, на что еще может быть похож этот вкус?","angry","angry") 
    call nar(">Гермиона начинает бессознательно облизывать свои губы.") 
    call her_main("По крайней мере, предупредите меня в следующий раз, когда вы заставите выпить свою сперму, [genie_name].","open","worriedL") 
    m "Что ты имеешь ввиду, говоря в следующий раз?"
    call her_main("Ну, вы такой извращенец, что, вероятно, попытаетесь сделать это снова. По крайней мере, предупредите меня, чтобы это не так шокировало.","annoyed","annoyed") 
    m "Хорошо, [hermione_name], теперь я буду говорить заранее."
    call her_main("Это все, [genie_name]?","annoyed","angryL") 
    m "Да, [hermione_name], 20 очков Гриффиндору."
    call her_main("Спасибо, [genie_name].","open","suspicious") 
    call nar(">Гермиона быстро уходит из кабинета, прихватив с собой зелье.") 
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    
    call her_walk("mid","leave",2) 
    
    $ addicted = True
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_3_1_2: #Scene where Hermione comes back addicted to your cum (replace sucking noises with actual text)
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base") 
    pause.5
    
    show screen bld1
    call nar(">Гермиона врывается в твой кабинет.") 
    call her_main("Что вы сделали со мной?!","scream","worriedCl") 
    m "О чем ты говоришь, [hermione_name]?"
    call her_main("Ааа, это не имеет значения! Просто дайте мне отсосать вам!!!","annoyed","worriedL") 
    m "Зачем тебе это нужно? Ты же самая примерная ученица в школе!"
    call her_main("Вы точно знаете, что сделали со мной. Теперь позвольте мне отсосать ваш грязный старый член.","angry","angry") 
    
    menu:
        "-Дать ей свой член-":
            m "Что ж, если ты настаиваешь... [hermione_name]."
        "-Заставить ее умолять тебя-":
            m "Я не думаю, что ты этого заслуживаешь, назвав его грязным и старым."
            m "Возможно, если ты будешь более вежливой..."
            call her_main("Ладно. Пожалуйста, дайте мне вам отсосать, [genie_name].","upset","wink") 
            m "Хмм, мне кажется, это было не слишком искренне."
            call her_main("Пожалуйста, [genie_name], позвольте мне отсосать ваш большой толстый член. Вполне достаточно?","angry","worriedCl",emote="05") 
            m "Гораздо лучше."
         
    call blkfade 
    pause 1
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u
    
    call her_chibi("hide") 
    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    call ctc 
    
    $ hermione_main_zorder = 8
    
    show screen bld1
    call nar(">Пока ты доставал свой член из-под мантии, Гермиона уже подошла к тебе.") 
    call her_main("","disgust","glance") 
    $ g_c_u_pic = "hand_ani"
    with d3      
    her "Вы хоть представляете как мне тяжело было сегодня на уроках?"
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3      
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    call her_main("","annoyed","angryL") 
    $ g_c_u_pic = "hand_ani"
    with d3   
    her "Такой возбужденный."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Gobble!* *Slurp!*"
    call her_main("","grin","baseL") 
    $ g_c_u_pic = "hand_ani"
    with d3   
    her "Почему вы не кончаете?"
    her "Я все попробовала."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Gobble!* *Slurp!* *Slurp!*"
    call her_main("","smile","glance") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Недавно я мастурбировала в ванной для девочек."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    call her_main("","annoyed","annoyed") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Ничего не работает."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","base","ahegao_raised") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Все, о чем я сейчас думаю - это какова на вкус ваша сперма."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Чавк.*"
    m "Кто-то становится полноценной шлюшкой, [hermione_name]"
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","open_tongue","glance") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Вы знаете, почему это происходит со мной."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3  
    her "*Slurp!* *Slurp!* *Gulp!*"
    call her_main("","smile","glance") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Что бы ни было в этом восхитительном зелье, вы заставили меня его выпить."
    hide screen hermione_main
    m "Восхитительном? По моему, ты сказала, что это просто бутылка с моей спермой?"
    m "Ты уверена, что ты просто не маленькая шлюха, которая стала зависимой от спермы своего директора?"
    call her_main("Я уверена, там внутри было что-то еще!","angry","wink") 
    hide screen hermione_main
    m "Ничего не говори, [hermione_name]. Теперь, если ты хочешь получить свою награду, лучше вернуться к работе."
    call her_main("","base","suspicious") 
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "..."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Slurp!* *Gulp!*"
    call nar(">Она так восторжена. Ты чувствуешь, что великий потоп уже на подходе.") 
    
    menu:
        "-Кончить ей в глотку-":
            m "Я уже готов, детка!"
            call nar(">Гермиона быстро проглатывает, большую часть твоей спермы. Ты чувствуешь, как кончик твоей головки прижат к входу в ее горло.") 
            m "Тебе нужно сделать больше, если хочешь получить свою награду, [hermione_name]."
            call nar(">Ты кладешь руки ей на затылок, притягивая к себе голову.") 
            call her_main("{size=+7}!!!{/size}","scream","worriedCl") 
            hide screen hermione_main
            call nar(">Ты получаешь море удовольствий, чувствуя членом ее горло.") 
            m "Лучше начинай глотать, шлюха!"
            call nar(">Ты начинаешь изливать свою густую сперму ей в желудок.") 
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call nar(">Глаза Гермионы расширяются. По ее щекам текут слезы, когда она ощущает, как сперма заполняет ее.") 
            call her_main("аааааааааа!!!","scream","wide") 
            hide screen hermione_main
            call nar(">Она тянет свои руки к себе под юбку и начинает оргазмировать.","start") 
            call nar(">Смотря на ее удовольствия, ты и сам гораздо дольше испытываешь оргазм.","end") 
            m "Ты грязная маленькая девочка. Отделалась от директора, засунув его член себе в глотку."
            m "Держу пари, тебе нравится быть моей игрушкой."
            call nar(">Она ничего не говорит, но ускоряет темп своей мастурбации.","start") 
            call nar(">Ты, наконец, достаешь свой член.","end") 
            call her_main("Оно не прекращается!","shock","worriedCl") 
            hide screen hermione_main
            m "О чем ты?"
            call her_main("Я-я не могу перестать кончать, [genie_name]...","angry","base") 
            hide screen hermione_main
            call nar(">Стимуляция оказывается слишком сильная, и она теряет сознание.") 
            
        "-Кончить ей в рот-":
            m "Вот так, детка! Готовься!"
            call nar(">В предвкушении, Гермиона пытается кончиком языка ласкать твой член.") 
            g4 "Вот и все! Начинай глотать!"
            call nar(">Ты кончаешь ей в рот.") 
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call her_main("мммммм.... *gulp* *gulp*","full_cum","dead") 
            hide screen hermione_main
            call nar(">Глаза Гермионы становятся пустыми, когда она глотает твою сперму.") 
            m "Вот так, глотаешь как хорошая девочка, ты заработала свой приз."
            call her_main("*чавк*","cum","worriedCl") 
            hide screen hermione_main
            call nar(">Когда она глотает, ты замечаешь, что ее ноги начинают биться в конвульсиях-она испытывает невероятный оргазм.") 
            call her_main("*gulp* *gulp* *gulp*","full_cum","dead") 
            hide screen hermione_main
            call nar(">Ты наконец достал член из ее ненасытного рта.") 
            m "Очень хорошая девочка. Ты почти не испачкалась."
            m "Наверное, стоит аккуратнее это делать."
            call nar(">Ты вытираешь кончик носа Гермионы.") 
            call her_main("...","cum","worriedCl") 
            hide screen hermione_main
            m "Так намного лучше."
            call nar(">Ее ноги не перестают дрожать с момента наступления оргазма.") 
            m "Хорошо, ты не собираешься ничего сказать, [hermione_name]?"
            call her_main("Спасибо, хозя...","silly","dead") 
            hide screen hermione_main
            call nar(">Она падает на землю, ее ноги все еще дрожат.") 
            
        "-Кончить ей на лицо-":
            m "Готовься, девочка, я на подходе!"
            call nar(">Гермиона увеличивает свои усилия и сосредотачивается на головке твоего члена.") 
            m "Не так быстро, [hermione_name]."
            $ g_c_u_pic = "hand_ani"
            with d3 
            call nar(">Ты быстро вытаскиваешь пенис из ее рта.") 
            call her_main("Что вы делаете, [genie_name]?","shock","wide") 
            hide screen hermione_main
            m "Вручаю тебе главную награду."
            $ g_c_u_pic = "cum_on_face_ani"
            with d3 
            $ uni_sperm = True
            call nar(">Ты начинаешь дрочить свой член и кончаешь на лицо этой похотливой ведьме.") 
            m "Получай, грязная шлюха!"
            call her_main("{size=+5}!!!{/size}","soft","ahegao") 
            hide screen hermione_main
            call nar(">Гермиона сразу начинает бесстыдно мастурбировать перед тобой.") 
            call her_main("{size=+5}Я кончаю{/size}","angry","base") 
            hide screen hermione_main
            m "Что это было, [hermione_name]?"
            call her_main("Я кончила!","scream","wide") 
            hide screen hermione_main
            m "Просто от того, что я кончил на тебя? Ты стала такой развратной, мисс Грейнджер!"
            m "Что подумали бы твои родители? Глядя на то, как ты глотаешь сперму старого деда?"
            call her_main("Нет, подалуйста, хватит, я-","angry","worriedCl",emote="05") 
            hide screen hermione_main
            m "Им будет стыдно за то, кем ты стала. Шлюха, которую используют как секс игрушку."
            call her_main("Я-я кончила снова, [genie_name]. Я не могу остановиться...","scream","worriedCl") 
            hide screen hermione_main
            call nar(">Голос Гермионы замирает, когда она перестает возбуждаться.") 
            
        "-Кончить на пол-":
            m "Я кончаю, детка!"
            call her_main("мммммммммм....","open_wide_tongue","base") 
            hide screen hermione_main
            call nar(">Она приготовилась принять сперму в лицо, но ты кладешь руку ей на лоб и отталкиваешь.") 
            $ g_c_u_pic = "hand_ani"
            with d3 
            call her_main("[genie_name], что вы делаете?","angry","wide") 
            hide screen hermione_main
            m "Даю тебе приз!"
            call nar(">После нескольких быстрых движений твой член взрывается и извергает сперму на пол.") 
            call her_main("ПРОФЕССОР! Зачем вы ее испортили?","angry","down_raised") 
            hide screen hermione_main
            m "Она не испортилась, [hermione_name], твоя награда ждет тебя прямо там."
            call her_main("Я не буду этого делать, слизывать ее с пола это очень отвратительно.","angry","base") 
            hide screen hermione_main
            m "Ну, ты всегда можешь прийти на следущий день."
            call her_main("ЖДАТЬ ДО ЗАВТРА?! Я не могу так долго ждать! Разве вы не можете снова кончить?","angry","wide") 
            hide screen hermione_main
            m "Нет, [hermione_name], я уставший старик который очень сильно хочет спать."
            m "Либо ты ешь мою сперму с пола, либо приходишь завтра."
            call her_main("...Ладно.","upset","closed") 
            hide screen hermione_main
            call nar(">Она неохотно начинает слизывать твою сперму с пола пальцами.") 
            
            menu:
                "-Наблюдать за ней-":
                    call her_main("","full_cum","dead") 
                    call nar(">Она собирает столько, сколько может, в ладонь и быстро подносит ее ко рту.","start") 
                "-Заставить ее лизать пол-":
                    m "Не с пальцев, [hermione_name]."
                    call her_main("Что вы имеете в виду? Как еще я должна ее съесть?","angry","base") 
                    hide screen hermione_main
                    m "У тебя прекрасный язычок, я предлагаю использовать его."
                    call her_main("Вы думаете, что я стану СЛИЗЫВАТЬ вашу сперму с пола?","angry","down_raised") 
                    hide screen hermione_main
                    m "Именно. Если, конечно, тебя устроит вернуться в свою комнату голодной и неудовлетворенной, то можешь этого не делать."
                    call her_main("...","angry","base") 
                    hide screen hermione_main
                    call nar(">Она наклоняется, опустив голову к полу.") 
                    $ aftersperm = True
                    call her_main("(Это так унизительно...)","open_wide_tongue","angry") 
                    hide screen hermione_main
                    call nar(">Она высовывает язык, слизывая твою сперму.","start") 
                    
            call nar(">Эффект мгновенен.","end") 
            $ aftersperm = True
            call her_main("Я-я...кончаю...","cum","worriedCl") #small text
            hide screen hermione_main
            m "Что?"
            call her_main("Я кончаю!","silly","dead") 
            hide screen hermione_main
            call nar(">Рука Гермионы возится под юбкой. Девченка начинает получать новый оргазм.") 
            call her_main("Что со мной не так, [genie_name]?","silly","ahegao") 
            hide screen hermione_main
            m "Много чего, [hermione_name], учитывая, что ты взяла и съела мою сперму с пола."
            call her_main("Я не могу перестать кончать...","shock","baseL",cheeks="blush",tears="soft") 
            hide screen hermione_main
            call nar(">Гермиона теряет сознание.") 
            
    hide screen bld1
    hide screen hermione_main
    call nar(">Гермиона находится в бессознательном состоянии на полу.") 
    
    menu:
        "-Вернуть ее в свою комнату-":   
            call nar(">Ты забираешь ее тело и несешь в комнату.","start") 
            call nar(">Когда ты входишь в общежитие, ты слышишь ее бормотание.","end") 
            call her_main("Да...Я проглотила ее...","open","worriedCl") 
            hide screen hermione_main
            call nar(">Ты аккуратно кладешь ее в постель.") 
            m "Приятных снов, шлюха."
        "-Очистить ее и отнести ее в свою комнату-":   
            $ uni_sperm = False
            call nar(">Ты забираешь ее тело и несешь в комнату.","start") 
            call nar(">Когда ты входишь в общежитие, ты слышишь, как она бормочет во сне.","end") 
            call her_main("Вы хотите поцеловаться, [genie_name]? Конечно, я не против...","open","closed") 
            hide screen hermione_main
            call nar(">Ты аккуратно кладешь ее в постель.") 
            m "Спи крепче, Гермиона."
            
    call blkfade 
    pause.5
    
    hide screen hermione_main
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk
    show screen genie
    hide screen blktone
    $ addicted = False
    $ uni_sperm = False
    $ aftersperm = False
    call hide_blkfade 
    
    $ hermione_main_zorder = 5
    
    $ hermione_sleeping = True
    call music_block
    jump night_main_menu
    
    
    
    
    
    
label potion_scene_7: #hyper sensitivity potion
    m "Я хочу, что бы ты выпила одно зелье."
    her "Ладно."
    m "Просто так? Даже не станешь возмущаться и спрашивать, что оно с тобой сделает?"
    her "Можете сказать мне что это?"
    m "Нет, конечно нет."
    her "Так, а зачем вы спросили?"
    m "Ладно, вот оно."
    menu:
        "-Бросить ей в грудь-":
            jump potion_scene_7_1
        "-Дать ей в руки-":
            jump potion_scene_7_2
        "-Бросить под юбку-":
            jump potion_scene_7_3

            
            
### HYPER SENITIVITY POTION ###
            
label potion_scene_3_2_1: #Hyper sensitive breasts
    call nar(">Ты открываешь зелье и выплескиваешь его на грудь Гермионы.") 
    her "Профессор! Что вы сделали?"
    call nar(">Ты положил наполовину заполненную бутыль на стол.") 
    m "Это несчастный случай. Мои руки уже не те, что были прежде."
    her "Уххх, теперь мне придется идти менять свою одежду перед занятиями."
    her "Я рассчитываю получить соответствующую компенсацию."
    m "Ладно, ладно. Как насчет того, чтобы я сделал тебе приятный массаж?."
    her "Массаж? Это вряд ли справедливая компенсация!"
    m "Ты серьезно?"
    her "Абсолютно."
    m "Хорошо, тогда я заключу с тобой пари."
    her "...{p}Продолжайте..."
    m "Я начну массировать тебя. Если тебе не понравится через две минуты, можешь сказать мне остановиться."
    her "И что я получу, если скажу вам остановиться?"
    m "Двести очков."
    her "ДВЕСТИ?!"
    m "Но если ты не попросишь меня прекратить, я смогу массировать тебя, так долго, что мы тут состаримся."
    her "По рукам."
    m "Ты уверена?"
    her "Без обид, [genie_name], но я думаю, что смогу устоять перед массажем за 200 очков."
    m "Ты совершенно уверена в себе, подымим ставки?"
    her "Вы хотите сказать что я могу получить еще больше?"
    m "Пятьсот."
    her "{size=+10}ПЯТЬСОТ???!{/size}" #size up
    her "Принято."
    m "Я же даже не сказал, что будет, если ты проиграешь."
    her "Это не имеет значения, за 500 очков я бы отказалась от массажа от самого Виктора Крама."
    m "Хорошо, ради ставки, я все равно объясню."
    m "Я ожидаю, что ты разденешься, если захочешь, чтобы я массировал тебя дальше."
    her "Голой!"
    m "Только если ты проиграешь."
    her "Ну, я полагаю, что это нормально, ведь мне не придется этого делать."
    m "Ты готова?"
    her "Да, давайте сделаем это быстро. Я должна вернуться в общежитие и переодеться. Моя рубашка мокрая."
    call nar(">Гермиона подходит и стоит перед тобой.") 
    her "Итак, каков ваш план? Вы ожидаете, что я сдамся только потому, что вы будете массажировать мои плечи?"
    m "Плечи? А кто говорил про плечи?"
    her "Вы собираетесь трогать мою задницу?"
    m "Нет, нет. Сегодня мы придерживаемся основ."
    call nar(">Ты хватаешь ее грудь, через пропитанную рубашку.") 
    her "!!!"
    m "Вот так. Я начинаю?"
    her "Что со мной не так?"
    m "Ничего, кроме недооценки старших."
    her "Мои сиськи... Они словно в огне."
    m "Если бы они горели, думаю я бы знал."
    call nar(">Ты аккуратно перекатываешь ее соски между большими и указательными пальцами.") 
    her "!!!"
    her "Пожалуйста, [genie_name], вы должны остановиться!"
    m "Тебе нельзя просить меня, пока не пройдут две минуты!"
    m "А по моим подсчетам еще полторы минуты."
    call nar(">Ты сжимаешь ее грудь.") 
    her "Я отменяю ставку..."
    m "Сейчас, не спеши."
    her "Это не шутка, похоже..."
    her "Это чувство восхитительно..."
    m "Я говорил тебе, что я хорош."
    her "Нет, [genie_name], это лучшее, что я когда-либо ощущала."
    her ""
    
label potion_scene_3_2_2: #Hyper sensitive mouth/throat
    
label potion_scene_3_2_3: #Hyper sensitive pussy
    
    
### HYPNO POTION ###    
    
### FACE NEEDS UPDATE ###
### EYE COLOR NEEDS TO BE CHANGED ###

label potion_scene_3_3_1: #Hypno potion
    m "[hermione_name], сегодня у меня есть для тебя одно зелье."
    call her_main("И где, вы их покупаете?","normal","frown") 
    m "Хороший фокусник никогда не расскрывает своих секретов."
    call her_main("Фокусник? Вы волшебник, и хорошо было бы, чтобы у него не было долгосрочных побочных эффектов.","normal","frown") 
    call her_main("Я до сих пор кашляю меховыми шариками из-за этого оборотного зелья.","normal","frown") 
    m "Этого не повторится, теперь выпей это зелье."
    call her_main("...","annoyed","angryL") 
    call her_chibi("drink_potion","mid","base") 
    with d3
    hide screen hermione_blink
    call nar(">Гермиона начинает осторожно пить зелье.") 
    call her_main("","cum","worriedCl") 
    pause .5
    call her_chibi("stand","mid","base") 
    
    call her_main("Совсем неплохо.","base","squint") 
    call her_main("Я чувствую...","base","happyCl") 
    m "Что ты чувствуешь?"
    call her_main("Я-я чувствую восхи-","annoyed","down") 
    call nar(">Глаза Гермионы пустые, она безучастно смотрит вперед.") 
    call her_main("Что я такое?","grin","dead") 
    m "Хм..."
    m "(Надо что-то придумать. По крайней мере зелье работает. Посмотрим...)"
    menu:
        "-Ты секс бомба-":
            show screen blktone
    #call set_h_hair(hair_style="B",color=2)
    call her_main("Я - секс бомба, которая хочет сделать людей счастливыми...","soft","dead") 
    menu:
        "-Ты любишь быть в моей сперме-":
            pass
    $ hermione_badge = "characters/hermione/accessories/badges/cum_badge.png"
    $ hermione_badges = True
    call her_main("Я люблю быть в вашей сперме...","soft","dead") 
    menu:
        "-Твои сиськи очень любят получать удовольствие-":
            pass
    call her_main("Мои сиськи очень любят получать удовольствие........","soft","dead") 
    pause.5
    
    hide screen blktone
    call nar(">Гермиона закрывает глаза и, кажется, кивает.") 
    call her_main("......","base","closed") 
    call her_main("Где я?","upset","wink") 
    m "Ты в моем кабинете."
    call her_main("Я?","upset","wink") 
    call her_main("Как я сюда попала?","upset","wink") 
    m "Ты пришла сюда несколько минут назад."
    call her_main("Да, я кажется забыла, такая глупышка....","base","squint") 
    call her_main("Итак, профессор, что я здесь делаю?","base","down") 
    call her_main("Ааааааа!!!!","shock","worriedCl",cheeks="blush") 
    call her_main("Что случилось с моей одеждой?!","shock","down_raised") 
    call her_main("Я не могу позволить что бы меня видели в этом!!!","disgust","down") 
    
    if hermione_wear_top:
    
        call set_hermione_action("lift_top") 
        pause.5
    
        $ hermione_wear_top = False
        call set_hermione_action("none","skip_update") 
        pause.5
    
        call her_main("Так намноооого лучше!","soft","ahegao") 
    
    if hermione_wear_bottom:
        call her_main("Это действительно отстооооой, что я должна носить что-нибудь вообще в этом скучном женском монастыре...","annoyed","ahegao") 
        call her_main("(Я могу носить что-нибудь короче. Как юбку...)","") 
        call her_main("(Ооочень короткую!{image=textheart}{image=textheart}{image=textheart})","grin","happyCl") 
    
        call set_hermione_action("lift_bottom") 
        pause.5
    
        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update") 
        pause.5
        
        call her_main("Бьюсь об заклад, вам нравится смотреть, как я раздеваюсь{image=textheart}","smile","glance") 
        
    call her_main("Я не уверена, какое нижнее белье я должна носить...","annoyed","down_raised") 
    call her_main("Определенно что-нибудь розовое!!!","smile","happyCl") 
    hide screen hermione_main
    call blkfade 
    
    call nar("Гермиона вытаскивает палочку и накладывает заклинание...") 
    
    #Setting up Bimbo clothes.
    $ h_hair_color = 2 #Blonde
    $ h_lipstick = "red"
    
    $ h_request_wear_top = True
    $ h_top = "uni_top_5"
    
    $ h_request_wear_bottom = True
    $ h_skirt = "uni_skirt_4_low"
    $ h_skirt_color = "purple"
    
    $ h_request_wear_bra = True
    $ h_bra = "bra_lace"
    $ h_bra_color = "pink"
    
    $ h_request_wear_panties = True
    $ h_panties = "panties_lace"
    $ h_panties_color = "pink"
    
    $ h_request_wear_neckwear = True
    $ h_neckwear = "neck_lace_choker"
    
    $ h_request_wear_stockings = True
    $ h_stockings = "stockings_fishnets"
    
    call load_hermione_clothing_saves 
    call update_her_hair #Always update hair before the uniform! In case she wears cat-ears!
    call update_her_uniform 
    
    pause.5
    call her_main("","base","glance") 
    call hide_blkfade 
    call ctc 
    
    call her_main("Как вам?","grin","happyCl") 
    
    menu:
        g9"!!!"
        "-Ты выглядишь потрясающе!-":
            call her_main("Спасииииибо!!!!{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") 
            call her_main("В любооооом случае....","open","baseL") 
            call her_main("Есть ли что-то, что вы хотите от меня...? Я сделаю все!{image=textheart}","soft","glance") 
        "-Где твой значок шлюхи?!-":
            call her_main("О нет! Я забыла о нем!","soft","wide") 
            call her_main("Извинииите....","shock","worriedCl",cheeks="blush") 
            call her_main("Это он, не правда ли...","soft","down") 
            call nar("Гермиона надевает значок -Я {image=textheart} СПЕРМУ-, который волшебным образом прикрепляется к ее груди.") 
            
            $ h_request_wear_body_accs = True
            $ hermione_body_accs_list = []
            $ hermione_body_accs_list.append("badge_I_love_cum")
            
            call load_hermione_clothing_saves 
            call update_her_uniform 
            
            call her_main("Ура! Вам нравится?","grin","happyCl") 
            call her_main("Что-нибудь еще, что вы хотите? Я сделаю все!{image=textheart}","soft","glance") 
    
    
    m "Я просто хочу задать тебе несколько вопросов."
    call her_main("(...)","annoyed","angry") 
    call her_main("(А я надеялась что мы просто потрахаемся...)","annoyed","angryL") 
    call her_main("(Вопросы такие скучные! Надеюсь, они, по крайней мере, будут пошлые...)","annoyed","ahegao") 
    call her_main("Эти вопросы будут сложными?","grin","worriedCl",emote="05") 
    call her_main("Я не люблю сложные вопросы...","grin","worriedCl") 
    m "Не беспокойся, для тебя они будут легкими."
    call her_main("Ура!","smile","happyCl") 
    m "Во-первых, кто ты?"
    call her_main("Это легко! Я Гермиона Грейнджер, самая красивая девушка во всей школе!","smile","happyCl",emote="06") 
    m "Какие у тебя хобби?"
    call her_main("Я люблю краситься{image=textheart}, Танцевать{image=textheart} и выглядеть счастливой{image=textheart}!","base","happyCl") 
    m "Выглядеть счастливой?"
    call her_main("Вы знаете, если ты счастлив, то ты можешь этим заражать других{image=textheart}","base","ahegao_raised") 
    m "Тебе нравится делать людей счастливыми?"
    call her_main("Разумеется, профессор, когда я делаю людей счастливыми{image=textheart} , это делает счастливой и меня{image=textheart}!","smile","happyCl") 
    call her_main("Как только я закончу школу, я хочу получить работу, где все, что я буду делать - это делать людей счастливыми{image=textheart}!","base","happyCl") 
    m "Хорошо, финальный вопрос."
    m "Как сделать счастливой тебя?"
    call her_main("Сделать меня счастливой?","annoyed","down") 
    call her_main("Но я уже счастлива, глупый!","base","happyCl") 
    m "Даже больше, чем обычно."
    call her_main("Больше? {size=+10}УАУ!{/size}","smile","happyCl",emote="06") 
    call her_main("Так как мне стать счастливой? Мне нужно раздеться?","grin","baseL") 
    m "Это будет неплохое начало."
    call her_main("{image=textheart}ЗЗЗДДДОООРРРОООВВВООО!!!{image=textheart}","grin","ahegao") 
    
    call set_hermione_action("lift_top") 
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") 
    pause.5
    
    call her_main("Вы знали, что правила не позволяют ходить нам голыми в школе?","annoyed","angryL") 
    m "Правда? Я не могу представить почему нельзя."
    call her_main("Вы согласны? Это так глупо! Все будут просто счастливее{image=textheart} если люди будут ходить голыми.","soft","ahegao") 
    
    call set_hermione_action("lift_skirt") 
    pause.5
    
    $ hermione_wear_bottom = False
    $ hermione_wear_panties = False
    call set_hermione_action("none","skip_update") 
    pause.5
    
    call her_main("Я знаю, что все, кто видит меня обнаженной, счастливы!","base","glance") 
    m "Ты, конечно, делаешь меня счастливым."
    call her_main("Спасибо, профессор! Это меня так радует{image=textheart}!","grin","worriedCl") 
    m "(Я не думаю, что могу выдержать больше...)"
    m "Теперь, Гермиона, я хочу, чтобы ты трогала свою грудь."
    call nar(">Гермиона поднимает руки к груди.") 
    call set_hermione_action("lift_breasts") 

    call her_main("Вот так? Я чувствую себя ооочень хорошо.","base","down") 
    call her_main("Мне кажется что мои руки двигаются самостоятельно.","soft","ahegao") 
    call her_main("Мне так хорошо, но это странно...Мне нужно что-то... что угодно...","open","worriedCl") 
    m "Хочешь потрогать себя, там, внизу?"
    call her_main("Да, [genie_name]. Пожалуйста.","shock","worriedCl") 
    
    menu:
        "-Заставить ее умолять-":
            m "Я хочу, что бы ты."
            call her_main("Пожалуйста, сэр...","shock","worriedCl") 
            m "Что пожалуйста?"
            call her_main("Пожалуйста, позвольте мне коснуться себя там...Я сделаю все...","clench","worried",cheeks="blush",tears="soft") 
            m "Что угодно?"
            call her_main("Да, я просто хочу быть счастливой...","silly","worried",cheeks="blush",tears="soft") 
            m "Скажи мне, кто ты, и я позволю тебе."
            call her_main("Я Гермиона, главная шлюха этой прекрасной школы.","grin","ahegao") 
            m "Еще."
            call her_main("Блин, Я маленькая и развратно доверчивая глупышка, которая просто хочет чувствовать себя счастливой...","silly","ahegao") 
            m "И что делает тебя счастливой?"
            call her_main("Я счастлива когда вы счастливы{image=textheart}, [genie_name].","silly","dead") 
            m "Хорошая девочка."
        "-Дай ей потрогать себя.-":
            m "Продолжай."
            call her_main("Спасибо, я ооооочень{image=textheart} благодарна, [genie_name]!","silly","ahegao") 
            
    call set_hermione_action("covering") 
    call her_main("Мне тааак хорошо.","grin","ahegao") 
    call her_main("[genie_name], пожалуйста, сделайте что-нибудь для меня.","grin","wink",cheeks="blush") 
    m "Например?"
    call her_main("Если это вас не затруднит...","silly","ahegao") 
    call nar(">Гермиона начинает щипать свой сосок.") 
    call set_hermione_action("pinch") 
    call her_main("Пожалуйста, вы можете обкончать меня?","open_tongue","ahegao_raised",cheeks="blush") 
    m "Если это сделает тебя счастливой."
    call nar(">Ты встаешь и направляешься к ней.") 
    call her_main("Спасибо, спасибо вам! Вы самый лучший директор! {size=+5}ВСЕГДА!{/size}","smile","happyCl",emote="06") 
    
    hide screen hermione_main
    call blkfade 
    
    hide screen genie
    call gen_chibi("jerking_off","desk","base") 
    show screen chair_left
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade 
    call ctc 
    
    call set_hermione_action("covering") 
    call her_main("...","base","ahegao_raised") 
    call set_hermione_action("pinch") 
    call her_main("Я не знаю, как это делают другие девушки...","annoyed","down") 
    m "Делают что?"
    call her_main("Останавливают себя от возможности полакомиться вашей вкусной спермой.","annoyed","down") 
    call set_hermione_action("covering") 
    call her_main("Я имею в виду, что я едва могу остановить себя, приходя сюда каждый день!","smile","happyCl") 
    m "Это..."
    call set_hermione_action("pinch") 
    call her_main("Хм, мне просто нравится играть с сиськами{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised") 
    call her_main("Они такие мягкие...","open","ahegao_raised",cheeks="blush") 
    call set_hermione_action("covering") 
    call her_main("Я чувствую себя так хорошо. Вы такой чут-","base","ahegao_raised",cheeks="blush") 
    call her_main("Чут-.","base","ahegao_raised",cheeks="blush") 
    call set_hermione_action("pinch") 
    call her_main("Какое слово?","annoyed","ahegao_raised",cheeks="blush") 
    m "Чуткий."
    call set_hermione_action("covering") 
    call her_main("Правильно, вы очень чуткий!","silly","ahegao_raised",cheeks="blush") 
    m "Я..."
    call her_main("Вы уже кончаете?","open_tongue","ahegao_raised",cheeks="blush") 
    call set_hermione_action("pinch") 
    call her_main("Пожалуйста, сделайте это мне на лицо!","open_tongue","ahegao_raised",cheeks="blush") 
    call her_main("Или на мои сиськи!","scream","worriedCl",cheeks="blush") 
    call set_hermione_action("covering") 
    call her_main("Или на мое лицо!","silly","ahegao_raised",cheeks="blush") 
    
    menu:
        "-Кончить ей на лицо-":
            g4 "Я уже близко, сучка!"
            call her_main("{image=textheart}!!!{image=textheart}","shock","wide",cheeks="blush") 
            call gen_chibi("cumming","desk","base") 
            $ u_sperm = "characters/hermione/face/auto_07.png"
            $ uni_sperm = True
            g4 "Вот так, все на твоем лице."
            call set_hermione_action("pinch") 
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") 
        "-Кончить на сиськи-":
            g4 "Великий потоп, надвигается fuckbunny!(непереводимо - слэнг)"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush") 
            call gen_chibi("cumming","desk","base") 
            $ u_sperm = "characters/hermione/face/auto_02.png"
            $ uni_sperm = True
            g4 "Все на твоих сиськах."
            call set_hermione_action("pinch") 
            call her_main("Так тепло...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") 
        "-Обкончать ее всю-":
            g4 "Готовься шлюха!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush") 
            call gen_chibi("cumming","desk","base") 
            $ u_sperm = "characters/hermione/face/auto_05.png"
            $ uni_sperm = True
            g4 "Какая хорошая шлюха, все для тебя."
            call set_hermione_action("pinch") 
            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") 
    
    call gen_chibi("hold_dick","desk","base") 
    call her_main("...","grin","ahegao") 
    $ hermione_dribble = True
    call her_main("Это чувство {size=+5}ТАКООООЕ!{/size} приятное!","silly","ahegao") 
    call set_hermione_action("lift_breasts") 
    
    call her_main("Можем ли мы сделать это снова?! Пожалуйста! Умоляю! Залейте меня своей спермой!","silly","dead") 
    m "Не сегодня."
    call her_main("Уууух.","shock","worriedCl") 
    
    hide screen hermione_main
    call blkfade 
    
    call gen_chibi("hide") 
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") 
    call hide_blkfade 
    
    call her_main("Ну ладно.... Наверное, я пойду в класс.","open","down") 
    m "Ах да. Я думаю, было бы лучше, если бы ты вернулась в свое общежитие."
    call her_main("Почему, [genie_name]?","annoyed","base") 
    m "Я думаю, тебе нужно немного поспать, чтобы эффект прошел."
    call her_main("Все, как вы скажите, сэр!","annoyed","closed") 
    call set_hermione_action("none","skip_update") 
    call her_main("Спасибо еще раз{image=textheart} Вы лучший!","smile","happyCl",emote="06") 

    call her_walk("desk","leave",2.5) 
    
    m "(Может, мне стоило сначала сказать ей одеться...)"
    
    $ reward_her_red_lipstick = True #Unlocks red lipstick
    call give_reward(">Теперь Гермиона можеть пользоваться красной помадой.","images/store/lipstick.png") #Need lipstick shop image!
    
    call reset_hermione_main 
    
    $ hermione_takes_classes = True
    call music_block 
    jump day_main_menu
      

### AHEGAO POTION ###

label potion_scene_3_4_1: 
    m "Сколько еще осталось до твоего урока, [hermione_name]?"
    call her_main("Около пятнадцати минут, сэр.","open","base") 
    m "В этом случае я думаю, тебе, возможно, придется немного опоздать."
    call her_main("Что? Почему?","open","worried") 
    g4 "Ну, наверное, тебе будет немного сложно посещать занятия, когда мой член будет находиться в твоей маленькой киске."
    call her_main("Ох...","soft","squintL") 
    m "Это для тебя не проблема, [hermione_name]?"
    call her_main("Конечно нет, [genie_name]! Позвольте мне просто снять одежду.","grin","ahegao") 

    show screen blkfade
    with d3
    hide screen bld1
    hide screen hermione_blink
    #SEX
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("Ахххххххх....{image=textheart}","scream","wide") 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ ccg_folder = "herm_sex"
    $ ccg1 = "blank"
    $ ccg3 = "blank"
    $ ccg2 = 1
    show screen ccg
    hide screen blkfade
    with d3
    her "Ах...{image=textheart}"
    g4 "Мммм, тебе нравится, что ты шлюха?"
    $ ccg2 = 2
    her "Да...{image=textheart}"
    $ ccg2 = 3
    her "Я пропущу этот урок..."
    $ ccg2 = 4
    her "Мне все равно...{image=textheart}"
    $ ccg2 = 5
    her "Я чувствую себя так хорошо...."
    pause
    ">Ты спокойно вытаскиваешь маленький флакон из кармана и открываешь пробку."
    $ ccg2 = 6
    her "Мммм, не тормозите, [genie_name]..."
    g4 "Ты сама это просила!"
    ">Ты ускоряешь темп, чтобы кончить на ее задницу, твоим рукам едва получается оставаться на месте..."
    $ ccg2 = 7
    her "Жестче!!! [genie_name]!!!"
    pause
    ">Ты чувствуешь, что Гермиона внезапно подталкивает свою киску к тебе, заставляя тебя пролить немного зелья из флакона на ее попку..."
    $ ccg3 = "p1"
    m "..."
    $ ccg2 = 8
    her "Что это было?"
    m "Ух... ничего... просто немного расплескалось. Продолжай подмахивать блядина."
    $ ccg2 = 9
    her "Ах...{image=textheart}..."
    ">Ты быстро закрываешь флакон и кладешь его обратно в свою мантию."
    $ ccg2 = 10
    her "Ах... ах... ах..."
    pause
    $ ccg2 = 11
    her "[genie_name], вы думаете, что можете... ах..."
    g4 "Что?"
    $ ccg2 = 12
    her "Не могли бы вы... Отшлепать меня... Ах...?"
    g4 "Конечно!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">Ты прохаживаешь ее задницу тяжелыми шлепками, случайно проливая зелье, которое покрывает ее еще больше."
    $ ccg3 = "p2"
    $ ccg2 = 13
    pause
    her "{size=+10}!!!{/size}"
    ">Мокрая киска Гермионы начинает безумно сокращаться и сжимать твой член."
    g4 "Ммм, уже кончаешь, шлюха?"
    $ ccg2 = 14
    her "Д-да...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 15
    her "Я{image=textheart} не могу{image=textheart} остановиться..........{image=textheart}{image=textheart}{image=textheart}"
    ">Честное слово, ты не чувствуешь конца ее безжалостным спазмам."
    g4 "Я люблю когда сперма на моей шлюхе."
    $ ccg2 = 16
    pause
    her "Нет...{image=textheart} сэр...{image=textheart} вы...{image=textheart} не можете...{image=textheart} понять...{image=textheart}"
    $ ccg2 = 17
    her "Это...{image=textheart} все...{image=textheart} не останавливается...{image=textheart}"
    g4 "Я не думаю что это моя проблема!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">Ты даете по ее заднице еще один мощный шлепок, предвкушая ощущения оргазма."
    $ ccg2 = 18
    her "{size=+10}!!!{/size}"
    $ ccg2 = 19
    her "Это......{image=textheart} {image=textheart} "
    $ ccg2 = 20
    pause
    her "Все{image=textheart}  мое{image=textheart}  тело...{image=textheart}{image=textheart}{image=textheart} "
    g4 "Говори, шлюха!"
    $ ccg2 = 21
    her "Мое тело....{image=textheart} {image=textheart} в огне..."
    $ ccg2 = 22
    her "Я не знаю...{image=textheart}"
    $ ccg2 = 23
    her "Почему...{image=textheart}"
    $ ccg2 = 24
    her "Почему {image=textheart}это {image=textheart}дает {image=textheart}чувство {image=textheart}такого {image=textheart}удовольствия.....{image=textheart}{image=textheart}{image=textheart}"
    g4 "Наслаждаешься?"
    $ ccg2 = 25
    her "Нет...{image=textheart} ах.. даа....{image=textheart}"
    $ ccg2 = 26
    her "Это как...{image=textheart}"
    $ ccg2 = 27
    her "Каждый раз, когда вы суете...{image=textheart}{image=textheart} этот большой {image=textheart}член{image=textheart} в меня...{image=textheart}"
    $ ccg2 = 28
    pause
    her "Я {image=textheart} безумно{image=textheart}{image=textheart}кончаю{image=textheart}{image=textheart}..."
    her "Но это никак не заканчивается..."
    $ ccg2 = 29
    her "Каждый раз это все больший {image=textheart}оргазм{image=textheart}..."
    $ ccg2 = 30
    her "{size=+10}И{image=textheart} ЭТО{image=textheart} НЕ{image=textheart} КОНЧ{image=textheart}АЕТСЯ!!!!!"
    g4 "Звучит неплохо... Как насчет того, что бы я надавал твоей большой заднице еще шлепков?"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">Ты шлепаешь ее по заднице, держишь ее теплую плоть и подливаешь зелье."
    $ ccg2 = 31
    her "{size=+20}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}"
    $ ccg2 = 32
    her "{image=textheart}мой{image=textheart} {image=textheart}мозг...{image=textheart}"
    $ ccg2 = 33
    her "Вы{image=textheart} собираетесь{image=textheart} меня{image=textheart} убить{image=textheart} ???...{image=textheart}"
    g4 "Не переоценивай ситуацию."
    pause
    $ ccg2 = 34
    her "Я не...{image=textheart}"
    her "Ах.....{image=textheart} некоторые....{image=textheart} вещи....{image=textheart} очень....{image=textheart} неправильны.{image=textheart}"
    ">Слова Гермионы начинают замедляться, в конце концов, она в состоянии только пробормотать писк, когда ты входишь в ее."
    g4 "Может быть, это было зелье, которое я налил тебе на задницу?"
    $ ccg2 = 35
    her "{size=+20}{image=textheart}{image=textheart}Что?{image=textheart}{image=textheart}{/size}"
    g4 "Не волнуйся, эффект должнен пройти примерно через час..."
    $ ccg2 = 36
    her "{size=+20}!!!!!!!{/size}"
    g4 "Между тем, почему бы тебе просто не расслабиться и насладиться сексом."
    $ ccg2 = 37
    her "{image=textheart}на-сла-ди-ться...{image=textheart}"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    $ ccg2 = 38
    pause
    her "{size=+20}!!!!!!!{/size}"
    $ ccg2 = 39
    her "Пожалууууйста...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 40
    her "Мой...{image=textheart}разум...{image=textheart}он...{image=textheart}разрывается..{image=textheart}"
    ">Ты начинаешь набирать темп, рассматривая ее как не что иное, как мяукающею свежую плоть..."
    g4 "MMMM, ты всегда знаешь, что сказать, чтобы заставить меня кончить!!"
    $ ccg2 = 41
    her "...{image=textheart}{image=textheart}{image=textheart}"
    ">В конце концов ее киска настолько сильно запульсировала, что ты не можешь противиться."
    g4 "Аххх! Я уже все, шлюха!"
    $ ccg2 = 42
    pause
    her "{image=textheart}........{image=textheart}"
    ">Ты начинаешь изливаться спермой прямо в ее вульву."
    $ ccg3 = "s4"
    $ ccg2 = 43
    pause
    her "{image=textheart}!!!{image=textheart}"
    g4 "ПОЛУЧАЙ!!!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">Ты шлепаешь ее задницу в последний раз."
    $ ccg3 = "s5"
    $ ccg2 = 44
    pause
    her "{image=textheart}........{image=textheart}"
    her "{image=textheart}...............{image=textheart}"
    $ ccg2 = 45
    pause
    her "{image=textheart}.......................{image=textheart}"
    show screen blkfade
    with d3
    ">Глаза Гермионы закатываются и она падает на твой стол."
    ">Ты несешь бессознательное тело в ее комнату."
    hide screen ccg
    hide screen hermione_main
    hide screen hermione_blink
    show screen genie
    hide screen blkfade
    with d3
    
    $ hermione_takes_classes = True
    call music_block
    jump day_main_menu