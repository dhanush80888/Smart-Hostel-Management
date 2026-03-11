import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_hostel.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from hostel.models import ChatMessage

print("\n" + "="*70)
print("CHATBOT FLOW TEST")
print("="*70 + "\n")

# create test client
client = Client()

# login as a student (assumes setup_data has created student1)
print("Logging in as student1...")
resp = client.post(reverse('login'), {'username': 'student1', 'password': 'pass123'}, follow=True)
if resp.status_code == 200:
    print("✓ Logged in")
else:
    print("✗ Login failed, cannot test chatbot")

# ensure no preexisting chat messages
ChatMessage.objects.filter(user__username='student1').delete()

# send a chat request
print("Sending message 'hello' to chatbot endpoint...")
resp = client.post(reverse('hostel_chatbot'), {'message': 'hello'})

print("Response status code:", resp.status_code)
try:
    data = resp.json()
    print("JSON returned:", data)
    if 'reply' in data:
        print("✓ Reply field present")
    else:
        print("✗ No reply field")
except Exception as e:
    print("✗ Response was not valid JSON", e)

# check database record saved
msgs = ChatMessage.objects.filter(user__username='student1')
print("Total messages saved:", msgs.count())
for m in msgs:
    print(f" - {m.is_from_user and 'user' or 'bot'}: {m.message or m.response}")

print("\n" + "="*70)
print("CHATBOT TEST COMPLETE")
print("="*70 + "\n")
