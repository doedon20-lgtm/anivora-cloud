#!/bin/bash

set -e

echo "======================================"
echo "       🎬 AniVora Cloud Notebook"
echo "======================================"

echo ""
echo "Python:"
python --version

echo ""
echo "Checking PyTorch..."

python - <<'PY'
try:
    import torch

    print("PyTorch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

        memory = (
            torch.cuda.get_device_properties(0).total_memory
            / (1024 ** 3)
        )

        print(f"VRAM: {memory:.2f} GB")
    else:
        print("GPU: Not detected")

except Exception as e:
    print("PyTorch check:", e)
PY

echo ""
echo "Starting JupyterLab..."
echo ""

jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root
