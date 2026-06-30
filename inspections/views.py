from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from customers.models import Customer

from .models import (
    Inspection,
    PoolInformation,
    WaterAnalysis,
    ReturnMainDrain,
    PoolFeatures,
    SkimmerBox,
    LightInspection,
    FilterInspection,
    PumpInspection,
    ChlorinatorInspection,
    SpaBlowerInspection,
    CleaningEquipmentInspection,
    FencingInspection,
    InspectionSummary,
)

from .forms import (
    PoolInformationForm,
    WaterAnalysisForm,
    ReturnMainDrainForm,
    PoolFeaturesForm,
    SkimmerBoxForm,
    LightInspectionForm,
    FilterInspectionForm,
    PumpInspectionForm,
    ChlorinatorInspectionForm,
    SpaBlowerInspectionForm,
    CleaningEquipmentInspectionForm,
    FencingInspectionForm,
    InspectionSummaryForm,
)


@login_required
def inspection_list(request):
    inspections = Inspection.objects.all().order_by("-created_at")
    return render(request, "inspections/inspection_list.html", {
        "inspections": inspections
    })


@login_required
def create_inspection(request):
    customers = Customer.objects.all().order_by("name")

    if request.method == "POST":
        inspection = Inspection.objects.create(
            customer_id=request.POST.get("customer"),
            inspection_date=request.POST.get("inspection_date"),
            inspector_name=request.POST.get("inspector_name"),
            reference=request.POST.get("reference"),
            status="Draft",
        )

        return redirect("pool_information", inspection_id=inspection.id)

    return render(request, "inspections/create_inspection.html", {
        "customers": customers
    })


def render_step(request, inspection, form, step_title, step_subtitle, step_label, progress, back_url):
    return render(request, "inspections/inspection_step.html", {
        "inspection": inspection,
        "form": form,
        "step_title": step_title,
        "step_subtitle": step_subtitle,
        "step_label": step_label,
        "progress": progress,
        "back_url": back_url,
    })


@login_required
def pool_information(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = PoolInformation.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = PoolInformationForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("water_analysis", inspection_id=inspection.id)
    else:
        form = PoolInformationForm(instance=section)

    return render_step(request, inspection, form, "Pool Information", "Step 2 of 15", "Step 2 / 15", 14, None)


@login_required
def water_analysis(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = WaterAnalysis.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = WaterAnalysisForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("return_main_drain", inspection_id=inspection.id)
    else:
        form = WaterAnalysisForm(instance=section)

    return render_step(request, inspection, form, "Water Analysis", "Step 3 of 15", "Step 3 / 15", 21, f"/inspections/{inspection.id}/pool-information/")


@login_required
def return_main_drain(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = ReturnMainDrain.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = ReturnMainDrainForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("pool_features", inspection_id=inspection.id)
    else:
        form = ReturnMainDrainForm(instance=section)

    return render_step(request, inspection, form, "Pool Return & Main Drain", "Step 4 of 15", "Step 4 / 15", 28, f"/inspections/{inspection.id}/water-analysis/")


@login_required
def pool_features(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = PoolFeatures.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = PoolFeaturesForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("skimmer_box", inspection_id=inspection.id)
    else:
        form = PoolFeaturesForm(instance=section)

    return render_step(request, inspection, form, "General Pool Features", "Step 5 of 15", "Step 5 / 15", 35, f"/inspections/{inspection.id}/return-main-drain/")


@login_required
def skimmer_box(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = SkimmerBox.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = SkimmerBoxForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("light_inspection", inspection_id=inspection.id)
    else:
        form = SkimmerBoxForm(instance=section)

    return render_step(request, inspection, form, "Skimmer Box", "Step 6 of 15", "Step 6 / 15", 42, f"/inspections/{inspection.id}/pool-features/")


@login_required
def light_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = LightInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = LightInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("filter_inspection", inspection_id=inspection.id)
    else:
        form = LightInspectionForm(instance=section)

    return render_step(request, inspection, form, "Lights", "Step 7 of 15", "Step 7 / 15", 49, f"/inspections/{inspection.id}/skimmer-box/")


@login_required
def filter_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = FilterInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = FilterInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("pump_inspection", inspection_id=inspection.id)
    else:
        form = FilterInspectionForm(instance=section)

    return render_step(request, inspection, form, "Filter", "Step 8 of 15", "Step 8 / 15", 56, f"/inspections/{inspection.id}/lights/")


@login_required
def pump_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = PumpInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = PumpInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("chlorinator_inspection", inspection_id=inspection.id)
    else:
        form = PumpInspectionForm(instance=section)

    return render_step(request, inspection, form, "Pump", "Step 9 of 15", "Step 9 / 15", 63, f"/inspections/{inspection.id}/filter/")


@login_required
def chlorinator_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = ChlorinatorInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = ChlorinatorInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("spa_blower_inspection", inspection_id=inspection.id)
    else:
        form = ChlorinatorInspectionForm(instance=section)

    return render_step(request, inspection, form, "Salt Chlorinator", "Step 10 of 15", "Step 10 / 15", 70, f"/inspections/{inspection.id}/pump/")


@login_required
def spa_blower_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = SpaBlowerInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = SpaBlowerInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("cleaning_equipment", inspection_id=inspection.id)
    else:
        form = SpaBlowerInspectionForm(instance=section)

    return render_step(request, inspection, form, "Spa Blower", "Step 11 of 15", "Step 11 / 15", 77, f"/inspections/{inspection.id}/chlorinator/")


@login_required
def cleaning_equipment(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = CleaningEquipmentInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = CleaningEquipmentInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("fencing_inspection", inspection_id=inspection.id)
    else:
        form = CleaningEquipmentInspectionForm(instance=section)

    return render_step(request, inspection, form, "Cleaning Equipment", "Step 12 of 15", "Step 12 / 15", 84, f"/inspections/{inspection.id}/spa-blower/")


@login_required
def fencing_inspection(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = FencingInspection.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = FencingInspectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            return redirect("inspection_summary", inspection_id=inspection.id)
    else:
        form = FencingInspectionForm(instance=section)

    return render_step(request, inspection, form, "Fencing", "Step 13 of 15", "Step 13 / 15", 91, f"/inspections/{inspection.id}/cleaning-equipment/")


@login_required
def inspection_summary(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)
    section, created = InspectionSummary.objects.get_or_create(inspection=inspection)

    if request.method == "POST":
        form = InspectionSummaryForm(request.POST, instance=section)
        if form.is_valid():
            form.save()

            inspection.status = "Completed"
            inspection.save()

            return redirect("inspection_list")
    else:
        form = InspectionSummaryForm(instance=section)

    return render_step(request, inspection, form, "Summary & Recommendations", "Step 14 of 15", "Step 14 / 15", 98, f"/inspections/{inspection.id}/fencing/")
# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from customers.models import Customer



# from .models import Inspection, PoolInformation, WaterAnalysis, ReturnMainDrain, PoolFeatures, SkimmerBox, LightInspection
# from .forms import PoolInformationForm, WaterAnalysisForm, ReturnMainDrainForm, PoolFeaturesForm, SkimmerBoxForm, LightInspectionForm

# @login_required
# def inspection_list(request):
#     inspections = Inspection.objects.all().order_by("-created_at")

#     return render(request, "inspections/inspection_list.html", {
#         "inspections": inspections
#     })


# @login_required
# def create_inspection(request):
#     customers = Customer.objects.all().order_by("name")

#     if request.method == "POST":
#         customer_id = request.POST.get("customer")
#         inspection_date = request.POST.get("inspection_date")
#         inspector_name = request.POST.get("inspector_name")
#         reference = request.POST.get("reference")

#         inspection = Inspection.objects.create(
#             customer_id=customer_id,
#             inspection_date=inspection_date,
#             inspector_name=inspector_name,
#             reference=reference,
#             status="Draft",
#         )

#         return redirect("pool_information", inspection_id=inspection.id)

#     return render(request, "inspections/create_inspection.html", {
#         "customers": customers
#     })

# @login_required
# def pool_information(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     pool_info, created = PoolInformation.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = PoolInformationForm(
#             request.POST,
#             request.FILES,
#             instance=pool_info
#         )

#         if form.is_valid():
#             form.save()
#             return redirect("water_analysis", inspection_id=inspection.id)
#     else:
#         form = PoolInformationForm(instance=pool_info)

#     # return render(request, "inspections/pool_information.html", {
#     #     "inspection": inspection,
#     #     "form": form,
#     # })
#     return render(request, "inspections/inspection_step.html", {
#     "inspection": inspection,
#     "form": form,
#     "step_title": "Pool Information",
#     "step_subtitle": "Step 2 of 15",
#     "step_label": "Step 2 / 15",
#     "progress": 14,
#     "back_url": None,
#     })
# @login_required
# def water_analysis(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     water, created = WaterAnalysis.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = WaterAnalysisForm(
#             request.POST,
#             request.FILES,
#             instance=water
#         )

#         if form.is_valid():
#             form.save()
#             return redirect("return_main_drain", inspection_id=inspection.id)
#     else:
#         form = WaterAnalysisForm(instance=water)

#     # return render(request, "inspections/water_analysis.html", {
#     #     "inspection": inspection,
#     #     "form": form,
#     # })
#     return render(request, "inspections/inspection_step.html", {
#     "inspection": inspection,
#     "form": form,
#     "step_title": "Water Analysis",
#     "step_subtitle": "Step 3 of 15",
#     "step_label": "Step 3 / 15",
#     "progress": 21,
#     "back_url": f"/inspections/{inspection.id}/pool-information/",
#     })

# @login_required
# def return_main_drain(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     section, created = ReturnMainDrain.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = ReturnMainDrainForm(
#             request.POST,
#             request.FILES,
#             instance=section
#         )

#         if form.is_valid():
#             form.save()
            
#             return redirect("pool_features", inspection_id=inspection.id)
#     else:
#         form = ReturnMainDrainForm(instance=section)

#     # return render(request, "inspections/return_main_drain.html", {
#     #     "inspection": inspection,
#     #     "form": form,
#     # })
#     return render(request, "inspections/inspection_step.html", {
#     "inspection": inspection,
#     "form": form,
#     "step_title": "Pool Return & Main Drain",
#     "step_subtitle": "Step 4 of 15",
#     "step_label": "Step 4 / 15",
#     "progress": 28,
#     "back_url": f"/inspections/{inspection.id}/water-analysis/",
#     })

# @login_required
# def pool_features(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     section, created = PoolFeatures.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = PoolFeaturesForm(
#             request.POST,
#             request.FILES,
#             instance=section
#         )

#         if form.is_valid():
#             form.save()
#             return redirect("skimmer_box", inspection_id=inspection.id)
#     else:
#         form = PoolFeaturesForm(instance=section)

#     # return render(request, "inspections/pool_features.html", {
#     #     "inspection": inspection,
#     #     "form": form,
#     # })
#     return render(request, "inspections/inspection_step.html", {
#     "inspection": inspection,
#     "form": form,
#     "step_title": "General Pool Features",
#     "step_subtitle": "Step 5 of 15",
#     "step_label": "Step 5 / 15",
#     "progress": 35,
#     "back_url": f"/inspections/{inspection.id}/return-main-drain/",
#     })
# @login_required
# def skimmer_box(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     section, created = SkimmerBox.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = SkimmerBoxForm(
#             request.POST,
#             request.FILES,
#             instance=section
#         )

#         if form.is_valid():
#             form.save()
#             return redirect("light_inspection", inspection_id=inspection.id)
#     else:
#         form = SkimmerBoxForm(instance=section)

#     return render(request, "inspections/inspection_step.html", {
#         "inspection": inspection,
#         "form": form,
#         "step_title": "Skimmer Box",
#         "step_subtitle": "Step 6 of 15",
#         "step_label": "Step 6 / 15",
#         "progress": 42,
#         "back_url": f"/inspections/{inspection.id}/pool-features/",
#     })

# @login_required
# def light_inspection(request, inspection_id):
#     inspection = get_object_or_404(Inspection, id=inspection_id)

#     section, created = LightInspection.objects.get_or_create(
#         inspection=inspection
#     )

#     if request.method == "POST":
#         form = LightInspectionForm(
#             request.POST,
#             request.FILES,
#             instance=section
#         )

#         if form.is_valid():
#             form.save()
#             return redirect("inspection_list")
#     else:
#         form = LightInspectionForm(instance=section)

#     return render(request, "inspections/inspection_step.html", {
#         "inspection": inspection,
#         "form": form,
#         "step_title": "Lights",
#         "step_subtitle": "Step 7 of 15",
#         "step_label": "Step 7 / 15",
#         "progress": 49,
#         "back_url": f"/inspections/{inspection.id}/skimmer-box/",
#     })

