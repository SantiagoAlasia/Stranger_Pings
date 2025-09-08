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

En la primera parte del trabajo se analizaron los fenómenos físicos asociados a la transmisión de señales (como el efecto Doppler, el ruido y la interferencia electromagnética) y su impacto sobre distintos tipos de transmisión de datos. Asimismo, se estudió el concepto de SNR y se lo relacionó con el concepto previamente abordado de BER. Finalmente, se llevaron a cabo análisis vinculados con la capa de enlace de datos.

---

## Introducción

El presente trabajo de laboratorio tiene como objetivos terminar de repasar conceptos fundamentales inherentes a la capa física, y entender los conceptos relacionados con la capa de enlace de datos. Asimismo, se empleó la herramienta Wireshark para capturar tráfico de paquetes y observar de manera práctica la aplicación de los conceptos estudiados a lo largo del trabajo.

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
**a)**
**b)**
**c)**
**d)**
**e)**

### 4.

---

## Discusión Y Conclusiones

---

## Referencias
{}