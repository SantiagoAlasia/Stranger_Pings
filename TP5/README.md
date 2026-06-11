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

