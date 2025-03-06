import datetime
from lunarcalendar import Lunar

# 获取今年的年份
current_year = datetime.datetime.now().year

# 查找今年农历大年三十的公历日期
for day in range(30, 0, -1):
    try:
        lunar_date = Lunar(current_year, 12, day, isleap=False)
        solar_date = lunar_date.to_solar()
        break
    except ValueError:
        continue

# 获取今天的日期
today = datetime.date.today()

# 获取农历大年三十对应的公历日期
new_year_eve = datetime.date(solar_date.year, solar_date.month, solar_date.day)

# 计算时间差
days_left = (new_year_eve - today).days

print(f"从今天 {today} 到今年农历大年三十 {new_year_eve} 还有 {days_left} 天。")