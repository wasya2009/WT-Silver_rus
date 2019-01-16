

label potion_scene_11: #Milking potion

    if potion_scene_11_progress == 0 or whoring < 13:
        $ potion_scene_11_progress = 1
        jump potion_scene_11_1
    elif potion_scene_11_progress == 1 or whoring < 18:
        $ potion_scene_11_progress = 2
        jump potion_scene_11_2
    else:
        jump potion_scene_11_3


label potion_scene_11_1: #Milking potion part 1
    m "[hermione_name], не хочешь ли попробовать маленькое зелье?"
    call her_main("...","open","angryCl") 
    call her_main("Если бы у меня был выбор, я бы предпочла ничего не пробовать...","open","base") 
    m "Ну-"
    call her_main("Но, к сожалению, похоже \"Слизерин\" выиграет Кубок факультетов в этом году, а это недопустимо!","scream","angryCl") 
    m "Значит, ты выпьешь зелье?"
    call her_main("Да, [genie_name], я выпью ваше зелье.","annoyed","suspicious") 
    m "Великолепно!"
    call nar(">Ты передаешь ей мутное зелье.","start") 
    call nar(">Гермиона осторожно нюхает его.","end") 
    call her_main("Это молоко?","annoyed","angryL") 
    call her_main("...","annoyed","frown") 
    call her_main("Думаю, это не имеет значения...","open","suspicious") 
    
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Гермиона быстро выпивает зелье.") 
    
    call her_chibi("stand","mid","base") 
    
    call her_main("Ах...","cum","worriedCl") 
    call her_main("Это было молоко!","smile","baseL") 
    m "Да. Вероятно, особый вид молока."
    call her_main("Вероятно?","open","suspicious") 
    call her_main("Вы хотя бы знаете, откуда оно взялось?","annoyed","frown") 
    m "К-конечно знаю."
    m "Я ведь великий Дингодор!"
    call her_main("...","open","suspicious") 
    call her_main("Если вы не хотите говорить откуда оно, ладно, сэр...","open","angryCl") 
    call her_main("Но нет нужды оскорблять меня...","normal","frown") 
    m "(А что я сказал?)"
    m "Да, но, ты должна заметить, что эффекты начнут проявляться достаточно скоро."
    call her_main("Хммм...","base","glance") 
    call her_main("И какого рода \'эффекты\' должны быть?","open","suspicious") 
    m "Ты заметишь небольшое набухание в своих красивых грудях."
    call her_main("...","base","base") 
    call her_main("Это молоко делает мою грудь больше, [genie_name]?","annoyed","frown") 
    m "Это еще не все."
    call her_main("...","normal","frown") 
    call her_main("И что же будет еще?","annoyed","angryL") 
    m "Ну, ты начнешь замечать немного молока, выходящего из твоих-"
    call her_main("Что???","shock","wide") 
    call her_main("Проффесор, вы хотите сказать, что это зелье вызовет у меня лактацию?","annoyed","frown") 
    m "Можно и так сказать."
    call her_main("...","normal","frown") 
    call her_main("Ну и как долго это продлится? У меня сегодня занятия.","annoyed","angryL") 
    call her_main("Я и так достаточно отстаю...","annoyed","worriedL") 
    m "Правда?"
    call her_main("Да... Я думаю, это все из-за дурачества, сэр.","normal","worriedCl") 
    call her_main("На днях я чуть не получила \"4\" по биологии...","angry","worried") 
    m "Кстати, говоря о биологии..."
    call nar(">Ты замечаешь, что грудь Гермионы слегка набухает.") 
    call her_main("!!!","angry","wide") 
    call her_main("[genie_name], они довольно быстро растут!","angry","worried") 
    m "Все нормально."
    call her_main("...","open","suspicious") 
    call nar(">Грудь Гермионы начинает заметно увеличиваться.") 
    call her_main("Угх... чувство, будто мои органы сдвигаются в грудь...","angry","worried") 
    call her_main("Это ведь не вызовет никаких проблем?","annoyed","frown") 
    m "К-к-конечно нет..."
    call her_main("...","normal","frown") 
    call her_main("Это было не особо убедительно...","annoyed","frown") 
    m "Просто сфокусируйся на текущем вопросе."
    
    $ hermione_expand_breasts = True #Temporary.
    
    call update_her_uniform #Updates body.
    with hpunch
    
    call her_main("!!!","angry","wide") 
    
    if hermione_wear_top:
        call nar(">Ты слышишь слабый хлопок, когда рубашка Гермионы не сдерживает ее быстро расширяющуюся грудь.") 
    else:
        if hermione_wear_bra:
            call nar(">Ты слышишь слабый хлопок, когда бюстгальтер Гермионы не сдерживает ее быстро расширяющуюся грудь.") 
        else:
            call nar(">Ты в страхе наблюдаешь, как грудь Гермионы начинает быстро расширяться!") 
            
    call her_main("[genie_name], это абсурд!","angry","worried") 
    call her_main("Я не могу пойти на занятия в таком виде.","annoyed","worriedL") 
    m "Почему нет? Не думаю что они намного больше, чем раньше."
    call her_main("Вы шутите надо мной?","disgust","glance") 
    call her_main("Они {size=+5}огромны!{/size}","angry","angry") 
    m "Ну, если ты хочешь вернуть их в норму..."
    call her_main("Что? У вас есть противоядие?","grin","baseL") 
    m "Не противоядие, у меня есть метод, который облегчит разбухание."
    call her_main("...","annoyed","angry") 
    call her_main("Я слушаю...","annoyed","frown") 
    m "Насколько я могу судить, твоя грудь разбухает из-за избытка молока."
    call her_main("...","annoyed","angry") 
    m "Если мы каким-то образом выжмем его оттуда, я уверен, что они мгновенно вернутся к нормальному размеру."
    call her_main("...","scream","wide_stare") 
    call her_main("Вы же не серьезно?","annoyed","annoyed") 
    call her_main("Вы предлагает меня подоить?! Как какое-то животное!","annoyed","annoyed") 
    m "Я просто предложил способ решить проблему."
    m "Если тебе не нужна моя помощь, боюсь, тебе придется идти на занятия в таком виде."
    call her_main("*хмпф*","annoyed","frown") 
    call her_main("Хрен редьки не слаще.","open","suspicious") 
    call her_main("Честно, [genie_name], я в шоке, что вы предложили что-то настолько нелепое.","normal","frown") 
    call her_main("Думаю мне нужно идти...","annoyed","angryL") 
    m "Хорошо, 20 очков \"Гриффиндору\""
    $ gryffindor += 20
    call her_main("Спасибо...","annoyed","suspicious") 
    $ milking = -1
    
    call her_walk("mid","leave",2) 
    
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_11_2: #Milking potion part 2
    #Genie offers hermione the potion again
    #She reluctantly accepts, but says that she expects to be paid double.
    #takes potion
    #comments on taste
    #wait
    #breasts expand
    #Genie offers milking
    #Hermione reluctantly accepts
    #Pulls out machine
    #Hermione shocked, expected to be by hand
    #Tries to refuse
    #Genie says she has already agreed
    #Upset, she puts on the milker
    #Slowly starts to work
    #Hermione is Cautious at first but gradually starts to enjoy it
    #starts to enjoy it a little too much
    #starts moaning, gets close to cumming
    #milking stops
    #she is somewhat upset but goes to class wearing expanded clothes
    
    m "[hermione_name], не хотела бы попробовать хорошего молока?"
    call her_main("...","annoyed","frown") 
    call her_main("Это снова то чертово молоко, сэр?","scream","angryCl") 
    m "Можеть быть..."
    call nar(">Ты передаешь ей мутное зелье.","start") 
    call nar(">Гермиона осторожно нюхает его.","end") 
    call her_main("Это оно!","annoyed","angryL") 
    call her_main("...","annoyed","frown") 
    call her_main("Ну...","open","suspicious") 
    call her_main("Если вы хотите, чтобы я снова выпила это проклятое молоко...","open","suspicious") 
    call her_main("У меня есть два условия...","annoyed","angryL") 
    m "Назови их."
    call her_main("Первое!","scream","angryCl") 
    call her_main("Я требую, чтобы мне заплатили сто очков!","scream","angryCl") 
    call her_main("Второе!","scream","angryCl") 
    call her_main("Я надеюсь, вы сможете извлечь молоко...","scream","worriedCl") 
    m "По рукам!"
    call her_main("Хорошо, тогда...","angry","worriedCl",emote="05") 
    call nar(">Гермиона в последний раз смотрит на зелье, прежде чем закрыть глаза...") 
    
    call her_chibi("drink_potion","mid","base") 
    
    call her_main("...","full_cum","dead") 
    call nar(">Гермиона быстро выпивает зелье.") 
    
    call her_chibi("stand","mid","base") 
    
    call her_main("Ах...","cum","worriedCl") 
    call her_main("На самом деле это не так уж плохо.","smile","baseL") 
    m "Как простое коровье молоко?"
    call her_main("Вроде того...","open","suspicious") 
    call her_main("Только немного слаще...","upset","wink") 
    call her_main("Но это не плохо...","base","baseL") 
    call her_main("А также оно выглядит немного более желтовато.","annoyed","down") 
    m "Да, ну, ты должна заметить, что оно начнет влиять на тебя довольно быстро."
    call her_main("Хммм...","annoyed","down") 
    call her_main("Ну, как вы собираетесь решить проблему с молоком, [genie_name]?","open","down") 
    call her_main("Мне прийдется стоять здесь...","base","ahegao_raised") 
    call her_main("В рубашке...","soft","squintL") 
    
    call set_hermione_action("lift_top") 
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") 
    pause.5
    
    call nar(">Гермиона быстро снимает ее.") 
    call her_main("Вы будете использовать свои грубые руки, чтобы подоить меня...","grin","ahegao") 
    call her_main("Как какое-то животное!","grin","dead") 
    m "Не совсем..."
    call nar(">Ты передаешь ей доильный аппарат.") 
    call her_main("Что это???","scream","wide") 
    m "Доилка."
    call her_main("Проффесор, вы правда думаете, что я это надену?","open","worriedCl") 
    m "Если только ты не хочешь пойти в класс с этими дыньками, полными молока."
    call her_main("Но...","shock","worriedCl") 
    call her_main("Разве вы не можете сделать это вручную?...","soft","ahegao") 
    call her_main("Я думала, что это будет так же, как когда вы играете с ними...","angry","wink") 
    m "Не могу. Я не думаю, что смогу выжить все, до начала твоих занятий."
    call her_main("Я уверена есть вре-","base","worriedCl") 
    
    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.png"
    
    call her_main("","shock","wide",cheeks="blush",trans="hpunch") 
    pause.5
    
    call her_main("!!!","angry","worriedCl",cheeks="blush") 
    call nar(">Ты замечаешь, что грудь Гермионы слегка распухла.") 
    call her_main("[genie_name], они слишком быстро растут!","angry","worriedCl",cheeks="blush",emote="05") 
    m "Все нормально."
    call her_main("Пожалуйста...","disgust","shocked",cheeks="blush") 
    
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png"
    with hpunch
    pause.5    
    
    call nar(">Грудь Гермионы снова начинает заметно распухать.") 
    call her_main("Угххх...","grin","ahegao") 
    
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png"
    with hpunch
    pause.5    
    
    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 1
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with d3
        
    call nar(">Ты замечаешь, что грудь Гермионы набухает в последний раз.") 
    call her_head("!!!","upset","worriedCl",cheeks="blush",xpos="base",ypos="base") 
    pause
    $ ccg1 = 2
    call her_head("[genie_name], это абсурд!","open","worriedCl",cheeks="blush") 
    call her_head("Они должны быть такими большими?","angry","angry",cheeks="blush") 
    m "Да."
    $ ccg1 = 3
    call her_head("...","annoyed","annoyed") 
    $ ccg1 = 4
    call her_head("Извращенец.","open","annoyed",cheeks="blush") 
    m "Ну, кажется они достигли своего максимального размера..."
    pause
    $ ccg1 = 2
    call her_head("*хмпф* Отлично!","annoyed","annoyed") 
    $ ccg1 = 1
    call her_head("Просто давайте я надену это ваше странное доильное устройство, которое, по какой-то причине, у вас есть!","annoyed","angryL") 
    m "Ну, технически, я просто одалживаю его, так что убедитесь, что не сломаешь его..."
    $ ccg1 = 2
    pause
    call her_head("...","annoyed","frown") 
    call her_head("Угх... я терплю эти вещи ради своего факультета.","annoyed","suspicious") 
    hide screen ccg 
    with d3
    call nar(">Гермиона медленно застегивает ремни.") 
    
    $ milking = 1
    call set_hermione_action("milk_breasts") 
    
    call her_main("Готово! Наконец-то!","disgust","narrow") 
    m "Я думаю, ты могла бы помычать для полноты картины..."
    call her_main("...","angry","angry") 
    call her_main("Давайте просто покончим с этим...","annoyed","angryL") 
    m "Эм... Он зачарован..."
    "(Имеет ли оно переключатель...)"
    call her_main("Подождите... Этот предмет зачарован? Пожалуйста, не вклю-","angry","base") 
    call nar(">Ты слышишь слабый шум, когда ремни на груди Гермионы оживают.") 
    
    $ milking = 2
    call set_hermione_action("milk_breasts") 
    
    call her_main("!!!","base","ahegao_raised",cheeks="blush") 
    call her_main("{size=+5}ВЫКЛЮЧИТЕ! ВЫКЛЮЧИТЕ ЕГО!{/size}","shock","worriedCl") 
    m "Думаю, тебе нужно подождать, пока все закончится."
    call her_main("Угх...","open_tongue","ahegao_raised",cheeks="blush") 
    call her_main("Не могу...","open","worriedCl") 
    call her_main("Слишком сильно...","open","worriedCl") 
    m "Что случилось?"
    call her_main("Угх... оно сосет...","open","worriedCl") 
    call her_main("Слишком сильно!","shock","worriedCl") 
    m "Сможешь просто перетерпеть?"
    call her_main("Угх.... наверное... {p}Я пытаюсь.","silly","ahegao") 
    call nar(">Ты ждешь еще несколько минут, пока Гермиона доится перед тобой.") 
    
    $ milking = 3
    call set_hermione_action("milk_breasts") 
    
    call her_main("...","open_wide_tongue","ahegao") 
    call nar(">Ее выражение лица медленно меняется от дискомфорта к удовольствию.") 
    call her_main("...","silly","dead") 
    
    $ milking = 4
    call set_hermione_action("milk_breasts") 
    
    call nar(">Закончив, машина издает приятный щелчок.") 
    m "Ладно, что ж, похоже, ты готова отправиться в класс."
    call her_main("Что?","annoyed","angryL") 
    call her_main("Разве вы не можете оставить его включенным...","open","worriedCl") 
    m "Боюсь, нет."
    m "(Я даже не знаю как оно включается...)"
    call her_main("Но я была так близка...","shock","worriedCl") 
    call her_main("...","annoyed","angryL") 
    call her_main("Хорошо... Тогда мне лучше пойти на зельеварение...","annoyed","down") 
    
    hide screen hermione_main
    call blkfade 
    
    call nar(">Гермиона расстегивает ремешки. Ты замечаешь мимолетное выражение сожаления на ее лице.") 
    
    $ hermione_expand_breasts = True
    call h_action("none") 
    call update_her_uniform 
    pause.5
    hide screen bld1
    call hide_blkfade 
    
    m "Тебе лучше?"
    call her_main("На удивление, да...","annoyed","base") 
    call her_main("Кажется, они даже немного уменьшились.","open","down") 
    call her_main("Вы уверены, что они больше не будут течь?","open","suspicious") 
    m "Ох, эм, нет, конечно нет..."
    call her_main("...","normal","frown") 
    call her_main("Ну, я хотела бы, чтобы вы мне сейчас заплатили [genie_name]...","annoyed","angryL") 


    m "Ох, да, абсолютно верно. 100 очков \"Гриффиндору\"!"
    $ gryffindor += 100
    
    call her_main("Спасибо вам, сэр...","open","suspicious") 
    call her_main("(Хотя мне все еще нужно бежать в класс с этими огромными буферами...)","annoyed","angryL") 
    call her_main("(Не то, чтобы я против лишнего внимания...)","soft","squintL") 

    $ milking = 0

    call her_walk("mid","leave",2) 
    
    $ hermione_takes_classes = True
    $ hermione_sleeping = True #this is intentional 
    jump day_main_menu

label potion_scene_11_3: #Milking potion part 3
    $ milking = 0
    #Genie offers hermione the potion
    #Agrees on the condition that she milks him
    #Genie agrees
    #option to add extra ingredient
    #Hermione drinks potion
    #Comments that the milk tastes sweeter than regular milk
    #wait
    #Breasts expand
    #takes her top off

    #option 1 (futa)

    #option 2 (Permanent expansion)
    m "[hermione_name], хочешь молочного коктейля?"
    call her_main("Правда? Клубничный, пожалуйста!","smile","happyCl",emote="06") 
    m "Извини, у меня только ванильный..."
    call nar(">Ты передаешь ей мутное зелье.","start") 
    call nar(">Гермиона осторожно нюхает его.","end") 
    call her_main("Это то самое чертово молоко!","angry","wide") 
    call her_main("...","annoyed","frown") 
    call her_main("Я хочу молочный коктейль...","annoyed","down") 
    m "Я уверен, если ты встряхнешь бутылку, оно станет пенистым."
    call her_main("Это не одно и то же!","scream","angryCl") 
    call her_main("Там нет сахара или ароматизатора!","annoyed","frown") 
    
    if potion_version > 1:
        m "Ну, у меня есть один особый ингредиент..."
        call her_main("Неужели?","angry","wink") 
        call her_main("Это клубника?","soft","ahegao") 
        m "Почему бы тебе не попробывать и не выяснить?"
        call her_main("Хорошо...","open","suspicious") 
        call her_main("(Я надеюсь это клубника!)","smile","happyCl",emote="06") 
    else:
        m "Просто, выпей это..."
        call her_main("*хмпф* Хорошо...","open","suspicious") 
        call her_main("(По крайней мере, он должен был добавить шоколадный ароматизатор...)","open","suspicious") 
        
    call nar(">Гермиона в последний раз смотрит на зелье, прежде чем закрыть глаза...") 
    
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Гермиона быстро выпивает зелье.") 
    
    call her_chibi("stand","mid","base") 
    
    call her_main("Ах...","cum","worriedCl") 
    call her_main("Это была не клубника!","annoyed","annoyed") 
    m "Ты действительно думала, что она там будет?"
    call her_main("Думала... Отчасти?","annoyed","down") 
    call her_main("Вы все таки маг...","annoyed","down") 
    call her_main("Домашние эльфы делают мне молочный коктейль, когда я прошу...","annoyed","angry") 
    m "Говоря о молочных коктейлях!"
    call nar(">Ты замечаешь, что грудь Гермионы начинает набухать...") 
    call her_main("Угх... это чувство всегда такое странное...","angry","down_raised") 
    
    if hermione_wear_top:
        call her_main("Я лучше сниму рубашку, прежде чем \'они\' порвут пуговицы...","normal","frown") 
    else:
        if hermione_wear_bra:
            call her_main("Я лучше сниму бюстгальтер, преждче чем \'они\' порвут застежку...","normal","frown") 
    
    call set_hermione_action("lift_top") 
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") 
    pause.5
    
    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.png" 
        with hpunch
        pause.5    
    
    
    if not potion_version == 2: #Orgasms while milking
        call her_main("!!!","angry","wide") 
        call nar(">Ты замечаешь, что грудь Гермионы начинает расти больше.") 
        call her_main("Угх...","grin","ahegao") 
        m "Мммм, вот так."
        call her_main("(Это так, странно...)","angry","down_raised") 
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png" 
        with hpunch
        pause.5    
    
        call her_main("!!!","angry","wide") 
        call nar(">Грудь Гермионы снова начинает заметно опухать.") 
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        with hpunch
        pause.5    
    
        call her_main("!!!","angry","down_raised") 
        call nar(">Ты замечаешь, что грудь Гермионы набухает в последний раз.") 
        call her_main("[genie_name], это нелепо!","annoyed","annoyed") 
        call her_main("В этот раз вы сделали зелье сильнее?","annoyed","angryL") 
        m "О чем ты говоришь, они такого же размера, как всегда."
        call her_main("Вы уверены...","annoyed","frown") 
        call nar(">Гермиона покачивает сиськи из стороны в сторону.") 
        call her_main("Просто, такое чувство, что они ...более тяжелые... чем раньше.","annoyed","down") 
        m "Ну, учитывая, как ты опустошила свое молоко в последний раз, может быть, они стали больше..."
        call her_main("Лучше бы их не было...","shock","worriedCl") 
        call her_main("Просто дайте мне доилку, чтобы я могла пойти на занятия...","annoyed","annoyed") 
        m "Это единственная причина, по который ты этого хочешь?"
        call her_main("Что? Зачем еще мне это нужно?","open","baseL") 
        m "Я припоминаю, как ты наслаждалась этим в прошлый раз."
        call her_main("Иногда вы действительно отвратительны, [genie_name]...","annoyed","angryL") 
        m "Что ты сказала..."
        call nar(">Ты передаешь Гермионе ремни.","start") 
        call nar(">Гермиона берет их из рук и медленно надевает, заботясь о том, чтобы грудь вошла в чаши.","end") 
        
        $ milking = 1
        call set_hermione_action("milk_breasts") 
        
        call her_main("...","upset","worriedCl",cheeks="blush") 
        m "Ты уверена что не хочешь помычать?..."
        call her_main("...","soft","squintL") 
        call her_main("{size=-5}Муу...{/size}","open","baseL") 
        m "Что это было?"
        call her_main("Я не скажу это снова, [genie_name]... {size=-5}достаточно одного раза...{/size}","annoyed","angryL") 
        call her_main("...","annoyed","down") 
        call her_main("Ох!","open","worriedCl") 
        call nar(">Ты слышишь слабый шум, когда ремени на груди Гермионы оживают.") 
        
        $ milking = 2
        call set_hermione_action("milk_breasts") 
        
        call her_main("!!!","soft","squintL") 
        call her_main("Угх... в этот раз все по другому...","open","worriedCl") 
        call her_main("Как будто в моей груди гораздо больше...","shock","worriedCl") 
        call her_main("И все оно хочет выйти...","silly","dead") 
        call her_main("Слишком много...","silly","ahegao") 
        m "Что случилось?"
        call her_main("Ах... оно сосет...","grin","ahegao") 
        call her_main("Не так, как раньше!","silly","ahegao") 
        m "Тебе больно?"
        call her_main("Ах.... нет... {p}Это неплохо...","silly","dead") 
        
        $ milking = 3
        call set_hermione_action("milk_breasts") 
        
        call her_main("Ах...{image=textheart}{image=textheart}{image=textheart}","grin","dead") 
        call nar(">Ты замечаешь, что канистра перед ней наполняется молоком с угрожающей скоростью...") 
        call her_main("Ах... это так приятно...","grin","ahegao") 
        
        $ milking = 4
        call set_hermione_action("milk_breasts") 
        
        call nar(">Закончив, машина издает приятный щелчок.") 
        m "Ладно, что ж, похоже, ты готова отправиться в класс."
        call her_main("Что? Но, сэр...","open","worriedCl") 
        call her_main("Они все еще полные...","shock","worriedCl") 
        m "Боюсь, что машина заполнена."
        call her_main("(Но я была так близко...)","open","worriedCl") 
        call her_main("Ах... и если я пойду так на занятия, то буду везде течь!","shock","worriedCl") 
        m "Ну, если ты опустошишь канистру, она включится обратно"
        call her_main("Опустошить ее...","angry","wink") 
        call nar(">Гермиона смотрит на канистру, заполненную молоком.") 
        call her_main("Могу я просто вылить его на пол?","annoyed","down") 
        m "И потратить все это питательное молоко?"
        
        menu:
            "-Убедить выпить-":
                call her_main("Не хочешь ли выпить его, [genie_name]?","angry","wink") 
                m "Эм, боюсь нет... Я только что съела большую миску хлопьев."
                call her_main("...","annoyed","down") 
                call her_main("Может у вас есть бутыль для хранения...","angry","wink") 
                m "Свободных нет..."
                call her_main("...","annoyed","angryL") 
                m "Я боюсь, тебе придется выпить его самой."
                call her_main("...","soft","squintL") 
                call her_main("{size=-5}Хорошо...{/size}","open","baseL") 
                m "Правда?"
                call her_main("Я не могу пойти на занятия, выделяя молоко...","annoyed","angryL") 
                call her_main("и кроме того, это не самое приятное чувство...","angry","down_raised") 
                call her_main("Я не прочь завести доилку еще раз...","soft","ahegao") 
                m "Хорошо, до дна!"
                call her_main("...","annoyed","down") 
                
                $ milking = 5
                call set_hermione_action("milk_breasts") 
                
                call nar(">Гермиона смотри на канистру в последний раз, прежде чем отвинтить ее и приложить к губам.") 
                call her_main("(За Гриффиндор!)","scream","angryCl") 
                call nar(">Она набирает полный рот собственного молока.") 
                call her_main("...","full_cum","dead") 
                call her_main("*глотает*","cum","worriedCl") 
                call nar(">Она набирает последнюю половину в рот.") 
                call her_main("...","full_cum","dead") 
                call her_main("*глотает*","cum","worriedCl") 
                call her_main("Ах...","grin","dead") 
                call her_main("Думаю, мне нужно будет пропустить еду после всего этого молока...","angry","wink") 
                call nar(">Она медленно завинчивает канистру обратно в доилку.") 
                
                $ milking = 1
                call set_hermione_action("milk_breasts") 
                
                call her_main("...","base","down") 
                call her_main("Ох!","open","closed") 
                call nar(">Доилка снова оживает и начинает доить Гермиону во второй раз.") 
                
            "-Выпить самому-":
                call her_main("Не хотите ли выпить его, [genie_name]?","angry","wink") 
                m "Не выкидывать же, но и не хочу!"
                call her_main("...","angry","wide") 
                call her_main("Что ж, тогда вы здесь...","angry","base") 
                
                $ milking = 5
                call set_hermione_action("milk_breasts") 
                
                call nar(">Гермиона смотрит на канистру в последний раз, прежде чем отвинтить и передать ее вам.") 
                call her_main("(Странный...)","angry","down_raised") 
                call nar(">Ты набираешь полный рот ее молока.") 
                m "Ммммммм... Вкуснотища!"
                call her_main("...","angry","wink") 
                call her_main("Правда? Вам нравится мое молоко?","open","baseL") 
                m "Больше, чем вода из оазиса!"
                call her_main("...","annoyed","angryL") 
                call her_main("Ну...","soft","squintL") 
                call her_main("Вы собираетесь заканчивать?","smile","angry") 
                call nar(">Ты опустошаешь канистру за один последний глоток.") 
                call her_main("...","smile","happyCl") 
                call nar(">Она медленно завинчивает канистру обратно в доилку.") 
                
                $ milking = 1
                call set_hermione_action("milk_breasts") 
                
                call her_main("(Я не могу поверить, что ему понравилось...)","smile","baseL") 
                call her_main("(Может быть, оно действительно вкусно...)","grin","baseL") 
                call her_main("...","base","down") 
                call her_main("Ох!","open","closed") 
                call nar(">Доилка снова оживает и начинает доить Гермиону во второй раз.") 


        call her_main("!!!","grin","dead") 
        call her_main("Угх... это тааааак приятно...","grin","ahegao") 
        $ hermione_dribble = True
        
        $ milking = 2
        call set_hermione_action("milk_breasts") 
        
        call her_main("Ах... похоже, ремни массируют меня, пока оно сосет...","silly","dead") 
        call her_main("ммм... это потрясающе...","silly","ahegao") 
        call nar(">Гермиона позволяет машине продолжить работу.") 
        
        $ milking = 3
        call set_hermione_action("milk_breasts") 
        
        call her_main("Ах... Я думаю это все [genie_name]...","annoyed","down") 
        call nar(">Ты заметил что поток молока, выступающий из грудей Гермионы, почти прекратился.") 
        m "Ну как?"
        call her_main("Это было невероятно...","grin","ahegao") 
        call her_main("Оно даже почти заставило меня кончить...","base","down") 
        call her_main("Но сейчас вы можете его выключить...","angry","wink") 
        m "Эм..."
        call nar(">Машина пытается сосать молоко из груди Гермионы.") 
        m "Я не уверен как... Я думаю, что оно отключается только тогда, когда заполнится?"
        call her_main("Ну, я не думаю, что оно сможет получить еще-","upset","closed") 
        call nar(">Ты начинаешь слышать жужжание, похожее на пылесос, который был зажеван ковром.") 
        call her_main("!!!","disgust","shocked",cheeks="blush") 
        call nar(">Ты слишишь странный щелчок, исходящий от ремней") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("Ах!!!","grin","ahegao_mad",cheeks="blush") 
        call nar(">Ты видишь, как из сосков Гермионы вытекает маленькая струйка молока.") 
        $ hermione_squirt = False
        
        call nar(">Канистра по-прежнему заполнена на половину.") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}Ах!!!{/size}","silly","ahegao") 
        call nar(">Еще одна маленькая струйка молока выходит из сосков Гермионы.") 
        $ hermione_squirt = False
        
        call her_main("{size=+5}Оно заставляет меня кончать!{/size}","shock","worriedCl") 
        call her_main("{size=+5}Почему это-{/size}","open","worriedCl") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","silly","dead") 
        $ hermione_squirt = False
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","ahegao") 
        $ hermione_squirt = False
        
        hide screen hermione_main
        call blkfade 
        
        call nar(">Машина продолжает еще пару минут. Каждый треск сопровождается небольшим брызгом молока в чашки...") 
        
        $ milking = 4
        call h_action("milk_breasts") 
        pause.5
        call hide_blkfade 

        call her_main("...","open_wide_tongue","ahegao") 
        call nar(">Гермиона стоит перед тобой, не в состоянии говорить.") 
        m "Ох, эм... 20 очков \"Гриффиндору\"!"
        $ gryffindor += 20
        call her_main("...","open_wide_tongue","ahegao") 
        m "И мне нужно это обратно."
        call her_main("...","open_wide_tongue","ahegao") 
        call blkfade 
        
        call nar(">Ты медленно снимаешь доильный аппарат, заполненный молоком. У нее остаются красные следы, окружающие ее нежные соски, где были чашки.") 
        call h_action("none","skip_update") 
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        m "Хммм... возможно, сегодня мы немного переусердствовали."
        call hide_blkfade 
        
        call her_main("...","silly","worried",cheeks="blush",tears="soft") 
        m "Почему бы тебе не вернуться в свою комнату... Думаю, ты заслужила выходной."
        call her_main("Да...","silly","dead") 
        call her_main("Сейчас пойду...","silly","ahegao") 
        m "Может быть, ты должна сначала одеться..."
        call her_main("...","grin","ahegao") 
        call blkfade 
        
        call nar(">Гермиона медленно одевается, постоянно путаясь.") 
        
        $ hermione_perm_expand_breasts = True #Temporary.
        call h_action("none") #Resets clothing.
        call hide_blkfade 
        
        call her_main("До свидания, сэр...","silly","dead") 
        if potion_version == 2:
            call nar(">Грудь Гермионы теперь будет постоянно большой благодаря добавленному ингредиенту Снейпа.","start") 
            call nar(">Однако, заставив ее снова принять зелье, можно сбросить эффект...","end") 



    else: #futa variant
        call nar(">Ты замечаешь, что грудь Гермионы начинает расти немного больше.") 
        call her_main("!!!","angry","wide") 
        # change boobs
        call her_main("Угх...","grin","ahegao") 
        m "Мммм, вот так."
        call her_main("(Это так странно...)","angry","down_raised") 
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png" 
        with hpunch
        pause.5
        
        call her_main("!!!","angry","wide") 
        call nar(">Грудь Гермионы снова начинает заметно набухать.") 
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        with hpunch
        pause.5
        
        call her_main("!!!","angry","down_raised") 
        call nar(">Ты замечаешь, что грудь Гермионы заметно набухает.") 
        call her_main("[genie_name], это абсурдн!","annoyed","annoyed") 
        call her_main("В этот раз вы сделали зелье сильнее?","annoyed","angryL") 
        m "Ну, там был особый ингредиент..."
        call her_main("Что? Моя грудь будет еще больше?","annoyed","angryL") 
        call nar(">Гермиона покачивает свои сиськи из стороны в сторону.") 
        call her_main("Я не думаю, что смогу это выдержать!","annoyed","down") 
        m "Твоя грудь не должна увеличиваться..."
        call her_main("Ох...","base","down") 
        m "Однако, ты можешь заметить, что что-то еще начнет расти."
        call her_main("Что? Только не кошачьи уши снова, пожалуйста...","annoyed","angryL") 
        m "Не волнуйся, это-- Эхм... что-то еще..."
        call her_main("...","angry","wide") 
        call her_main("Подождите...","angry","down_raised") 
        call her_main("Вы не имеете в виду...","disgust","down_raised") 
        call her_main("Вы бы не... не так ли?","annoyed","angryL") 
        m "Мы просто подождем и посмотрим..."
        call her_main("Вы действительно отвратительный извращенец [genie_name]...","open","annoyed",cheeks="blush") 
        m "Что ты сказала..."
        call her_main("Пожалуйста, скажите мне, что у меня не вырастет чертовск-","angry","down_raised") 
        
        hide screen hermione_main
        call h_action("lift_skirt") 
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        show screen hermione_main
        with d3
        pause.5
        
        hide screen hermione_main
        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call h_action("none","skip_update") 
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        show screen hermione_main
        with d3
        pause.5
        
        call her_main("...","angry","wide") 
        
        $ hermione_futa = True
        
        call her_main("","shock","down_raised",trans="hpunch") 
        pause.8
        
        call her_main("Вы чертов {size=+10}извращенец!{/size}","shock","worriedCl",cheeks="blush") 
        g9 "Вау! Неплохо..."
        call her_main("Неплохо? Это неплохо?","scream","angry",emote="01") 
        call her_main("У меня гребанный {size=+10}член!{/size}","angry","angry",emote="01") 
        m "Да ладно [hermione_name]... где твое чувство приключений?"
        call her_main("Приключений?","annoyed","annoyed") 
        call her_main("Войти в тайную комнату было приключением, сэр...","open","suspicious") 
        call her_main("Стоять в кабинете директора, пока он заставляет меня пить какое-то случайное зелье, которое он, вероятно, нашел в сточной канаве-","scream","angryCl") 
        call her_main("-Которое вызывает у меня, {size=+3}лактацию{/size}, {size=+5}сиськи{/size} и гигантский {size=+10}{b}ЧЛЕН{/b}{/size} это {size=+2}не {size=+2} {size=+4}Приключение!{/size}","scream","angry",emote="01") 
        m "Не забывай о волшебном доильном аппарате..."
        call nar(">Ты передаешь Гермионе ремни от доилки.") 
        m "Конечно, это делает его приключением..."
        call her_main("Что вы мне предлагаете делать с этим?","annoyed","frown") 
        call her_main("Вряд ли оно сможет избавиться от этого {size=+10}ЧЛЕНА{/size} .","angry","angry") 
        m "Фактически, оно должно."
        m "(Так или иначе, я на это надеюсь... Снейп сказал, что это магия..)"
        call her_main("Правда?","annoyed","annoyed") 
        m "Правда, правда."
        call her_main("Угх, отлично... (есть вещи, с которыми я мирюсь)","annoyed","angryL") 
        call nar(">Гермиона берет в руки и идет надевать.") 
        call her_main("Куда мой, тупой член должен войти...","angry","base") 
        call her_main("Он не входит в канистру.","angry","down_raised") 
        m "Попробуй воткнуть его в дно канистры."
        call her_main("Что... Почему он долж-","annoyed","annoyed") 
        
        $ milking = 1
        call set_hermione_action("milk_breasts") 
        
        call her_main("!!!","silly","dead") 
        m "И как?"
        call her_main("Простите, что злилась раньше [genie_name]...","silly","worried",cheeks="blush",tears="soft") 
        call her_main("Я не знала, что буду чувствовать что-то подобное...","grin","ahegao") 
        m "Как что?"
        call her_main("Это чертовски хорошо...","silly","ahegao") 
        call her_main("Я никогда не думал, что секс может быть таким...","silly","dead") 
        call her_main("Быть внутри чего-то...","silly","ahegao") 
        call her_main("Это лучше всего!","grin","ahegao") 
        call her_main("В таком случае я кончу, прежде чем вы даже включите эту-","silly","worried",cheeks="blush",tears="soft") 
        call nar(">Ты слышишь слабый шум, когда ремни на груди Гермионы оживают.") 
        
        $ milking = 2
        call set_hermione_action("milk_breasts") 
        
        call her_main("!!!","grin","dead") 
        call her_main("Нет!","clench","worried",cheeks="blush",tears="soft") 
        call her_main("Остановите его!","angry","suspicious",cheeks="blush") 
        call her_main("{size=+5}Я серьезно!!!{/size}","angry","dead",cheeks="blush",tears="crying") 
        call her_main("{size=+10}Это слишком... ВЫКЛЮЧИТЕ!!!{/size}","scream","wide") 
        m "Что случилось?"
        call her_main("Ах... все это {b}сосание{/b}...","silly","ahegao") 
        call her_main("Ах... и молоко брызгает на мой {image=textheart}член{image=textheart}......","grin","ahegao") 
        m "Это больно?"
        call her_main("Ах.... нет... {p}это просто слишком хорошо...{image=textheart}","grin","dead") 
        
        $ milking = 3
        call set_hermione_action("milk_breasts") 
        
        call her_main("Ах...{image=textheart}{image=textheart}{image=textheart}","silly","dead") 
        call nar(">Ты замечаешь, что канистра перед ней наполняется молоком с угрожающей скоростью...") 
        call her_main("Ах... пожалуйста [genie_name]...","angry","suspicious",cheeks="blush") 
        call her_main("Ах... вы должны выключить его...","shock","down_raised",cheeks="blush",tears="crying") 
        call her_main("{size=-2}я {size=-2}сойду {size=-2}с ума {size=-2}если {size=-2}вы {size=-2}не...{/size}","silly","worried",cheeks="blush",tears="soft") 
        
        $ milking = 4
        call set_hermione_action("milk_breasts") 
        
        call nar(">Ты заметил заполнение канистры, но машина продолжает работать.") 
        call her_main("Что? Но они полные...","annoyed","down") 
        call her_main("Он должен отключится...","angry","dead",cheeks="blush",tears="crying") 
        call her_main("Пожалуйста... пусть он выключится...","angry","suspicious",cheeks="blush",tears="messy") 
        m "(Еще раз, что сказал Снейп? невидимое внутреннее расширение пространства?)"
        m "Ну, я должен был упомянуть о том, что канистра невидимо расширяется..."
        call her_main("Вы наложили заклятие невидимого расширения на эту канистру?","open","surprised",cheeks="blush",tears="messy") 
        call her_main("{size=+5}Вы это сделали?!{/size}","scream","suspicious",cheeks="blush",tears="messy") 
        m "Возможно."
        call her_main("Нет...","scream","worriedCl",cheeks="blush",tears="messy") 
        call nar(">Гермиона смотрит на заполненый контейнер для молока.") 
        call her_main("Оно когда-нибудь остановится?","shock","down_raised",cheeks="blush",tears="crying") 
        m "Ахххх..."
        call her_main("!!!","angry","dead",cheeks="blush",tears="crying") 
        call her_main("Угх... {image=textheart}это так {image=textheart} хорошоооо...","silly","worried",cheeks="blush",tears="soft") 
        
        $ hermione_dribble = True
        call her_main("Ах... ремни массируют меня, пока оно сосет мой член...","silly","ahegao") 
        call her_main("мммм... это невероятно...{image=textheart}{image=textheart}","grin","ahegao") 
        call nar(">Гермиона позволяет машине продолжать работу.") 
        call her_main("...","open_wide_tongue","ahegao") 
        call nar(">Ты заметил, что количество молока, выступающего из груди Гермионы, почти прекратилось.") 
        call her_main("Эти ощущения потрясающие...","grin","ahegao") 
        call her_main("Оно заставляет меня так много кончать...","silly","ahegao") 
        call nar(">Машина пытается сосать молоко из выжатых грудей Гермионы.") 
        m "Ну, надеюсь, у него есть системы предохранения, когда молоко кончается..."
        call her_main("Хорошо, это должно скоро-","silly","worried",cheeks="blush",tears="soft") 
        call nar(">Ты начинаешь слышать жужжание, похожее на пылесос, который зажевал ковер.") 
        call her_main("!!!","angry","wide") 
        call nar(">Ты слышишь странный щелчок, исходящий из ремней.") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+15}!!!{image=textheart}{image=textheart}{image=textheart}!!!{/size}","grin","dead") 
        call nar(">Ты видишь, как из сосков Гермионы вытекают маленькие струйки молока.") 
        $ hermione_squirt = False
        
        call nar(">Канистра все еще выглядит полной..") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","dead") 
        call nar(">Еще одна маленькая струйка молока выходит из сосков Гермионы.") 
        $ hermione_squirt = False
        
        call her_main("{size=+5}Оно заставляет меня так {b}сильно{/b} кончать...{/size}","silly","worried",cheeks="blush",tears="soft") 
        call her_main("{size=+5}Почему эт-{/size}","shock","baseL",cheeks="blush",tears="soft") 
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","ahegao") 
        $ hermione_squirt = False
        
        "*Ззззккк*"
        
        call cum_block 
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","silly","ahegao") 
        $ hermione_squirt = False
        call blkfade 
        
        call nar(">Машина продолжает еще пару минут. Каждый треск сопровождается небольшим брызгом молока в чашки и пульсацией ее члена в канистру...") 
        
        $ milking = 4
        call h_action("milk_breasts") 
        call nar(">Ты позволяешь этому продолжаться еще немного, прежде чем оно окончательно остановится.") 
        call hide_blkfade 

        call her_main("{size=-10}В-выключите ее...{/size}","angry","suspicious",cheeks="blush") 
        call nar(">Гермиона стоит перед тобой, едва способная говорить.") 
        call her_main("{size=-8}В-выключите ее...{/size}","angry","suspicious",cheeks="blush") 
        call her_main("{size=-6}В-выключите ее...{/size}","angry","suspicious",cheeks="blush") 
        call her_main("{size=-4}В-выключите ее... ну...{/size}","angry","dead",cheeks="blush",tears="crying") 
        m "Думаю, с тебя достаточно... 20 очков \"Гриффиндору\"!"
        $ gryffindor += 20
        call her_main("...","angry","suspicious",cheeks="blush") 
        call nar(">И мне нужно это обратно.") 
        call her_main("...","shock","down_raised",cheeks="blush",tears="crying") 
        call blkfade 
        
        call nar(">Ты медленно снимаешь доильный аппарат, заполненный молоком. У нее остаются красные следы, окружающие ее нежные соски, где были чашки..") 
        call h_action("none","skip_update") 
        $ hermione_futa = False
        $ hermione_dribble = False
        
        call nar(">Когда ты вытаскиваешь тяжелую канистру с ее члена, он падает вниз, прежде чем увянуть в никуда.") 
        m "(Фуу...)"
        m "Хммм, думаю, ты сегодня немного переборщила."
        call hide_blkfade 
        
        call her_main("{size=-6}Очень...{/size}","angry","dead",cheeks="blush",tears="crying") 
        m "Почему бы тебе не вернуться в свою комнату... Думаю, ты заслужила еще один выходной."
        call her_main("Да...","angry","suspicious",cheeks="blush") 
        call her_main("Я сейчас пойду...","shock","down_raised",cheeks="blush",tears="crying") 
        m "Может быть, тебе стоит сначала одеться..."
        call her_main("...","angry","dead",cheeks="blush",tears="crying") 
        
        call blkfade 
        call nar(">Гермиона медленно одевается, постоянно путаясь.") 
        
        $ hermione_perm_expand_breasts = True #Temporary.
        call h_action("none") #Resets clothes.
        call hide_blkfade 
        
        call her_main("До свидания, сэр...","shock","down_raised",cheeks="blush",tears="crying") 


    $ milking = 0
    
    call her_walk("mid","leave",2) 
    
    $ hermione_takes_classes = True
    $ hermione_sleeping = True
    
    if potion_version == 3:
        $ hermione_perm_expand_breasts = True
        
    $ hermione_expand_breasts = True #Temporary one.
    $ hermione_expand_breasts_counter = 0 #If 0 resets temporary one the next day.
        
    jump day_main_menu



label potion_scene_11_1_2: #Milking potion part 1 night time
    $ aftersperm = True
    $ milking = 0
    
    call play_sound("door") 
    call her_walk("door","desk",2.5) 
    
    call her_main("Профессор! Почему вы не предупредили меня об этом!","angry","angry",xpos="right",ypos="base") 
    
    m "О чем? Я говорил, что твоя грудь расширится.."
    call her_main("Посмотрите на мою рубашку!","angry","angry",emote="01") 
    m "Хммм, похоже, с тобой произошло происшествие."
    call her_main("Происшествие?","open","suspicious") 
    call her_main("Я весь день истекаю молоком!","scream","angry",emote="01") 
    m "Это не так уж плохо..."
    call her_main("Это третья рубашка, что я носила за сегодня!","open","angryCl") 
    call her_main("Все остальные насквозь промокли!","angry","angry") 
    call her_main("Даже моя жилетка промокла....","annoyed","frown") 
    m "Ну, я предлагал облегчить твою проблему..."
    call her_main("Подоить меня, как свое какое-то... животное!","angry","angry") 
    call her_main("Я расстроен, что ты даже не рассматривала этот вариант.","angry","annoyed",emote="01") 
    m "Ну, это бы решило твои \'проблемы\'."
    call her_main("...","open","suspicious") 
    call her_main("Ну, я ожидаю, что мне дополнительно заплатят после этого унижения.","annoyed","annoyed") 
    m "Сколько?"
    call her_main("30 очков.","annoyed","angry") 
    m "Отлично, 30 очков \"Гриффиндору\"."
    $ gryffindor += 30 
    call her_main("*хмпф*","annoyed","annoyed") 
    call her_main("Так когда же эти \'штуки\' вернутся в норму? Или мне нужно позвать одну из медсестер, чтобы она уменьшила их?","angry","annoyed",emote="01") 
    m "Они должны вернуться в норму сегодня вечером."
    call her_main("Хорошо...","open","suspicious") 
    call her_main("Но не думайте, что я простила вас!","open","angryCl") 
    call nar(">Гермиона в гневе.") 
    $ mad =+ 10
    
    call her_walk("desk","leave",2.5) 
    
    $ hermione_sleeping = True
    $ aftersperm = False
    
    m "(Сучка... Можно подумать, она не была счастлива получить {size=+5}Big Kahunas{/size} бесплатно!) {size=-2}-прим. Big Kahunas Burger-отсылка к вымышленной сети фастфуда в фильмах Квентина Таррантино-Доказательство Жизни; Четыре комнаты; Криминальное чтиво; Бешеные псы{/size}"
    
    return
    
    #comes back after class
    #shirt covered in milk stains
    #furious at genie 
    #Genie responds saying he should have let him milk her
    #Hermione is angry again at him for suggesting it
    #demands more points 
    #asks when they're going to go away
    #genie says she has to get the milk out of them
    #offers to milk her again
    #refuses and says she can take care of it herself
    #leaves

label potion_scene_11_2_2: #Milking potion part 2 night time
    m "asd"
    #comes back after class
    #breasts still expanded
    #genie asks her how her day was
    #She had a good day
    #Appreciates the attention from everyone
    #Milking prevented her from leaking
    #Says she wouldn't mind taking the potion again some time

