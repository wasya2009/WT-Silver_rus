#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

### Equip Makeup ###
### Equip Glasses ###
### Equip Ears ###
### Equip Hat ###

label equip_makeup:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_makeup
    #Luna
    if active_girl == "luna":
        jump equip_lun_makeup
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_makeup


### Equip Hermione's Makeup ###

label equip_her_makeup:

    if mad >= 1:
        jump equipping_failed

    if makeup_choice == "lipstick":
        hide screen wardrobe
        call her_main(xpos="right",ypos="base",trans="fade") 
        
        menu:
            "-Изменить цвет помады-"
            "-Красная помада-" if reward_her_red_lipstick and not h_lipstick == "red": #Hypno potion event.
                $ makeup_choice = "red_lipstick"
                jump equi_her_makeup_lipstick
            "-Смыть красную помаду-" if h_lipstick == "red": #Unequip
                $ makeup_choice = "nude"
                jump equi_her_makeup_lipstick
            "-Назад-":
                jump return_to_wardrobe
        
        label equi_her_makeup_lipstick:
        
            if makeup_choice == "red_lipstick":
           
                $ wardrobe_active = 0 #activates dissolve in her_main 

                if h_lipstick == "nude":
                    call her_main("Хотите, чтобы я накрасила губы?","normal","worriedCl") 
                    call her_main("В самом деле, [genie_name]!","scream","angryCl") 
                    m "Чуть-чуть."
            
                    call her_main("Тогда...","base","glance") 
                    hide screen hermione_main
                    with d5
                
                    $ h_lipstick = "red"
            
                    call update_her_uniform #Updates clothing and body.
            
            else: #Nude
                call her_main("Хотите, чтобы я смыла помаду?","annoyed","ahegao") 
                call her_main("Хорошо...","annoyed","down") 
                hide screen hermione_main
                with d5
                
                $ h_lipstick = "nude"
            
                call update_her_uniform #Updates clothing and body.
                
            jump return_to_wardrobe
            
    if makeup_choice not in hermione_makeup_list:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Freckles
            if makeup_choice == "freckles":
                m "Не могла бы ты немного нанести макияж? Я думаю веснушки будут мило смотреться на тебе."
                if whoring >= 14:
                    call her_main("Конечно, [genie_name].","soft","base") 
                    call her_main("Позвольте мне нанести несколько точек на...","base","glance") 
                else:
                    call her_main("Хм","normal","frown") 
                    call her_main("Полагаю, я могу поставить несколько точек...","annoyed","frown") 

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Ты можешь нанести это? Это липовая--ууух... липовая сперма..."

                if whoring >= 20:
                    if whoring < 24:
                        call her_main("Липовая сперма...?","soft","base") 
                        call her_main("...","annoyed","suspicious") 
                        call her_main("Ну, пока еще она не реальна...","base","glance") 
                    else: #24
                        call her_main("Хм...?","soft","base") 
                        call her_main("Вы хотите, чтобы я покрыла себя фальшивой спермой?","annoyed","suspicious") 
                        call her_main("{size=-5}(Жаль, что она не настоящая...){/size}","base","down") 
                        call her_main("Хорошо, я сделаю это, [genie_name].","base","glance") 
                else:
                    if whoring < 8:
                        jump too_much
                    else: #8-19
                        call her_main("Липовая сперма...?","open","worried") 
                        call her_main("Вы же не серьезно, [genie_name]!","open","base") 
                        m "Что не так? Она же не реальная..."
                        call her_main("[genie_name] Я не собираюсь мазаться спермой, реальный или нет, а затем ходить с ней по школе!","normal","frown") 
                        call her_main("Я категорически отказываюсь!","annoyed","frown") 
                    ">Она не будет покрывать себя спермой."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз при уровне разврата 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe


    else: #Remove makeup

        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Freckles
            if makeup_choice == "freckles":
                m "Не могла бы ты снова удалить эти веснушки?"
                call her_main("Хорошо. С вашего позволения я бы их стерла","base","base") 

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Не могла бы ты снова убрать псевдосперму со своего лица?"
                call her_main("Хорошо. С вашего позволения позвольте мне все стереть","base","base") 

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice) #Removes Item

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice) #Removes Item
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe
#

#Add Luna Makeup Texts
#Add Astoria Makeup Texts





label equip_head_accessory:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_head_accessory

    #Luna
    if active_girl == "luna":
        jump equip_lun_head_accessory

    #Astoria
    if active_girl == "astoria":
        jump equip_ast_head_accessory


### Equip Hermione's Head Accessory ###

label equip_her_head_accessory:

    if head_accessory_choice == h_glasses and glasses_color_choice == h_glasses_color or head_accessory_choice == h_ears or head_accessory_choice == h_hat:
        jump remove_head_accessory

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Reading Glasses
            if head_accessory_choice == "reading_glasses":
                m "Можешь ли ты носить эти очки для чтения?"

                if whoring < 11:
                    call her_main("Очки для чтения...?","open","worried") 
                    call her_main("Но я прекрасно вижу, [genie_name].","normal","frown") 
                    m "Это не настоящие очки. Эти линзы поддельные."
                    call her_main("Думаю, я могу их надеть....","annoyed","frown") 
                    call her_main("Позвольте я их надену побыстрее.","base","base") 
                else:
                    call her_main("Конечно, [genie_name].","soft","base") 
                    call her_main("Я буду носить их для вас.","base","glance") 

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Не могла бы ты надеть, для меня, эти винтажные очки?"

                if whoring < 11:
                    call her_main("Винтажные очки...?","open","worried") 
                    call her_main("Мне не нужно носить очки, [genie_name]. Я прекрасно вижу!","open","closed") 
                    m "Это не настоящие очки. Эти линзы поддельные."
                    call her_main("Я вижу... Думаю, я смогу их носить....","annoyed","frown") 
                    call her_main("Позвольте я их надену побыстрее.","base","base") 
                else:
                    call her_main("Конечно, [genie_name].","soft","base") 
                    call her_main("Я не против выглядеть немного занудой...","open","baseL") 
                    call her_main("Позвольте мне надеть их для вас.","base","glance") 

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Примеришь для меня эти кошачьи ушки?"

                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Кошачьи ушки, [genie_name]?","open","worried") 
                        call her_main("(Они выглядят мило...)","base","glance") 
                        call her_main("...","annoyed","down") #annoyed, down
                        m "Так ты собираешься носить их или нет?"
                        call her_main("Прекрасно, [genie_name]. Позвольте я их надену побыстрее.","soft","baseL") 
                    else:
                        call her_main("Они выглядят мило...","base","glance") 
                        call her_main("(И они даже подходят к моим волосам!)","base","down") 
                        call her_main("Позвольте мне надеть их для вас.","base","glance") 
                else:
                    call her_main("Кошачьи ушки...?","open","worried") 
                    call her_main("Правда, [genie_name]?!","open","base") 
                    m "Что случилось? Они же милые..."
                    call her_main("Я не буду носить кошачьи ушки, [genie_name]!","annoyed","angryL") 
                    m "Хорошо. Забудь об этом..."

                    ">Она пока не будет носить кошачьи ушки."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe

            #Elf Ears
            if head_accessory_choice == "elf_ears":
                m "Примеришь для меня эти эльфийские ушки?"

                if whoring >= 11:
                    if h_hair_style != "B":
                        call her_main("Эльфийские ушки...?","soft","base") 
                        call her_main("Вы же не сможете увидеть их под моими волосами...","open","closed") 
                        m "Ты права..."
                        m "Может поменяем и прическу? Чтобы были видны такие милые маленькие ушки?"

                    if whoring < 17:
                        call her_main("...","annoyed","suspicious") 
                        call her_main("Я полагаю, они не слишком заметны...","base","glance") 
                        call her_main("Хорошо. Я буду носить их.","soft","base") 
                        call her_main("Позвольте я быстренько их надену.","soft","baseL") 
                    else:
                        call her_main("...","annoyed","down") 
                        call her_main("Они выглядят мило...","base","down") 
                        call her_main("Хорошо, [genie_name]. Я буду носить их.","base","glance") 
                else:
                    call her_main("Эльфийские ушки...?","open","worried") 
                    call her_main("Я отказываюсь, [genie_name]!","open","base") 
                    m "Почему нет? Ты не поддерживаешь домашних эльфов или что..."
                    call her_main("Дело не в том...","annoyed","angryL") 
                    call her_main("Я не собираюсь носить эти нелепые уши для вас, [genie_name]!","annoyed","angryL") 
                    call her_main("...","annoyed","baseL") 

                    ">Она пока не будет носить кошачьи ушки."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe

            #Tiara
            if head_accessory_choice == "tiara":

                call her_main("Диадема...?","open","worried") 
                call her_main("Полагаю, я могу носить ее...","annoyed","frown") 
                call her_main("Позвольте мне просто надеть ее.","base","glance") 

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) 
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) 
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) 
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                if whoring >= 11:
                    call set_h_ears(head_accessory_choice) 
                else:
                    ">Она пока не будет носить эти ушки."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 11."
                    jump return_to_wardrobe

            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) 

            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe


label remove_head_accessory: #Remove/Toggle off

        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Reading Glasses
            if head_accessory_choice == "reading_glasses":
                m "Не могла бы ты снова быть без очков для чтения?"
                call her_main("Конечно. Позвольте мне их снять.","base","base") 

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Не могла бы ты снова снять очки?"
                call her_main("Хорошо. Я обязательно их сниму.","base","base") 

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Не могла бы ты снова снять кошачьи ушки?"
                call her_main("Конечно. Позвольте мне их снять.","base","base") 

            #Elf Ears
            if head_accessory_choice == "elf_ears":
                m "Не могла бы ты снова снять эти уши?"
                call her_main("Хорошо. Позвольте снять их.","base","base") 

            #Tiara
            if head_accessory_choice == "tiara":
                m "Не могла бы ты снова снять диадему?"
                call her_main("Конечно. Я обязательно ее сниму.","base","base") 

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) 
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) 
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) 
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) 
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) 

            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe

#

#Add Luna's Head Accessory Texts
#Add Astoria's Head Accessory Texts