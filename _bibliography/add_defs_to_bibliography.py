# this converts these entries in a bibtex file:
#      journal = {\mnras},
# ...to the expanded version

import re 
from pathlib import Path

bib_original = 'papers_original.bib'
bib_out = 'papers.bib'

# figlet -d github/figlet-fonts -f "ANSI Shadow" bib proc 
print('''
██████╗ ██╗██████╗     ██████╗ ██████╗  ██████╗  ██████╗
██╔══██╗██║██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║██████╔╝    ██████╔╝██████╔╝██║   ██║██║
██╔══██╗██║██╔══██╗    ██╔═══╝ ██╔══██╗██║   ██║██║
██████╔╝██║██████╔╝    ██║     ██║  ██║╚██████╔╝╚██████╗
╚═════╝ ╚═╝╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝
''')
# read in all the definitions of journals into a dict
# Using readlines()
file1 = open('aas_journals.cls', 'r')
Lines = file1.readlines()

jour = {}
p = re.compile(r'command(\\.*)\{\\ref@jnl\{(.*)\}\}') # finds the macro and the replacement text
for l in Lines:
    if 'newcommand' in l:
        # from after the word 'command' to the first { that's the command
        m = p.search(l)
        jour[m.group(1)] = m.group(2)

# read in bibtex file
fbib = open(bib_original, 'r')
bibs = fbib.readlines()

# put in article full name
p = re.compile(r'journal.*\{(.*)\}') # find the journal key line
c = 0 # line counter
nj = 0 # journal counter
out=[]
for l in bibs:
    c=c+1
    if 'journal' in l:
        nj=nj+1
        m = p.search(l)
        journal = m.group(1)
        # replace the label into the current line
        try:
            newl = l.replace(journal,jour[journal])
            l = newl
        except:
            print(f'WARNING: that did not work, keeping it as {journal}')
            True
#    l = l.rstrip('\n')        
    out.append(l)

print(f'{c} lines scanned')
print(f'{nj} journals replaced')

# pdf={......},

# preview={asdf.png},
 #       preview = {2020MNRAS.492..431B.jpg},
#        additional_info = {. The solar mass star TYC 8998 and its planetary mass companion TYC 8998b, indicated by a white arrow.},
#              pdf = {https://home.strw.leidenuniv.nl/kenworthy/papers/2020MNRAS.492..431B.pdf},


c = 0
out2=[]
p = re.compile('abs\/(.*)\}')
pdfurl = r'https://home.strw.leidenuniv.nl/\%7Ekenworthy/papers/'
for l in out:
    c=c+1
    out2.append(l)

    if 'adsurl' in l:
        # grep out this: adsurl = {https://ui.adsabs.harvard.edu/abs/2024A&A...687A..11V},
        m = p.search(l)
        adsbib = m.group(1) # 2024A&A...687A..11V
        pdfloc = f'{pdfurl}{adsbib}.pdf'
        out2.append(f'\t\t  pdf = {{{pdfloc}}},\n')

        file = Path(f'../assets/img/publication_preview/{adsbib}.png')
        if file.is_file():
            out2.append(f'\t  preview = {{{adsbib}.png}},\n')
        else:
            file = Path(f'../assets/img/publication_preview/{adsbib}.jpg')
            if file.is_file():
                out2.append(f'\t  preview = {{{adsbib}.jpg}},\n')


print(f'Writing modified bibtex file: {bib_out}')
# writing to file
file1 = open(bib_out, 'w')
file1.writelines(out2)
file1.close()


