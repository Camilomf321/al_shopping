from al_shopping.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    """
    Task to send a email notification when an order is successfully created
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order_id}'
    message = f'Thanks for your purchasing , Your order number is {order.id}'
    mail_sent = send_mail(subject, message, 'aldatheproducer@gmail.com', [order.email])
    return mail_sent
