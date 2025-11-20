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

### 2.

<div>
 <img width="623" height="361" alt="image" src="https://github.com/user-attachments/assets/7fdfbec1-16a7-42ab-bf78-f56cbaaf6f6f" />
</div>

En la Figura 1 se muestra la configuración del broker HiveMQ Cloud, con los parámetros de red necesarios para establecer la conexión segura mediante TLS sobre el puerto 8883.

<div>
 <img width="1490" height="773" alt="image" src="https://github.com/user-attachments/assets/79b07603-0abb-46a0-a756-6b8bc84b6a9d" />
</div>

La Figura 2 muestra la ejecución del cliente MQTT en Python, donde se observa la recepción del mensaje “Hola Mundo desde MQTT”, validando la correcta conexión y funcionalidad del broker HiveMQ.


### Simulación entre 2 Nodos

Script del Dispositivo B - Subscriber 


<pre>
import argparse, ssl, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
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
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="nodo-B-subscriber",
        userdata=userdata,
        protocol=mqtt.MQTTv311,
    )
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

def on_connect(client, userdata, flags, reason_code, properties):
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

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="nodo-A-publisher",
        userdata=userdata,
        protocol=mqtt.MQTTv311,
    )
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

**RESULTADOS EN TERMINAL**

Publisher: 
<div>
 <img width="1414" height="501" alt="image" src="https://github.com/user-attachments/assets/104f91ef-029f-406c-b7bb-542c8cc9d4cb" />
</div>

Subscriber:
<div> 
 <img width="1458" height="765" alt="image" src="https://github.com/user-attachments/assets/1621589a-695b-4c93-9cf8-f2871b6f3b01" />
</div>

En las Figuras 3 y 4 se observa la simulación de dos nodos MQTT en una red local: el Dispositivo A publica su estado en el tópico lan/deviceA/status, mientras que el Dispositivo B recibe el mensaje, evidenciando el correcto enrutamiento de mensajes a través del broker.

### Broadcasting en la red local

Script del Dispositivo B - Subscriber 

<pre>
import argparse, ssl, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"[SUB][on_connect] reason_code={reason_code}")
    if reason_code == 0:
        print(f"[SUB] Conectado. Suscribiendo a: {userdata['topic']}")
        client.subscribe(userdata["topic"], qos=userdata["qos"])
    else:
        print(f"[SUB][ERROR] Falló la conexión. code={reason_code}")

def on_message(client, userdata, msg):
    try:
        text = msg.payload.decode("utf-8", errors="replace")
    except Exception:
        text = str(msg.payload)
    print(f"[SUB] {msg.topic} -> {text} (QoS={msg.qos}, retain={msg.retain})")

# Firmas robustas para distintas variantes en paho-mqtt 2.x
def on_disconnect(client, userdata, *rest, **kwargs):
    # formatos posibles: (reason_code, properties) o (disconnect_flags, reason_code, properties)
    reason_code = None
    if len(rest) == 2:
        reason_code = rest[0]
    elif len(rest) == 3:
        reason_code = rest[1]
    print(f"[SUB][on_disconnect] reason_code={reason_code}, extra_len={len(rest)}")

def main():
    p = argparse.ArgumentParser(description="MQTT Broadcast Subscriber")
    p.add_argument("--host", required=True)
    p.add_argument("--port", type=int, default=8883)
    p.add_argument("--user", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--topic", default="lan/broadcast/#")
    p.add_argument("--qos", type=int, default=0, choices=[0,1,2])
    p.add_argument("--keepalive", type=int, default=180)  # más tolerante a inactividad
    args = p.parse_args()

    userdata = {"topic": args.topic, "qos": args.qos}
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="sub-broadcast",
        userdata=userdata,
        protocol=mqtt.MQTTv311,
    )
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
    client.on_disconnect = on_disconnect

    print(f"[SUB] Conectando a {args.host}:{args.port} (TLS) como '{args.user}'...")
    try:
        client.connect(args.host, port=args.port, keepalive=args.keepalive)
    except Exception as e:
        print(f"[SUB][ERROR] No se pudo conectar: {e}")
        sys.exit(2)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[SUB] Cancelado por el usuario.")
        client.disconnect()

if __name__ == "__main__":
    main()
</pre>

Script del Dispositivo A — Publisher


<pre>
# mqtt_broadcast_pub.py
# Publicador para "broadcast". Compatible paho-mqtt >= 2.x

import argparse, ssl, sys
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"[PUB][on_connect] reason_code={reason_code}")
    if reason_code == 0:
        print("[PUB] Conectado. Publicando...")
        info = client.publish(
            userdata["topic"],
            payload=userdata["payload"],
            qos=userdata["qos"],
            retain=userdata["retain"]
        )
        print(f"[PUB] publish() mid={info.mid}, rc={info.rc}")
    else:
        print(f"[PUB][ERROR] Falló la conexión. code={reason_code}")

def on_publish(client, userdata, mid, reason_codes=None, properties=None):
    print(f"[PUB][on_publish] mid={mid} confirmado. reason_codes={reason_codes}")
    client.disconnect()

def on_disconnect(client, userdata, *rest, **kwargs):
    reason_code = None
    if len(rest) == 2:
        reason_code = rest[0]
    elif len(rest) == 3:
        reason_code = rest[1]
    print(f"[PUB][on_disconnect] reason_code={reason_code}, extra_len={len(rest)}")

def main():
    p = argparse.ArgumentParser(description="MQTT Broadcast Publisher")
    p.add_argument("--host", required=True)
    p.add_argument("--port", type=int, default=8883)
    p.add_argument("--user", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--topic", default="lan/broadcast/all")
    p.add_argument("--payload", default="Mensaje de broadcast")
    p.add_argument("--qos", type=int, default=0, choices=[0,1,2])
    p.add_argument("--retain", type=int, default=0, help="1 para publicar con retain")
    p.add_argument("--keepalive", type=int, default=60)
    args = p.parse_args()

    userdata = {
        "topic": args.topic,
        "payload": args.payload,
        "qos": args.qos,
        "retain": bool(args.retain),
    }

    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION2,
        client_id="pub-broadcast",
        userdata=userdata,
        protocol=mqtt.MQTTv311,
    )
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
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect

    print(f"[PUB] Conectando a {args.host}:{args.port} (TLS) como '{args.user}'...")
    try:
        client.connect(args.host, port=args.port, keepalive=args.keepalive)
    except Exception as e:
        print(f"[PUB][ERROR] No se pudo conectar: {e}")
        sys.exit(2)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n[PUB] Cancelado por el usuario.")
        client.disconnect()

if __name__ == "__main__":
    main()

</pre>

**RESULTADOS EN TERMINAL**

Publisher: 

<div>
 <img width="1488" height="764" alt="image" src="https://github.com/user-attachments/assets/189e9dba-04d8-48fe-b171-649bd5c94e03" />
</div>

Subscriber 1: 

<div>
 <img width="1450" height="626" alt="image" src="https://github.com/user-attachments/assets/a3911f95-c970-4245-844f-c1b579afd476" />
</div>

Subscriber 2: 

<div>
 <img width="1488" height="756" alt="image" src="https://github.com/user-attachments/assets/d211313a-9925-45cf-bbcd-283668968926" />
</div>

### 5. Jerarquía de tópicos


Terminal 1 – Script Gateway (suscriptor + CSV)
<pre>
 import argparse, ssl, time, csv
import paho.mqtt.client as mqtt

CSV_FILE = "datos_sensores.csv"

def on_message(client, userdata, msg):
    valor = msg.payload.decode()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"[GATEWAY] {timestamp} | {msg.topic} -> {valor}")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, msg.topic, valor])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    args = parser.parse_args()

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.username_pw_set(args.user, args.password)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

    client.on_message = on_message

    topic = "lan/+/sensor/+"
    print(f"[GATEWAY] Suscribiéndose a {topic}")

    client.connect(args.host, args.port, 60)
    client.subscribe(topic, qos=1)

    client.loop_forever()

if __name__ == "__main__":
    main()
</pre>
Foto: <img width="1458" height="739" alt="image" src="https://github.com/user-attachments/assets/e076622a-519b-4c19-b52e-da0442c75127" />

Terminal 2 – Script Sensor sala1/temp
<pre>
import argparse, ssl, time, random
import paho.mqtt.client as mqtt

running = False

def on_message(client, userdata, msg):
    global running
    comando = msg.payload.decode().lower()
    if comando == "start":
        running = True
        print("[sala1/temp] Recibido comando START → comenzando a transmitir")
    elif comando == "stop":
        running = False
        print("[sala1/temp] Recibido comando STOP → deteniendo transmisión")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()

    topic = "lan/sala1/sensor/temp"
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.username_pw_set(args.user, args.password)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

    client.on_message = on_message
    client.connect(args.host, args.port, keepalive=60)
    client.subscribe("lan/broadcast/cmd", qos=1)
    client.loop_start()

    print(f"[SALA1/TEMP] Esperando comando START...")

    try:
        while True:
            if running:
                valor = round(20 + random.uniform(-3, 5), 2)
                client.publish(topic, str(valor), qos=1)
                print(f"[SALA1/TEMP] -> {valor}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()

</pre>
Foto: <img width="1461" height="741" alt="image" src="https://github.com/user-attachments/assets/e757bb2f-9f92-4617-9bae-70e7bfb249b6" />

Terminal 3 – Script Sensor sala1/hum
<pre>
import argparse, ssl, time, random
import paho.mqtt.client as mqtt

running = False

def on_message(client, userdata, msg):
    global running
    comando = msg.payload.decode().lower()
    if comando == "start":
        running = True
        print("[sala1/hum] Recibido START → comenzando transmisión")
    elif comando == "stop":
        running = False
        print("[sala1/hum] Recibido STOP → deteniendo transmisión")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--interval", type=float, default=3.0)
    args = parser.parse_args()

    topic = "lan/sala1/sensor/hum"
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.username_pw_set(args.user, args.password)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

    client.on_message = on_message
    client.connect(args.host, args.port, keepalive=60)
    client.subscribe("lan/broadcast/cmd", qos=1)
    client.loop_start()

    print(f"[SALA1/HUM] Esperando comando START...")

    try:
        while True:
            if running:
                valor = round(40 + random.uniform(-15, 15), 2)
                client.publish(topic, str(valor), qos=1)
                print(f"[SALA1/HUM] -> {valor}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()

</pre>
Foto: <img width="1470" height="747" alt="image" src="https://github.com/user-attachments/assets/95a2cf6d-4fd0-4410-85a1-2ccef327be5f" />

Terminal 4 – Script Sensor sala2/temp
<pre>
import argparse, ssl, time, random
import paho.mqtt.client as mqtt

running = False

def on_message(client, userdata, msg):
    global running
    comando = msg.payload.decode().lower()
    if comando == "start":
        running = True
        print("[sala2/temp] Recibido START → comenzando transmisión")
    elif comando == "stop":
        running = False
        print("[sala2/temp] Recibido STOP → deteniendo transmisión")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--interval", type=float, default=2.5)
    args = parser.parse_args()

    topic = "lan/sala2/sensor/temp"
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.username_pw_set(args.user, args.password)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

    client.on_message = on_message
    client.connect(args.host, args.port, keepalive=60)
    client.subscribe("lan/broadcast/cmd", qos=1)
    client.loop_start()

    print(f"[SALA2/TEMP] Esperando comando START...")

    try:
        while True:
            if running:
                valor = round(18 + random.uniform(-2, 4), 2)
                client.publish(topic, str(valor), qos=1)
                print(f"[SALA2/TEMP] -> {valor}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()

</pre>
Foto: <img width="1458" height="748" alt="image" src="https://github.com/user-attachments/assets/d122e361-f9eb-465f-a95a-b856509820f7" />

Terminal 5 – Broadcast (comandos a todos)
<pre>
 import argparse, ssl
import paho.mqtt.client as mqtt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=8883)
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--cmd", required=True, help="start o stop")
    args = parser.parse_args()

    topic = "lan/broadcast/cmd"

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.username_pw_set(args.user, args.password)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS_CLIENT)

    print(f"[CMD] Enviando comando '{args.cmd}' a {topic}")
    client.connect(args.host, args.port, 60)

    client.publish(topic, args.cmd, qos=1)
    client.disconnect()

if __name__ == "__main__":
    main()
</pre>
Foto: 


### 6. Preguntas

**a) Protocolos de capa de transporte**

Como lo dice la documentación, MQTT  y por lo tanto el sistema, funciona sobre el protocolo TCP. Este protocolo garantiza la entrega ordenada y confiable de los paquetes, a diferencia de otros protocolos como UDP.

**b) Integridad, Confidencialidad y Disponibilidad** 

En cuanto a la integridad, al utilizar TCP nos garantizamos que los mensajes lleguen completos y sin errores, pero no nos garantiza protección contra ataques. En nuestro caso, también utilizamos TLS por lo tanto estamos protegidos en ese aspecto (Confidencialidad).
Como mencionamos anteriormente la disponibilidad del sistema depende del estado del broker, ya que este maneja la transmisión de todos los dispositivos (Pub/Sub). Si este se cae el sistema se cae.

**c) QoS**

La calidad de servicio de MQTT ofrece tres niveles de confiabilidad distintos, que se adaptan a diversos casos de uso de IoT que requieren diferentes niveles de confiabilidad según sus requisitos específicos.

- QoS 0 : QoS 0 ofrece mensajería "disparar y olvidar" sin acuse de recibo del receptor.

- QoS 1 : QoS 1 garantiza que los mensajes se entreguen al menos una vez al requerir un acuse de recibo PUBACK.

- QoS 2 : QoS 2 garantiza que cada mensaje se entregue exactamente una vez mediante un protocolo de enlace de cuatro pasos (PUBLISH, PUBREC, PUBREL, PUBCOMP).

Este enfoque por niveles permite a los desarrolladores tener más flexibilidad a la hora de diseñar sus sistemas.

**d) Ventajas del modelo pub/sub frente al modelo cliente-servidor**

El modelo publish/subscribe presenta varias ventajas importantes respecto al esquema tradicional cliente-servidor:

1. *Desacoplamiento entre dispositivos*
En pub/sub, el publicador y el suscriptor no necesitan conocerse entre sí. No deben saber la dirección IP ni el puerto del otro; solo deben conectarse al broker y trabajar mediante tópicos. Esto simplifica el diseño y permite agregar o quitar dispositivos sin modificar el sistema.

2. *Mayor tolerancia a fallos*
En un sistema cliente-servidor, si el servidor falla, todos los clientes pierden la comunicación. En cambio, en pub/sub, el broker puede almacenar mensajes (según el QoS configurado) y entregarlos cuando el cliente vuelva a conectarse, evitando pérdidas y mejorando la confiabilidad.

3. *Escalabilidad*
Gracias al desacoplamiento, esta arquitectura soporta fácilmente un gran número de clientes y mensajes. Cada dispositivo solo publica o se suscribe, mientras que el broker gestiona la distribución, lo que permite escalar el sistema sin grandes cambios.

4. *Flexibilidad*
MQTT ofrece distintos niveles de QoS, permitiendo seleccionar el grado de confiabilidad necesario para cada aplicación. Además, los tópicos jerárquicos y los comodines (+, #) hacen que el enrutamiento de mensajes sea muy flexible y fácil de organizar.
 
**e) Limitaciones de MQTT**

MQTT es ideal para aplicaciones IoT porque trabaja con mensajes pequeños y frecuentes. Sin embargo, cuando se necesita transferir datos de mayor tamaño como *archivos o imágenes* el protocolo deja de ser eficiente. Además, al depender de un intermediario (el broker) toda comunicación debe pasar por él, lo que introduce una latencia adicional respecto a una conexión directa entre dispositivos dentro de una red LAN.

**f) Broker central**

Como ya mencionamos el broker es el componente central que conecta a todos los dispositivos. Todos los mensajes deben pasar por él: los publishers envían sus datos al broker y los subscribers los reciben también desde ese mismo punto. Por lo tanto, el broker se convierte en un punto único de falla. Si el broker deja de funcionar, toda la red MQTT queda inmediatamente incomunicada.

Si bien la centralización tiene ventajas como:

- Controlar accesos.
- Registrar actividad.
- Ordenar los tópicos.
- Coordinar dispositivos.
- Realizar lógica de enrutamiento.

Esa misma centralización es lo que hace que el broker sea un componente demasiado crítico. 

---

## Discusión Y Conclusiones

Este Trabajo Práctico N.º 5 permitió adentrarse en el protocolo MQTT mediante la simulación del funcionamiento de una red local con múltiples dispositivos IoT. La experiencia facilitó la comprensión del modelo Publish/Subscribe y permitió analizar con mayor profundidad sus ventajas y limitaciones.

En una primera etapa se llevó a cabo una investigación teórica. Luego, con esos conocimientos, se procedió a la implementación práctica de los distintos componentes del sistema.

El desarrollo del trabajo permitió no solo implementar un sistema funcional, sino también analizar las caracteristicas de MQTT en un entorno controlado.

En conclusión, MQTT se presenta como una solución robusta, simple y flexible para redes de sensores y sistemas de automatización, siempre que se consideren cuidadosamente sus restricciones y se utilicen configuraciones adecuadas según el entorno y los objetivos de la aplicación.

---

## Referencias

- MQTT: https://mqtt.org/
- HiveMQ: https://www.hivemq.com/
