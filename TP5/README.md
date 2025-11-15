# Trabajo Práctico N°5

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Comunicaciones de Datos**</br>
**Santiago Martin Henn** </br>
**Miguel Ángel Solinas**</br>
**20/10/2025**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Resumen

En este trabajo se estudia el protocolo MQTT (Message Queuing Telemetry Transport) y el modelo de comunicación Publish/Subscribe (Pub/Sub) aplicado a la simulación de una red local IoT.
Se implementa un broker MQTT y varios clientes publicadores y suscriptores que intercambian mensajes bajo tópicos jerárquicos, explorando el funcionamiento de broadcasts, ruteo lógico, y niveles de QoS.
Además, se experimenta con la captura y análisis de paquetes mediante un sniffer, y se discuten aspectos de integridad, confidencialidad y disponibilidad de la arquitectura.
Finalmente, se reflexiona sobre las ventajas del modelo Pub/Sub frente al cliente-servidor y las limitaciones del protocolo MQTT en entornos LAN simulados.
---

## Introducción

En este trabajo práctico se estudia el protocolo MQTT, uno de los más utilizados en sistemas IoT por su bajo consumo de recursos y su modelo de comunicación Publish/Subscribe. A través de una simulación de red local, se implementa un broker MQTT y varios clientes que intercambian datos mediante tópicos jerárquicos. El objetivo es comprender cómo funciona esta arquitectura, cómo se gestionan los mensajes y qué ventajas ofrece respecto a otros modelos de comunicación.

---

## Desarrollo

### 1. Protocolo MQTT y patrón de diseño PubSub

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero diseñado para facilitar la comunicación entre dispositivos en entornos donde los recursos son limitados o la conexión es inestable. Funciona sobre TCP y está pensado para transmitir pequeños volúmenes de datos con muy bajo consumo de ancho de banda, lo que lo convierte en una opción ideal para aplicaciones de Internet de las Cosas. Su arquitectura se basa en el intercambio de mensajes a través de un broker, que actúa como intermediario entre los distintos clientes conectados, permitiendo que la comunicación sea asincrónica y no dependa de que los dispositivos estén activos al mismo tiempo. Además, MQTT utiliza tópicos jerárquicos y permite ajustar el nivel de fiabilidad mediante tres niveles de QoS, que determinan el grado de garantía con el que un mensaje llega a destino.

Entre sus principales ventajas se destacan su bajo consumo de recursos, su capacidad para escalar a grandes cantidades de dispositivos y la flexibilidad que ofrece gracias a la estructura de tópicos. También permite que los clientes se desconecten temporalmente sin perder mensajes importantes, dependiendo del QoS configurado. Sin embargo, el protocolo presenta algunas desventajas: depende por completo del broker para funcionar, ya que si este falla toda la comunicación se interrumpe; no incorpora mecanismos de seguridad por defecto, por lo que es necesario agregar cifrado como TLS de manera explícita; y no es la mejor opción para redes locales de alto rendimiento donde existen protocolos más rápidos o complejos.

En cuanto a sus usos, MQTT es ampliamente utilizado en sistemas IoT, como redes de sensores, actuadores, automatización del hogar o monitoreo industrial. También se emplea en aplicaciones donde se requiere enviar datos de manera eficiente y confiable, incluso en redes con alta latencia o poco ancho de banda.

El modelo sobre el que se basa MQTT es el patrón de diseño PubSub. En este enfoque, los dispositivos que generan información —llamados publishers— no envían mensajes directamente a otros dispositivos, sino que publican dichos mensajes en un tópico. Por su parte, los dispositivos que necesitan recibir esa información —los subscribers— se suscriben a los tópicos que les interesan. El broker se encarga de conectar ambos extremos, reenviando los mensajes publicados a todos los suscriptores correspondientes. Este desacoplamiento entre emisores y receptores simplifica el diseño de la red, mejora la escalabilidad y evita que cada dispositivo deba conocer la dirección de los demás para comunicarse.

### 2
<img width="623" height="361" alt="image" src="https://github.com/user-attachments/assets/7fdfbec1-16a7-42ab-bf78-f56cbaaf6f6f" />
En la Figura 1 se muestra la configuración del broker HiveMQ Cloud, con los parámetros de red necesarios para establecer la conexión segura mediante TLS sobre el puerto 8883.

<img width="1490" height="773" alt="image" src="https://github.com/user-attachments/assets/79b07603-0abb-46a0-a756-6b8bc84b6a9d" />
La Figura 2 muestra la ejecución del cliente MQTT en Python, donde se observa la recepción del mensaje “Hola Mundo desde MQTT”, validando la correcta conexión y funcionalidad del broker HiveMQ.

**Simulación entre 2 Nodos** 
Script del Dispositivo B - Subscriber 
<pre>
import argparse, ssl, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("[B] Conectado. Suscribiendo a:", userdata["topic"])
        client.subscribe(userdata["topic"], qos=1)
    else:
        print(f"[B][ERROR] Falló la conexión. code={reason_code}")

def on_message(client, userdata, msg):
    try:
        text = msg.payload.decode("utf-8", errors="replace")
    except Exception:
        text = str(msg.payload)
    print(f"[B] Recibido: {msg.topic} -> {text} (QoS={msg.qos})")

def main():
    p = argparse.ArgumentParser(description="MQTT Subscriber (Dispositivo B)")
    p.add_argument("--host", required=True)
    p.add_argument("--port", type=int, default=8883)
    p.add_argument("--user", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--topic", default="lan/deviceA/status")
    args = p.parse_args()

    userdata = {"topic": args.topic}
    client = mqtt.Client(client_id="nodo-B-subscriber", userdata=userdata, clean_session=True)
    client.username_pw_set(args.user, args.password)

    client.tls_set(
        ca_certs=None,
        certfile=None,
        keyfile=None,
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLS_CLIENT,
        ciphers=None
    )
    client.tls_insecure_set(False)

    client.on_connect = on_connect
    client.on_message = on_message

    print(f"[B] Conectando a {args.host}:{args.port} (TLS) como '{args.user}'...")
    try:
        client.connect(args.host, port=args.port, keepalive=60)
    except Exception as e:
        print(f"[B][ERROR] No se pudo conectar: {e}")
        sys.exit(2)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[B] Cancelado por el usuario.")
        client.disconnect()

if __name__ == "__main__":
    main()
</pre>

Script del Dispositivo A — Publisher
<pre>
import argparse, ssl, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("[A] Conectado. Publicando...")
        info = client.publish(
            userdata["topic"],
            payload=userdata["payload"],
            qos=userdata["qos"],
            retain=userdata["retain"]
        )
        info.wait_for_publish()
        print(f"[A] Publicado: {userdata['topic']} -> {userdata['payload']} (QoS={userdata['qos']}, retain={userdata['retain']})")
        client.disconnect()
    else:
        print(f"[A][ERROR] Falló la conexión. code={reason_code}")

def main():
    p = argparse.ArgumentParser(description="MQTT Publisher (Dispositivo A)")
    p.add_argument("--host", required=True)
    p.add_argument("--port", type=int, default=8883)
    p.add_argument("--user", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--topic", default="lan/deviceA/status")
    p.add_argument("--payload", default="Device A operativo")
    p.add_argument("--qos", type=int, default=1, choices=[0,1,2])
    p.add_argument("--retain", type=int, default=0, help="1 para publicar con retain")
    args = p.parse_args()

    userdata = {
        "topic": args.topic,
        "payload": args.payload,
        "qos": args.qos,
        "retain": bool(args.retain),
    }

    client = mqtt.Client(client_id="nodo-A-publisher", userdata=userdata, clean_session=True)
    client.username_pw_set(args.user, args.password)

    client.tls_set(
        ca_certs=None,
        certfile=None,
        keyfile=None,
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLS_CLIENT,
        ciphers=None
    )
    client.tls_insecure_set(False)

    client.on_connect = on_connect

    print(f"[A] Conectando a {args.host}:{args.port} (TLS) como '{args.user}'...")
    try:
        client.connect(args.host, port=args.port, keepalive=60)
    except Exception as e:
        print(f"[A][ERROR] No se pudo conectar: {e}")
        sys.exit(2)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[A] Cancelado por el usuario.")
        client.disconnect()

if __name__ == "__main__":
    main()
</pre>

### 5. Jerarquía de tópicos

**a) Simulación de sensores**


**b) Cliente "central"**


**c) Ploteo de datos**


**d) Broadcasting**


**e) Captura de paquete**




### 6. Preguntas

**a) Protocolos de capa de transporte**


**b) Integridad, Confidencialidad y Disponibilidad** 


**c) QoS**


**d) Ventajas de pub/sub frente a cliente-servidor**


**e) Limitaciones de MQTT**


**f) Broker central**

---

## Discusión Y Conclusiones

---

## Referencias
