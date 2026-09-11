import subprocess
import sys


packages = [
    "fastapi",
    "uvicorn[standard]",
    "python-multipart",
    "psutil",
]


print("Installing AniVora Cloud dependencies...")

subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    *packages
])

print()
print("✅ AniVora Cloud dependencies installed.")
