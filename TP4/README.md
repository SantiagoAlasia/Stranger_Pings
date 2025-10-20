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

---

## Discusión Y Conclusiones

---

## Referencias
