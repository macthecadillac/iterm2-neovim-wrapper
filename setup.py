"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Neovim.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'AppIcon.icns',
    'argv_emulation': True,
    'plist': {
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'NSStringPboardType',
                'CFBundleTypeRole': 'Editor',
                'LSIsAppleDefaultForType': True,
                'LSItemContentTypes': ['public.text'],
                'NSDocumentClass': 'Document',
            },
            {
                'CFBundleTypeName': 'NSStringPboardType',
                'CFBundleTypeRole': 'Editor',
                'LSIsAppleDefaultForType': True,
                'LSItemContentTypes': ['public.plain-text'],
                'NSDocumentClass': 'Document',
                'NSIsRelatedItemType': True,
            },
            {
                'CFBundleTypeName': 'Apple SimpleText document',
                'CFBundleTypeRole': 'Viewer',
                'LSIsAppleDefaultForType': True,
                'LSItemContentTypes': ['com.apple.traditional-mac-plain-text'],
                'NSDocumentClass': 'Document',
            },
            {
                'CFBundleTypeName': 'Unknown document',
                'CFBundleTypeRole': 'Viewer',
                'LSIsAppleDefaultForType': True,
                'LSItemContentTypes': ['public.data'],
                'NSDocumentClass': 'Document',
            },
        ]
    }
}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
