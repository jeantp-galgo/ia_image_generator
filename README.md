# Generador de Imágenes para Motocicletas con IA

Sistema especializado para generar imágenes de motocicletas usando inteligencia artificial, con soporte para prompts estructurados e imagen de referencia.

## Características

- ✅ Generación de imágenes de motocicletas usando IA (modelo configurable)
- ✅ Sistema de prompts estructurados por tipo de motocicleta
- ✅ Entornos específicos y apropiados para cada tipo (ciudad, offroad, sport, touring, transport)
- ✅ Composición natural con regla de tercios (no centrada)
- ✅ Soporte para imagen de referencia para mantener consistencia visual
- ✅ Configuración modular de entornos, acciones, iluminación y estilos
- ✅ Generación aleatoria con variedad automática
- ✅ Control de ciudad/ubicación geográfica
- ✅ Descarga automática de imágenes generadas
- ✅ Manejo de errores robusto
- ✅ Estructura de proyecto organizada y escalable

## SOP

[Accede al SOP aquí](https://docs.google.com/document/d/1HJJP0CVWSXMks39Rsei6seIly0ZY-5KWQe2C2eKG3o4/edit?usp=sharing)

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Obtén tu API token de Replicate:
   - Ve a [Replicate](https://replicate.com)
   - Crea una cuenta y obtén tu token de API

## Estructura del Proyecto

```
generar_imagenes/
├── src/
│   ├── processors/
│   │   ├── generador_imagenes_basico.py  # Generador principal
│   │   └── prompt_generator.py           # Constructor de prompts
│   ├── utils/
│   │   ├── utils.py                      # Utilidades generales
│   │   ├── replicate_utils.py            # Utilidades de Replicate
│   │   ├── variety_generator.py          # Generador de variedad
│   │   └── random_prompt_generator.py    # Generador de prompts aleatorios
│   ├── data/
│   │   ├── prompts/
│   │   │   └── img_prompts.json          # Configuración de prompts
│   │   └── img/
│   │       ├── input/                    # Imágenes de referencia
│   │       └── output/                   # Imágenes generadas
│   └── notebooks/
│       └── test/
│           └── app.ipynb                 # Notebook principal
├── requirements.txt
└── README.md
```

## Uso Rápido

### Método 1: Usando el Sistema de Prompts Estructurados
```python
import json
from src.processors.prompt_generator import PromptGenerator
from src.processors.generador_imagenes_basico import generar_imagen_con_referencia

# Cargar configuración de prompts
with open("src/data/prompts/img_prompts.json", "r") as f:
    prompts_config = json.load(f)

# Definir producto
PRODUCT_BRAND = "Yamaha"
PRODUCT_MODEL = "MT 15"
CITY = "Ciudad de México"

# Generar prompt estructurado
prompt_imagen = PromptGenerator.build_motorcycle_prompt(
    model=f"{PRODUCT_BRAND} {PRODUCT_MODEL}",
    city=CITY,
    environment=prompts_config["ENVIRONMENTS"]["city"]["street"],
    action=prompts_config["ACTIONS"]["default"]["riding_confident"],
    rider_block=prompts_config["RIDERS"]["city"]["default"],
    lighting_style=prompts_config["LIGHTING"]["night_cinematic"],
    extras=prompts_config["STYLE_EXTRAS"]["motion_blur"]
)

# Generar imagen
url_imagen = generar_imagen_con_referencia(
    prompt=prompt_imagen,
    imagen_referencia="ruta/a/imagen_referencia.jpg",
    ruta_destino="imagen_generada.png"
)
```

### Método 2: Generación Aleatoria Automática
```python
from src.utils.random_prompt_generator import generate_random_prompt
from src.processors.generador_imagenes_basico import generar_imagen_con_referencia

# Generar prompt aleatorio basado en tipo de motocicleta
prompt_aleatorio = generate_random_prompt(
    motorcycle_type="Naked",  # Tipo de motocicleta
    city="Ciudad de México",
    model="Yamaha MT 15"
)

# Generar imagen
url_imagen = generar_imagen_con_referencia(
    prompt=prompt_aleatorio,
    imagen_referencia="ruta/a/imagen_referencia.jpg",
    ruta_destino="imagen_generada.png"
)
```

### Método 3: Función Simple (Uso Básico)
```python
from src.processors.generador_imagenes_basico import generar_imagen_con_referencia

# Generar imagen con prompt manual
url_imagen = generar_imagen_con_referencia(
    prompt="Professional photograph of a Yamaha MT 15 motorcycle in a city street",
    imagen_referencia="ruta/a/imagen_referencia.jpg",
    ruta_destino="imagen_generada.png"
)
```

## Configuración de Prompts

El sistema utiliza un archivo JSON (`src/data/prompts/img_prompts.json`) para configurar los diferentes elementos del prompt:

### Tipos de Motocicletas Soportados
- **Ciudad**: Naked, Trabajo, Motoneta, Café Racer, Semiautomática, Chopper, Trimoto, Eléctrica
- **Offroad**: Doble Propósito, Enduro, Cuatrimoto, ATV
- **Sport**: Deportiva
- **Touring**: Touring
- **Transport**: Carga, Carguero

### Entornos por Tipo de Motocicleta

#### Entornos de Ciudad
- `street`: Calle típica de ciudad
- `downtown`: Centro con tiendas y cafés
- `suburban`: Área residencial suburbana
- `park`: Parque de la ciudad
- `commercial`: Distrito comercial
- `residential`: Barrio residencial
- `plaza`: Plaza o plaza de la ciudad
- `boulevard`: Bulevar con árboles
- `garage`: Garaje o showroom moderno

#### Entornos Offroad
- `desert`: Paisaje desértico
- `forest`: Entorno forestal
- `mountain`: Área montañosa
- `trail`: Sendero de tierra
- `rural`: Entorno rural
- `countryside`: Campo
- `hills`: Colinas onduladas
- `canyon`: Cañón

#### Entornos Deportivos
- `race_track`: Pista profesional de carreras
- `city_highway`: Autopista urbana moderna
- `urban_street`: Calle urbana con arquitectura moderna
- `garage`: Garaje o showroom moderno
- `city_center`: Centro de ciudad con edificios contemporáneos
- `asphalt_road`: Carretera de asfalto suave

### Acciones Disponibles
- `parked_angle`: Estacionada en ángulo
- `riding_confident`: Conduciendo con confianza
- `closeup_static`: Primer plano estático
- `offroad_action`: Acción todoterreno

### Conductores por Tipo
- **Ciudad**: default, rider_leather, rider_casual
- **Offroad**: default
- **Sport**: default
- **Touring**: default
- **Transport**: default, transport_trimoto

### Composición
- `rule_of_thirds`: Regla de tercios, composición descentrada
- `dynamic_angle`: Ángulo dinámico con sensación de movimiento
- `environmental`: Composición ambiental equilibrada
- `cinematic`: Composición cinematográfica
- `lifestyle`: Fotografía de estilo de vida natural
- `editorial`: Composición editorial

### Estilos de Iluminación
- `day_warm`: Luz diurna cálida
- `golden_hour`: Hora dorada
- `night_cinematic`: Iluminación nocturna cinematográfica
- `overcast_soft`: Luz difusa nublada

### Extras de Estilo
- `bokeh`: Fondo desenfocado
- `motion_blur`: Desenfoque de movimiento
- `advertising`: Estilo publicitario

## Parámetros

### PromptGenerator.build_motorcycle_prompt()
- `model`: Marca y modelo de la motocicleta (ej: "Yamaha MT 15")
- `city`: Ciudad donde se ubica la imagen (ej: "Ciudad de México")
- `environment`: Entorno desde img_prompts.json
- `action`: Acción desde img_prompts.json
- `rider_block`: Descripción del conductor (opcional)
- `lighting_style`: Estilo de iluminación (opcional)
- `extras`: Extras de estilo (opcional)
- `composition`: Composición (opcional, por defecto: regla de tercios)
- `camera_distance`: Distancia de cámara (opcional, por defecto: medium)

### generate_random_prompt()
- `motorcycle_type`: Tipo de motocicleta (ej: "Naked", "Deportiva", "Doble Propósito")
- `city`: Ciudad donde se ubica la imagen
- `model`: Modelo de la motocicleta
- `rider_block`: Descripción del conductor (opcional)
- `prompts_config_path`: Ruta al archivo de configuración

### generar_imagen_con_referencia()
- `prompt`: Prompt generado o manual
- `imagen_referencia`: Ruta a imagen de referencia
- `ruta_destino`: Donde guardar la imagen (opcional)
- `api_token`: Token de API de Replicate (obligatorio)
- `modelo`: Modelo a usar (por defecto: "google/nano-banana")

## Modelos Disponibles

Por defecto usa `google/nano-banana`, pero puedes cambiar a otros modelos de Replicate:

- `google/nano-banana` (por defecto)
- `stability-ai/sdxl`
- `stability-ai/stable-diffusion-xl-base-1.0`
- Y muchos más disponibles en [Replicate](https://replicate.com/explore)

## Ejemplos de Prompts Generados

### Motocicleta en Ciudad Nocturna
```
Professional realistic photograph of a Yamaha MT 15 motorcycle, keeping its original shape and design. The motorcycle is riding through a modern city street with tall glass buildings, trees, and light urban traffic. May include a Mexican rider wearing an open-face helmet, black leather jacket, and a pastel blue T-shirt Riding confidently with a relaxed posture, slight lean forward, wheels in motion. Cinematic night lighting, reflections on wet asphalt, soft contrast and controlled highlights. Subtle motion blur on the background and wheels to convey speed and movement.
```

### Motocicleta Estacionada en Avenida
```
Professional realistic photograph of a Honda CBR 250R motorcycle, keeping its original shape and design. Placed on a wide Latin American city avenue with modern buildings, trees, and light traffic. The motorcycle is parked upright, slightly angled toward the camera to highlight its design and metallic details. Warm daylight illumination, soft shadows, and natural reflections on the metallic tank. Background slightly blurred (soft bokeh) to emphasize the motorcycle in the foreground.
```

### Motocicleta Todoterreno
```
Professional realistic photograph of a Kawasaki KLX 150 motorcycle, keeping its original shape and design. Placed on a rugged dirt trail with rocks, loose soil, and patches of mud, surrounded by wild vegetation and open landscape. May include a Mexican rider wearing an adventure or motocross helmet with a visor, protective off-road jacket with armored pads, sturdy riding boots, and gloves. The motorcycle is navigating rugged terrain, with dust or mud thrown from the tires, suspension visibly compressed, and the rider in a dynamic posture. Soft overcast daylight, diffused shadows, balanced contrast and even surface reflections.
```

## Notas

- La imagen de referencia puede ser una ruta local o una URL
- El proceso puede tomar entre 30 segundos y 2 minutos dependiendo del modelo
- Las imágenes se generan en alta calidad
- Soporta formatos PNG y JPG
- El sistema está optimizado para motocicletas pero puede adaptarse a otros vehículos

## Ejemplo Completo

```python
import json
import os
from src.utils.random_prompt_generator import generate_random_prompt
from src.processors.generador_imagenes_basico import generar_imagen_con_referencia

# Configuración
API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
PRODUCT_BRAND = "Yamaha"
PRODUCT_MODEL = "MT 15"
MOTORCYCLE_TYPE = "Naked"  # Tipo de motocicleta
CITY = "Ciudad de México"

try:
    # Generar prompt aleatorio basado en tipo de motocicleta
    prompt_imagen = generate_random_prompt(
        motorcycle_type=MOTORCYCLE_TYPE,
        city=CITY,
        model=f"{PRODUCT_BRAND} {PRODUCT_MODEL}"
    )

    print("🎨 Prompt generado:")
    print(prompt_imagen)

    # Generar y descargar imagen
    ruta_resultado = generar_imagen_con_referencia(
        prompt=prompt_imagen,
        imagen_referencia="src/data/img/input/mi_moto_referencia.jpg",
        ruta_destino=f"src/data/img/output/{PRODUCT_BRAND}-{PRODUCT_MODEL}-generada.png"
    )

    print(f"✅ Imagen generada exitosamente: {ruta_resultado}")

except Exception as e:
    print(f"❌ Error: {e}")
```

## Características Avanzadas

### Generación con Variedad
El sistema incluye elementos de variedad automática:
- **Clima**: sunny day, cloudy day, golden hour, sunset, sunrise, rainy day, foggy morning
- **Tiempo**: during the day, at night, in the evening, in the morning, during twilight
- **Atmósfera**: natural lighting, dramatic lighting, soft lighting, vibrant colors, muted tones
- **Fondo**: varied background elements, architectural details, natural elements

### Composición Natural
- **Regla de tercios**: Posicionamiento descentrado para composición natural
- **Ángulos dinámicos**: Sensación de movimiento y dinamismo
- **Composición ambiental**: Equilibrio entre motocicleta y entorno
- **Estilo cinematográfico**: Composiciones más profesionales y atractivas

### Entornos Específicos por Tipo
- **Motocicletas deportivas**: Pistas de carreras, autopistas urbanas, calles modernas
- **Motocicletas de ciudad**: Calles típicas, centros comerciales, parques, garajes
- **Motocicletas offroad**: Desiertos, bosques, montañas, senderos de tierra
- **Motocicletas touring**: Carreteras escénicas, rutas de montaña, carreteras costeras
- **Motocicletas de transporte**: Áreas industriales, almacenes, puertos