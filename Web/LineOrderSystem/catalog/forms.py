import datetime

from django import forms
from django.contrib.admin.widgets import AdminDateWidget 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'


class UsernameForm(forms.Form):
    # Username = forms.CharField(required=False, label='Username')
    start_date = forms.DateField(widget = DateInput(), label='開始時間')
    end_date = forms.DateField(widget = DateInput(), label='結束時間')
    # date = forms.CharField(initial = '本日',
    # widget = forms.widgets.Select(choices=(('本日','本日'),('一周','一周'),('一個月','一個月')  )))
    
    
    #  pwd = forms.CharField(
    #     max_length=12,
    #     min_length=6,
    #     error_messages={'required':'not null'}
    # )

class CustomerForm(forms.Form):
    Username = forms.CharField(required=False, label='Username')
    start_date = forms.DateField(widget = DateInput(), label='開始時間')
    end_date = forms.DateField(widget = DateInput(), label='結束時間')
    # date = forms.CharField(initial = '昨日',
    # widget = forms.widgets.Select(choices=(('昨日','昨日'),('前三日','前三日'),('一周','一周'),('一個月','一個月')  )))