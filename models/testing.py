from diffusers import StableDiffusionPipeline
import torch

pipe = torch.load("image-model.pkl", map_location=torch.device('cuda'))
prompt=r"There was once a very rich merchant, who had six children, three sons, and three daughters; being a man of sense, he spared no cost for their education, but gave them all kinds of masters. His daughters were extremely handsome, especially the youngest. When she was little everybody admired her, and called her The little Beauty; so that, as she grew up, she still went by the name of Beauty, which made her sisters very jealous.The youngest, as she was handsomer, was also better than her sisters. The two eldest had a great deal of pride, because they were rich. They gave themselves ridiculous airs, and would not visit other merchants' daughters, nor keep company with any but persons of quality. They went out every day to parties of pleasure, balls, plays, concerts, and so forth, and they laughed at their youngest sister, because she spent the greatest part of her time in reading good books."
image = pipe(prompt).images[0]
image.save('o1.png')
