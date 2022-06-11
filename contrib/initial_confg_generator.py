# -*- coding: utf-8 -*-
"""Arquivo é utilizado para automatizar algumas tarefas."""

import shutil
from pathlib import Path

CURRENT_DIRECTORY: Path = Path(__file__).resolve().parent
ROOT_DIR: Path = CURRENT_DIRECTORY.parent
EXAMPLE_ENV: Path = CURRENT_DIRECTORY.joinpath('example.env')

# Creating .env file.
shutil.copy2(EXAMPLE_ENV, ROOT_DIR.joinpath('.env'))
