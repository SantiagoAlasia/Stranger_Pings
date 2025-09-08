# Trabajo Práctico N°2

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Comunicaciones de Datos**</br>
**Santiago Martin Henn** </br>
**Miguel Ángel Solinas**</br>
**8/09/2025**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Resumen

En este trabajo se analizaron los fenómenos físicos que afectan la transmisión de señales, como el efecto Doppler, el ruido y la interferencia electromagnética, y su impacto sobre distintos tipos de transmisión de datos. Se estudió la relación entre la relación señal-ruido (SNR) y la tasa de error de bits (BER), y se abordaron aspectos de la capa de enlace de datos, con énfasis en Ethernet, direcciones MAC y cables UTP. Además, se utilizó Wireshark para capturar y analizar tráfico de red, y se reflexionó sobre la trazabilidad de identificadores únicos de dispositivos y la protección de la privacidad mediante VPN.

---

## Introducción

El presente trabajo de laboratorio tiene como objetivo profundizar en los conceptos de la capa física y de la capa de enlace de datos, explorando cómo los fenómenos físicos afectan la transmisión de señales y cómo se gestionan los errores en las redes. Para ello se empleó Wireshark, permitiendo capturar y analizar paquetes de red de manera práctica. Además, se estudiaron identificadores únicos de dispositivos, como direcciones MAC y IMEI, y su relación con la privacidad en las comunicaciones digitales.

---

## Desarrollo
### 1.
**a)** En la figura del enunciado podemos notar una variación de la frecuencia de la señal, este fenómeno puede ser explicado por el efecto Doppler. Cuando un dispositivo móvil se aproxima o se aleja de la fuente de transmisión, las ondas de radio que se propagan entre ambos se comprimen o se expanden. Esta variación en la longitud de onda produce un desplazamiento de frecuencia, es decir, la señal recibida presenta una frecuencia distinta de la originalmente transmitida.

Esta diferencia de frecuencias puede ser calculada como:

$$\Delta f = \frac{\Delta v}{v} * f_0$$

**b)** El efecto Doppler afecta más a las transmisiones que implican un movimiento relativo significativo entre el transmisor y el receptor, como en la comunicación satélital o con vehículos aéreos. 

**c)** Los celulares no se pueden encender en los aviones ya que estos pueden generar interferencia con los sistemas de comunicación del avión.

### 2.
**a)** En la figura podemos ver como se intrduce ruido/interferencia electromagnetica en la señal debido a una herramienta electrica. Este fenomeno fisico ocaciona perturbaciones en la señal lo que complica la desmodulacion de la misma.

**b)** La transmisión mas afectada por el *ruido o interferencia electromagnética (EMI)* es la transmisión analógica. Como las señales analógicas son continuas, cualquier variación en el valor de la señal, puede interpretarse como parte de la señal.

En cambio,  la transmisión digital es significativamente más resilientes al ruido. Como la información se transmite en valores discretos, aunque el ruido puede alterar la señal, los receptores digitales están diseñados para distinguir entre los dos estados.

El tipo de transmisión que es inmune al ruido e interferencia electromagnética es la fibra óptica. Al transmitir la información con pulsos de luz, esta no se ve afectada por este fenómeno electromagnético. 

**c)** *Signal to Noise Ratio (SNR)* es una medida que nos permite comparar la potencia de la señal con la potencia del ruido presente en el canal. Se suele medir en decibelio $[dB]$ y se puede calcular como:

$$SNR[dB] = 10 * \log {(\frac{P_{señal}}{P_{ruido}})}$$

> Nota: Mientras mas alto el valor de $SNR$, la señal llegara con mejor calidad.

Como ya se reviso en el TP01, el *Bit Error Rato (BER)* nos indica la probabilidad de que el bit recibido sea distinto del transmitido. En un canal con bajo nivel de SNR (la potencia del ruido es mayor a la potencia de la señal), se espera un valor alto de BER ya que el efecto del ruido electromagnético en el canal es mayor al de la señal.

### 3. 
**a)** **Ethernet** Es una tecnologìa de capas de enlace de datos (capa 2 del modelo OSI), usada en redes LAN. Su mision es encapsular los datos de protocolos superiores (IP, ARP, IPv6, etc.) en tramas Ethernet y entregarlos de un dispositivo a otro dentro de la misma red local. 
Define:
- Direccionamiento físico (MAC): 48 bits, AA:BB:CC:DD:EE:FF
- Formato de trama
- Velocidades
- Medio Físico: cable, fira optica, etc.
- 
La estructura de la trama típica es aquella dada por Ethernet II:

|Destino MAC (6B) | Origen MAC (6B) | EtherType (2B) | Payload (46-1500B) | FCS (4B) |
  1. Destino MAC: a que equipo va dirigido el frame
  2. Origen MAC: identifica quien envía
  3. EtherType: qué protocolo está transportando
  4. Payload: datos reales
  5. FCS: campo de control de errores

**DIFERENCIAS ENTRE ETHERNET/ FAST ETHERNET/ GIGABIT ETHERNET** 

**VERSIÓN**          |     **VELOCIDAD**     |  **MEDIO TÍPICO**  

ETHERNET                     10 Mbps                UTP Cat3/5       

FAST ETHERNET                100 Mbps               UTP Cat5/5e        
 
GIGABIT ETHERNET             1 Gbps                 UTP Cat5e/6

<img width="1491" height="201" alt="image" src="https://github.com/user-attachments/assets/7c8b9f46-1420-4470-bc1b-7c4cebd9d5cb" />

En Esta figura observamos la sección 'Ethernet II' de un paquete ICMP capturado en Wireshark. El campo Destination corresponde a la MAC del router, mientras que el campo Source corresponde a la MAC de la interfaz local. El Ether type indica 0x0800, lo que señala que la carga es un paquete IPv4.

**b)** Un **Cable UTP**  es un cable de par trenzado no apantallado. Cada par de hilos (normalmente 4 pares u 8 hilos) se trenza para reducir interferencia. Es muy utilizado en Ethernet. 

El trenzado reduce la diafonía o crosstalk y las interferencias externas porque las señales se transmiten de modo diferencial. Un UTP de categoría más alta tiene trenzados mas firmes y por lo tanto mayor inmunidad al ruido y mayor capacidad de transmisión. 

El **Cable derecho** se usa típicamente enre la PC y un switch/router con el mismo pinout en ambos extremos.

El **Cable Cruzado** invierte pares Tx y Rx, se usa típicamente para conectar Switch-Switch o PC-PC.


**c)** La puerta de enlace predeterminada detectada fue: 192.168.100.1
<img width="1515" height="829" alt="image" src="https://github.com/user-attachments/assets/837ea9e8-3154-4cd3-a53a-ea2208489864" />

En esta captura se observa un paquete ICMP Echo Reply enviado por la puerta de enlace (192.168.100.86). En el encabezado Ethernet II se identifica como dirección MAC origen a4:00:e2:3a:69:9b (router Huawei) y como destino c4:75:ab:e9:a8:f9 (placa Intel de mi PC). El campo EthernetType (0x0800) indica que la carga es IPv4. Dentro del encabezado IP, el protocolo es el ICMP(1), y el bloque ICMP muestra un mensaje de tipo 0 (Echo Reply) con identificador 0x0001 y secuencia 4. El campo de datos contiene la cadena ASCII 'abcdef...', que corresponde al payload estandar del ping. El tamaño del frame fue de 74 bytes, lo que coincide con los campos Ethernet + IPv4 + ICMP + datos. 

**d)** La dirección MAC del gateway obtenida fue a4:00:e2:3a:69:9b. Los 3 primeros bytes (a4:00:e2) corresponden al OUI registrado por Huawei Technologies Co., Ltd., lo que confirma que el dispositivo que actúa como puerta de enlace es un router Huawei. Esto evidencia que la MAC no solo permite identificar de manera única a un equipo dentro de la red local, sino tambiín obtener información sobre el fabricante del hardware. 

Fuentes de información: https://maclookup.app/


**e)**

### 4.
La dirección MAC es un identificador único de cada dispositivo en la LAN, lo que implica que puede usarse para rastrear y distinguir a los usuarios dentro de una red local. Sin embargo, hacia Internet los servidores remotos no reciben la MAC, sino únicamente la dirección IP pública. 

El IMEI cumple un rol equivalente a la MAC pero en redes celulares: permite a los operadores móviles identificar y rastrear equipos. Tanto la MAC como el IMEI son identificadores únicos de hardware que comprometen la privacidad si son usados para trazabilidad 

El uso de una VPN no oculta dirección MAC en la LAN, ya que las tramas Ethernet siguen utilizando la MAC real del dispositivo para llegar al Router. La VPN sí cifra los datos y cambia la IP visible para los destinos remotos pero no modifica la información a nivel de capa de enlace. 


---

## Discusión Y Conclusione

El trabajo permitió entender los fundamentos de las redes, las interferencias en el medio físico y la función del Ethernet. Con Wireshark se analizaron tramas, direcciones MAC y fabricantes, comprobando como la comunicación difiere en una LAN y en Internet. Finalmente, se reflexionó sobre la trazabilidad de la MAC, su similitud con el IMEI y el rol de la VPN en la proteccion de la privacidad. 

---

## Referencias
{}
