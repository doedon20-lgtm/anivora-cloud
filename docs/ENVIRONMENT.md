# AniVora AI Environment

## Purpose

This document records the AI environment used by AniVora.

## Current experiments

### MimicMotion

Location used during development:

/kaggle/working/MimicMotion

Checkpoint:

/kaggle/working/MimicMotion/models/MimicMotion_1-1.pth

Anime test assets:

/kaggle/working/MimicMotion/assets/anime_test/

### Wan2GP

Location used during development:

/kaggle/working/Wan2GP

## Important rule

Do not store:

- Hugging Face tokens
- API keys
- passwords
- private credentials

inside GitHub.

Secrets must be provided through environment variables or a secure secret manager.

## GPU target

The AniVora worker should detect:

- NVIDIA GPU
- CUDA
- VRAM
- PyTorch
- available GPU memory

before starting an AI generation job.
