# Notes
School project based on https://gitlab.com/MatthiasDeLozzo/n2pac

------

# The N2PAC project

N2PAC is a Python-based academic project proposed by Matthias De Lozzo and Thierry Druot
in the frame of the course **"Design of experiments and metamodels"**
from the [ModIA program](https://www.math.insa-toulouse.fr/fr/enseignement/apprentissage-modia.html).

It aims to design a liquid hydrogen powered aircraft from the libraries 
[MARILib](https://github.com/marilib/MARILib_obj) for aircraft modeling, 
[scikit-learn](https://github.com/scikit-learn/scikit-learn) for surrogate modeling,  
[OpenTURNS](https://github.com/openturns/openturns) for uncertainty quantification
and [GEMSEO](https://gitlab.com/gemseo/dev/gemseo) for process orchestration and optimization.

After compilation,
N2PAC turns into an HTML website starting with the presentation of the project and use case.
Appendices contain a quickstart section to learn the basics of the Python libraries codes used in this project
and an introduction to the reST syntax used to create the HTML pages.

The participants must solve this project by writing two types of deliverables:
a series of Python scripts and a code-free report.
These deliverables will appear in the HTML website as properly formatted pages.

For more information, please install the project.

## Install N2PAC


### 1. Clone or download the repository

Repository: https://gitlab.com/MatthiasDeLozzo/n2pac.

### 2. Install GEMSEO with a conda environment

Use one of these procedures by naming the environment **n2pac**: 

- [Linux or MacOS](https://gemseo.readthedocs.io/en/stable/software/installation.html#linux-or-macos),
- [Windows or Python 2.7](https://gemseo.readthedocs.io/en/stable/software/installation.html#windows-or-python-2-7), with the full features (*[all]* at the end of the *pip* or *conda* installation line).

Then,
install the Sphinx dependencies to compile the reST project: 

```bash
conda activate n2pac
conda install -c anaconda sphinx
conda install -c conda-forge sphinx-gallery
pip install furo [--user]
```

### 3. Fill in the names of authors

Go to line 23 in **project/conf.py**:

```python
author = Author1, Author2 and Author3'
```

### 4. Compile the project

```bash
cd project
make html
```

Open the webpage **project/build/html/index.html**.

The N2PAC adventure starts here!
