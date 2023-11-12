from rest_framework import serializers
from .models import Article, TradingVolume, StockPrice


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['headline', 'crawling_time']


class TradingVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingVolume
        fields = ['name', 'current_price', 'price_change', 'percent_change', 'time']


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ['stock_name', 'date', 'price']

