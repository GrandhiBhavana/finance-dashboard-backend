from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class FinancialRecord(Base):
    _tablename_ = "records"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)