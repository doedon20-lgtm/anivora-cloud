from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import platform
import psutil
import os

app = FastAPI(title="AniVora Cloud", version="0.1.0")

BASE_DIR = Path(__file__).resolve().parent.parent


def gpu_status():
    try:
        import torch

        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            memory_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)

            return {
                "available": True,
                "name": gpu_name,
                "memory_gb": round(memory_gb, 2),
                "cuda": torch.version.cuda,
                "pytorch": torch.__version__,
            }

        return {
            "available": False,
            "name": "No CUDA GPU detected",
            "memory_gb": 0,
            "cuda": None,
            "pytorch": torch.__version__,
        }

    except ImportError:
        return {
            "available": False,
            "name": "PyTorch not installed",
            "memory_gb": 0,
            "cuda": None,
            "pytorch": None,
        }


@app.get("/api/status")
def status():
    gpu = gpu_status()

    return {
        "platform": platform.system(),
        "python": platform.python_version(),
        "cpu": os.cpu_count(),
        "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "gpu": gpu,
    }


@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AniVora Cloud</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b0b12;
            color: white;
        }

        header {
            padding: 18px 22px;
            border-bottom: 1px solid #292936;
            background: #101018;
        }

        .logo {
            font-size: 22px;
            font-weight: bold;
        }

        .subtitle {
            color: #9292a5;
            margin-top: 5px;
            font-size: 13px;
        }

        main {
            padding: 22px;
            max-width: 1100px;
            margin: auto;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 16px;
        }

        .card {
            background: #15151f;
            border: 1px solid #292936;
            border-radius: 14px;
            padding: 20px;
        }

        .card h2 {
            margin-top: 0;
            font-size: 17px;
        }

        .value {
            font-size: 25px;
            font-weight: bold;
            margin-top: 12px;
        }

        .muted {
            color: #9292a5;
            font-size: 13px;
        }

        .status {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 20px;
            background: #20202c;
            margin-top: 10px;
        }

        button {
            border: 0;
            border-radius: 10px;
            padding: 12px 16px;
            background: white;
            color: black;
            font-weight: bold;
            cursor: pointer;
        }

        #output {
            white-space: pre-wrap;
            color: #bcbccd;
            margin-top: 15px;
            font-family: monospace;
            font-size: 13px;
        }
    </style>
</head>

<body>

<header>
    <div class="logo">🎬 AniVora Cloud</div>
    <div class="subtitle">AI Creator Infrastructure • v0.1.0</div>
</header>

<main>

    <div class="grid">

        <div class="card">
            <h2>GPU</h2>
            <div class="value" id="gpu">Checking...</div>
            <div class="muted" id="gpuDetails"></div>
        </div>

        <div class="card">
            <h2>CPU</h2>
            <div class="value" id="cpu">Checking...</div>
            <div class="muted">Available CPU threads</div>
        </div>

        <div class="card">
            <h2>RAM</h2>
            <div class="value" id="ram">Checking...</div>
            <div class="muted">System memory</div>
        </div>

        <div class="card">
            <h2>Environment</h2>
            <div class="value" id="python">Checking...</div>
            <div class="muted" id="platform"></div>
        </div>

    </div>

    <br>

    <div class="card">
        <h2>⚙️ Environment Test</h2>
        <p class="muted">
            This checks whether the AniVora worker can see the machine's
            CPU, RAM and GPU.
        </p>

        <button onclick="checkStatus()">Run Hardware Check</button>

        <div id="output"></div>
    </div>

</main>

<script>

async function checkStatus() {

    const output = document.getElementById("output");

    output.textContent = "Checking AniVora environment...";

    try {

        const response = await fetch("/api/status");
        const data = await response.json();

        document.getElementById("cpu").textContent =
            data.cpu;

        document.getElementById("ram").textContent =
            data.ram_gb + " GB";

        document.getElementById("python").textContent =
            data.python;

        document.getElementById("platform").textContent =
            data.platform;

        if (data.gpu.available) {

            document.getElementById("gpu").textContent =
                data.gpu.name;

            document.getElementById("gpuDetails").textContent =
                data.gpu.memory_gb +
                " GB VRAM • CUDA " +
                data.gpu.cuda;

        } else {

            document.getElementById("gpu").textContent =
                "No GPU";

            document.getElementById("gpuDetails").textContent =
                "GPU will be connected later";
        }

        output.textContent =
            JSON.stringify(data, null, 2);

    } catch (error) {

        output.textContent =
            "Environment check failed:\\n" +
            error;
    }
}

checkStatus();

</script>

</body>
</html>
"""
