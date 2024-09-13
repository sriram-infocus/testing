from setuptools import setup, find_packages

setup(
    name='aetrex_daemon',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'SQLAlchemy',
    ],
    entry_points={
        'console_scripts': [
            'run-app=app.main:run_app',  # Ensure this matches the actual function and module
        ],
    },
    # Optional metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amit-infocus/python-setup',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
