from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User
from .forms import EmailPostForm, Add_userForm
from django.core.mail import send_mail


def users_list(request):

    object_list = User.active.all()
    paginator=Paginator(object_list,18)
    page=request.GET.get('page')
    try:
        users=paginator.page(page)
    except PageNotAnInteger:
        users=paginator.page(1)
    except EmptyPage:
        users=paginator.page(paginator.num_pages)

    success = 0
    if request.method=='POST':
        adduser_form=Add_userForm(data=request.POST)

        if adduser_form.is_valid():
            new_user=adduser_form.save(commit=False)
            new_user.save()
            success=1
            return redirect('.')


    else:
        adduser_form=Add_userForm()

    return render(request,
                  'user_list/list.html',
                  {'page': page,
                   'users': users,
                  'users':users,
                   'adduser_form':Add_userForm,
                   'success':success,
                   })

def user_details(request, username):
    user = get_object_or_404(User, name=username)
    return render(request,
                  'user_list/detail.html',
                  {'user': user})


def link_message(requset,user_id):
    user=get_object_or_404(User, id=user_id,status='Active')
    sent=False
    if requset.method=='USER':
        form=EmailPostForm(requset.USER)
        if form.is_valid():
            cd=form.cleaned_data
            user_url=requset.build_absolute_uri(user.get_absolute_url())
            subject='{} ({}) recommend you reading "{}"'.\
                format(cd['name'],cd['email'],user.name)
            massage='read "{}" at'.\
                format(user.name)
            send_mail(subject, message, 'avibraun@gmail.com', ['avibraun@gmail.com'],
                      fail_silently=False)
            sent=True
        else:
            form=EmailPostForm()
        return render(requset,'user_list/user/share.html',
                      {'user':user,
                       'form':form,
                       'sent':sent})


def send_to_emaillist(request):
    send_mail('subject', 'message', 'avibraun@gmail.com', ['avibraun@gmail.com'],
              fail_silently=False)


