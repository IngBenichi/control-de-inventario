# Control de Inventario

Este programa permite gestionar un inventario de productos, incluyendo funcionalidades para agregar, buscar, modificar y eliminar productos.

## Requisitos

- Python 3.x
- Flet (instalable con `pip install flet`)

## Archivos

- `inventario.json`: Archivo donde se almacenan los datos del inventario.

## Funciones Principales

### 1. `cargar_datos()`

Carga los datos del inventario desde `inventario.json`.

```python
def cargar_datos():
    if os.path.exists('inventario.json'):
        with open('inventario.json', 'r') as file:
            return json.load(file)
    return {"Vnombre": [], "Vcodigo_barras": [], "Vprecio": [], "Vcantidad_stock": []}
```

### 2. `guardar_datos(datos)`

Guarda los datos del inventario en `inventario.json`.

```python
def guardar_datos(datos):
    with open('inventario.json', 'w') as file:
        json.dump(datos, file, indent=4)
```

### 3. `main(page: ft.Page)`

Función principal que configura la interfaz gráfica usando Flet.

```python
def main(page: ft.Page):
    # Configuración de la página
    # Campos de entrada y botones para gestionar productos
    # Funciones para agregar, buscar, modificar, eliminar productos
```

## Funciones de Gestión de Productos

- **Agregar Producto:** Permite añadir un nuevo producto al inventario.
- **Buscar Producto:** Busca un producto por nombre o código de barras.
- **Modificar Producto:** Modifica los detalles de un producto existente.
- **Eliminar Productos:** Elimina productos con stock igual a cero.

### Ejemplo de Uso

```python
# Cargar los datos al iniciar el programa
datos = cargar_datos()
Vnombre = datos["Vnombre"]
Vcodigo_barras = datos["Vcodigo_barras"]
Vprecio = datos["Vprecio"]
Vcantidad_stock = datos["Vcantidad_stock"]

# Ejecutar la aplicación
ft.app(target=main)
```

## Interacción en Consola

Además de la interfaz gráfica, el programa ofrece un menú en consola para interactuar con el inventario.

### Opciones Disponibles

1. Agregar Producto
2. Buscar Producto
3. Modificar Producto
4. Eliminar Productos
5. Salir

## Conclusión

Este programa es una solución básica para el control de inventario, permitiendo gestionar productos de manera efectiva. Se pueden añadir más funcionalidades y mejoras en el futuro.
