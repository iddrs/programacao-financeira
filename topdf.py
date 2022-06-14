'''
Converte para PDF

https://nbconvert.readthedocs.io/en/latest/removing_cells.html
'''

from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import PDFExporter
from nbconvert.preprocessors import TagRemovePreprocessor

# Setup config
c = Config()

# Força a execução do notebook antes de exportar
c.ExecutePreprocessor.enabled = True

# Configure tag removal - be sure to tag your cells to remove  using the
# words remove_cell to remove cells. You can also modify the code to use
# a different tag word
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)
c.TagRemovePreprocessor.enabled = True

# Configure and run out exporter
c.PDFExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

exporter = PDFExporter(config=c)
exporter.register_preprocessor(TagRemovePreprocessor(config=c),True)

# Configure and run our exporter - returns a tuple - first element with PDF,
# second with notebook metadata
output = PDFExporter(config=c).from_filename("Avaliação da Programação Financeira de 2022.ipynb")

# Write to output PDF file
with open("report.pdf",  "wb") as f:
    f.write(output[0])
