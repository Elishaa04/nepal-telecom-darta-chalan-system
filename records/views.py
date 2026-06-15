from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DartaForm, ChalanForm
from .models import Darta, Chalan, ActivityLog
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
import openpyxl
from django.http import HttpResponse
from .forms import DartaForm, ChalanForm, UserForm

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):

    total_darta = Darta.objects.count()
    total_chalan = Chalan.objects.count()
    total_users = User.objects.count()

    today = timezone.now().date()

    today_darta = Darta.objects.filter(
        darta_date=today
    ).count()

    today_chalan = Chalan.objects.filter(
        chalan_date=today
    ).count()

    recent_activities = ActivityLog.objects.all().order_by(
        '-created_at'
    )[:5]

    context = {
    'total_darta': total_darta,
    'total_chalan': total_chalan,
    'total_users': total_users,
    'today_darta': today_darta,
    'today_chalan': today_chalan,
    'recent_activities': recent_activities,
    'total_users': total_users,
}

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def darta_list(request):

    if request.method == 'POST':
        form = DartaForm(request.POST, request.FILES)

        if form.is_valid():

            darta = form.save(commit=False)

            darta.created_by = request.user

            darta.save()

            ActivityLog.objects.create(
                action=f"{request.user.username} added Darta {darta.darta_no}"
                )

            return redirect('darta_list')

    else:
        form = DartaForm()

    search = request.GET.get('search')

    if search:
        dartas = Darta.objects.filter(
            darta_no__icontains=search
        ).order_by('-id')
    else:
        dartas = Darta.objects.all().order_by('-id')

    return render(
        request,
        'darta_list.html',
        {
            'form': form,
            'dartas': dartas,
            'search': search
        }
    )


@login_required
def chalan_list(request):

    if request.method == 'POST':
        form = ChalanForm(request.POST, request.FILES)

        if form.is_valid():

            chalan = form.save(commit=False)

            chalan.created_by = request.user

            chalan.save()

            ActivityLog.objects.create(
                action=f"{request.user.username} added Chalan {chalan.chalan_no}"
                )

            return redirect('chalan_list')

    else:
        form = ChalanForm()

    search = request.GET.get('search')

    if search:
        chalans = Chalan.objects.filter(
            chalan_no__icontains=search
        ).order_by('-id')
    else:
        chalans = Chalan.objects.all().order_by('-id')

    return render(
        request,
        'chalan_list.html',
        {
            'form': form,
            'chalans': chalans,
            'search': search
        }
    )


@login_required
def edit_darta(request, id):

    darta = get_object_or_404(Darta, id=id)

    if request.method == 'POST':
        form = DartaForm(
            request.POST,
            request.FILES,
            instance=darta
        )

        if form.is_valid():
            form.save()
            ActivityLog.objects.create(
                action=f"{request.user.username} edited Darta {darta.darta_no}"
                )
            return redirect('darta_list')

    else:
        form = DartaForm(instance=darta)

    dartas = Darta.objects.all().order_by('-id')

    return render(
        request,
        'darta_list.html',
        {
            'form': form,
            'dartas': dartas
        }
    )

@login_required
def delete_darta(request, id):

    darta = get_object_or_404(Darta, id=id)

    darta_no = darta.darta_no

    ActivityLog.objects.create(
        action=f"{request.user.username} deleted Darta {darta_no}"
    )

    darta.delete()

    return redirect('darta_list')


@login_required
def edit_chalan(request, id):

    chalan = get_object_or_404(Chalan, id=id)

    if request.method == 'POST':
        form = ChalanForm(
            request.POST,
            request.FILES,
            instance=chalan
        )

        if form.is_valid():
            form.save()
            ActivityLog.objects.create(
                action=f"{request.user.username} edited Chalan {chalan.chalan_no}"
                )
            return redirect('chalan_list')

    else:
        form = ChalanForm(instance=chalan)

    chalans = Chalan.objects.all().order_by('-id')

    return render(
        request,
        'chalan_list.html',
        {
            'form': form,
            'chalans': chalans
        }
    )


@login_required
def delete_chalan(request, id):

    chalan = get_object_or_404(Chalan, id=id)

    chalan_no = chalan.chalan_no

    ActivityLog.objects.create(
        action=f"{request.user.username} deleted Chalan {chalan_no}"
    )

    chalan.delete()

    return redirect('chalan_list')
@login_required
def export_darta_excel(request):

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Darta Records"

    sheet.append([
        "Darta No",
        "Date",
        "Received From",
        "Subject",
        "Created By"
    ])

    for darta in Darta.objects.all():
        sheet.append([
            darta.darta_no,
            str(darta.darta_date),
            darta.received_from,
            darta.subject,
            str(darta.created_by)
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=darta_records.xlsx'

    workbook.save(response)

    return response


@login_required
def export_chalan_excel(request):

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Chalan Records"

    sheet.append([
        "Chalan No",
        "Date",
        "Sent To",
        "Subject",
        "Created By"
    ])

    for chalan in Chalan.objects.all():
        sheet.append([
            chalan.chalan_no,
            str(chalan.chalan_date),
            chalan.sent_to,
            chalan.subject,
            str(chalan.created_by)
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=chalan_records.xlsx'

    workbook.save(response)

    return response
from django.contrib.auth.models import User

@login_required
def user_list(request):

    if not request.user.is_superuser:
        return redirect('dashboard')

    users = User.objects.all().order_by('username')

    return render(
        request,
        'user_list.html',
        {
            'users': users
        }
    )
@login_required
def create_user(request):

    if not request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            ActivityLog.objects.create(
                action=f"{request.user.username} created user {user.username}"
            )

            return redirect('user_list')

    else:
        form = UserForm()

    return render(
        request,
        'create_user.html',
        {
            'form': form
        }
    )
@login_required
def edit_user(request, id):

    if not request.user.is_superuser:
        return redirect('dashboard')

    user = get_object_or_404(User, id=id)

    if request.method == 'POST':

        form = UserForm(request.POST, instance=user)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data['password']

            if password:
                user.set_password(password)

            user.save()

            ActivityLog.objects.create(
                action=f"{request.user.username} edited user {user.username}"
            )

            return redirect('user_list')

    else:
        form = UserForm(instance=user)

    return render(
        request,
        'create_user.html',
        {
            'form': form
        }
    )


@login_required
def delete_user(request, id):

    if not request.user.is_superuser:
        return redirect('dashboard')

    user = get_object_or_404(User, id=id)

    username = user.username

    user.delete()

    ActivityLog.objects.create(
        action=f"{request.user.username} deleted user {username}"
    )

    return redirect('user_list')