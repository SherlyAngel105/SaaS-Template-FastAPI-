from enum import Enum

from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings


class AbstractModel(BaseModel):
    """Schema Models

    Args:
        BaseModel (_type_): Inherits from Pydantic and specifies Config
    """

    class Config:
        from_attributes = True
        use_enum_values = True


class AbstractSettings(BaseSettings):
    """Settings Models

    Args:
        BaseModel (_type_): Inherits from Pydantic and specifies Config
    """

    class Config:
        env_file = ".env"


class ResponseModel(AbstractModel):
    """Base Response Models

    Args:
        BaseModel (_type_): Inherits from Pydantic and specifies Config
    """

    message: str
    status: int


class RoleOptions(Enum):
    admin = "Admin"
    member = "Member"


class User(AbstractModel):
    """User Schema Models

    Args:
        BaseModel (_type_): Inherits from Pydantic and specifies Config
    """

    first_name: str
    last_name: str
    email: EmailStr
