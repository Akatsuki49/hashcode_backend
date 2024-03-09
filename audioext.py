import torch
import soundfile as sf

synthesiser = torch.load('audio-model.pkl',map_location=torch.device('cuda'))

music = synthesiser("Generate an EDM track with a catchy beat and uplifting melody", forward_params={"max_new_tokens": 200})

sf.write("musicgen_out.wav", music["audio"][0].T, music["sampling_rate"])