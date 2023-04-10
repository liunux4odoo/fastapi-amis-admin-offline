import setuptools
from pathlib import Path


def readme():
    return Path(__file__).parent.absolute().joinpath('README.md').read_text()


setuptools.setup(
    name='fastapi-amis-admin-offline',
    version='0.1.0',
    author='liunux',
    author_email='liunux@qq.com',
    description='make fastapi & amis-admin work offline without CDN',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/love4odoo/fastapi-amis-admin-offline',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires='>=3.6',
    install_requires=[
        'fastapi',
    ],
    extras_requires={
        'amis': [
            'fastapi_amis_admin',
        ]
    }
)
