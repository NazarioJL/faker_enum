==========
Faker Enum
==========

 |travis_ci| |license| |code_style|

`faker_enum`_ is a provider for the `Faker`_ Python package.


-------
Summary
-------
Faker enum provides the ability to generate enum values based on an enum type.

>>>>>>
Usage
>>>>>>

.. code:: python

    from enum import Enum

    from faker import Faker
    from faker_enum import EnumProvider

    fake = Faker()
    fake.add_provider(EnumProvider)

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    fake.enum(Color)
    # One of [Color.RED, Color.GREEN, Color.BLUE]


.. |travis_ci| image:: https://img.shields.io/travis/NazarioJL/faker_web/master.svg?style=flat-square&label=unix%20build
    :target: http://travis-ci.org/NazarioJL/faker_enum
    :alt: Build status of the master branch

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/NazarioJL/faker_enum/blob/master/LICENSE
    :alt: MIT License
.. |code_style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: Black

.. _Faker: https://github.com/joke2k/faker
.. _faker_enum: https://github.com/NazarioJL/faker_enum
