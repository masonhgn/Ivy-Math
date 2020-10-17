from django.http import HttpResponse
from django.shortcuts import render
from .models import postAlg
from .models import postPrec
from .models import postTrig
from .models import postCalc
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q





postsAlg = [
    {
        'author': 'mason',
        'title': 'first math post',
        'content': 'this is how to do dwqdwqdwqdstitution!!!!',
        'date_posted': 'september 20th, 2020',

    }, 
    {
        'author': 'mason2',
        'title': '2 math post',
        'content': 'this is4 to do dwqdwqdwqdstitution!!!!',
        'date_posted': 'september 20th, 2020',

    },
    {
        'author': 'mason344',
        'title': '321323 math post',
        'content': 'this is432434dwqdwqdstitution!!!!',
        'date_posted': 'september 40th, 2020',

    }
]





postsCalc = [
    {
        'author': 'mason3',
        'title': 'first calc post',
        'content': 'this is how to do u substitution!!!!',
        'date_posted': 'september 20th, 2020',

    }
]

def home(request):
    return render(request, 'boards/home.html')

class PostListViewAlg(ListView):
    model = postAlg
    template_name = 'boards/alg.html'
    context_object_name = 'postsAlg'
    ordering = ['-date_posted']


class PostListViewPrec(ListView):
    model = postPrec
    template_name = 'boards/prec.html'
    context_object_name = 'postsPrec'
    ordering = ['-date_posted']


class PostListViewTrig(ListView):
    model = postTrig
    template_name = 'boards/trig.html'
    context_object_name = 'postsTrig'
    ordering = ['-date_posted']


class PostListViewCalc(ListView):
    model = postCalc
    template_name = 'boards/calc.html'
    context_object_name = 'postsCalc'
    ordering = ['-date_posted']






#look at posts
class PostDetailViewAlg(DetailView):
    model = postAlg

class PostDetailViewTrig(DetailView):
    model = postTrig

class PostDetailViewPrec(DetailView):
    model = postPrec

class PostDetailViewCalc(DetailView):
    model = postCalc




#delete posts
class PostDeleteViewAlg(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postAlg
    success_url = '/alg'
    def test_func(self):
        postAlg = self.get_object()
        if self.request.user == postAlg.author:
            return True
        return False

class PostDeleteViewPrec(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postPrec
    success_url = '/prec'
    def test_func(self):
        postPrec = self.get_object()
        if self.request.user == postPrec.author:
            return True
        return False

class PostDeleteViewTrig(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postTrig
    success_url = '/trig'
    def test_func(self):
        postTrig = self.get_object()
        if self.request.user == postTrig.author:
            return True
        return False

class PostDeleteViewCalc(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = postCalc
    success_url = '/calc'
    def test_func(self):
        postCalc = self.get_object()
        if self.request.user == postCalc.author:
            return True
        return False

#create posts
class PostCreateViewAlg(LoginRequiredMixin, CreateView):
    model = postAlg
    fields = ['title', 'content', 'clip']

    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostCreateViewPrec(LoginRequiredMixin, CreateView):
    model = postPrec
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostCreateViewTrig(LoginRequiredMixin, CreateView):
    model = postTrig
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostCreateViewCalc(LoginRequiredMixin, CreateView):
    model = postCalc
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)



#update posts
class PostUpdateViewAlg(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = postAlg
    fields = ['title', 'content', 'clip']

    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def test_func(self):
        postAlg = self.get_object()
        if self.request.user == postAlg.author:
            return True
        return False

class PostUpdateViewPrec(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = postPrec
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def test_func(self):
        postPrec = self.get_object()
        if self.request.user == postPrec.author:
            return True
        return False

class PostUpdateViewTrig(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = postTrig
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def test_func(self):
        postTrig = self.get_object()
        if self.request.user == postTrig.author:
            return True
        return False

class PostUpdateViewCalc(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = postCalc
    fields = ['title', 'content', 'clip']
    def form_valid(self,form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def test_func(self):
        postCalc = self.get_object()
        if self.request.user == postCalc.author:
            return True
        return False







def contact(request):
    return HttpResponse("Contact Us")



def boardabout(request):
    return render(request, 'boards/about.html')


# Create your views here.



def alg(request):
    #if request.GET:
      #  query = request.GET['q']
   #     context['query'] = str(query)
    context1 = {
        'postsAlg': sorted(get_blog_queryset_alg(query)),
        'vlink': vlink,
    }
    return render(request, 'boards/alg.html', context1)
    



def prec(request):
    context2 = {
        'postsPrec': postPrec.objects.all(),
    }
    return render(request, 'boards/prec.html',context2)



def calc(request):
    context3 = {
        'postsCalc': postCalc.objects.all(),
    }
    return render(request, 'boards/calc.html', context3)



def trig(request):
    context4 = {
        'postsTrig': postTrig.objects.all(),
    }
    return render(request, 'boards/trig.html', context4)




def get_blog_queryset_alg(query=None):
        queryset = []
        queries = query.split(" ")
        for q in queries:
            postsAlg = PostAlg.objects.filter(Q(title__icontains=q) | Q(body__icontains=q)).distinct()

            for post in postsAlg:
                queryset.append(post)
        return list(set(queryset))