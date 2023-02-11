from django.conf import settings
from django.core.mail import send_mail
 
def send_mail_token(email,token):
    try:
        subject="Email Verfication"
        message=f'CLICK TO VERIFY http://127.0.0.1:8000/verify/{token}'
        email_from=settings.EMAIL_HOST_USER
        reciepient_list=[email,]
        send_mail(subject,message,email_from, reciepient_list,fail_silently=False )
    except Exception as e:
        return False
    return True
