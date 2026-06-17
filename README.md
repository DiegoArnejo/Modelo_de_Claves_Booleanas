Motor de Búsqueda Booleana con Índice Invertido
Implementación de un motor de búsqueda básico sobre una colección de documentos en español.
¿Qué hace?

Preprocesa los documentos eliminando stopwords y puntuación
Construye un índice invertido para mapear términos a documentos
Permite búsquedas booleanas con operadores AND, OR y NOT

Uso
Al ejecutar el programa, primero se genera y muestra el índice invertido. Luego se abre un buscador interactivo donde el usuario puede ingresar consultas combinando términos con operadores booleanos. Escribir salir para terminar.
Formatos de consulta válidos:

palabra — búsqueda simple
palabra AND palabra — documentos que contienen ambos términos
palabra OR palabra — documentos que contienen al menos uno
palabra NOT palabra — documentos con el primero pero no el segundo

Librerías

nltk — tokenización y stopwords
string / collections — utilidades estándar de Python
