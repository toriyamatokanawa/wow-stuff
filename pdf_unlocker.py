import glob, os, pikepdf

p = os.getcwd()
for file in glob.glob('*.pdf'):
    file_path = os.path.join(p, file).replace('\\','/')
    init_pdf = pikepdf.open(file_path)
    new_pdf = pikepdf.new()
    new_pdf.pages.extend(init_pdf.pages)
    new_pdf.save(str(file))



