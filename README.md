# Levantar el ambiente de citas

1. Crear un ambiente de pruebas con virtual env:
```{bash}
python -m venv venv
```

2. Crear el archivo .env para las variables de entorno
```{bash}
cat .env.dist > .env
```

3. Crear las migraciones necesarioas en la base de datos
```{bash}
python manage.py migrate
```

4. Correr el servicio
```{bash}
python manage.py runserver 0.0.0.0:8000
```

5. Accede a la pagina de las citas en la liga http://localhost:8000 o http://127.0.0.1:8000 para generar la base de datos de pruebas y despues cancelar el proceso con la tecla CTR + C
