import string
import numpy as np
import seaborn as sns
import re
import matplotlib.pyplot as plt
from unidecode import unidecode
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Stopwords en Español
spanish_stopwords = set(stopwords.words('spanish'))
excepciones = {"inteligencia", "artificial", "aprendizaje", "automático"} 

# Limpieza y Tokenizacion
def preprocesar_texto(texto):
    tokens = word_tokenize(texto.lower())
    
    tokens_limpios = [
        unidecode(w) for w in tokens 
        if (w not in spanish_stopwords or w in excepciones)
        and w not in string.punctuation 
    ]
    return tokens_limpios

documents = [
    "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "La civilización romana fue una de las mas influyentes en la historia occidental.",
    "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
]

# Indice Invertido

inverted_index = defaultdict(list)
procesados_para_tfidf = []

for idx, text in enumerate(documents):
    doc_label = f"Doc{idx+1}"
    
    # Llamado a la funcion de limpieza
    tokens_limpios = preprocesar_texto(text)
    
    # Join del texto limpio para que lo use el TF-IDF
    procesados_para_tfidf.append(" ".join(tokens_limpios))
    
    # Se guarda el indice invertido
    for token in set(tokens_limpios):
        inverted_index[token].append(doc_label)

# Imprimir el indice invertido 
print("--- INDICE INVERTIDO GENERADO ---")
for word, doc_list in sorted(inverted_index.items()):
    print(f"'{word}': {doc_list}")
print("-" * 40)

# Convertir documentos a vectores usando TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(procesados_para_tfidf)

# Calcular la similitud del coseno entre los documentos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Graficar la matriz de similitud
plt.figure(figsize=(8,6))
sns.heatmap(cosine_sim, annot=True, cmap="Blues", 
            xticklabels=[f"Doc{i+1}" for i in range(len(documents))], 
            yticklabels=[f"Doc{i+1}" for i in range(len(documents))])
plt.title("Matriz de Similitud del Coseno")
plt.show()

# Programa de consulta

print("\n=== BUSQUEDA BOOLEANA ===")
print("Escribi 'salir' para terminar")

while True:
    consulta = unidecode(input("Ingresa tu busqueda: ").strip().lower())

    if consulta == 'salir':
        print("Saliendo...")
        break

    partes = consulta.split()

    if len(partes) == 1:
        resultado = set(inverted_index.get(partes[0], []))

    # Consulta con operador: palabra AND/OR/NOT palabra
    elif len(partes) == 3:
        t1, operador, t2 = partes
        docs1 = set(inverted_index.get(t1, []))
        docs2 = set(inverted_index.get(t2, []))
        todos = set(f"Doc{i+1}" for i in range(len(documents)))

        if operador == 'and':
            resultado = docs1 & docs2
        elif operador == 'or':
            resultado = docs1 | docs2
        elif operador == 'not':
            resultado = docs1 - docs2
        else:
            print("  Operador no reconocido. Usa: and, or, not")
            continue
    else:
        print("  Formato valido: 'palabra' o 'palabra and/or/not palabra'")
        continue

    if resultado:
        print(f"  Documentos: {sorted(resultado)}")
    else:
        print("  Ningun documento encontrado.")