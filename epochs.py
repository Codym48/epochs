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
j2000_in_tt = spiceypy.timout(0, "YYYY-MM-DDTHR:MN:SC.############ ::TT")

# Convert the Unix time epoch into TDB
unix_s_past_j2000 = spiceypy.str2et("00:00:00 UTC 1 January 1970")
unix_in_tdb = spiceypy.timout(
    unix_s_past_j2000, "YYYY-MM-DDTHR:MN:SC.############ ::TDB"
)
unix_in_utc = spiceypy.timout(
    unix_s_past_j2000, "YYYY-MM-DDTHR:MN:SC.############ ::UTC"
)
unix_in_tt = spiceypy.timout(unix_s_past_j2000, "YYYY-MM-DDTHR:MN:SC.############ ::TT")

# (https://en.wikipedia.org/wiki/Unix_time#Variant_that_counts_leap_seconds) "Because
# TAI has no leap seconds, and every TAI day is exactly 86400 seconds long, this
# encoding is actually a pure linear count of seconds elapsed since
# 1970-01-01T00:00:10 TAI (1970-01-01T00:00:00 UTC)"
print(-unix_s_past_j2000)
