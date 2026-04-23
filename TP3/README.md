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

## Resumen



---

## Introducción

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

### 2) Conexión SSH a la VM

Se estableció una conexión SSH con la máquina virtual asignada utilizando una clave privada.  
Una vez dentro de la VM, se creó una carpeta con el nombre del grupo y luego se verificó su creación utilizando
Lo que permitió confirmar que la carpeta fue creada correctamente en el sistema remoto.

Luego entramos a la carpeta y creamos dentro de la misma un archivo de prueba y verificamos su existencia. Esto permitió confirmar la correcta interacción con el sistema de archivos de la máquina virtual.

Por último utilizamos el comando pwd para verificar la ruta actual dentro del sistema de archivos, confirmando que se estaba trabajando dentro de la carpeta del grupo StrangerPings.

Este proceso se realizó tanto para la pc1 como para la pc2.

<img width="925" height="262" alt="image" src="https://github.com/user-attachments/assets/74646f28-1045-4785-9c8b-72871862c0a3" />

<img width="890" height="255" alt="image" src="https://github.com/user-attachments/assets/af61e710-a0d9-4b54-8d40-f706a08f5ed0" />


### Consigna 3: Captura del tráfico SSH 

## 3) Captura de tráfico SSH

Se utilizó Wireshark para capturar el tráfico generado durante una conexión SSH previamente establecida con la máquina virtual.

Se aplicó un filtro para visualizar únicamente los paquetes correspondientes al protocolo SSH. Se generó tráfico ejecutando comandos en la terminal remota, lo que permitió observar múltiples paquetes SSH en la captura.

<img width="1919" height="343" alt="image" src="https://github.com/user-attachments/assets/ef0311d3-1c0d-477d-89b4-36293184806f" />

#### Análisis del contenido de los paquetes

Al inspeccionar los paquetes capturados en Wireshark, se observa que el contenido aparece como “Encrypted packet”.

Esto se debe a que el protocolo SSH utiliza cifrado para proteger la información transmitida entre el cliente y el servidor.

Por lo tanto, no es posible descifrar el contenido de los mensajes utilizando Wireshark, ya que los datos viajan de forma segura y no son legibles para terceros.


### Consigna 4: Comunicación TCP con netcat

a. 

Se implementó un servidor TCP en la máquina virtual utilizando el siguiente comando: ncat -l 5000

Desde la computadora local se estableció una conexión hacia la VM: ncat 4.174.129.188 5000 

Una vez establecida la conexión, se realizó un intercambio de mensajes entre la computadora local y la máquina virtual.

Los mensajes enviados desde la PC fueron recibidos correctamente en la VM, y viceversa, evidenciando una comunicación bidireccional entre ambas.

Esto permitió simular un canal de comunicación tipo “chat” utilizando el protocolo TCP sin cifrado.

<img width="904" height="91" alt="image" src="https://github.com/user-attachments/assets/2b8825c0-85e0-4eca-8418-72a53e957480" />


<img width="1045" height="194" alt="image" src="https://github.com/user-attachments/assets/6e10ec4d-f951-4e1a-9bdc-8926a71a52c4" />

#### Visualización del contenido en texto plano

Se identificó un paquete con datos (PSH, ACK) correspondiente a la comunicación mediante netcat.

Al inspeccionar dicho paquete en Wireshark, se pudo observar el contenido del mensaje en texto plano dentro de la sección de datos.

Esto evidencia que la comunicación no está cifrada, permitiendo que cualquier intermediario pueda leer la información transmitida.

En contraste con SSH, donde los paquetes aparecen como “Encrypted packet”, en este caso los datos son completamente visibles.

<img width="1914" height="920" alt="image" src="https://github.com/user-attachments/assets/feb7d835-0f43-436a-a5e9-40dd7367adc7" />


b. 

#### Comunicación utilizando UDP

Se implementó un servidor UDP en la máquina virtual mediante: ncat -u -l 5001

Desde la computadora local se estableció la conexión utilizando: ncat -u 4.174.129.188 5001 

Se realizó un intercambio de mensajes entre ambas partes, verificando que la comunicación también es posible utilizando el protocolo UDP.

A diferencia de TCP, UDP no establece una conexión formal, pero permite el envío de datos entre cliente y servidor.

<img width="630" height="158" alt="image" src="https://github.com/user-attachments/assets/58434db0-adaa-409c-90ab-33698557b05e" />

<img width="948" height="108" alt="image" src="https://github.com/user-attachments/assets/a13f1feb-5149-495a-ac26-50c300bdd9d1" />

#### Análisis del tráfico UDP

Se capturó el tráfico generado mediante el uso de netcat utilizando el protocolo UDP, aplicando el siguiente filtro en Wireshark: ip.addr == 4.174.129.188 and udp 


Durante la captura se identificaron paquetes UDP correspondientes a la comunicación entre la computadora local y la máquina virtual.

Al analizar uno de estos paquetes, se pudo observar el contenido del mensaje en texto plano dentro de la sección de datos. En particular, se visualiza claramente el mensaje enviado (“mensaje udp wireshark”), lo que evidencia que la información transmitida no se encuentra cifrada.

Esto demuestra que el protocolo UDP, al igual que una comunicación TCP sin mecanismos de seguridad adicionales, no garantiza la confidencialidad de los datos, ya que cualquier intermediario podría acceder al contenido de los mensajes. 

<img width="1919" height="1012" alt="image" src="https://github.com/user-attachments/assets/1ecaef9c-0514-4e3c-8d7f-cb08f762b17d" />

c. 

<img width="1316" height="287" alt="image" src="https://github.com/user-attachments/assets/d3f22a97-3ef1-41c6-a073-1cdf4dfee3e7" />

<img width="965" height="74" alt="image" src="https://github.com/user-attachments/assets/c8ef982f-776d-48ef-bbed-b0b317fe5c4e" />



### Consigna 5:


### Consigna 6:


---

## Discusión Y Conclusiones
