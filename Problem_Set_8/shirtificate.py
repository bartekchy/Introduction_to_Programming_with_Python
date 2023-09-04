from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering Shirt:
        self.image("shirtificate.png", 10, 70, 190)
        # Setting font: helvetica 30
        self.set_font("helvetica", size=50)
        # Printing title:
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def make_shirt(name):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 210, txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    make_shirt(name)


if __name__ == "__main__":
    main()
