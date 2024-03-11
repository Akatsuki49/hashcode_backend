import torch
import soundfile as sf
from transformers import pipeline

device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
synthesiser = pipeline("text-to-audio", "facebook/musicgen-medium", device=device, torch_dtype=torch.float16)

torch.save(synthesiser,'audio-model.pkl')
