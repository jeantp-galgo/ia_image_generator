
class PromptGenerator:
    @staticmethod
    def build_motorcycle_prompt(
        model: str,
        city: str,
        environment: str,
        action: str,
        rider: str = "",
        lighting_style: str = "",
        extras: str = "",
        composition: str = "",
        camera_distance: str = ""
    ) -> str:
        """
        Estructura:
        1) Tipo de imagen y objetivo
        2) Descripción del modelo
        3) Entorno y ambientación con ciudad
        4) Acción (debe ser coherente con la presencia/ausencia de conductor)
        5) Conductor (si existe)
        6) Composición y distancia de cámara
        7) Estilo fotográfico (iluminación)
        8) Extras
        """
        parts = [
            # 1) Tipo de imagen y objetivo
            f"Professional realistic photograph of a {model} motorcycle",
            # 2) Descripción del modelo
            "keeping its original shape and design.",
            # 3) Entorno y ambientación con ciudad
            environment.strip(),
            f"in {city.strip()}" if city.strip() else "",
            # 4) Acción (debe ser coherente con la presencia/ausencia de conductor)
            action.strip(),
            # 5) Conductor (si existe)
            rider.strip() if rider else "",
            # 6) Composición y distancia de cámara
            composition.strip() if composition else "positioned using rule of thirds, off-center composition for natural look",
            camera_distance.strip() if camera_distance else "medium distance shot",
            # 7) Estilo fotográfico
            lighting_style.strip() if lighting_style else "",
            extras.strip() if extras else "",
        ]
        # Une y limpia espacios dobles
        prompt = " ".join(p for p in parts if p).replace("  ", " ").strip()
        return prompt