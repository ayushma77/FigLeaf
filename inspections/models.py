from django.db import models
from customers.models import Customer


class Inspection(models.Model):
    STATUS_CHOICES = [
        ("Draft", "Draft"),
        ("Completed", "Completed"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspector_name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Draft"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.inspection_date}"
    
class PoolInformation(models.Model):
    POOL_TYPE_CHOICES = [
        ("Above Ground", "Above Ground"),
        ("In-ground", "In-ground"),
        ("Portable", "Portable"),
    ]

    WATER_LEVEL_CHOICES = [
        ("Below Skimmer", "Below Skimmer"),
        ("At Normal", "At Normal"),
        ("Above Skimmer", "Above Skimmer"),
    ]

    CONSTRUCTION_CHOICES = [
        ("Liner", "Liner"),
        ("Tile", "Tile"),
        ("Pebblecrete", "Pebblecrete"),
        ("Concrete", "Concrete"),
        ("Fibreglass", "Fibreglass"),
    ]

    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    ]

    AGE_CHOICES = [
        ("1-5 Years", "1-5 Years"),
        ("5-10 Years", "5-10 Years"),
        ("10+ Years", "10+ Years"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="pool_information"
    )

    pool_type = models.CharField(max_length=50, choices=POOL_TYPE_CHOICES)
    approximate_volume = models.CharField(max_length=50, blank=True, null=True)
    water_level = models.CharField(max_length=50, choices=WATER_LEVEL_CHOICES)
    construction_type = models.CharField(max_length=50, choices=CONSTRUCTION_CHOICES)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    approximate_age = models.CharField(max_length=50, choices=AGE_CHOICES)
    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/pool_information/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Pool Information - {self.inspection.customer.name}"
    
class WaterAnalysis(models.Model):
    WATER_CLARITY_CHOICES = [
        ("Clear", "Clear"),
        ("Cloudy", "Cloudy"),
        ("Green", "Green"),
    ]

    YES_NO_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="water_analysis"
    )

    ph = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    chlorine = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stabiliser = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alkalinity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    calcium = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    salt = models.CharField(max_length=50, blank=True, null=True)

    water_clarity = models.CharField(max_length=20, choices=WATER_CLARITY_CHOICES, blank=True, null=True)
    needs_balancing = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    needs_emptying = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    algae_present = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    scum_line = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    scale_forming = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)
    tiles_missing = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, null=True)

    approximate_cost = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/water_analysis/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Water Analysis - {self.inspection.customer.name}"
    
class ReturnMainDrain(models.Model):
    YES_NO_NA_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("N/A", "N/A"),
    ]

    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
        ("N/A", "N/A"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="return_main_drain"
    )

    return_lines_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    main_drain_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    main_drain_visible = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    suction_issue = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/return_main_drain/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Return & Main Drain - {self.inspection.customer.name}"
    
class PoolFeatures(models.Model):
    YES_NO_NA_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("N/A", "N/A"),
    ]

    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
        ("N/A", "N/A"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="pool_features"
    )

    coping_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    tiles_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    surface_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    cracks_visible = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    leaks_visible = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    staining_visible = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/pool_features/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Pool Features - {self.inspection.customer.name}"
class SkimmerBox(models.Model):
    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
        ("N/A", "N/A"),
    ]

    YES_NO_NA_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("N/A", "N/A"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="skimmer_box"
    )

    skimmer_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    skimmer_lid_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    basket_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    suction_working = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/skimmer_box/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Skimmer Box - {self.inspection.customer.name}"
    
class LightInspection(models.Model):
    CONDITION_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
        ("N/A", "N/A"),
    ]

    YES_NO_NA_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("N/A", "N/A"),
    ]

    inspection = models.OneToOneField(
        Inspection,
        on_delete=models.CASCADE,
        related_name="light_inspection"
    )

    lights_installed = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    lights_working = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    light_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    transformer_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)

    photo = models.ImageField(
        upload_to="inspection_photos/lights/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Lights - {self.inspection.customer.name}"

class FilterInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="filter_inspection")

    filter_type = models.CharField(max_length=100, blank=True, null=True)
    filter_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    filter_leaking = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    pressure_gauge_working = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    needs_cleaning = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/filter/", blank=True, null=True)


class PumpInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="pump_inspection")

    pump_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    pump_working = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    pump_leaking = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    pump_noise = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    basket_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/pump/", blank=True, null=True)


class ChlorinatorInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="chlorinator_inspection")

    chlorinator_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    cell_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    producing_chlorine = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    needs_cleaning = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/chlorinator/", blank=True, null=True)


class SpaBlowerInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="spa_blower_inspection")

    spa_present = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    blower_working = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    blower_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/spa_blower/", blank=True, null=True)


class CleaningEquipmentInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="cleaning_equipment_inspection")

    pool_cleaner_present = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    cleaner_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    pole_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    leaf_rake_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    vacuum_hose_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/cleaning_equipment/", blank=True, null=True)


class FencingInspection(models.Model):
    CONDITION_CHOICES = [("Good", "Good"), ("Fair", "Fair"), ("Poor", "Poor"), ("N/A", "N/A")]
    YES_NO_NA_CHOICES = [("Yes", "Yes"), ("No", "No"), ("N/A", "N/A")]

    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="fencing_inspection")

    fence_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True, null=True)
    gate_self_closing = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    gate_latching = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)
    safety_concern = models.CharField(max_length=20, choices=YES_NO_NA_CHOICES, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="inspection_photos/fencing/", blank=True, null=True)


class InspectionSummary(models.Model):
    inspection = models.OneToOneField(Inspection, on_delete=models.CASCADE, related_name="summary")

    priority_replacements = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    inspector_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Summary - {self.inspection.customer.name}"