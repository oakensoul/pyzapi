from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
]

setup(
    name='pyzapi',
    version='0.1dev',
    packages=['pyzapi', ],
    license='MIT',
    install_requires='requires',
    long_description=open('README.md').read(),
    entry_points="""\
    [paste.app_factory]
    main = pyzapi:main
    """
)
