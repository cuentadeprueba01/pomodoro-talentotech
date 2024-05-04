# Proyecto (POMODORO)

Crearemos una aplicación pomodoro funcional en python. Mientras aplicamos conceptos de control de versiones y buenas practicas.

## Empezar proyecto

Comando para crear el entorno virtual

```shell
python -m venv venv
```

Inicializar repositorio local

```shell
git init
```

Añadir cambios

```shell
git add .
```

Crear un commit

```shell
git commit -m "my commit"
```

Cambiar de rama

```shell
git branch -M main
```

Agregar un repositorio remoto

```shell
git remote add origin main "https://github.com/username/repo.git"
```

Publicar cambios

```shell
git push origin main
```

## Lista de tareas

[x] Crear la estructura basica del proyecto

- [x] Creación del entorno virtual de python
- [x] Inicialización del repositorio local

[x] Constantes inciales

```python
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
```

[x] Importar la libreria

- [x] [Documentación de la libreria tkinder](https://docs.python.org/es/3/library/tk.html)

[ ] Especificar funciones y su logica

- [ ] funcion de inicion (start)
- [ ] funcion de reinicio (restart)
