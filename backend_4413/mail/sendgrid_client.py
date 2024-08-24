import environ
import sendgrid

env = environ.Env()

class SendgridClient(object):

  _instance = None
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(SendgridClient, cls).__new__(cls, *args, **kwargs)
    return cls._instance

  def __init__(self):

    if env("SENDGRID_ENABLED") != 'True':
      return

    self.sendgrid = sendgrid.SendGridAPIClient(
      api_key=env('SENDGRID_API_KEY')
    )

  def send_email(self, to, subject, html_content):
    if env("SENDGRID_ENABLED") != 'True':
      print('Sendgrid is not enabled')
      print('Email to:', to)
      print('Subject:', subject)
      print('Content:', html_content)
      return

    message = sendgrid.Mail(
      from_email=env('SENDGRID_FROM_EMAIL'),
      to_emails=to,
      subject=subject,
      html_content=html_content
    )

    try:
      response = self.sendgrid.send(message)
      return response
    except Exception as e:
      print(e)
      return None

