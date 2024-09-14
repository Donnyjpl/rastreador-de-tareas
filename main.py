import json
from datetime import datetime

# Ruta al archivo JSON donde se almacenan las tareas
FILE_PATH = 'tareas.json'

# Función para leer las tareas del archivo JSON
def leer_tareas():
    try:
        with open(FILE_PATH, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para escribir las tareas en el archivo JSON
def escribir_tareas(tareas):
    with open(FILE_PATH, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

# Función para agregar una nueva tarea
def agregar_tarea(description):
    tareas = leer_tareas()
    nuevo_id = len(tareas) + 1
    fecha_actual = datetime.now().isoformat()  # Formato ISO 8601
    
    nueva_tarea = {
        "id": nuevo_id,
        "description": description,
        "status": "todo",  # El estado inicial es "todo"
        "createdAt": fecha_actual,
        "updatedAt": fecha_actual
    }

    tareas.append(nueva_tarea)
    escribir_tareas(tareas)
    print(f"Tarea '{description}' agregada con éxito.")

# Función para actualizar una tarea existente
def actualizar_tarea(tarea_id, description=None, status=None):
    tareas = leer_tareas()
    tarea_encontrada = False

    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea_encontrada = True
            if description:
                tarea['description'] = description
            if status:
                tarea['status'] = status
            tarea['updatedAt'] = datetime.now().isoformat()  # Actualiza el campo 'updatedAt'
            break

    if tarea_encontrada:
        escribir_tareas(tareas)
        print(f"Tarea con ID {tarea_id} actualizada con éxito.")
    else:
        print(f"Tarea con ID {tarea_id} no encontrada.")

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar una nueva tarea
    agregar_tarea("Terminar el proyecto de Django")
    
    # Actualizar una tarea existente
    actualizar_tarea(2, description="Comprar comida para el mes ", status="done")