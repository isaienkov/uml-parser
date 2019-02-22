import os
import shutil
from content_types import ContentType
from rels import Rels


def create_rels():
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
    return a.get_xml()


def create_document_rels():
    a = Rels()
    a.add(
        Id="rId2",
        Type="http://schemas.microsoft.com/visio/2010/relationships/windows",
        Target="windows.xml")
    a.add(
        Id="rId1",
        Type="http://schemas.microsoft.com/visio/2010/relationships/pages",
        Target="pages/pages.xml")
    return a.get_xml()


def create_pages_rels():
    a = Rels()
    a.add(
        Id="rId1",
        Type="http://schemas.microsoft.com/visio/2010/relationships/page",
        Target="page1.xml")
    return a.get_xml()


def create(filename, path='generates/'):
    folders = ['_rels', 'docProps', 'visio', 'visio/_rels', 'visio/pages', 'visio/pages/_rels']
    archive_path = '{}{}'.format(path, filename)
    os.makedirs(archive_path)
    for folder in folders:
        os.makedirs('{}/{}'.format(archive_path, folder))

    content_type = ContentType().get_xml()

    with open(archive_path + '/[Content_Types].xml', 'w') as f:
        f.write(content_type)

    with open(archive_path + '/_rels/.rels', 'w') as f:
        f.write(create_rels())

    with open(archive_path + '/docProps/app.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/core.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/custom.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/thumbnail.emf', 'w') as f:
        pass

    with open(archive_path + '/visio/_rels/document.xml.rels', 'w') as f:
        f.write(create_document_rels())

    with open(archive_path + '/visio/pages/_rels/pages.xml.rels', 'w') as f:
        f.write(create_pages_rels())

    with open(archive_path + '/visio/pages/page1.xml', 'w') as f:
        pass

    with open(archive_path + '/visio/pages/pages.xml', 'w') as f:
        pass

    with open(archive_path + '/visio/document.xml', 'w') as f:
        pass

    with open(archive_path + '/visio/windows.xml', 'w') as f:
        pass

    shutil.make_archive(archive_path, 'zip', archive_path)
    shutil.rmtree(archive_path, ignore_errors=True)
    os.rename(archive_path + '.zip', archive_path + '.vsdx')


create('test_2019-02-22_1')