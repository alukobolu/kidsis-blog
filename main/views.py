from re import T
from django.shortcuts import render,redirect
from .models import Topic,Responses
# Create your views here.
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, ListView

class Home(ListView):
    template_name = 'index.html'
    model = Topic
    context_object_name = 'topics'
    paginate_by = 20
    

class Response(View):
    def get(self,request,id):
        top = Topic.objects.get(topic_id = id)
        context = {
            'topic': top.name,
            'topic_id': top.topic_id,
        }
        template_name = 'response.html'
        return render(request, template_name,context)
    def post(self,request,id):
        res = request.POST['response']
        top = Topic.objects.get(topic_id = id)
        instance = Responses()
        instance.topic = top
        instance.comment = res
        instance.save()
        messages.success(request, 'Your Story has been recieved. Thank you for sharing')
        return redirect('home')

class  Dashboard(ListView):
    template_name = 'dashboard.html'
    model = Topic
    context_object_name = 'topics'
    paginate_by = 20

class MakeTopics(View):
    def get(self,request):
        context = {
            'action':'Add',
            'topic': "",
        }
        template_name = 'edit.html'
        return render(request, template_name,context)

    def post(self,request):
        top = request.POST['topic']
        instance = Topic()
        instance.name = top
        instance.save()
        messages.success(request, 'Topic has been created')
        return redirect('dashboard')

class ListResponses(View):
    def get(self,request,id):
        top = Topic.objects.get(topic_id = id)
        res = Responses.objects.filter(topic = top)
        context = {
            'topic': top.name,
            'responses': res,
        }
        template_name = 'response_list.html'
        return render(request, template_name,context)

class EditTopics(View):
    def get(self,request,id):
        top = Topic.objects.get(topic_id = id)
        context = {
            'action':'Edit',
            'topic': top.name,
        }
        template_name = 'edit.html'
        return render(request, template_name,context)

    def post(self,request,id):
        top = request.POST['topic']
        instance = Topic.objects.get(topic_id = id)
        instance.name = top
        instance.save()
        messages.success(request, 'Topic has been edited')
        return redirect('dashboard')

class DeleteTopic(View):
    def get(self,request,id):
        instance = Topic.objects.get(topic_id = id)
        instance.delete()
        messages.success(request, 'Topic has been deleted')
        return redirect('dashboard')