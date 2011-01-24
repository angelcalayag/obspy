# -*- coding: utf-8 -*-
"""
obspy.gse2 - GSE2 read and write support
========================================
This module provides read and write support for GSE2 CM6 compressed
waveform data and header info. Most methods are based on the C library
GSE_UTI of Stefan Stange, which is interfaced via Python ctypes.
See: http://www.orfeus-eu.org/Software/softwarelib.html#gse.

:copyright: The ObsPy Development Team (devs@obspy.org) & Stefan Stange
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)

Reading
-------
Similiar to reading any other waveform data format using obspy.core:

(Lines 2&3 are just to get the absolute path of our test data)

>>> from obspy.core import read
>>> from obspy.core import path
>>> filename = path("loc_RJOB20050831023349.z")
>>> st = read(filename)

You can also specify the following keyword arguments that change the
behavior of reading the file:

* headonly=True: Read only the header part, not the data part
* verify_chksum=False: Do not verify the checksum of the GSE2 file. This is
  very useful if the program, which wrote the checksum, calculated it in a
  wrong way. 

>>> st #doctest: +ELLIPSIS
<obspy.core.stream.Stream object at 0x...>
>>> print st
1 Trace(s) in Stream:
.RJOB..Z | 2005-08-31T02:33:49.849998Z - 2005-08-31T02:34:49.844998Z | 200.0 Hz, 12000 samples

The format will be determined automatically. Each trace (multiple 'WID2'
entries are mapped to multiple traces) will have a stats attribute
containing the usual information. When reading a GSE2 file it will have one
additional attribute: 'gse2'. This attribute contains all GSE2 specific
attributes:

>>> print st[0].stats #doctest: +NORMALIZE_WHITESPACE
         network: 
         station: RJOB
        location: 
         channel: Z
       starttime: 2005-08-31T02:33:49.849998Z
         endtime: 2005-08-31T02:34:49.844998Z
   sampling_rate: 200.0
           delta: 0.005
            npts: 12000
           calib: 0.0948999971151
         _format: GSE2
            gse2: AttribDict({'instype': '      ', 'datatype': 'CM6', 'hang': -1.0,
                              'auxid': 'RJOB', 'vang': -1.0, 'calper': 1.0})

The data are available via the data attribute.

>>> print st[0].data
[ 12 -10  16 ...,   8   0 -40]

Writing
-------
Writing is also done in the usual way:

>>> st.write('GSE2-filename.gse', format = 'GSE2') #doctest: +SKIP
"""

from obspy.core.util import _getVersionString


__version__ = _getVersionString("obspy.gse2")