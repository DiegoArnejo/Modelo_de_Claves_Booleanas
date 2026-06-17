# Motor de Búsqueda Booleana con Índice Invertido

Implementación de un motor de búsqueda básico sobre una pequeña colección de documentos en español.

## ¿Qué hace?

- Preprocesa los documentos eliminando stopwords y normalizando tildes
- Construye un índice invertido para mapear términos a documentos
- Permite búsquedas booleanas con operadores AND, OR y NOT
- Calcula similitud entre documentos usando TF-IDF y similitud del coseno
- Visualiza la matriz de similitud como un heatmap

## Uso

Al ejecutar el programa, primero se genera y muestra el índice invertido y el mapa de calor de similitud. 
Luego se abre un buscador interactivo donde el usuario puede ingresar consultas en lenguaje natural 
combinando términos con operadores booleanos hasta escribir 'salir' para terminar.

## Librerías

- `nltk` — tokenización y stopwords
- `sklearn` — vectorización TF-IDF y similitud del coseno
- `seaborn` / `matplotlib` — visualización
- `unidecode` — normalización de caracteres con tilde
