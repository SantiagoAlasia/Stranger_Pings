# Trabajo Práctico N°1

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Comunicaciones de Datos**</br>
**Santiago Martin Henn** </br>
**Miguel Ángel Solinas**</br>
**25/08/2025**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: 
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Resumen

---

## Introducción


## Desarrollo

### 1. Resumen breve de fundamentos básicos y escenciales

- Ondas electromagnéticas.

 Son perturbaciones que se propagan en el espacio, formadas por campos eléctricos y magnéticos que oscilan de mandera perpendicular entre sí y a la dirección de propagación. No requieren un medio material, por lo que pueden transmitirse incluso en el vacío. Están caracterizadas por su longitud de onda y su frecuencia.

- Modulación.

Es el proceso mediante el cual una señal de información (de baja frecuencia) se combina con una señal portadora de alta frecuencia, para su transmisión a través de un medio.

- Demodulación.

Es el proceso inverso a la modulación, se realiza en el receptor para recuperar la señal de información original a partir de la señal modulada recibida.

- Señales de tiempo continuo.

Son aquellas cuya variable independiente, generalmente el tiempo (*t*), puede tomar cualquier valor real dentro de un intervalo, formando un dominio continuo.

- Señales de tiempo discreto.

Son señales representadas por una secuencia de valores definidos únicamente en instantes de tiempo específicos, en lugar de en cada momento posible.

**b)** Considerando que esta onda viaja exactamente a la velocidad de la luz, tenemos:
- Longitud de onda: $ \lambda = 60mm = 0,06m $
- Frecuencia: $f = \frac{c}{\lambda} = \frac{3.10^8}{0,06} = 5 GHz$

**c)** Esta onda electromagnética, al tener una frecuencia de 5 GHz, opera en la banda SHF (Super High Frequency), ya que la misma abarca el rango de frecuencias de 3 a 30 GHz.

**d)** Uno de los dispositivos para comunicaciones que opera en esta banda son, por ejemplo, los bucles locales inalámbricos (WLL - Wireless Local Loop), los cuales están diseñados específicamente para proveer acceso de telefonía y transmisión de datos (internet, voz, fax) entre el abonado y la central, reemplazando el par de cobre por un enlace radioeléctrico.

**e)** Con la línea de trazos roja en la figura se representa la atenuación de la onda. Este fenómeno demuestra como, a medida que la onda se propaga, su intensidad va disminuyendo con la distancia. Esto sucede porque parte de la energía se dispersa o se pierde, lo que provoca un decrecimiento prograsivo de la amplitud.

**f)** El fenómeno de la atenuación sí afecta a los bucles locales inalámbricos, porque la señal de radio que conecta al abonado con la estación base pierde intensidad con la distancia y los obstáculos. Un ejemplo cotidiano de esto es cuando, en una zona rural, se usa WLL para acceder a telefonía o internet. Si la vivienda está muy lejos de la torre o hay árboles o lluvia intensa, la señal se debilita y se pueden notar cortes en la comunicación o baja velocidad de conexión.

**g)** 
- i) La atenuación sí afecta a las transmisiones de telefonía celular, ya que provoca una pérdida de intensidad a la señal a medida que viaja por el espacio o atraviesa obstáculos tales como edificios, árboles o paredes. Esto puede reducir la calidad de la comunicación, generar interferencias o incluso pérdida de la conexión si la señal llega demasiado débil al receptor.

- ii) Las transmisiones por cable coaxial también se ven afectadas por la atenuación, en este tipo de transmisiones la señal se debilita por la resistencia del conductor y las pérdidas en el aislamiento, especialmente en largas distancias, lo que obliga a usar amplificadores.

- iii) En las transmisiones por fibra óptica, la atenuación es mucho menor que en otros medios, y se produce principalmente por absorción y dispersión de la luz dentro de la fibra, requiriendo en enlaces muy extensos el uso de regeneradores ópticos.

### 2. Comunicación de Datos
**a)** En la figura podemos observar dos señales: una de datos y otra de reloj. Este coneccion corresponde a una comunicación serial síncrona, en la cual la señal de reloj es utilizada por el receptor para muestrear los bits de datos en los instantes correctos, garantizando que la información sea interpretada de manera confiable. 

**b)** 

**c)** En este caso, se desea transmitir el símbolo ‘a’, cuya codificación en ASCII corresponde al byte 01100001. A partir de esta representación binaria, es posible deducir la forma que adoptará la señal durante la transmisión.

![Figura1: Codificación ASCII de la letra "a"](img/Figura1-Codificacion%20ASCII.drawio.png) 

**d)** Para determinar el valor de la señal, se debe realizar la medición en el centro de la celda de cada bit. En el caso de la figura mostrada más abajo, la muestra debería tomarse en el instante de tiempo correspondiente a T4. De esta manera, se garantiza que el valor de la señal en cada celda sea el correcto.

![Figura2: Momento de muestreo de la señal](img/Figura2-MuestreoDeLaSeñal.png)

### 3.
**a)**

**b)**
![Figura3: Modulación PSK](img/Figura3-ModulacionPSK.drawio.png)

**c)**

**d)**

### 4.

---

## Discusión Y Conclusiones

---

## Referencias

Stallings, W. (2004). Comunicaciones y redes de computadoras (7.ª ed.). Pearson Education.

