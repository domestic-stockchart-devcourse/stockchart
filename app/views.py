from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, TradingVolume, StockPrice
from .serializers import ArticleSerializer, TradingVolumeSerializer, StockPriceSerializer


class LatestArticlesView(APIView):
    def get(self, request):
        latest_articles = Article.objects.order_by('-crawling_time')[:6]
        serializer = ArticleSerializer(latest_articles, many=True)
        return Response(serializer.data)


class LatestTradingVolumesView(APIView):
    def get(self, request):
        latest_volumes = TradingVolume.objects.order_by('-time')[:6]
        serializer = TradingVolumeSerializer(latest_volumes, many=True)
        return Response(serializer.data)


class StockPricesView(APIView):
    def get(self, request):
        stock_name = request.query_params.get('stock_name', None)

        if stock_name is not None:
            stock_prices = StockPrice.objects.filter(stock_name=stock_name).order_by('-date')[:6]
        else:
            stock_prices = StockPrice.objects.none()

        serializer = StockPriceSerializer(stock_prices, many=True)
        return Response(serializer.data)
