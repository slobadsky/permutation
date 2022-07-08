from django.shortcuts import render,HttpResponseRedirect,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import damndePermutForm
from myapp.models import Permutation
from xhtml2pdf import pisa
from django.template.loader import get_template
from datetime import date
import datetime,time

# Create your views here.

@login_required(redirect_field_name=None)
def home(request):
    context={}
    context={
        'active_page':'home-page',
        'form':damndePermutForm(request.POST or None),
        'users':User.objects.exclude(username= u'admin'),
    }
    form=damndePermutForm(request.POST or None)
    if request.method == 'POST': 
        print(User.objects.get(id=request.POST['permut_acceptant']))
        if form.is_valid():
            x=form.save(commit=False)
            x.permut_start_datetime=request.POST['permut_start_datetime']
            x.permut_acceptant_start_datetime=request.POST['permut_acceptant_start_datetime']
            x.permut_end_time=request.POST['permut_end_time']
            x.permut_acceptant_end_time=request.POST['permut_acceptant_end_time']
            x.permut_demandant_id=User.objects.filter(username=request.user).values_list('id', flat=True)[0]
            x.permut_acceptant_id=User.objects.filter(id=request.POST['permut_acceptant']).values_list('id', flat=True)[0]
            x.permut_motif=request.POST['permut_motif']
            x.save()
            messages.success(request, "La demande a bien été envoyée")                
            return HttpResponseRedirect('/')
            
            
            
    return render(request, 'permutation/index.html',context)

@login_required(redirect_field_name=None)
def mes_demandes(request):
    context={}
    context={
        'active_page':'mes_demandes',
        'users':User.objects.all(),
        'demandes':Permutation.objects.filter(permut_demandant_id=User.objects.filter(username=request.user).values_list('id', flat=True)[0])
    }
    return render(request, 'permutation/mes-demandes.html',context)


@login_required(redirect_field_name=None)
def acceptation(request):
    context={}
    context={
        'active_page':'acceptation',
        'demandes':Permutation.objects.filter(permut_acceptant_id=request.user)
    }
    return render(request, 'permutation/acceptation.html',context)

def html_to_pdf_view(request,unique_ref): 
    
    #template pdf path
    template_path = 'permutation/pdf-template.html'
    
    #collect user info
    user_info=Permutation.objects.get(permut_unique_ref=unique_ref)
    #recover all the datas to fetch into the template page
    context = {
        
        'permutations':user_info,
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    
    #create file name
    temp_date=datetime.datetime.strptime(str(user_info.permut_start_datetime), '%Y-%m-%d %H:%M:%S+00:00').strftime('%Y_%m_%d_%H_%M_%S')
    pdf_filename="permut_"+str(user_info.permut_demandant)+'_'+str(user_info.permut_acceptant)+'_'+temp_date+str(int(time.time()*1000.0)).replace(".", "_")
    #pdf_filename='test'
    response['Content-Disposition'] = 'filename="'+pdf_filename+'.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    
    return response


@login_required(redirect_field_name=None)
def update_permutation_demande(request,upd_ref):
    data=get_object_or_404(Permutation,permut_unique_ref=upd_ref)
    context={}
    context={
        'active_page':'mes_demandes',
        'data':data,
        'form':damndePermutForm(request.POST  or None, data),
        'users':User.objects.exclude(username= u'admin'),
    }
    
    if request.method == 'POST':
         
        Permutation.objects.filter(
            permut_unique_ref=upd_ref,
            ).update(
                permut_start_datetime=request.POST['permut_start_datetime'],
                permut_acceptant_start_datetime=request.POST['permut_acceptant_start_datetime'],
                permut_end_time=request.POST['permut_end_time'],
                permut_acceptant_end_time=request.POST['permut_acceptant_end_time'],
                permut_acceptant_id=User.objects.get(id=request.POST['permut_acceptant']),
                permut_motif=request.POST['permut_motif'],
            )
        messages.success(request, "La modification a bien été prise en compte")                
        return HttpResponseRedirect('/mes-demandes')
        
    return render(request, 'permutation/update-permutation-demande.html',context)

@login_required(redirect_field_name=None)
def update_permutation_accept(request,upd_ref):
    data=get_object_or_404(Permutation,permut_unique_ref=upd_ref)
    context={}
    context={
        'active_page':'acceptation',
        'data':data,
        'form':damndePermutForm(request.POST  or None, data),
        'users':User.objects.exclude(username= u'admin'),
    }
    
    if request.method == 'POST':
         
        Permutation.objects.filter(
            permut_unique_ref=upd_ref,
            ).update(
                permut_accepted=True,
            )
        messages.success(request, "La modification a bien été prise en compte")                
        return HttpResponseRedirect('/acceptation')
        
    return render(request, 'permutation/update-permutation-accept.html',context)


@login_required(redirect_field_name=None)
def delete_permutation_demande(request,upd_ref):
    data=get_object_or_404(Permutation,permut_unique_ref=upd_ref)
    data.delete()
    messages.success(request, "La demande a bien été supprimée.")
    context={}
    context={
        'active_page':'mes_demandes',
    }
    
    return render(request, 'permutation/mes-demandes.html',context)

@login_required(redirect_field_name=None)
def liste_salaries(request):
    context={}
    context={
        'active_page':'liste-salaries',
        'users':User.objects.all().exclude(username='admin')
    }
    return render(request, 'permutation/liste-salaries.html',context)
    
    
def login_page(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Manual code to Check whether username is valid or not
        try:
            myuser = User.objects.get(username=username)
        except:
            myuser = False

        if myuser == False:
            mypass = False
        else:
            mypass = myuser.check_password(password)
        
        
        user = authenticate(username=username, password=password)
               
        if myuser != False:
            if user is not None:            
                login(request, user)
                
                #request.session.set_expiry(10) # session expire after 10 sec
                #messages.success(request, "You have Successfully Logged in")
                return HttpResponseRedirect('/')                    
            else:
                messages.error(request, "Le mot de passe incorrect")                
                return HttpResponseRedirect('/login')
        else:
            messages.error(request, "L'identifiant incorrect")
            return HttpResponseRedirect('/login')
       
            
            

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'permutation/login-page.html',{}) 

def logout_page(request):
    logout(request)
    return redirect('/login')