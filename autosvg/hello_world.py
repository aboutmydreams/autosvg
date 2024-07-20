import svgwrite


def draw_polygon(points, filename="polygon.svg"):
    # 创建一个SVG绘图对象
    dwg = svgwrite.Drawing(filename, profile="tiny")

    # 添加一个多边形
    dwg.add(dwg.polygon(points, fill="none", stroke="black"))

    # 保存到文件
    dwg.save()


# 定义点的坐标列表
points = [(50, 150), (150, 50), (250, 150), (200, 250), (100, 250)]

# 绘制多边形并保存为SVG
draw_polygon(points)
