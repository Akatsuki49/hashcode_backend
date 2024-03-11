import torch
import soundfile as sf
from pydub import AudioSegment

def audgen(prompt1):

    synthesiser = torch.load('./models/audio-model.pkl',map_location=torch.device('cuda' if torch.cuda.is_available() else "cpu"))
    music = synthesiser("Generate an EDM track with a catchy beat and uplifting melody", forward_params={"max_new_tokens": 200})
    sf.write("musicgen_out.wav", music["audio"][0].T, music["sampling_rate"])
    # audio = AudioSegment.from_wav("musicgen_out.wav")
    # audio.export("music.mp3",format="mp3",bitrate='192k')