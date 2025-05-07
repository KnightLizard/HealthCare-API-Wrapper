from setuptools import setup, find_packages

setup(
    name='healthcarepy',
    version='0.1.0',
    description='A library for interacting with healthcare data',
    author='Brandon Wilson',
    author_email='brandonaw2000@gmail.com',
    url='https://github.com/KnightLizard/healthcarepy',
    packages=find_packages(['healthcarepy']),
    install_requires=[
        'requests',
        'json'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Lnaguage :: English',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)

