from django.shortcuts import render
from django.views.generic import ListView
from django.core.files.storage import FileSystemStorage

from .forms import DCNCreateForm, DCNPartsForm
from .models import DCNCreateNewModel, DCNPartsModel

class DCNListView(ListView):
    model = DCNCreateNewModel
    queryset = DCNCreateNewModel.objects.all()
    template_name = 'dcn/create_new.html'


class DCNPartsView(ListView):
    model = DCNPartsModel
    queryset = DCNPartsModel.objects.all()
    template_name = 'app/addrows.html'


def add_create(request):
    if request.method == 'POST':
        form = DCNCreateForm(request.POST)
        if True:
            dcn_no = request.POST['dcn_no']
            sap_change_no = request.POST['sap_change_no']
            segment = request.POST['segment']
            dcn_received_date = request.POST['dcn_received_date']
            dcn_model = request.POST['dcn_model']
            execute_type = request.POST['execute_type']
            dcn_type = request.POST['dcn_type']
            dcn_title = request.POST['dcn_title']

            upload_file = request.FILES['documents']
            print("File name:", upload_file.name)
            print("File size:", upload_file.size)
            fs = FileSystemStorage(location='media/documents/'+dcn_no+'/')
            fs.save(upload_file.name, upload_file)

            info = DCNCreateNewModel(dcn_no=dcn_no, sap_change_no=sap_change_no, segment=segment, dcn_received_date=dcn_received_date,
                                     dcn_model=dcn_model, execute_type=execute_type, dcn_type=dcn_type, dcn_title=dcn_title)
            info.save()
            context = {'form': DCNPartsForm(), 'info': info}
            return render(request, 'dcn/addrows.html', context)
    else:
        form = DCNCreateForm()

    return render(request, 'dcn/create_new.html', {'form': form})


def dcn_parts(request):
    if request.method == 'POST':
        if True:
            dcn_no_id = request.POST['dcn_no_id']
            parent_part_no = request.POST.getlist('parent_part_no')
            part_no_old = request.POST.getlist('part_no_old')
            part_no_new = request.POST.getlist('part_no_new')
            part_description_old = request.POST.getlist('part_description_old')
            part_description_new = request.POST.getlist('part_description_new')
            usage_qty_old = request.POST.getlist('usage_qty_old')
            usage_qty_new = request.POST.getlist('usage_qty_new')
            stock_details_on_hand = request.POST.getlist('stock_details_on_hand')
            stock_details_open_po = request.POST.getlist('stock_details_open_po')
            stock_details_total_stock = request.POST.getlist('stock_details_total_stock')
            remarks = request.POST.getlist('remarks')
            impl_date = request.POST.getlist('impl_date')
            impl_serial_no = request.POST.getlist('impl_serial_no')
            for i in range(len(parent_part_no)):
                info1 = DCNPartsModel(dcn_no_id=dcn_no_id, parent_part_no=parent_part_no[i], part_no_old=part_no_old[i], part_no_new=part_no_new[i], part_description_old=part_description_old[i],
                                  part_description_new=part_description_new[i], usage_qty_old=usage_qty_old[i], usage_qty_new=usage_qty_new[i],
                                  stock_details_on_hand=stock_details_on_hand[i], stock_details_open_po=stock_details_open_po[i],
                                  stock_details_total_stock=stock_details_total_stock[i], remarks=remarks[i], impl_date=impl_date[i], impl_serial_no=impl_serial_no[i])
                info1.save()

            return render(request, 'app/workflow_config.html')
    else:
        form = DCNPartsForm()

    return render(request, 'dcn/create_new.html', {'form': form})
