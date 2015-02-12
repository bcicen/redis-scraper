import os
import shutil
from setuptools import setup, find_packages
from redis_scraper import __version__

requires = [
    'redis',
    ]

setup(name='redis_scraper',
        version=__version__,
        description='redis_scraper',
        long_description='',
        author='Bradley Cicenas',
        author_email='bradley.cicenas@gmail.com',
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires,
        tests_require=requires,
        entry_points = {
        'console_scripts' : [ 'redis-scraper = redis_scraper.scraper:main' ]
        }
)
