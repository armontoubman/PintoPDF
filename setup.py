from distutils.core import setup

try:
    import py2exe
except ImportError:
    pass

try:
    import py2app
except ImportError:
    pass

py2exe_options = dict(
    excludes=['_ssl',  # Exclude _ssl
              'pyreadline', 'difflib', 'doctest', 'locale',
              'optparse', 'pickle', 'calendar'],  # Exclude standard library
    dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
    compressed=True,  # Compress library.zip
    bundle_files=2,
)

py2app_options = dict(
    argv_emulation=True
)

setup(
    name='PintoPDF',
    version='1.0',
    description='<Description>',
    author='Armon Toubman',
    url='http://github.com/armontoubman/PintoPDF/',
    windows=['pintopdf.py'],
    options={'py2exe': py2exe_options,
             'py2app': py2app_options},
    app=['pintopdf.py'],
    data_files=[]
)
