# Introduction #

- *Version*: 0.1
- *Authors*: Sven Brauch, Benjamin Winkel

# Purpose#

`pyfitsviewer` is a lightweight tool that is used to look into [FITS](https://en.wikipedia.org/wiki/FITS) files. It is similar to the [fv](http://heasarc.gsfc.nasa.gov/ftools/fv/) tool, but based on a modern widget system (Qt).

# Features

* Shows structure of FITS files (headers and data of the so-called HDUs)
* Provides simple plotting functionality for tables

Note, that image data is currently not displayed, but this is planned for a future release.

# Usage #

### Installation ###

TODO

### Starting the pyfitsviewer ###

After installation, you can use the `pyfv` start script to run pyfitsviewer.

### Dependencies ###

Dependencies are kept as minimal as possible. The following packages are
required:
* `PyQt4`
* `numpy>=1.10`
* `numpy>=1.8`
* `matplotlib>=1.4`
* `astropy>=1.0`

### Examples ###

TODO

### Who do I talk to? ###

If you encounter any problems or have questions, do not hesitate to raise an
issue or make a pull request. Moreover, you can contact the dev directly:

* <mail@svenbrauch.de>
* <bwinkel@mpifr.de>

### Contributions ###

Contributions are more than welcome.
