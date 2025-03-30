from setuptools import setup, find_packages

setup(
    name='Clodd',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A client for interacting with Claude.ai API with Cloudflare bypass capabilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/Clodd',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'requests',
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)