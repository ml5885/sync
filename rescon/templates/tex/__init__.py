
        
    

import subprocess

def main():
    ttm = TexTemplate("/home/tanush/Programming/Projects/rescon/rescon/templates/tex/func.ttx")
    # ttx = "".join(ttm.file.readlines())
    # print(ttx[ttx.find("{% begin tag"): ttx.find("{% begin tag") + 100])
    # print(re.match("^{%.*%}$", ttx))
    # print(ttx)
    rf = open("/home/tanush/Programming/Projects/rescon/rescon/templates/tex/tmp.xml", "r")
    wf = open("/home/tanush/Programming/Projects/rescon/rescon/templates/tex/CATERED.tex", "w")
    et_xml = ET.fromstring(rf.read())
    ttm.modify(et_xml, wf)
    subprocess.Popen(["./generate_pdf.sh"], shell=True)

if __name__ == "__main__":
    main()