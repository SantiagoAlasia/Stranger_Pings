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

**b)**

**c)**

**d)**

**e)**

### 2. Transmisiones en Fibra Óptica

**a)** En la figura se muestran dos formas de propagación de la luz en una fibra óptica:

   1. **Fibra monomodo (izquierda):** la luz viaja en línea recta por el núcleo, sin rebotar. Se utiliza un núcleo muy delgado (aproximadamende entre 8-10 micrómetros). Permite transmitir a largas distancias con muy baja atenuación y mínima dispersión. Es la opción más costoda, ya que requiere fuentes de luz láser y mayor precisión en la fabricación.
   2. **Fibra multimodo (derecha):** la luz viaja rebotando dentro del núcleo en distintos ángulos o modos. El núcleo es más ancho (entre 50-62,5 micrómetros). Tiene mayor dispersión modal, lo que limita la distancia y la velocidad de transmisión. Es más barata de implementar porque suele usarse LED como fuente de luz.

Entonces, las principales diferencias son que la fibra monomodo es más cara, y tiene mayor capacidad y alcance, mientras que la fibra multimodo es más económica pero tiene un menor alcance y velocidad.

**b)** La Ley de Snell establece la relación entre los ángulos de incidencia y refracción al pasar la luz de un medio a otro, donde $n$ es el índice de refracción del medio. 

$n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$

En relación con la fibra óptica, el núcleo tiene un índice de refracción mayor que el revestimiento, lo que provoca que la luz que incide con cierto ángulo se refleje totalmente dentro del núcleo, lo cual se conoce como reflexión interna total. Además, según el ángulo de entrada, como se observa en las imágenes, pueden existir distintos modos de propagación (multimodo) o único modo (monomodo).

**c)** Como similitudes entre las conexiones inalámbricas y las transmisiones en fibra óptica, podemos mencionar que ambos transportan información mediante ondas electromagnéticas (en la fibra, en forma de luz; en lo inalámbrico, en radiofrecuencia). Además, en los dos casos la señal está sujera a fenómenos de atenuación, interferencia o dispersión.

Por otro lado, se pueden destacar como diferencias clave que la fibra es un medio guiado, con un recorrido fijo y protegido, mientras que las inalámbricas son no guiadas, propagándose por el espacio abierto. Se puede agregar que la fibra suele ofrecer mayor capacidad y confiabilidad, en cambio las inalámbricas ofrecen movilidad y flexibilidad.

En redes modernas, según explica Kurose-Ross, ambas tecnologías son complementarias, ya que la fibra se usa en el backbone de alta capacidad y los enlaces inalámbricos para la última milla o acceso del usuario.

### 3. Protocolos de comunicación inalámbrica

**a)**

**b)**

**c)**

### 4. Estado del arte

**a)**

**b)**

**c)**

---

## Discusión Y Conclusiones



---

## Referencias

Kurose, J. F., & Ross, K. W. (2017). Redes de computadoras: Un enfoque descendente (7.ª ed.). Pearson.
