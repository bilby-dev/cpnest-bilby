import sys

import bilby


def test_sampling_cpnest(
    bilby_gaussian_likelihood_and_priors, tmp_path, npool
):
    likelihood, priors = bilby_gaussian_likelihood_and_priors
    outdir = tmp_path / "test_sampling_cpnest"

    # Signal handling doesn't work with Windows
    resume = False if sys.platform.startswith("win") else True

    bilby.run_sampler(
        outdir=outdir,
        label="gaussian_cpnest",
        sampler="cpnest",
        likelihood=likelihood,
        priors=priors,
        nlive=100,
        npool=npool,
        resume=resume,
    )
