# Estructura Inicial del Proyecto AguaClara

## Propósito del Proyecto
Desarrollar una plataforma web y aplicación móvil ligera que permita a los ciudadanos de Cuba consultar el estado del suministro de agua potable, reportar incidencias y recibir alertas, cerrando la brecha de información entre las instituciones (Acueducto, Poder Popular) y la población.

## Metodología
El proyecto se rige por la metodología **Design Thinking**, cuyas fases (Empatizar, Definir, Storytelling, Idear y Prototipar) están documentadas en el repositorio principal del equipo.

## Detalle de las Aplicaciones (Apps)
1. **`accounts`**: Maneja el sistema de autenticación y los tres roles principales (Administrador, Delegado, Ciudadano).
2. **`zones`**: Modelo de datos que representa la división geográfica (Provincia, Municipio, Zona/Reparto).
3. **`supply`**: Registra los eventos de suministro (fecha, hora estimada, estado de calidad).
4. **`reports`**: Permite a los ciudadanos enviar reportes con descripción, foto y geolocalización.
5. **`search`**: Vista optimizada para que el ciudadano encuentre rápidamente la información de su zona.
6. **`assistant`**: Módulo preparado para la integración futura de Inteligencia Artificial (Predicción, PLN, Visión Artificial y LLM).

## Próximos Pasos
1. Definir los modelos de datos detallados en `models.py` de cada app.
2. Configurar las vistas y plantillas básicas para el flujo de consulta ciudadana.
3. Implementar el panel de administración personalizado para los delegados.