import socket
import json

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
    
        print(f"\nConectando a {host}:{port}...")

        # Conexión con el servidor
        client.connect((host, port))

        print("Conexión establecida.")

        # Crear mensaje
        message = { 
            "group": "-",
            "payload": "-"
        } 

        while(1):
            payload = input("\nMensaje: ")
            message["group"] = group
            message["payload"] = payload

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