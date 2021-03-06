import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModeTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        #import pdb; pdb.set_trace()
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_qestion = Question(pub_date=time)
        self.assertIs(old_qestion.was_published_recently(),False)

    def test_was_published_recently_with_recently_question(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)
