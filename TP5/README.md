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



