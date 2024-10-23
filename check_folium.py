import folium

# 创建基础地图
m = folium.Map(location=[20, 0], zoom_start=2)

# 自定义大小的Marker
size = 40  # 可以根据需要调整大小

# 添加Marker
folium.Marker(
    location=[48.8588897, 2.3200410217200766],  # 示例位置
    icon=folium.DivIcon(html=f'<div style="font-size: {size}px; color: red;"></div>'),  # 使用自定义HTML
    popup="巴黎"
).add_to(m)

# 保存地图为HTML文件
map_file = "my_custom_map.html"
m.save(map_file)
