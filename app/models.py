from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=200, default='')
    article_url = models.CharField(max_length=300, default="https://finance.naver.com")

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
    stock_name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_close_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume_increase_rate = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.TimeField()

    def __str__(self):
        return f"{self.stock_name} - {self.time}"
