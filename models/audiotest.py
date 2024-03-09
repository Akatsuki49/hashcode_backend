import torch
import soundfile as sf
from transformers import pipeline

synthesiser = pipeline("text-to-audio", "facebook/musicgen-stereo-small", device="cuda:0", torch_dtype=torch.float16)

torch.save(synthesiser,'audio-model.pkl')
