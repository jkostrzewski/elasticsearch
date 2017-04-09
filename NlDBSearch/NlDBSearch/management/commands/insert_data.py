from django.core.management import BaseCommand
from NlDBSearch.models import Entry
import random
from django.db import transaction
    
class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
    	for i in range(1000):
    		e = Entry()
    		e.cat = "cat"+''.join([random.choice('ABCDEFGHIJKLMNOPRSTUWXZ') for _ in range(5)])
    		e.act = "act"+''.join([random.choice('1234567890') for _ in range(5)])
    		e.utt = "utt"+''.join([random.choice('ABCDEFGHIJKLMNOPRSTUWXZ'.lower()) for _ in range(5)])
    		e.save()