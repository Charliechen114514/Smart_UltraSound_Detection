
# Start from the Raw Source

If you wanna start by merging(or forking) the project in your own, you should install the torch as the following, your machine requires the following hardware including Nvidia GPU, and its drivers including CUDA 12.4 or above:), after ensuring you have the above hardware and drivers...

## Building In Conda

you should use conda or the other python env manager to setup a new env. remember that python 3.12 above is required.

```
conda create --prefix="path/to/your/target/install/path" python=3.12
```

### Manage in conda

to install the correct version of torch, you are supposed to add the source url of torch, then you are supposed download the dependency currently required.

### Use Conda package manager to manage

in conda, install torch is easy:

```
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

```

and Pyside6(Qt in Python) is also required in this project

```
conda install conda-forge::pyside6
```

### Use Poetry to manage

```
# We currently depend on torch with cuda124 version
poetry source add --priority explicit pytorch https://download.pytorch.org/whl/cu124
poetry add --source pytorch torch torchvision torchaudio
```
