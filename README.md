# cpnest-bilby

Plugin for using CPNest with bilby.

## Installation

The package can be install using pip

```
pip install cpnest-bilby
```

or conda

```
conda install conda-forge:cpnest-bilby
```

## Usage

Once `cpnest-bilby` is installed, it can be used directly via the `run_sampler` method in `bilby.

See the [CPNest documentation](https://johnveitch.github.io/cpnest/) for
details about the sampler settings.

## Changes compared to the original plugin

- Fix for multiprocessing when using `npool`.
