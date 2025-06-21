import socket
import threading

def handle_receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(f"\nFriend: {message}")
        except:
            print("Connection lost.")
            break

def chat_client(server_ip='127.0.0.1', port=12345):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, port))
        print(f" Connected to server {server_ip}:{port}")
    except:
        print(" Failed to connect.")
        return

    threading.Thread(target=handle_receive, args=(client,), daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        client.send(msg.encode())

    client.close()

if __name__ == "__main__":
    ip = input("Enter server IP (default 127.0.0.1): ").strip() or "127.0.0.1"
    chat_client(server_ip=ip)
