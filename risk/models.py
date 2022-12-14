from django.db import models


# Create your models here.
class Equities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=10)
    description = models.CharField(max_length=2000)
    start_date = models.DateField()
    end_date = models.DateField()
    sector = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    employee_count = models.IntegerField()
    sic_no = models.IntegerField()
    location = models.CharField(max_length=40)
    exchange_id = models.IntegerField()
    cik_no = models.IntegerField()
    cuisp = models.CharField(max_length=20)
    currency_id = models.IntegerField()
    data_source_id = models.IntegerField()
    ckr_log = models.BooleanField()
    similar_fund_log = models.BooleanField()
    address = models.CharField(max_length=70)
    company_name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=20)
    website = models.CharField(max_length=60)
    is_active = models.BooleanField()
    url_slug = models.CharField(max_length=40)
    delisted_date = models.DateField()
    delisted_reason = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)
    image_aspect_ratio = models.FloatField()
    cumulative_return_update = models.DateTimeField()


class Returns(models.Model):
    date = models.DateField()
    returns = models.FloatField()
    equity_id = models.ForeignKey(Equities, on_delete=models.CASCADE)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
