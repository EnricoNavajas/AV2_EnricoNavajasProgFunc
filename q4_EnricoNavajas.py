GAMES = lambda: ("Games", {"id_game": "int", "title": "varchar(255)", "genre": "varchar(255)", "release_date": "date", "id_console": "int"})

VIDEOGAMES = lambda: ("VideoGames", {"id_console": "int", "nome": "varchar(255)", "id_company": "int", "release_date": "date"})

COMPANY = lambda: ("Company", {"id_company": "int", "nome": "varchar(255)", "country": "varchar(255)"})

gen_inner_join = lambda t1, t2: f"{t1[0]} {t1[1]} INNER JOIN {t2[0]} {t2[1]} ON {' AND '.join([f'{t1[1]}.{attr} = {t2[1]}.{attr}' for attr in t1[1].keys() if attr in t2[1].keys()])}"

gen_select = lambda attributes, tables: f"SELECT {', '.join([f'{alias}.{attribute}' for attribute in attributes for alias, table in tables.items() if attribute in table[1].keys()])} FROM {', '.join([f'{table[0]} AS {alias}' for alias, table in tables.items()])};"

tables = {
    "a": GAMES(),
    "i": VIDEOGAMES(),
    "o": COMPANY()
}

attributes = ["id_game", "title", "release_date", "nome"]
join_code = gen_inner_join(GAMES(), VIDEOGAMES())
select_query = gen_select(attributes, tables)

print(join_code)

print("\nSelect com o join:")
print(select_query)