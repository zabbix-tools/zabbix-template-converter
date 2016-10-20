# zabbix-template-convertor

This Python script aims to resolve compatability issues when migrating Zabbix
template XML files between versions of Zabbix. For example, you may wish to
import a Zabbix v3.2 template into Zabbix v2.0.

The script works by applying conversion rules to a template, which manipulate
the template XML to match the desired Zabbix version template format.

To convert a Zabbix 3.2 template for import into v2.0:

    $ zabbix-template-convertor -o 2.0 my_template.xml > my_template-2.0.xml

__WARNING__: This project is still under active development and not ready for
             release.

```
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

```


## Coverage

This project relies heavily on the community to report incompatability problems
when importing templates. 

__Please raise an issue__ if you find a template that won't import after being
converted. Be sure to include the error messages and template file.

Over time, as conversion rules are added, the script should become more comprehensive, and more reliable.


## Installation

Copy the script file to your bin directory and add the executable flag:

    $ curl -Lo /bin/zabbix-template-convertor \
        https://raw.githubusercontent.com/cavaliercoder/zabbix-template-convertor/master/zabbix-template-convertor
    $ chmod +x /bin/zabbix-template-convertor


## License

Copyright (c) 2015 Ryan Armstrong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
