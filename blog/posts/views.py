from django.shortcuts import render, redirect
from .models import Member
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
# dynamically generate url
from django.urls import reverse
from .forms import MemberForm
from django.contrib import messages


posts = [
    {
        "id": 0,
        "title": "let us ecplore python",
        "content": "You will create a backend application for a telemedicine "
        "service using Node.js, Express, and MySQL. This application will allow "
        "patients to manage their healthcare appointments and profiles, while doctors can"
        " manage their schedules."

    },
    {
        "id": 1,
        "title": "let us ecplore python",
        "content": "You will create a backend application for a telemedicine "
        "service using Node.js, Express, and MySQL. This application will allow "
        "patients to manage their healthcare appointments and profiles, while doctors can"
        " manage their schedules."

    },

    {
        "id": 2,
        "title": "Details about their specialization and availability.",
        "content": "YCreate a project structure for your application using Express.js.Define different routes (URLs) for accessing various features,"

    }
]

# Create your views here.


def home(req):
    html = ""

    # send data to template and it willl be a dic

    for post in posts:
        html += f"""
    <div>
    <a href="/post/{post['id']}/"><h1>{post['id']} - {post['title']}</h1></a>
    <p>{post['content']}</p>        
    </div>
    """

        getAllMembers = Member.objects.all

        return render(req, 'posts/index.html', {"posts": posts, 'all': getAllMembers})


def post(req, id):
    validId = False
    for post in posts:
        if post['id'] == id:
            postDic = post
            validId = True
            break
    if validId:
        return render(req, 'posts/post.html', {'postDict': postDic, })
    else:
        raise Http404()


def join(req):
    if req.method == 'POST':
        form = MemberForm(req.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.success(req, ('There is ia Error '))
            return redirect('join')

        messages.success(req, ('Sucessfully saved signup'))
        return redirect('home')

    else:
        return render(req, 'posts/join.html', {})
