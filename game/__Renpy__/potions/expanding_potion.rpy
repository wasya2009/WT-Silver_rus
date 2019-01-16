

### BREAST AND ASS EXPANSION ###

label potion_scene_2_1_1: #breast expansion - Until chibis are added for it tifucking won't be written (ayylmao)
    m "Угадай, что сегодня у меня для тебя есть."
    call her_main("Еще одно гадкое зелье, которое попытается превратить меня в отвратительное животное?","open","angryCl") 
    m "Ну, я думаю, оно хотя бы приятно пахнет."
    call her_main("Оно вкусное?","open","base") 
    m "Есть только один способ выяснить."
    call nar(">Ты передаешь ей зелье и она подносит его к носу.") 
    call her_main("Ну, вы правы, пахнет хорошо. Давайте выясним, хорошо ли оно на вкус...","base","base") 
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Она неторопливо пьет зелье.") 
    call her_main("Аххх.","base","happyCl") 
    call her_main("","smile","glance") 
    call her_chibi("stand","mid","base") 
    
    her "Это было не так уж плохо."
    call her_main("Итак, теперь, когда я испытала зелье, вы скажите мне, что оно должно делать.","angry","wink") 
    m "Не нужно портить веселье, оно должно вступить в силу относительно быстро."
    call her_main("И что же мне делать до этого момента?","base","glance") 
    m "Ты можешь показать мне свои сиськи."
    call her_main("Я так не думаю, [genie_name]. Вы платите мне только за то, что я пью зелья.","open","closed") 
    call her_main("Если вы надеетесь увидеть меня без рубашки, вам придется постараться.","base","suspicious") 
    m "О, я бы не был так уверен в этом."
    call her_main("Так что делает это зелье? Заставляет меня показать вам мою грудь? Это что-то вроде зелья контроля над разумом?","base","base") 
    m "Контроль разума? И что в этом интересного? Нет, это что-то гораздо более веселое."
    call her_main("Ну, лучше бы это произошло поскорее, иначе я уй-","annoyed","angryL") 
    call nar(">Ты замечаешь что ее грудь начала слегка увеличиваться.") #Start using facial expressions mixed with Captain Nemo art
    call her_main("...","annoyed","annoyed") 
    call her_main("Как я уже сказала, лучше бы это произошло поскорее, иначе я уйду.","annoyed","worriedL") 
    m "Я бы не беспокоился об этом, судя по всему, уже началось."
    call her_main("Чего..? Что со мной не так?","open","base") 
    m "С тобой все в порядке. Во всяком случае, это улучшение."
    call her_main("Что?","annoyed","annoyed") 
    call nar(">Она начала щупать свое тело, проверяя, нет ли у нее новых ушей или хвоста.") 
    call her_main("Я не вижу, что вы...","open","down") 
    call nar(">Она хватает свою грудь, чтобы проверить ее.") 
    call her_main("!!!","angry","down_raised") 
    call her_main("Моя грудь стала больше?","angry","wide") 
    m "Ты вовремя заметила."
    call her_main("Зачем вы делаете мою грудь больше? Она уже достаточно большая!","angry","base") 
    m "Ты знаешь, как говорят, хорошего много не бывает."
    call her_main("Все совсем наоборот [genie_name].","annoyed","annoyed") 
    m "Правда? Ну, я предпочитаю свою версию."
    call her_main("Ну, насколько большими они должны-","angry","down_raised") 
    call nar(">Ее грудь снова раздувается.") 
    call her_main("Вы же не серьезно? Такими темпами она порвет мне рубашку.","angry","wide") 
    m "Ну, они должны остановиться на этом."
    call her_main("Хорошо, они и так достаточно большие.","angry","angry") 
    
    menu:
        "-Отправить ее в класс-":
            m "Вы правы, я полагаю, они достаточно большие."
            m "Ну, это все на сегодня, 20 очков Гриффиндору."
            call her_main("Это все? Вы не собираетесь сделать еще что-нибудь?","shock","wide") 
            m "Я не должен. Я попросил тебя выпить зелье и ты выпила его. Ты свободно можешь идти."
            call her_main("Спасибо вам [genie_name], я вернусь в свою комнату.","smile","baseL") 
            m "Комнату? Наступило время занятий [hermione_name]. Как ты думаешь, что скажет профессор Снейп, когда услышит, что ты пропустила урок?"
            call her_main("Я не могу пойти в таком виде.","disgust","glance") 
            m "Почему нет? Все же скрыто."
            call her_main("Едва. И что люди обо мне подумают.","angry","down_raised") 
            m "Просто скажите им, что ты все еще растешь. Я уверен, что они все ровно привыкли к огромным грудям, вроде нескольких дополнительных размеров."
            call her_main("...Хорошо. Просто пообещайте мне, что они не станут больше.","upset","closed") 
            m "Я не могу обещать, ты все еще учишься в школе. Многие девочки не перестают расти до 30 лет."
            call her_main("Вы знаете что я имею в виду [genie_name].","scream","angry",emote="01") 
            m "Боюсь что нет [hermione_name], тебе лучше поторопиться, если не хочешь опоздать."
            call her_main("...Да [genie_name].","annoyed","annoyed") 
            
            hide screen hermione_main
            hide screen blktone
            hide screen bld1
            with d3
            
            call her_walk("mid","leave",2) 
            
            $ hermione_takes_classes = True
            
            call h_action("expand_breasts") 
            
            jump day_main_menu
            
        "-Играть с ее грудью-":
            pass
            
    m "Ну, это спорный вопрос."
    m "Теперь, как бы ты хотела заработать дополнительные очки?"
    call her_main("Я хочу еще 40.","annoyed","annoyed") 
    m "Я даже не сказал тебе, чего я хочу-"
    call her_main("Если вы хотите прикоснуться к моей груди, это будет стоить дополнительные 40 очков.","annoyed","angryL") 
    m "По рукам."
    
    call her_walk_desk_blkfade 
    
    call nar(">Гермиона подходит к твоему столу, ее грудь ритмично качается, когда она движется.") 
    pause .8
    
    hide screen hermione_main
    call h_action("lift_top") 
    call her_chibi("hide") 
    hide screen genie
    show screen groping_naked_tits
    call hide_blkfade 
    
    call her_main("Ну...","upset","wink",xpos="mid",ypos="base") 
    call nar(">Ты протягиваешь руку и хватаешь ее грудь через растянутую рубашку.") 
    call her_main("!!!","angry","wide") 
    call her_main("Пожалуйста, полегче [genie_name]. Они гораздо, более чувствительные чем обычно, это должно быть из-за зелья.","angry","base") 
    m "Хорошо, я приму это во внимание..."
    call nar(">Ты берешь грудь в каждую руку и начинаешь массировать пальцами.") 
    call her_main("...","open","closed") 
    m "Они, конечно, намного больше, чем обычно."
    call her_main("...да","soft","ahegao") 
    call nar(">Ты продолжаешь нежно массировать грудь через рубашку. Разминая их, а затем прижимая друг к другу.") 
    call her_main("...Такое чувство, что они увеличив-","angry","down_raised") 
    call ctc 
    
    call h_action("expand_breasts") 
    with vpunch
    
    call her_main("!!!","angry","wide") 
    call her_main("Вы сказали что они не станут больше! Как вы это объясните?!","scream","angry",emote="01") 
    m "Не переживай об этом, [hermione_name], беспокойся о заработке 40 очков"
    call her_main("Просто поторопитесь","annoyed","annoyed") 
    menu: #Will add titfuck here
        #"-Сосать ее соски-":
            #"asd"
        "-Трахнуть сиськи-":
            m "Ну, подойди сюда!"
            hide screen hermione_main
            call blkfade 
            
            hide screen groping_naked_tits
            jump start_titfuck
        "-Играть с ее сосками-":
            pass
            
    call nar(">Ты берешь ее обнаженную грудь обратно в руки и продолжаешь массировать") 
    
    call her_main("Сэр... кажется, они стали более чувствительными...","base","ahegao_raised") 
    call her_main("Пожалуйста, не делайте ничего резкого.","soft","ahegao") 
    m "Вот так?"
    call nar(">Ты берешь оба соска между большим и указательным пальцами.") 
    call her_main("!!!","scream","wide") 
    call her_main("Пожалуйста, остановитесь... слишком сильно, будто мои соски горят.","shock","worriedCl") 
    m "Шшшш, просто успокойся, все скоро закончится."
    call nar(">Ты начинаешь катать ее соски между пальцами.") 
    call her_main("...","open","worriedCl") 
    call nar(">Ты чувствуешь как она касается своей промежностью твоего бедра.") 
    m "Чувствуешь себя немного возбужденно?"
    call nar(">Ты начинаешь щипать и тянуть ее соски.") 
    call her_main("Оххх...","soft","ahegao") 
    call nar(">Она начинает тереться о твое бедро.") 
    m "Так, так... ты теперь очень чувствительна, не так ли? Пытаешься достигнуть оргазма о ногу директора, какое бесстыдство."
    call her_main("...","grin","dead") 
    m "Давай посмотрим, можем ли мы что-то с этим сделать."
    call nar(">Ты начинаешь попеременно щипать и сильно тянуть ее соски насколько можешь, а затем толкать их обратно в грудь.") 
    call her_main("!!!","scream","wide") 
    her "Я-Я-Я кончаю!"
    call nar(">Когда на ее юбке начинает формироваться мокрое пятно, она начинает сильно тереться о твою ногу.") 
    m "Какая шалунья."
    call nar(">Она тяжело дышит, упираясь в тебя") 
    
    call blkfade 
    pause 1
    hide screen hermione_main
    hide screen chair_left
    hide screen desk
    hide screen groping_naked_tits
    hide screen blktone 
    call her_chibi("stand","desk","base") 
    show screen genie
    hide screen bld1
    hide screen blktone
    call hide_blkfade 
    pause.5
    
    show screen bld1
    call her_main("И... это все [genie_name]?","soft","ahegao") 
    m "Да, [hermione_name]. Теперь ты можешь идти."
    pause.2
    
    call her_walk("desk","leave",2) 
    
    $ hermione_takes_classes = True
    jump day_main_menu


label potion_scene_2_1_2: #Hermione comes back after having her breasts expand in class



label potion_scene_2_2: #ass expansion
    m "[hermione_name], сегодня у меня есть еще одно зелье для тебя."
    call her_main("Еще одно? Где вы их достаете?","open","suspicious") 
    m "Это тебя не касается. Что должно тебя касаться, так это 20 очков, которые ты можешь заработать, если выпьешь это."
    call her_main("...Хорошо, дайте мне бутылочку.","normal","frown") 
    call nar(">Она недоумевая берет бутылек.") 
    call her_main("По крайней мере оно хорошо пахнет.","base","base") 
    
    call her_chibi("drink_potion","mid","base") 
    pause 2

    call nar(">Она выпивает все зелье несколькими глотками.") 
    
    call her_chibi("stand","mid","base") 
    pause.5
    
    call her_main("Аххх, это было хорошо! Так что это?","grin","worriedCl",emote="05") 
    m "Эффект мы увидим достаточно скоро."
    call her_main("Можете хотя бы намекнуть?","open","base") 
    m "Скажем так, оно меняет размер твоей задницы" ###Added {w} instead of your ...
    call her_main("Что вы имеете в виду--","annoyed","angryL") 
    call nar(">Гермиона побледнела, когда начала ощущать, как ее тело изменяется.") 
    call her_main("Что происходит. Такое чувство будто что-то движется внутри меня.","angry","wide") 
    call her_main("Моя попа, чувство такое... приятное.","soft","ahegao") 
    call nar(">Ты замечаешь, как ее задница увеличивается в размерах.") #Use bigger butt from Captain Nemo
    call her_main("Я стала очень чувствительной... Я должна снять с себя юбку","angry","wide") #changed so to too
    
    $ hermione_wear_panties = False
    call set_hermione_action("lift_skirt") 
    pause.5
    
    $ hermione_wear_bottom = False
    call set_hermione_action("none","skip_update") 
    
    call her_main("","silly","ahegao_intense",cheeks="blush") 
    pause.8
    
    call her_main("","soft","wide") 
    call ctc 
    
    call her_main("Что-то происходит с моим телом, [genie_name]!","open","down_raised") 
    call ctc 
    
    call set_hermione_action("expand_ass") 
    with vpunch
    
    call her_main("","angry","down_raised") 
    call ctc 
    
    
    call her_main("Угххх, моя задница стала больше!","angry","down_raised") 
    call her_main("Это то, что должно делать это зелье? Увеличивать мой зад?","upset","closed") 
    m "Несомненно"
    call her_main("Почему моей заднице так хорошо?","soft","ahegao") #new
    call nar(">Гермиона поглаживает свою попку, скользя пальцами по расширенным ягодицам.") 
    m "Хммм, этого не должно было произойти, но я думаю, что каждый случай уникален."
    call her_main("Это так чувственно... [genie_name] как думаете, вы могли бы... помассировать меня?","grin","dead") 
    m "Ну, я вряд ли смогу отказать тебе."
    hide screen hermione_main
    hide screen bld1
    with d3
    
    call her_walk_desk_blkfade 
    
    call nar(">Гермиона подходит к твоему столу, ее задница колыхается, при движении, и предстает перед тобой.") 
    pause 1
    show screen chair_left
    hide screen genie
    show screen no_groping_02
    call hide_blkfade 
    call ctc 
    
    show screen bld1
    show screen blktone
    call her_main("Пожалуйста [genie_name]... пожалуйста, воспользуйтесь мной...","open","worriedCl",xpos="mid",ypos="base") 
    m "Как скажешь."
    call nar(">Ты берешь ее набухшие ягодицы в свои руки. Каждая из них теперь намного больше, чем раньше.") 
    hide screen no_groping_02
    show screen groping_02
    with d3
    m "Это зелье, безусловно, эффективно."
    call nar(">Ты начинаешь сильно гладить ее ягодицы. Раздвигая их, чтобы увидеть дырочку, а затем хлопать ими.","start") 
    call nar(">Увидев ее тугую дырку, у тебя появляется идея.","end") 
    $ hermione_main_zorder = 8
    
    menu: #Thought about adding a rimming option here but the chibis don't really support it
        "-Сунуть палец-":
            call nar(">Ты снова открываешь ягодицы, чтобы увидеть ее сморщенную дырочку.") 
            m "Посмотрим, насколько ты на самом деле чувствительна."
            call nar(">Ты начинаешь дразнить вход пальцем, медленно гладя его.") 
            call her_main("!!!","shock","worriedCl") 
            call her_main("[genie_name] пожалуйста... Я слишком чувствительна. Если вы это сделаете, \nЯ не уверена, что смогу сдержать себя.","soft","ahegao") 
            hide screen hermione_main
            m "В таком случае..."
            call nar(">Ты медленно отрываешь палец от ее задницы.") 
            call her_main("Спасибо бо-","soft","ahegao") 
            call nar(">А затем резко вставляешь его.") 
            call her_main("...","angry","wide") 
            her "..."
            her "..."
            call her_main("{size=-10}Я кончаю.{/size}","scream","wide") 
            hide screen hermione_main
            m "Что это было?"
            call nar(">Ты начинаешь вращать палец.") 
            call her_main("{size=+10}Я кончаю!{/size}","scream","worriedCl") 
            call nar(">Ее задница начинает пульсировать вокруг твоего пальца.") 
            hide screen hermione_main
            m "Какая маленькая анальная шлюшка. Интересно, что ты сделаешь, когда я попробую это."
            call nar(">Ты начинаешь двигать пальцем в ее дрожащей попе.") 
            call her_main("!!!","shock","worriedCl") 
            call her_main("Я снова кончаю!","open","worriedCl") 
            m "Так быстро?"
            call her_main("Я не могу остановиться! Пожалуйста [genie_name], пожалуйста, прекратите!","angry","wide") 
            
            menu:
                "-Остановиться-":
                    m "Ну, полагаю, на сегодня достаточно...."
                    call nar(">Ты вытаскиваешь палец из ее задницы, и она сразу же падает на твой стол.") 
                    call her_main("Это было... замечательно...","grin","dead") 
                    call nar(">Она лежит на твоем столе, тяжело дыша.") 
                "-Продолжить-":
                    m "Что это было [hermione_name]? Готов поклясться,  что слышал будто ты попросила меня остановиться."     ###Или было бы лучше, если бы она начала плакать и слегка вопить?
                    call nar(">Ты увеличиваешь темп.") 
                    call her_main("Пожалуйста...","open","worriedCl") 
                    m "Что пожалуйста?"
                    call nar(">Ты вставляешь второй палец.") 
                    call her_main("Пожалуйста... остановитесь... вы мне  все разорвете...","angry","down_raised") 
                    call nar(">Одной рукой ты хватаешь ее за бедро и продолжаешь трахать пальцем попу.") 
                    call her_main("...","shock","worriedCl") 
                    call her_main("...","scream","worriedCl") 
                    call nar(">Ты чувствуешь что ее тело стало мокрым, а дырочка неустанно пульсирует вокруг твоих пальцев.") 
                    m "Разве это не приятно?"
                    call nar(">Ты замедляешься и вытаскиваешь палец из ее попки") 
                    call her_main("...дааааа...[genie_name]...","grin","dead") 
                    m "Хорошая девочка."
                    
            m "Ну, тебе лучше отправиться в класс."
            call her_main("...С такой задницей?","angry","down_raised") 
            m "Я уверен никто ничего не скажет \nведь твоя юбка на тебе. А теперь поторопись \nу меня есть дела."
            $ hermione_main_zorder = 5
            call blkfade 
            pause 1
            
            hide screen bld1
            hide screen chair_left
            hide screen groping_01
            hide screen groping_02
            call her_chibi("stand","desk","base") 
            show screen genie
            hide screen blktone
            hide screen bld1
            call hide_blkfade 
            pause.5
            
            show screen bld1
            call her_main("Да [genie_name].","base","down") 
            m "Ох, чуть не забыл, 20 очков Гриффиндору!"
            $ gryffindor += 20
            call her_main("Ох... верно, очки. Спасибо.","grin","dead") 
            call nar(">Гермиона поднимает свою юбку и пытается надеть. Ее задница настолько огромна, что юбка едва скрывает половину.") 
            $ custom_skirt = 0
            $ h_action_show_skirt = True
            call her_main("...","open","down") 
            
        "-Хотдог-" if whoring >= 17:
            m "Наклонись [hermione_name]."
            call nar(">Прежде чем она успевает среагировать, ты толкаешь ее вперед на свой стол.") 
            hide screen groping_02
            show screen ch_hotdog
            with d3
            call her_main("!!!","angry","wide") 
            call her_main("Что вы собираетесь делать [genie_name]?","angry","wink") 
            hide screen hermione_main
            m "Ну, видя как твоя задница стала такой чертовски огромной, я подумал что смогу найти ей хорошее применение."
            call nar(">Ты достаешь член из штанов и кладешь его поверх ее задницы.") 
            call her_main("Вы же не собираетесь трахать меня в задницу [genie_name]?","grin","dead") 
            hide screen hermione_main
            m "Не твою дырочку, [hermione_name], я собираюсь трахнуть твои ягодички!"
            call nar(">Ты крепко хватаешь ее ягодицы и раздвигаешь их, позволяя своему стволу упасть между ними, поверх ее дырочки.") 
            m "Идеально подходит, не так ли?"
            call her_main("Что вы-","angry","base") 
            hide screen hermione_main
            call nar(">Ты сжимаешь ее ягодицы около своего члена, который начинает твердеть между ними.") 
            call her_main("!!!","grin","ahegao") 
            hide screen hermione_main
            m "Черт, твоя задница такая мягкая. Это как трахать подушку."
            call her_main("Аххх...","silly","worried",cheeks="blush",tears="soft") 
            call her_main("Пожалуйста, [genie_name]...","silly","ahegao") 
            hide screen hermione_main
            m "Угххх, это так хорошо, возможно нам придется делать это постоянно."
            call her_main("Постоянно?","shock","baseL",cheeks="blush",tears="soft") 
            hide screen hermione_main
            m "Ты ведь, не возражаешь?"
            m "Каждый день иметь твою задницу как секс-игрушку."
            call her_main("...","angry","suspicious",cheeks="blush") 
            hide screen hermione_main
            m "Я задал тебе вопрос, [hermione_name]."
            call her_main("... нет [genie_name]...","silly","dead") 
            hide screen hermione_main
            call nar(">Ты чувствуешь, как ее дырка начинает пульсировать, когда ты скользишь мимо нее.") 
            m "Конечно ты бы не отказала, ты наслаждаешься этим больше, чем я, не так ли?"
            call her_main("...да... я люблю... когда вы используете мою задницу как свою игрушку...","silly","ahegao") 
            hide screen hermione_main
            m "Вот так, девочка, сейчас я..."
            call nar(">Своим последним толчком ты кончаешь, покрывая ее большую попу своим семенем.") 
            hide screen ch_hotdog
            $ g_c_u_pic = "sex_cum_out_ani"
            show screen chair_left
            $ genie_chibi_xpos = -70
            $ genie_chibi_ypos = 10
            show screen g_c_u
            
            call cum_block 
            
            call ctc 
            
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"
            m "Угххх."
            m "Да... и на спину получай."
            call nar(">Ты опустошенно падаешь обратно в кресло.") 
            m "Можешь идти [hermione_name]."
            call blkfade 
            pause 1
            
            $ hermione_main_zorder = 5
            hide screen chair_left
            hide screen groping_01
            hide screen groping_02
            hide screen g_c_u
            call her_chibi("stand","desk","base") 
            show screen genie
            hide screen blktone
            hide screen bld1
            call hide_blkfade 
            pause.5
            
            show screen bld1
            call her_main("...Со своей такой попой, в таком виде?","angry","suspicious",cheeks="blush") 
            m "Я уверен никто ничего не скажет, ведь твоя юбка на тебе. А теперь поторопись, я хочу вздремнуть.'"
            #call her_main("Да [genie_name].","angry","suspicious",cheeks="blush")
            m "Ох, чуть не забыл, 20 очков Гриффиндору!"
            $ gryffindor += 20
            call her_main("Ох... верно, очки. Спасибо вам.","grin","ahegao") 
            call nar(">Гермиона поднимает юбку и пытается ее надеть. Задница настолько огромна, что едва покрывает половину.") 

            call nar(">Твоя сперма все еще видна на ее заднице.") 
            call her_main("...","open","closed") 
    
    
    hide screen hermione_main
    $ uni_sperm = False
    hide screen no_groping_02
    hide screen groping_02
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    call her_chibi("stand","desk","base") 
    show screen genie
    hide screen blktone
    hide screen bld1
    with d3
    
    call her_walk("desk","leave",2) 
    
    $ hermione_takes_classes = True
    call update_her_uniform 

    jump day_main_menu
        #will add this later
        #"-Выебать жопу-" if whoring >= 22: 