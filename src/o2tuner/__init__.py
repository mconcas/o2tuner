"""
o2tuner module
"""


from o2tuner.o2tuner import O2tuner
from o2tuner.backends import OptunaHandler


def obj(trial):
    """
    This is the objective function to minimise
    """
    x_var = trial.suggest_float("x", -10, 10)
    return (x_var-2)**2


def entrypoint():
    """
    Entrypoint of the program
    """

    optuna_handler = OptunaHandler()
    optuna_handler.set_objective(obj)

    # Create and run the tuner
    tuner = O2tuner(optuna_handler)
    tuner.init(n_trials=50)
    tuner.run()
