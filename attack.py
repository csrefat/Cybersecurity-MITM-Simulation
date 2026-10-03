import socket

HOST = "127.0.0.1"
REAL_SERVER_PORT = 5000
ATTACKER_PORT = 5001

def attack():
    print("=== ATTACK PROGRAM (Modification of Messages) ===")
    
    attacker_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    attacker_server.bind((HOST, ATTACKER_PORT))
    attacker_server.listen(1)
    
    print(f"[ATTACKER] Listening on {HOST}:{ATTACKER_PORT} (Waiting for client...)")
    client_conn, client_addr = attacker_server.accept()
    print(f"[ATTACKER] Intercepted connection from client: {client_addr}")

    real_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    real_server.connect((HOST, REAL_SERVER_PORT))
    print("[ATTACKER] Secretly connected to the real server.")

    while True:
        data = client_conn.recv(1024)
        if not data:
            break
        
        original_message = data.decode()
        print(f"\n[ATTACKER] Original Message from Client: '{original_message}'")

        # The Attack: Modifying the message
        modified_message = original_message + " [HACKED! TRANSFER MONEY TO ATTACKER]"
        print(f"[ATTACKER] Modified Message to Server: '{modified_message}'")

        real_server.send(modified_message.encode())
        server_response = real_server.recv(1024)
        client_conn.send(server_response)

    client_conn.close()
    real_server.close()
    attacker_server.close()

if __name__ == "__main__":
    attack()