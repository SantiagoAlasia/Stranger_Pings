import socket
import json
import rsa
import base64

def main():
    try:
        print("======================================")
        print("  Bienvenido al terminal del cliente ")
        print("======================================\n")
        print("======================================")

        host = input("IP del servidor: ")
        port = int(input("Puerto: "))
        group = input("Grupo: ")

        print("======================================")

        # Crear socket TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        print("\n======================================")
        print(f"Conectando a {host}:{port}...")

        # Conexión con el servidor
        client.connect((host, port))

        print("Conexión establecida.")

        # Recibir clave pública del servidor
        public_key_data = client.recv(4096)

        # Decodificar la clave pública y cargarla en formato RSA
        public_key = rsa.PublicKey.load_pkcs1(public_key_data)
        
        print("\nClave pública recibida:\n")
        print(public_key_data.decode())
        print("======================================")
        
        # Crear mensaje
        message = { 
            "group": "-",
            "payload": "-"
        } 

        while(1):
            payload = input("\nMensaje: ")

            # Cifrado del payload utilizando la clave pública del servidor
            encrypted_payload = rsa.encrypt(payload.encode(), public_key)

            # Codificación del payload cifrado en base64 para su transmisión
            encrypted_payload_b64 = base64.b64encode(encrypted_payload).decode()

            message["group"] = group
            message["payload"] = encrypted_payload_b64

            # Serialización y envío
            client.sendall(json.dumps(message).encode("utf-8"))

            print(f"Mensaje Enviado Correctamente:\n{json.dumps(message, indent=4)}")

    except ConnectionRefusedError:
        print("[Error] El servidor rechazó la conexión.")

    except TimeoutError:
        print("[Error] Tiempo de espera agotado.")

    except socket.gaierror:
        print("[Error] Dirección IP inválida.")

    except ValueError:
        print("[Error] El puerto debe ser un número entero.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    except KeyboardInterrupt:
        print("\n\n[Info] Interrupción por teclado detectada.")

    except:
        print("[Error] Ocurrió un error inesperado.")

    finally:
        try:
            client.close()
            print("Conexión cerrada.")
        except:
            pass
        finally:
            print("Bye!")

if __name__ == "__main__":
    main()