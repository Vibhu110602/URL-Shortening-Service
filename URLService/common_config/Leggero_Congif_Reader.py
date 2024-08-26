import os
from xml.etree import ElementTree


class XMLToDictLG(dict):

    def __init__(self, tree_root):
        super().__init__()
        for node in tree_root:
            if not len(node):
                self.update({node.tag: node.text})
            else:
                self.update({node.tag: XMLToDictLG(node)})


class LGConfig:

    def __init__(self):
        tree = ElementTree.parse(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Leggero_Config.xml'))
        root = tree.getroot()
        self.xml2dict_obj = XMLToDictLG(root)

    def get_config(self):
        return self.xml2dict_obj


# if __name__ == "__main__":
#     obj = LGConfig()
#     print(obj.get_config()['DB']['schema'])
