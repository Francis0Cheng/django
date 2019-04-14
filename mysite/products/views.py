from django.shortcuts import render

from .models import Product
from .froms import ProductForm, RawProductForm


# Create your views here.


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            # create new obj with cleaned_data
            Product.objects.create(**my_form.cleaned_data)
            # the ** turns my_form.cleaned_data into args
        else:
            print(my_form.errors)
    context = {
        'form': my_form,
    }

    return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#         # rerender it, to clear the text
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context={
    #     'title':obj.title,
    #     'description':obj.description,
    # }
    context = {
        'obj': obj,
    }
    return render(request, "products/product_detail.html", context)
