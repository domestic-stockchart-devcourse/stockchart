from django.db import models
from django.utils import timezone


class Article(models.Model):
    headline = models.CharField(max_length=200)
    crawling_time = models.DateTimeField()

    def __str__(self):
        return self.headline


class StockPrice(models.Model):
    stock_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.stock_name} - {self.date} {self.time}"


class TradingVolume(models.Model):
    rank = models.IntegerField(verbose_name='순위', default=0)
    name = models.CharField(max_length=100, verbose_name='종목명', default='없음')
    current_price = models.IntegerField(verbose_name='현재가', default=0)
    price_change = models.IntegerField(verbose_name='전일비', default=0)
    percent_change = models.CharField(max_length=100, verbose_name='등락률', default='0%')
    volume = models.BigIntegerField(verbose_name='거래량', default=0)
    prev_volume = models.BigIntegerField(verbose_name='전일거래량', default=0)
    market_cap = models.IntegerField(verbose_name='시가총액', default=0)
    created_at = models.DateTimeField(verbose_name='시간', auto_now_add = True)

    
    def __str__(self) :
        return self.name
