import os
import json

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

#如果是初次安装，创建installed文件作为标记，并修改采样器样式为下拉菜单，如果已经有installed文件则跳过。
if not os.path.exists(os.path.join(current_dir, 'installed')):
    with open(os.path.join(current_dir, 'installed'), 'w') as f1:
        f1.write('')

# 获取 config.json 文件的绝对路径
    json_file_path = os.path.join(current_dir, '..', '..', 'config.json')

# 读取 config.json 文件
    with open(json_file_path, 'r') as f2:
        config = json.load(f2)

# 修改配置项
    config['samplers_in_dropdown'] = True

# 写入修改后的配置
    with open('config.json', 'w') as f2:
        json.dump(config, f2, indent=4)

