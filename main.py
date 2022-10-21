from docxtpl import DocxTemplate

import pandas as pd
df = pd.read_csv('template_plan_invatamant.csv')
doc = DocxTemplate("template-fisa-disciplinei.docx")
for i in range(20):
    context = {}
    for item in df.loc[[i]]:
        context[item] =df.loc[[i]][item].values[0]
        if context[item] == 'nan':
            context[item] = ''
    doc.render(context)
    doc.save(f"./files/generated_doc{context['p1_8']}.docx")