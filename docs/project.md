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
│   ├── etl_scripts/            # Scripts for extracting, cleaning and finalizing data 
│   ├── raw/                    # Raw data
│   ├── clean/                  # Data processed through cleaning measures
│   ├── final/                  # Finalized data ready to be commited to database
│   └── rg_project_database.db  # Database for housing finalized data                  
├── docs/                       # Project documentation
│   └── project.md              # Project description and instructions
├── notebooks/                  # Jupyter Notebooks and Python Scripts
│   ├── nb_setup_v2.py          # Establishing SQlite3 connection to database
│   └── sql_import.py           # Importing database into Jupyter Notebooks
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

- **`etl_scripts/`**: Jupyter Notebooks for creating raw, clean and final versions of data 
- **`raw/`**: Original unprocessed version of data 
- **`clean/`**: Data quality checking and cleaning up NaN values 
- **`final/`**: Transforming data using Base-100 normalization and adding new % change columns 
- **`rg_project_database.db/`**: Warehouse of finalized data for analysis

### `notebooks/`

Jupyter Notebooks for exploratory data analysis and experiments.

- **`nb_setup_v2.py`**: Script for establishing a connection to rg_project_database.db
- **`sql_import.py`**: Script to running rg_project_database.db within Jupyter Notebooks

### `src/core/`

Python modules with reusable code that are outsourced from notebooks.

- **`__init__.py`**: Make `core` a Python package

### `pyproject.toml`

Central configuration file for the Python project. It defines metadata and dependencies.

```pyproject.toml
[project]
name = "dpp-template"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "ipykernel>=7.0.1",
    "kagglehub>=0.3.13",
    "matplotlib>=3.10.7",
    "pandas>=2.3.3",
    "seaborn>=0.13.2",
    "duckdb>=1.4.1",
    "scikit-learn>=1.7.2",
    "ipywidgets>=8.1.8",
]

[build-system]
requires = ["uv_build>=0.8.9,<0.9.0"]
build-backend = "uv_build"

[tool.uv.build-backend]
module-name = "core"
```

#### Build System

The build system allows the `src/core` code to be used as an importable Python package:

```toml
[build-system]
requires = ["uv_build>=0.8.9,<0.9.0"]
build-backend = "uv_build"

[tool.uv.build-backend]
module-name = "core"
```

### `.gitignore`

Defines files and folders that should not be committed to the Git repository:

- Virtual environments (`.venv/`)
- Data directories (`data/`)
- Cache files (`__pycache__/`, `*.pyc`)
- IDE-specific files
- Was with [gitignore.io](https://www.toptal.com/developers/gitignore) generated

### `uv.lock`

A lock file that stores the exact versions of all dependencies. Ensures reproducibility.
