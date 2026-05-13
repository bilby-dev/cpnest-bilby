import sys

import bilby
import pytest


def test_sampling_cpnest(
    bilby_gaussian_likelihood_and_priors, tmp_path, n_pool
):
    likelihood, priors = bilby_gaussian_likelihood_and_priors
    outdir = tmp_path / "test_sampling_cpnest"

    if n_pool > 1 and sys.platform.startswith("win"):
        pytest.skip(
            "Multiprocessing with n_pool > 1 is not supported on Windows."
        )

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
