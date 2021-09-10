from pydantic import BaseModel, Field

class Calculate_Data(BaseModel):
    money: int = Field(170000000, title='invest money', description='about invest money')
    years: int = Field(10, title='investing years', description='about investing years')
    profit: float = Field(0.12, title='profit percentage', description='about profit percentage')
    add_money_per_year: int = Field(14000000, title='added invest money per year',
                                    description='about added invest money per year')