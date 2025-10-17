
class PromptGenerator:
    @staticmethod
    def build_motorcycle_prompt(
        model: str,
        environment: str,
        action: str,
        rider_block: str = "",
        lighting_style: str = "",
        extras: str = ""
    ) -> str:
        """
        Estructura:
        1) Tipo de imagen y objetivo
        2) Descripción del modelo
        3) Entorno y ambientación
        4) Acciones y si existe conductor
        5) Estilo fotográfico y extras (iluminación, foco, tono, etc.)
        """
        parts = [
            # 1) Tipo de imagen y objetivo
            f"Professional realistic photograph of a {model} motorcycle",
            # 2) Descripción del modelo
            "keeping its original shape and design.",
            # 3) Entorno y ambientación
            environment.strip(),
            # 4) Acciones y si existe conductor
            action.strip() + (f" {rider_block.strip()}" if rider_block else ""),
            # 5) Estilo fotográfico
            lighting_style.strip() if lighting_style else "",
            extras.strip() if extras else "",
        ]
        # Une y limpia espacios dobles
        prompt = " ".join(p for p in parts if p).replace("  ", " ").strip()
        return prompt