from django.shortcuts import render, redirect

# Create your views here.
from .forms import VQAForm
from .models import VQA
from .answering.answer import main
import os
import sys
sys.path.append('../')
from vqa_app.settings import MEDIA_ROOT


def upload(request):
    if request.method == "POST":
        form = VQAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            vqa = VQA.objects.get(pk=VQA.objects.count())
            image = form.cleaned_data['image']
            text = form.cleaned_data['text']
            answer = main(image, text)
            vqa.answer = answer
            #vqa = VQA.objects.create(image=form, text=text, answer=answer)
            # vqa.answer = output
            vqa.save()
            return redirect("vqa:result")
    else:
        form = VQAForm()
    context = {"form": form}
    return render(request, "vqa/upload.html", context)


def result(request):
    images = VQA.objects.all().order_by("-pk")
    context = {"images": images[1:], "now_image": images[0]}
    return render(request, "vqa/result.html", context)

