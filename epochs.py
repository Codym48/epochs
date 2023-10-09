# Calculate the offset between the Unix epoch (https://en.wikipedia.org/wiki/Unix_time)
# and J2000 (https://en.wikipedia.org/wiki/Epoch_(astronomy)#Julian_years_and_J2000)
# using the NAIF SPICE Toolkit (https://naif.jpl.nasa.gov/naif/toolkit.html)

# Python wrapper for the C SPICE Toolkit (https://github.com/AndrewAnnex/SpiceyPy)
import spiceypy

# Load the leapseconds kernel, which is required for ET↔UTC conversions, downloaded from
# (https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/)
spiceypy.furnsh("naif0012.tls.pc")

# Some notes on time systems:
#   UTC = TAI - 37s (after 1 January 2017)
#   TAI = TT - 32.184s
#   TT == TDT
#   ET == TDB = TT + 0.001658s * sin(E)

# What is the J2000 epoch used by SPICE?
j2000_in_tdb = spiceypy.timout(0, "YYYY-MM-DDTHR:MN:SC.############ ::TDB")
j2000_in_utc = spiceypy.timout(0, "YYYY-MM-DDTHR:MN:SC.############ ::UTC")
j2000_in_tdt = spiceypy.timout(0, "YYYY-MM-DDTHR:MN:SC.############ ::TDT")
j2000_tdt = spiceypy.unitim(0, "TDB", "TDT")
j2000_tai = spiceypy.unitim(0, "TDB", "TAI")
print([0, j2000_tdt, j2000_tai])

# Convert the Unix time epoch into TDB
unix_tdb = spiceypy.str2et("00:00:00 UTC 1 January 1970")
unix_in_tdb = spiceypy.timout(unix_tdb, "YYYY-MM-DDTHR:MN:SC.############ ::TDB")
unix_in_utc = spiceypy.timout(unix_tdb, "YYYY-MM-DDTHR:MN:SC.############ ::UTC")
unix_in_tdt = spiceypy.timout(unix_tdb, "YYYY-MM-DDTHR:MN:SC.############ ::TDT")
unix_tdt = spiceypy.unitim(unix_tdb, "TDB", "TDT")
unix_tai = spiceypy.unitim(unix_tdt, "TDT", "TAI")
print([unix_tdb, unix_tdt, unix_tai])

# Calculate offset between J2000 epoch and Unix time epoch
j2000_since_unix_epoch = 0 - unix_tdb
j2000_since_unix_epoch = j2000_tdt - unix_tdt
j2000_since_unix_epoch = j2000_tai - unix_tai
print(j2000_since_unix_epoch)
