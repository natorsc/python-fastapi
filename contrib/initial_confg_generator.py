# -*- coding: utf-8 -*-
"""Arquivo é utilizado para automatizar algumas tarefas."""

import datetime
import shutil
import subprocess
from pathlib import Path

CURRENT_DIRECTORY: Path = Path(__file__).resolve().parent
ROOT_DIR: Path = CURRENT_DIRECTORY.parent
EXAMPLE_ENV: Path = CURRENT_DIRECTORY.joinpath('example.env')
ALEMBIC_PATH: Path = ROOT_DIR.joinpath('alembic')

# Creating .env file.
shutil.copy2(EXAMPLE_ENV, ROOT_DIR.joinpath('.env'))


if not ALEMBIC_PATH.exists():
    subprocess.call(
    ['poetry', 'run', 'alembic', 'init', 'alembic'],
    cwd=ROOT_DIR,
)

# Create migration.
subprocess.call(
    ['poetry', 'run', 'alembic', 'revision', '--autogenerate',
    f'-m "{datetime.datetime.now()}"'],
    cwd=ROOT_DIR,
)

# Run migration.
subprocess.call(
    ['poetry', 'run', 'alembic', 'upgrade', 'head'],
    cwd=ROOT_DIR,
)
