from django.shortcuts import render
from django.shortcuts import redirect
from .models import Table
from .forms import AddRecordForm


def record(request):
    records = Table.cars.all()
    return render(request, 'table/table.html', {'records': records})


def add_post(request):
    if request.method == 'POST':
        post_form = AddRecordForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.full_clean()
            new_post.save()
            records = Table.cars.all()
            return redirect('/table')
    else:
        post_form = AddRecordForm()
    return render(request, 'table/add_record.html', {'post_form': post_form})