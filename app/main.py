from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import torch
from diffusers import DiffusionPipeline
from fastapi.responses import StreamingResponse
from PIL import Image
import io
#import gc

app = FastAPI()

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")
generator = torch.Generator(device="cpu").manual_seed(42)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/serve")
def read_root():
    return {"Hello": "World World"}

@app.get("/crear_imagen")
def read_item(w: Union[str, None] = None):
    generator = torch.Generator(device="cuda").manual_seed(42) # usaremos una seed para que todos veamos la misma imagen
    prompt = w # descripción de la imagen a generar
    images = pipeline(prompt, generator=generator).images # generamos una imagen y retornamos los resultados
    #media.show_images(images) # mostramos la imagen
    img_byte_arr = io.BytesIO()
    images[0].save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    return StreamingResponse(io.BytesIO(img_byte_arr), media_type="image/jpeg")
    #return {"Hello":w}