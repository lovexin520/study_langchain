#查天气智能体
#agent开发步骤
# 1-加载变量环境
# 2-定义工具
# 3-定义agent
# 4-调用agent

from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain.tools import tool

#1-加载环境变量
load_dotenv()
# api_key = os.getenv("DEEPSEEK_API_KEY")
# print(api_key)

# #2-1-OpenAI创建客户端
# client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
#
# #OpenAI调用模型
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你是谁?"}
#     ],
#     temperature=0.9,
#     stream=False,
# )
# print(response.choices[0].message.content)


#2-2-langchain创建Agent
#安装DeepSeeksdk
#uv add langchain-deepseek
#不用api_key = os.getenv("DEEPSEEK_API_KEY")


# 2-定义工具
@tool
def getWeather(location: str) -> str:
    """Get the weather for a given location"""
    return f"{location}的天气是晴朗的"


#3-定义agent
from langchain.agents import create_agent
agent = create_agent(
    "deepseek-chat",
    tools=[getWeather]
)


#4-调用agent
print("正在调用模型")
response = agent.invoke({
    "messages":[
        {"role": "user", "content": "今天北京的天气如何?"}
    ]
})

#输出结果
# print(response)

#格式化输出
print(response["messages"][-1].content)


