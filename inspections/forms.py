from django import forms
from .models import PoolInformation
from .models import (
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

class PoolInformationForm(forms.ModelForm):
    class Meta:
        model = PoolInformation
        fields = [
            "pool_type",
            "approximate_volume",
            "water_level",
            "construction_type",
            "condition",
            "approximate_age",
            "remarks",
            "photo",
        ]

        widgets = {
            "pool_type": forms.Select(attrs={"class": "form-select"}),
            "approximate_volume": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 30,000L"}),
            "water_level": forms.Select(attrs={"class": "form-select"}),
            "construction_type": forms.Select(attrs={"class": "form-select"}),
            "condition": forms.Select(attrs={"class": "form-select"}),
            "approximate_age": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }

class WaterAnalysisForm(forms.ModelForm):
    class Meta:
        model = WaterAnalysis
        fields = [
            "ph",
            "chlorine",
            "stabiliser",
            "alkalinity",
            "calcium",
            "salt",
            "water_clarity",
            "needs_balancing",
            "needs_emptying",
            "algae_present",
            "scum_line",
            "scale_forming",
            "tiles_missing",
            "approximate_cost",
            "remarks",
            "photo",
        ]

        widgets = {
            "ph": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "chlorine": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stabiliser": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "alkalinity": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "calcium": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "salt": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 5000ppm"}),

            "water_clarity": forms.Select(attrs={"class": "form-select"}),
            "needs_balancing": forms.Select(attrs={"class": "form-select"}),
            "needs_emptying": forms.Select(attrs={"class": "form-select"}),
            "algae_present": forms.Select(attrs={"class": "form-select"}),
            "scum_line": forms.Select(attrs={"class": "form-select"}),
            "scale_forming": forms.Select(attrs={"class": "form-select"}),
            "tiles_missing": forms.Select(attrs={"class": "form-select"}),

            "approximate_cost": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. $20.00"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }

class ReturnMainDrainForm(forms.ModelForm):
    class Meta:
        model = ReturnMainDrain
        fields = [
            "return_lines_condition",
            "main_drain_condition",
            "main_drain_visible",
            "suction_issue",
            "remarks",
            "photo",
        ]

        widgets = {
            "return_lines_condition": forms.Select(attrs={"class": "form-select"}),
            "main_drain_condition": forms.Select(attrs={"class": "form-select"}),
            "main_drain_visible": forms.Select(attrs={"class": "form-select"}),
            "suction_issue": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }

class PoolFeaturesForm(forms.ModelForm):
    class Meta:
        model = PoolFeatures
        fields = [
            "coping_condition",
            "tiles_condition",
            "surface_condition",
            "cracks_visible",
            "leaks_visible",
            "staining_visible",
            "remarks",
            "photo",
        ]

        widgets = {
            "coping_condition": forms.Select(attrs={"class": "form-select"}),
            "tiles_condition": forms.Select(attrs={"class": "form-select"}),
            "surface_condition": forms.Select(attrs={"class": "form-select"}),
            "cracks_visible": forms.Select(attrs={"class": "form-select"}),
            "leaks_visible": forms.Select(attrs={"class": "form-select"}),
            "staining_visible": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }
class SkimmerBoxForm(forms.ModelForm):
    class Meta:
        model = SkimmerBox
        fields = [
            "skimmer_condition",
            "skimmer_lid_condition",
            "basket_condition",
            "suction_working",
            "remarks",
            "photo",
        ]

        widgets = {
            "skimmer_condition": forms.Select(attrs={"class": "form-select"}),
            "skimmer_lid_condition": forms.Select(attrs={"class": "form-select"}),
            "basket_condition": forms.Select(attrs={"class": "form-select"}),
            "suction_working": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }
class LightInspectionForm(forms.ModelForm):
    class Meta:
        model = LightInspection
        fields = [
            "lights_installed",
            "lights_working",
            "light_condition",
            "transformer_condition",
            "remarks",
            "photo",
        ]

        widgets = {
            "lights_installed": forms.Select(attrs={"class": "form-select"}),
            "lights_working": forms.Select(attrs={"class": "form-select"}),
            "light_condition": forms.Select(attrs={"class": "form-select"}),
            "transformer_condition": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }
class FilterInspectionForm(forms.ModelForm):
    class Meta:
        model = FilterInspection
        fields = "__all__"
        exclude = ["inspection"]
        widgets = {field: forms.Select(attrs={"class": "form-select"}) for field in [
            "filter_condition", "filter_leaking", "pressure_gauge_working", "needs_cleaning"
        ]}
        widgets.update({
            "filter_type": forms.TextInput(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        })


class PumpInspectionForm(forms.ModelForm):
    class Meta:
        model = PumpInspection
        exclude = ["inspection"]
        widgets = {
            "pump_condition": forms.Select(attrs={"class": "form-select"}),
            "pump_working": forms.Select(attrs={"class": "form-select"}),
            "pump_leaking": forms.Select(attrs={"class": "form-select"}),
            "pump_noise": forms.Select(attrs={"class": "form-select"}),
            "basket_condition": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }


class ChlorinatorInspectionForm(forms.ModelForm):
    class Meta:
        model = ChlorinatorInspection
        exclude = ["inspection"]
        widgets = {
            "chlorinator_condition": forms.Select(attrs={"class": "form-select"}),
            "cell_condition": forms.Select(attrs={"class": "form-select"}),
            "producing_chlorine": forms.Select(attrs={"class": "form-select"}),
            "needs_cleaning": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }


class SpaBlowerInspectionForm(forms.ModelForm):
    class Meta:
        model = SpaBlowerInspection
        exclude = ["inspection"]
        widgets = {
            "spa_present": forms.Select(attrs={"class": "form-select"}),
            "blower_working": forms.Select(attrs={"class": "form-select"}),
            "blower_condition": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }


class CleaningEquipmentInspectionForm(forms.ModelForm):
    class Meta:
        model = CleaningEquipmentInspection
        exclude = ["inspection"]
        widgets = {
            "pool_cleaner_present": forms.Select(attrs={"class": "form-select"}),
            "cleaner_condition": forms.Select(attrs={"class": "form-select"}),
            "pole_condition": forms.Select(attrs={"class": "form-select"}),
            "leaf_rake_condition": forms.Select(attrs={"class": "form-select"}),
            "vacuum_hose_condition": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }


class FencingInspectionForm(forms.ModelForm):
    class Meta:
        model = FencingInspection
        exclude = ["inspection"]
        widgets = {
            "fence_condition": forms.Select(attrs={"class": "form-select"}),
            "gate_self_closing": forms.Select(attrs={"class": "form-select"}),
            "gate_latching": forms.Select(attrs={"class": "form-select"}),
            "safety_concern": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }


class InspectionSummaryForm(forms.ModelForm):
    class Meta:
        model = InspectionSummary
        exclude = ["inspection"]
        widgets = {
            "priority_replacements": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "recommendations": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "inspector_comments": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }