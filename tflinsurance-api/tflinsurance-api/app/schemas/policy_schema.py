from pydantic import BaseModel, Field


class PolicyCreate(BaseModel):
    self.connection =mysql.connector.connect(**database_config)

    name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=100)
    maturity: str
    premium: float = Field(gt=0)


class PolicyUpdate(PolicyCreate):
    pass


class PolicyResponse(PolicyCreate):
    id: int