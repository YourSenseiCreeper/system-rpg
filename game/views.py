from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# def oops(request):
#     args = {'user': request.user}
#     return render(request, 'memes/oops.html', args)

from .forms import DialogueForm
from .models import Dialogue


def index(request):
    return render(request, 'index.html', None)

def dashboard(request):
    args = {'data': Dialogue.objects.all()}
    if request.method == "GET":
        return render(request, 'dashboard.html', args)


def editor(request, dialogue_id=None):
    if request.method == 'POST':
        form = DialogueForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', None)
    if request.method == 'GET':
        if dialogue_id is None:
            return render(request, 'editor.html', {'form': DialogueForm()})
        else:
            dialogue = Dialogue.objects.get(pk = dialogue_id)
            form = DialogueForm(instance = dialogue)
            return render(request, 'editor.html', {'form': form})


def user(request, user):
    user = User.objects.get(username=user)
    if user is None:
        return render(request, 'game/user.html', None)
    else:
        args = {'user': request.user, 'user_profile': user, 'memes': None}
        return render(request, 'game/user.html', args)


def logout_view(request):
    logout(request)
    return redirect('game:index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'game/register.html', args)


# @login_required(login_url="/login/")
def meme_add(request):
    # if this is a POST request we need to process the form data
    # args = {'form': AddMeme(), 'user': request.user}
    # if request.method == 'POST' and request.user is not None:
    #     form = AddMeme(request.POST, request.FILES)
    #     if form.is_valid():
    #         internal = form.save(commit=False)
    #         internal.author = request.user
    #         internal.save()
    #         return redirect('memes:index')
    # if a GET (or any other method) we'll create a blank form
    return render(request, 'game/add.html', None)


def meme_like(request):
    # if request.method == 'POST':
    #     meme = Meme.objects.get(pk=request.POST.get('meme_id'))
    # 	# is_liked = False
    #     if meme.likes.filter(id=request.user.id).exists():
    #         meme.likes.remove(request.user)
    #         meme.likes_number = meme.likes_number -1
    #     else:
    #         meme.likes.add(request.user)
    #         meme.likes_number = meme.likes_number +1
    #
    #     meme.save()
    return redirect('/')


def meme_dislike(request):
    # meme = Memes.objects.get(pk=request.POST.get('meme_id'))
    # meme.dislikes.add(request.user)
    return redirect('/')
