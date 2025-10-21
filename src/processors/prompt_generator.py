
class PromptGenerator:
    @staticmethod
    def build_motorcycle_prompt(
        model: str,
        city: str,
        environment: str,
        action: str,
        rider_block: str = "",
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
        4) Acciones y si existe conductor
        5) Composición y distancia de cámara
        6) Estilo fotográfico y extras (iluminación, foco, tono, etc.)
        """
        parts = [
            # 1) Tipo de imagen y objetivo
            f"Professional realistic photograph of a {model} motorcycle",
            # 2) Descripción del modelo
            "keeping its original shape and design.",
            # 3) Entorno y ambientación con ciudad
            environment.strip(),
            f"in {city.strip()}" if city.strip() else "",
            # 4) Acciones y si existe conductor
            action.strip() + (f" {rider_block.strip()}" if rider_block else ""),
            # 5) Composición y distancia de cámara
            composition.strip() if composition else "positioned using rule of thirds, off-center composition for natural look",
            camera_distance.strip() if camera_distance else "medium distance shot",
            # 6) Estilo fotográfico
            lighting_style.strip() if lighting_style else "",
            extras.strip() if extras else "",
        ]
        # Une y limpia espacios dobles
        prompt = " ".join(p for p in parts if p).replace("  ", " ").strip()
        return prompt