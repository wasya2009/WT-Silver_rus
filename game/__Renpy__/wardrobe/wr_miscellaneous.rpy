

#Needs to be updated

label equip_misc_item:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_misc_item
    #Luna
    if active_girl == "luna":
        jump equip_lun_misc_item
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_misc_item
        
label equip_her_misc_item:

    if mad >= 1:
        jump equipping_failed
        
    else:
        if misc_item_choice == "transparency":
            if whoring <= 11:
                jump too_much
    
            $ wardrobe_active = 0 #activates dissolve in her_main 

            if transparency == 1:
                call her_main("Вы хотите, чтобы моя одежда просвечивала?","normal","worriedCl") 
                call her_main("В самом деле, [genie_name]!","scream","angryCl") 
                m "Совсем немного."
                call her_main("Хорошо...","open","suspicious") 
                call her_main("Сколько я должна выпить...","annoyed","worriedL") 
            
                menu: 
                    "-Немного-":
                        $ transparency_amount = 0.8
                        call her_main("(По крайней мере, это не должно быть слишком заметно.","normal","worriedCl") 
                    "-Больше половины-" if whoring >= 20:
                        $ transparency_amount = 0.5
                        call her_main("(Надеюсь, это не так уж плохо","annoyed","worriedL") 
                    "-Много-" if whoring >= 23:
                        $ transparency_amount = 0.3
                        call her_main("(...)","base","down") 
                    "-Все это-" if whoring == 24:
                        $ transparency_amount = 0.1
                        call her_main("...","grin","baseL") 

                call her_main("Ладно...","annoyed","down") 
                hide screen hermione_main
                with d5
                $ transparency = transparency_amount
            
                call update_her_uniform #Updates clothing and body.
            
            else:
                call her_main("Хотите, чтобы я надела новую одежду?","annoyed","ahegao") 
                call her_main("О... тогда, [genie_name].","annoyed","down") 
                hide screen hermione_main
                with d5
                $ transparency = 1
            
                call update_her_uniform #Updates clothing and body.
                
            jump return_to_wardrobe
            
        if misc_item_choice == "small_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("Вы хотите, чтобы я использовала анальную пробку? Снова?","angry","wink") 
            call her_main("(...)","annoyed","ahegao") 
            call her_main("(Используемая, уже недостаточного размера. Эта должна подойти...)","disgust","down_raised") 
            call her_main("Разумеется... Позвольте мне вставить ее побыстрее...","base","base") 
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_a_on") #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "medium_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("Вы уверены, что она среднего размера?","soft","wink") 
            call her_main("(Она все так же выглядит большой.)","angry","worriedCl") 
            call her_main("Хорошо, я буду ее использовать... Просто дайте мне секунду...","disgust","down") 
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_b_on") #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "large_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("Большая?","soft","base") 
            g9 "Гигантская!"
            call her_main("...","annoyed","angry") 
            call her_main("(И почему меня это не удивляет...)","annoyed","angryL") 
            call her_main("(Это будет больно...)","angry","worriedCl",cheeks="blush") 
            call her_main("Хорошо... Позвольте мне вставить ее.","base","baseL") 
            g9 "Ты имеешь в виду... \"в себя\"?"
            call her_main("...","annoyed","frown") 
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_c_on") #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "remove_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("Вы хотите, чтобы я вытащила пробку?","angry","wink") 
            call her_main("(Я только начала привыкать....)","annoyed","ahegao") 
            call her_main("Ну тогда, хорошо...","base","base") 
            hide screen hermione_main
            with d5
            call play_sound("pop") 
            pause.2
                
            call set_h_buttplug("remove") #Updates clothing and body.
            
            jump return_to_wardrobe
            
            
            
            
            
            