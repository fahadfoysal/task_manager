from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, DetailView,
CreateView, UpdateView, DeleteView
)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task, TaskImage
from .forms import TaskForm, TaskImageForm

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        # Implement search by title
        title_query = self.request.GET.get('title')
        if title_query:
            tasks = tasks.filter(title__icontains=title_query)
        # Implement filters
        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            tasks = tasks.filter(created_on__date=creation_date)
        #for due date
        due_date = self.request.GET.get('due_date')
        if due_date:
            tasks = tasks.filter(due_date__date=due_date)
        #for priority
        priority = self.request.GET.get('priority')
        if priority:
            tasks = tasks.filter(priority=priority)
        #for stauts
        is_completed = self.request.GET.get('is_completed')
        if is_completed is not None:
            is_completed = bool(is_completed.lower() == 'true')
            tasks = tasks.filter(is_completed=is_completed)

        return tasks
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/tasks_detail.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreate,self).form_valid(form)
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/tasks_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        messages.success(self.request, "The task was Updated successfully.")
        return super(TaskUpdate,self).form_valid(form)
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/tasks_delete_confirmation.html'
    success_url = reverse_lazy('task_list')


class TaskImageUpload(View):
    template_name = 'tasks/tasks_image_upload.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskImageForm()
        return render(request, self.template_name, {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.task = task
            image.save()
            messages.success(self.request, "Image uploaded successfully")
            return redirect('task_detail', pk=task.pk)
        return render(request, self.template_name, {'form': form, 'task': task})
    
class TaskImageDelete(View):
        def get(self, request, t_id, i_id):
            task_image = get_object_or_404(TaskImage, pk=i_id)
            task_image.delete()
            messages.success(self.request, "Image Deleted successfully")
            return redirect('task_detail', pk=t_id)