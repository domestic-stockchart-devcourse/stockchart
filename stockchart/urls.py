from django.contrib import admin
from django.urls import path, include
from app.views import LatestArticlesView, LatestTradingVolumesView, StockPricesView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.home.urls")),
    path('latest-articles/', LatestArticlesView.as_view(), name='latest-articles'),
    path('latest-trading-volumes/', LatestTradingVolumesView.as_view(), name='latest-trading-volumes'),
    path('stock-prices/', StockPricesView.as_view(), name='stock-prices'),
]
