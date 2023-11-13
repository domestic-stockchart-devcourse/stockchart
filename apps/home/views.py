from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from app.models import *


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def get_stock_price_data(request):
    stock_name = "삼성전자"  # 원하는 주식명으로 수정
    stock_prices = StockPrice.objects.filter(stock_name=stock_name).order_by('date')
    labels = [str(price.date) for price in stock_prices]
    data = [float(price.price) for price in stock_prices]
    chart_data = {'labels': labels, 'data': data}
    return JsonResponse(chart_data)

def article_list(request):
    articles = Article.objects.all()[:10]  # Article 모델에서 모든 레코드를 가져옴
    context = {'article_list': articles}
    return render(request, 'index.html', context)