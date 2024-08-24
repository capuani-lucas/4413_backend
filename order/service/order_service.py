
import os
from backend_4413 import settings
from backend_4413.mail.sendgrid_client import SendgridClient
from django.template.loader import render_to_string
from order.models.Order import Order

def get_total_price(orders: list[Order]) -> float:
  total_price = 0
  for order in orders:
    total_price += order.price
  return total_price

def send_order_confirmation_email(user_email, orders: list[Order]):
  sendgrid_client = SendgridClient()
  html_content = render_to_string('order_confirmation.html', {
    'orders': orders,
    'total_price': get_total_price(orders)
  })

  sendgrid_client.send_email(
    to=user_email,
    subject='Order Confirmation',
    html_content=html_content
  )
