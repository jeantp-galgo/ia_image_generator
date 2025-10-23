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

    def get_random_rider(self, img_count: int, avoid: str = None) -> str:
        """Obtiene un elemento de Rider aleatorio dependiendo del tipo de moto, evitando el valor anterior."""

        # Si el contador de imágenes es mayor a 0.7, entonces retornará un conductor aleatorio
        if img_count == 1:
            if random.random() > 0.1:
                return ""

        # Determinar el diccionario de riders según el tipo de moto
        if self.motorcycle_type in self.motorcycles_city:
            rider_dict = self.config["RIDERS"]["city"]
        elif self.motorcycle_type in self.motorcycles_offroad:
            rider_dict = self.config["RIDERS"]["offroad"]
        elif self.motorcycle_type in self.motorcycles_sport:
            rider_dict = self.config["RIDERS"]["sport"]
        elif self.motorcycle_type in self.motorcycles_tour:
            rider_dict = self.config["RIDERS"]["touring"]
        elif self.motorcycle_type in self.motorcycles_transport:
            rider_dict = self.config["RIDERS"]["transport"]
        elif self.motorcycle_type in self.motorcycles_transport_trimoto:
            rider_dict = self.config["RIDERS"]["transport_trimoto"]
        else:
            rider_dict = self.config["RIDERS"]["default"]

        # Filtrar el valor a evitar si existe
        available_keys = list(rider_dict.keys())
        if avoid and avoid in rider_dict.values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in rider_dict.items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(rider_dict.keys())

        rider_key = random.choice(available_keys)
        return rider_dict[rider_key]

    def get_random_action(self, has_rider: bool = True, avoid: str = None) -> str:
        """Obtiene una acción aleatoria, evitando el valor anterior."""
        if not has_rider:
            # Sin conductor: usar acciones genéricas
            action_dict = self.config["ACTIONS"]["without_rider"]
        else:
            # Con conductor: usar acciones específicas por tipo
            if self.motorcycle_type in self.motorcycles_offroad:
                action_dict = self.config["ACTIONS"]["with_rider"]["offroad"]
            elif self.motorcycle_type in self.motorcycles_city:
                action_dict = self.config["ACTIONS"]["with_rider"]["city"]
            elif self.motorcycle_type in self.motorcycles_sport:
                action_dict = self.config["ACTIONS"]["with_rider"]["sport"]
            elif self.motorcycle_type in self.motorcycles_tour:
                action_dict = self.config["ACTIONS"]["with_rider"]["touring"]
            elif self.motorcycle_type in self.motorcycles_transport:
                action_dict = self.config["ACTIONS"]["with_rider"]["transport"]
            elif self.motorcycle_type in self.motorcycles_transport_trimoto:
                action_dict = self.config["ACTIONS"]["with_rider"]["transport_trimoto"]
            else:
                # Fallback: usar acciones de ciudad
                action_dict = self.config["ACTIONS"]["with_rider"]["city"]

        # Filtrar el valor a evitar si existe
        available_keys = list(action_dict.keys())
        if avoid and avoid in action_dict.values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in action_dict.items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(action_dict.keys())

        action_key = random.choice(available_keys)
        return action_dict[action_key]

    def get_random_environment(self, avoid: str = None) -> str:
        """Obtiene un entorno aleatorio según el tipo de moto, evitando el valor anterior."""
        # print("La moto es de tipo: ", self.motorcycle_type)
        if self.motorcycle_type in self.motorcycles_offroad:
            env_dict = self.config["ENVIRONMENTS"]["offroad"]
        elif self.motorcycle_type in self.motorcycles_city:
            env_dict = self.config["ENVIRONMENTS"]["city"]
        elif self.motorcycle_type in self.motorcycles_sport:
            env_dict = self.config["ENVIRONMENTS"]["sport"]
        elif self.motorcycle_type in self.motorcycles_tour:
            env_dict = self.config["ENVIRONMENTS"]["touring"]
        elif self.motorcycle_type in self.motorcycles_transport:
            env_dict = self.config["ENVIRONMENTS"]["transport"]
        elif self.motorcycle_type in self.motorcycles_transport_trimoto:
            env_dict = self.config["ENVIRONMENTS"]["transport_trimoto"]
        else:
            # Fallback: usar entorno de ciudad por defecto
            env_dict = self.config["ENVIRONMENTS"]["city"]

        # Filtrar el valor a evitar si existe
        available_keys = list(env_dict.keys())
        if avoid and avoid in env_dict.values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in env_dict.items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(env_dict.keys())

        env_key = random.choice(available_keys)
        return env_dict[env_key]

    def get_random_lighting(self, avoid: str = None) -> str:
        """Obtiene una iluminación aleatoria, evitando el valor anterior."""
        available_keys = list(self.config["LIGHTING"].keys())

        # Filtrar el valor a evitar si existe
        if avoid and avoid in self.config["LIGHTING"].values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in self.config["LIGHTING"].items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(self.config["LIGHTING"].keys())

        light_key = random.choice(available_keys)
        return self.config["LIGHTING"][light_key]

    def get_random_style_extra(self, has_rider: bool = True, avoid: str = None) -> str:
        """Obtiene un estilo extra aleatorio basado en si hay conductor o no, evitando el valor anterior."""
        if has_rider:
            # Con conductor: usar estilos dinámicos
            style_dict = self.config["STYLE_EXTRAS"]["dynamic"]
        else:
            # Sin conductor: usar estilos estáticos
            style_dict = self.config["STYLE_EXTRAS"]["static"]

        available_keys = list(style_dict.keys())

        # Filtrar el valor a evitar si existe
        if avoid and avoid in style_dict.values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in style_dict.items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(style_dict.keys())

        style_key = random.choice(available_keys)
        return style_dict[style_key]

    def get_random_composition(self, avoid: str = None) -> str:
        """Obtiene una composición aleatoria, evitando el valor anterior."""
        available_keys = list(self.config["COMPOSITION"].keys())

        # Filtrar el valor a evitar si existe
        if avoid and avoid in self.config["COMPOSITION"].values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in self.config["COMPOSITION"].items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(self.config["COMPOSITION"].keys())

        comp_key = random.choice(available_keys)
        return self.config["COMPOSITION"][comp_key]

    def get_random_camera_distance(self, avoid: str = None) -> str:
        """Obtiene una distancia de cámara aleatoria, evitando el valor anterior."""
        available_keys = list(self.config["CAMERA_DISTANCE"].keys())

        # Filtrar el valor a evitar si existe
        if avoid and avoid in self.config["CAMERA_DISTANCE"].values():
            # Encontrar la clave que corresponde al valor a evitar
            for key, value in self.config["CAMERA_DISTANCE"].items():
                if value == avoid:
                    available_keys.remove(key)
                    break

        # Si no hay opciones disponibles, usar todas
        if not available_keys:
            available_keys = list(self.config["CAMERA_DISTANCE"].keys())

        camera_distance_key = random.choice(available_keys)
        return self.config["CAMERA_DISTANCE"][camera_distance_key]

# Función helper para uso rápido
def generate_random_prompt(
    motorcycle_type: str,
    city: str,
    model: str,
    img_count: int = 0,
    prompts_config_path: str = "./src/data/prompts/img_prompts.json",
) -> str:
    """
    Genera un prompt aleatorio para una motocicleta.

    Args:
        motorcycle_type: Tipo de motocicleta
        city: Ciudad donde se generará la imagen
        model: Marca y modelo de la motocicleta
        img_count: Número de imagen para determinar si hay conductor
        prompts_config_path: Ruta de los prompts predefinidos

    Returns:
        Prompt aleatorio para una motocicleta
    """
    from src.processors.prompt_generator import PromptGenerator
    from src.utils.temp_prompt import TempPrompt
    random_prompt_generator = randomPromptGenerator(motorcycle_type, prompts_config_path)

    # Cargar prompt temporal anterior para evitar repeticiones
    temp_prompt_info = TempPrompt.load_temp_prompt(model)
    if not temp_prompt_info:
        print(f"No se encontró el prompt temporal para {model} - Generando completamente aleatorio")
        # Si no hay prompt anterior, generar completamente aleatorio
        environment = random_prompt_generator.get_random_environment()
        rider = random_prompt_generator.get_random_rider(img_count)
        has_rider = bool(rider.strip())
        action = random_prompt_generator.get_random_action(has_rider)
        lighting_style = random_prompt_generator.get_random_lighting()
        extras = random_prompt_generator.get_random_style_extra(has_rider)
        composition = random_prompt_generator.get_random_composition()
        camera_distance = random_prompt_generator.get_random_camera_distance()
    else:
        print(f"Prompt temporal encontrado para {model} - Evitando repeticiones")
        # Usar valores anteriores para evitar repeticiones
        environment = random_prompt_generator.get_random_environment(avoid=temp_prompt_info.get("environment"))
        rider = random_prompt_generator.get_random_rider(img_count, avoid=temp_prompt_info.get("rider"))
        has_rider = bool(rider.strip())
        action = random_prompt_generator.get_random_action(has_rider, avoid=temp_prompt_info.get("action"))
        lighting_style = random_prompt_generator.get_random_lighting(avoid=temp_prompt_info.get("lighting_style"))
        extras = random_prompt_generator.get_random_style_extra(has_rider, avoid=temp_prompt_info.get("extras"))
        composition = random_prompt_generator.get_random_composition(avoid=temp_prompt_info.get("composition"))
        camera_distance = random_prompt_generator.get_random_camera_distance(avoid=temp_prompt_info.get("camera_distance"))

    # Generar prompt base
    prompt_generator = PromptGenerator(
        model=model,
        city=city,
        environment= environment,
        rider=rider,
        action=action,
        lighting_style=lighting_style,
        extras=extras,
        composition=composition,
        camera_distance=camera_distance
    )
    # Generar prompt
    base_prompt = prompt_generator.build_motorcycle_prompt()

    prompt_info = {
        "model": model,
        "city": city,
        "environment": environment,
        "rider": rider,
        "action": action,
        "lighting_style": lighting_style,
        "extras": extras,
        "composition": composition,
        "camera_distance": camera_distance
    }
    TempPrompt.save_temp_prompt(prompt_info)

    return base_prompt
