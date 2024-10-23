from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task


# Task List View
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'  # Renamed to plural 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
            context['search_input'] = search_input
        return context


# Task Detail View
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task.html'


# Task Create View
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')  # Changed to 'tasks' (plural)

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = form.save()
        print(f"Task '{task.title}' created by {task.user}")  # Debugging
        return super(TaskCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Debugging
        return super().form_invalid(form)


# Task Update View
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')  # Changed to 'tasks' (plural)


# Task Delete View
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')  # Changed to 'tasks' (plural)


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('tasks')  # Changed to 'tasks' (plural)


# User Registration View
class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            print(f"User {user.username} created successfully")  # Debugging line
            login(self.request, user)
        else:
            print("User creation failed")  # Debugging line
        return super(RegisterPage, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # This will print the form errors
        messages.error(self.request, "Invalid form submission. Please try again.")
        #return super(RegisterPage, self).form_invalid(form)
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, **kwargs)
