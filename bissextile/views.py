from django.http import JsonResponse
from django.utils import timezone
from bissextile.models import CallHistory

def is_leap_year(request, year):
    is_leap_year_result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    current_date = timezone.now()

    CallHistory.objects.create(
        endpoint='is_leap_year',
        result=is_leap_year_result,
        call_date=current_date
    )

    return JsonResponse({"is_leap_year": is_leap_year_result})

def leap_years_in_range(request, start_year, end_year):
    leap_years_list = [year for year in range(start_year, end_year + 1) if
                       (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
    current_date = timezone.now()

    CallHistory.objects.create(
        endpoint='leap_years_in_range',
        result=leap_years_list,
        call_date=current_date
    )

    return JsonResponse({"leap_years": leap_years_list})

def call_history(request):
    history = CallHistory.objects.all().order_by('-call_date')

    history_data = []
    for entry in history:
        result_display = entry.result if isinstance(entry.result, bool) else 'vrai' if entry.result == 'True' else entry.result
        entry_data = {
            'endpoint': entry.endpoint,
            'result': result_display,
            'call_date': entry.call_date.strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        history_data.append(entry_data)

    return JsonResponse({"history": history_data})

