import socket
import datetime

dt_now= datetime.datetime.now()

client = socket.socket(

	socket.AF_INET,
	socket.SOCK_STREAM,

	)

client.connect(
	("127.0.0.1", 6060)
	)


while True:
	data = client.recv(2048)
	print(data.decode("utf-8"))
	a = input("text blyat ")
	client.send(a.encode("utf-8"))
	client.send("aboba".encode("utf-8"))