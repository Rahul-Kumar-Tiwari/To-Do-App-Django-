from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse
from .models import list,mail_id
from .forms import ListForm
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
import time



def mail_sending(reciver_mail,task_list):
    def message(task_list):
        msglist = []
        for i in range(len(task_list)):
            msg = str((task_list[i]) + "\n")
            msglist.append(msg)
        return ("".join(msglist))
    subject = "Your pending Task in To Do List"
    from_email = "To Do App"
    to_email = [reciver_mail]
    task= message(task_list)
    message = """Welcome To the To Do App
Hey dear user some of your task is pending in To Do List.
please complete these task\n\n"""
    mail_message=message+task+"\n\n\n Thank You"
    #text_content = 'Welcome to To Do App'

    # message=EmailMultiAlternatives(subject=subject,body=text_content,from_email=from_email,to=to_email)
    # html_template=get_template('message.html').render()
    # message.attach_alternative(html_template,"text/html")
    # message.send()
    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=mail_message,fail_silently=False)

def home(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = list.objects.all
            messages.success(request, ('Item has been added to List'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})
def Email_Subscription(request):
    if request.method == "POST":
        mail =request.POST.get("mail")
        all_items = list.objects.all
        task_list = []
        for m in list.objects.filter(completed="False"):
            task_list.append(m.item)
        try:
            subsciption = mail_id(mail=mail)
            subsciption.save()
            mail_sending(subsciption.mail,task_list)
            # boom = 59
            # while boom > 0:
            #     time.sleep(1)
            #     print(boom)
            #     boom -= 1
            messages.success(request, ('Email subscription is sucessfully activated'))
            return render(request, 'home.html', {'all_items': all_items})
        
        except:
            return HttpResponse("Something went wrong with database")
    else:
        all_items = list.objects.all 
        return render(request, 'home.html', {'all_items': all_items})
    boom = 59
    while boom > 0:
        time.sleep(1)
        print(boom)
        boom -= 1

# def home1(request):
#     if request.method =='POST':
#         form = MailForm(request.POST or None)
#         if form.is_valid():
#             mail_items = request.POST.get("mail")
#             print("hi")
#             print(mail_items)
#             form.save()
#             #mail_items = list.objects.all
#             print(mail_items.filter(mail_items))
#             messages.success(request, ('Mail subsccription is sucessfully activated'))
#             return redirect('home')
#     else:
#         print("hello")
#         return redirect('home')
# def home(request):
#     if request.method == 'POST':
#         if 'task' in request.POST:
#             form = ListForm(request.POST, prefix='banned')
#             if form.is_valid():
#                 form.save()
#                 all_items = list.objects.all
#                 messages.success(request, ('Item has been added to List'))
#                 return render(request, 'home.html', {'all_items': all_items})
#             mail_form = MailForm(prefix='expected')
#         elif 'mailsubscription' in request.POST:
#             mail_form = MailForm(request.POST, prefix='expected')
#             if mail_form.is_valid():
#                 mail_items = request.POST.get("mail")
#                 print("hi")
#                 print(mail_items)
#                 mail_form.save()
#                 mail_items = list.objects.all
#                 print(mail_items.filter(mail_items))
#                 messages.success(request, ('Mail subsccription is sucessfully activated'))
#                 return redirect('home')
#             form =ListForm(prefix='banned')
#     else:
#         form = ListForm(prefix='banned')
#         mail_form = MailForm(prefix='expected')


def delete(request,list_id):
    item =list.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item Has Been Deleted"))
    return redirect('home')
def cross_off(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed =True
    item.save()
    return redirect('home')

def Uncross(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed =False
    item.save()
    return redirect('home')
def edit(request,list_id):
    if request.method =='POST':
        item = list.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to List'))
            return redirect('home')
    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})