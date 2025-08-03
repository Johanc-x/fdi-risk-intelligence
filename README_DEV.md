# 🧠 Developer Quick Reference – Jhojan's Data Ops

Este archivo contiene comandos clave para trabajar en este proyecto de forma ordenada y profesional.

---

## 🔁 Activar entorno virtual (cada vez que abras VS Code o una nueva terminal)

```powershell
.\venv\Scripts\Activate

```

## Instalar librerías necesarias. 

pip install pandas numpy matplotlib cx_Oracle

## Librerias instaladas

pip freeze > requirements.txt

## Iniciar Git 

git init

## Añadir y guardar cambios en Git

git add .
git commit -m "mensaje claro del cambio realizado"

## Ver el estado actual del proyecto

git status

## Omitir archivos sensibles o innecesarios (Usar .gitignore)

venv/
__pycache__/
*.csv
.env

## Subir los proyectos a GitHub una vez enlazados

git remote add origin https://github.com/tuusuario/tu-repo.git
git branch -M main
git push -u origin main

# Ejecutar desde la terminal de VSCODE. Asegúrate de estar ubicado en la raíz del proyecto
python Scripts/exploracion_fdi.py

