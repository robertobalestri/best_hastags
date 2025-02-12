from setuptools import setup, find_packages

setup(
    name='best_hashtags',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'best_hashtags=best_hashtags:main',
        ],
    },
    author='Roberto Balestri',
    author_email='roberto.balestri2@unibo.it',
    description='A simple hashtag scraper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/robertobalestri/best_hashtags',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)