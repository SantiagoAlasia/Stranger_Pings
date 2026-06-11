# Trabajo Práctico N°5 - Server Survival

- **Santiago Alasia**
- **Lucia Feiguin Malkoni**
- **Elena Monutti**

**Stranger Pings** </br>
**Universidad Nacional de Córdoba**</br>
**Redes de Computadoras**</br>
**Santiago Martin Henn** </br>
**Facundo Nicolas Oliva Cuneo**</br>
**11/06/2026**

---

### Información de los autores
 
- **Información de contacto**: santiago.alasia@mi.unc.edu.ar 
- **Información de contacto**: lucia.feiguin@mi.unc.edu.ar
- **Información de contacto**: elena.monutti@mi.unc.edu.ar


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

# 5. Escalabilidad y balanceo

A partir de la arquitectura desarrollada en el punto anterior se realizaron distintas modificaciones con el objetivo de soportar una mayor cantidad de tráfico y reducir los cuellos de botella identificados durante las pruebas.

Las estrategias implementadas estuvieron orientadas a distribuir mejor la carga de procesamiento y optimizar el acceso a los datos. 

## Estrategia 1: Agregar más capacidad de cómputo

La primera estrategia consistió en agregar una segunda instancia de Compute detrás del Load Balancer.

<img width="1927" height="830" alt="image" src="https://github.com/user-attachments/assets/0e6d3caa-f10e-46d9-9ff3-b2a7f988c3ee" />

*Figura 6. Arquitectura modificada incorporando una segunda instancia de Compute para distribuir la carga de procesamiento.*

Al incorporar una segunda instancia de Compute, el Load Balancer pudo distribuir las solicitudes entre ambos servidores. Esto permitió reducir la carga individual de cada instancia y aumentar la capacidad total de procesamiento de la arquitectura.

Esta estrategia resultó efectiva para resolver el cuello de botella identificado en el punto anterior, donde una única instancia de Compute se saturaba al incrementar la tasa de tráfico.

## Estrategia 2: Incorporación de Cache

La segunda estrategia consistió en agregar un componente de Cache para almacenar temporalmente datos consultados con frecuencia.

La utilización de caché permite responder solicitudes READ sin necesidad de acceder constantemente a la base de datos principal.

Como consecuencia, disminuye la carga sobre SQL DB y mejora el tiempo de respuesta para los usuarios.

Esta estrategia resulta especialmente efectiva cuando predominan las operaciones de lectura sobre las de escritura.

## Estrategia 3: Réplicas de lectura

Otra estrategia posible consiste en incorporar réplicas de la base de datos.

Las réplicas permiten distribuir las consultas de lectura entre varias instancias, evitando que una única base de datos reciba toda la carga.

Esta solución mejora la disponibilidad y permite escalar aplicaciones con grandes volúmenes de consultas READ.

## ¿Escalar horizontalmente siempre mejora el sistema?

No necesariamente.

Durante las pruebas realizadas se observó que agregar una segunda instancia de Compute permitió distribuir mejor la carga y reducir la saturación del componente de procesamiento.

Sin embargo, si el cuello de botella se encontrara en la base de datos, el almacenamiento o el motor de búsqueda, agregar más servidores de cómputo no resolvería el problema.

Por lo tanto, la efectividad del escalado horizontal depende de identificar correctamente qué componente limita el rendimiento general de la arquitectura.

# 6. Sobrevivir

<img width="1024" height="482" alt="image" src="https://github.com/user-attachments/assets/eac41262-10c0-454e-b457-1b18c812d7b9" />

*Figura 7. Arquitectura final con los resultados y componentes utilizados.*

### Justificación y Análisis de la Arquitectura

- Flujo Estático Desacoplado (`Internet ──> CDN ──> Storage <── Computes`): Diseñado específicamente para absorber de raíz el tráfico `STATIC` y `UPLOAD`. El CDN cachea el contenido en la frontera de la red para evitar transferencias redundantes, y se apoya en el Storage como almacenamiento de origen. Al conectar este Storage hacia todos los nodos de cómputo, se garantiza que los servidores de aplicación tengan acceso inmediato a los archivos subidos y estáticos de forma centralizada sin duplicar datos.
- Línea de Defensa y Asincronismo (`Internet ──> Firewall ──> Queue ──> LB ──> Computes`): El Firewall actúa como el escudo inicial contra el tráfico `ATTACK`. Las peticiones legítimas de procesamiento e ingreso de datos pasan de inmediato a una Queue (Cola de mensajes), que actúa como un amortiguador (buffer) ante ráfagas masivas. Un Load Balancer (LB) toma los mensajes ordenadamente de la cola y los distribuye de manera balanceada entre el clúster de servidores Compute para que ninguno se sature.
- Procesamiento y API Gateway (`Computes ──> API GW`): Los Computes procesan la lógica de negocio y se conectan a la API Gateway para centralizar, unificar y exponer de forma segura los endpoints de los microservicios de la aplicación.
- Capa de Caché y Búsquedas Indexadas (`Computes ──> Cache ──> Search Engine`): Para mitigar el tráfico pesado de `READ` y `SEARCH`, cada Compute delega las solicitudes de lectura en memoria a una Cache. Si la consulta requiere procesamiento de texto indexado, la Cache se comunica directamente con el Search Engine, optimizando drásticamente los tiempos de respuesta.
- Segregación de Base de Datos y Réplicas (`Computes ──> DB` y `Cache/DB ──> Read Replica`): Los servidores Compute realizan las operaciones de escritura (`WRITE`) directamente sobre la base de datos principal (DB). Para evitar cuellos de botella por concurrencia , tanto la DB (para sincronización) como la Cache se conectan a una Read Replica (Réplica de lectura) dedicada de forma exclusiva a resolver las peticiones `READ`.

**Qué cuello de botella apareció primero:**

El primer cuello de botella crítico apareció en los servidores Compute individuales y en la base de datos DB principal al inicio del laboratorio. Al procesar el tráfico de manera síncrona y sin intermediarios, las ráfagas concurrentes de escrituras (`WRITE`) y búsquedas de texto (`SEARCH`) bloqueaban las tablas de la base de datos relacional y saturaban el procesamiento de los servidores , lo que provocaba degradación del servicio (componentes en amarillo) y un alto costo operativo en reparaciones antes de implementar este diseño distribuido.

**Qué componente escalaría si tuviera más presupuesto:**

Contando con el excelente presupuesto remanente de $3,919, la estrategia ideal de escalabilidad consistiría en añadir funciones serverless (`λ Func`) conectadas en paralelo a la salida de la Queue, u hacer un escalamiento horizontal añadiendo más nodos de Compute al clúster del Load Balancer. Esto permitiría vaciar la cola de mensajes a una velocidad drásticamente mayor durante los picos de tráfico máximo de solicitudes por segundo ($req/s$).  

**Conclusión de "Estabilidad" (Condición de Victoria)**

Evaluando los resultados del simulador, la arquitectura desarrollada ha alcanzado con éxito la condición de estabilidad económica y técnica requerida para ganar el escenario. El sistema es capaz de mitigar fallas de manera automatizada manteniendo la reputación al 100% y generando ingresos constantes que superan con creces el costo de mantenimiento operativo ($\text{Upkeep Cost de }-\$12.60/\text{s}$), logrando romper ampliamente el objetivo con una puntuación final superior a los 354,000 puntos.

## Conclusión

El análisis y la experimentación con el simulador Server Survival permitieron comprobar de manera práctica que una infraestructura eficiente no depende únicamente de la cantidad de recursos de cómputo asignados, sino de un diseño arquitectónico estratégico y adaptado a la naturaleza del tráfico.

A lo largo del trabajo práctico, se evidenció cómo los esquemas tradicionales y síncronos colapsan ante picos de demanda debido a cuellos de botella en la capa de datos y procesamiento. La implementación exitosa de la arquitectura final en el modo Survival —que logró la condición de estabilidad económica y técnica superando los 354,000 puntos— demostró que patrones avanzados como el procesamiento asíncrono mediante colas (`Queue`), el desacoplamiento del tráfico estático con tecnologías de borde (`CDN` + `Storage`), la optimización de búsquedas indexadas y la segregación de lecturas y escrituras en las bases de datos (`Read Replica` y `Cache`) son indispensables para garantizar la alta disponibilidad, la tolerancia a fallos y la viabilidad financiera de una plataforma moderna en la nube.
