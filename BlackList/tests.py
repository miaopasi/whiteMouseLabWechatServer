# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone

from .models import Shop


class ShopMethodTests(TestCase):

    def test_was_update_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        old_question = Shop(update_date=time)
        self.assertIs(old_question.was_update_recently(), False)

    def test_was_update_recently_with_recent_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(hours=15)
        recent_question = Shop(update_date=time)
        self.assertIs(recent_question.was_update_recently(), True)