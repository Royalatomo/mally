import socket

ip = "192.168.1.12"
port = 5000

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

if __name__ == '__main__':
  main()
