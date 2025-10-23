# ============================================================================
# GENERADOR DE IMÁGENES BÁSICO CON REFERENCIA
# Versión simplificada para generar imágenes usando prompt + imagen de referencia
# ============================================================================

import os
import time
import requests
import replicate
from src.utils.utils import *
from src.utils.replicate_utils import *
from typing import Optional

class GeneradorImagenes:
    """Clase básica para generar imágenes usando Replicate con imagen de referencia."""

    def __init__(self, modelo: str = "google/nano-banana"):
        """
        Inicializa el generador de imágenes.

        Args:
            api_token: Token de API de Replicate
            modelo: Modelo a usar para generación (por defecto: google/nano-banana)
        """
        self.api_token = os.getenv("REPLICATE_API_TOKEN")
        self.modelo = modelo
        self.client = replicate.Client(api_token=self.api_token)


    def descargar_imagen(self, url: str, ruta_destino: str, nombre_archivo: str, nombre_carpeta: str) -> str:
        """
        Descarga una imagen desde URL y la guarda localmente en la carpeta especificada.

        Args:
            url: URL de la imagen
            ruta_destino: Ruta donde guardar la imagen
            nombre_archivo: Nombre del archivo
            nombre_carpeta: Nombre de la carpeta
        Returns:
            Ruta del archivo descargado
        """
        try:
            # Crear la carpeta dentro de ruta_destino con el nombre proporcionado
            carpeta_completa = os.path.join(ruta_destino, nombre_carpeta)
            os.makedirs(carpeta_completa, exist_ok=True)

            response = requests.get(url, timeout=60)
            response.raise_for_status()

            print("nombre archivo: ", nombre_archivo)

            ruta_archivo = os.path.join(carpeta_completa, nombre_archivo)
            with open(ruta_archivo, 'wb') as f:
                f.write(response.content)

            return ruta_archivo

        except Exception as e:
            raise RuntimeError(f"Error descargando imagen: {e}")

    def generar_imagen(self,
                      prompt: str,
                      imagen_referencia: str,
                      aspect_ratio: str = "4:3",
                      output_format: str = "png") -> str:
        """
        Genera una imagen usando prompt e imagen de referencia.

        Args:
            prompt: Descripción de la imagen a generar
            imagen_referencia: Ruta a imagen de referencia o data URL
            aspect_ratio: Proporción de la imagen ("1:1", "16:9", "9:16", etc.)
            output_format: Formato de salida ("png" o "jpg")

        Returns:
            URL de la imagen generada
        """
        try:
            print(f"🎨 Generando imagen con modelo: {self.modelo}")
            # print(f"📝 Prompt: {prompt}")
            # print(f"🖼️ Imagen referencia: {imagen_referencia[:50]}...")

            # Preparar parámetros de entrada
            input_params = {
                "prompt": prompt,
                "output_format": output_format,
                "aspect_ratio": aspect_ratio
            }

            # Si imagen_referencia es una ruta de archivo, convertir a data URL
            if os.path.exists(imagen_referencia):
                imagen_data_url = imagen_a_data_url(imagen_referencia)
                input_params["image_input"] = [imagen_data_url]
                print("✅ Imagen de referencia cargada desde archivo local")
            else:
                # Asumir que es una URL o data URL
                input_params["image_input"] = [imagen_referencia]
                print("✅ Usando imagen de referencia desde URL/data URL")

            # ? Enviar trabajo a Replicate
            print("📤 Enviando trabajo a Replicate...")
            prediction = self.client.predictions.create(
                model=self.modelo,
                input=input_params
            )

            if not prediction.id:
                raise RuntimeError("No se recibió ID de predicción")

            print(f"🔄 Procesando... (ID: {prediction.id})")

            # * Esperar a que complete
            resultado = esperar_completado(self.client, prediction.id)

            # * Extraer URL de la imagen generada
            url_imagen = extraer_url_imagen(resultado)

            print("✅ Imagen generada exitosamente!")
            return url_imagen

        except Exception as e:
            raise RuntimeError(f"Error generando imagen: {e}")

    # Función casi principal
    def generar_y_descargar(self,
                           prompt: str,
                           imagen_referencia: str,
                           ruta_destino: str,
                           nombre_archivo: str,
                           nombre_carpeta: str,
                           aspect_ratio: str = "4:3",
                           output_format: str = "png") -> str:
        """
        Genera imagen y la descarga automáticamente.

        Args:
            prompt: Descripción de la imagen
            imagen_referencia: Ruta o URL de imagen de referencia
            ruta_destino: Ruta donde guardar la imagen generada
            nombre_archivo: Nombre del archivo
            nombre_carpeta: Nombre de la carpeta
            aspect_ratio: Proporción de la imagen
            output_format: Formato de salida

        Returns:
            Ruta del archivo descargado
        """
        # Generar imagen
        url_imagen = self.generar_imagen(prompt, imagen_referencia, aspect_ratio, output_format)

        # Descargar imagen
        print(f"📥 Descargando imagen a: {ruta_destino}")
        ruta_final = self.descargar_imagen(url_imagen, ruta_destino, nombre_archivo, nombre_carpeta)

        print(f"✅ Imagen guardada en: {ruta_final}")
        return ruta_final


def generar_imagen_con_referencia(modelo: Optional[str],
                                  prompt: str,
                                  imagen_referencia: str,
                                  ruta_destino: Optional[str],
                                  nombre_archivo: Optional[str],
                                  nombre_carpeta: Optional[str]) -> str:
    """
    Genera una imagen rápidamente.

    Args:
        prompt: Descripción de la imagen
        imagen_referencia: Ruta o URL de imagen de referencia
        ruta_destino: Donde guardar (opcional, si no se da retorna URL)
        modelo: Modelo a usar

    Returns:
        URL de la imagen generada o ruta del archivo si se descargó
    """
    generador = GeneradorImagenes(modelo)

    if ruta_destino:
        return generador.generar_y_descargar(prompt, imagen_referencia, ruta_destino, nombre_archivo, nombre_carpeta)
    else:
        return generador.generar_imagen(prompt, imagen_referencia)