

### TRANSPARENCY POTION ###

label potion_scene_4: #Transparent uniform
    m "[hermione_name], у меня есть еще одно зелье для тебя."
    call her_main("Я не думаю, что мне стоит это употреблять, [genie_name].","normal","frown") 
    call her_main("Особенно после того, как вы пытались превратить меня в кошку.","annoyed","frown") 
    m "Если быть честным, я пытался превратить тебя в другую девушку..."
    call her_main("Это ничем не лучше, [genie_name].","angry","angry") 
    m "Разве?"
    call her_main("Ну, по крайней мере, пообещайте мне, что я никак не опозорюсь посреди класса.","open","angryCl") 
    call her_main("Моя репутация страдает и без того. Мне не нужны эти зелья, заставляющие меня трансформироваться перед моими сверстниками.","annoyed","angryL") 
    m "Я обещаю, что это зелье никак не повлияет на твое тело."
    call her_main("Ну и что же оно будет тогда делать?","angry","angry") 
    m "Как всегда, [hermione_name], ты выпьешь это и мы пос..."
    call her_main("Придется подождать и посмотреть. Я знаю.","normal","frown") 
    
    call her_chibi("drink_potion","mid","base") 
    
    call nar(">Гермиона быстро выпивает зелье.") #new
    call her_main("","open","angryCl") 
    
    call her_chibi("stand","mid","base") 
    
    her "Я могу идти?"
    m "Да, можешь. 20 очков Гриффиндору!"
    call her_main("Спасибо, [genie_name].","open","closed") 
    
    $ gryffindor += 20
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk("mid","leave",2) 
    
    $ hermione_takes_classes = True
    if whoring <= 7:
        $ transparency = 0.8
    elif whoring <= 13:
        $ transparency = 0.6
    elif whoring <= 20:
        $ transparency = 0.4
    else:
        $ transparency = 0.2
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_normal.png"
    $ transparent_quest = True
    jump day_main_menu

label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ transparent_quest = False
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base") 
    
    show screen bld1
    if whoring <= 7: #Very angry and embarrassed
        call nar(">Гермиона врывается в твой кабинет.") 
        call her_main("Как вы могли, [genie_name]!","angry","base",tears="soft") 
        call her_main("Я стала посмешищем на всю школу!","angry","base",tears="soft") 
        call her_main("Теперь все знают, как я выгляжу голой!","mad","worriedCl",tears="soft_blink") 
        m "Расскажи подробнее что произошло..."
        call her_main("Рассказать, что произошло? Я больше никогда с вами не буду разговаривать!.","angry","base",tears="soft") 
        $ mad += 20
        $ transparency = 1
        # $ hermione_breasts = "characters/hermione/body/breasts/"+outfit.breast_layer+".png"
        # This is bugged and causes a crash. Things don't go catistrophically wrong without this line, so I've edited it out until you can fix it.
    elif whoring <= 13: #Mildly aggravated
        call nar(">Гермиона быстро без стука заходит в твой кабинет") 
        call her_main("Снова?","angry","worriedCl",emote="05") 
        m "О чем ты, [hermione_name]?"
        call her_main("Почему бы вам снова не сделать мою одежду видимой?","open","base") 
        m "Зачем?"
        call her_main("Вы такая свинья...","annoyed","worriedL") 
        m "Скажи мне, что произошло...."
        call her_main("...","normal","worriedCl") 
        call her_main("Ладно, но за это мне нужно дополнительно 10 очков...","open","base") 
        m "Как скажешь."
        call her_main("Так... В классе зельеварения я заметила, что у всех взор обращен на меня...","disgust","glance") 
        m "Интересно, почему же?"
        call her_main("Как я сказала, я была в классе зельеварения.","annoyed","angryL") 
        call her_main("Я не думала о других, пока в конце урока ко мне не подошел профессор Снейп.","annoyed","annoyed") 
        call her_main("Обычно он критикует меня во время уроков. За такие вещи, как неправильные дозировки и прочее...","annoyed","worriedL") 
        m "Возвращайся к рассказу, [hermione_name]."
        call her_main("Ну, когда он сказал, что ему нравится мой наряд, я насторожилась. Я подумала, что, возможно, он говорил о моей рубашке, пока я не посмотрела вниз и не увидела, что на мне - ничего нет.","disgust","glance") 
        call her_main("Но я просто проигнорировала его и после урока побежала сюда.","annoyed","angryL") 
        m "Ты просто вышла из класса?"
        call her_main("Само-собой, я не могу позволять себе пропускать уроки зельеварения. Я нынче занимаюсь довольно плохо, что бы пропускать его.","annoyed","annoyed") 
        m "Хорошо, справедливо. Ты можешь идти."
        call her_main("Хм... До свидания, [genie_name].","annoyed","worriedL") 

    elif whoring <= 20: #Slightly aroused
        call nar(">Гермиона входит в твой кабинет.") 
        call her_main("Может, вы хотя бы будете предупреждать меня?","open","suspicious") 
        m "Ну, это уберет весь интерес, не так ли?"
        call her_main("Хмммм, ну хотя бы спрашивайте, что я буду делать, прежде чем вы дадите мне очередное зелье.","open","worriedL") 
        m "Зачем? У тебя разве было что то важное сегодня?"
        call her_main("Я должна была выступить с речью на собрании!","angry","worried") 
        call her_main("Есть ли у вас хоть какие-либо представления о том, насколько было неуместно высказывание о нравственности перед всем классом,...","open","closed") 
        call her_main("{size=+5}Когда моя одежда стала прозрачной!{/size}","angry","worried") 
        m "Я думаю, это зависит от того, какую сторону морали ты поддерживала."
        call her_main("Это не имеет значения.","open","closed") 
        m "Ты уверена, что тебе это не понравилось?"
        call her_main("Нет конечно... Я стояла там, на виду у своих друзей и сверстников и они видели меня обнаженной...","annoyed","suspicious") 
        m "Ты закончила свою речь?"
        call her_main("Конечно, должна же я была убедиться, что все понимают мои взгляды на мораль.","soft","base") 
        m "Ну, я уверен, что теперь у них кристально-чистое представление об этом."
        call her_main("Хммм, вы закончили?","annoyed","angryL") 
        m "Да, ты можешь идти."
        call her_main("До свидания, [genie_name].","open","base") 
        
    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        call nar(">Гермиона небрежно входит в кабинет.") 
        m "Привет, [hermione_name], как день прошел?"
        call her_main("Хорошо, [genie_name]. Почему вы спрашиваете?","base","base") 
        m "Просто так, ничего необычно сегодня не происходило?"
        call her_main("Хмммм, теперь, когда вы упомянули об этом, я вспомнила, что мальчики в классе немного странно себя вели, не так, как обычно.","open","worriedL") 
        m "Почему?"
        call her_main("Ничего серьезного, они просто трогали меня.","soft","baseL") 
        m "Трогали? Что могло их спровоцировать на это?"
        call her_main("Я не знаю, [genie_name]. Я даже не могу представить такую причину.","base","base") 
        m "Ну и как, ты справляешься?"
        call her_main("...","smile","baseL") 
        call her_main("Моя жизнь уже не станет прежней. Все глаза были устремлены на меня. Каждый в своем воображении делал со мной...","soft","ahegao") 
        call her_main("Но Снейп заставил меня выйти из класса после нашего с ним разговора.","base","down") 
        call her_main("Мне кажется, что я просто получала оргазм от взглядов.","grin","dead") 
        m "Очень хорошо, [hermione_name]. Ты определенно становишься шлюхой."
        call her_main("Спасибо, [genie_name]. Это все?","base","glance") 
        m "Да, ты можешь идти, шлюшка."
        call her_main("{image=textheart}","smile","baseL") 
        
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    $ transparency = 1
    call update_her_uniform 
    
    call her_walk("mid","leave",2) 
    
    $ hermione_sleeping = True
    jump night_main_menu
    
    
    