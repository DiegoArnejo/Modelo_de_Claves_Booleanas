# Motor de Búsqueda Booleana con Índice Invertido

Implementación de un motor de búsqueda básico sobre una pequeña colección de documentos en español.

## ¿Qué hace?

- Preprocesa los documentos eliminando stopwords y normalizando tildes
- Construye un índice invertido para mapear términos a documentos
- Permite búsquedas booleanas con operadores AND, OR y NOT
- Calcula similitud entre documentos usando TF-IDF y similitud del coseno
- Visualiza la matriz de similitud como un heatmap

## Uso

El programa solicita una consulta en formato:
- `escritura` — busca documentos que contengan esa palabra
- `egipcios and piramides` — documentos que contengan ambos términos
- `escritura or democracia` — documentos que contengan alguno de los dos
- `escritura not cuneiforme` — documentos con el primero pero no el segundo
- `salir` — termina el programa

## Librerías

- `nltk` — tokenización y stopwords
- `sklearn` — vectorización TF-IDF y similitud del coseno
- `seaborn` / `matplotlib` — visualización
- `unidecode` — normalización de caracteres con tilde
