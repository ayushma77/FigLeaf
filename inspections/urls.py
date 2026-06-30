from django.urls import path
from . import views

urlpatterns = [
    path("", views.inspection_list, name="inspection_list"),
    path("create/", views.create_inspection, name="create_inspection"),

    path("<int:inspection_id>/pool-information/", views.pool_information, name="pool_information"),
    path("<int:inspection_id>/water-analysis/", views.water_analysis, name="water_analysis"),
    path("<int:inspection_id>/return-main-drain/", views.return_main_drain, name="return_main_drain"),
    path("<int:inspection_id>/pool-features/", views.pool_features, name="pool_features"),
    path("<int:inspection_id>/skimmer-box/", views.skimmer_box, name="skimmer_box"),
    path("<int:inspection_id>/lights/", views.light_inspection, name="light_inspection"),
    path("<int:inspection_id>/filter/", views.filter_inspection, name="filter_inspection"),
    path("<int:inspection_id>/pump/", views.pump_inspection, name="pump_inspection"),
    path("<int:inspection_id>/chlorinator/", views.chlorinator_inspection, name="chlorinator_inspection"),
    path("<int:inspection_id>/spa-blower/", views.spa_blower_inspection, name="spa_blower_inspection"),
    path("<int:inspection_id>/cleaning-equipment/", views.cleaning_equipment, name="cleaning_equipment"),
    path("<int:inspection_id>/fencing/", views.fencing_inspection, name="fencing_inspection"),
    path("<int:inspection_id>/summary/", views.inspection_summary, name="inspection_summary"),
]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.inspection_list, name="inspection_list"),
#     path("create/", views.create_inspection, name="create_inspection"),
#     path(
#         "<int:inspection_id>/pool-information/",
#         views.pool_information,
#         name="pool_information"
#     ),
#     path(
#     "<int:inspection_id>/water-analysis/",
#     views.water_analysis,
#     name="water_analysis"
# ),
#     path("<int:inspection_id>/return-main-drain/", views.return_main_drain, name="return_main_drain"),
#     path("<int:inspection_id>/pool-features/", views.pool_features, name="pool_features"),
#     path("<int:inspection_id>/skimmer-box/", views.skimmer_box, name="skimmer_box"),
#     path("<int:inspection_id>/lights/", views.light_inspection, name="light_inspection"),
# ]