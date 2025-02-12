# 导入Flask库，用于构建web应用
from flask import Flask
# 导入NacosClient，用于与Nacos服务器交互，实现配置管理和服务发现功能
from nacos import NacosClient

# 初始化Flask应用实例
app = Flask(__name__)

# 设置Nacos服务器地址，请替换为实际的Nacos服务器地址
SERVER_ADDRESSES = "10.0.201.34:8848"

# 设置Nacos命名空间ID，请替换为实际的命名空间ID
NAMESPACE = "685ee9f3-70db-4f52-ae4c-a4b7789a752e"

# # 设置Nacos用户名和密码，用于认证访问Nacos服务器
USERNAME = ''
PASSWORD = ''

config_name = 'python-dev'


client = NacosClient(server_addresses=SERVER_ADDRESSES, namespace=NAMESPACE,
                     log_level='INFO')


# 定义路由，访问根路径'/'时返回的消息，展示来自Nacos的配置信息
@app.route('/')
def hello_world():
    # 使用flask的config对象获取名为"config"的配置项，展示配置内容
    return f'Hello, World! Config from Nacos: {app.config.get("config")}'


def init():
    # 服务注册：让Flask应用在启动时自动注册到Nacos，实现服务发现的自动化。heartbeat_interval可以调整后台心跳间隔时间，默认为5秒。
    client.add_naming_instance(service_name='my-flask-service', ip='localhost', port=5000, heartbeat_interval=5)

    # 设置Nacos中配置数据的数据ID和分组，默认分组为'DEFAULT_GROUP'
    data_id = 'python-dev'
    group = 'DEFAULT_GROUP'

    # 从Nacos获取配置，并更新到Flask应用的config对象中，以便在应用中使用这些配置
    app.config.update(config=client.get_config(data_id=data_id, group=group))

    # 添加配置监听器，当Nacos中的配置发生变化时，自动更新Flask应用的config对象
    client.add_config_watcher(data_id=data_id, group=group,
                              cb=lambda cfg: app.config.update(config=cfg['content']))


if __name__ == '__main__':
    init()
    app.run()
