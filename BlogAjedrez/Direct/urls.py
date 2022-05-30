from django.urls import path
from Direct.views import PeopleWeCanMessage, NewMessage, Inbox

urlpatterns = [
    path('', Inbox, name="Inbox"),
    path('view_people', PeopleWeCanMessage, name="PeopleWeCanMessage"),
    path('new/<pk>', NewMessage.as_view(), name="NewMessage"),
]