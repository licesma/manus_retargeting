# Repository for Retargeting Manus gloves to a Dextrous Hand

## Setup

Create and activate the conda environment:
```bash
conda create -n manus_retargeting python=3.10 -y
```
```bash
conda activate manus_retargeting
```

Install pinocchio via conda (not available on PyPI):
```bash
conda install -c conda-forge pinocchio -y
```

Install remaining dependencies:
```bash
pip install -r requirements.txt
```