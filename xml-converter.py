import os
import xml.etree.ElementTree as et


# variavel = retorna o diretorio como string
base_path = os.path.dirname(os.path.realpath(__file__))

# join base_path with data folder.
#variavel = caminho string + nome do arquivo

xml_file = os.path.join(base_path, "read.xml")

# variavel guarda o xml file dentro da memoria
tree = et.parse(xml_file)

root = tree.getroot()
print()
print()

#print(root)
#print(root.tag)
#print(root.attrib)
#print(root.tag, root.attrib)


"""
#listando in root
for child in root:
    print(child.tag ,child.attrib)
"""
"""
#listando todos os elementos
for child in root:
    print()
    for element in child:
        print(element.tag, ":", element.text)
"""
"""
#imprimindo um elemento
print(root[1][1].text)
"""


#Buscando um elemento de interesse

#for c in root.iter('value'):
 #     print(c.text)

for e in root.findall("RYAN"):
      print(e.text)