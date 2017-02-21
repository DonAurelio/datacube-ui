# Copyright 2016 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. All Rights Reserved.
#
# Portion of this code is Copyright Geoscience Australia, Licensed under the
# Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License
# at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# The CEOS 2 platform is licensed under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django import forms

import datetime

from data_cube_ui.models import Baseline

"""
File designed to house the different forms for taking in user input in the web application.  Forms
allow for input validation and passing of data.  Includes forms for creating Queries to be ran.
"""

# Author: AHDS
# Creation date: 2016-06-23
# Modified by:
# Last modified date:



class DataSelectForm(forms.Form):
    """
    Django form to be created for selecting information and validating input for:
        result_type
        band_selection
        title
        description
    """

    title = forms.CharField(widget=forms.HiddenInput())
    description = forms.CharField(widget=forms.HiddenInput())

    baseline_length = forms.ChoiceField(help_text='Select the number of acquisitions that will be used to create the baseline',
        label="Baseline Length (Acquisitions):",
        choices=[(number, number) for number in range(1,11)],
        widget=forms.Select(attrs={'class': 'field-long tooltipped'}))

    def __init__(self, *args, **kwargs):
        super(DataSelectForm, self).__init__(*args, **kwargs)

        baseline_list = [(baseline.baseline_id, baseline.baseline_name) for baseline in Baseline.objects.all()]

        self.fields["baseline_selection"] = forms.ChoiceField(
            help_text='Select the method by which the baseline will be created.',
            label="Baseline Method:",
            choices=baseline_list,
            widget=forms.Select(attrs={'class': 'field-long tooltipped'}))


class AreaExtentForm(forms.Form):
    """
    Django form for taking geospatial information for Query requests:
        latitude_min
        latitude_min
        longitude_min
        longitude_max
    """
    two_column_format = True

    latitude_min = forms.FloatField(label='Min Latitude', widget = forms.NumberInput(attrs={'class': 'field-divided', 'step': "any", 'required': 'required'}))
    latitude_max = forms.FloatField(label='Max Latitude', widget = forms.NumberInput(attrs={'class': 'field-divided', 'step': "any", 'required': 'required'}))
    longitude_min = forms.FloatField(label='Min Longitude', widget = forms.NumberInput(attrs={'class': 'field-divided', 'step': "any", 'required': 'required'}))
    longitude_max = forms.FloatField(label='Max Longitude', widget = forms.NumberInput(attrs={'class': 'field-divided', 'step': "any", 'required': 'required'}))
 
    def __init__(self, satellite=None, *args, **kwargs):
        super(AreaExtentForm, self).__init__(*args, **kwargs)

class TwoDateForm(forms.Form):
    two_column_format = True

    old = forms.ChoiceField(help_text='Select the date of a historic acquisition.',
        label="t1 (old date):",
        choices=[(number, number) for number in range(1999,2017)],
        widget=forms.Select(attrs={'class': 'field-long tooltipped'}))

    new = forms.ChoiceField(help_text='Select the date of a new acquisition',
        label="t2 (new date):",
        choices=[(number, number) for number in range(1999,2017)],
        widget=forms.Select(attrs={'class': 'field-long tooltipped'}))

    def __init__(self, satellite=None, *args, **kwargs):
        super(TwoDateForm, self).__init__(*args, **kwargs)

class ProductSelectionForm(forms.Form):
    two_column_format = False


    product_setting = forms.ChoiceField(help_text='Select your prefered product.',
        label="product:",
        choices=[ ('change','Coastal Change')],
        widget=forms.Select(attrs={'class': 'tooltipped'}))

    def __init__(self, satellite=None, *args, **kwargs):
        super(ProductSelectionForm, self).__init__(*args, **kwargs)