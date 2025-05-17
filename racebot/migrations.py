# -*- coding: utf-8 -*-
# migrations.py

import subprocess

def apply_migrations():
    subprocess.run([sys.executable, "-m", "alembic", "upgrade", "head"], check=True)
