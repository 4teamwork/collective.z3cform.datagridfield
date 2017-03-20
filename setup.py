# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = '2.0.0.dev0'

setup(
    name='collective.z3cform.datagridfield',
    version=version,
    description='A DataGridField for use with plone.dexterity / z3c.form',
    long_description=(
        open("README.rst").read() +
        '\n' +
        open("CHANGES.rst").read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Plone, Dexterity, z3c.form, field, table, grid, multi',
    author='Kevin Gill',
    author_email='kevin@movieextras.ie',
    url='https://github.com/collective/collective.z3cform.datagridfield',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.z3cform'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.z3cform',
        'setuptools',
        'z3c.form >=2.4.3dev',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'collective.z3cform.datagridfield_demo',
            'unittest2',
            'transmogrify.dexterity',
        ]
    },
    entry_points="""
        # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
    """,
)
