
#  optional & non-nullable
from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    name: str = "Ram"
    product_id: int

value = {
    "product_id": "50"
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total error count: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, Message: {error['msg']}")

# optional & nullable
#  what happens if value is None


value = {
    "product_id": "50",
    "name": None
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"total error count: {e.error_count()}")
    for error in e.errors():
        print(f"Fields: {error['loc']}, Type: {error['type']}, Message: {error['msg']}")

class Product(BaseModel):
    product_id: int
    name: str | None = None

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total Number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, message: {err['msg']}")
from pydantic import BaseModel, ValidationError  

class Product(BaseModel):
    product_id: int
    name: str | None =None

value = {
    "product_id": "50",
    "name": None

}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total error count: {e.error_count()}")
    for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, message: {err['msg']}")



class Product(BaseModel):
    product_id: int = "abc"

p = Product()
print(p)

from datetime import datetime, UTC
import time
class BadExample(BaseModel):
    created_at: datetime = datetime.now(UTC)

b1 = BadExample()
time.sleep(2)
b2 = BadExample()
b3 = BadExample()


from uuid import UUID, uuid4
from pydantic import BaseModel, Field
import time



class GoodExample(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

g1 = GoodExample()
time.sleep(2)
g2 = GoodExample()

print(g1)
print(g2)
print(g1.created_at == g2.created_at)


from datetime import datetime, UTC

from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class LLMChatRequest(BaseModel):
    prompt: str



class Prompt(BaseModel):
    text: str = Field(description="User text value")
    user_id: str = Field(..., desciption="Caller user id")
    value: str | None = Field(default=None, description = "random value")

print(Prompt(text="abc", user_id="pqr", value=None))

#  validate default value
class ValidateVal(BaseModel):
    product_id: int = Field(default="xyz", validate_default=True)

try:
    ValidateVal()
except ValidationError as e:
    print(e.errors()[0]['msg'])


# dynamic data assign
class Modeldata(BaseModel):
    model_name: str
    version: int = 1
    attribute_val: str = Field(
        default_factory=lambda data: f"{data['model_name']}: {data['version']}"
    
    )

a = Modeldata(model_name="gpt", version=2)
print(a)


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
    "parent_run_id": "1"
}
r1 = ExperimentRun(**data1)
r2 = ExperimentRun(**data2)

print(r1)
print(r2)
print(r1.run_id == r2.run_id)
print(r1.metrics == r2.metrics)