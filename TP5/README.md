# Trabajo Práctico N°5 - Server Survival

## Introducción

En este trabajo práctico se utilizó el simulador Server Survival para analizar el comportamiento de una arquitectura de servicios frente a distintos tipos de tráfico. El objetivo fue comprender la función de los principales componentes de infraestructura cloud, identificar posibles cuellos de botella y evaluar estrategias de escalabilidad y balanceo de carga.

A través de distintas pruebas se observó cómo intervienen mecanismos de seguridad, almacenamiento, procesamiento, caché y bases de datos para mantener la estabilidad del sistema ante diferentes niveles de demanda.

# 1. Reconocimiento de arquitectura 
En esta etapa se identificaron los componentes disponibles en el simulador y se analizó la función que cumple cada uno dentro de una arquitectura cloud.

<img width="961" height="414" alt="image" src="https://github.com/user-attachments/assets/3ca74347-0f75-420c-b076-438d40d4c257" />

*Figura 1. Vista inicial del simulador mostrando los distintos componentes de infraestructura disponibles.* 

## Firewall

El Firewall es la primera línea de defensa de una arquitectura. Su función es analizar el tráfico entrante y bloquear solicitudes maliciosas antes de que lleguen a los servicios internos.

### a) ¿Qué problema resuelve?

Evita que ataques, bots o tráfico malicioso consuman recursos de la infraestructura y afecten la disponibilidad del sistema.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en las capas de Internet y Aplicación, ya que puede filtrar paquetes de red y también solicitudes específicas.

### c) ¿Qué pasaría si faltara?

La arquitectura quedaría expuesta a ataques y tráfico malicioso, aumentando el riesgo de caídas del servicio, pérdida de rendimiento y disminución de la reputación del sistema.

## Load Balancer

El Load Balancer o balanceador de carga distribuye las solicitudes entrantes entre distintos servidores o instancias de procesamiento.

### a) ¿Qué problema resuelve?

Evita que un único servidor reciba todo el tráfico y se sobrecargue.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Transporte y, en algunos casos, en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Todo el tráfico llegaría a un único servidor, aumentando las probabilidades de saturación y fallos.

## Compute

El componente Compute representa los servidores o instancias encargadas de ejecutar la lógica principal de la aplicación.

### a) ¿Qué problema resuelve?

Procesa las solicitudes de los usuarios y ejecuta las operaciones necesarias para responderlas.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

La aplicación no tendría capacidad de procesamiento y no podría responder solicitudes. 

## SQL DB

La base de datos SQL almacena información estructurada utilizando tablas y relaciones entre datos.

### a) ¿Qué problema resuelve?

Permite almacenar y recuperar información de forma organizada y consistente.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Capa de Aplicación.

### c) ¿Qué pasaría si faltara?

No existiría un almacenamiento persistente para la información crítica de la aplicación.

## Cache

La caché almacena temporalmente información utilizada con frecuencia para evitar consultas repetidas a otros servicios.

### a) ¿Qué problema resuelve?

Reduce los tiempos de respuesta y disminuye la carga sobre la base de datos y los servidores.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Las consultas repetitivas llegarían constantemente a la base de datos, aumentando la latencia y el consumo de recursos.

## Storage

Storage representa el almacenamiento de archivos como imágenes, videos, documentos o cualquier contenido subido por los usuarios.

### a) ¿Qué problema resuelve?

Permite almacenar grandes cantidades de archivos sin utilizar recursos de los servidores de aplicación.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Los archivos deberían almacenarse directamente en los servidores de aplicación, reduciendo la escalabilidad y aumentando los costos.

## Search Engine

El Search Engine es un motor especializado en realizar búsquedas rápidas sobre grandes volúmenes de información.

### a) ¿Qué problema resuelve?

Permite ejecutar búsquedas complejas de forma eficiente sin sobrecargar la base de datos principal.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Las búsquedas deberían realizarse directamente sobre la base de datos, generando consultas lentas y una mayor carga de procesamiento.

## Queue

La Queue o cola de mensajes almacena temporalmente solicitudes para que sean procesadas de manera ordenada por otros servicios.

### a) ¿Qué problema resuelve?

Permite absorber picos de tráfico y desacoplar componentes de la arquitectura, evitando que los servidores se saturen ante una gran cantidad de solicitudes simultáneas.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Las solicitudes llegarían directamente a los servidores de procesamiento, aumentando el riesgo de sobrecarga y pérdida de peticiones durante momentos de alta demanda.

## Serverless Function

Las funciones serverless son pequeños fragmentos de código que se ejecutan bajo demanda cuando ocurre un evento específico.

### a) ¿Qué problema resuelve?

Permite ejecutar tareas puntuales sin mantener servidores funcionando permanentemente.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Algunas tareas simples deberían ejecutarse en servidores tradicionales, aumentando costos y consumo de recursos.

## NoSQL

Las bases de datos NoSQL almacenan información utilizando modelos más flexibles que las bases de datos relacionales tradicionales.

### a) ¿Qué problema resuelve?

Facilita el almacenamiento de grandes volúmenes de datos con estructuras variables y permite escalar horizontalmente de forma sencilla.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Algunas aplicaciones con datos poco estructurados tendrían dificultades para escalar o requerirían modelos de almacenamiento menos eficientes.

## CDN

Una Content Delivery Network (CDN) distribuye contenido estático desde servidores ubicados en diferentes regiones geográficas.

### a) ¿Qué problema resuelve?

Reduce la latencia y acelera la entrega de archivos estáticos como imágenes, hojas de estilo y archivos JavaScript.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Todo el contenido estático debería ser servido desde los servidores principales, aumentando la carga y los tiempos de respuesta.

## Réplica

Una réplica es una copia sincronizada de una base de datos o servicio utilizada para distribuir carga y mejorar la disponibilidad.

### a) ¿Qué problema resuelve?

Permite repartir consultas de lectura y mejorar la tolerancia a fallos.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en la capa de Aplicación.

### c) ¿Qué pasaría si faltara?

Toda la carga recaería sobre una única base de datos o servicio, aumentando el riesgo de saturación y fallos.

## Conclusión del punto 1

Los componentes disponibles en Server Survival representan elementos comunes de una arquitectura cloud moderna. Cada uno cumple una función específica relacionada con seguridad, procesamiento, almacenamiento, distribución de tráfico o escalabilidad. La ausencia de cualquiera de estos componentes puede generar problemas de rendimiento, disponibilidad o seguridad, dependiendo del rol que desempeñe dentro del sistema.

# 2. Tipos de tráfico

El simulador Server Survival trabaja con distintos tipos de solicitudes que representan situaciones habituales dentro de una arquitectura informática. Cada tipo de tráfico posee características particulares y suele ser procesado por componentes especializados para optimizar el rendimiento y la escalabilidad del sistema.

| Tipo de tráfico | Ejemplo real | Componente recomendado | Riesgo si se procesa incorrectamente |
|----------------|-------------|------------------------|-------------------------------------|
| STATIC | Imágenes, archivos CSS y JavaScript de una página web | CDN o Storage | Se desperdician recursos de cómputo y aumenta la latencia |
| READ | Consulta de perfiles, productos o publicaciones | Cache, Réplica o SQL DB | Sobrecarga de la base de datos y respuestas lentas |
| WRITE | Registro de usuarios, compras o publicaciones | SQL DB o Queue + Compute | Pérdida de datos o inconsistencias |
| UPLOAD | Subida de imágenes, videos o documentos | Storage | Saturación de servidores de aplicación |
| SEARCH | Búsqueda de productos, artículos o usuarios | Search Engine | Consultas lentas y sobrecarga de la base de datos |
| MALICIOUS | Ataques DDoS, bots o solicitudes maliciosas | Firewall | Caída del servicio y pérdida de reputación |

## Análisis

Los distintos tipos de tráfico requieren tratamientos diferentes para garantizar un funcionamiento eficiente del sistema. El contenido estático suele beneficiarse del uso de CDN y almacenamiento especializado, mientras que las operaciones de lectura y escritura dependen principalmente de bases de datos y mecanismos de caché.

Por otra parte, las búsquedas suelen procesarse mediante motores especializados para evitar sobrecargar las bases de datos transaccionales. Finalmente, el tráfico malicioso debe ser bloqueado por mecanismos de seguridad como los firewalls para proteger la disponibilidad y estabilidad de la infraestructura.


<img width="189" height="304" alt="image" src="https://github.com/user-attachments/assets/fc02bd21-d098-4f12-ad1f-11be59334a84" />

*Figura 2. Distribución de los distintos tipos de tráfico simulados por Server Survival.*

# 3. Testeamos Queues

Para analizar el comportamiento de una cola de mensajes se construyó una arquitectura mínima compuesta por un Firewall, una Queue y una instancia de Compute.

La prueba consistió en incrementar progresivamente la tasa de tráfico (Traffic Rate) para observar cómo reaccionaba la cola ante distintos niveles de carga.

<img width="1922" height="830" alt="image" src="https://github.com/user-attachments/assets/ef05b393-7656-4876-aee1-43982b95ceef" />

*Figura 3. Arquitectura utilizada para evaluar el comportamiento de una cola de mensajes. El tráfico ingresa a través del Firewall, pasa por la Queue y finalmente es procesado por Compute.*

<img width="1922" height="830" alt="image" src="https://github.com/user-attachments/assets/4deedaf0-f2b4-45b8-9c52-50cfe07c14a9" />

*Figura 4. Comportamiento de la Queue con una tasa de tráfico de 20 solicitudes por segundo.*

<img width="1932" height="818" alt="image" src="https://github.com/user-attachments/assets/86d47b9a-39f8-4b66-8238-e81dce2db3fe" />

*Figura 5. Comportamiento de la Queue con una tasa de tráfico de 50 solicitudes por segundo.*

## Observaciones

Inicialmente se ejecutó la arquitectura con una tasa de tráfico de 1 solicitud por segundo. En estas condiciones la Queue permaneció prácticamente vacía, ya que Compute podía procesar las solicitudes al mismo ritmo en que llegaban.

Posteriormente se incrementó la tasa de tráfico a 20 solicitudes por segundo. En este escenario comenzó a observarse una acumulación temporal de mensajes dentro de la Queue. Sin embargo, el sistema continuó funcionando correctamente debido a que la cola absorbió parte de la carga.

Finalmente se aumentó el tráfico a 50 solicitudes por segundo. La cantidad de mensajes almacenados en la Queue creció considerablemente, evidenciando su función como mecanismo de amortiguación frente a picos de demanda. Compute continuó procesando solicitudes mientras la cola regulaba el flujo de trabajo.

## Respuestas

### ¿Qué sucede después de la Queue cuando se incrementa el rate?

Al aumentar la tasa de tráfico, la Queue comienza a acumular solicitudes y las envía progresivamente hacia Compute. De esta manera evita que el componente de procesamiento reciba toda la carga de forma instantánea.

### ¿Qué sucede después de la Queue cuando el rate se lleva rápidamente a cero?

Aunque el tráfico entrante disminuye o desaparece, la Queue continúa enviando las solicitudes que habían quedado almacenadas. Esto provoca que Compute siga trabajando durante un tiempo hasta vaciar completamente la cola.

## Conclusión

La Queue actúa como un mecanismo de desacople entre la llegada de solicitudes y su procesamiento. Su principal ventaja es absorber picos de tráfico, mejorar la estabilidad del sistema y evitar sobrecargas repentinas sobre los servicios de cómputo.

# 4. Primera infraestructura mínima

Se diseñó una arquitectura capaz de atender tráfico estático, cargas de archivos, consultas de lectura y escritura, búsquedas y tráfico malicioso.

La arquitectura implementada estuvo compuesta por un Firewall, un Load Balancer, una instancia de Compute, una base de datos SQL, un servicio de Storage y un Search Engine.


<img width="1929" height="827" alt="image" src="https://github.com/user-attachments/assets/52594763-319d-4ac5-9aaf-9fb363949e39" />

*Figura 6. Arquitectura diseñada para atender los diferentes tipos de tráfico presentes en el simulador.*

## Presupuesto inicial

La arquitectura fue desplegada con un presupuesto inicial aproximado de $1555, manteniendo todos los servicios operativos y en estado saludable.

## Estado inicial de los servicios

Al iniciar la simulación todos los componentes se encontraban en estado saludable. El Firewall filtraba tráfico malicioso, el Load Balancer distribuía solicitudes hacia Compute y los servicios de almacenamiento, búsqueda y base de datos respondían correctamente.

## Observaciones

Se realizaron pruebas incrementando progresivamente la tasa de tráfico.

Con una tasa de 20 solicitudes por segundo comenzó a observarse una mayor carga sobre el componente Compute. Este servicio fue el primero en mostrar signos de saturación.

Al aumentar el tráfico a 50 solicitudes por segundo y posteriormente a 100 solicitudes por segundo, la carga sobre Compute continuó creciendo, mientras que el resto de los servicios mantuvo un comportamiento relativamente estable.

Esto indica que la principal limitación de la arquitectura se encontraba en la capacidad de procesamiento y no en los servicios de almacenamiento, búsqueda o seguridad.

## Respuestas

### ¿Qué componente falló primero?

El primer componente en presentar signos de saturación fue Compute.

### ¿Por qué creés que falló?

Porque toda la lógica de procesamiento de solicitudes dependía de una única instancia de cómputo. A medida que aumentó el tráfico, la cantidad de solicitudes superó su capacidad de procesamiento.

### ¿Fue un problema de capacidad, diseño, costo o seguridad?

Principalmente fue un problema de capacidad. La arquitectura contaba con una sola instancia de Compute y no disponía de mecanismos de escalado horizontal que permitieran distribuir mejor la carga. 

## Conclusión

La arquitectura propuesta logró procesar correctamente los distintos tipos de tráfico requeridos por la consigna. Sin embargo, las pruebas demostraron que el componente de cómputo constituye el principal cuello de botella cuando aumenta la demanda. Esto evidencia la necesidad de aplicar estrategias de escalabilidad para soportar mayores volúmenes de tráfico.
