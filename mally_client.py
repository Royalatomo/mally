import socket

serverIP = "192.168.1.12"
port = 5000

def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    client.connect((serverIP, port))
    print("Connceted To Server")
  except:
    print("Error connecting to server")

  while True:
    #receiving
    data = client.recv(1024)
    response = data.decode('utf-8')
    print(response)

    if (response == "hello"):
      # sending
      message = "hello from client"
      client.sendall(message.encode('utf-8'))
    elif (response == "quit"):
      # sending
      client.close()
      exit()


if __name__ == '__main__':
  main()