from django.shortcuts import render, redirect
from members.models import *
from .models import *
from datetime import timedelta, datetime

# Create your views here.
def home(request):
    member_set = Member.objects.all()
    context = {
        'member_set': member_set
    }
    return render(request, 'manager/home.html', context)


def add_member(request):
    if request.method == 'POST':
        member = Member()
        member.name = request.POST.get('name')
        member.picture = request.FILES.get('image')
        member.advance = request.POST.get('advance')
        member.join_date = request.POST.get('join_date')

        member.save()

        return redirect('home')

    return render(request, 'manager/add_member.html')


def meal(request):
    temp =  MealMonth.objects.all().last()
    from_date = temp.from_date
    to_date = temp.to_date

    all_dates = []
    num_days = (to_date - from_date).days
    for i in range(num_days + 1):
        current_date = from_date + timedelta(days=i)
        all_dates.append(current_date)
    
    meal_list = []
    all_joma = []
    for item in temp.members.all():
        tmp = {
            'name': item.name,
            'meals': temp.all_meals.filter(member=item)
        }
        meal_list.append(tmp)

        bbb = 0
        for i in Joma.objects.filter(joma_month=MealMonth.objects.all().last(), joma_by=item):
            bbb += i.joma_amount
        
        joma_temp = {
            'name': item.name,
            'amount': bbb
        }

        all_joma.append(joma_temp)

    context = {
        'current_meal': temp,
        'all_dates': all_dates,
        'members': temp.members.all(),
        'meal_list': meal_list,
        'member_set': Member.objects.all(),
        'all_meal': MealMonth.objects.all().order_by('-pk'),
        'all_joma': all_joma,
        'all_bazar': Bazar.objects.filter(bazar_month=temp)
    }
    return render(request, 'manager/meal.html', context)



def update_meal(request):
    member = Member.objects.get(pk=int(request.POST.get('member')))
    date_obj = datetime.strptime(request.POST.get('date'),  "%b. %d, %Y")
    date = date_obj.strftime("%Y-%m-%d")
    print(date)
    total = int(request.POST.get('number_of_meal'))
    print(total)

    m = Meal.objects.filter(member=member, date=date).last()
    print(m)
    m.number_of_meals = total
    m.save()
    print(m.date)

    return redirect('meal')


def create_month(request):
    mm = MealMonth()
    mm.month_name = request.POST.get('month_name')
    mm.year = request.POST.get('year')
    mm.from_date = datetime.strptime(request.POST.get('from_date'), '%Y-%m-%d').date()
    mm.to_date = datetime.strptime(request.POST.get('to_date'), '%Y-%m-%d').date()
    mm.save()

    members = request.POST.getlist('members')


    num_days = (mm.to_date - mm.from_date).days

    

    for member in members:
        member = Member.objects.get(pk=int(member))
        mm.members.add(member)
        mm.save()

        for i in range(num_days + 1):
            current_date = mm.from_date + timedelta(days=i)
            print(current_date)
            meal = Meal()
            meal.member = member
            meal.date = current_date
            meal.save()
            mm.all_meals.add(meal)
            mm.save()
    return redirect('meal')


def add_joma(request):
    member = Member.objects.get(pk=int(request.POST.get('member_pk')))
    amount = int(request.POST.get('joma_amount'))
    joma_month = MealMonth.objects.get(pk=int(request.POST.get('joma_month_pk')))

    joma_obj = Joma()
    joma_obj.joma_by = member
    joma_obj.joma_month = joma_month
    joma_obj.joma_amount = amount
    joma_obj.joma_date = datetime.now()
    joma_obj.save()
    
    return redirect('meal')



def add_bazar(request):
    amount = int(request.POST.get('bazar_amount'))
    member = Member.objects.get(pk=int(request.POST.get('bazar_member_pk')))
    month = MealMonth.objects.get(pk=int(request.POST.get('bazar_month_pk')))

    bazar_obj = Bazar()
    bazar_obj.bazar_by = member
    bazar_obj.bazar_month = month
    bazar_obj.bazar_amount = amount
    bazar_obj.bazar_details = request.POST.get('bazar_details')
    bazar_obj.save()

    return redirect('meal')
