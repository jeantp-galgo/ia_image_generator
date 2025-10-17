# Generador de Imágenes Básico con Referencia

Un generador de imágenes simplificado que utiliza Replicate para crear imágenes usando un prompt y una imagen de referencia.

## Características

- ✅ Generación de imágenes usando IA (modelo configurable)
- ✅ Soporte para imagen de referencia para mantener consistencia visual
- ✅ Descarga automática de imágenes generadas
- ✅ Manejo de errores robusto
- ✅ Interfaz simple y fácil de usar
- ✅ Soporte para diferentes formatos y proporciones

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Obtén tu API token de Replicate:
   - Ve a [Replicate](https://replicate.com)
   - Crea una cuenta y obtén tu token de API

## Uso Rápido

### Método 1: Función Simple
```python
from generador_imagenes_basico import generar_imagen_simple

# Generar imagen y obtener URL
url_imagen = generar_imagen_simple(
    api_token="tu_token_aqui",
    prompt="Una persona sonriendo, estilo realista, fondo blanco",
    imagen_referencia="ruta/a/tu/imagen_referencia.jpg"
)

# Generar imagen y descargar automáticamente
ruta_imagen = generar_imagen_simple(
    api_token="tu_token_aqui",
    prompt="Una persona sonriendo, estilo realista, fondo blanco",
    imagen_referencia="ruta/a/tu/imagen_referencia.jpg",
    ruta_destino="imagen_generada.png"
)
```

### Método 2: Usando la Clase (Más Control)
```python
from generador_imagenes_basico import GeneradorImagenes

# Crear generador
generador = GeneradorImagenes("tu_token_aqui")

# Generar imagen
url = generador.generar_imagen(
    prompt="Una persona sonriendo, estilo realista, fondo blanco",
    imagen_referencia="ruta/a/tu/imagen_referencia.jpg",
    aspect_ratio="1:1",
    output_format="png"
)

# Descargar imagen
ruta_final = generador.descargar_imagen(url, "imagen_final.png")
```

## Parámetros

### Función Simple
- `api_token`: Token de API de Replicate (obligatorio)
- `prompt`: Descripción de la imagen a generar (obligatorio)
- `imagen_referencia`: Ruta a imagen de referencia o URL (obligatorio)
- `ruta_destino`: Donde guardar la imagen (opcional, si no se da retorna URL)
- `modelo`: Modelo a usar (por defecto: "google/nano-banana")

### Clase GeneradorImagenes
- `api_token`: Token de API de Replicate
- `modelo`: Modelo a usar (por defecto: "google/nano-banana")

#### Métodos:
- `generar_imagen()`: Genera imagen y retorna URL
- `generar_y_descargar()`: Genera imagen y la descarga automáticamente
- `descargar_imagen()`: Descarga imagen desde URL

#### Parámetros de generación:
- `prompt`: Descripción de la imagen
- `imagen_referencia`: Ruta o URL de imagen de referencia
- `aspect_ratio`: Proporción ("1:1", "16:9", "9:16", etc.)
- `output_format`: Formato ("png" o "jpg")

## Modelos Disponibles

Por defecto usa `google/nano-banana`, pero puedes cambiar a otros modelos de Replicate:

- `google/nano-banana` (por defecto)
- `stability-ai/sdxl`
- `stability-ai/stable-diffusion-xl-base-1.0`
- Y muchos más disponibles en [Replicate](https://replicate.com/explore)

## Ejemplos de Prompts

- "Una persona sonriendo, estilo realista, fondo blanco"
- "Un gato jugando con una pelota, estilo cartoon"
- "Una casa moderna, arquitectura minimalista, iluminación natural"
- "Un coche deportivo rojo, estilo fotográfico, fondo borroso"

## Manejo de Errores

El código incluye manejo robusto de errores para:
- Token de API inválido
- Imagen de referencia no encontrada
- Errores de red
- Fallos en la generación
- Problemas de descarga

## Notas

- La imagen de referencia puede ser una ruta local o una URL
- El proceso puede tomar entre 30 segundos y 2 minutos dependiendo del modelo
- Las imágenes se generan en alta calidad
- Soporta formatos PNG y JPG

## Ejemplo Completo

```python
from generador_imagenes_basico import generar_imagen_simple

# Configuración
API_TOKEN = "r8_xxxxxxxxxxxxxxxxxxxxxxxxxx"  # Tu token real
PROMPT = "Una persona sonriendo, estilo realista, fondo blanco"
IMAGEN_REF = "foto_referencia.jpg"

try:
    # Generar y descargar imagen
    ruta_resultado = generar_imagen_simple(
        api_token=API_TOKEN,
        prompt=PROMPT,
        imagen_referencia=IMAGEN_REF,
        ruta_destino="resultado.png"
    )

    print(f"✅ Imagen generada exitosamente: {ruta_resultado}")

except Exception as e:
    print(f"❌ Error: {e}")
```
