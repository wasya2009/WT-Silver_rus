label cheats:
    menu:
        "-Гермиона, Коды-":
            label cheats_hermione:
            menu:
                "-Сброс настроения Гермионы-":
                    $ mad = 0
                    ">Гермиона больше не злится на тебя."
                    jump cheats_hermione
                "-Максимум Развращенности-":
                    $ whoring = 24
                    ">Гермиона теперь ненасытная шлюха."
                    jump cheats_hermione
                    
                "-Увеличение Развращенности-":
                    if whoring >= 24:
                        ">Распутство Гермионы на макс. уровне и не может быть дальше увеличено!"
                    else:
                        $ whoring += 1
                        ">Гермиона стала более развращенной..."
                    jump cheats_hermione
                "-Уменьшение Развращенности-":
                    if whoring <= 0:
                        "Распутство Гермионы больше не может быть уменьшено!"
                    else:
                        $ whoring -= 1
                        "Гермиона восстановила немного своего достоинства"
                    jump cheats_hermione

                "-Разблокировать общественные услуги-":
                    $ force_unlock_pub_favors = True
                    $ touched_by_boy = True
                    $ lock_public_favors = False
                    ">Общественные услуги разблокированы!"
                    jump cheats_hermione

                "-Добавить все костюмы-":
                    python:
                        for i in hermione_outfits_list:
                            i.purchased = True
                    ">Все костюмы Гермионы были разблокированы"
                    jump cheats

                "-Переключить Размер Груди-":
                    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts:
                        $ hermione_perm_expand_breasts = False
                        $ hermione_expand_breasts = False
                        $ hermione_perm_expand = False
                        "Грудь Гермионы сжимается..."
                    else:
                        $ hermione_perm_expand_breasts = True
                        "Грудь Гермионы растет..."
                    jump cheats

                "-Включить Futa Гермионы-":
                    if hermione_futa:
                        $ hermione_futa = False
                        "Член Гермионы сжимается..."
                    else:
                        $ hermione_futa = True
                        "У Гермионы вырастает... Член!"
                    jump cheats
                "-Назад-":
                    jump cheats

        "-Полумна, Коды-":
            label cheats_luna:
            menu:
                "-Сброс всего контента Полумны-":
                    $ hat_known = False
                    call luna_progress_init 
                    ">Сброс контента Полумны!"
                    jump cheats
                "-Назад-":
                    jump cheats

        "-Книжные Коды-":
            label cheats_books:
            menu:
                "-Максимум Фантазии":
                    $ imagination = 5
                    "Твое воображение растет!"
                    jump cheats_books
                "-Супер Чтение ([cheat_reading])-":
                    $ cheat_reading = not cheat_reading
                    jump cheats_books
                "-Все книги-" if day >= 16:
                    python:
                        for book in Books_OBJ.get_all():
                            book.purchased = True
                    "Получить все книги."
                    jump cheats_books
                "-Назад-":
                    jump cheats

        "-Зелье, Коды-":
            label cheats_potions:
            menu:
                "-Добавить все обычные зелья-":
                    $ potion_inv.extend(["p_cum_addiction","p_ass_expansion","p_breast_expansion","p_cat_transformation","p_luna_transformation","p_transparency","p_hypno"])
                    ">Все зелья добавлены (кроме зелий Снейпа)"
                    jump cheats_potions
                "-Назад-":
                    jump cheats

        "-Добавить Галлеонов-":
            $ gold += 500
            "Ты получил 500 галлеонов."
            jump cheats

        "-Добавить очков Слизерину-":
            $ slytherin +=100
            "100 очков Слизерину!"
            jump cheats

        "-Карта-":
            "Карта добавлена в инвентарь!"
            $ cataloug_found = True
            jump cheats

        "-Выйти-":
            jump day_main_menu
