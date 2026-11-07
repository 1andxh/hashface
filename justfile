peek:
    docker run --rm -v "{{justfile_directory()}}":/app -w /app \
      -e UV_PROJECT_ENVIRONMENT=/opt/venv \
      -v hashface-uv-cache:/root/.cache/uv \
      ghcr.io/astral-sh/uv:python3.12-bookworm-slim \
      uv run --no-dev python scratch.py