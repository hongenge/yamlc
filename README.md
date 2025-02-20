### yamlc

`yamlio` 是一个简单的 Python 库，用于读取和管理 YAML 配置文件。它允许用户轻松加载、访问和重新加载配置。


### 特性

- 支持加载 YAML 配置文件。
- 支持点语法访问嵌套的配置项。
- 支持重新加载配置文件。
- 可以设置配置文件路径。


### 安装
使用 pip 安装：
```
pip install yamlc
```


### 示例用法：
```python
from yamlc import Yamlc

# 获取配置项
value = Yamlc.get("database.host", default="localhost")
print(value) # 如果配置中没有 "database.host"，则返回 "localhost"
```

### 设置配置文件路径
```python
from yamlc import Yamlc

# 设置新的配置文件路径
Yamlc.set_config_file_path("new_config.yaml")
```

### 重新加载配置文件
```python
from yamlc import Yamlc

# 重新加载配置文件
Yamlc.reload()
```

### 配置文件示例
yamlc 库支持的配置文件格式如下所示：
```yaml
database:
  host: localhost
  port: 5432
  username: user
  password: pass
```