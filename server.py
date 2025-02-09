import socket
from faker import Faker

def main():
    fake = Faker()
    HOST = '127.0.0.1'  # ローカルホスト
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print('Listening on {}:{}'.format(HOST, PORT))

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # クライアントから最大1024バイトのデータを受信
                data = conn.recv(1024)
                if not data:
                    # 受信データがない場合、クライアントが切断したと判断
                    print("No data received. Closing connection.")
                    break
                client_message = data.decode('utf-8')
                print(f"Received from client: {client_message}")

                fake_response = fake.sentence(nb_words=10)
                response = f"Fake response: {fake_response}"
                conn.sendall(response.encode('utf-8'))
                print("Sent response to client.")

if __name__ == '__main__':
    main()