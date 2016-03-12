from django.shortcuts import render_to_response
from django.template.context import RequestContext, Context
from django.core.mail import send_mail
from django.template.loader import render_to_string

from models import *
# Create your views here.
def index(request):
    args = {}
    if request.method == 'POST':
        cf = MessageForm(request.POST)
        if cf.is_valid():
            message = cf.save()
            args['message_valid'] = True
            welcomeEmail(message)
            notifyEmail(message)
            '''
            send_mail('Thanks for contacting the Code Coop!',
                          "We got your message! We'll get back to you as soon as we can.",
                          'from-example@email.com',
                          [message.email],
                          fail_silently=False
                          )
            send_mail(message.name + ' just sent us a message!',
                      message.message,
                      'admin-example@email.com',
                      ['to-example@email.com'],
                      fail_silently=False
                      )
            '''
        else:
            args['message_valid'] = False
    args['messageform'] = MessageForm()
    return render_to_response('contact/index.html', RequestContext(request,args))

def welcomeEmail(message):
    d = Context({ 'message': message })
    msg_plain = render_to_string('email/welcome.txt', d)
    msg_html = render_to_string('email/welcome.html', d)

    send_mail(
        'Thanks for the message!',
        msg_plain,
        'from-example@email.com',
        [message.email],
        html_message=msg_html,
    )

def notifyEmail(message):
    d = Context({ 'message': message })
    msg_plain = render_to_string('email/notification.txt', d)
    msg_html = render_to_string('email/notification.html', d)

    send_mail(
        message.name + ' sent us a message!',
        msg_plain,
        'admin-example@email.comp',
        ["to-example@email.com"],
        html_message=msg_html,
    )
