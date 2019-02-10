import os
import shutil


def create(filename, path='generates/'):
    folders = ['_rels', 'docProps', 'visio', 'visio/_rels', 'visio/pages', 'visio/pages/_rels']
    archive_path = '{}{}'.format(path, filename)
    os.makedirs(archive_path)
    for folder in folders:
        os.makedirs('{}/{}'.format(archive_path, folder))

    with open(archive_path + '/[Content_Types].xml', 'w') as f:
        pass

    with open(archive_path + '/_rels/.rels', 'w') as f:
        pass

    with open(archive_path + '/docProps/app.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/core.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/custom.xml', 'w') as f:
        pass

    with open(archive_path + '/docProps/thumbnail.emf', 'w') as f:
        pass

    with open(archive_path + '/visio/_rels/document.xml.rels', 'w') as f:
        pass

    with open(archive_path + '/visio/pages/_rels/pages.xml.rels', 'w') as f:
        pass

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


create('test')