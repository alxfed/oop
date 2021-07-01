# -*- coding: utf-8 -*-
"""...
"""
from typing import List, Dict, Optional, Union, Literal
from pydantic import BaseModel
from enum import Enum
from json import loads

class ModuleName(str, Enum):
    bandit                  = 'bandit'
    bayesian_optimization   = "bayesian_optimization"
    constrained             = 'constrained_optimization'


class ExperimentType(str, Enum):
    fake        = 'fake'
    real        = 'real'


class ProjectCode(str, Enum):
    tbz         = 'tbz'
    tbz_alpha   = 'tbz_alpha'
    tsi         = 'tsi'
    stt         = 'stt'


class PlatformName(str, Enum):
    windows     = 'windows'
    amazon      = 'amazon'
    ios         = 'ios'
    android     = 'android'
    samsung     = 'samsung'
    beta        = 'beta'
    alpha       = 'alpha'


class UserType(str, Enum):
    all         = 'all'
    new         = 'new'
    old         = 'old'


class TrafficType(str, Enum):
    all         = 'all'
    organic     = 'organic'
    paid        = 'paid'


class TestDescription(BaseModel):
    project                 : ProjectCode
    platform                : List[PlatformName]
    user_type               : UserType
    traffic_type            : TrafficType
    module                  : ModuleName
    main_description        : str


class SearchSpaceDescription(BaseModel):
    parameters              : Dict[str, dict]
    parameter_constraints   : Optional[Dict[str, dict]]


class ExperimentDescription(BaseModel):
    experiment_type         : ExperimentType
    project                 : str
    platform                : str
    user_type               : UserType
    traffic_type            : TrafficType
    test_name               : str
    test_description        : TestDescription
    arms_to_generate        : int
    search_space            : SearchSpaceDescription
    control_group           : Dict
    metrics_weights         : Dict[str, float]
    evaluation_options      : Dict

json_data = {
    "experiment_type": "fake",
    "project": "solitaire",
    "platform": "google_play",
    "user_type": "new",
    "traffic_type": "all",
    "test_name": "New Bayesian Test",
    "test_description" :
    {
        "project": "stt",
        "platform": ["ios", "android"], # platformS would be much better here
        "user_type": "new",
        "traffic_type": "all",
        "module": "bayesian_optimization",
        "main_description":"new null hypothesis is:..."
    },
    "arms_to_generate" : 5,
    "search_space":
    {
    "parameters":{
        "x": {"type":"range", "dtype":"INT", "lower_bound":3, "upper_bound":100},
        "y": {"type":"range", "dtype":"FLOAT", "lower_bound":0.03, "upper_bound":0.99}
        }
    },
    "control_group":{"x":2, "y":0.5},
    "metrics_weights":
    {
        "Retention_1":1.0,
        "Retention_3":0.0,
        "Conversion_1":0.0,
        "Conversion_all":1.0,
        "ARPU_all":0
    },
    "evaluation_options":
    {
        "mode":"manual"
    }
}

c = ExperimentDescription(**json_data)
a = c.dict(include={'test_description': {'platform'}}) # https://pydantic-docs.helpmanual.io/usage/exporting_models/#advanced-include-and-exclude
b = loads(c.json(include={'main_description'}))
print('ok')