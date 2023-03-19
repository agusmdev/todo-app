# todoapp-backend

## This is an Example of the FastAPI-ddd-template

The steps that generated this repository were the following:

1) Run `cookiecutter https://github.com/agusmdev/fastapi-ddd-template.git`
2) Set the following values:
```text
project_name [FastAPI DDD project]: TodoApp
project_slug [todoapp]: todo-app
project_description [FastAPI Domain Driven Design (DDD) template]: Example on how to use fastapi-ddd-template
author [Agustín Marchi <agusmdev@gmail.com>]: Agustín Marchi <agusmdev@gmail.com>
first_entity [your_first_entity]: task
```
3) Modified the `Task` model with the correspondant fields (also the `update_task` test)
4) Done! You have a ToDo App with repository pattern in just 30 seconds!


## 🎯 Summary

- Setup and dependencies managed with [Poetry](https://python-poetry.org/) and [virtualenv](https://virtualenv.pypa.io/en/latest/)
- Architecture based on [Repository pattern](https://www.cosmicpython.com/book/chapter_02_repository.html), with dependency injection using [Dependency Injector](https://python-dependency-injector.ets-labs.org/)
- Repository management through [Redbird](https://github.com/Miksus/red-bird)
- App with endpoints served through [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
- Testing managed with [pytest](https://docs.pytest.org/) (+ plugins)
- Code style driven with [black](https://github.com/psf/black) + [ruff](https://beta.ruff.rs/docs/) 

## 🧬 Project structure

```text
.
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── apis
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── containers.py
│   │   ├── repositories.py
│   │   ├── routers.py
│   │   └── task
│   │       ├── __init__.py
│   │       ├── container.py
│   │       ├── models.py
│   │       ├── routers.py
│   │       ├── schemas.py
│   │       └── service.py
│   ├── core
│   │   ├── __init__.py
│   │   └── model_factory.py
│   └── main.py
├── pyproject.toml
├── scripts
│   ├── clean.sh
│   ├── install.sh
│   ├── lint.sh
│   ├── run_app.sh
│   ├── setup_dev.sh
│   ├── test.sh
│   └── venv.sh
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        ├── conftest.py
        ├── endpoints
        │   └── test_task.py
        └── test_repositories.py
```

## 🍴 Setup

### Local 

To install the project locally, run the following scripts:


```bash
# Install the repository with its dependencies
$ ./scripts/install.sh
# Activate the environment
$ source scripts/venv.sh
```

## ⚙️ Usage

### Local

To run the service locally, execute the following script:


```shell
./scripts/run_app.sh
```

This command will start the service on port 8000.


## 🔧 Scripts

This is the list of commands implemented to facilitate the development of this project:

```text
clean.sh                 Remove temporary files
install.sh               Install the repository in the current directory
lint.sh                  Run linting on the source code
run_app.sh               Run the app
setup_dev.sh             Set up for local development
tests.sh                 Run a specific test suite
venv.sh                  Activate the environment created with virtualenv
```

## 🔍 Tests

To run the project tests, execute the following command:

```bash
# run unit tests
$ ./scripts/tests.sh unit

# run system tests
$ ./scripts/tests.sh system
```

By default, all unit tests defined in the project will be run.


## 🤝 Contributions

If you would like to contribute to the project, open a pull request on GitHub. We welcome all contributions!
