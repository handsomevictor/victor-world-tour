import json
import math
import folium
from resources import all_places

all_locations = {}
with open("locations_database.json", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        place, location = line.split(":")
        # 将字符串转换为列表
        all_locations[place] = eval(location)  # 请确保 location 格式正确，例如 "[48.8588897, 2.3200410217200766]"

# 创建基础地图
m = folium.Map(location=[20, 0], zoom_start=2)
scale_factor = 15000  # 这个值可以调整，以控制圆的大小


for place, location in all_locations.items():
    city, country = place.split(", ")
    # 绘制透明圆圈
    folium.Circle(
        location=location,  # 这里是一个列表，包含纬度和经度
        radius = scale_factor * (math.sqrt(all_places[country][city]) * 2),
        color='green',  # 圆圈颜色
        fill=True,  # 填充
        fill_color='lightblue',  # 填充颜色
        fill_opacity=0.3  # 透明度（0-1之间）
    ).add_to(m)

    # 颜色深，表示呆的时间久
    # 用自定义笑脸和苦脸？？
    

# 保存地图为HTML文件
map_file = "my_travel_map.html"
m.save(map_file)
