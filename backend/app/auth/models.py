from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from core.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
