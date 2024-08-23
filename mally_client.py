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

if __name__ == '__main__':
  main()