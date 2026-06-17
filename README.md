# Motor de Búsqueda Booleana con Índice Invertido

Implementación de un motor de búsqueda básico sobre una pequeña colección de documentos en español.

## ¿Qué hace?

- Preprocesa los documentos eliminando stopwords y puntuación
- Construye un índice invertido para mapear términos a documentos
- Permite búsquedas booleanas con operadores AND, OR y NOT

## Uso

Al ejecutar el programa, primero se genera y muestra el índice invertido.
Luego se abre un buscador interactivo donde el usuario puede ingresar consultas
combinando términos con operadores booleanos. Escribir `salir` para terminar.

### Formatos de consulta válidos

| Formato | Descripción |
|---|---|
| `palabra` | Búsqueda simple |
| `palabra AND palabra` | Documentos que contienen ambos términos |
| `palabra OR palabra` | Documentos que contienen al menos uno |
| `palabra NOT palabra` | Documentos con el primero pero no el segundo |

## Librerías

| Librería | Uso |
|---|---|
| `nltk` | Tokenización y stopwords |
| `string` / `collections` | Utilidades estándar de Python |

## Ejemplo

```
--- INDICE INVERTIDO
