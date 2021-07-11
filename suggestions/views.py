import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from recommendations.recommender import get_similar_stress_reduction_method
from . import forms
# from django.http import HttpResponse
from .models import Method


def suggestion_list(request):
    # this grabs all of the records from this method database table
    methods = Method.objects.all().order_by('name')  # this orders the list by name
    return render(request, 'suggestions/suggestion_list.html', {"methods": methods})


@login_required(login_url="/accounts/login/")  # This prevents a user from accessing this page unless he has logged in
def suggestion_detail(request, slug):
    suggestion = Method.objects.get(slug=slug)
    return render(request, "suggestions/suggestion_detail.html", {"suggestion": suggestion})


@login_required(login_url="/accounts/login/")  # This prevents a user from accessing this page unless he has logged in
def give_recommendation(request):
    form = forms.GetSelections()
    selection_list = []

    def get_data(method_id, method_rating):
        selection_list.append((method_id, method_rating))
        return selection_list

    def recommendation(selections_list):
        similar_method = pd.DataFrame()
        for method, rating in selections_list:
            similar_method = similar_method.append(get_similar_stress_reduction_method(method, rating),
                                                   ignore_index=True)
        recommended = similar_method.sum().sort_values(ascending=False)
        return recommended

    # if it's a post request, pass the data as an argument into the get_data function to generate a selection list
    get_data('Yoga', 4)  # post data should go in here)
    get_data("laughter", 4)

    recommend = recommendation(selection_list)
    return render(request, 'suggestions/recommend.html', {"form": form, "recommend": recommend})


def rate_image(request):
    if request.method == 'POST':
        element_id = request.POST.get('element_id')
        val = request.POST.get('val')
        obj = Method.objects.get(id=element_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success': 'true', 'score': val}, safe=False)
    return JsonResponse({'success': 'false'})
