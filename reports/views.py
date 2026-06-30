from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

from inspections.models import Inspection


def add_section(elements, title, rows, photo=None):
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    table = Table(rows, colWidths=[7 * cm, 9 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))

    if photo:
        try:
            elements.append(Image(photo.path, width=12 * cm, height=8 * cm))
            elements.append(Spacer(1, 16))
        except Exception:
            pass


@login_required
def download_report(request, inspection_id):
    inspection = get_object_or_404(Inspection, id=inspection_id)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="inspection_report_{inspection.id}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("<b>FIGLEAF POOL INSPECTION REPORT</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    customer_rows = [
        ["Field", "Details"],
        ["Customer", inspection.customer.name],
        ["Phone", inspection.customer.phone or "-"],
        ["Email", inspection.customer.email or "-"],
        ["Address", inspection.customer.address or "-"],
        ["Inspection Date", str(inspection.inspection_date)],
        ["Inspector", inspection.inspector_name],
        ["Reference", inspection.reference or "-"],
        ["Status", inspection.status],
    ]

    add_section(elements, "Customer & Inspection Details", customer_rows)

    if hasattr(inspection, "pool_information"):
        p = inspection.pool_information
        rows = [
            ["Field", "Details"],
            ["Pool Type", p.pool_type],
            ["Approximate Volume", p.approximate_volume or "-"],
            ["Water Level", p.water_level],
            ["Construction Type", p.construction_type],
            ["Condition", p.condition],
            ["Approximate Age", p.approximate_age],
            ["Remarks", p.remarks or "-"],
        ]
        add_section(elements, "Pool Information", rows, p.photo)

    if hasattr(inspection, "water_analysis"):
        w = inspection.water_analysis
        rows = [
            ["Field", "Details"],
            ["pH", w.ph or "-"],
            ["Chlorine", w.chlorine or "-"],
            ["Stabiliser", w.stabiliser or "-"],
            ["Alkalinity", w.alkalinity or "-"],
            ["Calcium", w.calcium or "-"],
            ["Salt / TDS", w.salt or "-"],
            ["Water Clarity", w.water_clarity or "-"],
            ["Needs Balancing", w.needs_balancing or "-"],
            ["Needs Emptying", w.needs_emptying or "-"],
            ["Algae Present", w.algae_present or "-"],
            ["Scum Line", w.scum_line or "-"],
            ["Scale Forming", w.scale_forming or "-"],
            ["Tiles Missing", w.tiles_missing or "-"],
            ["Approximate Cost", w.approximate_cost or "-"],
            ["Remarks", w.remarks or "-"],
        ]
        add_section(elements, "Water Analysis", rows, w.photo)

    section_map = [
        ("Return & Main Drain", "return_main_drain"),
        ("General Pool Features", "pool_features"),
        ("Skimmer Box", "skimmer_box"),
        ("Lights", "light_inspection"),
        ("Filter", "filter_inspection"),
        ("Pump", "pump_inspection"),
        ("Salt Chlorinator", "chlorinator_inspection"),
        ("Spa Blower", "spa_blower_inspection"),
        ("Cleaning Equipment", "cleaning_equipment_inspection"),
        ("Fencing", "fencing_inspection"),
    ]

    for title, attr in section_map:
        if hasattr(inspection, attr):
            section = getattr(inspection, attr)

            rows = [["Field", "Details"]]

            for field in section._meta.fields:
                if field.name in ["id", "inspection", "photo"]:
                    continue

                label = field.verbose_name.title()
                value = getattr(section, field.name)

                rows.append([label, value or "-"])

            add_section(elements, title, rows, getattr(section, "photo", None))

    if hasattr(inspection, "summary"):
        s = inspection.summary
        rows = [
            ["Field", "Details"],
            ["Priority Replacements", s.priority_replacements or "-"],
            ["Recommendations", s.recommendations or "-"],
            ["Inspector Comments", s.inspector_comments or "-"],
        ]
        add_section(elements, "Summary & Recommendations", rows)

    doc.build(elements)
    return response