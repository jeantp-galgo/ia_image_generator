import json
import os

class PromptGenerator:
    def __init__(self, model: str, city: str, environment: str, action: str, rider: str = "", lighting_style: str = "", extras: str = "", composition: str = "", camera_distance: str = "") -> None:
        self.model = model
        self.city = city
        self.environment = environment
        self.action = action
        self.rider = rider
        self.lighting_style = lighting_style
        self.extras = extras
        self.composition = composition
        self.camera_distance = camera_distance

    def build_motorcycle_prompt(self) -> str:
        """
        Estructura:
        1) Tipo de imagen y objetivo (marca, modelo, forma original)
        2) Entorno y ambientación con ciudad
        3) Conductor (si existe)
        4) Acción (debe ser coherente con la presencia/ausencia de conductor)
        5) Composición y distancia de cámara
        6) Estilo fotográfico (iluminación)
        7) Extras
        """
        parts = [
            # 1) Tipo de imagen y objetivo (marca, modelo, forma original)
            f"Professional realistic photograph of a {self.model} motorcycle",
            "keeping its original shape and design.",
            # 2) Entorno y ambientación con ciudad
            self.environment.strip(),
            f"in {self.city.strip()}" if self.city.strip() else "",
            # 3) Conductor (si existe)
            self.rider.strip() if self.rider else "",
            # 4) Acción (debe ser coherente con la presencia/ausencia de conductor)
            self.action.strip(),
            # 5) Composición y distancia de cámara
            self.composition.strip() if self.composition else "positioned using rule of thirds, off-center composition for natural look",
            self.camera_distance.strip() if self.camera_distance else "medium distance shot",
            # 6) Estilo fotográfico (iluminación)
            self.lighting_style.strip() if self.lighting_style else "",
            # 7) Extras
            self.extras.strip() if self.extras else "",
        ]
        # Une y limpia espacios dobles
        prompt = " ".join(p for p in parts if p).replace("  ", " ").strip()
        return prompt