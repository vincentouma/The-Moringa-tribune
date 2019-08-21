from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article


# Create your views here.
#def welcome(request):
    #return render(request, 'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})

# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        editor = Editor.objects.get(email = 'example@gmail.com')
        print('Editor found')
    except DoesNotExist:
        print('Editor was not found')



        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})