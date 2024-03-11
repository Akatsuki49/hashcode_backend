from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from io import BytesIO
import base64

def imggen(prompt1):
    seed_value = 1
    pipe = torch.load("./models/image-model.pkl", map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    torch.manual_seed(seed_value)
    image = pipe(prompt1).images[0]
    bys = BytesIO()
    image.save(bys,format='PNG')
    bys.seek(0)
    return base64.b64encode(bys.read()).decode("utf-8")


    
