import platform
import os

print("=" * 50)
print("AniVora GPU Worker")
print("=" * 50)

print(f"Operating system: {platform.system()}")
print(f"Python: {platform.python_version()}")
print(f"CPU threads: {os.cpu_count()}")

try:
    import torch

    print(f"PyTorch: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():

        print(f"GPU count: {torch.cuda.device_count()}")

        for i in range(torch.cuda.device_count()):

            name = torch.cuda.get_device_name(i)

            memory = (
                torch.cuda.get_device_properties(i).total_memory
                / (1024 ** 3)
            )

            print(f"GPU {i}: {name}")
            print(f"VRAM: {memory:.2f} GB")

    else:
        print("No CUDA GPU detected.")

except ImportError:
    print("PyTorch is not installed.")

print("=" * 50)
