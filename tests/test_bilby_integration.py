import sys

import bilby
import pytest


def test_sampling_cpnest(
    bilby_gaussian_likelihood_and_priors, tmp_path, n_pool
):
    likelihood, priors = bilby_gaussian_likelihood_and_priors
    outdir = tmp_path / "test_sampling_cpnest"

    if n_pool is not None and not sys.platform.startswith("linux"):
        pytest.skip("Skipping multiprocessing test on Windows and macOS")

    # Signal handling doesn't work with Windows
    resume = False if sys.platform.startswith("win") else True

    bilby.run_sampler(
        outdir=outdir,
        label="gaussian_cpnest",
        sampler="cpnest",
        likelihood=likelihood,
        priors=priors,
        nlive=100,
        n_pool=n_pool,
        resume=resume,
    )
