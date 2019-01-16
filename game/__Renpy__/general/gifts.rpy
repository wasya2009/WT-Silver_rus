init python:
    
    class silver_item(object):
        cost = 0
        name = ""
        image = ""
        description = ""
    
    class gift_item(silver_item):
        id = 0
        whoringNeeded = 0
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def costOf(self, number_of_item):
            return self.cost * number_of_item
    
label __init_variables:
    
    
    # $ gift_list = []
    
    # gift_list.append(cost=20, name="Lollipop candy", users=["hermione"],
        # description="A lollipop candy. An adult candy for kids or kids candy for adults?")
    
    # gift_list.append(cost=40, name="Chocolate",
        # description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
    
    # gift_list.append(cost=35, name="Plush owl",
        # description="a Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
    
    # gift_list.append(cost=50, name="Butterbeer", whoringNeeded=3,
        # description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
    
    # gift_list.append(cost=30, name="Educational magazines",
        # description="Educational magazines. \nthe Trusty companions of every social outcast.")
    
    # gift_list.append(cost=45, name="Girly magazines",
        # description="Girly magazines. \nAll cool girls are reading these.")
    
    # gift_list.append(cost=60, name="Adult magazines",
        # description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
    
    # gift_list.append(cost=80, name="Porn magazines", whoringNeeded=3,
        # description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
    
    # gift_list.append(cost=25, name="Viktor Krum Poster",
        # description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
    
    # gift_list.append(cost=75, name="Sexy lingerie",
        # description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
    
    # gift_list.append(cost=50, name="A pack of condoms", whoringNeeded=3,
        # description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
    
    # gift_list.append(cost=55, name="Vibrator", whoringNeeded=3,
        # description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
    
    # gift_list.append(cost=60, name="Jar of anal lubricant",
        # description="A Jar of anal lube, Buy this for your loved one - show that you care.")
    
    # gift_list.append(cost=70, name="Ball gag and cuffs",
        # description="Ball gag and cuffs, Turn your soulmate into your cellmate.")

    # gift_list.append(cost=85, name="Anal plugs", whoringNeeded=3,
        # description="Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike.")

    # gift_list.append(cost=200, name="Thestral Strap-on", whoringNeeded=3,
        # description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")

    # gift_list.append(cost=500, name="Lady Speed Stick-2000",
        # description="The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")

    # gift_list.append(cost=350, name="Sex doll \"Joanne\"",
        # description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
               
                                                                                                                         
                         
                           
             
                    
                                      
                                             
                                       

    # gift_list.append(cost=65, name="Anal beads",image="images/store/gift_anal_beads.png",
        # description="Anal beads engraved with a strange inscription \"Property of L.C.\".")
    
    
    if not hasattr(renpy.store,'Lollipop'): #important!
        $ Lollipop = gift_item()
    $ Lollipop.id = 0
    $ Lollipop.cost = 20
    $ Lollipop.name = "Леденец на палочке"
    $ Lollipop.image = "images/store/gifts/1.png"
    $ Lollipop.description = "Леденец на палочке. Взрослые Конфеты для детей или детские конфеты для взрослых?"
    
    
    if not hasattr(renpy.store,'Chocolate'): #important!
        $ Chocolate = gift_item()
    $ Chocolate.id = 1
    $ Chocolate.cost = 40
    $ Chocolate.name = "Шоколад"
    $ Chocolate.image = "images/store/gifts/2.png"
    $ Chocolate.description = "Рецепт этого вкусного молочного шоколада держится в секрете. (по слухам, содержит сушеных фей)."
    
    if not hasattr(renpy.store,'PlushOwl'): #important!
        $ PlushOwl = gift_item()
    $ PlushOwl.id = 2
    $ PlushOwl.cost = 35
    $ PlushOwl.name = "Плюшевая сова"
    $ PlushOwl.image = "images/store/gifts/3.png"
    $ PlushOwl.description = "Игрушечная сова, набитая перьями настоящей совы. Это так мило!"
    
    if not hasattr(renpy.store,'Butterbeer'): #important!
        $ Butterbeer = gift_item()
    $ Butterbeer.id = 3
    $ Butterbeer.cost = 50
    $ Butterbeer.whoringNeeded = 3
    $ Butterbeer.name = "Сливочное пиво"
    $ Butterbeer.image = "images/store/gifts/4.png"
    $ Butterbeer.description = "Девушки не могут устоять перед маслянистой текстурой этого напитка.{size=-3} Поэтому он всегда пользуется большим спросом у мальчиков. \n{size=-4}Предупреждение: несовершеннолетним не разрешается пить, без присутствия взрослых.{/size}"
    
    if not hasattr(renpy.store,'EducationalMagazines'): #important!
        $ EducationalMagazines = gift_item()
    $ EducationalMagazines.id = 4
    $ EducationalMagazines.cost = 30
    $ EducationalMagazines.name = "Образовательные журналы"
    $ EducationalMagazines.image = "images/store/gifts/5.png"
    $ EducationalMagazines.description = "Образовательные журналы \n{size=-2}Верные спутники, каждого социального изгоя.{/size}"
    
    if not hasattr(renpy.store,'GirlyMagazines'): #important!
        $ GirlyMagazines = gift_item()
    $ GirlyMagazines.id = 5
    $ GirlyMagazines.cost = 45
    $ GirlyMagazines.name = "Журналы про гламур"
    $ GirlyMagazines.image = "images/store/gifts/6.png"
    $ GirlyMagazines.description = "Девчачий журнал. \n{size=-2}Все классные девчонки читают его.{/size}"
    
    if not hasattr(renpy.store,'AdultMagazines'): #important!
        $ AdultMagazines = gift_item()
    $ AdultMagazines.id = 6
    $ AdultMagazines.cost = 60
    $ AdultMagazines.name = "Журналы для Взрослых(эротика)"
    $ AdultMagazines.image = "images/store/gifts/7.png"
    $ AdultMagazines.description = "{size=-3}Твой парень превращается в милого? Ваш муж больше вас не оскорбляет? Все, что вы хотели знать об отношениях, любви и сексе. Главным образом о сексе.{/size}"
    
    if not hasattr(renpy.store,'PornMagazines'): #important!
        $ PornMagazines = gift_item()
    $ PornMagazines.id = 7
    $ PornMagazines.cost = 80
    $ PornMagazines.whoringNeeded = 3
    $ PornMagazines.name = "Порно Журналы"
    $ PornMagazines.image = "images/store/gifts/8.png"
    $ PornMagazines.description = "{size=-3}Дайте их своей девушке, чтобы проверить ее. Вашей жене, чтобы пристыдить ее или вашей дочери, чтобы избежать сложного \"разговора\".{/size}"
    
    if not hasattr(renpy.store,'ViktorKrumPoster'): #important!
        $ ViktorKrumPoster = gift_item()
    $ ViktorKrumPoster.id = 8
    $ ViktorKrumPoster.cost = 25 #placeholder number
    $ ViktorKrumPoster.name = "Плакат Виктора Крама"
    $ ViktorKrumPoster.image = "images/store/gifts/9.png"
    $ ViktorKrumPoster.description = "{size=-3}Опытный ловец Квиддича, Виктор был выбран, чтобы играть за болгарскую национальную команду по Квиддичу, несмотря на то, что он все еще ходит в школу, его широко рассматривают, как одного из лучших игроков в мире.{/size}"
    
    if not hasattr(renpy.store,'SexyLingerie'): #important!
        $ SexyLingerie = gift_item()
    $ SexyLingerie.id = 9
    $ SexyLingerie.cost = 75 #placeholder number
    $ SexyLingerie.name = "Сексуальное белье"
    $ SexyLingerie.image = "images/store/gifts/10.png"
    $ SexyLingerie.description = "{size=-3}Сексуальное белье \"Добрая фея\". Очаруйте вашего волшебника в постели, или императрицу со своими сестрами в шабаш.{/size}"
    
    if not hasattr(renpy.store,'PackOfCondoms'): #important!
        $ PackOfCondoms = gift_item()
    $ PackOfCondoms.id = 10
    $ PackOfCondoms.cost = 50
    $ PackOfCondoms.whoringNeeded = 3
    $ PackOfCondoms.name = "Пачка презервативов"
    $ PackOfCondoms.image = "images/store/gifts/11.png"
    $ PackOfCondoms.description = "Презервативы \"Розовый единорог\". \nРаскройте однорогого зверя!\n{size=-4}Может содержать следы слюны единорога.{/size}"
    
    if not hasattr(renpy.store,'Vibrator'): #important!
        $ Vibrator = gift_item()
    $ Vibrator.id = 11
    $ Vibrator.cost = 55
    $ Vibrator.whoringNeeded = 3
    $ Vibrator.name = "Вибратор"
    $ Vibrator.image = "images/store/gifts/12.png"
    $ Vibrator.description = "{size=-3}Великолепный, магически усиленный вибратор, сделанный из виноградной лозы, с ядром из сердца дракона.{/size}"
    
    if not hasattr(renpy.store,'JarOfLube'): #important!
        $ JarOfLube = gift_item()
    $ JarOfLube.id = 12
    $ JarOfLube.cost = 60
    $ JarOfLube.name = "Банка анальной смазки"
    $ JarOfLube.image = "images/store/gifts/13.png"
    $ JarOfLube.description = "Баночка анальной смазки,{size=-3} купи это для любимого партнера - покажи, что тебе не все равно.{/size}"
    
    if not hasattr(renpy.store,'BallGagAndCuffs'): #important!
        $ BallGagAndCuffs = gift_item()
    $ BallGagAndCuffs.id = 13
    $ BallGagAndCuffs.cost = 70
    $ BallGagAndCuffs.name = "Кляп и наручники"
    $ BallGagAndCuffs.image = "images/store/gifts/14.png"
    $ BallGagAndCuffs.description = "Кляп и наручники,{size=-3} превратите свою вторую половинку в своего сокамерника.{/size}"
    
    if not hasattr(renpy.store,'AnalPlugs'): #important!
        $ AnalPlugs = gift_item()
    $ AnalPlugs.id = 14
    $ AnalPlugs.cost = 85
    $ AnalPlugs.whoringNeeded = 3
    $ AnalPlugs.name = "Анальные пробки"
    $ AnalPlugs.image = "images/store/gifts/15.png"
    $ AnalPlugs.description = "Анальные пробки украшеные реальными хвостами. \n{size=-3}Размеры варьируются, чтобы удовлетворить как экспертов, так и начинающих практиков.{/size}"
    
    if not hasattr(renpy.store,'ThestralStrapon'): #important!
        $ ThestralStrapon = gift_item()
    $ ThestralStrapon.id = 15
    $ ThestralStrapon.cost = 200
    $ ThestralStrapon.whoringNeeded = 3
    $ ThestralStrapon.name = "Фестральный Страпон"
    $ ThestralStrapon.image = "images/store/gifts/16.png"
    $ ThestralStrapon.description = "Фестральный Страпон\n{size=-3}Когда ты его увидишь, ты будешь срать кирпичами.{/size}"
    
    if not hasattr(renpy.store,'SpeedStick2000'): #important!
        $ SpeedStick2000 = gift_item()
    $ SpeedStick2000.id = 16
    $ SpeedStick2000.cost = 500
    $ SpeedStick2000.name = "Lady Speed Stick-2000"
    $ SpeedStick2000.image = "images/store/gifts/17.png"
    $ SpeedStick2000.description = "\"Женская Скоростная Метла-2000\", {size=-5}изящный способ транспортировки для влюбленных ведьм. Седло известной торговой марки гарантирует полное удовлетворение. Подарите ее для своей ведьмы, и она больше никогда не будет использовать свою старую и скучную метлу!{/size}"
    
    if not hasattr(renpy.store,'SexDollJoanne'): #important!
        $ SexDollJoanne = gift_item()
    $ SexDollJoanne.id = 17
    $ SexDollJoanne.cost = 350
    $ SexDollJoanne.name = "Секс-кукла \"Джоан\""
    $ SexDollJoanne.image = "images/store/gifts/18.png"
    $ SexDollJoanne.description = "Секс-кукла \"Джоан Роулинг\"... {size=-3}Она настолько реалистична. Выглядит почти как настоящий человек под воздействием какого-то заклинания.{/size}"
    
    if not hasattr(renpy.store,'AnalBeads'): #important!
        $ AnalBeads = gift_item()
    $ AnalBeads.id = 18
    $ AnalBeads.cost = 65 #placeholder number
    $ AnalBeads.name = "Анальные шарики"
    $ AnalBeads.image = "images/store/gift_anal_beads.png"
    $ AnalBeads.description = "Анальные шарики {size=-3}с выгравированной странной надписью \"Properti of L.C.\".{/size}"
    
    
    $ gift_list = []
    $ gift_list.append(Lollipop)
    $ gift_list.append(Chocolate)
    $ gift_list.append(PlushOwl)
    $ gift_list.append(Butterbeer)
    $ gift_list.append(EducationalMagazines)
    $ gift_list.append(GirlyMagazines)
    $ gift_list.append(AdultMagazines)
    $ gift_list.append(PornMagazines)
    $ gift_list.append(ViktorKrumPoster)
    $ gift_list.append(SexyLingerie)
    $ gift_list.append(PackOfCondoms)
    $ gift_list.append(Vibrator)
    $ gift_list.append(JarOfLube)
    $ gift_list.append(BallGagAndCuffs)
    $ gift_list.append(AnalPlugs)
    $ gift_list.append(ThestralStrapon)
    $ gift_list.append(SpeedStick2000)
    #$ gift_list.append(SexDollJoanne)
    #$ gift_list.append(AnalBeads)
    
    return

label happy(sub_mad = 0):
    hide screen hermione_main
    with d3
    $ mad -= sub_mad
    if mad <= 0:
        $ mad = 0
    if mad == 0:
        ">Настроение Гермионы улучшилось...\n>Гермиона {size=+5}не расстроена{/size} тобой..."
    else:
        ">Настроение Гермионы улучшилось...\n>Гермиона {size=+5}все еще расстроена{/size} тобой..."
    return

label no_change:
    hide screen hermione_main
    with d3  
    ">Настроение Гермионы не сильно изменилось..."
    return

label upset(add_mad):
    hide screen hermione_main
    with d3
    $ mad += add_mad
    ">Настроение Гермионы ухудшилось...\n>Гермиона {size=+5}расстроена{/size} тобой..."
    return
    
label her_gift_menu:
    python:
        choices = []
        for i in gift_list:
            if gift_item_inv[i.id] > 0:
                choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
        
        choices.append(("-Неважно-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump day_time_requests
    else:
        call give_her_gift(result) 
    
label give_her_gift(gift_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if gift_id == 0:#candy
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Леденец?","base","base") 
            call give_gift(">Ты отдаешь конфету Гермионе....",gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(5) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Конфета?","normal","base") 
            call her_main("Конфеты для детей, [genie_name].","open","base") 
            call give_gift(">Ты отдаешь конфету Гермионе....",gift_id) 
            call her_main("Спасибо...","annoyed","worriedL") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Конфета?","normal","base") 
            call give_gift(">Ты отдаешь конфету Гермионе....",gift_id) 
            call her_main("Эмм... Конечно, спасибо...","open","suspicious") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("Леденец?","base","base") 
            call her_main("Умные девушки используют конфеты, как \"оружие\".","smile","baseL") 
            call give_gift(">Ты отдаешь конфету Гермионе....",gift_id) 
            call her_main("Спасибо, [genie_name].","base","happyCl") 
            call happy(5) 
            $ h_body = "body_128"
    if gift_id == 1:#chocolate
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Плитка шоколада?","base","base") 
            call give_gift(">Ты отдаешь шоколадку Гермионе....", gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Плитка шоколада?","normal","base") 
            call her_main("Хм...","annoyed","frown") 
            call her_main("Она с феями...") 
            call her_main("Это шутка такая, да?","open","worried") 
            call give_gift(">Ты отдаешь шоколад Гермионе....", gift_id) 
            call her_main("Спасибо...","soft","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Плитка шоколада?","normal","base") 
            call her_main("Мне нравится, как она хрустит, [genie_name]! Н-но вкус...","grin","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь шоколадку Гермионе....", gift_id) 
            call her_main("Эмм... Спасибо...","base","base") 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("Плитка шоколада?","base","base") 
            call her_main("Вы меня балуете, [genie_name].","smile","angry") 
            call give_gift(">Ты отдаешь шоколадку Гермионе....", gift_id) 
            call her_main("Спасибо.","base","suspicious") 
            call happy(10) 
    if gift_id == 2:#plush owl
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Чучело совы?","base","base") 
            call her_main("Это так мило...","base","base") 
            call give_gift(">Ты отдаешь сову Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(7) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Плюшевая игрушка?","open","worried") 
            call her_main("Мне нравится!","base","base") 
            call give_gift(">Ты отдаешь сову Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Игрушка?","base","base") 
            call her_main("Такие игрушки для детей, [genie_name].","open","base") 
            call her_main("Но я возьму ее...","annoyed","worriedL") 
            call give_gift(">Ты отдаешь сову Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("Это одна из тех игрушек для взрослых, не так ли?","disgust","glance") 
            call her_main("Там где-то должен быть переключатель или кнопка...","open","down") 
            call her_main("Для... вибрации или подобного?","base","down") 
            call her_main("Ох...?","open","squint",cheeks="blush") 
            call her_main("Так это действительно просто игрушка?") 
            call her_main("Какой стыд...","angry","down_raised") 
            call her_main("Я имею в виду, спасибо [genie_name].","angry","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь сову Гермионе...",gift_id) 
            $ h_body = "body_01"
            call happy(4) 
    if gift_id == 3:#butterbeer
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Сливочное пиво?","base","base") 
            call her_main("Вы уверены в этом, [genie_name]?","open","suspicious") 
            call her_main("Он содержит алкоголь, вы же знаете...","base","base") 
            call give_gift(">Ты отдаешь бутылочку Гермионе...",gift_id) 
            call her_main("Спасибо.","base","base") 
            call happy(3) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Сливочное пиво, [genie_name]?","open","worried") 
            call her_main("Я поделюсь с вами одним маленьким секретом, [genie_name]...","open","base") 
            call her_main("Я большая поклонница этого совершенно безвредного напитка.","base","base") 
            call give_gift(">Ты отдаешь бутылочку Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","base") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Сливочное пиво?","base","base") 
            call her_main("Спасибо, [genie_name].","grin","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь бутылочку Гермионе...",gift_id) 
            call her_main("Я выпью его с девочками позже.","base","base") 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("Сливочное пиво...?","base","base") 
            call her_main("Спасибо, [genie_name].","base","base") 
            call give_gift(">Ты отдаешь бутылочку Гермионе...",gift_id) 
            call her_main("Я выпью его позже с мальчиками.","base","base") 
            call her_main("Эээ... я хотела сказать, конечно с девочками.","open","baseL",cheeks="blush") 
            call happy(20) 
            $ h_body = "body_01"
    if gift_id == 4:#edu mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("\"Популярная магия\" журнал?","base","base") 
            call give_gift(">Ты отдаешь один учебный журнал Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name]!","base","base") 
            call her_main("Я использую эти знания для свего исследования!") 
            call happy(15) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Иногда я нахожу информацию в журналах, которую не могу найти в книгах...","base","base") 
            call give_gift(">Ты отдаешь один учебный журнал Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name]!","base","base") 
            call her_main("Я использую их для своих исследований!") 
            call happy(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Ой...","open","base") 
            call her_main("Да, я часто читала подобные журналы...","base","base") 
            call her_main("В последнее время не так много...","open","worriedL") 
            call give_gift(">Ты отдаешь один учебный журнал Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name]!","base","base") 
            call happy(3) 
        if whoring >= 18: # Lv 7+  
            call her_main("Эм...","open","worriedL") 
            call her_main("Честно говоря, такие журналы в последнее время для меня полностью утратили свою привлекательность ...","open","suspicious") 
            call her_main("Но я в любом случае приму его от вас, [genie_name].","open","worried") 
            call give_gift(">Ты отдаешь один учебный журнал Гермионе...",gift_id) 
            call her_main("Спасибо.","soft","baseL") 
            call no_change 
    if gift_id == 5:#girl mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Хм?","soft","base") 
            call her_main("Это своего рода пресса, которую оценила бы какая-нибудь \"Слизеринская\" проститутка.","annoyed","suspicious") 
            call her_main("Я выше таких глупых журналов, как этот, [genie_name].","open","closed") 
            call no_change 
            $ h_body = "body_01"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Я не читаю журналы такого характера, [genie_name]...","open","angryCl") 
            call her_main("................","soft","baseL") 
            call her_main("Но, полагаю, что могла бы посмотреть его, для вашего развлечения ...","open","angryCl") 
            call give_gift(">Ты отдаешь гламурный журнал для девочек Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name]!","open","suspicious") 
            call happy(5) 
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Мне стыдно признаваться, но...","open","worriedL") 
            call her_main("Я в последнее время очень люблю читать такие журналы...","grin","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь гламурный журнал для девочек Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","open","suspicious") 
            call happy(15) 
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("Последний выпуск \"Girlz\"?!","angry","wide") 
            call her_main("Я с нетерпением ждала новый выпуск!","grin","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь гламурный журнал для девочек Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","open","suspicious") 
            call happy(15) 
            $ h_body = "body_06"
    if gift_id == 6:#adult mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Это же..?","open","base") 
            call her_main("Журналы для взрослых, [genie_name]?","open","base") 
            call her_main("Получить их, от уважаемого волшебника вашего статуса?","annoyed","angryL") 
            call her_main("[genie_name], Конечно, вы могли бы найти более продуктивный способ провести свободное время.","disgust","glance") 
            call her_main("И я определенно не буду использовать их...","angry","angry") 
            call upset(7) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Журналы для взрослых?","angry","angry") 
            call her_main("[genie_name] Я не заинтересована в подобных вещах.","annoyed","angryL") 
            call her_main("Это по вашему подходящий подарок для одного из ваших студентов, [genie_name]?","angry","angry") 
            call upset(3) 
            $ h_body = "body_29"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Журналы для взрослых?","open","base") 
            call her_main("[genie_name], это такой неуместный подарок для девушки моего возраста...","angry","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь журнал для взрослых Гермионе...",gift_id) 
            call her_main("Я должна его выкинуть вместо вас...?","annoyed","annoyed") 
            call happy(8) 
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("Новый выпуск журнала \"L.o.v.e.\"!!!","smile","happyCl") 
            call her_main("Эээ.. я имею в виду, журнал для взрослых?","angry","wink") 
            call her_main("Это немного неуместно...") 
            call her_main("Но я возьму его...","base","happyCl") 
            call give_gift(">Ты отдаешь журнал для взрослых Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","happyCl") 
            call happy(15) 
    if gift_id == 7:#porn mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Хм... Что это?","base","base") 
            call her_main("[genie_name], это же порно журналы!","scream","wide") 
            call her_main("Какой позор, [genie_name]!","angry","angry",cheeks="blush") 
            call upset(15) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Порно журналы?","shock","wide") 
            call her_main("[genie_name], что вы предлагаете мне с ним делать?","open","down") 
            call her_main("Исследовать их?","annoyed","annoyed") 
            call her_main("Гадость!","scream","angry",emote="01") 
            call upset(8) 
            $ h_body = "body_120"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Это же жесткое порно, [genie_name]!","open","base") 
            call her_main("Это совершенно неподходящий подарок для девушки моего возраста!","angry","worriedCl",emote="05") 
            call her_main("..............","angry","down_raised") 
            call her_main("Но я возьму его...","angry","base") 
            call give_gift(">Ты отдаешь порно журнал Гермионе...",gift_id) 
            call her_main("И я выброшу их в мусорное ведро, где им и подобным девушкам самое место...","annoyed","annoyed") 
            call no_change 
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("Порнография?","shock","wide") 
            call her_main("................","angry","down_raised") 
            call her_main("Как женщины могут соглашаться на такие вещи, [genie_name]?","angry","base") 
            call her_main(".................","angry","down_raised") 
            call her_main("Хорошо, я возьму его...","upset","closed") 
            call her_main("Конечно исключительно в исследовательских целях...","open","baseL",cheeks="blush") 
            call give_gift(">Ты отдаешь порно журнал Гермионе...",gift_id) 
            call happy(15) 
            $ h_body = "body_45"
    if gift_id == 8:#krum poster
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Плакат по Квиддичу?","annoyed","down") 
            call her_main("Что мне с ним делать, [genie_name]?","annoyed","annoyed") 
            call her_main("Но, спасибо.","annoyed","closed") 
            call no_change 
            $ h_body = "body_71"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Плакат по Квиддичу?","annoyed","down") 
            call her_main("Хм...","annoyed","annoyed") 
            call her_main("Думаю, что видела этого игрока один или два раза...","annoyed","down") 
            call her_main("Он ведь студент из Дурмстранга, верно?","base","base") 
            call give_gift(">Ты отдаешь плакат Гермионе...",gift_id) 
            call happy(5) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Плакат с Виктором Крамом, [genie_name]?","annoyed","down") 
            call her_main("Не могу сказать, что меня волнует Квиддич, но...","open","suspicious") 
            call her_main("Я понимаю, почему девушки находят грубое телосложение некоторых игроков привлекательным...","open","down") 
            call give_gift(">Ты отдаешь плакат Гермионе...",gift_id) 
            call happy(15) 
        if whoring >= 18: # Lv 7+  
            call her_main("Постер Виктора Крама?!","scream","wide_stare") 
            call her_main("Спасибо, [genie_name]!","grin","worriedCl",emote="05") 
            call give_gift(">Ты отдаешь плакат Гермионе...",gift_id) 
            call her_main("Не могу дождаться, чтобы повесить его над своей кроватью!","smile","baseL") 
            call her_main("Девчонки позеленеют от зависти...","smile","glance") 
            call happy(25) 
    if gift_id == 9:#lingerie
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Нижнее белье?","angry","down_raised") 
            call her_main("[genie_name], я не могу принять от вас такой подарок...","upset","closed") 
            call upset(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Сексуальное белье?","angry","down_raised") 
            call her_main("Вы знаете, я не могу принять от вас такой подарок, [genie_name].","angry","base") 
            call her_main("(Хотя, оно довольно симпатичное).........","angry","down_raised") 
            call no_change 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Сексуальное белье?","base","down") 
            call her_main("[genie_name], это так неуместно...","angry","wink") 
            call give_gift(">Ты отдаешь белье Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","baseL",cheeks="blush") 
            call happy(7) 
        if whoring >= 18: # Lv 7+  
            call her_main("Сексуальное белье?","base","down") 
            call her_main("Как вы думаете, я стану похожа на одну из тех ведьм взрослых журналов, [genie_name]?","grin","dead") 
            call her_main("Ох... Я хотела сказать, спасибо, [genie_name].","angry","wink") 
            call give_gift(">Ты отдаешь белье Гермионе...",gift_id) 
            call happy(15) 
    if gift_id == 10:#condoms
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Презервативы?!","angry","wide") 
            call her_main("[genie_name], я даже не знаю, что мне с ними делать...","scream","angryCl") 
            call upset(6) 
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("...Презервативы?","normal","frown") 
            call her_main("Эм... Это часть новой программы сексуального воспитания в Хогвартсе, или что-то подобное?","open","angryCl") 
            call her_main("Нет, [genie_name]... Это неправильно, принимать от вас подобные вещи...","open","baseL",cheeks="blush") 
            call no_change 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Пачка презервативов?","normal","base") 
            call her_main("[genie_name], и как мне их использовать?") 
            call her_main("Ну, я приму их, просто потому, что отказываться от подарков очень грубо...","open","angryCl") 
            call give_gift(">Ты отдаешь пачку презервативов Гермионе...", gift_id) 
            call happy(3) 
            $ h_body = "body_29"
        if whoring >= 18: # Lv 7+
            call her_main("Пачка презервативов?","open","suspicious") 
            call her_main("Я ценю ваше беспокойство, [genie_name]. Благодарю вас.","base","glance") 
            call give_gift(">Ты отдаешь пачку презервативов Гермионе...", gift_id) 
            call happy(4) 
            $ h_body = "body_45"
    if gift_id == 11:#vibrator
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Волшебная палочка?","base","base") 
            call her_main("Нет, это похоже на--","soft","base") 
            call her_main(".........?") 
            call her_main("!!!","angry","wide") 
            call her_main("[genie_name]!","angry","angry",cheeks="blush") 
            call her_main("Это крайне неуместно!","scream","angryCl") 
            call upset(10) 
            $ h_body = "body_120"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Это именно то, о чем я думаю?","angry","down_raised") 
            call her_main("[genie_name], Позвольте вам напомнить, что я принадлежу к благородному факультету \"Гриффиндора\".","open","annoyed",cheeks="blush") 
            call her_main("А этот подарок был бы более подходящим для девушки из \"Слизерина\", [genie_name].","upset","closed") 
            call upset(10) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Это.... Вибратор?","angry","down_raised") 
            call her_main("Дизайн...") 
            call her_main("Он напоминает мне о моей палочке...") 
            call her_main("Вы делали его для меня на заказ, [genie_name]?","angry","down_raised") 
            call her_main("Это неуместно...","scream","angryCl") 
            call her_main("Но, я все равно возьму его...","annoyed","worriedL") 
            call give_gift(">Ты отдаешь вибратор Гермионе...",gift_id) 
            call no_change 
        if whoring >= 18: # Lv 7+  
            call her_main("Этот вибратор...","open","worried") 
            call her_main("Он... зовет меня...","open","worriedL") 
            call her_main("Но, не в непристойном смысле, [genie_name].","disgust","glance") 
            call give_gift(">Ты отдаешь вибратор Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","down") 
            call happy(10) 
    if gift_id == 12:#anal lube
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Я не знаю, что это...","open","base") 
            call her_main("У меня такое ощущение, что баночка полна чего-то мерзкого и пошлого...","angry","angry") 
            call her_main("Нет, благодарю, [genie_name].") 
            call upset(6) 
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Хм...","annoyed","down") 
            call her_main("Я догадываюсь, что это...","disgust","glance") 
            call her_main("Но, почему вы отдаете нечто подобное одному из своих студентов, [genie_name]?") 
            call her_main("Нет, благодарю.","annoyed","angryL") 
            call upset(2) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Анальная смазка?","angry","down_raised") 
            call her_main("Эм.. Ну... Я знаю одну девушку...","open","baseL",cheeks="blush") 
            call her_main("Я имею в виду, что я не знаю ее лично, она подруга моей подруги...") 
            call her_main("Да, я возьму это для нее...") 
            call give_gift(">Ты отдаешь баночку Гермионе...", gift_id, 0) 
            call her_main("Но, я считаю, что не стоит делать такие подарки своим студентам, [genie_name].","open","annoyed",cheeks="blush") 
            call no_change 
            $ h_body = "body_79"
        if whoring >= 18: # Lv 7+  
            call her_main("Анальная смазка, [genie_name]?","base","down") 
            call her_main("Я знаю пару девушек, готовых на все, ради такого подарка.","open","annoyed",cheeks="blush") 
            call her_main("Благодарю за заботу о нас, [genie_name].","base","glance") 
            call give_gift(">Ты отдаешь баночку Гермионе...", gift_id) 
            call happy(5) 
    if gift_id == 13:#gag and cuffs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Что это?","angry","down_raised") 
            call her_main("Это одна из тех игрушек для взрослых?","angry","suspicious",cheeks="blush") 
            call her_main("Какая женщина, в здравом уме, подвергнет себя такому унижению?","scream","angryCl") 
            call her_main("И, как мне использовать подобные вещи?","open","annoyed",cheeks="blush") 
            call her_main("Это просто оскорбительно, [genie_name]...","angry","angry",cheeks="blush") 
            call upset(10) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], Вы не понимаете, насколько неуместно было бы для меня принять подобный подарок?","open","annoyed",cheeks="blush") 
            call her_main("И, я даже не знаю, что мне с ним делать...","open","baseL",cheeks="blush") 
            call her_main("Я имею в виду, что эти пушистые штуки, вероятно, наручники...","angry","down_raised") 
            call her_main("Но, этот шар... Эм...") 
            call her_main("[genie_name], пожалуйста...","upset","closed") 
            call her_main("Просто, уберите их.") 
            call upset(5) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Месяц назад мне было бы обидно получить подобный подарок...","upset","closed") 
            call her_main("Но, теперь я знаю, что некоторые девушки действительно находят удовольствие в подобных игрушках...","angry","down_raised") 
            call her_main("Но, уверяю вас, я не одна из них, [genie_name].","upset","closed") 
            call her_main("Но, я знаю девушку, которая знает девушку, которая любит подобные штучки...","open","baseL",cheeks="blush") 
            call her_main("Да, я отдам это ей...","base","baseL",cheeks="blush") 
            call give_gift(">Ты отдаешь кляп и наручники Гермионе...",gift_id) 
            call happy(9) 
        if whoring >= 18: # Lv 7+  
            call her_main("Наручники с кляпом?","open","squint",cheeks="blush") 
            call her_main("Это совершенно неприлично, [genie_name].","angry","wink") # :)
            call her_main("Но, ведь подарок - есть подарок, верно?","base","suspicious") 
            call give_gift(">Ты отдаешь кляп и наручники Гермионе...",gift_id) 
            call happy(15) 
    if gift_id == 14:#anal plugs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Хм...?","base","base") 
            call her_main("Это вроде брелка для ключей?","soft","base") 
            call give_gift(">Ты отдаешь анальную пробку Гермионе...",gift_id) 
            call her_main("Благодарю вас, [genie_name].","annoyed","annoyed") 
            call happy(8) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], это какая-то игрушка для взрослых?","open","annoyed",cheeks="blush") 
            call her_main("Это что-то из анальных игрушек, не так ли?","angry","angry",cheeks="blush") 
            call her_main("[genie_name] это не что иное, как оружие для угнетения женщин!") 
            call her_main("Отвратительно!","upset","closed") 
            call upset(15) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Да, я знаю, что есть некие девушки...","upset","closed") 
            call her_main("Использующие подобные вещи...","open","annoyed",cheeks="blush") 
            call her_main("Но, я не из таких, [genie_name].") 
            call her_main("Нет, благодарю вас.","upset","closed") 
            call no_change 
        if whoring >= 18: # Lv 7+  
            call her_main("Анальная пробка?","angry","down_raised") 
            call her_main("Я не нуждаюсь в подобных вещах, [genie_name]...","angry","base") 
            call her_main("Они очень красивые...","angry","wink") 
            call her_main(".....................","angry","down_raised") 
            call her_main("Ну, хорошо... Я приму одну от вас, [genie_name], если так надо.","soft","ahegao") 
            call give_gift(">Ты отдаешь анальнкю пробку Гермионе...",gift_id) 
            call her_main("Но, конечно, я никогда не буду ее использовать...","open","closed") 
            call her_main("................","base","down") 
            call happy(10) 
    if gift_id == 15:#strap on
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Что это?","angry","wide") 
            call her_main("Это какой-то вид артефакта или трофея?","open","base") 
            call her_main("Такая хорошая обработка...","base","base") 
            call her_main("Вы уверены, что иметь такое, это нормально для меня, [genie_name]?","base","base") 
            call give_gift(">Ты отдаешь страпон Гермионе...",gift_id) 
            call her_main("Большое спасибо, [genie_name]. Я обещаю позаботиться о нем.","open","closed") 
            call happy(20) 
            $ h_body = "body_15"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("!!!","angry","wide") 
            call her_main("Это же...","angry","down_raised") 
            call her_main("Но, он даже не выглядит... человеческим...") 
            call her_main("Я имею в виду...","annoyed","angryL") 
            call her_main("[genie_name], вы потеряли стыд?!","scream","angry",emote="01") 
            call her_main("Преподнести подобную вещь ученику?!") 
            call her_main("..................","open","down") 
            call her_main("Пожалуйста, уберите его, [genie_name].","angry","angry") 
            call upset(15) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Эта штука...","angry","down_raised") 
            call her_main("Разве, это фактический размер... реальной \"штуки\"?","angry","base") 
            call her_main("Я имею в виду...","open","baseL",cheeks="blush") 
            call her_main(".......................","angry","down_raised") 
            call her_main("Это новый микрофон для собраний?","angry","base") 
            call her_main("Такая продуманность...","angry","down_raised") 
            call her_main("Я возьму его...","normal","worriedCl") 
            call give_gift(">Ты отдаешь страпон Гермионе...",gift_id) 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("Он... Он великолепен, [genie_name]...","shock","wide") 
            call her_main("Он и правда сделан по образу фестрала?","open","baseL",cheeks="blush") 
            call her_main("Но, ведь он невидимый...","open","squint",cheeks="blush") 
            call her_main("..................","angry","down_raised") 
            call her_main("Потрясающе...","grin","dead") 
            call her_main("Не так, как вы подумали, [genie_name]...","upset","closed") 
            call her_main("Просто, я восхищаюсь мастерством...","open","closed") 
            call give_gift(">Ты отдаешь страпон Гермионе...",gift_id) 
            call her_main("Спасибо за подарок, [genie_name].","base","suspicious") 
            call happy(30) 
    if gift_id == 16:#speed stick
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Метла...?","base","base") 
            call her_main("Хм...","normal","base") 
            call her_main("Что это за дурацкая штука к ней прилагается?","normal","frown") 
            call her_main("Это похоже на седло...?","open","suspicious") 
            call give_gift(">Ты отдаешь метлу Гермионе...",gift_id) 
            call her_main("Спасибо за подарок, [genie_name].","open","worried") 
            $ h_body = "body_06"
            call happy(20) 
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Метла..?","base","base") 
            call her_main("Хмм...","normal","frown") 
            call her_main("Это какая-то секс-игрушка, не так ли?","angry","angry") 
            call her_main("Но, она так хорошо изготовлена...","open","down") 
            call give_gift(">Ты отдаешь страпон Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","upset","closed") 
            call happy(20) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Метла...?","angry","down_raised") 
            call her_main("Хм...") 
            call her_main("Это какое-то седло...?","disgust","glance") 
            call her_main("Ну, не важно.","open","closed") 
            call her_main("Отказываться от такого дорогого подарка было бы грубо...") 
            call give_gift(">Ты отдаешь метлу Гермионе...",gift_id) 
            call her_main("Благодарю вас, [genie_name].","upset","closed") 
            call happy(30) 
        if whoring >= 18: # Lv 7+  
            call her_main("Метла...","base","down") 
            call her_main("Хм...") 
            call her_main("Это седло, [genie_name]...","open","baseL",cheeks="blush") 
            call her_main("Оно было разработанно специально для ведьм, не так ли?","open","squint",cheeks="blush") 
            call her_main("Я не уверена, является ли это неприличным или умным...","annoyed","annoyed") 
            call her_main("Но, это гениальное произведение инженерного искусства, не так ли...","base","suspicious") 
            call give_gift(">Ты отдаешь метлу Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","glance") 
            call happy(30) 
    if gift_id == 17:#sex doll
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Это...","shock","wide") 
            call her_main("Секс-кукла?!","angry","worriedCl",emote="05") 
            call her_main("[genie_name]!!!","scream","worriedCl") 
            call upset(20) 
            $ h_body = "body_33"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Секс-кукла?","shock","wide") 
            call her_main("Это так неприлично для такого волшебника, как вы, [genie_name]...","upset","closed") 
            call upset(20) 
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Секс-кукла...","angry","down_raised") 
            call her_main("Это немного неуместно...","upset","closed") 
            call her_main("Но, может быть, мы могли бы использовать ее для розыгрыша, или чего-то подобного...","base","down") 
            call give_gift(">Ты отдаешь надувную куклу Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","down") 
            call happy(10) 
        if whoring >= 18: # Lv 7+  
            call her_main("Это секс-кукла Джоаны?","annoyed","down") 
            call her_main("Не могу сказать, что одобряю этого...","open","baseL",cheeks="blush") 
            call her_main("Но, я знаю, что Гарри хотел бы ее попробовать...","base","down") 
            call give_gift(">Ты отдаешь надувную куклу Гермионе...",gift_id) 
            call her_main("Спасибо, [genie_name].","base","baseL",cheeks="blush") 
            call happy(30) 
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    show screen hermione_main
    with d3
    return
    
label give_gift(text = "", gift = 0):
    hide screen hermione_main
    with d3
    # note that gift is the index (starting with 0), while the image
    # files are starting with/off by 1!
    $ the_gift = "images/store/gifts/"+str(gift+1)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift_item_inv[gift] -= 1
    return
    
    
###GIVING CLOTHING RESPONSES
label giving_gryffindor_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("Костюм болельщицы?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">Ты отдаешь костюм Гермионе...\n>Костюм болельщицы Гриффендора был добавлен в гардероб."
    hide screen gift
    call her_main("Благодарю вас, [genie_name], хотя я и не знаю, когда его одену.","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_slytherin_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("Костюм болельщицы..? Слизерина?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">Ты отдаешь костюм Гермионе...\n>Костюм болельщицы Слизерина был добавлен в гардероб."
    hide screen gift
    call her_main("Благодарю вас, [genie_name], даже если я и не из Слизерина...","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_maid_outfit:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    $ nets = 7 # Means already gifted.
    call her_main("Костюм горничной?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">Ты отдаешь костюм Гермионе...\n>Костюм горничной был добавлен в гардероб."
    hide screen gift
    call her_main("Благодарю вас, [genie_name].","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    

label giving_silk_nightgown:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("Ночная рубашка?","normal","base",xpos=140) 
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png"# blue box
    show screen gift
    with d3
    ">Ты отдал ночную рубашку Гермионе...\n>В гардероб добавлена шелковая сорочка."
    hide screen gift
    call her_main("Спасибо, [genie_name].","open","angryCl") 
    call happy 
    
    call her_main("","normal","base",xpos=370) 
    jump day_time_requests    
    
    
label giving_skirt:
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    m "Вот... Это тебе..."
    $ the_gift = "images/store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Ты дал нано-юбку Гермионе..."
    hide screen gift
    with d3
    hide screen hermione_main
    with d3
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    call her_main("Хм...? Что это?","base","base") 
    call her_main("Юбка?","open","worried") 
    call her_main("Спасибо, [genie_name].","base","base") 
    #her "Thank you professor."
    m "Не стоит благодарности."
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
                      
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "body_01"
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    jump day_time_requests
    
### DRESS CODE ###

label mini_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("Вы же не всерьез, [genie_name]!","open","angryCl") 
        her "Такая короткая юбка?!"
        call her_main("...Она же почти ничего не скрывает, [genie_name].","annoyed","annoyed") 
                                                  
                                                    
        menu:
            m "..."
            "\"Прекрасно. Забудь об этом.\"":
                call her_main("С удовольствием...","disgust","glance") 
                jump day_time_requests
                 

                                             
                                       
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("Ну, ладно...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset 
        
        



    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Хм...?","soft","base") 
        call her_main("Но, она такая короткая...","annoyed","suspicious") 
                                                  
                                                        
        menu:
            m "..."
            "\"Просто надень ее!\"":
                call her_main("[genie_name] этот наряд едва ли подходит для студентки Хогвартса.","normal","frown") 
                call her_main("Я отказываюсь!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                                   
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                call her_main("Хм...","normal","frown") 
                call her_main("Ну, в таком случае...","open","suspicious") 
                call her_main("Пока это приносит пользу моему факультету...","annoyed","worriedL") 
            "\"Отлично. Забудь об этом\"":
                call her_main("Хорошо...","base","base") 
                jump day_time_requests
                      
                                                                                                           
                  
                                                                                      
                                       

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Хм...?","soft","base") 
        call her_main("Но, она такая короткая...","annoyed","suspicious") 
                                                  
                                                        
        menu:
            m "..."
            "\"Просто надень ее!\"":
                call her_main("Хорошо, хорошо...","annoyed","angryL") 
                                               
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                call her_main("Хм...","normal","frown") 
                call her_main("Хорошо, тогда я не возражаю.","grin","baseL") 
                                                                                                           
                                                       
            "\"Прекрасно. Забудь\"":
                call her_main("Ох...","soft","baseL") 
                jump day_time_requests
        
                                       


    

    if whoring >= 18: # Lv 7+
        call her_main("Конечно, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_02 = True
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    

label mini_off:
                   
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("Я рада, что вы пришли в чувство, [genie_name].","open","angryCl") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("С удовольствием, [genie_name].","base","base") 

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Хорошо...","soft","baseL") 
    
    if whoring >= 18: # Lv 7+
        call her_main("Снова эта скучная вещица?","angry","worried") 
    
    
    $ legs_02 = False
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
label tiny_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("Вы не можете на полном серьезе предлагать такое, [genie_name]!","open","angryCl") 
        her "Эта юбка СОВЕРШЕННО короткая?!"
        call her_main("...Она ничего не скрывает, [genie_name].","annoyed","annoyed") 
        menu:
            m "..."
            "\"Прекрасно. Забудь.\"":
                call her_main("С радостью...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                her "........................"
                her "..............................."
                call her_main("Ну, хорошо...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset 
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Хм...?","soft","base") 
        call her_main("Но, она такая короткая...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Просто, надень ее!\"":
                call her_main("[genie_name] вряд ли это подходящий наряд для студентки Хогвартса.","normal","frown") 
                call her_main("Я отказываюсь!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 35 очков.\"":
                $ gryffindor +=35
                call her_main("Хм...","normal","frown") 
                call her_main("Ну, в таком случае...","open","suspicious") 
                call her_main("Пока это приносит пользу моему факультету...","annoyed","worriedL") 
            "\"Прекрасно. Забудь.\"":
                call her_main("Ладно...","base","base") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Хм...?","soft","base") 
        call her_main("Но, она тааакая короткая...","annoyed","suspicious") 
        menu:
            m "..."
            "\"Просто надень ее!\"":
                call her_main("Ладно, ладно...","annoyed","angryL") 
            "\"Я дам тебе 10 очков.\"":
                $ gryffindor +=10
                call her_main("Хм...","normal","frown") 
                call her_main("Хорошо. Я ее надену.","grin","baseL") 
            "\"Прекрасно. Забудь.\"":
                call her_main("Ох...","soft","baseL") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Конечно, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_03 = True
    $ legs_02 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label give_glasses:
    call her_main("Но, мне не нужны очки...","base","base") 
    
    $ glasses_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label take_glasses:
    call her_main("Хотя, я пока просто привыкаю к ним.","base","base") 
    
    $ glasses_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    


label badge_put:
    call her_main("Конечно, [genie_name]...","base","base") 
    
    $ hermione_badges = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_off:
    call her_main("Это скучное старье? Хорошо.","open","suspicious") 
    
    $ wear_shirts = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_on:
    call her_main("Наконец, это было на стооолько скучно, так одеваться.","base","base") 
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_on:
    call her_main("Что, я не могу этого сделать, все назовут меня шлюхой!","angry","angry") 
    m "Просто сделай это."
    $ h_body = "body_30"
    her "[genie_name], это грань дозволенного. Я не собираюсь ходить без рубашки!"
    m "Я дам тебе 100 очков."
    her "200"
    m "Конечно, почему бы и нет?"
    her ".......... прекрасно"
    
    $ wear_shirts = False
    $ gryffindor +=200
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_off:
    call her_main("Ох, спасибо... Вы понятия не имеете, каково это было...","base","base") 
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label g_stockings_on:
    call her_main("Ok then","base","base") 
    
    $ stockings = 2
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label g_stockings_off:
    call her_main("Хорошо.","base","base") 
    
    $ stockings = 0
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_on:
    call her_main("Бюстгалтер?","base","base") 
    m "Я подумал, что тебе не помешает новый."
    her "Благодарю вас, [genie_name]."
    
    $ custom_bra = 1
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_off:
    call her_main("Хорошо.","base","base") 
    
    $ custom_bra = 0
    
                                          
                       

                                            

    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_on:
    call her_main("Вы хотите, что бы я надела его?","base","base") 
    m "Его никто не увидит."
    her "...прекрасно."
    
    $ custom_bra = 2
    
                                                  
                                                 
             
                   
                      
                                                                                                           
                                            
                                                                                      
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                                           
                 
                                   
                          

                                                  
                                                  
                      
                                                  
                                                               
                                                                              
             
                   
                                                    
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                            
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                    
                                                  
                                                
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       



                           
                                                   
                                                             
                          
                                              




                                           



    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_off:
    call her_main("В конце-концов, в нем не очень удобно.","base","base") 
    
    $ custom_bra = 0
    
                                                 
                                                  
                                                        
                          
                                              

                                                  
                                                  
                                                    

                                                   
                                                  
                        

                           
                                                  
                  


                                           


    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
















                       
                         
                   

                                                 
                           
                                                 
                                                
                                                  
                                                                                 
                       
                          
                  
                                              



                                                  
                           
                                                 
                     
                                                  
                                                    
                                                                                    
                                                  
                   
                          
                  


                                                   
                                                                    
                                                  
                         
                                                   
                                                         
                                                                                            
                                                    
                          
                                            
                        
               
                                                         
                        
               
                                                   
                                                                                                                         
                          
                      
                                                   

                           
                                                                    
                          
                                                  
                                                          
                                                   
                                                                                                                                 
                                                   
                                                                                        
                          
                  

                   
                                 
                           




label silk_on:
    call her_main("Вы хотите, что бы я сменила лифчик?","base","base") 
                   

                                                 
                           
                                                 
                    
                                                  
                                                                                   
                          
                  
                                              


                                                  
                                                 
                     
                                                  
                                                                                                                                                                             
                                                   
                                                                                                                   
                          
                      


                                                   
                                                                    
                           
                                                 
                          
                                            
                                                  
                                                                                                                
                          
                                            
                        
               
                                                        
                        
               
                  
                                              



                           
                                                                    
                          
                                                 
                          
                                                   
                                                
                          
                                            
                        
               
                                                        
                        
               
                  
                                              

                   
                                 
                           



                     
                                     
                                                                                                                     
                                                                                                                                                                                                                                                                                           
         
                                   
                                            
                    
                                                                                                                                                               
                                            
                   
                                                                                                                                                         
                                                                                                                
                                                                                                                                               
                                                                                                                                                     
                                                                                                                      
                                                              
             
                                                                                                                 
             
                                                                 
                                                                
                                                                                                            
                                                                                      
                                                                                                                 
                          
                                              


                    
                            

                   
                                 
                           





                   
                         
                   

                                                 
                           
                                                                    
                                                 
    her "Тогда ладно."
    
    $ custom_bra = 3
    
               
                                                             
                        
               
                                              
                   
                  

                                                  
                           
                                                                    
                                                 
                             
                                                  
                                                       
                          
                                            
                        
               
                                                             
                        
               
                                              
                   
                  
                                              



                                                   
                           
                                                                    
                                                 
                             
                          
                                            
                        
               
                                                             
                        
               
                                              
                                                      
                  
                                              

                           
                                                                    
                          
                                                 
                             
                                                  
                                                                             
                          
                                            
                        
               
                                                             
                        
               
                                              
                   
                  
                                               

                   
                                 
                           






                       
                         
                   

                                                 
                            
                                                                    
                                                 
                      
                          
                                            
                        
               
                                                   
                        
               
                                              
                   
                  

                                                  
                            
                                                                    
                                                 
                      
                                                  
                     
                        
                                                  
                                            
                          
                                            
                        
               
                                                   
                        
               
                                              
                   
                  



                                                   
                            
                                                                    
                                                 
                      
                                                  
                                                                                 
                          
                                            
                        
               
                                                   
                        
               
                                              
                                                       
                  



                           
                                                                    
                            
                                                 
                      
                                                   
                                                   
                          
                                            
                        
               
                                                   
                        
               
                                               
                  
                  


                   
                                 
                           



                      
                         
                   

                                                 
                            
                                                 
                         
                                                  
                        
                        
                                                  
                 
                                                   
                         
                                                  
                    
                  
                                               

                                                  
                            
                                                  
                        
                                                   
                                                                                                                            
                                                   
                                                                                                            
                  

                                                   
                                                                    
                                                  
                    
                             
                                                
                                                   
                                              
                                                  
                    
                                                  
                       
                          
                                            
                        
               
                                                               
                        
               
                      


                           
                                                                    
                            
                                                 
                    
                                                  
                                                       
                                                  
                        
                          
                                            
                        
               
                                                               
                        
               
                                               
                   
                          
                  


                   
                                 
                           
















                     
                         
                   
                                                 
                            
                                                                    
                                                 
                            
                                                  
                        
                                                  
                                                     
                                                  
                                                          
                          
                                            
                        
               
                                                             
                        
               
                                              
                                                                                       
                          
                  
                                              


                                                  
                            
                                                 
                 
                                                   
                       
                                                   
                                                  
                              
                                                  
                        
                                                    
                                                  
                                
                                                  
                                                          
                          
                  

                                                   
                                                                    
                            
                                                  
                 
                                                   
                                                     
                                                   
                    
                                                   
                                     
                                                   
                                                       
                                                   
                          
                                                  
                    
                          
                                            
                        
               
                                                             
                        
               
                  


                           
                                                                    
                            
                                                 
                                                                
                                                   
                                                           
                                                   
                                                              
                                                   
                                
                                                   
                     
                                                   
                                                        
                                                   
                                               
                          
                                            
                        
               
                                                             
                        
               
                                               
                                                                
                          
                  


                   
                                 
                           







                     
                         
                   

                                                 
                            
                                                  
                            
                                                   
                                                             
                                                  
                                                                                                             
                                                   
                                                          
                                                   
                                                       
                  

                                                  
                           
                                                  
                                                                                                                                                    
                                                   
                                                                            
                                                   
                                                                                               
                                                            
                                                   
                       
                         
                  


                                                   
                                                                    
                           
                                                  
                                                                                                                                 
                                                   
                                                                                                                       
                                                   
                                                   
                                                   
                                                   
                                                                                                                
                                                   
                                                                
                          
                                            
                        
               
                                                    
                        
               
                  

                           
                                                                    
                            
                                                  
                       
                                                   
                                              
                                                   
                                                                 
                          
                                            
                        
               
                                                    
                        
               
                  



                   
                                 
                           















                  
                         
                   

                                                 
                           
                                                                    
                                                 
                      
                                                  
                                                           
                          
                                            
                        
               
                                                   
                        
               
                                                   
                   
                  


                                                  
                            
                                                  
                                                        
                                                   
                                                        
                                                                                                                
                                                   
                         
                  


                                                   
                                                  
                                                                 
                                                   
                                            
                  
                                                   
                   
                      

                           
                                                                    
                            
                                                  
                      
                                                   
                                                      
                                                   
                                                          
                                                   
                                   
                                                   
                                                             
                          
                                            
                        
               
                                                   
                        
               
                                               
                                                                                        
                                                   
                              
                  



                   
                                 
                           








                  
                         
                   

                                                 
                            
                                                                    
                                                 
                                                  
                          
                                            
                        
               
                                                                            
                        
               
                                              
                   
                                                        
                  

                                                  
                            
                                                                    
                                                 
                                                                                                                   
                          
                                            
                        
               
                                                                            
                        
               
                                              
                   
                                                        
                  

                                                   
                           
                                                                    
                                                 
                     
                                                  
                                                        
                                                  
                                                    
                          
                                            
                        
               
                                                                            
                        
               
                                              
                   
                  


                           
                                                                    
                                                 
                     
                                                  
                                                                                         
                                                  
                                                
                          
                                            
                        
               
                                                                            
                        
               
                                              
                  
                      


                   
                 
                           






                  
                         
                   

                                                 
                                                 
                   
                                                  
                                                                                                                      
                                                  
                                                  
                      
                                              



                                                  
                           
                                                                    
                                                 
                                                
                                                  
                              
                                                  
                                                                                          
                          
                                            
                        
               
                                                   
                        
               
                                              
                   
                  
                                              

                                                   
                            
                                                                    
                                                 
                                             
                                                  
                                                                                                
                          
                                            
    show screen blkfade
               
                                                   
                        
               
                                              
                   
                  
                                              


                           
                                                                    
                            
                                                 
                                              
                                                  
                                                
                          
                                            
                        
               
                                                   
                        
               
                                              
                   
                  
                                              


                   
                                 
                           




                  
                         
                   

                                                 
                           
                                                 
                        
                                                  
                                                             
                                                  
                                            
                                                  
                                                                                                                    
                                                  
                                                  
                  


                                                  
                           
                                                 
                                                     
                                                  
                                               
                                                  
                                                                                                                               
                  
                                              


                                                   
                           
                                                                    
                                                 
                                                     
                                                  
                                                                                                                    
                          
                                            
                        
               
                                                                                
                        
               
                                              
                                                    
                  
                                               


                           
                                                                    
                            
                                                 
                                                            
                                                   
                                                                                             
                                                           
                                                  
                     
                          
                                            
                        
               
                                                                                
                        
               
                                              
                   
                  



                   
                                 
                           






                  
                         
                   

                                                 
                            
                                                 
                  
                                                   
                                                       
                                                   
                                                        
                  



                                                  
                           
                                                 
                    
                                                  
                                                             
                                                  
                     
                                                  
                         
                  
                                               


                                                   
                                                                    
                                                 
                        
                                                  
                                                                              
                                                   
                            
                                                   
                   
                          
                                            
                        
               
                                                                                             
                        
               
                                              
                                                                                                                                                             
                      
                                               

                           
                                                                    
                            
                                                 
                   
                                                   
                              
                                                   
                                                        
                                                   
                               
                                                   
                                                 
                                                   
                                                                                                 
                          
                                            
                        
               
                                                                                             
                        
               
                  
                                              


                   
                                 
                           






                  
                         
                   

                                                 
                                                                    
                           
                                                 
                     
                                                  
                                                          
                                                  
                                                         
                          
                                            
                        
               
                                                             
                        
               
                                              
                  
                  



                                                  
                            
                                                                    
                                                 
                         
                          

                                              
                                                 
                                                  
                                                                             
                          
                                            
                        
               
                                                             
                        
               
                                              
                   
                  




                                                   
                            
                                                                    
                                                 
                     
                                                  
                   
                          
                                            
                        
               
                                                             
                        
               
                                              
                                                                                         
                  


                           
                            
                                                                    
                                                 
                       
                                                  
                   
                          
                                            
                        
               
                                                             
                        
               
                                              
                                                                                             
                                                   
                                                       
                  
                                              


                   
                                 
                           







                 
                         

                   

                                                 
                                                                    
                           
                                                 
                    
                                                  
                                
                          
                                            
                        
               
                                                
                        
               
                                              
                   
                  



                                                  
                            
                                                                    
                                                 
                    
                                                  
                   
                          
                                            
                        
               
                                                
                        
               
                                              
                   
                  

                                                   
                            
                                                                    
                                                 
                             
                                                  
                                                       
                                                  
                   
                          
                                            
                        
               
                                                
                        
               
                                              
                   
                  




                           
                           
                                                                    
                                                 
                                                    
                                                  
                                                                                    
                                                   
                                                            
                                                   
                      
                                                                                              
                                                   
                             
                                                  
                                                    
                          
                                            
                        
               
                                                
                        
               
                                              
                  

                   
                                 
                           





                     
                         

                   

                                                 
                            
                                                 
                       
                                                  
                  
                                                  
                                                    
                  
                                              

                                                  
                            
                                                 
                 
                                                   
                                                                                        
                  

                                                   
                            
                                                                    
                                                  
                  
                                                   
                                                         
                                                   
                                                                                                            
                          
                                            
                        
               
                                            
                        
               
                                               
                   
                  

                           
                            
                                                                    
                                                 
                         
                                                   
                                                        
                                                   
                                                   
                          
                                            
                        
               
                                            
                        
               
                                               
                   
                  



                   
                                 
                           



                      
                         

                   

                                                 
                            
                                                  
                   
                                                   
                                                                                             
                  



                                                  
                                                  
                                                             
                                                   
                                                                               
                                                   
                                              
                      

                                                   
                           
                                                                    
                                                  
                                                             
                                                   
                                              
                          
                                            
                        
               
                                                                                             
                        
               
                                               
                   
                  


                           
                            
                                                                    
                                                  
                                                             
                                                   
                                                                                                               
                                                   
                                                            
                          
                                            
                        
               
                                                                                             
                        
               
                  


                   
                                 
                           


                   
                         

                   

                                                 
                            
                                                                    
                                                 
                            
                                                  
                     
                                                  
                                                 
                                                  
                                                    
                          
                                            
                        
               
                                                         
                        
               
                                              
                                                                
                                              
                  



                                                  
                            
                                                                    
                                                 
                            
                                                  
                     
                                                  
                                                     
                                                  
                                                    
                          
                                            
                        
               
                                                         
                        
               
                                               
                   
                  


                                                   
                            
                                                                    
                                                  
                            
                     
                                                  
                        
                                                   
                  
                                                                              
                          
                                            
                        
               
                                                         
                        
               
                                               
                   
                  

                           
                            
                                                                    
                                                  
                           
                     
                                                   
                     
                                                   
                                                                                 
                                                   
                                                                                        
                                                   
                                                        
                          
                                            
                        
               
                                                         
                        
               
                                               
                   
                  


                   
                                 
                           


                  
                         
                   

                                                 
                                                 
                      
                                                   
                                                           
                                                   
                   
                      
                                              


                                                  
                           
                                                                    
                                                 
                         
                                                   
                     
                                                  
                                                                                               
                                                  
                                                
                          
                                            
                        
               
                                                           
                        
               
                  



                                                   
                            
                                                                    
                                                 
                                                             
                                                  
                                                       
                                                  
                                                                                            
                          
                                            
                        
               
                                                           
                        
               
                  



                           
                            
                                                                    
                                                 
                                                      
                                                  
                   
                          
                                            
                        
               
                                                           
                        
               
                                              
                                                                                         
                                                  
                                                          
                  


                   
                           






                   
                         
                        
                   

                        
                                                                                  
                                 
                                             
                       
                      
                                        
                    
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3

                                          
                                 
              


                   
                                 
                           


                      
                         
                        
                   

                        
                                                                                  
                                             
                    
                      
                                        
    hide screen blkfade
    with d3
    jump day_time_requests
    

                       

                                          
                                 
              


                   
                                 
                           
                           




label silk_off:
    call her_main("Ладненько.","base","base") 
    
    $ custom_bra = 0
    
                        
                                                                                  
                                
                                             
                                
                      
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3

                                          
                                 
              

                                          

                   
                                 
                           


                    
                         
                        
                   

                        
                                                                                  
                 
                                             
                            
                      
                                        
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_on:
    call her_main("Что это?","base","base") 
    m "Я понятия не имею."
    her "Тогда ладно."
    
    $ custom_06_worn = True
    
                                          

                   
                                 
                           



                
                          


                                                                                                                                             
                                                                                                                                                                      
                                                                                                                                                                                                        
              



                    
                          
                                                    
              

                
                          
                                                                                                            
              


                        
                       
                   
                        

                               
                         
                                                                  
                                      

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_off:
    call her_main("Ладненько.","base","base") 
    
    $ custom_06_worn = False
    
                       
                          
                      
                                     
                     

                   
                                         
                           


                         
                       
                   
                        

                               
                         
                                                                    
                                       

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_on:
    call her_main("Что это?","base","base") 
    m "Я понятия не имею."
                   
                                              
    her "Тогда ладно."
    
    $ custom_07_worn = True
    
                     

                   
                                         
                           


                          
                       
                   
                        

                               
                         
                                                                     
                                        

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_off:
    call her_main("Хорошо","base","base") 
    
    $ custom_07_worn = False
    
                       
                          
                      
                                     
                     

                   
                                         
                           


                         
                       
                   
                        

                               
                         
                                                                    
                                       

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_on:
    call her_main("Что это такое?","base","base") 
    m "Я совершенно не имею понятия."
                   
                                              
    her "Тогда ладно."
    
    $ custom_08_worn = True
    
                     

                   
                                         
                           


                          
                       
                   
                        

                               
                         
                                                                     
                                        

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
                                          
                                 
                                              
                   
                                              
                       
                          
                      
                                     
                     

                   
                                         
                           


label custom_08_off:
    call her_main("Хорошо","base","base") 
    
    $ custom_08_worn = False
    
                               
                         
                                                                            
                                             

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_on:
    call her_main("Что это?","base","base") 
    m "Я совершенно не имею понятия."
                   
                                              
    her "Тогда ладно."
    
    $ custom_09_worn = True
    
                     

                   
                                         
                           


                            
                       
                   
                        

                               
                         
                                                                        
                                          

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_off:
    call her_main("Хорошо.","base","base") 
    
    $ custom_09_worn = False
    
                       
                          
                      
                                     
                     

                   
                                         
                           


                         
                       
                   
                        

                               
                         
                                                                    
                                       

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_on:
    call her_main("Что это?","base","base") 
    m "Я совершенно не имею понятия."
                                                        
                                              
    her "Тогда ладно."
    
    $ custom_10_worn = True
    
                     

                   
                                         
                           

                            
                       
                   
                        

                               
                         
                                                                        
                                          

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
                                          
                                 
                                              
                          
                                              
                       
                          
                      
                                     
                     

                   
                                         
                           

label custom_10_off:
    call her_main("Хорошо.","base","base") 
    
    $ custom_10_worn = False
    
                               
                         
                                                                            
                                             

                      
                  
                                        
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
                                          
                                 
                                              
                      
                                              
                       
                          
                      
                                     
                     

                   
                                         
                           



                               
                        
                      

                      

                   
                                          
                  

                           


label h_top_on:

                   
                                                 
                                                  
                      
                                                  
                                                 
             
                   
                      
                                                                                                           
                                            
                                                                                      
    hide screen hermione_main
    with d5  
                                 
                                                                                 
                                                                      
                                                                                                           
                                           
                 
                                   
                          

                                                  
                                                  
                      
                                                  
                                                               
                                                                              
             
                   
                                                    
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                            
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                    
                                                  
                                                
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
    $ hermione_wear_top = True
    call update_her_uniform 


                           
                                                   
                                                             
                          
                                              

                        
                  
                       

                             

                   
                                              
                  
                            
                                                  
                                             
                                              
                                                                                        
                                                        

                        
                    
                         

                                 

                   
                                                 
                                                  
                                                     
                        
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
    show screen hermione_main
    with d5 

                           
                                                   
                     
                          
                                              

                        
                        
                             

                 

                           
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   
                                                 
                                                  
                                                     
                                            
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                         
                              


                                   

                            
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   
                                                 
                                                  
                                                     
                                            
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              


                        
                          
                               


                 

                             
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   

                                                 
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                 
                 
                                   
                          
                                       

                                                  
                                                  
                                                     
                                                  
                                                  
                                                          
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                                
                                                                                              
                                          
                                            
                 




                                                   
                                                  
                      
                                                  
                                                                
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                                
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              


                        
                         
                              

                                   

                            
                                                  
                                                   
                                                 
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   

                                                 
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                                                                
                            
                  
                               

                                                  
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                   
                          
                                       

                                                   
                                                  
                                                     
                                                
                                                  
                                                                                              
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                              
                                              
                                          
                                            
                 




                                                   
                                                  
                         
                                                  
                                              
                                                                                                 
             
                   
                                                  
                                                                                                           
                                                                                                                                         
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                           
                                                  
                                 
                                                  
                                                    
             
                   
                                                  
                                                                                                           
                                                   
                                                    
                                 
                                                                                                           
                  
                                                                                                           
                  
                      
                                                                                                           
                 
                                                                                      
                                       


                        
                          
                               

                                    

                             
                                                  
                                                   
                                                 
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                                                                                                                  
                                                                                                                              
                                                               
                                                  
                                              
                                                   
                            
                  
                               

                                                   
                                                  
                                                                                                                  
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                    
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                    
                          
                                       

                                                   
                                                  
                                                     
                                                               
                                                  
                                                                                   
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                           
                                          
                                                                  
                                                   
                                                                                              
                                                                                               
                                          
                                            
                 




                           
                                                  
                         
                                                  
                                                          
                                                                                                 
             
                   
                                                  
                                                                                                           
                                                                                  
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                                                                                           
                 
                                                                                                           
                                                             
                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                           
                                          
                                                                  
                                                   
                                               
                                                                                               
                                          
                 
                      
                                                                                                           
                  
                                                                                      
                                       

                        
                           
                                

                                        

                                                                                                                                            
                                                  
                                                                                                                                          
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                 
                                                  
                                                     
                                                               
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                           
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                       
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                               
                                    

                                     

                                                                                                                                        
                                                  
                                                                                                 
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                 
                                                  
                                                     
                                              
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              


                        
                            
                                 

                                 

                                                 
                                                  
                      
                                                  
                                                                                        
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                          
                                                   
                     
                          
                                              

                        
                             


                                 

                                                  
                                                  
                      
                                                  
                                                                                        
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                             

                                 

                                                  
                                                  
                      
                                                  
                                                                                              
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                             

                                 

                                                  
                                                  
                      
                                                  
                                                                          
             
                   
                                                    
                                 
                                                                                                           
                                 
                                                                                                           
                                                                                             
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                             

                 

                           
                                                  
                     
                                                       
                                                                                                 
                                                                                                                        
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                                                                               
                                                                                                                              
                                                               
                                                  
                                              
                                                   
                            
                  
                               

                                                   
                                                  
                                                                               
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                   
                          
                                       

                                                   
                                                  
                                                     
                                                  
                                                  
                                                      
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                              
                                                                                               
                                          
                                            
                 




                                                   
                                                  
                                              
                                                  
                         
                                                                                         
                                              
             
                   
                                                  
                                                                                                           
                                                                                                       
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                                                                                           
                 
                                                                                                           
                                                             
                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                               
                                                                                               
                                          
                 
                      
                                                                                                           
                  
                                                                                      
                                       

                           
                                                   
                     
                          
                                              

                        
                         
                              

                                        

                                                                                                                                            
                                                  
                                                                                                                                          
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                  
                                                  
                                                     
                                                                 
                                                  
                                                                                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 


                           
                                                   
                     
                          
                                              

                        
                               
                                    


                                     

                                                                                                                                        
                                                  
                                                                                                 
                                                                                   
                                                                                                                     
                                                             
                                                  
                               


                                                  
                                                  
                      
                                                  
                                                                                              
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                        
                            
                                 


                        
                           
                         
                           

                         
                           
                      
                         
                           

                       
                         
                         
                           

                     
                         
                  
                         
                           

                       
                         
                    
                         
                           

                      
                           
                   
                         
                           

                           
                           
                        
                         
                           

                            
                           
                         
                         
                           

                             
                           
                          
                         
                           

                            
                           
                         
                         
                           

                             
                           
                          
                         
                           

                              
                           
                           
                         
                           

                 
                           
                               
                         
                           

                               
                           
                            
                         
                           

                           
                           
                        
                         
                           

                           
                           
                        
                         
                           

                           
                           
                        
                         
                           

                           
                           
                        
                         
                           

                           
                           
                        
                         
                           

                            
                           
                         
                         
                           

                 
                           
                               
                         
                           

                               
                           
                            
                         
                           


                         

                         
                          
    return
    
label h_top_off:
    hide screen hermione_main
    with d5    
    $ hermione_wear_top = False
    call update_her_uniform 
    show screen hermione_main
    with d5 
    return
    
label h_skirt_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = True
    call update_her_uniform 
    show screen hermione_main
    with d5 
                             
                             
                              
                            
                             
                             
                              
                              
                               
                 
                                   
                               
                                
    return
    
label h_skirt_off:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = False
    call update_her_uniform 
    show screen hermione_main
    with d5 
                           
                            
                           
                            
                            
                             
                 
                                   
                               
                                
    return
    
###WEAR PANTIES
label h_panties_on:
    m "Я хочу, что бы ты снова начала носить трусики"
    her "Эти скучные старые вещи?"
    m "Угу."
    her "Я получу что-нибудь за это?"
    menu:
        "Звучание 5 очков.":
            $ gryffindor += 5
            pass
        "Нет, просто сделай это.":
            pass
    her "Хорошо, я сделаю это."
    $ h_request_wear_panties = True
    return
    
label h_panties_off:
    m "Хватит носить эти трусики."
    her "Наконец-то, свобода!"
    $ h_request_wear_panties = False
                                                            
                                                                                 
                                                            
                                                                                 
                                                                                  
                                                            
                                                                    

    return
    
label h_badge_on(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = True
    $ h_badge = badge
    call update_her_uniform 
    show screen hermione_main
    with d5
                                                                            
                                                                                   
                                                                    
                                                                                 
                                                                    

    return
    
label h_badge_off(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = False
    $ h_badge = ""
    call update_her_uniform 
    show screen hermione_main
    with d5
    return
    

    

                                            

    
label set_h_costume(costume_id = 0):
    hide screen hermione_main
    with d5
    call h_outfit_OBJ(costume_id) 
    show screen hermione_main
    with d5
    return
    

#call play_sound("door") #Sound of a door opening.
    
label badge_take:
    call her_main("Как пожелаете, [genie_name]...","base","base") 
    $ badges = True
    $ ba_01 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
### FISHNETS ###
label nets_put:
                                               
                        
                                                  

                         
                                                

                     
                                               
                       
                                                           

                      
                                                
                           
                                                                                                                    
                            
                                                                                                                        
                             
                                                                                                                         
                            
                                                                                                                        
                             
                                                                                                                         
                              
                                                                                                      
                               
                                                                                                                        
                 
                                                                                                                

                           
                                                
                           
                                                                                                                 
                           
                                                                                                           
                           
                                                                                                    
                           
                                                                                                                                                 
                            
                                                                                                                
                               
                                                                                                                         
                 
                                                                                                                

          



                      
                        
                      

                      

                   
                                          
                  
         

                 
                                
                           

          


                     

                   
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("Ажурные чулки...?","open","worried") 
        call her_main("Вы же не серьезно, [genie_name]?!","open","base") 
                                                  
                                                 
        menu:
            m "..."
            "\"Прекрасно. Забудь.\"":
                call her_main("С радостью...","annoyed","angryL") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("Ну, хорошо...","disgust","glance") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset 
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Хм...?","soft","base") 
        call her_main("Я не такая девушка, [genie_name]...","annoyed","suspicious") 
        her "Попытайте счастье с кем-то из \"Слизерина\"..."
                                                               
                                                                              
        menu:
            m "..."
            "\"Просто надень их!\"":
                call her_main("[genie_name] это едва ли подходит для студентки Хогвартса.","normal","frown") 
                call her_main("Я отказываюсь!","annoyed","frown") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                                   
                call upset #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                call her_main("Хм...","normal","frown") 
                call her_main("Ну, в таком случае...","open","suspicious") 
                call her_main("Если это принесет пользу моему факультету...","annoyed","worriedL") 
                                            
                                                                                                           
                                                                                                      
            "\"Прекрасно. Забудь.\"":
                call her_main("Хорошо...","base","base") 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
    
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Хм...?","soft","base") 
        call her_main("Ажурные чулки?","annoyed","suspicious") 
        call her_main("Я ничего не знаю об этом, [genie_name]...","annoyed","worriedL") 
        m "..."
                                                  
                                                
        menu:
            "\"Просто, надень их!\"":
                call her_main("Ладно, ладно...","annoyed","angryL") 
                                                                                                           
                                               
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                call her_main("Хм...","normal","frown") 
                call her_main("Хорошо, я надену их.","grin","baseL") 
            "\"Прекрасно. Забудь.\"":
                call her_main("Ох...","soft","baseL") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3            
        jump day_time_requests
    
    if whoring >= 18: # Lv 7+
        call her_main("Если вы настаиваете, [genie_name]...","angry","down_raised") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
    
    $ ne = True # Shows fishnets layer.
    $ ne_01 = True # Shows the fishnets.
    
    #$ legs_02 = True
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label nets_take:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("Я рада, что вы одумались, [genie_name].","open","angryCl") 
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("С удовольствием, [genie_name].","base","base") 

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Как пожелаете, [genie_name].","annoyed","angryL") 
    
    if whoring >= 18: # Lv 7+
        call her_main("Правда? Оу...","angry","worried") 
    
    
    $ ne = False # Shows fishnets layer.
    $ ne_01 = False # Shows the fishnets.
    #$ legs_02 = False
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") #Sound of a door opening.
    pause 2
    call play_sound("door") #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main
    with d3
    jump day_time_requests

#

    
                                                   
                                                             
                          
                                              

                                 
                               
                           

    

                       

                   
                                              
                  
                            
                                                  
                                             
                                              
                                                                                        
                                                        

                                   
                                 
                           

          

                           

                   
                                                 
                                                  
                                                     
                        
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                       
                                     
                           

          

                            

                                        
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   
                                                 
                                                  
                                                     
                                            
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                        
                                      
                           

          


                             

                                         
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   
                                                 
                                                  
                                                     
                                            
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                         
                                       
                           

          


                            

                                          
                                                  
                                                   
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   

                                                 
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                 
                 
                                   
                          
                                       

                                                  
                                                  
                                                     
                                                  
                                                  
                                                          
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                                
                                                                                              
                                          
                                            
                 




                                                   
                                                  
                      
                                                  
                                                                
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                                
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                        
                                      
                           

          

                             

                                         
                                                  
                                                   
                                                 
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                                                  
                               

                   

                                                 
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                                                                
                            
                  
                               

                                                  
                                                  
                                                                                                                    
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                   
                          
                                       

                                                   
                                                  
                                                     
                                                
                                                  
                                                                                                                                
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                              
                                              
                                          
                                            
                 




                                                   
                                                  
                         
                                                  
                                              
                                                                                                 
             
                   
                                                  
                                                                                                           
                                                                                                                                         
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                           
                                                  
                                 
                                                  
                                                    
             
                   
                                                  
                                                                                                           
                                                   
                                                    
                                 
                                                                                                           
                  
                                                                                                           
                  
                      
                                                                                                           
                 
                                                                                      
                                       

                                         
                                       
                           

                                                                                                                                                                                       
                     
                                                  

                                                  
                         
                                                   

                                     

          

                              

                                          
                                                  
                                                   
                                                 
                                                                                                 
                                                                                          
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                                                                                                                  
                                                                                                                              
                                                               
                                                  
                                              
                                                   
                            
                  
                               

                                                   
                                                  
                                                                                                                  
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                    
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                    
                          
                                       

                                                   
                                                  
                                                     
                                                               
                                                  
                                                                                                                          
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                           
                                          
                                                                  
                                                   
                                                                                              
                                                                                               
                                          
                                            
                 




                           
                                                  
                         
                                                  
                                                          
                                                                                                 
             
                   
                                                  
                                                                                                           
                                                                                  
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                                                                                           
                 
                                                                                                           
                                                             
                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                           
                                          
                                                                  
                                                   
                                               
                                                                                               
                                          
                 
                      
                                                                                                           
                  
                                                                                      
                                       

                                          
                                        
                           

                                                                                                                                                                                       
                     
                                                  

                                                  
                         
                                                   

                                     

          

                 

                                                                                                                                            
                                                  
                                                                                                                                          
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                 
                                                  
                                                     
                                                               
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                           
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                       
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                              
                                            
                           

          

                               

                                                                                                                                        
                                                  
                                                                                                 
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                 
                                                  
                                                     
                                              
                                                  
                                                    
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 
                                    
                          



                                                  
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                                                                                                                                    
                                                                                                           
                                                
                 
                                   
                          
                                             
                                       
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                         
                                                                                                           
                                                                                                      
                      
                                                                                                           
                  
                                                                                      
                                       

                                                   
                                                  
                      
                                                  
                                                        
             
                   
                                                  
                                                                                                           
                                               
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                             
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                           
                                         
                           

          

                          

                                                 
                                                  
                      
                                                  
                                                                                        
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                          
                                                   
                     
                          
                                              

                                      
                                    
                           
                                     

          


                          

                                       
                                                  
                     
                                                       
                                                                                                 
                                                                                                                        
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                      
                                                  
                                                                                        
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                      
                                    
                           
                                     

          

                          

                                       
                                                  
                     
                                                       
                                                                                                 
                                                                                                                        
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                      
                                                  
                                                                                              
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                      
                                    
                           
                                     

          

                          

                                       
                                                  
                     
                                                       
                                                                                                 
                                                                                                                        
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                      
                                                  
                                                                          
             
                   
                                                    
                                 
                                                                                                           
                                 
                                                                                                           
                                                                                             
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                      
                                    
                           

          

                            

                                       
                                                  
                     
                                                       
                                                                                                 
                                                                                                                        
                                                                                                                             
                                                  
                                                                                               
                               

                   

                                                  
                                                  
                                                                               
                                                                                                                              
                                                               
                                                  
                                              
                                                   
                            
                  
                               

                                                   
                                                  
                                                                               
                                                                                                                              
                                                               
                                                  
                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                   
                          
                                       
                                                    
                                                                                                           
                                                                                                              
                                                                                                           
                                               
                                                                                                            
                 
                                   
                          
                                       

                                                   
                                                  
                                                     
                                                  
                                                  
                                                      
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                                                                 
                                                                      
                                                   

                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                                                                              
                                                                                               
                                          
                                            
                 




                                                   
                                                  
                                              
                                                  
                         
                                                                                         
                                              
             
                   
                                                  
                                                                                                           
                                                                                                       
                                                                                                           
                                                
                 
                                    
                          
                                             
                                       
                                                    
                                                                                                           
                 
                                                                                                           
                                                             
                     
                                                    
                                                                  
                                                              
                                          
                                                     
                                               
                                          
                                         
                                                                  
                                                   
                                               
                                                                                               
                                          
                 
                      
                                                                                                           
                  
                                                                                      
                                       

                           
                                                   
                     
                          
                                              

                                        
                                      
                           

          

                 

                                                                                                                                            
                                                  
                                                                                                                                          
                                                                                   
                                                                                                                     
                                                             
                                                  
                               

                   
                                                  
                                                  
                                                     
                                                                 
                                                  
                                                                                     
             
                   
                      
                                                                                                           
                                                      
                 

                                             
                                       
                                                    
                                 
                                                                                 
                                                                      
                                                                                                           
                     
                 


                           
                                                   
                     
                          
                                              

                                              
                                            
                           

          


                               

                                                                                                                                        
                                                  
                                                                                                 
                                                                                   
                                                                                                                     
                                                             
                                                  
                               


                                                  
                                                  
                      
                                                  
                                                                                              
             
                   
                                                    
                                 
                                                                                                           
                             
                                                                                                           
                                                       
                      
                                                                                                           
                      
                                                                                      
                                       


                           
                                                   
                     
                          
                                              

                                           
                                         
                           

          
                                                                  
