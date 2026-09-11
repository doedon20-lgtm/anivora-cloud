# 🎬 AniVora Cloud

AniVora Cloud is the infrastructure project behind AniVora's AI
creation system.

The long-term goal is to provide a Kaggle-like environment designed
specifically for AI animation and video generation.

## Current version

v0.1.0

## Planned capabilities

- Browser-based notebook
- Python environment
- GPU workers
- Persistent storage
- Model management
- Character assets
- Motion transfer
- AI video generation
- Job queue
- GPU monitoring
- Project management

## Architecture

GitHub
  ↓
AniVora Cloud
  ↓
Notebook / Web Interface
  ↓
Job Manager
  ↓
GPU Worker
  ↓
AI Models
  ↓
Generated Video

## Important

GitHub stores the source code.

Large AI checkpoints and generated videos should not be committed
to the repository.

Secrets must never be committed to GitHub.

## Development history

Initial AI experiments were performed using:

- Kaggle
- MimicMotion
- DWPose
- Stable Video Diffusion
- Wan2GP
- Viggle/Viggle-Animate research
