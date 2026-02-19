# 📘 Flex & Bison — Analizador Léxico y Sintáctico

Proyecto académico de la asignatura **Lenguajes de Programación** enfocado en la implementación de:

- 🧠 Análisis léxico con Flex  
- 🧩 Análisis sintáctico con Bison  
- ⚡ Comparación entre implementación manual y generada  

---

# 📌 1️⃣ Contador de Palabras

Implementado en dos versiones:

- 🔹 Flex  
- 🔹 C puro  

Cuenta:

- Líneas  
- Palabras  
- Caracteres  

---

## 🔧 Versión con Flex

### Compilación

```bash
flex fb1-1.l
gcc lex.yy.c -o wc_flex -lfl
```

### Ejecución

```bash
./wc_flex < archivo.txt
```

---

## 🔧 Versión en C

### Compilación

```bash
gcc wc_c.c -o wc_c
```

### Ejecución

```bash
./wc_c < archivo.txt
```

---

# 📌 2️⃣ Calculadora con Flex + Bison

### Soporta:

### 🧮 Operaciones Aritméticas
- Suma (`+`)
- Resta (`-`)
- Multiplicación (`*`)
- División (`/`)
- Valor absoluto (`|x|`)
- Números hexadecimales (`0x...`)

### 🔗 Operadores Lógicos
- AND
- OR

### 💬 Otros
- Comentarios (`//`)

---

## 🔧 Compilación

```bash
bison -d fb1-5.y
flex fb1-5.l
gcc fb1-5.tab.c lex.yy.c -o calc -lfl
```

## ▶️ Ejecución

```bash
./calc
```

### Ejemplo de uso

```
2 + 4
= 6

0xA + 5
= 15

1 AND 0
= 0

1 OR 0
= 1
```

---

---

# 📚 Respuestas Teóricas

## 4️⃣ ¿La versión escrita a mano del scanner reconoce exactamente los mismos tokens que la versión con Flex?

No necesariamente.

Aunque ambas implementaciones pueden diseñarse para reconocer los mismos patrones léxicos, la versión generada con **Flex** se basa en expresiones regulares que se transforman automáticamente en un autómata finito determinista (AFD). Esto garantiza que las reglas se apliquen de forma estricta y consistente según su definición.

En cambio, la versión escrita manualmente en C depende completamente de la lógica implementada por el programador. Esto puede generar:

- Diferencias sutiles en el reconocimiento de tokens  
- Problemas en casos límite  
- Errores relacionados con espacios, saltos de línea o caracteres especiales  

Por lo tanto, aunque pueden comportarse de forma similar en la mayoría de los casos, no hay garantía absoluta de que reconozcan exactamente los mismos tokens si no están cuidadosamente implementadas.

---

## 5️⃣ ¿Existen lenguajes para los cuales Flex no sea una buena herramienta para escribir un scanner?

Sí.

Flex funciona muy bien para lenguajes donde el análisis léxico puede describirse mediante expresiones regulares y donde el contexto no influye significativamente en el reconocimiento de tokens.

Sin embargo, no es la mejor opción en casos como:

- Lenguajes con indentación significativa (por ejemplo, Python)
- Lenguajes donde el significado de un token depende fuertemente del contexto
- Lenguajes con reglas léxicas altamente dependientes de información semántica
- Sintaxis donde el análisis no puede resolverse únicamente con expresiones regulares

En estos casos, puede ser necesario un análisis más complejo o herramientas que integren mejor el contexto dentro del proceso de reconocimiento.

---


# 📊 Análisis de Rendimiento

Pruebas realizadas con:

```bash
time ./wc_flex < grande.txt
time ./wc_c < grande.txt
```

### Resultado

La versión en **C puro** presentó mejor rendimiento que la versión generada con Flex.

<img width="808" height="830" alt="Captura desde 2026-02-18 22-40-03" src="https://github.com/user-attachments/assets/e9c2c3ff-f9e5-42dc-87cd-36ed048ec0ef" />


## 📈 Comparación

La implementación en **C puro** fue aproximadamente:

- 🔥 ~52 segundos más rápida
- 📊 Cerca de un **35% más eficiente en tiempo de ejecución**

---

## 🧩 Interpretación Técnica

La diferencia de rendimiento se debe a que:

- La versión en C utiliza lógica directa y control manual del estado.
- Flex genera una máquina de estados automática más general.
- El código generado por Flex incluye capas adicionales de abstracción.
- Existe overhead asociado al motor del lexer generado.

---


# 🛠️ Requisitos

Instalar previamente:

- flex
- bison
- gcc

En sistemas basados en Debian/Ubuntu:

```bash
sudo apt install flex bison build-essential
```

---



