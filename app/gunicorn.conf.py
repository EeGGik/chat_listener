import os

bind = os.environ.get("APP_HOST", '0.0.0.0:8000')
workers = os.environ.get("WORKERS", default=1)
timeout = int(os.environ.get("TIMEOUT", default=180))
