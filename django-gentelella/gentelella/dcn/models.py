from django.db import models


class DCNCreateNewModel(models.Model):
    dcn_no = models.CharField(max_length=50)
    sap_change_no = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    dcn_received_date = models.DateField(null=True, blank=True)
    dcn_model = models.CharField(max_length=50)
    execute_type = models.CharField(max_length=50)
    dcn_type = models.CharField(max_length=5)
    dcn_title = models.CharField(max_length=50)
    effective_type = models.CharField(max_length=30, null=True, blank=True)
    documents = models.ImageField(default='')


class DCNPartsModel(models.Model):
    dcn_no = models.ForeignKey(DCNCreateNewModel, on_delete=models.SET_NULL, null=True)
    parent_part_no = models.CharField(max_length=25)
    part_no_old = models.CharField(max_length=25)
    part_no_new = models.CharField(max_length=25)
    part_description_old = models.CharField(max_length=25)
    part_description_new = models.CharField(max_length=25)
    usage_qty_old = models.CharField(max_length=25)
    usage_qty_new = models.CharField(max_length=25)
    stock_details_on_hand = models.CharField(max_length=25)
    stock_details_open_po = models.CharField(max_length=25)
    stock_details_total_stock = models.CharField(max_length=25)
    remarks = models.CharField(max_length=25)
    impl_date = models.DateField()
    impl_serial_no = models.CharField(max_length=25)
