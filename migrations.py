# -*- coding: utf-8 -*-
# migrations.py

import subprocess

def apply_migrations():
    subprocess.run(["alembic", "upgrade", "head"], check=True)
