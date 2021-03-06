from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name="django_b2storage",
    version='1.0',
    description='A backblaze b2 storage system for django',
    long_description=readme(),
    keywords='backblaze b2 django storage media',
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
    url='https://github.com/amlatyrngom/django-b2storage',
    author='Amadou Latyr Ngom',
    author_email='amlatyr.ngom@gmail.com',
    licence='MIT',
    packages=['django_b2storage'],
    install_requires=[
        'Django >= 1.9',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    zip_safe=False
)
