from django.core.mail import EmailMessage, send_mail,mail_admins,BadHeaderError
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
import requests
from django.core.cache import cache
from rest_framework.views import APIView
import logging 

logger = logging.getLogger(__name__)



class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self,request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})
        



# @cache_page(5*60)
# def say_hello(request):
    # response = requests.get('https://httpbin.org/delay/2')
    # data = response.json()
    # return render(request, 'hello.html', {'name': data})
    # key = 'httpbin_result'
    # if cache.get('key') is None:
    #     response = requests.get('https://httpbin.org/delay/2')
    #     data = response.json()
    #     cache.set(key,data)
    # return render(request, 'hello.html', {'name': cache.get(key)})

    # notify_customers.delay("Hello")

    # try:
        # send_mail('subject','message','info@moshbuy.com',['bob@moshbuy.com'])
        # mail_admins('subject','message',html_message='message')
        # message = EmailMessage('subject','message','from@moshbuy.com',['john@moshbuy.com'])
        # message.attach_file('playground/static/images/img1.jpg')
        # message.send()

    #     message = BaseEmailMessage(
    #         template_name = 'emails/hello.html',
    #         context= {'name':'Mosh'}
    #     )
    #     message.send(['john@moshbuy.com'])

    # except BadHeaderError:
    #     pass 


