import mimetypes
import base64

def imagen_a_data_url(ruta_imagen: str) -> str:
    """
    Convierte una imagen local a data URL en formato base64.

    Args:
        ruta_imagen: Ruta al archivo de imagen

    Returns:
        Data URL en formato base64
    """
    try:
        # Detectar tipo MIME
        mime_type, _ = mimetypes.guess_type(ruta_imagen)
        if not mime_type:
            mime_type = "image/png"

        # Leer y codificar imagen
        with open(ruta_imagen, 'rb') as f:
            imagen_data = base64.b64encode(f.read()).decode('utf-8')

        # Crear data URL
        data_url = f"data:{mime_type};base64,{imagen_data}"
        return data_url

    except Exception as e:
        raise RuntimeError(f"Error convirtiendo imagen a data URL: {e}")


def extraer_url_imagen(resultado: dict) -> str:
    """Extrae la URL de la imagen desde el resultado."""
    output = resultado.get("output")

    if not output:
        raise RuntimeError("No se encontró output en el resultado")

    # Caso 1: Output es directamente una URL string
    if isinstance(output, str):
        return output

    # Caso 2: Output es una lista con URLs
    if isinstance(output, list) and len(output) > 0:
        first_item = output[0]
        if isinstance(first_item, str):
            return first_item
        if hasattr(first_item, 'url'):
            return first_item.url

    # Caso 3: Output es un diccionario con 'url'
    if isinstance(output, dict):
        return output.get("url")

    # Caso 4: Output es un objeto con atributo url
    if hasattr(output, 'url'):
        return output.url

    raise RuntimeError("No se pudo extraer URL de imagen del resultado")