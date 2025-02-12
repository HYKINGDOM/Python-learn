# 导入FastAPI库，用于构建API服务
import asyncio

from fastapi import FastAPI
from nacos import NacosClient

app = FastAPI()

# 设置Nacos服务器地址，请替换为实际的Nacos服务器地址
SERVER_ADDRESSES = "10.0.201.34:8848"

# 设置Nacos命名空间ID，请替换为实际的命名空间ID
NAMESPACE = "685ee9f3-70db-4f52-ae4c-a4b7789a752e"

# 设置Nacos用户名和密码，用于认证访问Nacos服务器
USERNAME = 'Your user name'
PASSWORD = 'Your password'

client = NacosClient(server_addresses=SERVER_ADDRESSES, namespace=NAMESPACE, log_level='INFO')


# 定义一个异步函数，在FastAPI应用启动时执行
@app.on_event("startup")
async def startup_event():
    # 在启动时创建一个任务来初始化配置
    asyncio.create_task(init())


# 通过NacosClient获取配置，并存储在应用的状态(state)中，以便后续使用
async def load_config(data_id, group):
    app.state = {'config_data': client.get_config(data_id=data_id, group=group)}


# 异步函数，用于初始化应用所需的各种配置和监听器
async def init():
    data_id = 'python-dev'
    group = 'DEFAULT_GROUP'
    await load_config(data_id, group)

    def on_config_change(cfg):
        # 当Nacos中的配置发生变化时，更新应用状态中的配置数据
        app.state = {'config_data': cfg['content']}

    client.add_config_watcher(data_id, group, cb=on_config_change)
    client.add_naming_instance(service_name='my-flask-service', ip='localhost', port=8000, heartbeat_interval=5)


# 定义一个GET请求的路由，返回简单的欢迎信息及当前从Nacos获取的配置数据
@app.get("/")
def hello_world():
    return f'Hello, World! Config from Nacos: {app.state["config_data"]}'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
