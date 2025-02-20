# yamlc

`yamlc` 是一个简单的 YAML 配置加载库，支持加载和获取嵌套的配置项。

## 安装
使用 pip 安装：
```
pip install yamlc
```


## 示例用法：
```python
from yamlc import Yamlc

# 获取配置项
host = Yamlc.get('database.host')
print(host)
```