zabbix-template-converter
=========================

This Python script aims to resolve compatability issues when migrating Zabbix
template XML files between versions of Zabbix. For example, you may wish to
import a Zabbix v3.2 template into Zabbix v2.0.

The script works by applying conversion rules to a template, which manipulate
the template XML to match the desired Zabbix version template format.

Installation
------------

Install the Python script to ``/usr/local/bin`` with pip:

.. code-block:: shell

    $ pip install zabbix-template-converter

Usage
-----

.. code-block:: shell

    $ zabbix-template-convertor -h
    usage: zabbix-template-convertor [-h] [-v] -o X.Y.Z [-s] file

    Migrate Zabbix templates between versions

    positional arguments:
    file                  Zabbix template XML file

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -o X.Y.Z, --output-version X.Y.Z
                            target Zabbix version
    -s, --squash-value-maps
                            remove references to value maps for versions older
                            than 3.0.0

Examples
--------

To convert a Zabbix 3.2 template for import into v2.0:

.. code-block:: shell

    $ zabbix-template-convertor -o 2.0 my_template.xml > my_template-2.0.xml

A number of transformations will take place. For example, Discovery Rule
filters will be downgraded from the multiple-filter format introduced in Zabbix 2.4, to a single filter expression as follows:

.. code-block:: xml

    <filter>
        <evaltype>0</evaltype>
        <formula/>
        <conditions>
            <condition>
                <macro>{#IFNAME}</macro>
                <value>@Network interfaces for discovery</value>
                <operator>8</operator>
                <formulaid>A</formulaid>
            </condition>
        </conditions>
    </filter>

Becomes:

.. code-block:: xml

    <filter>{#IFNAME}:@Network interfaces for discovery</filter>

Coverage
--------

This project relies heavily on the community to report incompatibility problems
when importing templates. 

**Please raise an issue** if you find a template that won't import after being
converted. Be sure to include the error messages and template file.

Over time, as conversion rules are added, the script should become more
comprehensive, and more reliable.
