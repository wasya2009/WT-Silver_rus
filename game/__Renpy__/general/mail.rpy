init python:
    
    class deliveryItem(object):
        object = None
        transit_time = 0
        quantity=1
        type = ''
        
        def __init__(self,object,transit_time,quantity,type):
            self.object = object
            self.transit_time = transit_time
            self.quantity = quantity
            self.type = type
        
    class deliveryQueue(object):
        queue = []
        max_wait = 15
        
        def send(self, item, transit_time, quantity, type):
            if transit_time > self.max_wait:
                transit_time = self.max_wait
            self.queue.append(deliveryItem(item, transit_time, quantity, type))
        
        def got_mail(self):
            for i in self.queue:
                i.transit_time -= 1
            for i in self.queue:
                if i.transit_time <= 0:
                    return True
            return False
        
        def get_mail(self):
            delivery = []
            for i in self.queue:
                if i.transit_time <= 0:
                    delivery.append(i)
            for i in delivery:
                self.queue.remove(i)
            return delivery
    
    deliveryQ = deliveryQueue()
    
label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">Ты читаешь свою почту."
        play sound "sounds/money.mp3"  #Quiet...

        if game_difficulty <= 1: #Rewards Doubled.
            if finished_report == 1:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение одного отчета на этой неделе.\nВаш гонорар:{/size} \n{size=+4}80 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 80
        
            if finished_report == 2:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим вас за заполнение двух отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}140 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 140
    
            if finished_report == 3:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение трех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}180 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 180
            
            if finished_report == 4:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение четырех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}220 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 220
        
            if finished_report == 5:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение пяти отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}300 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 300
            
            if finished_report >= 6:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение шести отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}400 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 400

        elif game_difficulty == 2: #normal difficulty
            if finished_report == 1:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение одного отчета на этой неделе.\nВаш гонорар:{/size} \n{size=+4}60 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 60
        
            if finished_report == 2:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение двух отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}90 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 90
    
            if finished_report == 3:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение трех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}120 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 120
            
            if finished_report == 4:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение четырех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}160 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 160
        
            if finished_report == 5:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение пяти отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}220 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 220
            
            if finished_report >= 6:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение шести отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}300 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 300

        else: #hardcore difficulty
            if finished_report == 1:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение одного отчета на этой неделе.\nВаш гонорар:{/size} \n{size=+4}40 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 40
        
            if finished_report == 2:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение двух отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}70 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 70
    
            if finished_report == 3:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение трех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}90 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 90
            
            if finished_report == 4:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение четырех отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}110 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 110
        
            if finished_report == 5:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение пяти отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}150 галлеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 150
            
            if finished_report >= 6:
                $ letter_text = "{size=-7}От: Министерство магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим за заполнение шести отчетов на этой неделе.\nВаш гонорар:{/size} \n{size=+4}200 галеонов.{/size}\n\n\n{size=-3}-С глубочайшим уважением-{/size}"    
                $ gold += 200
        
        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc
            
        $ finished_report = 0

        call screen main_room_menu
    
    
### MAIL FROM HERMIONE ###
#place after ### MAIL FROM HERMIONE ###

if outfit_ready:
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}От: Мадам Мафкин\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой профессор Дамблдор.\nЭто напоминание о том, что у вас есть заказ, готовый для вручения в лавке одежды\n\n{size=-3}Спасибо за ваш заказ,\n М.М.{/size}"
    label letter_outfit:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Закончить чтение-":
            pass    
        "-Еще-":
            jump letter_outfit
    $ letters -= 1
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_room_menu
    
if day == 1:
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger-{/size}"
    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Мне жаль снова вас беспокоить, профессор. Я просто хочу убедиться, что вы серьезно относитесь к этой проблеме.\n\nПрошлой ночью другой одноклассник признался мне... Я дала слово держать это в секрете, поэтому я не могу вдаваться в подробности.\n\nВсе, что я могу сказать, что один из профессоров был скомпрометирован.\n\nПожалуйста, примите меры.\n\n{size=-3}С глубочайшим уважением,\nГермиона Грейнджер.{/size}" 
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Закончить чтение-":
            pass    
        "-Еще-":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Хм..............................."
    m "Что?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_room_menu
    


if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger--{/size}"
    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Мне жаль снова вас беспокоить, профессор. Я просто хочу убедиться, что вы серьезно относитесь к этой проблеме.\n\nПрошлой ночью другой одноклассник признался мне.... Я дала слово держать это в секрете, поэтому я не могу вдаваться в подробности.\n\nВсе что я могу сказать, что один из профессоров был скомпрометирован.\n\nПожалуйста, примите меры.\n\n{size=-3}С глубочайшим уважением,\nГермиона Грейнджер.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Закончить чтение-":
            pass    
        "-Еще-":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_room_menu

if ministry_letter: #Letter from the ministry
    $ ministry_letter = False
    $ letter_text = "{size=-7}Дорогой Альбус Дамблдор, мы уверены, вы знаете, что на территории Хогвартса было обнаружено непростительное проклятие.\nХотя наказание за такое проклятие, как правило, пожизненное заключение в тюрьме, Азкабана, мы позволяем вам решить этот вопрос по своему усмотрению.\nЭто связано с возможным характером заклинания, наложенного несовершеннолетним, который не полностью понял серьезный характер проклятия.\nЕсли это так, мы не ожидаем от вас дальнейших сообщений относительно этого несчастного случая.\nЕсли, однако, вы считаете, что проклятие было наложено кем-то другим, кроме студента, или если возникают какие-либо другие осложнения, мы ожидаем немедленного сообщения.\nНаконец, обнаружение любых дальнейших проклятий, приведет к немедленной отправке мракоборца в Хогвартс.\n\nКорнелиус Фадж,\nНачальник отдела: Improper Use of Magic(Неправильное использование волшебства) {/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label ministry_letter_again:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Закончить чтение-":
            pass    
        "-Еще-":
            jump ministry_letter_again
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Это звучит неплохо..."
    m "Возможно, мне стоит рассказать об этом Снейпу."
    m "Или может мисс Грейнджер?"
    
    #Unlocks next event.
    $ ministry_letter_received = True
    call screen main_room_menu





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}От: Министерство Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой профессор Дамблдор,\nМы напоминаем вам, что только после предоставления нам, заполненного отчета, мы сможем произвести оплату на Ваше имя.\n\n{size=-3}С глубочайшим уважением,\nМинистерство магии.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Закончить чтение-":
            pass    
        "-Еще-":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Оплаты? Хм..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">С этого момента ты можешь делать отчеты за своим столом, чтобы заработать дополнительные галлеоны..."
    hide screen blktone8
    with d3
    call screen main_room_menu



label get_package:
    python:
        for item in deliveryQ.get_mail():
            if item.type == 'Gift':
                gift = item.object
                gift_item_inv[gift.id] += item.quantity
                the_gift = gift.image
                renpy.show_screen("gift")
                renpy.with_statement(Dissolve(0.3))
                if item.quantity > 1:
                    renpy.say(None,"Ты получил "+str(item.quantity)+" "+str(gift.name)+"")
                else:
                    renpy.say(None,"Ты получил "+str(item.quantity)+" "+str(gift.name))
                renpy.hide_screen("gift")
                renpy.with_statement(Dissolve(0.3))
            
            if item.type == 'Event_item':
                pass
               
    $ package_is_here = False
    call screen main_room_menu
    
label mail_02: #Packages only. <=====================================================================### PACKAGES ###=================================================== 
    
### ITEMS ###   
    if gift_order != None:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ gift_item_inv[gift_order.id] += order_quantity
        
        $ the_gift = gift_order.image
        show screen gift
        with d3
        $ tmp_str = "\""+gift_order.name
        if order_quantity > 1:
            $ tmp_str += "'s\""
            ">([order_quantity]) [tmp_str] были добавлены к твоему имуществу."
        else:
            $ tmp_str += "\""
            ">([order_quantity]) [tmp_str] был добавлен к твоему имущество."
        hide screen gift
        with d3
        $ gift_order = None
        call screen main_room_menu
        
    
    
    if bought_ball_dress:
        $ bought_ball_dress = False
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_dress_already = True #Makes sure that you won't buy the dress twice.
        
        $ gifts12.append("ball_dress")
        $ the_gift = "images/store/01.png" # THE NIGHT DRESS.
        show screen gift
        with d3
        ">Модная ночная рубашка была добавлена ​​в ваше имущество."
        hide screen gift
        with d3
        call screen main_room_menu
    
    if bought_miniskirt:
        $ bought_miniskirt = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_skirt_already = True #Makes sure that you won't buy the skirt twice.
        $ have_miniskirt = True # Turns TRUE when you have the skirt in your possession.
        $ the_gift = "images/store/07.png" # MINISKIRT.
        show screen gift
        with d3
        ">Школьная мини-юбка добавлена ​​к твоему имуществу."
        hide screen gift
        with d3
        call screen main_room_menu
    
    if bought_glasses:
        $ bought_glasses = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ glasses = True #Glasses owned
        $ glasses_worn = False

        $ the_gift = "images/store/glasses.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">Прекрасные очки для чтения были добавлены к твоему имуществу."
        hide screen gift
        with d3
        call screen main_room_menu
    
    if bought_badge_01:
        $ bought_badge_01 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ badge_01 = 1 

        $ the_gift = "images/store/29.png" # S.P.E.W. Badge.
        show screen gift
        with d3
        ">Значок \"П.У.К.Н.И. \" был добавлен к твоему имуществу."
        hide screen gift
        with d3
        call screen main_room_menu
    
    if bought_nets:
        $ bought_nets = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ nets = 1 

        $ the_gift = "images/store/30.png" # FISHNETS.
        show screen gift
        with d3
        ">Пара чулок в сеточку была добавлена к твоему имуществу."
        hide screen gift
        with d3
        call screen main_room_menu


