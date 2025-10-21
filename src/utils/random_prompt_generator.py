import random
import json
from typing import List, Dict

class randomPromptGenerator:
    """Generador de prompts de variedad."""

    def __init__(self, motorcycle_type: str, prompts_config_path: str = "../src/data/prompts/img_prompts.json"):
        """Inicializa el generador con la configuración de prompts."""
        self.motorcycle_type = motorcycle_type # Según el tipo de moto, se define el environment base
        self.motorcycles_offroad = ["Doble Propósito", "Enduro", "Cuatrimoto", "ATV"]
        self.motorcycles_city = ["Naked", "Trabajo", "Motoneta", "Café Racer", "Semiautomática", "Chopper", "Eléctrica"]
        self.motorcycles_sport = ["Deportiva"]
        self.motorcycles_tour = ["Touring"]
        self.motorcycles_transport = ["Carga", "Carguero"]
        self.motorcycles_transport_trimoto = ["Trimoto"]

        with open(prompts_config_path, "r") as f:
            self.config = json.load(f)

    def get_random_weather(self) -> str:
        """Obtiene un elemento de clima aleatorio."""
        return random.choice(self.config["VARIETY_ELEMENTS"]["weather"])

    def get_random_time(self) -> str:
        """Obtiene un elemento de tiempo aleatorio."""
        return random.choice(self.config["VARIETY_ELEMENTS"]["time"])

    def get_random_atmosphere(self) -> str:
        """Obtiene un elemento de atmósfera aleatorio."""
        return random.choice(self.config["VARIETY_ELEMENTS"]["atmosphere"])

    def get_random_background_variety(self) -> str:
        """Obtiene un elemento de variedad de fondo aleatorio."""
        return random.choice(self.config["VARIETY_ELEMENTS"]["background_variety"])

    def get_random_action(self) -> str:
        """Obtiene una acción aleatoria."""
        action_key = random.choice(list(self.config["ACTIONS"].keys()))
        return self.config["ACTIONS"][action_key]

    def get_random_environment(self) -> str:
        """Obtiene un entorno aleatorio según el tipo de moto."""
        print("La moto es de tipo: ", self.motorcycle_type)
        if self.motorcycle_type in self.motorcycles_offroad:
            env_dict = self.config["ENVIRONMENTS"]["offroad"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        elif self.motorcycle_type in self.motorcycles_city:
            env_dict = self.config["ENVIRONMENTS"]["city"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        elif self.motorcycle_type in self.motorcycles_sport:
            env_dict = self.config["ENVIRONMENTS"]["sport"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        elif self.motorcycle_type in self.motorcycles_tour:
            env_dict = self.config["ENVIRONMENTS"]["touring"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        elif self.motorcycle_type in self.motorcycles_transport:
            env_dict = self.config["ENVIRONMENTS"]["transport"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        elif self.motorcycle_type in self.motorcycles_transport_trimoto:
            env_dict = self.config["ENVIRONMENTS"]["transport_trimoto"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]
        else:
            # Fallback: usar entorno de ciudad por defecto
            env_dict = self.config["ENVIRONMENTS"]["city"]
            env_key = random.choice(list(env_dict.keys()))
            return env_dict[env_key]

    def get_random_lighting(self) -> str:
        """Obtiene una iluminación aleatoria."""
        light_key = random.choice(list(self.config["LIGHTING"].keys()))
        return self.config["LIGHTING"][light_key]

    def get_random_style_extra(self) -> str:
        """Obtiene un estilo extra aleatorio."""
        style_key = random.choice(list(self.config["STYLE_EXTRAS"].keys()))
        return self.config["STYLE_EXTRAS"][style_key]

    def get_random_composition(self) -> str:
        """Obtiene una composición aleatoria."""
        comp_key = random.choice(list(self.config["COMPOSITION"].keys()))
        return self.config["COMPOSITION"][comp_key]

    def get_random_camera_distance(self) -> str:
        """Obtiene una distancia de cámara aleatoria."""
        camera_distance_key = random.choice(list(self.config["CAMERA_DISTANCE"].keys()))
        return self.config["CAMERA_DISTANCE"][camera_distance_key]

    def generate_variety_elements(self, num_elements: int = 2) -> List[str]:
        """
        Genera una lista de elementos aleatorios para añadir variedad.

        Args:
            num_elements: Número de elementos aleatorios a generar

        Returns:
            Lista de elementos aleatorios
        """
        all_elements = []

        # Agregar elementos de variedad
        all_elements.extend(self.config["VARIETY_ELEMENTS"]["weather"])
        all_elements.extend(self.config["VARIETY_ELEMENTS"]["time"])
        all_elements.extend(self.config["VARIETY_ELEMENTS"]["atmosphere"])
        all_elements.extend(self.config["VARIETY_ELEMENTS"]["background_variety"])

        # Seleccionar elementos aleatorios sin repetir
        selected = random.sample(all_elements, min(num_elements, len(all_elements)))
        return selected

    def add_variety_to_prompt(self, base_prompt: str, num_variety_elements: int = 2) -> str:
        """
        Añade elementos de variedad a un prompt base.

        Args:
            base_prompt: Prompt base al que añadir variedad
            num_variety_elements: Número de elementos de variedad a añadir

        Returns:
            Prompt con elementos de variedad añadidos
        """
        variety_elements = self.generate_variety_elements(num_variety_elements)

        # Añadir elementos de variedad al final del prompt
        variety_text = ", ".join(variety_elements)
        return f"{base_prompt}, {variety_text}"

    def get_random_combination(self) -> Dict[str, str]:
        """
        Obtiene una combinación aleatoria de todos los elementos.

        Returns:
            Diccionario con la combinación aleatoria
        """
        return {
            "environment": self.get_random_environment(),
            "lighting": self.get_random_lighting(),
            "style_extra": self.get_random_style_extra(),
            "composition": self.get_random_composition(),
            "weather": self.get_random_weather(),
            "time": self.get_random_time(),
            "atmosphere": self.get_random_atmosphere(),
            "background_variety": self.get_random_background_variety()
        }

# Función helper para uso rápido
def generate_random_prompt(
    motorcycle_type: str,
    city: str,
    model: str,
    rider_block: str = "",
    prompts_config_path: str = "./src/data/prompts/img_prompts.json"
) -> str:
    """
    Genera un prompt aleatorio para una motocicleta.

    Args:
        motorcycle_type: Tipo de motocicleta
        model: Modelo de la motocicleta
        rider_block: Descripción del conductor

    Returns:
        Prompt aleatorio para una motocicleta
    """
    from src.processors.prompt_generator import PromptGenerator

    random_prompt_generator = randomPromptGenerator(motorcycle_type, prompts_config_path)


    # Generar prompt base
    base_prompt = PromptGenerator.build_motorcycle_prompt(
        model=model,
        city=city,
        environment= random_prompt_generator.get_random_environment(),
        action=random_prompt_generator.get_random_action(),
        rider_block=rider_block,
        lighting_style=random_prompt_generator.get_random_lighting(),
        extras=random_prompt_generator.get_random_style_extra(),
        composition=random_prompt_generator.get_random_composition(),
        camera_distance=random_prompt_generator.get_random_camera_distance()
    )

    # Añadir variedad
    # return random_prompt_generator.add_variety_to_prompt(base_prompt, variety_elements)
    return base_prompt
