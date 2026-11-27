
# Question for students 
"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via default_factory)

Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""

from pydantic import BaseModel, ValidationError, Field
from uuid import UUID, uuid4


class ExperimentRun(BaseModel):
    experiment_name: str
    parent_run_id: str | None
    learning_rate: float = 0.001
    run_id: UUID = Field(default_factory=uuid4)
    metrics: dict[str, float] = Field(default_factory=dict)

data1 = {
    "experiment_name": "testrun1",
    "parent_run_id": None,
    

}

data2 = {
    "experiment_name": "testrun2",
    "parent_run_id": "1",
    "metrics":{
        "accuracy": "0.95",
        "precision": "0.91",
        "recall":"0.89",
        "loss": "0.12"
    }
}
r1 = ExperimentRun(**data1)
r2 = ExperimentRun(**data2)

print(r1)
print(r2)
print(r1.run_id == r2.run_id)
print(r1.metrics == r2.metrics)
