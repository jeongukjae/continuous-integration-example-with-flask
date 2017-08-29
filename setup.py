from setuptools import setup, find_packages

setup(
    name='Flask-CI-Example',
    packages=find_packages(),
    version='0.1',
    long_description=__doc__,
    zip_safe=False,
    test_suite='nose.collector',
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'Flask==0.12.2',
        'Flask-WTF==0.14.2',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'Werkzeug==0.12.2',
        'WTForms==2.1',
    ],
    tests_require=['nose'],
)