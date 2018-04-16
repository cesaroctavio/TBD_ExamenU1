from django.shortcuts import render

from django.shortcuts import redirect
from .models import Movie
import redis


r = redis.Redis(host='localhost', port=6379, db=0)

# Create your views here.

def sql_to_redis(request):
    m = Movie.objects.all()

    Theater = []

    for i in m:
        peli ={
        'Movies':{m.get(id=i.id).id:
        [m.get(id=i.id).name,
        m.get(id=i.id).year,
        m.get(id=i.id).studio,
        m.get(id=i.id).genre,
        m.get(id=i.id).active,
        m.get(id=i.id).created]}
        }

        Theater.append(peli)

    r.set('Movies', Theater)
    return redirect('/')

def home(request):
    context = {'Movies': r.get('Movies')}

    return render(request, 'index.html', context)
