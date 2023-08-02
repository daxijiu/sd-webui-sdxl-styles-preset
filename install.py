import os
import json

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取 a.json 文件的绝对路径
json_file_path = os.path.join(current_dir, '..', '..', 'config.json')

# 读取 a.json 文件
with open(json_file_path, 'r') as f:
    config = json.load(f)

# 修改配置项
config['samplers_in_dropdown'] = True

# 写入修改后的配置
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
