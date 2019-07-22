from .forms import EntryForm
from .models import Entry
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


# Create your views here.
def entry_list(request):
    entries = Entry.objects.filter(last_saved_date__lte=timezone.now()).order_by('last_saved_date')
    return render(request, 'entry/entry_list.html', {'entries':entries})

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry/entry_detail.html', {'entry': entry})

def entry_new(request):
    # entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.last_saved_date = timezone.now()
            entry.save()
            return redirect('entry_detail', pk=entry.pk)

    else:
        form = EntryForm()
    return render(request, 'entry/entry_edit.html', {'form': form})

def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.last_saved_date = timezone.now()
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'blog/post_edit.html', {'form': form})
