import torch
from diffusers import StableDiffusionPipeline

seed_value = 1
torch.manual_seed(seed_value)

model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda" if torch.cuda.is_available() else "cpu")

torch.save(pipe, 'image-model.pkl')
