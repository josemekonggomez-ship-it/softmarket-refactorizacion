# Guía de contribución

## Flujo de trabajo
1. Crear un issue describiendo la tarea.
2. Crear la rama desde `develop`: `feature/<id>-<descripcion>`.
3. Hacer commits pequeños con Conventional Commits.
4. Abrir Pull Request hacia `develop` (usar la plantilla).
5. Esperar CI en verde y mínimo 1 aprobación de otra persona.
6. Fusionar con "Squash and merge" y eliminar la rama de trabajo.

## Convención de commits
`<tipo>(<alcance>): <descripción corta en imperativo>`
Tipos: feat, fix, docs, style, refactor, test, chore.

## Estilo y calidad
- PEP 8 con `black` y `flake8`.
- Pruebas con `pytest`; cobertura mínima 70%.
- Docstrings en clases y funciones públicas.

## Ramas
- Nunca hacer push directo a `main` ni a `develop`.
- `hotfix/*` sale de `main` y se fusiona a `main` y `develop`.
