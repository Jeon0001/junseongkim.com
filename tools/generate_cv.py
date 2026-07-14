from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Jun_Seong_Kim_CV.pdf"
WEBSITE_COPY = ROOT / "assets" / "documents" / "Jun_Seong_Kim_CV.pdf"
FONT_DIR = ROOT / "assets" / "fonts"


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Lato", str(FONT_DIR / "Lato-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Lato-Bold", str(FONT_DIR / "Lato-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Lato-Italic", str(FONT_DIR / "Lato-Italic.ttf")))
    pdfmetrics.registerFontFamily(
        "Lato",
        normal="Lato",
        bold="Lato-Bold",
        italic="Lato-Italic",
        boldItalic="Lato-Bold",
    )


def paper_link(label: str, url: str) -> str:
    return f'<u><link href="{escape(url)}" color="#000000">{escape(label)}</link></u>'


class ContactBar(Flowable):
    """Draw the compact icon-and-link contact row from the original CV."""

    def __init__(self) -> None:
        super().__init__()
        self.height = 17

    def wrap(self, available_width, available_height):
        self.width = available_width
        return available_width, self.height

    def draw(self):
        canvas = self.canv
        font_size = 9.96
        baseline = 5.1
        icon_width = 11
        icon_gap = 4.5
        group_gap = 14
        items = [
            ("phone", "010-8375-7470", None, False),
            ("email", "09jkim@kaist.ac.kr", "mailto:09jkim@kaist.ac.kr", True),
            ("linkedin", "LinkedIn", "https://www.linkedin.com/in/jun-kim-702885224/", True),
            ("person", "https://junseongkim.com", "https://junseongkim.com", True),
        ]

        widths = []
        for _, label, _, _ in items:
            widths.append(icon_width + icon_gap + pdfmetrics.stringWidth(label, "Lato", font_size))
        x = (self.width - sum(widths) - group_gap * (len(items) - 1)) / 2

        for index, (icon, label, url, underline) in enumerate(items):
            self._draw_icon(canvas, icon, x, baseline)
            text_x = x + icon_width + icon_gap
            canvas.setFont("Lato", font_size)
            canvas.setFillColor(colors.black)
            canvas.drawString(text_x, baseline, label)
            text_width = pdfmetrics.stringWidth(label, "Lato", font_size)
            if underline:
                canvas.setLineWidth(0.45)
                canvas.line(text_x, baseline - 1.25, text_x + text_width, baseline - 1.25)
            if url:
                canvas.linkURL(
                    url,
                    (text_x, baseline - 2, text_x + text_width, baseline + font_size + 1),
                    relative=1,
                    thickness=0,
                )
            x += widths[index] + group_gap

    @staticmethod
    def _draw_icon(canvas, icon: str, x: float, baseline: float) -> None:
        canvas.saveState()
        canvas.setFillColor(colors.black)
        canvas.setStrokeColor(colors.black)

        if icon == "phone":
            # A small handset silhouette matching the weight of the original icon.
            path = canvas.beginPath()
            path.moveTo(x + 1, baseline + 8.5)
            path.curveTo(x + 0.5, baseline + 6, x + 1.7, baseline + 2.4, x + 4.5, baseline + 0.6)
            path.curveTo(x + 6.4, baseline - 0.5, x + 9.2, baseline + 0.4, x + 10.2, baseline + 2)
            path.lineTo(x + 7.8, baseline + 4)
            path.curveTo(x + 7, baseline + 3.1, x + 6.3, baseline + 2.7, x + 5.3, baseline + 2.7)
            path.curveTo(x + 3.8, baseline + 3.8, x + 3.1, baseline + 5.1, x + 3, baseline + 6.2)
            path.lineTo(x + 5.7, baseline + 7.5)
            path.lineTo(x + 4.4, baseline + 10.5)
            path.close()
            canvas.drawPath(path, fill=1, stroke=0)
        elif icon == "email":
            canvas.roundRect(x, baseline + 1.2, 10.8, 8, 1.1, fill=1, stroke=0)
            canvas.setStrokeColor(colors.white)
            canvas.setLineWidth(0.7)
            canvas.line(x + 0.8, baseline + 8.1, x + 5.4, baseline + 4.7)
            canvas.line(x + 10, baseline + 8.1, x + 5.4, baseline + 4.7)
        elif icon == "linkedin":
            canvas.roundRect(x + 0.5, baseline + 0.8, 9.5, 9.5, 1, fill=1, stroke=0)
            canvas.setFillColor(colors.white)
            canvas.setFont("Lato-Bold", 6.2)
            canvas.drawCentredString(x + 5.25, baseline + 3.1, "in")
        else:
            canvas.circle(x + 5.4, baseline + 7.7, 2.7, fill=1, stroke=0)
            canvas.roundRect(x + 1.1, baseline + 0.3, 8.6, 5.2, 1.5, fill=1, stroke=0)
        canvas.restoreState()


def build_cv(output_path: Path) -> None:
    register_fonts()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.31 * inch,
        bottomMargin=0.34 * inch,
        title="Jun Seong Kim - Curriculum Vitae",
        author="Jun Seong Kim",
        subject="Curriculum vitae",
    )
    available_width = letter[0] - doc.leftMargin - doc.rightMargin

    name_style = ParagraphStyle(
        "Name",
        fontName="Lato-Bold",
        fontSize=24.79,
        leading=27.2,
        alignment=1,
        textColor=colors.black,
        spaceAfter=0,
    )
    section_style = ParagraphStyle(
        "Section",
        fontName="Lato",
        fontSize=11.96,
        leading=14.2,
        textColor=colors.black,
        spaceBefore=5.4,
        spaceAfter=0.7,
    )
    entry_title_style = ParagraphStyle(
        "EntryTitle",
        fontName="Lato-Bold",
        fontSize=10.91,
        leading=12.4,
        textColor=colors.black,
    )
    entry_date_style = ParagraphStyle(
        "EntryDate",
        parent=entry_title_style,
        fontName="Lato",
        alignment=TA_RIGHT,
    )
    entry_meta_style = ParagraphStyle(
        "EntryMeta",
        fontName="Lato-Italic",
        fontSize=9.96,
        leading=11.6,
        textColor=colors.black,
    )
    entry_location_style = ParagraphStyle(
        "EntryLocation",
        parent=entry_meta_style,
        alignment=TA_RIGHT,
    )
    body_style = ParagraphStyle(
        "Body",
        fontName="Lato",
        fontSize=9.96,
        leading=11.65,
        textColor=colors.black,
        alignment=TA_LEFT,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=24,
        rightIndent=3,
        firstLineIndent=-10,
        bulletIndent=8,
        spaceBefore=0.3,
        spaceAfter=0.15,
    )
    def section(title: str):
        return [
            Paragraph(title, section_style),
            HRFlowable(width="100%", thickness=0.45, color=colors.black, spaceBefore=0, spaceAfter=4.1),
        ]

    def header_rows(title: str, date: str, subtitle: str, location: str):
        table = Table(
            [
                [Paragraph(title, entry_title_style), Paragraph(date, entry_date_style)],
                [Paragraph(subtitle, entry_meta_style), Paragraph(location, entry_location_style)],
            ],
            colWidths=[available_width - 2.18 * inch, 2.18 * inch],
            hAlign="LEFT",
        )
        table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (0, -1), 10.8),
                    ("RIGHTPADDING", (0, 0), (0, -1), 0),
                    ("LEFTPADDING", (1, 0), (1, -1), 0),
                    ("RIGHTPADDING", (1, 0), (1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )
        return table

    def entry(title: str, date: str, subtitle: str, location: str, bullets: list[str], space_after=3.1):
        content = [header_rows(title, date, subtitle, location)]
        content.extend(Paragraph(f"<bullet>&bull;</bullet>{bullet}", bullet_style) for bullet in bullets)
        content.append(Spacer(1, space_after))
        return KeepTogether(content)

    def publication(
        number: int,
        title: str,
        url: str,
        venue: str,
        date: str,
        authors: str,
        award: str | None = None,
    ):
        title_line = f"{paper_link(title, url)} [{number}]"
        bullets = [f"<b>Authors:</b> {authors}"]
        if award:
            bullets.append(f"<b>{award}</b>")
        return entry(title_line, "", venue, date, bullets, space_after=2.4)

    story = [
        Paragraph("Jun Seong Kim", name_style),
        ContactBar(),
        Spacer(1, 5.6),
    ]

    story.extend(section("Education"))
    story.append(
        entry(
            "Korea Advanced Institute of Science and Technology (KAIST)",
            "Mar 2026 - Present",
            "Master of Science in Computer Science, U&amp;I Lab (Advisor: Alice Oh)",
            "Daejeon, South Korea",
            [],
            space_after=3,
        )
    )
    story.append(
        entry(
            "Korea Advanced Institute of Science and Technology (KAIST)",
            "Sep 2020 - Feb 2026",
            "Bachelor of Science in Computer Science, Double Major in Business and Technology Management",
            "Daejeon, South Korea",
            [],
            space_after=1.6,
        )
    )

    story.extend(section("Experience"))
    story.append(
        entry(
            "KAIST U&amp;I Lab, School of Computing",
            "Mar 2026 - Present",
            "Graduate Researcher",
            "Daejeon, South Korea",
            [
                "Research cultural AI evaluation, multimodal model behavior, bias, and reliability across diverse real-world contexts.",
                "Contribute to large-scale benchmarks for culture mixing and localized AI safety evaluation, including CultureMix and Pluralis.",
            ],
        )
    )
    story.append(
        entry(
            "Institute for Basic Science, Data Science Lab",
            "Dec 2022 - Mar 2024",
            "Data Science (+Planetary Atmospheres) Internship and Collaboration",
            "Daejeon, South Korea",
            [
                "Created image-preprocessing pipelines for NetCDF and FITS observations from the Akatsuki and Venus Express orbiters.",
                "Developed GAN/VAE-based anomaly-detection models in PyTorch; the strongest model achieved 90.81% AUC on UVI data.",
            ],
            space_after=1.7,
        )
    )

    story.extend(section("Projects"))
    story.append(
        entry(
            "Particall",
            "Ongoing",
            "Web project for finding gaming communities and teammates",
            "",
            [
                "Designed and developed a platform that helps players find compatible people and communities to play games with.",
            ],
            space_after=2.5,
        )
    )
    story.extend(section("Publications"))
    story.append(
        publication(
            1,
            "Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability",
            "https://arxiv.org/abs/2607.06196",
            "arXiv:2607.06196",
            "2026",
            "Alicia Parrish et al. (including <b>Jun Seong Kim</b>)",
        )
    )
    story.append(
        publication(
            2,
            "World in a Frame: Understanding Culture Mixing as a New Challenge for Vision-Language Models",
            "https://openaccess.thecvf.com/content/CVPR2026/html/Kim_World_in_a_Frame_Understanding_Culture_Mixing_as_a_New_CVPR_2026_paper.html",
            "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
            "2026",
            "Eunsu Kim, Junyeong Park, Na Min An, <b>Jun Seong Kim</b>, et al.",
        )
    )
    story.append(
        publication(
            3,
            "When Tom Eats Kimchi: Evaluating Cultural Awareness of Multimodal Large Language Models in Cultural Mixture Contexts",
            "https://aclanthology.org/2025.c3nlp-1.11/",
            "The 3rd Workshop on Cross-Cultural Considerations in NLP (C3NLP)",
            "2025",
            "<b>Jun Seong Kim</b>, Kyaw Ye Thu, Javad Ismayilzada, Junyeong Park, Eunsu Kim, et al.",
            "Outstanding Paper",
        )
    )
    story.append(
        publication(
            4,
            "Detecting Stationary Atmospheric Waves in Venus with a Self-Supervised Adversarial Model Using Anomaly Detection",
            "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11705606",
            "Korea Software Congress (KSC)",
            "Dec 2023",
            "<b>Jun Seong Kim</b>, Husnu Baris Baydargil, Jose Eduardo Silva, Yeon-Joo Lee, Meeyoung Cha",
            "Best Student Paper",
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build_cv(OUTPUT)
    WEBSITE_COPY.write_bytes(OUTPUT.read_bytes())
    print(f"Generated {OUTPUT}")
    print(f"Updated website copy {WEBSITE_COPY}")
