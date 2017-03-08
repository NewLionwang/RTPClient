from distutils.core import setup
import py2exe

setup(
    console=['Base.py'],
    options = {
        'py2exe': {
            'includes': 'decimal',
            }
        }
    
    )