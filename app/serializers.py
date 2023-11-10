from rest_framework import serializers
from .models import Article, TradingVolume, StockPrice


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['headline', 'crawling_time']


class TradingVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingVolume
        fields = ['stock_name', 'current_price', 'previous_close_price', 'volume_increase_rate', 'time']


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ['stock_name', 'date', 'price']

