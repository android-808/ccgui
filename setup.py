try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='ccgui',
    version='0.2.0',
    packages = find_packages(exclude=["docs", "tests"]),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        'ccgui': ['data/pixmaps/*.png'],
        '':['*.png'],
    },
    include_package_data = True,
    
    #install_requires=["pygobject"],

    entry_points="""
     [console_scripts]
     ccgui = ccgui.ccgui:main
     """,

    # Metadata for PyPI
    author='Robert Irvin',
    author_email='android_808@hotmail.com',
    description='GUI configuration wizard for conky-colors.',
    license='Unknown',
    keywords = "conky colors wizard",
    url='www.example.com',
)
