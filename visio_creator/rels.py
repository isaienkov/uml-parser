from bs4 import BeautifulSoup


class Rels:
    def __init__(self):
        self.soup = BeautifulSoup('', 'xml')
        self.root = self.soup.new_tag(
            'Types',
            xmlns="http://schemas.openxmlformats.org/package/2006/relationships"
        )
        self.soup.append(self.root)

    def add(self, **attributes):
        self.root.insert(len(self.root.contents),
                         self.soup.new_tag('Relationship', **attributes))

    def get_xml(self):
        return self.soup.prettify()


if __name__ == '__main__':
    a = Rels()
    a.add(
        Id="rId3",
        Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
        Target="docProps/core.xml")
    a.add(
        Id="rId2",
        Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail",
        Target="docProps/thumbnail.emf")
    a.add(
        Id="rId1",
        Type="http://schemas.microsoft.com/visio/2010/relationships/document",
        Target="visio/document.xml")
    a.add(
        Id="rId5",
        Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
        Target="docProps/custom.xml")
    a.add(
        Id="rId4",
        Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
        Target="docProps/app.xml")
    print(a.get_xml())