import os
from PIL import Image

"""
CARROS USADOS
"""

class ResizeImage:
    @staticmethod
    def resize_and_crop_transparent(image_path, output_path, target_width, target_height):
        """
        Redimensiona y recorta la imagen para llenar completamente el área objetivo, dejando el fondo transparente.
        """
        # Cargar la imagen con PIL y asegurar canal alfa
        img = Image.open(image_path).convert("RGBA")

        # Convertir a escala de grises para encontrar los bordes del contenido
        gray = img.convert("L")
        bbox = gray.getbbox()

        if bbox:
            # Recortar la imagen para eliminar el fondo blanco alrededor
            img = img.crop(bbox)

        # Calcular las proporciones
        target_ratio = target_width / target_height
        img_ratio = img.width / img.height

        if img_ratio > target_ratio:
            # La imagen es más ancha, recortar los lados
            new_height = target_height
            new_width = int(target_height * img_ratio)
            img_resized = img.resize((new_width, new_height), Image.LANCZOS)
            left = int((new_width - target_width) / 2)
            img_cropped = img_resized.crop((left, 0, left + target_width, target_height))
        else:
            # La imagen es más alta, recortar la parte superior e inferior
            new_width = target_width
            new_height = int(target_width / img_ratio)
            img_resized = img.resize((new_width, new_height), Image.LANCZOS)
            top = int((new_height - target_height) / 2)
            img_cropped = img_resized.crop((0, top, target_width, top + target_height))

        # Crear un fondo transparente
        background = Image.new("RGBA", (target_width, target_height), (255, 255, 255, 0))
        # Pegar la imagen recortada sobre el fondo transparente usando el canal alfa como máscara
        background.paste(img_cropped, (0, 0), img_cropped)

        # Si el formato de salida es JPEG, convertir a RGB y fondo blanco (JPEG no soporta transparencia)
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            # Crear fondo blanco para JPEG
            background_rgb = Image.new("RGB", (target_width, target_height), (255, 255, 255))
            # Usar el canal alfa como máscara para pegar la imagen sobre el fondo blanco
            background_rgb.paste(background, mask=background.split()[3])
            background_rgb.save(output_path)
        else:
            # Guardar la imagen con fondo transparente
            background.save(output_path)
        return True

    @staticmethod
    def process_images_in_folder(input_folder, output_folder, target_width, target_height):
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.avif')):
                image_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                # Verificar si el nombre del archivo contiene "lifestyle"
                if "lifestyle" in filename.lower():
                    specific_width = 1000
                    specific_height = 700
                else:
                    specific_width = target_width
                    specific_height = target_height

                try:
                    success = ResizeImage.resize_and_crop_transparent(
                        image_path,
                        output_path,
                        specific_width,
                        specific_height
                    )
                    if success:
                        print(f"Procesada: {filename}")
                    else:
                        print(f"No se pudo procesar: {filename}")
                except Exception as e:
                    print(f"Error procesando {filename}: {e}")