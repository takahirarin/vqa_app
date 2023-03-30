from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
from .model import *
import os

import sys
sys.path.append('.../')
from vqa_app.settings import MEDIA_ROOT



def main(img_path, text):
    # prepare image + question
    #url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    print(f'image_path: {img_path}')
    print(f'MEDIA_ROOT: {MEDIA_ROOT}')
    image = Image.open(os.path.join(MEDIA_ROOT, 'images', str(img_path)))
    #image = Image.open(requests.get(img_path, stream=True).raw)
    #text = "How many cats are there?"

    processor, model = initialize_model()

    #processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    #model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    print("Predicted answer:", model.config.id2label[idx])
    return model.config.id2label[idx]


if __name__ == "__main__":
    main()