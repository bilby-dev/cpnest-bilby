import array

from cpnest.model import Model as BaseCPNestModel
from cpnest.parameter import LivePoint


class Model(BaseCPNestModel):
    """A wrapper class to pass our log_likelihood into cpnest

    Parameters
    ==========
    names: list
        The names of the parameters to sample over
    priors: dict
        The bilby priors.
    bilby_log_likelihood: func
        The bilby log likelihood function.
    bilby_log_prior: func
        The bilby log prior function.
    """

    def __init__(
        self,
        names,
        priors,
        bilby_log_likelihood=None,
        bilby_log_prior=None,
    ):
        self.names = names
        self.priors = priors
        self._update_bounds()
        self.bilby_log_likelihood = bilby_log_likelihood
        self.bilby_log_prior = bilby_log_prior

    def log_likelihood(self, x, **kwargs):
        theta = [x[n] for n in self.names]
        return self.bilby_log_likelihood(theta)

    def log_prior(self, x, **kwargs):
        theta = [x[n] for n in self.names]
        return self.bilby_log_prior(theta)

    def _update_bounds(self):
        self.bounds = [
            [self.priors[key].minimum, self.priors[key].maximum]
            for key in self.names
        ]

    def new_point(self):
        """Draw a point from the prior"""
        prior_samples = self.priors.sample()
        self._update_bounds()
        point = LivePoint(
            self.names,
            array.array("d", [prior_samples[name] for name in self.names]),
        )
        return point
