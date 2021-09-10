
from controllers.models.test import Calculate_Data

def service_calculate_profit(cal_data: Calculate_Data):
    print("inputed money :", cal_data.money, end=", ")
    print("inputed years :", cal_data.years, end=", ")
    print("inputed profit :", cal_data.profit)
    result = cal_data.money

    for year in range(1, int(cal_data.years) + 1):
        result += result * cal_data.profit
        print(f"After {year} year: {result}")
        result += cal_data.add_money_per_year

    return {"result": int(result - cal_data.add_money_per_year)}