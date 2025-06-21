import socket
import threading

def handle_receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nFriend: {message}")
        except:
            print("Connection lost.")
            break

def chat_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f" Waiting for connection on port {port}...")
    
    client_socket, addr = server.accept()
    print(f" Connected with {addr}")

    threading.Thread(target=handle_receive, args=(client_socket,), daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        client_socket.send(msg.encode())

    client_socket.close()
    server.close()

if __name__ == "__main__":
    chat_server()
