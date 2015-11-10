import sqlite3
import csv
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import forms

def program_of_study(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pos/thanks/')
    else:
        form = forms.StudentForm()
    return render(request, 'pos/pos_form.html', {'form': form})

def thanks(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'
    
    conn = sqlite3.connect("/home/bitnami/Projects/ece_pos/db.sqlite3")
    c = conn.cursor().execute("SELECT * FROM pos_student")
    writer = csv.writer(response)
    writer.writerows(c)

    return response
