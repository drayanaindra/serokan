from setuptools import setup


with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='serokan',
    version='0.1',
    download_url='https://github.com/drayanaindra/serokan.git',
    license='GNU',
    author='M Asep Indrayana - drayanaindra',
    author_email='di@colok.in',
    description='Indexing Builder for ElasticSearch',
    long_description=long_description,
    py_modules=['serokan'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'elasticsearch',
    ],
    classifiers=[
        'Environment :: Libray Package',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
