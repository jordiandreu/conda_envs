#!/usr/bin/env python
import tango
import taurus
import sardana

print("tango {}".format(tango.__version__))
print("taurus {}".format(taurus.Release.version))
print("sardana {}".format(sardana.Release.version))
