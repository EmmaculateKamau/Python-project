from django.shortcuts import render
from .models import User
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class MemberListView(ListView):
    model = User
    template_name = 'Emmaculate/index.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        query=self.request.GET.get('q')
        if query:
            return User.objects.filter(name__icontains=query)| User.objects.filter(primary__icontains=query)
        else:
            return User.objects.all()

class MemberCreateView(CreateView):
     model = User
     fields = '__all__'
class MemberUpdateView(UpdateView):
    model = User
    fields = '__all__'
class MemberDeleteView(DeleteView):
    model = User
    success_url = '/'