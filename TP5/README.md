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

### 2. 3. 4. Broker MQTT



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
