#!/usr/bin/env bash
# Uso: ./subir_a_github.sh https://github.com/TU_USUARIO/softmarket-refactorizacion.git
# 1) Crea primero un repositorio VACÍO en GitHub (sin README) con ese nombre.
# 2) Descomprime el .zip, entra a la carpeta y ejecuta este script dentro de ella.
set -e
[ -z "$1" ] && { echo "Falta la URL del repositorio"; exit 1; }
git remote remove origin 2>/dev/null || true
git remote add origin "$1"
git push -u origin --all
git push origin --tags
echo "Listo: ramas y etiquetas subidas."
