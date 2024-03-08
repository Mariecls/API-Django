import os
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from bissextile.models import CallHistory

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bissextileapi.settings')
settings.configure()

class LeapYearAPITest(TestCase):
    def test_leap_year_endpoint(self):

        year = 2024
        response = self.client.get(reverse('is_leap_year', args=[year]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_leap_year'], True)


        call_history_entry = CallHistory.objects.latest('call_date')
        self.assertEqual(call_history_entry.endpoint, 'is_leap_year')
        self.assertEqual(call_history_entry.result, True)


        non_leap_year = 2021
        response = self.client.get(reverse('is_leap_year', args=[non_leap_year]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['is_leap_year'], False)


        call_history_entry = CallHistory.objects.latest('call_date')
        self.assertEqual(call_history_entry.endpoint, 'is_leap_year')
        self.assertEqual(call_history_entry.result, False)


        invalid_year = "invalid"
        response = self.client.get(reverse('is_leap_year', args=[invalid_year]))
        self.assertEqual(response.status_code, 400)


    def test_leap_years_in_range_endpoint(self):

        start_year = 2000
        end_year = 2020
        response = self.client.get(reverse('leap_years_in_range', args=[start_year, end_year]))
        self.assertEqual(response.status_code, 200)



        call_history_entry = CallHistory.objects.latest('call_date')
        self.assertEqual(call_history_entry.endpoint, 'leap_years_in_range')
        # Vérifiez que l'historique des appels contient les détails appropriés pour cet appel

    def test_call_history_endpoint(self):

        response = self.client.get(reverse('call_history'))
        self.assertEqual(response.status_code, 200)


        history_data = response.json()['history']
        dates = [entry['call_date'] for entry in history_data]
        self.assertEqual(dates, sorted(dates, reverse=True))
