import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123",
    database = "testepf"
)

mycursor=mydb.cursor()

#Criação das tabelas
#mycursor.execute("CREATE TABLE Users (id int, nome varchar (255), country varchar (255), id_console int)")

#mycursor.execute("CREATE TABLE VideoGames (id_console int, nome varchar (255), id_company  int, release_date date)")

#mycursor.execute("CREATE TABLE Games (id_game  int, title varchar (255), genre varchar (255), release_date  date, id_console  int)")

#mycursor.execute("CREATE TABLE Company (id_company  int, nome varchar (255), country varchar (255))")


#Iserindo 
inserir_user = lambda mycursor, id, nome, country, id_console: mycursor.execute("INSERT INTO Users (id, nome, country, id_console) VALUES (%s, %s, %s, %s)", (id, nome, country, id_console))

inserir_videogame = lambda mycursor, id_console, nome, id_company, release_date: mycursor.execute("INSERT INTO VideoGames (id_console, nome, id_company, release_date) VALUES (%s, %s, %s, %s)", (id_console, nome, id_company, release_date))

inserir_game = lambda mycursor, id_game, title, genre, release_date, id_console: mycursor.execute("INSERT INTO Games (id_game, title, genre, release_date, id_console) VALUES (%s, %s, %s, %s, %s)", (id_game, title, genre, release_date, id_console))

inserir_company = lambda mycursor, id_company, nome, country: mycursor.execute("INSERT INTO Company (id_company, nome, country) VALUES (%s, %s, %s)", (id_company, nome, country))

#inserir_user(mycursor, 1, 'Enrico', 'Brasil', 1)

#inserir_videogame(mycursor, 1, 'Xbox One Slim', 1, '2014-5-14')

#inserir_game(mycursor, 1, 'Rainbow Six Siege', 'Ação', '2016-8-25', 1)

#inserir_company(mycursor, 1, 'Nintendo', 'Japão')

#Consultas de Select
mycursor.execute("SELECT * FROM Users")
myresult = mycursor.fetchall()
(lambda res : [print (x) for x in res]) (myresult)

mycursor.execute("SELECT * FROM VideoGames")
myresult = mycursor.fetchall()
(lambda res : [print (x) for x in res]) (myresult)

mycursor.execute("SELECT * FROM Games")
myresult = mycursor.fetchall()
(lambda res : [print (x) for x in res]) (myresult)

mycursor.execute("SELECT * FROM Company")
myresult = mycursor.fetchall()
(lambda res : [print (x) for x in res]) (myresult)

mydb.commit()
mydb.close()
