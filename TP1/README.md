# Trabajo Práctico N°1

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Redes de Computadoras**</br>
**Santiago Martin Henn** </br>
**Facundo Nicolas Oliva Cuneo**</br>
**26/03/2026**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Resumen

---

## Introducción

---

## Desarrollo

### Parte 1. Repaso general didáctico: Simulación de enviío de paquetes, ARP y ruteo entre redes.
### 1.

<div align="center">

#### *Identidad de Red*

|Dispositivo|Rol    |IP        |MAC     |Mascara        |Gateway |
|:----------|:------|:---------|:-------|:--------------|:-------|
|Elena      |Host   |10.1.0.101|AB:45:71|255.255.255.0  |AA:44:53|
|Lucia      |Host   |10.1.0.102|AA:45:72|255.255.255.0  |AA:44:53|
|Santiago   |Router |10.1.0.1  |AA:44:53|255.255.255.0  |    -   |

</div>

### 2.

<div align="center"> 

#### *Tabla de ruteo*

|Dispositivo |IP        |MAC     |
|:-----------|:---------|:-------|
|Elena       |10.1.0.101|AB:45:71|
|Lucia       |10.1.0.102|AA:45:72|
|Concentrador|     -    |AA:43:80|

</div>

### 3.

En nuestro caso tuvimos que generar dos *frame de transmisión* y los enviamos a través del default gateway. Los frames quedaron de la siguiente manera:

<div align="center">

#### *Paquete 1*

|Frame Ethernet       |
|:--------------------|
|MAC Destino: AA:44:53|
|MAC Origen:  AB:45:71|

|Paquete IP               |
|:------------------------|
|IP Origen: 10.1.0.101    |
|IP Destino: 10.7.0.103   |
|TTL:                6    |
|PAYLOAD: 1101001111000011|
|CRC:      -              |

#### *Paquete 2*

|Frame Ethernet       |
|:--------------------|
|MAC Destino: AA:44:53|
|MAC Origen:  AA:45:72|

|Paquete IP               |
|:------------------------|
|IP Origen: 10.1.0.102    |
|IP Destino: 10.3.0.103   |
|TTL:            6        |
|PAYLOAD: 1101111000111010|
|CRC:      -              |

</div>

### 4.

Una vez generados los paquetes, estos son enviados desde los *hosts* hacia el
*default gateway* quien primero debe verificar que el destinatario de los paquetes no sea un *host* de la misma LAN. Como podemos ver por la *IP destino* este no es nuestro caso, por lo tanto, el *router* o *default gateway* envía los paquetes al *concentrador* para que estos puedan llegar a destino.

Para enviar los paquetes el *router* o *default gateway* deberá modificar el *Frame Ethernet* y cambiará las direcciones MAC, esto con el fin de enviar el paquete al concentrador. Y descontará en 1 el valor de TTL.

Luego de un tiempo, el *router* o *default gateway* recibió 2 paquetes provenientes de *hosts* de otras redes LAN. Los paquetes recibidos fueron los siguientes

<div align="center">

#### *Paquete 1*

|Frame Ethernet       |
|:--------------------|
|MAC Destino: AA:44:53|
|MAC Origen:  AA:43:80|

|Paquete IP               |
|:------------------------|
|IP Origen: 10.13.0.101   |
|IP Destino: 10.1.0.101   |
|TTL:                2    |
|PAYLOAD: 1111011111110111|
|CRC:      -              |

#### *Paquete 2*

|Frame Ethernet       |
|:--------------------|
|MAC Destino: AA:44:53|
|MAC Origen:  AA:43:80|

|Paquete IP               |
|:------------------------|
|IP Origen: 10.11.0.103   |
|IP Destino: 10.1.0.102   |
|TTL:            2        |
|PAYLOAD: 11001010110111  |
|CRC:      -              |

</div>

Ahora, el *default gateway* deberá volver a modificar las direcciones MAC's para que lleguen a los *hosts* de su propia red LAN. Como se puede ver los paquetes llegaron a la LAN correcta.

### 5.

a. Esto se debe a que la dirección lógica (IP) se utiliza para identificar el destino final, mientras que la dirección física (MAC) cambia en cada salto porque se utiliza para identificar a los nodos adyacentes.

b. Se utiliza este mecanismo porque cuando el destino está en otra red, el host no puede obtener directamente su dirección física. El gateway resuelve este problema ya que posee una tabla de rutas que le permite determinar el siguiente salto para llegar al destino final.

c. El enrutamiento *hop-by-hop* permite que cada router tome decisiones basadas en en su tabla de enrutamiento, lo que mejora la escalabilidad, ya que no requiere conocimiento global de la red. Además, aporta tolerancia a fallos, ya que en caso de que se caiga un nodo se pueden usar otros caminos para entregar el paquete.

d. Es necesario reconstruir la trama Ethernet en cada salto porque las direcciones MAC indican el siguiente salto del paquete. El router desencapsula el paquete IP y lo vuelve a encapsular con nuevas direcciones físicas correspondientes al siguiente salto (Basado en su tabla de enrutamiento). Si se reenviara el mismo frame, la dirección MAC destino sería incorrecta y la trama no podría ser entregada.

e.El campo TTL evita que los paquetes permanezcan indefinidamente en la red en caso de no alcanzar su destino. Al decrementarse en cada salto, garantiza que el paquete tenga una vida limitada. Si este mecanismo no existiera, los paquetes podrían circular indefinidamente, provocando congestión y un uso innecesario de los recursos de la red.

### Parte 2. Inyección y Detección de errores.

---

## Discusión Y Conclusiones

---

## Referencias
