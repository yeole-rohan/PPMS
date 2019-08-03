from django.shortcuts import render, redirect, render_to_response
from .models import Account, DieselStock, DieselNozzle, DieselDensity, PetrolDensity, PetrolNozzle, PetrolStock
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
import requests
# from datetime import datetime


# Create your views here.
def home(request):
    # response = requests.get("https://fuelprice.p.rapidapi.com/beta",
    # headers={
    # "X-RapidAPI-Host": "fuelprice.p.rapidapi.com",
    # "X-RapidAPI-Key": "0ac878f7damsha34523367ef1038p18de5cjsnbd6187a88519",
    # "Content-Type": "application/json",
    # "Accept": "application/json"
    # },
    # params=("{\"fuel\":\"p\",\"state\":\"dl\"}")
    # )
    # res = response.json()
    # print(res)
    return render(request, 'index.html')


def accountForm(request):
    student_list = Account.objects.all()
    return render(request, 'account.html', {'account': student_list})


def account(request):
    if request.method == 'POST':
        invoiceNumber = request.POST['invoiceNumber']
        petrolQuantity = request.POST['petrolQuantity']
        dieselQuantity = request.POST['dieselQuantity']
        lubricantQuantity = request.POST['lubricantQuantity']
        invoiceAount = request.POST['invoiceAount']
        payNumber = request.POST['payNumber']
        paymentDate = request.POST['paymentDate']
        amountPaid = request.POST['amountPaid']
        amountRemain = int(invoiceAount) - int(amountPaid)
        comment = request.POST['comment']
        shortExcess = request.POST['shortExcess']
        account = Account(invoiceNumber=invoiceNumber, petrolQuantity=petrolQuantity, dieselQuantity=dieselQuantity,
                          amountRemainPaid=amountRemain, lubricantQuantity=lubricantQuantity,
                          invoiceAmount=invoiceAount, cheque_demand_number=payNumber, paymentDate=paymentDate,
                          amountPaid=amountPaid, comment=comment, shortExcess=shortExcess)
        account.save()
        return redirect(accountForm)
    return render(request, 'account-form.html')


# Diesel Views Handle over here

def dieselStock(request):
    diesel = DieselStock.objects.all()
    return render(request, 'diesel.html', {'diesel': diesel})


def dieselNozzle(request):
    dieselData = DieselNozzle.objects.all()
    return render(request, 'diesel-nozzle.html', {'dieselData': dieselData})


def dieselDensity(request):
    density = DieselDensity.objects.all()
    return render(request, 'diesel-density.html', {'density': density})


def dieselNozzleForm(request):
    if request.method == 'POST':
        openingReadingForNozzle1 = request.POST['openingReadingForNozzle1']
        openingReadingForNozzle2 = request.POST['openingReadingForNozzle2']
        openingReadingForNozzle3 = request.POST['openingReadingForNozzle3']
        openingReadingForNozzle4 = request.POST['openingReadingForNozzle4']
        saleForNozzle1 = request.POST['saleForNozzle1']
        saleForNozzle2 = request.POST['saleForNozzle2']
        saleForNozzle3 = request.POST['saleForNozzle3']
        saleForNozzle4 = request.POST['saleForNozzle4']
        testing = request.POST['testing']
        rate = request.POST['rate']
        totalMeterSale = float(saleForNozzle1) + float(saleForNozzle2) + float(saleForNozzle3) + float(saleForNozzle4)
        totalAmount = float(totalMeterSale) * float(rate)
        dieselData = DieselNozzle(openingReadingForNozzle1=openingReadingForNozzle1,
                                  openingReadingForNozzle2=openingReadingForNozzle2,
                                  openingReadingForNozzle3=openingReadingForNozzle3,
                                  openingReadingForNozzle4=openingReadingForNozzle4, saleForNozzle1=saleForNozzle1,
                                  saleForNozzle2=saleForNozzle2, saleForNozzle3=saleForNozzle3,
                                  saleForNozzle4=saleForNozzle4, testing=testing, rate=rate, totalAmount=totalAmount,
                                  totalMeterSale=totalMeterSale)
        dieselData.save()
        return redirect(dieselNozzle)
    return render(request, 'dieselNozzleForm.html')


def dieselForm(request):
    if request.method == 'POST':
        openingStock = request.POST['openStock']
        receiptStock = request.POST['receiptStock']
        totalStock = float(openingStock) + float(receiptStock)
        actualSale = request.POST['actualSale']
        productDip = request.POST['productDip']
        actualDip = request.POST['actualDip']
        closingStock = float(totalStock) - float(actualSale)
        variation = float(actualDip) - float(closingStock)
        watertCm = request.POST['waterCm']
        waterLtrs = request.POST['waterLtr']
        diesel = DieselStock(
            openingStock=openingStock, receiptStock=receiptStock, totalStock=totalStock, actualSale=actualSale,
            productDip=productDip, actualDip=actualDip, closingStock=closingStock, variations=variation,
            waterCm=watertCm, waterLtrs=waterLtrs)
        diesel.save()
        return redirect(dieselStock)
    return render(request, 'diesel-form.html')


def dieselDensityForm(request):
    if request.method == 'POST':
        morningObservedHydroDensity = request.POST['morningObservedHydroDensity']
        morningObservedTemperatureDensity = request.POST['morningObservedTemperatureDensity']
        morningDensity = request.POST['morningDensity']
        receiptsInvoiceNumber = request.POST['receiptsInvoiceNumber']
        receiptsQuantity = request.POST['receiptsQuantity']
        receiptsObservedHydroDensity = request.POST['receiptsObservedHydroDensity']
        receiptsObservedTemperatureDensity = request.POST['receiptsObservedTemperatureDensity']
        receiptsDensity = request.POST['receiptsDensity']
        asPerChallanDensity = request.POST['asPerChallanDensity']
        decantationObservedHydroDensity = request.POST['decantationObservedHydroDensity']
        decantationObservedTemperatureDensity = request.POST['decantationObservedTemperatureDensity']
        decantationDensity = request.POST['decantationDensity']
        densityDifference = float(receiptsDensity) - float(asPerChallanDensity)

        dieselDensityTable = DieselDensity(morningObservedHydroDensity=morningObservedHydroDensity,
                                           morningObservedTemperatureDensity=morningObservedTemperatureDensity,
                                           morningDensity=morningDensity, receiptsInvoiceNumber=receiptsInvoiceNumber,
                                           receiptsQuantity=receiptsQuantity,
                                           receiptsObservedHydroDensity=receiptsObservedHydroDensity,
                                           receiptsObservedTemperatureDensity=receiptsObservedTemperatureDensity,
                                           receiptsDensity=receiptsDensity, asPerChallanDensity=asPerChallanDensity,
                                           decantationDensity=decantationDensity,
                                           decantationObservedHydroDensity=decantationObservedHydroDensity,
                                           decantationObservedTemperatureDensity=decantationObservedTemperatureDensity,
                                           densityDifference=densityDifference)
        dieselDensityTable.save()
        return redirect(dieselDensity)
    return render(request, 'diesel-density-form.html')


# Petrol Views will handled here

def petrolDensity(request):
    density = PetrolDensity.objects.all()
    return render(request, 'petrol-density.html', {'density': density})


def petrolNozzle(request):
    nozzle = PetrolNozzle.objects.all()
    return render(request, 'petrol-nozzle.html', {'nozzle': nozzle})


def petrolStock(request):
    stock = PetrolStock.objects.all()
    return render(request, 'petrol-stock.html', {'stock': stock})


def petrolNozzleForm(request):
    if request.method == 'POST':
        openingReadingForNozzle1 = request.POST['openingReadingForNozzle1']
        openingReadingForNozzle2 = request.POST['openingReadingForNozzle2']
        openingReadingForNozzle3 = request.POST['openingReadingForNozzle3']
        openingReadingForNozzle4 = request.POST['openingReadingForNozzle4']
        saleForNozzle1 = request.POST['saleForNozzle1']
        saleForNozzle2 = request.POST['saleForNozzle2']
        saleForNozzle3 = request.POST['saleForNozzle3']
        saleForNozzle4 = request.POST['saleForNozzle4']
        testing = request.POST['testing']
        rate = request.POST['rate']
        totalMeterSale = float(saleForNozzle1) + float(saleForNozzle2) + float(saleForNozzle3) + float(saleForNozzle4)
        totalAmount = float(totalMeterSale) * float(rate)
        petrolData = PetrolNozzle(openingReadingForNozzle1=openingReadingForNozzle1,
                                  openingReadingForNozzle2=openingReadingForNozzle2,
                                  openingReadingForNozzle3=openingReadingForNozzle3,
                                  openingReadingForNozzle4=openingReadingForNozzle4, saleForNozzle1=saleForNozzle1,
                                  saleForNozzle2=saleForNozzle2, saleForNozzle3=saleForNozzle3,
                                  saleForNozzle4=saleForNozzle4, testing=testing, rate=rate, totalAmount=totalAmount,
                                  totalMeterSale=totalMeterSale)
        petrolData.save()
        return redirect(petrolNozzle)
    return render(request, 'petrol-nozzle-form.html')


def petrolStockForm(request):
    if request.method == 'POST':
        openingStock = request.POST['openStock']
        receiptStock = request.POST['receiptStock']
        totalStock = float(openingStock) + float(receiptStock)
        actualSale = request.POST['actualSale']
        productDip = request.POST['productDip']
        actualDip = request.POST['actualDip']
        closingStock = float(totalStock) - float(actualSale)
        variation = float(actualDip) - float(closingStock)
        watertCm = request.POST['waterCm']
        waterLtrs = request.POST['waterLtr']
        petrol = PetrolStock(
            openingStock=openingStock, receiptStock=receiptStock, totalStock=totalStock, actualSale=actualSale,
            productDip=productDip, actualDip=actualDip, closingStock=closingStock, variations=variation,
            waterCm=watertCm, waterLtrs=waterLtrs)
        petrol.save()
        return redirect(petrolStock)
    return render(request, 'petrol-stock-form.html',{})


def petrolDensityForm(request):
    if request.method == 'POST':
        morningObservedHydroDensity = request.POST['morningObservedHydroDensity']
        morningObservedTemperatureDensity = request.POST['morningObservedTemperatureDensity']
        morningDensity = request.POST['morningDensity']
        receiptsInvoiceNumber = request.POST['receiptsInvoiceNumber']
        receiptsQuantity = request.POST['receiptsQuantity']
        receiptsObservedHydroDensity = request.POST['receiptsObservedHydroDensity']
        receiptsObservedTemperatureDensity = request.POST['receiptsObservedTemperatureDensity']
        receiptsDensity = request.POST['receiptsDensity']
        asPerChallanDensity = request.POST['asPerChallanDensity']
        decantationObservedHydroDensity = request.POST['decantationObservedHydroDensity']
        decantationObservedTemperatureDensity = request.POST['decantationObservedTemperatureDensity']
        decantationDensity = request.POST['decantationDensity']
        densityDifference = float(receiptsDensity) - float(asPerChallanDensity)

        petrolDensities = PetrolDensity(morningObservedHydroDensity=morningObservedHydroDensity,
                                        morningObservedTemperatureDensity=morningObservedTemperatureDensity,
                                        morningDensity=morningDensity, receiptsInvoiceNumber=receiptsInvoiceNumber,
                                        receiptsQuantity=receiptsQuantity,
                                        receiptsObservedHydroDensity=receiptsObservedHydroDensity,
                                        receiptsObservedTemperatureDensity=receiptsObservedTemperatureDensity,
                                        receiptsDensity=receiptsDensity, asPerChallanDensity=asPerChallanDensity,
                                        decantationDensity=decantationDensity,
                                        decantationObservedHydroDensity=decantationObservedHydroDensity,
                                        decantationObservedTemperatureDensity=decantationObservedTemperatureDensity,
                                        densityDifference=densityDifference)
        petrolDensities.save()
        return redirect(petrolDensity)
    return render(request, 'petrol-density-form.html')


def get_dta(request):
    dates = []
    totalAmount = []
    nozz = PetrolNozzle.objects.all()
    for dataset in nozz:
        dates.append(dataset.date)
        totalAmount.append(dataset.totalAmount)
    data = {
        "defaultDatas":totalAmount,
        "labels": dates,   
    }
    return JsonResponse(data)

def getDieselProfit(request):
    date = []
    totalAmount= []
    diesel = DieselNozzle.objects.all()
    for datas in diesel:
        date.append(datas.date)
        totalAmount.append(datas.totalAmount)
    data = {
        "date":date,
        "amount":totalAmount,
    }
    print(JsonResponse(data))
    return JsonResponse(data)
def getPetrolSale(request):
    month = []
    totalSales = []
    petrolSale = PetrolNozzle.objects.all()
    for alls in petrolSale:
        print(alls.totalMeterSale)
        month.append(alls.date)
        totalSales.append(alls.totalMeterSale)
        print(totalSales)
    data = {
        'month':month,
        'totalSale':totalSales
    }
    return JsonResponse(data)