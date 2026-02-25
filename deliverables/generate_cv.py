"""
Generate Harvard-format CV PDF for Diego Estrada Medina using fpdf2.
Fallback when no LaTeX compiler is available.
"""
from fpdf import FPDF
import os

PAGE_W = 215.9  # Letter width mm

class HarvardCV(FPDF):
    LEFT_M = 15
    RIGHT_M = 15

    def __init__(self):
        super().__init__(format='Letter')
        self.set_auto_page_break(auto=True, margin=13)
        self.set_margins(self.LEFT_M, 12, self.RIGHT_M)
        self.usable_w = PAGE_W - self.LEFT_M - self.RIGHT_M
        self.add_font("CV", "", "C:/Windows/Fonts/arial.ttf")
        self.add_font("CV", "B", "C:/Windows/Fonts/arialbd.ttf")
        self.add_font("CV", "I", "C:/Windows/Fonts/ariali.ttf")
        self.add_font("CV", "BI", "C:/Windows/Fonts/arialbi.ttf")

    def _right_edge(self):
        return PAGE_W - self.RIGHT_M

    def header_block(self, name, location, email, linkedin):
        self.set_font("CV", "B", 20)
        self.cell(0, 9, name, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

        self.set_font("CV", "", 9)
        contact = f"{location}  |  {email}"
        self.cell(0, 5, contact, align="C", new_x="LMARGIN", new_y="NEXT")

        self.set_text_color(26, 82, 118)
        self.cell(0, 5, linkedin, align="C", new_x="LMARGIN", new_y="NEXT",
                  link=f"https://{linkedin}")
        self.set_text_color(0, 0, 0)

        self.ln(2)
        self.set_draw_color(44, 62, 80)
        self.set_line_width(0.4)
        self.line(self.LEFT_M, self.get_y(), self._right_edge(), self.get_y())
        self.ln(3)

    def section_title(self, title):
        self.ln(2)
        y = self.get_y()
        self.set_draw_color(44, 62, 80)
        self.set_line_width(0.25)

        self.set_font("CV", "B", 12)
        tw = self.get_string_width(title)
        center_x = self.LEFT_M + self.usable_w / 2
        gap = 3

        self.line(self.LEFT_M, y + 3, center_x - tw/2 - gap, y + 3)
        self.line(center_x + tw/2 + gap, y + 3, self._right_edge(), y + 3)

        self.cell(0, 7, title, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def entry_header(self, org, location, role, dates):
        self.set_font("CV", "B", 10)
        org_w = self.get_string_width(org) + 2
        self.cell(org_w, 5, org)
        self.set_font("CV", "", 9)
        self.cell(0, 5, location, align="R", new_x="LMARGIN", new_y="NEXT")

        self.set_font("CV", "I", 9.5)
        role_w = self.get_string_width(role) + 2
        self.cell(role_w, 5, role)
        self.cell(0, 5, dates, align="R", new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("CV", "", 9)
        indent = self.LEFT_M + 5
        bullet_w = 4
        text_x = indent + bullet_w
        text_w = self._right_edge() - text_x

        # Draw bullet character
        self.set_x(indent)
        self.cell(bullet_w, 4.5, "\u2022")

        # Draw wrapped text
        self.set_x(text_x)
        self.multi_cell(text_w, 4.5, text)

    def entry_spacing(self):
        self.ln(2.5)

    def skills_row(self, label, value):
        self.set_font("CV", "B", 9)
        lw = self.get_string_width(label) + 4
        self.cell(lw, 5, label)
        self.set_font("CV", "", 9)
        val_w = self._right_edge() - self.get_x()
        self.multi_cell(val_w, 5, value)
        self.ln(0.5)


def build():
    pdf = HarvardCV()
    pdf.add_page()

    # HEADER
    pdf.header_block(
        "Diego Estrada Medina",
        "Lima, Peru",
        "e.diegoandre@gmail.com",
        "linkedin.com/in/diegoestradamed"
    )

    # EXPERIENCE
    pdf.section_title("Experience")

    pdf.entry_header("Match Comms", "Lima, Peru",
                     "Community and Content Manager", "2022 \u2013 2024")
    pdf.bullet("Managed end-to-end communication strategies for 3 international clothing brands (Gap, Banana Republic, Kipling), aligning messaging with each brand\u2019s identity")
    pdf.bullet("Developed 50+ pieces of creative content per quarter, driving consistent brand engagement across digital platforms")
    pdf.entry_spacing()

    pdf.entry_header("Profonanpe", "Lima, Peru",
                     "Consultant for Social Media", "2023")
    pdf.bullet("Designed and executed creative content strategies that boosted audience engagement across key social media channels")
    pdf.bullet("Grew Instagram following by 10,000+ followers through targeted campaigns over a 6-month period")
    pdf.entry_spacing()

    pdf.entry_header("Sustainable Ocean Alliance Peru", "Remote",
                     "Communications Director", "2020 \u2013 2022")
    pdf.bullet("Spearheaded awareness campaigns on marine conservation reaching 50,000+ users across social media platforms")
    pdf.bullet("Produced multimedia content to promote ocean sustainability and engage youth audiences in 5+ countries")
    pdf.bullet("Coordinated strategic alliances with 10+ environmental organizations and grassroots movements")
    pdf.entry_spacing()

    pdf.entry_header("Stakeholders Magazine", "Lima, Peru",
                     "Journalist", "2019")
    pdf.bullet("Researched and published articles on sustainability, corporate responsibility, and social impact for a leading industry publication")
    pdf.bullet("Conducted interviews with 15+ key figures in the environmental and business sectors")
    pdf.entry_spacing()

    # PROJECTS & ACHIEVEMENTS
    pdf.section_title("Projects & Achievements")

    pdf.entry_header("Ancestral Wisdom for the Future", "Climate Adaptation",
                     "Project Coordinator", "2025")
    pdf.bullet("Coordinated a cross-cultural project preserving Aymara ancestral knowledge in response to climate change")
    pdf.bullet("Led digital content creation training for Aymara youth, building a TikTok-based knowledge bank")
    pdf.entry_spacing()

    pdf.entry_header("Ocean Watchers", "Environmental Monitoring",
                     "Communications Lead", "2022")
    pdf.bullet("Led communication strategies for a youth-driven environmental monitoring initiative")
    pdf.bullet("Strengthened community impact in areas affected by the La Pampilla oil spill in Lima")
    pdf.entry_spacing()

    pdf.entry_header("Pacific Whale Festival", "Sustainable Tourism",
                     "Communications Strategist", "2020 \u2013 2021")
    pdf.bullet("Designed the festival\u2019s communication strategy focused on sustainable tourism, reaching 5,000+ attendees")
    pdf.bullet("Coordinated interactive and educational activities to engage diverse audiences")
    pdf.entry_spacing()

    # LEADERSHIP & ACTIVITIES
    pdf.section_title("Leadership & Activities")

    pdf.entry_header("COP16: Biodiversity Conference", "Cali, Colombia",
                     "Delegate \u2013 Creadores del Ma\u00f1ana (TikTok)", "2024")
    pdf.bullet("Represented \u201cCreadores del Ma\u00f1ana\u201d collective, creating content on agrobiodiversity and food security")
    pdf.entry_spacing()

    pdf.entry_header("RCOY Latinoamericana", "Bel\u00e9m, Brazil",
                     "Youth Climate Delegate", "2024")
    pdf.bullet("Participated in the Regional Conference of Youth on Climate, collaborating with 200+ Latin American delegates")
    pdf.entry_spacing()

    pdf.entry_header("DeudaXClima (Debt for Climate)", "International",
                     "Active Member", "2024 \u2013 Present")
    pdf.bullet("Contributed communication strategies to a global movement advocating for climate debt cancellation")
    pdf.entry_spacing()

    # EDUCATION
    pdf.section_title("Education")

    pdf.entry_header("San Martin de Porres University", "Lima, Peru",
                     "Degree in Communications", "2015 \u2013 2021")
    pdf.bullet("Specialized in environmental and cultural communication")
    pdf.entry_spacing()

    pdf.entry_header("Toulouse Lautrec", "Lima, Peru",
                     "University Extension Course in Web Design", "2019")
    pdf.entry_spacing()

    # SKILLS & ADDITIONAL
    pdf.section_title("Skills & Additional")

    pdf.skills_row("Technical:",
                   "Content Strategy, Digital Marketing, Graphic Design, Visual Storytelling, Social Media Management, Web Analytics")
    pdf.skills_row("Languages:", "Spanish (Native), English")
    pdf.skills_row("Certifications:",
                   "Young People for Climate Finance (2024), Youth for Climate Action (2024), BausaTech Camp Mentor (2023), Youth Ambassadors for the Climate (2023)")
    pdf.skills_row("Interests:",
                   "Climate Justice, Ocean Conservation, LGBTQ+ Rights, Gender Equality, Sustainable Fashion, Ancestral Culture")

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "cv-estrada.pdf")
    pdf.output(out_path)
    print(f"PDF generated: {out_path}")
    return out_path


if __name__ == "__main__":
    build()
