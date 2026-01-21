# Bowling Pin Detection & Scoring System

## 📌 Español

Este proyecto consiste en un **sistema de visión computacional** para detectar y contar pinos de boliche a partir de una **imagen tomada desde una perspectiva cenital (vista superior)**, simulando el conteo automático de puntos en una partida de boliche.

El sistema procesa imágenes capturadas desde arriba, detectando los **pinos restantes** mediante el reconocimiento del **color blanco**, eliminando el resto de la imagen y enfocándose únicamente en los objetos relevantes.

A partir de esto:
- Se detectan contornos circulares (cabezas de los pinos)
- Se cuentan los pinos visibles
- Se calcula el puntaje por ronda
- Se genera un marcador para dos jugadores
- Se determina el ganador y el perdedor

### ⚙️ Funcionamiento general
- Carga imágenes de boliche de forma aleatoria
- Convierte la imagen a escala de grises y aplica desenfoque
- Detecta el color blanco mediante umbrales
- Encuentra contornos usando OpenCV
- Cuenta objetos circulares como pinos
- Calcula el puntaje según los pinos derribados
- Simula varias rondas para dos jugadores

### 🛠️ Tecnologías utilizadas
- Python
- OpenCV
- NumPy
- Matplotlib

⚠️ **Nota:** Este proyecto es una **simulación basada en imágenes estáticas**.  
El rendimiento depende de factores como la iluminación y la calidad de la imagen.

---

## 📌 English

This project implements a **computer vision system** to detect and count bowling pins using a **top-down (zenith) image perspective**, simulating an automatic scoring system for a bowling game.

The system processes images captured from above, detecting **remaining pins** by identifying the **white color**, removing irrelevant information, and focusing only on the objects of interest.

Based on this process:
- Circular contours (pin heads) are detected
- Visible pins are counted
- Scores are calculated per round
- A scoreboard for two players is generated
- The winner and loser are determined

### ⚙️ General Workflow
- Randomly loads bowling images
- Converts images to grayscale and applies blur
- Detects white regions using thresholding
- Finds contours using OpenCV
- Counts circular objects as pins
- Calculates scores based on knocked-down pins
- Simulates multiple rounds for two players

### 🛠️ Technologies Used
- Python
- OpenCV
- NumPy
- Matplotlib

⚠️ **Note:** This project is a **simulation based on static images**.  
Performance depends on factors such as lighting conditions and image quality.
