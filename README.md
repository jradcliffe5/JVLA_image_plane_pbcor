## JVLA image plane primary beam correction

Usage: `casa -c pbcor_CASA.py <msfile> <image>`

where `msfile` should be replaced by the measurement set in order to generate the correct VLA primary beam and `<image>` should be replaced by the non-pb corrected image.

Nb. This should work for any array which has primary beam models in CASA. However, it has only been tested on JVLA & VLA data
