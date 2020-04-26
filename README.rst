****************************
Mopidy-SeeedRelays
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-SeeedRelays
    :target: https://pypi.org/project/Mopidy-SeeedRelays/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/circleci/build/gh/rmichalak/mopidy-seeedrelays
    :target: https://circleci.com/gh/rmichalak/mopidy-seeedrelays
    :alt: CircleCI build status

.. image:: https://img.shields.io/codecov/c/gh/rmichalak/mopidy-seeedrelays
    :target: https://codecov.io/gh/rmichalak/mopidy-seeedrelays
    :alt: Test coverage

Mopidy extension to drive relays on Seeed Relay board (http://wiki.seeedstudio.com/Raspberry_Pi_Relay_Board_v1.0/)

Turns on selected relay on playback start and turns it off on playback end.
You can use it to turn on/off your amplifier.

Installation
============

Install by running::

    cd ~
    git clone https://github.com/rmichalak/mopidy-seeedrelays.git
    cd mopidy-seeedrelays
    sudo python setup.py develop

Alternatively for a local installation you can change the last line to::

    python setup.py install --user

Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-SeeedRelays to your Mopidy configuration file::

    [relays]
    i2c = 1            # (default) i2c bus with board connected
    address = 0x20     # (default) board address
    relay=1            # (required) relay number to control

For board settings, please refer to http://wiki.seeedstudio.com/Raspberry_Pi_Relay_Board_v1.0/

Project resources
=================

- `Source code <https://github.com/rmichalak/mopidy-seeedrelays>`_
- `Issue tracker <https://github.com/rmichalak/mopidy-seeedrelays/issues>`_
- `Changelog <https://github.com/rmichalak/mopidy-seeedrelays/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `Robert Michalak <https://github.com/rmichalak>`__
- Current maintainer: `Robert Michalak <https://github.com/rmichalak>`__
- `Contributors <https://github.com/rmichalak/mopidy-seeedrelays/graphs/contributors>`_
