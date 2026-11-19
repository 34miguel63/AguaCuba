# AguaClara

Plataforma web para consultar el **estado del suministro de agua potable reportado en las zonas de Cuba**, de forma rápida y centralizada.

> **Estado:** estructura inicial. El proyecto tiene la base organizada y configurada, pero todavía no incluye funcionalidades de negocio ni modelos de datos definitivos.

## Tecnologías

| Capa | Tecnología |
| --- | --- |
| Lenguaje | Python 3.13 |
| Backend | Django 6.0 |
| Base de datos | PostgreSQL (definitiva, pendiente) · SQLite (temporal, desarrollo) |
| Frontend | HTML5, CSS3 y JavaScript |

## Estructura del proyecto

```text
config/      Configuración principal de Django
apps/        Aplicaciones: accounts, zones, supply, reports, search y assistant
templates/   Plantillas HTML globales
static/      CSS, JavaScript e imágenes
docs/        Documentación del proyecto y Design Thinking
tests/       Pruebas de la configuración del proyecto
```

La descripción completa (árbol de archivos, propósito de cada módulo, configuración y comprobaciones) está en `docs/ESTRUCTURA_INICIAL.md`.

## Puesta en marcha

Requisitos: Python 3.13 y Django 6.0.

```powershell
# 1. Crear y activar un entorno virtual
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
py -m pip install -r requirements.txt

# 3. Configurar variables de entorno
Copy-Item .env.example .env

# 4. Comprobar la configuración
py manage.py check

# 5. Crear la base de datos SQLite temporal
py manage.py migrate

# 6. Arrancar el servidor de desarrollo
py manage.py runserver
```

La página de inicio estará en <http://127.0.0.1:8000/> y el panel de administración en <http://127.0.0.1:8000/admin/>.

## Variables de entorno
La configuración se lee desde variables de entorno. El archivo `.env.example` documenta todas las variables. El archivo `.env` es local y no se versiona.

## Aplicaciones

| Aplicación | Responsabilidad |
| --- | --- |
| `accounts` | Usuarios y autenticación (Administrador, Delegado, Ciudadano) |
| `zones` | Registro y administración geográfica de las zonas de suministro |
| `supply` | Publicación de horarios de llegada y estado de calidad del agua |
| `reports` | Recepción y clasificación de reportes ciudadanos (fugas, mala calidad) |
| `search` | Búsqueda y consulta del estado del agua por zona |
| `assistant` | Futura integración del asistente inteligente con IA (PLN, Visión, LLM) |

## About
Plataforma web para facilitar el acceso a información confiable sobre el suministro de agua potable en Cuba.

### Equipo de Desarrollo
- **Addel Vidal García**
- **Miguel Ángel Banteurt Blanco**
- **Alejandro Colón Álvarez**

**Universidad de Oriente**  
Facultad de Ingeniería en Telecomunicaciones, Informática y Biomédica  
Carrera: Ingeniería Informática | 2026-2027