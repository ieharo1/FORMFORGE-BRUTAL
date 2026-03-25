# 🚨 FormForge Brutal

---

## 📱 Descripción

**FormForge Brutal** es un sistema completo tipo **Google Forms** desarrollado con **Django + PostgreSQL + Bootstrap 5 (sin CSS custom)**, diseñado para crear formularios dinámicos, recolectar respuestas y analizar indicadores en tiempo real desde un panel administrativo robusto y escalable.

> Arquitectura preparada para producción con Docker, separación por capas (core/apps/templates), administración vía Django Admin y despliegue reproducible.

---

## ✨ Características

### Funcionalidades Implementadas ✅

- ✅ **Autenticación** (login/logout)
- ✅ **CRUD de formularios** por usuario propietario
- ✅ **Constructor de preguntas** (texto corto, texto largo, selección única, múltiple)
- ✅ **Gestión de opciones** para preguntas cerradas
- ✅ **Formulario público** para capturar respuestas
- ✅ **Validaciones de obligatorias**
- ✅ **Dashboard ejecutivo** con métricas por formulario
- ✅ **Indicadores por pregunta** con barras de progreso Bootstrap
- ✅ **Panel Admin** para administración total de datos
- ✅ **Docker Compose** con Django + PostgreSQL
- ✅ **Diseño responsive 100% Bootstrap 5**

### Próximamente 🔄

- 🔄 Tokens públicos firmados para compartir formularios
- 🔄 Exportación a CSV/XLSX
- 🔄 Versionado de formularios
- 🔄 Paginación y búsqueda avanzada
- 🔄 API REST con DRF
- 🔄 Gráficas avanzadas

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Backend | Python | 3.12 |
| Framework | Django | 5.1.7 |
| Base de datos | PostgreSQL | 16 |
| Servidor WSGI | Gunicorn | 23 |
| Frontend | Bootstrap | 5.3.3 |
| Contenedores | Docker / Compose | latest |

---

## 📁 Estructura del Proyecto

```bash
googleforms_brutal/
├── apps/
│   └── forms_app/
│       ├── migrations/
│       ├── templatetags/
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── docker/
│   └── entrypoint.sh
├── templates/
│   ├── registration/login.html
│   └── forms_app/*.html
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio
```bash
git clone <tu_repo>
cd googleforms_brutal
```

### 2. Levantar con Docker
```bash
docker compose up --build
```

### 3. Crear superusuario
```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Acceder
- App: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## 🧠 Flujo recomendado de uso

1. Inicia sesión.
2. Crea un formulario.
3. Agrega preguntas (editor).
4. Configura opciones para preguntas cerradas.
5. Comparte enlace público del formulario.
6. Revisa indicadores en módulo Analytics.

---

## 📊 Indicadores disponibles

- Total de respuestas por formulario.
- Conteo por opción en preguntas cerradas.
- Porcentaje por opción con barra de progreso.
- Conteo de respuestas contestadas en preguntas abiertas.

---

## ⚙️ Variables de entorno principales

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Clave secreta | `cambia-esto` |
| `DEBUG` | Modo debug | `0` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
| `POSTGRES_DB` | Nombre DB | `formsdb` |
| `POSTGRES_USER` | Usuario DB | `formsuser` |
| `POSTGRES_PASSWORD` | Password DB | `formspassword` |
| `POSTGRES_HOST` | Host DB | `db` |
| `POSTGRES_PORT` | Puerto DB | `5432` |

---

## 👨‍💻 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack Developer · Automatización · Data**

### 📞 Contacto

- 📧 **Email:** zackharo1@gmail.com
- 📱 **WhatsApp:** [+593 988055517](https://wa.me/593988055517)
- 💻 **GitHub:** [ieharo1](https://github.com/ieharo1)
- 🌐 **Portafolio:** [ieharo1.github.io](https://ieharo1.github.io/portafolio-isaac.haro/)

---

## 📄 Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

---

⭐ Si te gustó el proyecto, ¡dame una estrella en GitHub!
