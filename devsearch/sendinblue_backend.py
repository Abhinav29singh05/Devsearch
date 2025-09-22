# sendinblue_backend.py

import os
from sib_api_v3_sdk import Configuration, ApiClient, TransactionalEmailsApi
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage
from decouple import config

class SendinblueBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = os.getenv('SENDINBLUE_API_KEY') or config('SENDINBLUE_API_KEY', default='') 
        
        # Configure API key authorization
        configuration = Configuration()
        configuration.api_key['api-key'] = self.api_key
        
        # Create API client instance
        self.api_instance = TransactionalEmailsApi(ApiClient(configuration))

    def send_messages(self, email_messages):
        success = 0
        for message in email_messages:
            # Create the email data structure
            email_data = {
                "to": [{"email": to} for to in message.to],
                "sender": {"email": message.from_email},
                "subject": message.subject,
                "textContent": message.body
            }

            try:
                response = self.api_instance.send_transac_email(email_data)
                success += 1
            except Exception as e:
                self._handle_error(e)
        return success

    def _handle_error(self, error):
        print("Error sending email:", str(error))
        raise Exception("Email sending failed")
