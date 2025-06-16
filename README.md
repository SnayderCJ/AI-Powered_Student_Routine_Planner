# 🤖 Planificador de Rutinas Inteligente con IA

¡Bienvenido al futuro de la organización estudiantil! [cite_start]Este proyecto es un **Planificador de Rutinas Inteligente**, una plataforma web dinámica diseñada para revolucionar la gestión del tiempo de los estudiantes mediante el poder de la Inteligencia Artificial. 

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20.svg)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3-38B2AC.svg)](https://tailwindcss.com/)
[![AWS](https://img.shields.io/badge/AWS-Amazon_Web_Services-FF9900.svg)](https://aws.amazon.com/)

---

## 📜 Descripción del Proyecto

[cite_start]Este sistema, desarrollado con el robusto framework **Django** [cite: 10][cite_start], tiene como objetivo principal optimizar el uso del tiempo de los estudiantes, equilibrando sus actividades académicas con descansos adecuados[cite: 7]. [cite_start]La plataforma utiliza algoritmos de IA para ofrecer recomendaciones personalizadas y ajustes automáticos basados en los hábitos y el rendimiento del usuario [cite: 8][cite_start], buscando ser una herramienta proactiva y centrada en el bienestar estudiantil.

[cite_start]El público objetivo son estudiantes de nivel medio y superior que deseen mejorar su organización [cite: 19][cite_start], evitar la procrastinación  [cite_start]y potenciar su rendimiento académico con una solución automática y adaptativa.

## ✨ Características Principales

[cite_start]El proyecto está organizado en los siguientes módulos para ofrecer una experiencia completa e intuitiva:

* [cite_start]**🔐 Módulo de Autenticación y Gestión de Usuarios:** Registro seguro, inicio de sesión tradicional e inicio de sesión rápido con Google. 
* [cite_start]**🗓️ Módulo de Gestión de Horarios:** Permite crear y visualizar horarios, planificar tareas y programar descansos de forma manual o automática. 
* [cite_start]**🧠 Módulo de Optimización Inteligente:** El núcleo de IA del sistema, que prioriza tareas, genera bloques de tiempo enfocados y reorganiza el horario automáticamente. 
* [cite_start]**🔔 Módulo de Recordatorios Inteligentes:** Envía notificaciones y recordatorios que se adaptan a la rutina y comportamiento del usuario. 
* [cite_start]**📊 Módulo de Seguimiento y Aprendizaje:** Analiza el rendimiento, registra la actividad y aprende de los hábitos del estudiante para ofrecer una personalización continua. 
* [cite_start]**❤️ Módulo de Bienestar y Formación:** Incluye alertas de descanso y recomendaciones de técnicas de estudio basadas en el desempeño del usuario. 

## 🛠️ Tecnologías Utilizadas

Este proyecto se construyó utilizando un stack de tecnologías moderno y escalable:

* [cite_start]**Backend:** Django (Python) 
* **Frontend:** Tailwind CSS
* **Base de Datos:** PostgreSQL (Recomendado para producción), SQLite (para desarrollo)
* [cite_start]**Despliegue:** Amazon Web Services (AWS) 
* [cite_start]**Inteligencia Artificial:** Modelo de IA personalizado para optimización de rutinas. 
* [cite_start]**Autenticación Externa:** Google OAuth 2.0 

## 🚀 Guía de Instalación y Ejecución Local

Para ejecutar este proyecto en tu máquina local, sigue estos pasos detallados:

### 1. Prerrequisitos

Asegúrate de tener instalados **Python** y **Node.js** en tu sistema. Puedes verificarlo con los siguientes comandos en tu terminal:

```bash
# Verificar la versión de Python (se recomienda 3.8 o superior)
python --version

# Verificar la versión de Node.js (se recomienda 14.x o superior)
node --version

# Verificar la versión de npm (gestor de paquetes de Node.js)
npm --version
```

### 2. Clonar el Repositorio

Primero, clona el repositorio desde GitHub a tu máquina local.

```bash
git clone [https://github.com/SnayderCJ/AI-Powered_Student_Routine_Planner.git](https://github.com/SnayderCJ/AI-Powered_Student_Routine_Planner.git)
cd AI-Powered_Student_Routine_Planner
```

### 3. Configuración del Backend (Django)

Vamos a configurar el entorno virtual y las dependencias de Python.

```bash
# 1. Crear un entorno virtual para aislar las dependencias del proyecto
python -m venv venv

# 2. Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# 3. Instalar todas las dependencias de Python listadas en requirements.txt
pip install -r requirements.txt
```

### 4. Configuración del Frontend (Tailwind CSS)

Ahora, instalaremos las dependencias de Node.js para que Tailwind CSS funcione correctamente.

```bash
# Instalar las dependencias de node (tailwindcss, postcss, etc.)
npm install
```

### 5. Configuración de Variables de Entorno

La seguridad es crucial. Este proyecto usa un archivo `.env` para gestionar las variables sensibles.

1.  En la raíz del proyecto, crea un archivo llamado `.env`.
2.  Copia el contenido del archivo `.env.example` (si existe) o usa la siguiente plantilla y pégala en tu nuevo archivo `.env`.
3.  **Completa los valores con tus propias credenciales.**

```env
# Configuración de Django
# ¡IMPORTANTE! Genera tu propia clave secreta. No uses esta en producción.
SECRET_KEY='tu-super-secreta-django-key'
DEBUG=True

# Configuración de la Base de Datos (ejemplo para PostgreSQL)
DATABASE_URL='postgres://user:password@host:port/dbname'

# Credenciales de Google OAuth 2.0 (para el inicio de sesión con Google)
# Obtenlas desde la Google Cloud Console
GOOGLE_CLIENT_ID='tu-google-client-id'
GOOGLE_CLIENT_SECRET='tu-google-client-secret'

# Credenciales de AWS (si usas S3 para archivos estáticos)
AWS_ACCESS_KEY_ID='tu-aws-access-key'
AWS_SECRET_ACCESS_KEY='tu-aws-secret-key'
AWS_STORAGE_BUCKET_NAME='tu-s3-bucket-name'
```

### 6. Finalizando la Configuración

Ya casi terminamos. Solo falta aplicar las migraciones de la base de datos.

```bash
# Aplicar las migraciones para crear las tablas en la base de datos
python manage.py migrate

# (Opcional pero recomendado) Crear un superusuario para acceder al admin de Django
python manage.py createsuperuser
```

### 7. ¡Ejecutar la Aplicación! ⚡️

Para correr la aplicación, necesitarás **dos terminales** abiertas simultáneamente en la raíz del proyecto.

**Terminal 1: Iniciar el proceso de Tailwind CSS**

Este comando vigilará tus archivos de plantilla y CSS para compilarlos automáticamente cada vez que hagas un cambio.

```bash
# Este comando ejecuta el script "tailwind" definido en tu package.json
npm run tailwind
```

**Terminal 2: Iniciar el servidor de Django**

Este comando pondrá en marcha el servidor de desarrollo de Django.

```bash
# ¡Asegúrate de que tu entorno virtual (venv) esté activado!
python manage.py runserver
```

¡Y listo! 🎉 Abre tu navegador web y visita **`http://127.0.0.1:8000`**. Deberías ver la página de inicio de sesión de tu aplicación.

## 🖼️ Vistas Previas de la Aplicación

Aquí tienes un vistazo de cómo luce nuestro **Planificador de Rutinas Inteligente**:

**Interfaz de Inicio de Sesión y Registro**
![Interfaz de Login](https://i.imgur.com/G5gR8t8.png)
[cite_start]_Ilustración 1: interfaz de usuario login _

**Dashboard Principal del Estudiante**
![Dashboard](https://i.imgur.com/2s3j4gH.png)
[cite_start]_Ilustración 3: interfaz de usuario Dashboard _

**Gestión de Tareas y Calendario Inteligente**
![Gestión de Tareas](https://i.imgur.com/bY3b6jT.png)
[cite_start]_Ilustración 4: interfaz de usuario Gestión de tareas y Calendario _

**Análisis de Productividad**
![Análisis de Productividad](https://i.imgur.com/uN8P8qR.png)
[cite_start]_Ilustración 6: interfaz de usuario Análisis de Productividad _

## 🧑‍💻 Autores

Este proyecto fue desarrollado con dedicación por los siguientes estudiantes de la carrera de Software en la UNEMI:

* [cite_start]**Mayerly Anabela Piloso Muñoz** 
* [cite_start]**Oswaldo Danilo Angulo Tamayo** 
* [cite_start]**Jostyn Snayder Cedeño Jimenez** (Gerente del Proyecto) 

Bajo la supervisión del docente Ing. [cite_start]Rodrigo Josue Guevara Reyes. 

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.