import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 整个网页的全局配置，一次性设置整个页面的样子
st.set_page_config(
    # 浏览器标签页上显示的文字，打开网页，标签写着 “AI 会话模型”。
    page_title="AI会话模型",
    # 浏览器标签页上显示的图标，打开网页，图标显示一个笑脸。
    page_icon="🤩",
    # 页面布局，wide表示全屏，centered表示中屏
    layout="wide",
    # 侧边栏是否展开，expanded表示展开，collapsed表示收起
    # 如果不设置，默认是collapsed
    initial_sidebar_state="expanded",
    # 菜单项，可以设置帮助、bug报告、关于等信息，点击这些菜单项会跳转到对应的链接。
    # 如果不设置，默认是None
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# 页面标题
st.title("AI会话模型")
# 页面logo
st.logo('./resources/202_小猫.png')


system_prompt = "你是一个脾气暴躁的ai智能助手，回答问题的语气是暴躁的，必要时可以说脏话，没有关系的"
# 定义一个列表，用于保存聊天记录。列表里的每个元素都是一个字典，字典里包含两个键值对，role和content。
# role表示消息的角色，content表示消息的内容。
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 遍历聊天记录，将每个消息显示在界面上。
for message in st.session_state.messages:
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])
    # 简洁版写法
    st.chat_message(message["role"]).write(message["content"])



prompt = st.chat_input("Say something")
# 判断用户输入是否为空，这里会将字符串自动转换成布尔值，如果用户输入了内容，则返回True，否则返回False
if prompt:
    # 在界面上显示用户发送的消息
    # chat_message("user")：创建一个用户角色的消息气泡。
    # .write(prompt)：把用户输入的内容显示出来。
    st.chat_message("user").write(prompt)
    # 将用户输入的消息添加到聊天记录中。添加到列表中保存
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            # {"role": "user", "content": prompt},
            # 将存储的聊天记录，解包出来，放到messages中,这样就可以解决记忆会话问题
            *st.session_state.messages,
        ],
        # 此代码不支持 stream=True 否则会报错
        # stream=True（流式模式）
        # response 是一段一段的数据流，每一段用 chunk.choices[0].delta.content 拿内容，choices[0].message.content
        # 没有完整的 .message.content。
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    print("<------ai响应的内容------->", response.choices[0].message.content)
    # 显示AI 助手的回复消息。
    # chat_message("assistant")：AI 助手的消息气泡。
    # .write(...)：显示 AI 返回的内容。
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 将AI的回复消息添加到聊天记录中。添加到列表中保存
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
