import json
import os

class TempPrompt:
    """ Clase para manejar prompts temporales """

    @staticmethod
    def load_temp_prompt(file_name: str) -> dict:
        try:
            with open(f"../../../src/data/temp/{file_name}.json", "r") as f:
                temp_prompt = json.load(f)
                return temp_prompt
        except FileNotFoundError:
            print(f"El archivo {file_name}.json no existe")
            return False

    @staticmethod
    def delete_temp_prompt(file_name: str) -> None:
        os.remove(f"../../../src/data/temp/{file_name}.json")
        print(f"Prompt temporal eliminado: {file_name}.json")

    @staticmethod
    def save_temp_prompt(prompt_info: dict) -> None:
        """ Guarda el prompt generado en un archivo JSON """
        model = prompt_info['model']
        with open(f"../../../src/data/temp/{model}.json", "w", encoding="utf-8") as f:
            json.dump(prompt_info, f, indent=4)