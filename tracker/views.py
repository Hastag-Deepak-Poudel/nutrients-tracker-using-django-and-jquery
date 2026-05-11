from django.shortcuts import render, redirect, get_object_or_404
from .models import Nutrients, FoodConsumed


def index(request):
    if request.method == "POST":
        food_option = request.POST.get('food_option')
        food_selected = get_object_or_404(Nutrients, food=food_option)
        #object = FoodConsumed.objects.create(user=request.user, food_consumed=food_selected)
        #object.save()
        FoodConsumed.objects.create(user=request.user, food_consumed=food_selected) # automatically saves the object
        return redirect('index')

    consumed = FoodConsumed.objects.filter(user=request.user)
    foods = Nutrients.objects.all()
    return render(request, 'tracker/index.html', {'foods' : foods, 'consumed': consumed})

#def index(request):
    # if request.method == "POST":
    #     food_option = request.POST.get('food_option')
    #     # Use get_object_or_404 for better error handling
    #     food_selected = get_object_or_404(Nutrients, food=food_option)
    #     FoodConsumed.objects.create(user=request.user, food_consumed=food_selected)
    #     return redirect('index')  # Redirect to prevent form resubmission

# def consumed_food(request):
#     if request.method == "GET":
#         consumed = FoodConsumed.objects.filter(user=request.user)
#     return render(request, 'tracker/index.html', {'consumed': consumed})
    
