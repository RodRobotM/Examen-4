# 🎬 FICHA 4 - Sistema de Gestión de Películas

## Información General

| Campo | Contenido |
|-------|-----------|
| **Sigla** | FPY1101 |
| **Asignatura** | Fundamentos de Programación |
| **Experiencia de Aprendizaje** | EA3: Colecciones y funciones en Python |
| **Tiempo** | 2 horas |
| **Modalidad** | Individual |
| **Indicadores de Logro** | IL 3.1 al IL 4.2 |

---

## 📝 Descripción General

Desarrolla un programa en Python que implemente un **sistema de gestión de películas de un cine**, donde todo el comportamiento se organice mediante funciones bien definidas.

El programa debe incluir:
- ✅ Menú interactivo
- ✅ Validaciones de entrada
- ✅ Operaciones lógicas (decisiones y comparaciones)
- ✅ Uso de funciones separadas

---

## 1️⃣ Datos que debe manejar el sistema

### Estructura de la colección

El sistema trabaja con una **colección de películas** que:
- Debe existir desde que el programa inicia
- Está disponible durante toda la ejecución
- Se incorporan nuevas películas a medida que se agregan

Cada película se representa como un **diccionario** con los siguientes campos:

| Campo | Descripción | Restricciones de Validación |
|-------|-------------|----------------------------|
| `"titulo"` | Título de la película | No vacío ni solo espacios en blanco |
| `"duracion"` | Duración en minutos | Número entero mayor que cero |
| `"calificacion"` | Calificación (0.0–10.0) | Número decimal entre 0.0 y 10.0 (incluidos) |
| `"disponible"` | ¿Recomendada para exhibición? | Inicialmente `False`. Se actualiza automáticamente según calificación |

### Almacenamiento de datos

- Cada **diccionario** representa una película individual
- Los diccionarios se guardan dentro de una **lista**
- La lista es la colección general que se va llenando a medida que se agregan registros
- El programa comienza con la lista vacía

---

## 2️⃣ Lo que debe hacer el sistema

### Funcionamiento general

El sistema se controla desde un **menú interactivo** que:
1. Aparece en pantalla cada vez que el usuario termina una acción
2. El usuario elige una opción numérica
3. El programa ejecuta la tarea correspondiente
4. Vuelve a mostrar el menú
5. Este ciclo se repite hasta que el usuario elige salir

### Menú Principal

```
========== MENÚ PRINCIPAL ==========
1. Agregar película
2. Buscar película
3. Eliminar película
4. Actualizar disponibilidad
5. Mostrar películas
6. Salir
=====================================
```

### Implementación del menú

Debes definir **dos funciones separadas**:
1. **Función de visualización**: Muestra las opciones en pantalla (sin parámetros, sin retorno)
2. **Función de lectura**: Lee y retorna la opción elegida (sin parámetros, retorna número validado)

Ambas funciones deben invocarse en **cada vuelta del ciclo**.

---

## 📋 Opciones del Sistema

### Opción 1️⃣ - Agregar película

#### Proceso:
1. El sistema solicita al usuario: **título**, **duración** y **calificación**
2. Antes de guardar, verifica que cada dato cumpla sus restricciones:
   - ✓ El título no puede estar vacío ni ser solo espacios en blanco
   - ✓ La duración debe ser un número entero mayor que cero
   - ✓ La calificación debe ser un número decimal entre 0.0 y 10.0

#### Comportamiento:
- **Si hay error**: El sistema informa al usuario y **no registra** la película
- **Si es válido**: Se crea el diccionario y se agrega a la lista

#### Implementación:
Debes definir una función que:
- Reciba la lista como parámetro
- Solicite los datos al usuario
- Llame a una **función de validación distinta para cada campo**
- Muestre los mensajes de error en esta función (no dentro de las validaciones)

---

### Opción 2️⃣ - Buscar película

#### Proceso:
1. El sistema solicita un título de película al usuario
2. Recorre la lista buscando un registro con ese título exacto
3. Si lo encuentra, muestra la **posición** y sus **datos**
4. Si no existe, informa al usuario

#### Implementación:
Debes definir una función que:
- Reciba dos parámetros: **lista** y **título a buscar**
- Recorra la lista
- Retorne la **posición del registro encontrado**, o **-1 si no existe**
- El programa principal decide qué hacer con el valor retornado

---

### Opción 3️⃣ - Eliminar película

#### Proceso:
1. El sistema solicita el título de la película a eliminar
2. Llama a la función de búsqueda (Opción 2)
3. Si existe la película, la elimina
4. Si no existe, muestra el mensaje: `La película 'titulo' no se encuentra registrada.`

---

### Opción 4️⃣ - Actualizar disponibilidad

#### Regla:
Para cada película en la lista:
- **Si calificación ≥ 7.0**: `disponible = True`
- **Si calificación < 7.0**: `disponible = False`

#### Proceso:
Esta operación afecta a **todos los registros** de la lista sin excepción.

#### Implementación:
Debes definir una función que:
- Reciba la lista como parámetro
- Aplique la regla a cada elemento

---

### Opción 5️⃣ - Mostrar películas

#### Proceso:
1. Primero actualiza la disponibilidad de todas las películas (llamando a la función anterior)
2. Recorre la lista mostrando los datos de cada película

#### Formato de salida:
```
=== LISTA DE PELICULAS ===

Título: Oppenheimer
Duración: 180
Calificación: 8.5
Estado: DISPONIBLE
*******************************************
Título: Morbius
Duración: 104
Calificación: 5.2
Estado: NO RECOMENDADA
*******************************************
```

---

### Opción 6️⃣ - Salir

#### Proceso:
El sistema termina la ejecución de forma limpia, sin errores.

#### Mensaje de despedida:
```
Gracias por usar el sistema. Vuelva Pronto
```

---

## 💡 Notas Importantes

- Utiliza estructuras de control adecuadas (bucles, condicionales)
- Implementa validaciones robustas para entrada de datos
- Organiza tu código en funciones reutilizables
- Mantén la lista disponible durante toda la ejecución del programa
- Sigue convenciones de nombres y espaciado en Python
