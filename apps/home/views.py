from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from app.models import Article, TradingVolume, StockPrice
from app.serializers import *
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
from rest_framework.views import APIView
from rest_framework.response import Response

class StockPricesView(APIView):
    def get(self, request):
        stock_name = request.query_params.get('stock_name', None)

        if stock_name is not None:
            # stock_name을 기반으로 StockPrice 데이터를 필터링하여 가져옴
            stock_prices = StockPrice.objects.filter(stock_name=stock_name).order_by('-date')[:6]
            # 필요한 데이터를 시리얼라이즈하여 JSON 응답 생성
            serializer = StockPriceSerializer(stock_prices, many=True)
            return Response(serializer.data)
        else:
            # stock_name이 제공되지 않은 경우에 대한 처리
            return Response({"error": "stock_name을 제공하세요."}, status=400)