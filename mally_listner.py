import socket

ip = "192.168.1.12"
port = 5000

def handel_cmd(msg, connection):
  connection.sendall(msg.encode('utf-8'))
  if (msg == "quit"):
    connection.close()
    exit()

  while True:
    data = connection.recv(1024)
    if not data:
      connection.close()
      break
    message = data.decode('utf-8')
    print(message)
    break

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    server.bind((ip, port))
  except:
    print("Could not bind")

  server.listen(1)
  print(f"Server listening on {port}")

  while True:
    connection, address = server.accept()
    print(f"Connceted to: {address[0]}:{address[1]}")

    while True:
      cmd = input(">> ")
      handel_cmd(cmd, connection)

if __name__ == '__main__':
  main()
