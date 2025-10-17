import time
import replicate

def esperar_completado(client: replicate.Client, prediction_id: str, intervalo: int = 10) -> dict:
    """Espera a que la predicción se complete."""
    print("⏳ Esperando generación...")

    while True:
        try:
            prediction = replicate.predictions.get(prediction_id)
            status = prediction.status

            if status == "succeeded":
                return {
                    "id": prediction.id,
                    "status": status,
                    "output": prediction.output
                }

            if status in ("failed", "canceled"):
                error_msg = getattr(prediction, 'error', 'Error desconocido')
                raise RuntimeError(f"Generación {status}: {error_msg}")

            print(f"   Estado: {status}...")
            time.sleep(intervalo)

        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            time.sleep(intervalo)