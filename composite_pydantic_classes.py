# -*- coding: utf-8 -*-
"""...
"""
from typing import List, Dict, Optional, Union
from pydantic import BaseModel
from enum import Enum


class ExperimentDescription(BaseModel):
    project                 : str
    platform                : List[str]
    user_type               : str
    traffic_type            : str
    module                  : str
    main_description        : Optional[str]


class SearchSpaceDescription(BaseModel):
    parameters              : Dict


class EvaluationOptionsDescription(BaseModel):
    mode                    : str


class GeneratorRunType(Enum):
    DEFAULT: 0
    STATUS_QUO: 1


class ExperimentType(str, Enum):
    fake = 'fake'
    real = 'real'


class SearchSpaceDesc(BaseModel):
    parameters: Dict
    parameter_constraints: Optional[Dict]


class MetricsWeights(BaseModel):
    str_floats: Dict[str, float]


class MetricName(BaseModel):
    metric : str

class MetricWeight(BaseModel):
    weight : float


class ExperimentMeta(BaseModel):
    experiment_type         : ExperimentType = ExperimentType.fake
    project                 : str
    platform                : str
    user_type               : str
    traffic_type            : str
    test_name               : str
    test_description        : Dict
    arms_to_generate        : int
    search_space            : SearchSpaceDesc
    control_group           : Dict
    metrics_weights         : Dict[str, float]
    evaluation_options      : EvaluationOptionsDescription

    class Config:
        orm_mode = True

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
        "platform": ["ios", "android"],
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

a = ExperimentMeta(**json_data)
print('ok')