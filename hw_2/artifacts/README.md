# Важное

Перед запуском, необходимо скопировать Dockerfile и docker-compose.yaml файлы в папку hw_2

# Задание 2.1

Смотреть файлик `2.1.py`

Артефакт - `hw_2/artifacts/example_2.1.tex`

## Запуск

```bash
python 2.1.py --output <filename>
```

# Задание 2.2

Смотреть файлик `2.2.py`

Артефакт - `hw_2/artifacts/example_2.2.tex` и `hw_2/artifacts/example_2.2.pdf`

Ссылка на пакет на PyPi - https://pypi.org/project/latex-generator-hbashift/ 

Так же артефактами являются папки build, dist и latex_generator_hbashift.egg-info

## Запуск

```bash
python .\2.2.py <path_to_image> --output <filename>
```

Сборка производилась с помощью setuptools и пакет был запушен в PyPi репозиторий

# Задание 2.3

Артефакты - `hw_2/artifacts/Dockerfile` и `hw_2/artifacts/docker-compose.yaml`

Для запуска в консоли нужно:
```bash
cd hw_2 #перейти в директорию hw_2
docker compose up
```

После, сгенерированные pdf и tex файлы будут в папке `hw_2/output`