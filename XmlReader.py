from xml.etree.ElementTree import Element, SubElement, ElementTree


class LinkNote(object):
    head = ""
    url = ""


class XmlReader():
    def __init__(self):
        self.ET = ElementTree()
        self.ET.parse("fx1.xml")
        self.root = self.ET.getroot()

    def get_ln_list(self):
        link_list = []
        for i in self.root:
            ln = LinkNote()
            ln.head = i.find("head").text
            ln.url = i.find("URL").text
            link_list.append(ln)

        return link_list

# fil1 = XmlReader()
# lst = fil1.get_link_list()
# for i in range(0, len(lst)):
#     print(lst[i].head)
