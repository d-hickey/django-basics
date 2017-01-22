from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect

from .forms import TimeEntryForm
from .models import TimeEntry

# Create your views here.
def index(request):
    tdate = date.today()
    tdate = "%d-%d-%d" % (tdate.year, tdate.month, tdate.day)
    return givenDate(request, tdate)


def createDateObj(input_date):
    year, month, day = input_date.split('-')
    chosen_date = date(year=int(year), month=int(month), day=int(day))
    return chosen_date


def givenDate(request, date_given):
    if request.method == "POST":
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.rec_date = createDateObj(date_given)
            entry.save()
            redirect(reverse('timetracker:date', args=(date_given)))
    else:
        form = TimeEntryForm()
        chosen_date = createDateObj(date_given)
        date_entries = TimeEntry.objects.filter(rec_date=chosen_date).filter(user=request.user)
        return render(request, "timetracker/index.html", {'form': form, 'entries': date_entries, 'date': date_given})

