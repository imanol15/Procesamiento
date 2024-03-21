from pydantic import BaseModel, validator, Field
from datetime import datetime
import random

class DatosGenerador(BaseModel):
    id: int = Field(..., description="El identificador único del generador")
    valor_produccion: float = Field(..., description="La producción en kWh")
    velocidad_viento: float = Field(..., description="Velocidad del viento en m/s")
    direccion_viento: str = Field(..., description="Dirección del viento")
    temperatura: float = Field(..., description="Temperatura en grados Celsius")  
    error: bool = Field(..., description="Indica si hay un error en los datos")

    @validator('valor_produccion', 'velocidad_viento', 'temperatura')
    def valores_no_negativos(cls, v):
        if v < 0:
            raise ValueError(f'{cls.__name__} must be non-negative')
        return v

class Generador:
    def __init__(self, identificador: int):
        self.id = identificador


    def generar_datos(self, probabilidad_error: float) -> DatosGenerador:
        # Genera valores dentro del rango normal
        valor_produccion = random.uniform(10, 100)
        velocidad_viento = random.uniform(2, 25)
        direccion_viento = random.choice(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
        temperatura = random.uniform(0, 40)
        
        # Decide si se generarán datos erróneos
        datos_erroneos = random.random() < probabilidad_error
        
        # Si se decide que hay un error, asigna valores fuera del rango esperado pero positivos
        if datos_erroneos:
            # Asegúrate de que los valores sigan siendo positivos pero fuera del rango "normal"
            valor_produccion = random.uniform(120, 200)  # Valor más alto que el rango normal
            velocidad_viento = random.uniform(30, 100)  # Valor más alto que el rango normal
            temperatura = random.uniform(50, 100)  # Valor más alto que el rango normal
        
        # Comprueba si los valores están fuera del rango permitido
        valores_fuera_de_rango = valor_produccion > 100 or \
                                 velocidad_viento > 25 or \
                                 temperatura > 40

        error_en_datos = datos_erroneos or valores_fuera_de_rango

        # Crea el objeto DatosGenerador con los datos generados y el estado de error correspondiente
        return DatosGenerador(
            id=self.id,
            valor_produccion=valor_produccion,
            velocidad_viento=velocidad_viento,
            direccion_viento=direccion_viento,
            temperatura=temperatura,
            error=error_en_datos
        )





class Concentrador:
    def __init__(self):
        self.generadores = [Generador(i) for i in range(1, 11)]

    def validar_datos(self, datos: DatosGenerador) -> bool:
        try:
            datos = DatosGenerador(**datos.dict())
            return True
        except Exception as e:
            print(f"Error en la validación de datos: {e}")
            return False

    def obtener_datos_generadores(self) -> list:
        datos_generados = [generador.generar_datos(probabilidad_error=0.1).dict() for generador in self.generadores]
        for datos in datos_generados:
            if datos['error']:
                print(f"Datos con error: {datos}")  # Muestra los datos que dieron error
        return datos_generados

    def agregar_datos(self) -> dict:
        datos_generados = self.obtener_datos_generadores()
        datos_validos = [datos for datos in datos_generados if not datos['error']]
        
        if not datos_validos:
            return {"media_produccion": 0, "total_produccion": 0, "numero_errores": len(self.generadores)}
        
        total_produccion = sum(dato["valor_produccion"] for dato in datos_validos)
        media_produccion = total_produccion / len(datos_validos)
        numero_errores = len(self.generadores) - len(datos_validos)

        return {
            "media_produccion": media_produccion,
            "total_produccion": total_produccion,
            "numero_errores": numero_errores
        }
    
