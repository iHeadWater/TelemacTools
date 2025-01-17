import numpy as np
import sys
sys.path.append("D:/Program/Telemac/scripts/python3")  # Telemac 安装路径
from data_manip.extraction.telemac_file import TelemacFile

def LoadData(filename):
    # 加载slf文件
    res = TelemacFile(filename)
    res.print_info()  # 输出模型基本信息
    return res


def ExportMesh(res):
    # Node xxx Element xxx
    # 只输出节点坐标x y
    # 单元索引n1 n2 n3
    mesh = res.tri  # 获取网格
    x, y, triangles = mesh.x, mesh.y, mesh.triangles  # 节点经纬度和单元
    f = open('mesh.txt', 'w')
    # 输出节点数和单元数
    print(f'Node\t{len(x)}\tElement\t{len(triangles)}', file=f)
    # 输出节点坐标
    for i in range(len(x)):
        print(f'{x[i]}\t{y[i]}', file=f)
    # 输出单元节点索引
    for i in range(len(triangles)):
        print(f'{triangles[i][0]}\t{triangles[i][1]}\t{triangles[i][2]}', file=f)
    f.close()


def ExportPointValue(res, varname, time):
    # 只输出节点值
    value = res.get_data_value(varname, time)  # 获取time时间的变量值
    f = open(f'point_{varname}_{time}.txt', 'w')
    for i in range(len(value)):
        print(f'{value[i]}', file=f)
    f.close()


def ExportMeshValue(res, varname, time):
    # Node xxx Element xxx
    # 节点坐标和值x y z
    # 单元索引n1 n2 n3
    mesh = res.tri  # 获取网格
    x, y, triangles = mesh.x, mesh.y, mesh.triangles  # 节点经纬度和单元
    value = res.get_data_value(varname, time)  # 获取time时间的变量值
    f = open(f'mesh_{varname}_{time}.txt', 'w')
    # 输出节点数和单元数
    print(f'Node\t{len(x)}\tElement\t{len(triangles)}', file=f)
    # 输出节点坐标和节点值
    for i in range(len(x)):
        print(f'{x[i]}\t{y[i]}\t{value[i]}', file=f)
    # 输出单元节点索引
    for i in range(len(triangles)):
        print(f'{triangles[i][0]}\t{triangles[i][1]}\t{triangles[i][2]}', file=f)
    f.close()


res = LoadData('geo.slf')

ExportMesh(res)  # 输出网格结构 mesh.txt
ExportPointValue(res, 'BOTTOM', 0)  # 输出节点值，0指时间步
ExportMeshValue(res, 'BOTTOM', 0)  # 输出带节点值的网格结构
