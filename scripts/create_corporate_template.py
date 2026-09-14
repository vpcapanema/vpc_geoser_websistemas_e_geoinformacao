from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "fontes" / "templates" / "TEMPLATE_CORPORATIVO_VPC_WEBSISTEMAS.docx"
LOGO = ROOT / "assets" / "identidade-visual" / "favicon" / "favicon-512x512.png"

NAVY = "071B45"
BLUE = "0878D1"
CYAN = "11B8D8"
GREEN = "67B900"
GRAY = "59636E"
LIGHT = "EEF4F8"
SLOGAN = "Inteligência em geoprocessamento e sensoriamento remoto."


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=80, start=100, bottom=80, end=100) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def remove_table_borders(table) -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = borders.find(qn(f"w:{edge}"))
        if tag is None:
            tag = OxmlElement(f"w:{edge}")
            borders.append(tag)
        tag.set(qn("w:val"), "nil")


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def add_field(paragraph, instruction: str) -> None:
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t")
    text.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend((begin, instr, separate, text, end))


def add_bottom_rule(paragraph, color: str = CYAN, size: str = "14") -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    p_pr.append(borders)


def apply_font(run, size=None, bold=None, color=None) -> None:
    run.font.name = "Arial"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if color is not None:
        run.font.color.rgb = RGBColor.from_string(color)


def configure_styles(doc: Document) -> None:
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = RGBColor.from_string("25313C")
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    for name, size, color, before, after in (
        ("Title", 26, NAVY, 0, 10),
        ("Subtitle", 13, GRAY, 0, 12),
        ("Heading 1", 17, NAVY, 18, 8),
        ("Heading 2", 13, BLUE, 14, 6),
        ("Heading 3", 11, NAVY, 10, 4),
    ):
        style = doc.styles[name]
        style.font.name = "Arial"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        style.font.size = Pt(size)
        style.font.bold = name != "Subtitle"
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True

    if "Legenda VPC" not in doc.styles:
        style = doc.styles.add_style("Legenda VPC", WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = "Arial"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        style.font.size = Pt(8.5)
        style.font.italic = True
        style.font.color.rgb = RGBColor.from_string(GRAY)
        style.paragraph_format.space_before = Pt(3)
        style.paragraph_format.space_after = Pt(8)


def configure_section(section) -> None:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.4)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.0)
    section.header_distance = Cm(0.7)
    section.footer_distance = Cm(0.7)

    header = section.header
    header.is_linked_to_previous = False
    table = header.add_table(rows=1, cols=2, width=Cm(16.5))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.columns[0].width = Cm(2.0)
    table.columns[1].width = Cm(14.5)
    remove_table_borders(table)
    logo_cell, text_cell = table.rows[0].cells
    logo_cell.width = Cm(2.0)
    logo_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p_logo = logo_cell.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_logo = p_logo.add_run()
    picture = run_logo.add_picture(str(LOGO), width=Cm(1.55))
    doc_pr = picture._inline.docPr
    doc_pr.set("name", "Símbolo VPC — satélite")
    doc_pr.set("descr", "Símbolo institucional principal da VPC WebSistemas & Geoinformação")
    text_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p_name = text_cell.paragraphs[0]
    p_name.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p_name.add_run("VPC WEBSISTEMAS & GEOINFORMAÇÃO")
    apply_font(run, size=10, bold=True, color=NAVY)
    p_tag = text_cell.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_tag.paragraph_format.space_after = Pt(0)
    run = p_tag.add_run(SLOGAN)
    apply_font(run, size=7.5, color=GRAY)
    add_bottom_rule(p_tag)

    footer = section.footer
    footer.is_linked_to_previous = False
    table = footer.add_table(rows=1, cols=2, width=Cm(16.5))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(table)
    left, right = table.rows[0].cells
    p = left.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    run = p.add_run("vpcwebsistemas.com.br")
    apply_font(run, size=7.5, color=GRAY)
    p = right.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Página ")
    apply_font(run, size=7.5, color=GRAY)
    add_field(p, "PAGE")
    run = p.add_run(" de ")
    apply_font(run, size=7.5, color=GRAY)
    add_field(p, "NUMPAGES")


def add_cover(doc: Document) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(55)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    picture = run.add_picture(str(LOGO), width=Cm(5.0))
    picture._inline.docPr.set("descr", "Símbolo institucional principal da VPC — satélite")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    run = p.add_run("[TÍTULO DO DOCUMENTO]")
    apply_font(run, size=26, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[Subtítulo ou descrição curta]")
    apply_font(run, size=13, color=GRAY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(16)
    run = p.add_run("VPC WebSistemas & Geoinformação")
    apply_font(run, size=12, bold=True, color=BLUE)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(SLOGAN)
    apply_font(run, size=10, color=GREEN)

    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Cm(4.0)
    table.columns[1].width = Cm(8.5)
    remove_table_borders(table)
    values = (("Documento", "[código ou referência]"), ("Versão", "[0.1]"), ("Data", "[dd/mm/aaaa]"))
    for row, (label, value) in zip(table.rows, values):
        set_cell_shading(row.cells[0], LIGHT)
        set_cell_margins(row.cells[0])
        set_cell_margins(row.cells[1])
        r = row.cells[0].paragraphs[0].add_run(label)
        apply_font(r, size=9, bold=True, color=NAVY)
        r = row.cells[1].paragraphs[0].add_run(value)
        apply_font(r, size=9, color=GRAY)


def add_content_sample(doc: Document) -> None:
    doc.add_page_break()
    doc.add_heading("1. Título da seção", level=1)
    doc.add_paragraph(
        "Substitua este conteúdo pelo texto do documento. O estilo Corpo de texto utiliza Arial 10,5 pt, "
        "entrelinha 1,15 e espaçamento posterior de 6 pt. Use os estilos de título para preservar a hierarquia visual."
    )
    doc.add_heading("1.1 Subseção", level=2)
    doc.add_paragraph(
        "Mantenha parágrafos curtos, títulos descritivos e terminologia consistente com a identidade institucional da VPC."
    )
    for item in (
        "Primeiro item de exemplo;",
        "segundo item de exemplo;",
        "terceiro item de exemplo."
    ):
        doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("Quadro de informações", level=2)
    table = doc.add_table(rows=2, cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ("Campo", "Descrição", "Responsável")
    for cell, value in zip(table.rows[0].cells, headers):
        set_cell_shading(cell, NAVY)
        p = cell.paragraphs[0]
        r = p.add_run(value)
        apply_font(r, size=9, bold=True, color="FFFFFF")
    set_repeat_table_header(table.rows[0])
    for cell, value in zip(table.rows[1].cells, ("[Item]", "[Descrição do conteúdo]", "[Nome ou área]")):
        p = cell.paragraphs[0]
        r = p.add_run(value)
        apply_font(r, size=9, color="25313C")

    p = doc.add_paragraph("Figura 1 — Legenda de exemplo", style="Legenda VPC")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    note = doc.add_table(rows=1, cols=1)
    note.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = note.cell(0, 0)
    set_cell_shading(cell, LIGHT)
    set_cell_margins(cell, top=150, start=180, bottom=150, end=180)
    p = cell.paragraphs[0]
    r = p.add_run("NOTA — ")
    apply_font(r, size=9, bold=True, color=BLUE)
    r = p.add_run("Use este bloco para observações, ressalvas ou decisões relevantes.")
    apply_font(r, size=9, color="25313C")


def build() -> None:
    doc = Document()
    configure_styles(doc)
    for section in doc.sections:
        configure_section(section)

    props = doc.core_properties
    props.title = "Template Corporativo — VPC WebSistemas & Geoinformação"
    props.subject = "Modelo oficial A4 para documentos institucionais e técnicos"
    props.author = "VPC WebSistemas & Geoinformação"
    props.keywords = "VPC, WebSistemas, Geoinformação, template corporativo, A4"
    props.comments = "Símbolo principal: satélite. Identidade institucional vigente."
    props.category = "Template corporativo"
    props.language = "pt-BR"

    add_cover(doc)
    add_content_sample(doc)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    build()
