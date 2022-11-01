from django.shortcuts import render , redirect
from .models import soccer
from django.contrib.auth.models import User


def index(request):
    
    if request.method == "POST":
        #프론트에서 백으로 데이터 가져오기
        유저아이디 = request.user.pk
        coach = User.objects.get(id=유저아이디).username
        name = request.POST['축구선수이름']
        team = request.POST['팀명']
        backnumber = request.POST['백넘버']
        salary = request.POST['연봉']
        
        # 가져온 정보를 어떤 열에 넣을지 정하기
        saveplayer = soccer.objects.create(
            name = name,
            team = team,
            backnumber = backnumber,
            coach = coach,
            salary = salary
        )
        # 정해졌으면 저장하기
        saveplayer.save()
        return redirect('/')
    else: 
        # try:
            user_id = request.user.pk
            coach = User.objects.get(id=user_id).username
            allplayer = soccer.objects.filter(coach=coach).order_by('name')

            a = len(allplayer)
            
            total = 0
            for i in range(0,a):
                salary = int(allplayer[i].salary)
                total = total + salary                
            context = {'allplayer' : allplayer , 'total' : total}
            return render(request,'index.html', context)
        #     return redirect('/accounts/login')
    
def searchplayer(request):
    #POST방식
    if request.method == "POST":
        name = request.POST['name']
        backnumber = request.POST['backnumber']
        내가찾은축구선수 = soccer.objects.filter(name=name ,backnumber=backnumber)
        context = {'축구선수출력' : 내가찾은축구선수}
        return render(request,'searchplayer.html', context)
    #GET방식
    else: 
        return render(request,'searchplayer.html')
    
def updateplayer(request,id):
    if request.method == "GET":
        updateplayer = soccer.objects.get(pk=id)
        context = {'updateplayer' : updateplayer}
        return render(request,'updateplayer.html', context)
    else :
        updateplayer = soccer.objects.filter(pk=id)
        updateplayer.update(
            name = request.POST['name'],
            team = request.POST['team'],
            backnumber = request.POST['backnumber'],
            coach = request.POST['coach'], 
            salary = request.POST['salary'],
        )
        return redirect('/')
    
def deleteplayer(request,id):
    deleteplayer = soccer.objects.get(pk=id)
    deleteplayer.delete()
    return redirect('/')

def plus(request,id):
    
    howmuch = int(request.POST['howmuch'])
    salary = int(soccer.objects.get(pk=id).salary)  #=> 1500
    
    player = soccer.objects.filter(pk=id)
    player.update(
        salary = salary + howmuch
    )
    return redirect('/')

def minus(request,id):
    
    salary = int(soccer.objects.get(pk=id).salary)  #=> 1500
    
    player = soccer.objects.filter(pk=id)
    player.update(
        salary = salary - 100
    )
    return redirect('/')