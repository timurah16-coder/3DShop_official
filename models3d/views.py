# models3d/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Model3D, Order


def home(request):
    models = Model3D.objects.all().order_by('id')
    return render(request, 'home.html', {'models': models})

def order(request, model_id):
    model = get_object_or_404(Model3D, id=model_id)
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        color = request.POST.get('color', '').strip()
        pickup_date = request.POST.get('pickup_date', '').strip()

        # ✅ Проверяем, что всё заполнено
        if not all([email, first_name, last_name, color, pickup_date]):
            messages.error(request, "Пожалуйста, заполните все поля!")
            return render(request, 'order.html', {'model': model})

        # ✅ Сохраняем заказ, передавая модель
        Order.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            model=model,  # ← ВОТ ОНА!
            color=color,
            pickup_date=pickup_date
        )
        return redirect('success')

    return render(request, 'order.html', {'model': model})

def success(request):
    return render(request, 'success.html')