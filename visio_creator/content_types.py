from bs4 import BeautifulSoup


class ContentType:
    def __init__(self):
        self.soup = BeautifulSoup('', 'xml')
        self.root = self.soup.new_tag(
            'Types',
            xmlns="http://schemas.openxmlformats.org/package/2006/content-types"
        )
        self.soup.append(self.root)

        self.add_default("emf", "image/x-emf")
        self.add_default("rels", "application/vnd.openxmlformats-package.relationships+xml")
        self.add_default("xml", "application/xml")
        self.add_override("/visio/document.xml", "application/vnd.ms-visio.drawing.main+xml")
        self.add_override("/visio/pages/pages.xml", "application/vnd.ms-visio.pages+xml")
        self.add_override("/visio/pages/page1.xml", "application/vnd.ms-visio.page+xml")
        self.add_override("/visio/windows.xml", "application/vnd.ms-visio.windows+xml")
        self.add_override("/docProps/core.xml", "application/vnd.openxmlformats-package.core-properties+xml")
        self.add_override("/docProps/app.xml", "application/vnd.openxmlformats-officedocument.extended-properties+xml")
        self.add_override("/docProps/custom.xml", "application/vnd.openxmlformats-officedocument.custom-properties+xml")

    def add_default(self, extension, content_type):
        self.add_tag('Default', Extension=extension, ContentType=content_type)

    def add_override(self, part_name, content_type):
        self.add_tag('Override', PartName=part_name, ContentType=content_type)

    def add_tag(self, tag, **attributes):
        self.root.insert(len(self.root.contents),
                         self.soup.new_tag(tag, **attributes))

    def get_xml(self):
        return self.soup.prettify()


if __name__ == '__main__':
    a = ContentType()
    print(a.get_xml())