from docxtpl import DocxTemplate

doc = DocxTemplate("template-fisa-disciplinei.docx")
context = { 
'p1_8' : "salut",
'p2_1' : "salut",
'p2_2' : "salut",
'p2_3' : "salut",
'p2_4' : "salut",
'p2_5' : "salut",
'p2_6' : "salut",
'p2_7_a' : "salut",
'p2_8_b' : "salut", 
'p3_1' : "salut",
'p3_2' : "salut",
'p3_3_a' : "salut",
'p3_3_b' : "salut",
'p3_3_c' : "salut",
'p3_4' : "salut",
'p3_5' : "salut",
'p3_6_a' : "salut",
'p3_6_b' : "salut",
'p3_6_c' : "salut",
'p3_7_a' : "salut",
'p3_7_b' : "salut",
'p3_7_c' : "salut",
'p3_7_d' : "salut",
'p3_7_e' : "salut",
'p3_7_f' : "salut",
'p3_8' : "salut",
'p3_9' : "salut",
'p3_10' : "salut",
}
 


doc.render(context)
doc.save("generated_doc.docx")