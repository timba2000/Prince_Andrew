#!/bin/bash
cd /data/.openclaw/workspace
venv_scuba/bin/python get_sdu_progress.py >> sdu_progress.log 2>&1
