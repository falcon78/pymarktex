from distutils.core import setup

setup(
    name             = 'pymarktex',
    version          = '1.0.4',
    description      = 'Will convert a markdown text file to a fancy PDF document',
    license          = 'MIT',
    url              = 'http://github.com/xapple/pymarktex/',
    author           = 'Lucas Sinclair',
    author_email     = 'lucas.sinclair@me.com',
    packages         = ['pymarktex', 'pymarktex.figures', 'pymarktex.templates'],
    scripts          = ['scripts/pymarktex'],
    install_requires = ['sh', 'pystache'],
    long_description = open('README.md').read(),
)