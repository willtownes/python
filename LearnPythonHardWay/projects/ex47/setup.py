try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Practice script',
    'author': 'Will Townes',
    'url': 'https://github.com/willtownes/python',
    'download_url': 'Coming soon...',
    'author_email': 'will.townes@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)