Calculate the offset between the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time)
and [J2000](https://en.wikipedia.org/wiki/Epoch_(astronomy)#Julian_years_and_J2000)
using the [NAIF SPICE Toolkit](https://naif.jpl.nasa.gov/naif/toolkit.html)

Environment created and managed by Anaconda
```bash
conda create -n py311 python=3.11
conda activate py311
conda config --add channels conda-forge
conda install spiceypy

conda install flake8
conda install black
conda install isort
```

Run in VS Code via F5 or by calling
```bash
python epochs.py
```
