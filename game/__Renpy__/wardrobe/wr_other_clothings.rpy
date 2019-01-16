#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

### Equip Neckwear ### MISSING TEXTS
### Equip Body Accessories ###
### Equip Gloves ### MISSING TEXTS
### Equip Stockings ### MISSING TEXTS
### Equip Robe ### MISSING TEXTS



### Neckwear Equip ###
label equip_neckwear:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_neckwear
    #Luna
    if active_girl == "luna":
        jump equip_lun_neckwear
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_neckwear
    #Susan
    if active_girl == "susan":
        jump equip_sus_neckwear
        
### Equip Hermione's Neckwear ###
label equip_her_neckwear:
    call set_h_neckwear(neckwear_choice, neckwear_color_choice) 
    
    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Neckwear ###
label equip_ast_neckwear:
    call set_ast_neckwear(neckwear_choice) 
    
    hide screen wardrobe
    call screen wardrobe
    
### Equip Susan's Neckwear ###
label equip_sus_neckwear:
    call set_sus_neckwear(neckwear_choice) 
    
    hide screen wardrobe
    call screen wardrobe

    
    
### Gloves Equip ###
label equip_gloves:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_gloves
    #Luna
    if active_girl == "luna":
        jump equip_lun_gloves
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_gloves
    #Susan
    if active_girl == "susan":
        jump equip_ast_gloves
        
### Equip Hermione's Gloves ###
label equip_her_gloves:
    call set_h_gloves(gloves_choice, gloves_color_choice) 
    
    hide screen wardrobe
    call screen wardrobe
    
### Equip Astoria's Gloves ###
label equip_ast_gloves:
    call set_ast_gloves(gloves_choice) 
    
    hide screen wardrobe
    call screen wardrobe
    
### Equip Susan's Gloves ###
label equip_sus_gloves:
    call set_sus_gloves(gloves_choice) 
    
    hide screen wardrobe
    call screen wardrobe
    
    
    
### Body Accs Equip ###
label equip_body_accessory:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_body_accessory
    #Luna
    if active_girl == "luna":
        jump equip_lun_body_accessory
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_body_accessory
    #Susan
    if active_girl == "susan":
        jump equip_sus_body_accessory

### Equip Hermione's Body Accessory ###
label equip_her_body_accessory:

    if mad >= 1:
        jump equipping_failed

    if body_accessory_choice not in hermione_body_accs_list:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #S.P.E.W Badge
            if body_accessory_choice == "badge_SPEW":
                m "Ты бы надела этот значок для меня?"
                if whoring >= 0:
                    call her_main("значок П.У.К.Н.И. ?","base","base") 
                    call her_main("Я буду носить его с гордостью [genie_name].","open","closed") 

            #I <3 Cum Badge
            if body_accessory_choice == "badge_I_love_cum":
                m "Ты наденешь этот значок для меня?"

                if whoring >= 20:
                    if whoring < 24:
                        call her_main("Хм...?","soft","base") 
                        call her_main("Значок \"I love cum\"?","annoyed","suspicious") 
                        call her_main("{size=-5}(Я полагаю, что это не совсем ложь...){/size}","base","down") 
                        call her_main("Хорошо, я надену его.","base","glance") 
                    else: #24
                        call her_main("Значок \"I love cum\"?","annoyed","suspicious") 
                        call her_main("Конечно, [genie_name]!","soft","base") 
                        call her_main("Позвольте мне надеть его для вас.","base","glance") 
                else:
                    if whoring < 8:
                        jump too_much
                    else: #8-19
                        call her_main("Значок I love cum (прим: я люблю сперму)...?","open","worried") 
                        call her_main("Вы же не серьезно, [genie_name]!","open","base") 
                        m "Что не так?"
                        call her_main("Я не собираюсь носить значок, в котором говорится, что{w=0.5} {b}Я{/b}{w=0.5} {b}люблю{/b}{w=0.5} {b}сперму!{/b}","normal","frown") 
                        call her_main("Я категорически отказываюсь!","annoyed","frown") 
                    ">Она пока не станет носить такой значок."
                    if cheats_active or game_difficulty <= 2:
                        ">Попробуй еще раз на уровне разврата 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_body_accessory(body_accessory_choice) 

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_body_accessory(body_accessory_choice) 
            call her_main("","","",xpos="wardrobe") 
            call screen wardrobe


    else: #Remove makeup

        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ wardrobe_active = 0 #activates dissolve in her_main 
            $ hermione_xpos = 665

            m "[hermione_name]..."

            #S.P.E.W Basge
            if body_accessory_choice == "badge_SPEW":
                m "Не могла бы ты снова снять значок П.У.К.Н.И.?"
                call her_main("Хорошо. С вашего позволения.","annoyed","down") 

            #I <3 Cum Badge
            if body_accessory_choice == "badge_I_love_cum":
                m "Не могла бы ты снова снять значок I love Cum?"
                call her_main("Хорошо. С вашего позволения.","annoyed","down") 

            hide screen hermione_main
            with d3

            pause.5

            call set_h_body_accessory(body_accessory_choice) #Removes Item

            call her_main("","","",xpos="wardrobe") 
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_body_accessory(body_accessory_choice) #Removes Item
            call her_main("",xpos="wardrobe") 
            call screen wardrobe
#

#Add Luna Body Accessory Texts
#Add Astoria Body Accessory Texts

### Stockings Equip ###
label equip_stockings:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_stockings
    #Luna
    if active_girl == "luna":
        jump equip_lun_stockings
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_stockings
    #Susan
    if active_girl == "susan":
        jump equip_sus_stockings
        
### Equip Hermione's Stockings ###
label equip_her_stockings:
    call set_h_stockings(stockings_choice, stockings_color_choice) 
    
    hide screen wardrobe
    call screen wardrobe
    
### Equip Astoria's Stockings ###
label equip_ast_stockings:
    call set_ast_stockings(stockings_choice) 

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Stockings ###
label equip_sus_stockings:
    call set_sus_stockings(stockings_choice) 

    hide screen wardrobe
    call screen wardrobe
    
    

### Robe Equip ###
label equip_robe:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_robe
    #Luna
    if active_girl == "luna":
        jump equip_lun_robe
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_robe
    #Susan
    if active_girl == "susan":
        jump equip_sus_robe
        
        
### Equip Hermione's Robe ###
label equip_her_robe:
    call set_h_robe(robe_choice) 

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Robe ###
label equip_ast_robe:
    call set_ast_robe(robe_choice) 

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Robe ###
label equip_sus_robe:
    call set_sus_robe(robe_choice) 

    hide screen wardrobe
    call screen wardrobe