# Logo Detector Practice 🎯

Mini proyecto para aprender detección de logos usando YOLO antes del proyecto principal del bootcamp.

## Objetivos
- [ ] Recolectar imágenes de 2-3 logos conocidos
- [ ] Aprender a etiquetar objetos manualmente
- [ ] Entrenar un modelo YOLO desde cero
- [ ] Hacer predicciones en imágenes nuevas
- [ ] Documentar todo el proceso de aprendizaje

## Logos Objetivo
- Apple 🍎
- McDonald's 🍟
- Nike ✅

## Setup del Proyecto

### Instalación
```bash
git clone https://github.com/TU-USUARIO/logo-detector-practice.git
cd logo-detector-practice
python -m venv logo-detector-env
source logo-detector-env/bin/activate  # En Windows: logo-detector-env\Scripts\activate
pip install -r requirements.txt
```

### Estructura del Proyecto
```
logo-detector-practice/
├── data/
│   ├── raw_images/      # Imágenes originales descargadas
│   ├── labeled_images/  # Imágenes etiquetadas
│   ├── train/          # Dataset entrenamiento
│   ├── val/            # Dataset validación
│   └── test/           # Dataset prueba
├── models/             # Modelos entrenados
├── scripts/            # Scripts principales
├── notebooks/          # Experimentación
└── results/            # Resultados y predicciones
```

## Progreso
- [x] ✅ Setup inicial completado
- [ ] 🔄 Recolección de imágenes (Próximo)
- [ ] ⏳ Etiquetado manual
- [ ] ⏳ Entrenamiento del modelo
- [ ] ⏳ Evaluación y predicciones

## Notas de Aprendizaje
_Aquí iré documentando lo que aprendo en cada paso..._
