import socket
import threading
import json
import rsa
import base64

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024
public_key, private_key = rsa.newkeys(512) # Generar par de claves RSA de 512 bits


def handle_client(client_socket, client_address):
    ip_address = client_address[0]

    print(f"Hello {ip_address} welcome to the server!", flush=True)

    try:
        # Serializar clave pública
        public_key_bytes = public_key.save_pkcs1()

        # Enviar clave pública
        client_socket.sendall(public_key_bytes)

        print("Clave pública enviada.", flush=True)

        while True:
            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                break

            try:
                message = json.loads(data.decode("utf-8"))

                # Payload Cifrado con la clave pública del servidor
                encrypted_payload_b64 = message["payload"]
                print("Payload cifrado recibido: ", encrypted_payload_b64, flush=True)

                # Decodificar el payload cifrado de base64
                encrypted_payload = base64.b64decode(encrypted_payload_b64)

                # Descifrar el payload utilizando la clave privada del servidor
                decrypted_payload = rsa.decrypt(encrypted_payload,private_key)

                # Convertir el payload descifrado a string
                decrypted_payload = decrypted_payload.decode()

                if (
                    isinstance(message, dict)
                    and "group" in message
                    and "payload" in message
                    and isinstance(message["group"], str)
                    and isinstance(message["payload"], str)
                ):
                    print(f"{message['group']}: {decrypted_payload}", flush=True)
                else:
                    print(f"{ip_address} wants to send an ill formatted message.", flush=True)

            except json.JSONDecodeError:
                print(f"{ip_address} wants to send an ill formatted message.", flush=True)

    except ConnectionResetError:
        pass

    finally:
        print(f"Bye {ip_address}!", flush=True)
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}", flush=True)

    try:
        while True:
            client_socket, client_address = server_socket.accept()

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )

            client_thread.start()

    except KeyboardInterrupt:
        print("\nServer stopped.", flush=True)

    finally:
        server_socket.close()


if __name__ == "__main__":
    main()