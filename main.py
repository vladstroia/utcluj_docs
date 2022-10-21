from docxtpl import DocxTemplate

import pandas as pd
df = pd.read_csv('template_plan_invatamant.csv')
doc = DocxTemplate("template-fisa-disciplinei.docx")
context = {}
for i in df:
    context[i] = df[i]


doc.render(context)
doc.save("generated_doc.docx")