
from BlogEconomia.models import Blog
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BlogList(ListView):
    
    model= Blog
    template_name= "blog/blog.html"

class BlogDetalle(DetailView):
    model= Blog
    template_name= "blog/detail.html"

class BlogCreacion(CreateView, LoginRequiredMixin):
    model= Blog    
    template_name= "blog/blog_formulario.html"
    fields= ["Titulo", "Subtitulo", "Contenido", "categoria", "imagen","autor"]
    success_url = "/pages"


class BlogUpdate(UpdateView, LoginRequiredMixin):
    model= Blog    
    template_name= "blog/blog_form.html"
    fields= ["Titulo", "Subtitulo", "Contenido"]
    success_url = "/pages"

class BlogDelete(DeleteView):
    model= Blog    
    template_name= "blog/blog_confirm_delete.html"
    success_url = "/pages"