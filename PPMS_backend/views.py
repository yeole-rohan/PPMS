from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as user
from django.shortcuts import get_object_or_404
from .models import Account, DieselStock, DieselNozzle, DieselDensity, PetrolDensity, PetrolNozzle, PetrolStock


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
    username = {
            'username':request.user.get_username()
            if request.user.is_authenticated else []
        }
    return render(request, 'index.html', username)

@login_required
def accountForm(request):
    student_list = Account.objects.all()
    return render(request, 'account.html', {'account': student_list})

@login_required
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
@login_required
def dieselStock(request):
    diesel = DieselStock.objects.all()
    return render(request, 'diesel.html', {'diesel': diesel})

@login_required
def dieselNozzle(request):
    dieselData = DieselNozzle.objects.all()
    return render(request, 'diesel-nozzle.html', {'dieselData': dieselData})

@login_required
def dieselDensity(request):
    density = DieselDensity.objects.all()
    return render(request, 'diesel-density.html', {'density': density})

@login_required
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

@login_required
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

@login_required
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
@login_required
def petrolDensity(request):
    density = PetrolDensity.objects.all()
    return render(request, 'petrol-density.html', {'density': density})

@login_required
def petrolNozzle(request):
    nozzle = PetrolNozzle.objects.all()
    return render(request, 'petrol-nozzle.html', {'nozzle': nozzle})

@login_required
def petrolStock(request):
    stock = PetrolStock.objects.all()
    return render(request, 'petrol-stock.html', {'stock': stock})

@login_required
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

@login_required
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

@login_required
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

@login_required
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
@login_required
def getDieselProfit(request):
    date = []
    totalAmount= []
    diesel = DieselNozzle.objects.all()
    for datas in diesel:
        date.append(datas.date)
        totalAmount.append(datas.totalAmount)
        totalAmount.append(datas.totalAmount)
    data = {
        "date":date,
        "amount":totalAmount,
    }
    return JsonResponse(data)
@login_required
def getPetrolSale(request):
    month = []
    totalSales = []
    petrolSale = PetrolNozzle.objects.all()
    for alls in petrolSale:
        #print(petrolSale.values())
        month.append(alls.date)
        # monts = str(month)
        # year, month, date = (monts.split('-'));
        # print(month)
        # assert isinstance(alls, object)
        totalSales.append(alls.totalMeterSale)
    data = {
        'month':month,
        'totalSale':totalSales
    }
    return JsonResponse(data)