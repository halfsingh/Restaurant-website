from django.shortcuts import render
from meals.models import Meals, category
from blog.models import Post
from aboutus.models import Why_Choose_Us, AboutUs
# Create your views here.

def home(request):
    
    meals = Meals.objects.all()
    categories= category.objects.all()
    meal_list = Meals.objects.all()
    posts = Post.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()
    about = AboutUs.objects.last()

    
    context = {
        'meals' : meals,
        'categories' : categories,
        'meal_list' : meal_list,
        'posts' : posts,
        'why_choose_us' : why_choose_us,
        'about' : about,
    }

    return render(request , 'home/index.html' , context)




