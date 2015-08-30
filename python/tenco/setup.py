# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='tenco',
    version='0.1.0',
    license='MIT License',
    packages=['tenco'],
    download_url='https://github.com/ymizushi/tenco/archive/master.zip',
    platforms=['POSIX'],
    description='https://github.com/ymizushi/tenco',
    author='ymizushi',
    author_email='mizushi@gmail.com',
    url='https://github.com/ymizushi/tenco',
    keywords=['japanese', 'tenji', 'braille'],
    scripts=['scripts/tenco'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Software Development',
    ],
    long_description='',
    requires=['flask'],
)
