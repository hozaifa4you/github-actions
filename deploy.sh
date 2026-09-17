#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/home/ubuntu/websites/actions"
export PATH="$HOME/.local/bin:$PATH"

cd "$APP_DIR"

pkill -f "manage.py runserver" || true
sleep 1

nohup uv run manage.py runserver > runserver.log 2>&1 < /dev/null &

echo "Application started up..."
