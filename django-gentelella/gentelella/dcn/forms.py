from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from gentelella import settings

from .models import DCNCreateNewModel, DCNPartsModel


class DCNCreateForm(forms.Form):
    dcn_no = forms.CharField(max_length=50)
    sap_change_no = forms.CharField(max_length=50)
    segment = forms.CharField(max_length=50)
    dcn_received_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    dcn_model = forms.CharField(max_length=50)
    execute_type = forms.CharField(max_length=50)
    dcn_types = (('yoj', 'YOJ'), ('int', 'INT'))
    dcn_type = forms.ChoiceField(choices=dcn_types, widget=forms.RadioSelect, label='dcn_type')
    dcn_title = forms.CharField(max_length=50)
    CHOICES = [('FromTP', 'From TP'), ('FromMPStart', 'From MP Start'), ('OnlyforTP', 'Only for TP'),
               ('InprogressofMP', 'Inprogress of MP')]
    effective_type = forms.ChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = DCNCreateNewModel
        fields = ['dcn_no', 'sap_change_no', 'segment', 'dcn_received_date', 'dcn_model',
                  'execution_type', 'dcn_title', 'effective_type', 'documents']


class DCNPartsForm(forms.ModelForm):
    parent_part_no = forms.CharField(max_length=25, required=False)
    part_no_old = forms.CharField(label='Old Part No', max_length=25, required=False)
    part_no_new = forms.CharField(label='New Part No', max_length=25, required=False)
    part_description_old = forms.CharField(label='Old Part Description', max_length=25, required=False)
    part_description_new = forms.CharField(label='New Part Description', max_length=25, required=False)
    usage_qty_old = forms.CharField(max_length=25, required=False)
    usage_qty_new = forms.CharField(max_length=25, required=False)
    stock_details_on_hand = forms.CharField(max_length=25, required=False)
    stock_details_open_po = forms.CharField(max_length=25, required=False)
    stock_details_total_stock = forms.CharField(max_length=25, required=False)
    remarks = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    impl_date = forms.DateField(label='Implementation Date', required=False)
    impl_serial_no = forms.CharField(label='Implementation Serial No', max_length=25, required=False)

    class Meta:
        model = DCNPartsModel
        fields = ['dcn_no', 'parent_part_no', 'part_no_old', 'part_no_new',
                  'part_description_old', 'part_description_new', 'usage_qty_old', 'usage_qty_new',
                  'stock_details_on_hand', 'stock_details_open_po', 'stock_details_total_stock',
                  'remarks', 'impl_date', 'impl_serial_no']
        widgets = {'dcn_no': forms.HiddenInput()}