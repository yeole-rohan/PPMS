from django.db import models
from django.contrib.auth.models import User


DEFAULT = 1

class Account(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    invoiceNumber = models.IntegerField(unique_for_date=True)
    petrolQuantity = models.IntegerField(blank=True)
    dieselQuantity = models.IntegerField(blank=True)
    lubricantQuantity = models.IntegerField(blank=True)
    invoiceAmount = models.IntegerField(blank=False, null=False)
    cheque_demand_number = models.IntegerField(blank=False, null=False)
    paymentDate = models.DateField(auto_now_add=False, auto_now=False)
    amountPaid = models.IntegerField()
    amountRemainPaid = models.IntegerField()
    shortExcess = models.IntegerField(null=True)
    comment = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '%s' % self.date

class DieselStock(models.Model):
    date = models.DateField(auto_now_add=True)
    openingStock = models.FloatField(default=0)
    receiptStock = models.FloatField(default=0)
    totalStock = models.FloatField(blank=False, null=False)
    actualSale = models.FloatField(default=0)
    closingStock = models.FloatField(null=False, blank=False)
    productDip = models.FloatField(default=0)
    actualDip = models.FloatField(default=0)
    variations = models.FloatField(default=0)
    waterCm = models.FloatField(default=0)
    waterLtrs = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.date

class DieselNozzle(models.Model):
    date = models.DateField(auto_now_add=True)
    openingReadingForNozzle1 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle2 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle3 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle4 = models.FloatField(null=False, blank=False)
    saleForNozzle1 = models.FloatField(default=0)
    saleForNozzle2 = models.FloatField(default=0)
    saleForNozzle3 = models.FloatField(default=0)
    saleForNozzle4 = models.FloatField(default=0)
    totalMeterSale = models.FloatField(null=False, blank=False)
    testing = models.IntegerField(default=0)
    rate = models.FloatField(null=False, blank=False)
    totalAmount = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.date

class DieselDensity(models.Model):
    date = models.DateField(auto_now_add=True)
    morningObservedHydroDensity = models.IntegerField(default=0)
    morningObservedTemperatureDensity = models.FloatField(default=0)
    morningDensity = models.FloatField(default=0)
    receiptsInvoiceNumber = models.IntegerField(default=0)
    receiptsQuantity = models.IntegerField(default=0)
    receiptsObservedHydroDensity = models.FloatField(default=0)
    receiptsObservedTemperatureDensity = models.FloatField(default=0)
    receiptsDensity = models.FloatField(default=0)
    asPerChallanDensity = models.FloatField(default=0)
    decantationObservedHydroDensity = models.IntegerField(default=0)
    decantationObservedTemperatureDensity = models.FloatField(default=0)
    decantationDensity = models.FloatField(default=0)
    densityDifference = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.date

class PetrolDensity(models.Model):
    date = models.DateField(auto_now_add=True)
    morningObservedHydroDensity = models.IntegerField(default=0)
    morningObservedTemperatureDensity = models.FloatField(default=0)
    morningDensity = models.FloatField(default=0)
    receiptsInvoiceNumber = models.IntegerField(default=0)
    receiptsQuantity = models.IntegerField(default=0)
    receiptsObservedHydroDensity = models.FloatField(default=0)
    receiptsObservedTemperatureDensity = models.FloatField(default=0)
    receiptsDensity = models.FloatField(default=0)
    asPerChallanDensity = models.FloatField(default=0)
    decantationObservedHydroDensity = models.IntegerField(default=0)
    decantationObservedTemperatureDensity = models.FloatField(default=0)
    decantationDensity = models.FloatField(default=0)
    densityDifference = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.date

class PetrolNozzle(models.Model):
    date = models.DateField(auto_now_add=True,null=False,blank=False,verbose_name="Should n0t be null")
    openingReadingForNozzle1 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle2 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle3 = models.FloatField(null=False, blank=False)
    openingReadingForNozzle4 = models.FloatField(null=False, blank=False)
    saleForNozzle1 = models.FloatField(default=0)
    saleForNozzle2 = models.FloatField(default=0)
    saleForNozzle3 = models.FloatField(default=0)
    saleForNozzle4 = models.FloatField(default=0)
    totalMeterSale = models.FloatField(null=False, blank=False)
    testing = models.IntegerField(default=0)
    rate = models.FloatField(null=False, blank=False)
    totalAmount = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.date)

class PetrolStock(models.Model):
    date = models.DateField(auto_now_add=True)
    openingStock = models.FloatField(default=0)
    receiptStock = models.FloatField(default=0)
    totalStock = models.FloatField(blank=False, null=False)
    actualSale = models.FloatField(default=0)
    closingStock = models.FloatField(null=False, blank=False)
    productDip = models.FloatField(default=0)
    actualDip = models.FloatField(default=0)
    variations = models.FloatField(default=0)
    waterCm = models.FloatField(default=0)
    waterLtrs = models.FloatField(default=0)

    def __str__(self):
        return '{} '.format(self.date)
