# Procesamiento


# Implementación de un Bróker MQTT Seguro y Aplicación de Python

## Autor: Imanol Anda Garcia

Este proyecto simula un conjunto de generadores de un parque eólico y un concentrador que recoge y valida datos de producción de energía. Utiliza FastAPI para implementar un servicio de API que interactúa con los generadores.

## Descripción del Proyecto

- Se simulan 10 generadores de energía eólica, cada uno generando datos de producción de energía, velocidad del viento y temperatura.
- Un concentrador implementado con FastAPI recoge estos datos y verifica su validez, considerando una probabilidad N de recibir datos erróneos.
- La aplicación realiza agregaciones de los datos, como la media de producción del parque, y puede entregar agregados en distintos intervalos (por ejemplo, minutales).

## Instrucciones de Uso

### Configurar y Ejecutar el Concentrador

1. Asegúrate de tener instalado Python 3.8 o superior y FastAPI.
2. Ejecuta el servidor FastAPI con `uvicorn main:app --reload` desde la línea de comandos.

### Interactuar con la API

1. Utiliza el endpoint `POST /generador/` para enviar datos de producción de los generadores.
2. Accede al endpoint `GET /agregados/` para obtener los datos agregados de producción.
3. Utiliza el endpoint `GET /datos-generadores/` para obtener los últimos datos de todos los generadores.


## Alternativas a FastAPI

Si bien este proyecto utiliza FastAPI por su rendimiento y facilidad de uso, otras alternativas para la creación de APIs incluyen:

- **Flask**: Un micro framework de Python que es fácil de usar y ampliar para necesidades específicas.
- **Django REST framework**: Un potente y flexible toolkit para construir APIs Web, que funciona sobre el framework de Django.
- **Tornado**: Un framework y servidor web de Python que es particularmente bueno en la gestión de conexiones largas y persistentes.

## Posibles Vías de Mejora

- **Monitoreo y Alertas**: Implementar un sistema de monitoreo para rastrear el rendimiento y la salud de los generadores en tiempo real.
- **Autenticación más Robusta**: Añadir soporte para OAuth2 o JWT para mejorar la seguridad en la autenticación.
- **Base de Datos**: Persistir los datos en una base de datos para análisis histórico y respaldo de información.

## Conclusión

El proyecto proporciona un modelo efectivo para la simulación de un sistema de parque eólico y su concentrador asociado. Con la incorporación de FastAPI , el sistema puede evolucionar para adaptarse a escenarios de producción reales.
