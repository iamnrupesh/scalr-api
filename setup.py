import os
from setuptools import find_packages, setup

with open(os.path.join('scalr', 'VERSION')) as file:
    version = file.read().strip()

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='scalr-api',
    description='Scalr REST API Python Wrapper',
    long_description=long_description,
    version=version,
    license='MIT',
    author='Nrupesh Patel',
    author_email='nrupesh.patel2912@gmail.com',
    url='https://github.com/Nrupesh29/scalr-api',
    download_url='https://github.com/Nrupesh29/scalr-api',
    keywords='scalr infrastructure software rest api',
    packages=find_packages(),
    package_dir={'scalr': 'scalr'},
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pytz"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
