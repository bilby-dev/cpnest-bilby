import pytest
from bilby.core.sampler.base_sampler import NestedSampler

from cpnest_bilby.plugin import CPNest


@pytest.fixture()
def create_sampler(bilby_gaussian_likelihood_and_priors, tmp_path):
    likelihood, priors = bilby_gaussian_likelihood_and_priors

    def create_fn(**kwargs):
        return CPNest(
            likelihood,
            priors,
            outdir=tmp_path / "outdir",
            label="test",
            **kwargs,
        )

    return create_fn


@pytest.fixture(params=NestedSampler.npoints_equiv_kwargs)
def npoints_name(request):
    return request.param


def test_default_kwargs(create_sampler):
    sampler = create_sampler()
    expected = dict(
        verbose=3,
        nthreads=1,
        nlive=500,
        maxmcmc=1000,
        seed=None,
        poolsize=100,
        nhamiltonian=0,
        resume=True,
        output=f"{sampler.outdir}/cpnest_{sampler.label}/",
        proposals=None,
        n_periodic_checkpoint=8000,
    )
    assert sampler.kwargs == expected


def test_translate_kwargs_nlive(create_sampler, npoints_name):
    sampler = create_sampler(**{npoints_name: 250})
    expected = dict(
        verbose=3,
        nthreads=1,
        nlive=250,
        maxmcmc=1000,
        seed=None,
        poolsize=100,
        nhamiltonian=0,
        resume=True,
        output=f"{sampler.outdir}/cpnest_{sampler.label}/",
        proposals=None,
        n_periodic_checkpoint=8000,
    )
    assert sampler.kwargs == expected


def test_translate_kwargs_npool(create_sampler):
    sampler = create_sampler(npool=4)
    expected = dict(
        verbose=3,
        nthreads=4,
        nlive=500,
        maxmcmc=1000,
        seed=None,
        poolsize=100,
        nhamiltonian=0,
        resume=True,
        output=f"{sampler.outdir}/cpnest_{sampler.label}/",
        proposals=None,
        n_periodic_checkpoint=8000,
    )
    assert sampler.kwargs == expected
