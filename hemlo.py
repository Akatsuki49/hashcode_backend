import torch
from diffusers import StableDiffusionPipeline

model_id = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
pipe = pipe.to("cuda")
    # return pipe

# Save the model to a .pkl file
torch.save(pipe, 'image-model.pkl')

