from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirmPassword = request.POST['pass2']
        if password != confirmPassword:
            messages.warning(request, "Passwors is not matching??")
            return render(request,'signup.html')
        try:
            if User.object.get(username = email):
                messages.info(request,"Email is Taken")
                return render(request,'signup.html')

        except Exception as identifier:
            pass
            
        user = User.objects.create_user(name, email,password)
        user.is_active = False
        user.save()
        email_subject = "Activate Your Account"
        message = render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsefe_based64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
         # email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        # email_message.send()
        messages.success(request,f"Activate Your Account by clicking the link in your gmail {message}")
        return redirect('/auth/login/')
    return render(request,"signup.html")



class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        return render(request,'activatefail.html')

def handlelogin(request):
    if request.method=="POST":
        username = request.POST['emial']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username,password=userpassword)


        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successfully")       
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")   
            return redirect('/auth/login')
        return render(request,'login.html')




def handlelogout(request):
    logout(request)
    messages.ifno(request,"Logout Success")
    return redirect('/auth/login')          


class RequestResetEmailView(View):
    def get(self, request):
        return render(request,'requestResetEmail.html')



    def Post(self,request):
        email = request.POST['email']
        user = User.objects.filter(email = email) 
        if user.exists():
            email_subject = '[Reset Your Password]' 
            message = render_to_string('resetUserPassword.html',{
                'domain':'127.0.0.1:8000',
                 'uid': urlsafe_base64_decode(force_bytes(user[0].pk)),
                 'token':PasswordResetTokenGenerator().make_token(user[0])

            })  



            messages.info(request,f"We have sent to an email with the instructions on how to reset the password {message}")
            return render (request,"requestResetEmail.html")


class SetNewPasswordView(View):
      def get(self, request,uidb64,token):
        context={
            'uidb64':uidb64,
            'token':token
        }   
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.object.get(pk=user_id)
            if not PassworsResetTokenGenerator().check_token(user,token):
                messages.warning(request,"Password Reset Link is Invalid")
                return render(request,"requestResetEmail.html")   

        except DjangoUnicodeDecodeError as identifier:
            pass 
        return render(request,"setNewPassword.html") 

        def post(self,request, uidb64, token):
            context={
                'uidb64':uidb64,
                'token':token
            }       
            password = request.POST['pass1']
            confirm_password = request.POST['pass2']
            if password!= confirm_password:
                messages.warning(request,"Password is not Matching ")
                return render(request,"setNewPassword.html",context)

            try:
                user_id = force_text(urlsafe_base64_decode(uidb64))
                user= User.objects.get(pk=user.id)
                user.set_password(password)
                user.save()
                messages.success(request,"Password Reset Success Please Login with New Password")
                return redirect('auth/login')

            except DjangoUnicodeDecodeError as identifier:
                message.error(request,"something went wrong ")
                return render(request,"setNewPassword.html",context)

            return render(request,"setNewPassword.html",context)    

         
