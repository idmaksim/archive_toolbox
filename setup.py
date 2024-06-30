from setuptools import setup, find_packages

setup(
    name='archive_toolbox',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'atb = archive_tollbox.main:main',
        ],
    },
    install_requires=[
        'pyfiglet==1.0.2',
    ],
    author='Dementev Maksim',
    author_email='i@dmaksim.ru',
    description='A toolbox for managing archives',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/idmaksim/archive_toolbox',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
