'''import fitz
print(fitz.__doc__)   
dope = fitz.open('./dope/dope.pdf')
dope_file = open('./dope/dope.html', '+w')
for i in range(dope.page_count):
    print(f"Imprimindo página {i}")
    page = dope.load_page(i).get_text('html')
    dope_file.write(page)
dope_file.close()


'''
import fitz
print(fitz.__doc__)   
dope = fitz.open('./dope/dope.pdf')
page0 = dope.load_page(0)
dope_html_0 = page0.get_text()
dope_file = open('./dope/dope0.txt', '+w',  encoding="iso-8859-1")
dope_file.write(dope_html_0)
dope_file.close()

