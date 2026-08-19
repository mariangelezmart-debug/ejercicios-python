def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for caracter in texto:
        if caracter in vocales:
            contador += 1
            
    return contador

# Prueba del programa
frase = "Programacion en Python"
resultado = contar_vocales(frase)
print(f"La frase '{frase}' tiene {resultado} vocales.")


# ==========================================
# EJERCICIO 2: Gestor de Inventario
# ==========================================

inventario = {}

def agregar_producto(nombre, precio, cantidad):
    nombre = nombre.lower()
    if nombre in inventario:
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}

def calcular_valor_total():
    return sum(datos['precio'] * datos['cantidad'] for datos in inventario.values())

def mostrar_inventario():
    print("\n--- INVENTARIO ACTUAL ---")
    for producto, datos in inventario.items():
        print(f"- {producto.capitalize()}: ${datos['precio']} | Stock: {datos['cantidad']}")
    print(f"Valor total en stock: ${calcular_valor_total():.2f}\n")

# Prueba
agregar_producto("Laptop", 750.00, 3)
agregar_producto("Teclado", 25.50, 10)
mostrar_inventario()


# ==========================================
# EJERCICIO 3: Gestión de Tareas con POO
# ==========================================

class TareaNoEncontradaError(Exception):
    pass

class Tarea:
    def __init__(self, id_tarea, titulo):
        self.id = id_tarea
        self.titulo = titulo
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✓ Completada" if self.completada else "✗ Pendiente"
        return f"[{self.id}] {self.titulo} - {estado}"

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self._contador_id = 1

    def agregar_tarea(self, titulo):
        nueva_tarea = Tarea(self._contador_id, titulo)
        self.tareas.append(nueva_tarea)
        self._contador_id += 1

    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.marcar_completada()
                return
        raise TareaNoEncontradaError(f"No existe la tarea con ID {id_tarea}.")

    def listar_pendientes(self):
        print("\n--- TAREAS PENDIENTES ---")
        for tarea in self.tareas:
            if not tarea.completada:
                print(tarea)

# Prueba
gestor = GestorTareas()
gestor.agregar_tarea("Estudiar algoritmos")
gestor.agregar_tarea("Subir proyecto a GitHub")
gestor.completar_tarea(1)
gestor.listar_pendientes()
