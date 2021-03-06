"""
Constrcut and manage samplers
"""

import sys

# NOTE There are more smapler implemented in optuna, however, let's start with these
from optuna.samplers import BaseSampler, GridSampler, RandomSampler, TPESampler, NSGAIISampler

SAMPLERS = {"base": BaseSampler,
            "grid": GridSampler,
            "random": RandomSampler,
            "tpe": TPESampler,
            "genetic": NSGAIISampler}


def construct_sampler(sampler_config=None):
    if not sampler_config:
        return TPESampler()
    name = sampler_config.get("name").lower()
    if name not in SAMPLERS:
        print(f"ERROR: Unknwon sampler {name}")
        sys.exit(1)
    # NOTE Only YAMLable arguments can be used for this of course. We need to find a way to pass more complex things.
    #      E.g. some samplers take lambda function/callables etc.
    args = sampler_config.get("args", {})
    return SAMPLERS[name](**args)
