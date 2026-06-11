# Trabajo Práctico N°5 - Server Survival

## Introducción

En este trabajo práctico se utilizó el simulador Server Survival para analizar el comportamiento de una arquitectura de servicios frente a distintos tipos de tráfico. El objetivo fue comprender la función de los principales componentes de infraestructura cloud, identificar posibles cuellos de botella y evaluar estrategias de escalabilidad y balanceo de carga.

A través de distintas pruebas se observó cómo intervienen mecanismos de seguridad, almacenamiento, procesamiento, caché y bases de datos para mantener la estabilidad del sistema ante diferentes niveles de demanda.

# 1. Reconocimiento de arquitectura 
En esta etapa se identificaron los componentes disponibles en el simulador y se analizó la función que cumple cada uno dentro de una arquitectura cloud.

<img width="971" height="413" alt="{C57BDCEA-745B-4C78-A1B8-53DA330A4B43}" src="https://github.com/user-attachments/assets/cde3a8f7-2c6d-454d-997d-8f88be0385a8" /> 

*Figura 1. Vista inicial del simulador mostrando los distintos componentes de infraestructura disponibles.* 

## Firewall

El Firewall es la primera línea de defensa de una arquitectura. Su función es analizar el tráfico entrante y bloquear solicitudes maliciosas antes de que lleguen a los servicios internos.

### a) ¿Qué problema resuelve?

Evita que ataques, bots o tráfico malicioso consuman recursos de la infraestructura y afecten la disponibilidad del sistema.

### b) ¿En qué capa del modelo TCP/IP se ubica?

Principalmente en las capas de Internet y Aplicación, ya que puede filtrar paquetes de red y también solicitudes específicas.

### c) ¿Qué pasaría si faltara?

La arquitectura quedaría expuesta a ataques y tráfico malicioso, aumentando el riesgo de caídas del servicio, pérdida de rendimiento y disminución de la reputación del sistema.

<img width="960" height="412" alt="image" src="https://github.com/user-attachments/assets/c9002d08-1eca-4bbe-bb50-476cbfab5e22" />

*Figura 2. Implementación del Firewall como primera línea de defensa de la arquitectura.*

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

<img width="1921" height="843" alt="image" src="https://github.com/user-attachments/assets/f0033708-8c12-4474-9301-810e18e26332" />

*Figura 3. Componentes principales utilizados para procesar y distribuir solicitudes dentro de la arquitectura: Firewall, Load Balancer, Compute y SQL Database.*




