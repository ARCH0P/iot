import time
import mysql.connector
from datetime import datetime
import pyfirmata

board = pyfirmata.Arduino('COM6')
it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:13:i')

print(digital_input.read())

mydb = mysql.connector.connect(
	host= "localhost",
	user= "root",
	password= "Elev",
	database= "test1"
)
verdi = 0
mycursor = mydb.cursor()

print("connected...")

sql = "INSERT INTO sensor(verdi,tid) VALUES (%s,%s)"

while True:
	print(digital_input.read())
	if digital_input.read():
		verdi = verdi + 1
		time.sleep(5)
		tid = datetime.now()

		val = (verdi, tid)

		mycursor.execute(sql, val)
		mydb.commit()
		print("ferdig")
	time.sleep(10)