# Trabajo Práctico N°3

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Comunicaciones de Datos**</br>
**Santiago Martin Henn** </br>
**Miguel Ángel Solinas**</br>
**22/09/2025**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Resumen

En el desarrollo de este trabajo práctico de laboratorio se investigan los principales estándares de redes locales, las versiones recientes de Wi-Fi y las características que diferencian los medios guiados de los inalámbricos. También se analizan la Ley de Snell y su relación con la propagación de la luz en fibras ópticas, así como la seguridad asociada a distintas versiones de los protocolos.

Se recopilan y comparan las propiedades de protocolos inalámbricos como Bluetooth, ZigBee, LTE, 5G o LoRa, considerando su alcance y tasa de transmisión. Finalmente, se examinan las tecnologías que permiten acceso a internet en vuelo, sus limitaciones y la forma en que se gestiona el tráfico entre servicios locales y globales.

---

## Introducción

El presente informe de este trabajo práctico de laboratorio está enfocado en el análisis de las capas de acceso en redes locales, los estándares asociados y los fundamentos físicos que las sustentan. Se busca comprender la evolución de los protocolos más utilizados, como IEEE 802.3 y 802.11, y su impacto en la transmisión de datos.

A lo largo del trabajo se abordan tecnologías cableadas e inalámbricas, destacando la fibra óptica y sus modos de propagación, así como protocolos de comunicación relevantes en el ámbito del IoT y las redes móviles. Además, se exploran casos actuales, como la conectividad en aviones, integrando teoría y aplicaciones reales.

---

## Desarrollo

### 1. Normalización y estandarización de las tecnologías

**a)**

*IEEE 802.3*:

- Historia: Fue desarrollada en los años 70 por Xerox PARC, con los primeros cables coaxiles como medio de transmisión. En 1983, fue estandarizado por la IEEE como 802.3. Inicialmente funcionaba a 10Mbps sobre cable coaxil con CSMA/CD, pero luego evoluciono a 100Mbps(*Fast Ethernet*), 1Gbps(Gigabit Ethernet), y actualmente llega a 400Gbps y 800Gbps usando par trenzado y fibra óptica.

- Campo de Aplicación: Es utilizado principalmente en redes de area local (*LAN*) cableadas, interconexiónes de backbone y aplicaciones industriales.

*IEEE 802.11*:

- Historia: El estándar original se aprobó en 1997 con velocidades de 1–2 Mbps. En 1999 aparecieron 802.11a (5 GHz, 54 Mbps) y 802.11b (2.4 GHz, 11 Mbps). Luego vinieron 802.11g (2003, 54 Mbps en 2.4 GHz), 802.11n (2009, hasta 600 Mbps con MIMO), 802.11ac (2013, WiFi 5, hasta 7 Gbps), 802.11ax (2019, WiFi 6/6E, hasta 9.6 Gbps con OFDMA y 6 GHz) y actualmente 802.11be (WiFi 7) en desarrollo.

- Campo de Aplicación: Es utilizado en redes de area local inalámbricas(WLAN). También es muy utilizado en las aplicaciones de IoT, que son muy populares hoy en día.

**b)** **FALTA EJERCICIO DE LA FACU**

**c)**
Cuando una red Wi-Fi opera bajo un determinado protocolo y un dispositivo posee una tarjeta de red inalámbrica (NIC) que solo soporta un estándar más antiguo, pueden ocurrir dos situaciones:

1. Los estándares de la familia 802.11 fueron diseñados en gran medida para mantener compatibilidad hacia atrás, es decir, el punto de acceso es retrocompatible. En este caso, el dispositivo podrá conectarse, pero lo hará utilizando las características de la versión más antigua soportada. Esto genera una degradación en la experiencia del usuario, ya que no podrá aprovechar las ventajas del protocolo más reciente, como mayores tasas de datos o nuevas funciones de seguridad.

2. También se puede dar la situación en la que el administrador de la red configure el punto de acceso para trabajar únicamente con protocolos nuevos, entonces los dispositivos con hardware antiguo no podrán asociarse a la red. Esta decisión suele tomarse en redes que priorizan rendimiento y seguridad.

**d)** **FALTA EJERCICIO DE LA FACU**
La evolución de los protocolos IEEE 802.11 no solo ha incrementado las tasas de transmisión y la eficiencia espectral, sino que también ha estado fuertemente vinculada a mejoras en los mecanismos de seguridad. Cada nueva versión incorporó o reforzó algoritmos de autenticación y cifrado para enfrentar vulnerabilidades descubiertas en estándares previos.

**e)**
<div align="center">

|                    |**Wi-Fi 5**|**Wi-Fi 6**|**Wi-Fi 7**|
|--------------------|-----------|-----------|-----------|
|Versión IEEE        |  802.11ac | 802.11ax  ̣| 802.11be  |
|Tasa de Datos Máxima|  ~ 7Gbps  | ~ 10Gbps  | > 30Gbps  |
|Bandas              |   5 GHz   |2.4/5/6 GHz|2.4/5/6 GHz|
|Ancho de Banda      |Max 160 MHz|Max 160 MHz|Max 320 MHz|
|Modulación          |  256 QAM  |  1024 QAM |  4096 QAM |
|Sistema de Seguridad|   WPA2    |   WPA3    |   WPA3    |

</div>

### 2. Transmisiones en Fibra Óptica

**a)** En la figura se muestran dos formas de propagación de la luz en una fibra óptica:

   1. **Fibra monomodo (izquierda):** la luz viaja en línea recta por el núcleo, sin rebotar. Se utiliza un núcleo muy delgado (aproximadamende entre 8-10 micrómetros). Permite transmitir a largas distancias con muy baja atenuación y mínima dispersión. Es la opción más costoda, ya que requiere fuentes de luz láser y mayor precisión en la fabricación.
   2. **Fibra multimodo (derecha):** la luz viaja rebotando dentro del núcleo en distintos ángulos o modos. El núcleo es más ancho (entre 50-62,5 micrómetros). Tiene mayor dispersión modal, lo que limita la distancia y la velocidad de transmisión. Es más barata de implementar porque suele usarse LED como fuente de luz.

Entonces, las principales diferencias son que la fibra monomodo es más cara, y tiene mayor capacidad y alcance, mientras que la fibra multimodo es más económica pero tiene un menor alcance y velocidad.

**b)** La Ley de Snell establece la relación entre los ángulos de incidencia y refracción al pasar la luz de un medio a otro, donde $n$ es el índice de refracción del medio. 

$$n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$$

En relación con la fibra óptica, el núcleo tiene un índice de refracción mayor que el revestimiento, lo que provoca que la luz que incide con cierto ángulo se refleje totalmente dentro del núcleo, lo cual se conoce como reflexión interna total. Además, según el ángulo de entrada, como se observa en las imágenes, pueden existir distintos modos de propagación (multimodo) o único modo (monomodo).

**c)** Como similitudes entre las conexiones inalámbricas y las transmisiones en fibra óptica, podemos mencionar que ambos transportan información mediante ondas electromagnéticas (en la fibra, en forma de luz; en lo inalámbrico, en radiofrecuencia). Además, en los dos casos la señal está sujera a fenómenos de atenuación, interferencia o dispersión.

Por otro lado, se pueden destacar como diferencias clave que la fibra es un medio guiado, con un recorrido fijo y protegido, mientras que las inalámbricas son no guiadas, propagándose por el espacio abierto. Se puede agregar que la fibra suele ofrecer mayor capacidad y confiabilidad, en cambio las inalámbricas ofrecen movilidad y flexibilidad.

En redes modernas, según explica Kurose-Ross, ambas tecnologías son complementarias, ya que la fibra se usa en el backbone de alta capacidad y los enlaces inalámbricos para la última milla o acceso del usuario.

### 3. Protocolos de comunicación inalámbrica

**a)**

**b)**

**c)**

### 4. Estado del arte

**a)** Las tecnologías que permiten Internet en el vuelo son las siguientes:

- **Satélites:** estos satélites retransmiten la señal entre la aeronave y estaciones terrestres. El avión lleva antenas orientables o electrónicamente ditigidas para conectarse al satélite. La principal ventaja es que tienen cobertura global, sobre océanos y zonas remotas, y además pueden dar buen ancho de banda. Algunas de las limitaciones son la latencia alta (aprox. 500 ms o más ida y vuelta), el coste de equipamiento y de operación, consumo de energía, atenuación por lluvia u otros fenómenos atmosféricos en bandas altas, visibilidad del satélite, etc.
- **Air-to-Ground (ATG):** se usan redes terrestres celulares / torres de comunicación con antenas "vista al cielo" o con lobos dirigidos hacia aviones. El avión lleva antenas que se conectan con esas torres. Su principal ventaja es que tiene mucha menor latencia que los satélites, menor coste por bit y equipamiento más simple y ligero. La mayor limitacion es su cobertura limitada, ya que no funciona sobre océanos o zonas sin infraestructura, y además puede tener interferencia o congestión si hay muchas aeronaves o móviles.

**b)** Publicación científico/tecnológica relacionada con el tema: 

**From GEO to LEO: First Look Into Starlink In-Flight Connectivity**, de los autores: Daniel Jang, Matteo Varvello, Aravindh Raman, Yasir Zaki.

Este estudio compara el rendimiento de la conectividad a bordo entre satélites geostacionarios (GEO) y la constelación de satélites de órbita baja (LEO) Starlink. Se realizaron mediciones en 26 vuelos de 7 aerolíneas diferentes utilizando dispositivos Android con la plataforma AmiGo. Los resultados mostraron que Starlink ofrece latencias significativamente menores y mayor ancho de banda en comparación con los sistemas GEO. Sin embargo, también se identificaron desafíos relacionados con la selección dinámica de gateways, problemas de DNS y la influencia de algoritmos de control de congestión en el rendimiento.

**c)** En muchos aviones con WiFi a bordo y un sistema de entretenimiento, hay dos fuentes de tráfico:

- Tráfico local: es el contenido de entretenimiento que está "hosteado" a bordo, en servidores dentro del avión o conectado localmente. El mismo no sale hacia internet, sino que se transmite localmente en la red interna del avión, quizás mediante WiFi local o una red interna, sin usar el enlace satelital o el ATG.
- Tráfico hacia afuera / internet: este tráfico (correo, navegación web, redes sociales, etc.) sí pasa por el enlace externo, ya sea de satélite o ATG.

Con respecto al ancho de banda, el contenido local puede consumir mucho si hay muchas personas viendo la misma película, pero como es local no se ve afectado por latencia de enlace externo. Por su parte, el internet externo sí: latencia, pérdida de paquetes y ancho de banda limitado.

---

## Discusión Y Conclusiones



---

## Referencias

Kurose, J. F., & Ross, K. W. (2017). Redes de computadoras: Un enfoque descendente (7.ª ed.). Pearson.
