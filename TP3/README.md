# Trabajo Práctico N°3

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Redes de Computadoras**</br>
**Santiago Martin Henn** </br>
**Facundo Nicolas Oliva Cuneo**</br>
**23/04/2026**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar

---

## Introducción a infraestructura de servicios web con perspectiva de redes

Este trabajo práctico tiene como objetivo introducirnos en el uso de herramientas y conceptos fundamentales para la administración y análisis de servicios en red. A lo largo del desarrollo, se trabajará con máquinas virtuales en la nube, conexiones seguras mediante SSH y análisis de tráfico utilizando herramientas como Wireshark y netcat.

Se abordarán tanto aspectos teóricos como prácticos, permitiendo comprender cómo se establecen las comunicaciones en red, cómo se protegen mediante mecanismos de cifrado y cómo pueden ser analizadas desde el punto de vista del tráfico de datos.

Además, se realizarán experiencias prácticas que incluyen la creación de servidores simples, la captura y análisis de paquetes de red, y el despliegue de servicios HTTP, con el fin de observar el comportamiento real de los protocolos estudiados.

Este trabajo busca consolidar los conocimientos adquiridos en los trabajos prácticos anteriores y aplicar conceptos clave relacionados con la seguridad, la confidencialidad y el funcionamiento de las comunicaciones en redes.

---

## Desarrollo

### Consigna 1:

**a) ¿Qué es SSH y qué problema resuelve?**

SSH (Secure Shell) es un protocolo de red que permite conectarse de forma segura a otra máquina (por ejemplo, un servidor remoto). Resuelve el problema de comunicaciones inseguras, ya que cifra los datos y evita que terceros los intercepten.

**b) Diferencia entre autenticación y cifrado** 

- Autenticación: proceso de verificación de identidad de un usuario o sistema.
- Cifrado: proceso de protección de información transformándola para que solo pueda ser leída por destinatarios autorizados.

**c) ¿Qué es una clave pública y una clave privada?** 

Una clave pública es una clave que se puede compartir libremente y se usa para cifrar información o verificar identidad.

Una clave privada es secreta y se usa para descifrar información o generar firmas digitales.

**d) ¿Por qué la clave privada no debe compartirse?**

La clave privada no debe compartirse porque garantiza la identidad del usuario; su divulgación permite a terceros suplantar dicha identidad y acceder a sistemas de manera no autorizada.

**e) ¿Qué ventajas tienen las claves SSH frente a contraseñas?**

- Mayor nivel de seguridad criptográfica.
- No requieren el envío de credenciales sensibles por la red.
- Reducen el riesgo de ataques de fuerza bruta.
- Permiten automatización en procesos de conexxión.

## 2) Conexión SSH a la VM

Se estableció una conexión SSH con la máquina virtual asignada utilizando autenticación mediante clave privada:

```bash
ssh -i <path/a/la/clave> <usuario>@<ip>
```

Una vez dentro de la VM, se creó una carpeta con el nombre del grupo: 

```bash
mkdir StrangerPings
```

Luego se verificó su creación utilizando:

```bash
ls
```

Lo que permitió confirmar que la carpeta fue creada correctamente en el sistema remoto.

<img width="925" height="262" alt="image" src="https://github.com/user-attachments/assets/74646f28-1045-4785-9c8b-72871862c0a3" />

A continuación, se ingresó a la carpeta creada:

```bash
cd StrangerPings
```

Dentro de la misma un archivo de prueba:

```bash
touch prueba.txt
```
Y se verificó su existencia nuevamente con:

```bash
ls
```

Esto permitió validar la correcta interacción con el sistema de archivos de la máquina virtual.

<img width="890" height="255" alt="image" src="https://github.com/user-attachments/assets/af61e710-a0d9-4b54-8d40-f706a08f5ed0" />

Por último, se utilizó el comando:

```bash
pwd
```

para verificar la ruta actual dentro del sistema de archivos, confirmando que se estaba trabajando dentro del directorio /home/.../StrangerPings.

Este procedimiento se realizó en ambas máquinas virtuales (pc1 y pc2), obteniendo resultados consistentes en ambos casos.


## 3) Captura de tráfico SSH

Se utilizó Wireshark para capturar el tráfico generado durante una conexión SSH previamente establecida con la máquina virtual.

Para ello, se aplicó un filtro que permitió visualizar únicamente los paquetes correspondientes al protocolo SSH:

```plaintext
ssh
```
### Captura de tráfico

#### Análisis del contenido de los paquetes
Al inspeccionar los paquetes capturados en Wireshark, se observa que en la columna "Info" aparece el mensaje:

Encrypted packet

Esto indica que el contenido del paquete se encuentra cifrado.

El protocolo SSH (Secure Shell) implementa mecanismos de cifrado para garantizar la confidencialidad e integridad de la información transmitida entre el cliente y el servidor. Como resultado, los datos no pueden ser interpretados en texto plano por herramientas de captura de paquetes como Wireshark.

Por lo tanto, no es posible descifrar el contenido de los mensajes capturados, ya que viajan de forma segura y protegida frente a posibles interceptaciones.

<img width="1919" height="343" alt="image" src="https://github.com/user-attachments/assets/ef0311d3-1c0d-477d-89b4-36293184806f" />


## 4) Comunicación con netcat

### a) Comunicación TCP

Se implementó un servidor TCP en la máquina virtual utilizando el siguiente comando:

```bash
ncat -l 5000
```

Desde la computadora local se estableció una conexión hacia la VM mediante 

```bash
ncat 4.174.129.188 5000 
```

Una vez establecida la conexión, se realizó un intercambio de mensajes entre la computadora local y la máquina virtual, funcionando como un canal de comunicación bidireccional tipo “chat”.

<img width="904" height="91" alt="image" src="https://github.com/user-attachments/assets/2b8825c0-85e0-4eca-8418-72a53e957480" />

<img width="1045" height="194" alt="image" src="https://github.com/user-attachments/assets/6e10ec4d-f951-4e1a-9bdc-8926a71a52c4" />

#### Análisis del tráfico TCP
Se capturó el tráfico utilizando Wireshark y se identificaron paquetes correspondientes a la comunicación TCP.

En particular, se observó un paquete con flags PSH, ACK, indicando el envío de datos.

Al inspeccionar el contenido del paquete, se pudo visualizar el mensaje en texto plano dentro de la sección de datos.

Esto demuestra que la comunicación mediante netcat utilizando TCP no se encuentra cifrada, a diferencia de SSH. Por lo tanto, cualquier intermediario podría acceder al contenido de los mensajes transmitidos.

<img width="1914" height="920" alt="image" src="https://github.com/user-attachments/assets/feb7d835-0f43-436a-a5e9-40dd7367adc7" />

### b) Comunicación UDP

Se implementó un servidor UDP en la máquina virtual utilizando:

```bash
ncat -u -l 5001 
```

Desde la computadora local se estableció la conexión mediante:

```bash
ncat -u 4.174.129.188 5001 
```

Se realizó un intercambio de mensajes entre ambas partes, verificando que la comunicación también es posible utilizando el protocolo UDP.

A diferencia de TCP, UDP no establece una conexión formal, sino que envía los datos directamente sin garantizar entrega ni orden.

<img width="630" height="158" alt="image" src="https://github.com/user-attachments/assets/58434db0-adaa-409c-90ab-33698557b05e" />

<img width="948" height="108" alt="image" src="https://github.com/user-attachments/assets/a13f1feb-5149-495a-ac26-50c300bdd9d1" />

#### Análisis del tráfico UDP

Se capturó el tráfico en Wireshark aplicando el siguiente filtro:  

```bash
ip.addr == 4.174.129.188 and udp
```
Durante la captura se identificaron paquetes UDP correspondientes a la comunicación.

Al analizar uno de estos paquetes, se pudo observar el contenido del mensaje en texto plano dentro de la sección de datos.

Esto evidencia que UDP tampoco cifra la información, por lo que los datos pueden ser interceptados y leídos por terceros.

<img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/1ecaef9c-0514-4e3c-8d7f-cb08f762b17d" />

### c) Comunicación entre máquinas virtuales

Se estableció una comunicación directa entre dos máquinas virtuales utilizando netcat.

En la primera VM se ejecutó:

```bash
ncat -u -l 5002 
```

Mientras que desde la segunda VM se realizó la conexión:

```bash
ncat -u 4.174.129.188 5001 
```

Una vez establecida la conexión, se intercambiaron mensajes entre ambas máquinas, simulando un chat bidireccional.

Esto permitió demostrar la comunicación directa entre instancias en la nube utilizando el protocolo TCP sin cifrado.


<img width="1316" height="287" alt="image" src="https://github.com/user-attachments/assets/d3f22a97-3ef1-41c6-a073-1cdf4dfee3e7" />

<img width="965" height="74" alt="image" src="https://github.com/user-attachments/assets/c8ef982f-776d-48ef-bbed-b0b317fe5c4e" />


### Consigna 5: Despliegue de servidor HTTP

#### Creación de la página web

Se creó un archivo `index.html` dentro de la carpeta del grupo con el siguiente contenido:

<h1>Hola Mundo StrangerPings 🚀</h1>
<p>Este es nuestro servidor web</p>

Este archivo representa una página web básica que será servida mediante un servidor HTTP.

Despliegue del servidor web

Se levantó un servidor web utilizando Python con el siguiente comando:

python3 -m http.server 5000

Se utilizó el puerto 5000 debido a que se encuentra dentro del rango de puertos habilitados en la máquina virtual.

Luego, desde la computadora local, se accedió al servidor mediante un navegador web utilizando la dirección:

http://4.174.129.188:5000

Se verificó el correcto funcionamiento al visualizar la página creada previamente.

Análisis del tráfico HTTP

Se capturó el tráfico HTTP generado al acceder a la página web desde el navegador, utilizando Wireshark.

Al analizar los paquetes, se observó que el contenido de la página (HTML) es visible en texto plano dentro de los paquetes capturados.

Esto demuestra que el protocolo HTTP no cifra la información transmitida, permitiendo que los datos puedan ser interceptados y leídos por terceros.

En consecuencia, HTTP no garantiza la confidencialidad de la comunicación.

<img width="1481" height="761" alt="image" src="https://github.com/user-attachments/assets/cbd18f6e-cbf0-465e-9aff-4be71baa420b" />

<img width="961" height="872" alt="image" src="https://github.com/user-attachments/assets/f723d1b4-6e65-4fba-8984-1198cff4b0d8" />





### Consigna 6:


---

## Discusión Y Conclusiones
