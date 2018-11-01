import os
import xml.etree.ElementTree as et

# variavel = retorna o diretorio como string
base_path = os.path.dirname(os.path.realpath(__file__))

# join base_path with data folder.
# variavel = caminho string + nome do arquivo

xml_file = os.path.join(base_path, "RYAN OLIVEIRA.xml")

# variavel guarda o xml file dentro da memoria
tree = et.parse(xml_file)

root = tree.getroot()

print()
print()

for e1 in root:
    # print(e1.text)
    for e2 in e1:
        # print(e2.text)
        for e3 in e2:
            #   print(e3.text)
            for e4 in e3:
                # print(e4.text)
                for e5 in e4:
                    # print(e5.text)
                    for e6 in e5.iter('value'):
                        print(e6.text)
                        for e7 in e6.iter('value'):
                            print(e7.text)
                            # for e8 in e7.iter('value'):
                            #   print(e8.text)
