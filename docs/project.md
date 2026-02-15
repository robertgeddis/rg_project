# Project Documentation

## Overview

Below is an outline of the foundation for the 'Is Bitcoin Digital Gold' project. It follows best practices for organization, reproducibility, and collaborative work.

## Project Structure

```
rg_project/
├── .git/                       # Git Repository
├── .venv/                      # Virtual Python environment
├── .vscode/                    # VS Code configuration
│   ├── extensions.json         # VS Code extensions
│   └── settings.json           # Workspace-specific settings
├── data/                       # Data directory
│   ├── raw/                    # Raw data
│   ├── clean/                  # Data processed through cleaning measures
│   ├── final/                  # Finalized data ready to be commited to database
│   └── rg_project_database.db  # Database for housing finalized data                  
├── docs/                       # Project documentation
│   └── project.md              # Project description and instructions
├── notebooks/                  # Jupyter Notebooks and Python Scripts
│   ├── nb_setup_v2.py          # Script for establishing SQlite3 connections to database
│   └── sql_import.py           # Script for importing database into Jupyter Notebooks
├── src/                        # Python Source Code
│   └── core/
│       ├── __init__.py         # Make core a package
│       └── data.py             # Data loading functions
├── .gitignore                  # Git Ignore rules
├── .python-version             # Python Version fur uv
├── pyproject.toml              # Project configuration
├── README.md                   # Project description
└── uv.lock                     # Dependencies Lock file
```

## Verzeichnisse und Dateien

### `.vscode/`

Includes VS Code-specific configurations:

- **`extensions.json`**: VS Code extensions for the project (e.g., Python, Jupyter)
- **`settings.json`**: Workspace-specific settings

### `data/`

- **`raw/`**: Ursprüngliche, unveränderte Rohdaten
- **`raw/`**: Ursprüngliche, unveränderte Rohdaten
- **`processed/`**: Bereinigte, transformierte oder aggregierte Daten
- **`processed/`**: Bereinigte, transformierte oder aggregierte Daten

### `notebooks/`

Jupyter Notebooks für explorative Datenanalyse und Experimente.

- **`01_exploration.ipynb`**: Beispiel-Notebook zum Testen des Setups
  - Lädt einen Datensatz von Kaggle
  - Zeigt erste explorative Analysen
  - Dient als Vorlage für weitere Notebooks

**Naming Convention**: Nummerierung mit Präfix (01*, 02*, ...) für chronologische Reihenfolge.

### `src/core/`

Python-Module mit wiederverwendbarem Code, der aus Notebooks ausgelagert wird.

- **`__init__.py`**: Macht `core` zu einem Python-Package
- **`data.py`**: Funktionen zum Laden und Verarbeiten von Daten (z.B. Kaggle Downloads)

**Best Practice**: Code, der in mehreren Notebooks verwendet wird, sollte in Module ausgelagert werden.

### `pyproject.toml`

Zentrale Konfigurationsdatei für das Python-Projekt. Sie definiert Metadaten und Abhängigkeiten.

#### Projekt-Metadaten anpassen

```toml
[project]
name = "dpp-template"                       # Ändern Sie dies auf Ihren Projektnamen
version = "0.1.0"                           # Versionsnummer
description = "Add your description here"   # Kurze Projektbeschreibung
readme = "README.md"                        # Pfad zur README-Datei
requires-python = ">=3.14"                  # Unterstützte Python-Version
```

*Passe diese Felder an dein Projekt an!*

#### Abhängigkeiten

Die `dependencies` Liste enthält alle benötigten Python-Pakete:

```toml
dependencies = [
    "ipykernel>=7.0.1",      # Jupyter Kernel
    "kagglehub>=0.3.13",     # Kaggle Integration
    "matplotlib>=3.10.7",    # Plotting
    "pandas>=2.3.3",         # Datenanalyse
    "seaborn>=0.13.2",       # Visualisierung
    "duckdb>=1.4.1",         # In-Memory Datenbank für Analysen mit SQL
    "scikit-learn>=1.7.2",   # Machine Learning
]
```

> [**ipykernel**](https://ipykernel.readthedocs.io/)  
  Stellt die Verbindung zwischen Jupyter Notebooks und dem Python-Kernel her. Ermöglicht die interaktive Ausführung von Python-Code in Jupyter-Umgebungen.

> [**kagglehub**](https://github.com/Kaggle/kagglehub)  
  Offizielles Python-Package für die Integration mit Kaggle, ermöglicht den einfachen Zugriff auf Kaggle-Datasets und -Modelle. Vereinfacht das Herunterladen und Verwalten von Kaggle-Ressourcen direkt aus Python-Code.

> [**matplotlib**](https://matplotlib.org/stable/index.html)  
  Die grundlegende Plotting-Bibliothek für Python, bietet umfangreiche Möglichkeiten zur Erstellung statischer, animierter und interaktiver Visualisierungen. Dient als Basis für viele andere Visualisierungsbibliotheken.

> [**pandas**](https://pandas.pydata.org/docs/)  
  Die zentrale Bibliothek für Datenanalyse in Python mit leistungsstarken Datenstrukturen wie DataFrame und Series. Bietet intuitive Werkzeuge für Datenmanipulation, -bereinigung und -analyse.

> [**seaborn**](https://seaborn.pydata.org/)  
  High-Level-Visualisierungsbibliothek basierend auf matplotlib, spezialisiert auf statistische Grafiken. Ermöglicht die Erstellung ästhetisch ansprechender und informativer Visualisierungen mit weniger Code.

> [**duckdb**](https://duckdb.org/docs/)  
  Hochperformante In-Memory SQL-Datenbank, optimiert für analytische Workloads (OLAP). Ermöglicht SQL-Abfragen direkt auf DataFrames und CSV-Dateien ohne externe Datenbankserver.

> [**scikit-learn**](https://scikit-learn.org/stable/documentation.html)  
  Die umfassendste Machine-Learning-Bibliothek für Python mit Algorithmen für Klassifikation, Regression, Clustering und mehr. Bietet eine einheitliche API und umfangreiche Tools für Modelltraining, -evaluation und -präprozessierung.

#### Build System

Das Build System ermöglicht es, den `src/core` Code als importierbares Python-Package zu verwenden:

```toml
[build-system]
requires = ["uv_build>=0.8.9,<0.9.0"]
build-backend = "uv_build"

[tool.uv.build-backend]
module-name = "core"
```

Dadurch kannst du in Notebooks `from core.data import ...` verwenden.

### `.gitignore`

Definiert Dateien und Ordner, die nicht ins Git Repository committed werden sollen:

- Virtuelle Umgebungen (`.venv/`)
- Datenverzeichnisse (`data/`)
- Cache-Dateien (`__pycache__/`, `*.pyc`)
- IDE-spezifische Dateien
- Wurde mit [gitignore.io](https://www.toptal.com/developers/gitignore) generiert

### `uv.lock`

Lock-File, das exakte Versionen aller Abhängigkeiten festhält. Gewährleistet Reproduzierbarkeit.
