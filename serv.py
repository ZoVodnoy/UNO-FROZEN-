import socket
import threading

server = socket.socket(

	socket.AF_INET,
	socket.SOCK_STREAM,

	)


server.bind(
	("127.0.0.1", 6060)
	)

server.listen(8)
print("Listening")

users = []


def send_all(data):
	for user in users:
		user.send(data)


def listen_user(user):
	print('Listening')
	while True:
		data = user.recv(2048)
		print(f"User send {data}")
		send_all(data)


def start_server():
	while True:
		user_socket, address = server.accept()
		print(f"User {user_socket} connected!")
		user_socket.send("Connected!".encode("utf-8"))

		users.append(user_socket)
		listen_accepted_user = threading.Thread(

			target=listen_user,
			args=(user_socket,)

			)

		listen_accepted_user.start()


if __name__ == '__main__':
	start_server()