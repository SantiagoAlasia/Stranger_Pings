# Trabajo Práctico N°4

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

El Trabajo Práctico N°4 aborda la configuración y segmentación de redes LAN a través de la creación de VLANs, el uso del protocolo IEEE 802.1Q y la práctica con dispositivos de red locales. Se realizan ejercicios de configuración básica y pruebas de conectividad entre equipos. Finalmente, se aplica lo aprendido en una simulación de red a bordo de una aeronave, donde se utilizan NAT, ACLs y DHCP para definir distintos niveles de acceso según el tipo de usuario. El trabajo integra teoría y práctica, fortaleciendo la comprensión del funcionamiento de las redes locales.

---

## Introducción

En este trabajo práctico se estudian las capas de acceso en redes locales, sus protocolos y estándares principales, y la forma en que permiten la comunicación entre distintos dispositivos. Mediante el uso de Cisco Packet Tracer, se configuran switches, routers y VLANs, aplicando conceptos como NAT y ACLs. El objetivo es comprender cómo se estructuran, segmentan y administran las redes LAN, y cómo estos mecanismos garantizan conectividad y control del tráfico en entornos reales.

---

## Desarrollo

### 1. Alcance de Redes y Virtualización

**a)** Clasificación de las redes según su alcance. Las redes se clasifican según su tamaño, cobertura geográfica y propósito.

- **PAN (Personal Area Network):** red de área personal. Conecta dispositivos cercanos a una persona (como celular, smartwatch o auriculares Bluetooth). Su alcance es de pocos metros.

- **LAN (Local Area Network):** red de área local. Cubre espacios reducidos como un hogar, oficina o institución. Usa medios cableados o inalámbricos y ofrece altas velocidades de transmisión.

- **MAN (Metropolitan Area Network):** red metropolitana. Conecta varias LAN dentro de una ciudad o campus. Utiliza infraestructura pública o privada.

- **WAN (Wide Area Network):** red de área amplia. Conecta redes distribuidas en grandes distancias, incluso países. Internet es el ejemplo más representativo.

- **WLAN (Wireless LAN):** red LAN inalámbrica basada en el estándar IEEE 802.11 (Wi-Fi), que permite la conexión sin cables dentro de un área local.

**b)** Una VLAN (Virtual Local Area Network) es una red local lógica que se crea dentro de un switch para segmentar el tráfico sin necesidad de separar físicamente los dispositivos. Permite agrupar equipos por función, área o nivel de seguridad, mejorando el rendimiento y la administración de la red.

Clasificación:

- **Estáticas (por puerto):** el administrador asigna manualmente cada puerto del switch a una VLAN.

- **Dinámicas:** la asignación se realiza automáticamente según criterios como dirección MAC, protocolo o autenticación.

**c)** El estándar IEEE 802.1Q define el mecanismo para identificar y manejar múltiples VLANs en una misma conexión física.
Agrega una etiqueta (tag) de 4 bytes en el encabezado Ethernet que indica a qué VLAN pertenece cada trama. Esta etiqueta permite que varios switches compartan información de VLANs a través de enlaces trunk, manteniendo la separación lógica entre redes.

**Relación con VLAN:**

El protocolo 802.1Q es el que permite el transporte simultáneo de varias VLAN sobre un mismo enlace, garantizando que las tramas lleguen solo a los dispositivos de su misma VLAN.

**d)** El tagging es el proceso de añadir o leer la etiqueta 802.1Q en las tramas Ethernet. Esta etiqueta identifica la VLAN de origen y permite que los switches y routers distingan el tráfico de distintas VLANs cuando viajan por un enlace trunk.

Cuando la trama llega a su destino final (una interfaz de acceso), la etiqueta se elimina (untagged), entregando la información al dispositivo como si perteneciera a una única red.

### 2. Implementación en Packet-Tracer



### 3. Despliegue de red LAN a bordo de una aeronave

En este ejercicio se implementó una red de área local segmentada mediante VLANs utilizando Cisco Packet Tracer. El objetivo principal fue configurar un switch con tres VLANs distintas (Turista, Business y Administración), y un router que actúe como punto de interconexión entre ellas mediante la técnica Router-on-a-Stick.

Además, se estableció un enlace con un router ISP, simulando la conexión a Internet, y se configuraron las direcciones IP correspondientes a cada subred para permitir el enrutamiento interno y el acceso externo según las políticas del enunciado.

**Diagrama general de la red**

<img width="827" height="514" alt="Captura de pantalla 2025-11-13 003800" src="https://github.com/user-attachments/assets/fe7c47f8-f49e-49c8-8e00-6135603d474a" />

La red se compone de un router principal conectado a un switch, al cual se asocian distintos dispositivos distribuidos en tres VLANs.
El router secundario (ISP) representa la conexión hacia Internet.
Cada grupo de usuarios y el servidor se encuentran en subredes diferentes para garantizar la segmentación lógica del tráfico.

**Configuración del switch**

<img width="652" height="196" alt="Captura de pantalla 2025-11-13 003732" src="https://github.com/user-attachments/assets/db0efbc0-b8c6-438a-abf1-842b58c4a36e" />

Se crearon las VLAN 10 (Turista), 20 (Business) y 99 (Admin) y se asignaron los puertos correspondientes según cada grupo de usuarios.


**Configuración del router principal**

<img width="662" height="98" alt="image" src="https://github.com/user-attachments/assets/a9368154-64d7-4cf9-9237-17d0d2f36f11" />

Se configuraron subinterfaces para cada VLAN con encapsulación 802.1Q, permitiendo la comunicación entre redes internas mediante un único enlace trunk con el switch.

**Enlace con el ISP**

<img width="654" height="38" alt="image" src="https://github.com/user-attachments/assets/8e2db2a1-324a-4124-996d-b25f1c24db66" />

Se configuró la red 200.0.0.0/30 para la interconexión entre ambos routers, garantizando la conectividad hacia la red externa.

**IP DHCP de las laptops**

<img width="867" height="456" alt="image" src="https://github.com/user-attachments/assets/21571372-5448-4a4f-9009-41b32aef4211" />

<img width="860" height="482" alt="image" src="https://github.com/user-attachments/assets/eacb057f-ad06-4efb-8a17-ebebd0a09358" />

<img width="865" height="450" alt="image" src="https://github.com/user-attachments/assets/6a6ec3af-ae18-4dc3-955a-40a03decb83c" />

Las capturas evidencian que los equipos conectados a cada VLAN reciben automáticamente una dirección IP válida dentro de su red, junto con la máscara y el gateway predeterminado asignado (10.10.x.11).

Esto confirma el correcto funcionamiento del servidor DHCP implementado en el router y la adecuada segmentación del tráfico mediante VLANs.

Además, la obtención automática de direcciones IP valida la comunicación entre el switch y el router a través del enlace trunk 802.1Q, el cual transporta las tramas etiquetadas de cada VLAN hasta el router (“Router-on-a-Stick”) para su administración centralizada.

**Configuración de la traducción de direcciones NAT**

<img width="554" height="134" alt="image" src="https://github.com/user-attachments/assets/e658d8e3-02ee-4870-89b8-a710ea3b5e55" />

Se observa la implementación de NAT con sobrecarga (PAT), que permite que las redes internas Business (10.10.20.0/24) y Administración (10.10.99.0/24) accedan a Internet utilizando la dirección pública 200.0.0.1 del router principal.

**Tabla de traducciones NAT**

<img width="621" height="173" alt="image" src="https://github.com/user-attachments/assets/1b4829e8-cf90-4bdd-a680-7e185079d50d" />

Cada dirección interna es traducida a la IP pública del router principal, lo que confirma la correcta operación del mecanismo de NAT.

**Laptop Business**

<img width="468" height="443" alt="image" src="https://github.com/user-attachments/assets/4e35e5b7-8778-40a1-8831-8c25db47a160" />

El equipo de la VLAN 20 logra comunicarse con el host 8.8.8.8 y con el host 200.0.0.2, demostrando que el NAT traduce correctamente las direcciones internas hacia la red externa.

**Laptop Turista**

<img width="479" height="180" alt="image" src="https://github.com/user-attachments/assets/c3a3817c-1e0b-47a4-98fd-c535a4cde23b" />

El filtrado mediante listas de control de acceso (ACL) impide que los dispositivos de la VLAN 10 accedan a Internet, cumpliendo con la política de seguridad establecida.



---

## Discusión Y Conclusiones

---

## Referencias
