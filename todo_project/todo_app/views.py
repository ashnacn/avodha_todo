from django.shortcuts import render, redirect
from . models import task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django . urls import reverse_lazy
from . forms import Todoforms
class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')
class taskupdate(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
class tasklistview(ListView):
    model=task
    template_name = 'task_view.html'
    context_object_name = 'obj1'
class taskdetailview(DetailView):
    model=task
    template_name = 'task_view.html'
    context_object_name = 'i'
def home(request):
    return render(request,'home.html')
def task_view(request):
    obj1=task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date=request.POST.get('date')
        obj= task(name=name, priority=priority,date=date)
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})

def delete(request,task_id):
    task1=task.objects.get(id=task_id)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html',{'task1':task1})


def update(request,id):
    task1=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task1':task1,'form':form})

