"""
Usage:
    python setup.py py2app
"""

from setuptools import setup


setup(
    app=['launch_neovim_in_iterm2.py'],
    name='Neovim',
    options={
        'py2app': {
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
    },
    setup_requires=['py2app'],
)
