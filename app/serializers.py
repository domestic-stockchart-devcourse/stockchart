from rest_framework import serializers
from .models import Article, TradingVolume, StockPrice


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['headline', 'crawling_time']


class TradingVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingVolume
        fields = ['rank', 'stock_name', 'current_price', 'price_change', 'percent_change', 'volume',
                  'prev_volume', 'market_cap', 'created_at']


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ['stock_name', 'date', 'price']

