import bilby


def test_sampling_cpnest(
    bilby_gaussian_likelihood_and_priors, tmp_path, n_pool
):
    likelihood, priors = bilby_gaussian_likelihood_and_priors
    outdir = tmp_path / "test_sampling_cpnest"
    bilby.run_sampler(
        outdir=outdir,
        label="gaussian_cpnest",
        likelihood=likelihood,
        priors=priors,
        nlive=100,
        n_pool=n_pool,
    )
