import socket

def main():
    # サーバのホストとポートを指定
    HOST = '127.0.0.1'  # サーバが動作しているローカルホスト
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        print("Type your message and press Enter (type 'exit' to quit).")

        while True:
            # ユーザーからの入力を待つ（コマンドラインから）
            user_input = input("Your message: ")
            if user_input.lower() == 'exit':
                break
            client_socket.sendall(user_input.encode('utf-8'))
            data = client_socket.recv(1024)
            if not data:
                print("No response from server. Exiting.")
                break
            print("Received from server:", data.decode('utf-8'))
        print("Closing connection.")

if __name__ == '__main__':
    main()