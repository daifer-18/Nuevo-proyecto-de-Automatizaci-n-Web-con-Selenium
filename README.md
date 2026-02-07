# 💰 Dolarito Scraper - Cotización del Dólar en Tiempo Real

Bot automatizado con **Selenium** y **Python** que extrae las cotizaciones del dólar oficial y blue desde [Dolarito.ar](https://www.dolarito.ar/) en tiempo real.

## 🚀 Características

- ✅ Extracción automática de precios del **Dólar Oficial**
- ✅ Extracción automática de precios del **Dólar Blue**
- ✅ Automatización con **Selenium WebDriver**
- ✅ Compatible con **Chrome** (gestión automática de ChromeDriver)
- ✅ Código limpio y documentado

## 📋 Requisitos

- Python 3.8 o superior
- Google Chrome instalado
- Conexión a internet

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/dolarito-scraper.git
cd dolarito-scraper
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**Windows:**
```bash
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🎯 Uso

Ejecuta el script principal:

```bash
python main.py
```

El script abrirá Chrome automáticamente, navegará a Dolarito.ar, extraerá los precios y los mostrará en consola.

### Ejemplo de salida:

```
Abriendo dolarito.ar...
Esperando que cargue el contenido...

======================================================================
           COTIZACIONES DEL DÓLAR - DOLARITO.AR
======================================================================

💵 DÓLAR OFICIAL
   Compra: $ 1.400
   Venta: $ 1.450

💶 DÓLAR BLUE
   Compra: $ 1.415
   Venta: $ 1.435

======================================================================

✅ Script ejecutado correctamente
```

## 📁 Estructura del Proyecto

```
dolarito-scraper/
│
├── venv/                 # Entorno virtual (no incluido en Git)
├── drivers/              # Carpeta para drivers opcionales
├── main.py               # Script principal
├── requirements.txt      # Dependencias del proyecto
├── .gitignore           # Archivos ignorados por Git
└── README.md            # Este archivo
```

## 🔧 Tecnologías Utilizadas

- **Python 3.14.3**
- **Selenium 4.40.0** - Automatización web
- **WebDriver** - Control del navegador Chrome

## 📝 Notas

- Selenium 4.x gestiona automáticamente ChromeDriver, no necesitas descargarlo manualmente
- El script espera 10 segundos para que la página cargue completamente
- Si la estructura de la página cambia, es posible que necesites actualizar los selectores

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👤 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [Tu Perfil](https://linkedin.com/in/tu-perfil)

## ⭐ ¿Te gustó el proyecto?

Si este proyecto te fue útil, ¡dale una estrella en GitHub! ⭐

---

**Nota:** Este proyecto es solo para fines educativos. Asegúrate de respetar los términos de servicio de Dolarito.ar al usar este scraper.
