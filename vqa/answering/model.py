from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image

def initialize_model():
    # prepare image + question

    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    return processor, model
