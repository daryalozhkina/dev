from django.shortcuts import render
import datetime


def index(request):
    date = datetime.date.now()
    context = {
       'date': date.strtime("%d-%m"),
       'page_title': 'Дата'
   }
    return render(request, 'mainapp/index.html', context)


def about(request):
        context = {
            'page_title': 'О нас'
        }
        return render(request, 'mainapp/about.html', context)



