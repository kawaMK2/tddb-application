from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import *
from .forms import *
from .solidify2 import *


# Create your views here.
def index(request):
    form = ObjInputForm()
    contexts = {
        "all_data": ObjInput.objects.all(),
        "form": form,
    }
    return render(request, "solidify/index.html", contexts)


def upload(request):
    form = ObjInputForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/solidify/")

    contexts = {
        "all_data": File.objects.all(),
        "form": form,
    }
    return render(request, 'main/index.html', contexts)


def add(request):
    if request.method == "POST":
        form = AddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = request.POST
            print(str(request.FILES['file']).split(".")[0])
            new_file = ObjInput(name=str(request.FILES['file']).split(".")[0],
                                file=request.FILES['file'],
                                added_time=data.get("date", ""),
                                r=data.get("r", ""),
                                g=data.get("g", ""),
                                b=data.get("b", ""),
                                thickness=data.get("thickness", ""))
            new_file.save()
            path = settings.BASE_DIR+new_file.file.url
            vertices, _, _, _, _, _, _ = loadOBJ(path)
            print(vertices)
            solidify2(path, vertices, float(new_file.thickness), float(new_file.height), True)
            saveMTL(path.split(".")[0]+".mtl", convert_rgb([int(new_file.r), int(new_file.g), int(new_file.b)]))

            return redirect("/solidify/")
    else:
        form = AddForm()
    return render(request, "solidify/add.html", {"add_form": form})


# def download(request, file_name):
#     file = get_object_or_404(ObjInput, name=file_name)
#     solidify2("/Users/shintarooo0079/Desktop/output.obj", file.name, file.thickness, file.height, True)
#     saveMTL("/Users/shintarooo0079/Desktop/output.mtl", convert_rgb([file.r, file.g, file.b]))
#     return redirect("/solidify")

