from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import AccountForm, myform

# Create your views here.

# def MyFormView(request):
#     if request.method == "POST":
#         m_form = myform(request.POST)
#         a_form = AccountForm(request.POST)
#         if m_form.is_valid() and a_form.is_valid():
#             user = m_form.save()
#             if user.is_active == True:
#                 a_form.instance.user
#                 a_form.save()
#                 return redirect('/')
            
#             # else:
#             #     return render(request, 'app/index.html', {'m_form':m_form, 'a_form':a_form})
#             # return HttpResponse('home')
#         else:
         
#             m_form : myform()
#             a_form : AccountForm()
#         context = {
#                 'm_form' : m_form,
#                 'a_form': a_form
#                 }
#         return HttpResponse(context)
        # return render(request, 'app/index.html',context)

def MyFormView(request):
    if request.method == 'POST':
        m_form = myform(request.POST)
        a_form = AccountForm(request.POST)
        if m_form.is_valid() and a_form.is_valid():
            user = m_form.save()
            user.is_active = True
            a_form.instance.user = user
            a_form.save()
            messages.success(request,f'Your Account Has Been created')
            return redirect('/')
    else:
        m_form = myform()
        a_form = AccountForm()
    return render(request, 'app/index.html', {'m_form':m_form, 'a_form':a_form})



        
