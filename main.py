from docxtpl import DocxTemplate

doc = DocxTemplate("template-fisa-disciplinei.docx")
context = { 'p1_8' : "World company",
'p2_1' : "World company",
'p2_2' : "World company",
'p2_3' : "World company",
'p2_4' : "World company",
'p2_5' : "World company",
'p2_6' : "World company",
'p2_7_a' : "World company",
'p2_8_b' : "World company", 
'p3_1' : "World company",
'p3_2' : "World company",
'p3_3_a' : "World company",
'p3_3_b' : "World company",
'p3_3_c' : "World company",
'p3_4' : "World company",
'p3_5' : "World company",
'p3_6_a' : "World company",
'p3_6_b' : "World company",
'p3_6_c' : "World company",
'p3_7_a' : "World company",
'p3_7_b' : "World company",
'p3_7_c' : "World company",
'p3_7_d' : "World company",
'p3_7_e' : "World company",
'p3_7_f' : "World company",
'p3_8' : "World company",
'p3_9' : "World company",
'p3_10' : "World company",
}
 


doc.render(context)
doc.save("generated_doc.docx")