import json
import streamlit as st
import os
from openai import OpenAI
from datetime import datetime

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
st.logo('../resources/202_小猫.png')

def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话信息
def save_session():
    if st.session_state.current_session:
        # 构建会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 创建文件夹session 用于保存会话记录
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        # 保存会话记录
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载所有会话列表
def load_sessions():
    session_list = []
    # 判断sessions目录是否存在
    if os.path.exists("sessions"):
        # 列出sessions里面的所有文件
        file_list = os.listdir("sessions")
        for filename in file_list:
            # 判断文件名是否以.json结尾
            if filename.endswith(".json"):
                # 字符串切片 从0开始，切到-5，步长为1等价于filename[0:-5:1]
                session_list.append(filename[:-5])
    return session_list

# 加载当前会话
def load_session(session_name):
    try:

        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
            st.session_state.nick_name = session_data["nick_name"]
            st.session_state.nature = session_data["nature"]
            st.session_state.current_session = session_name
            st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话失败")


# 定义一个列表，用于保存聊天记录。列表里的每个元素都是一个字典，字典里包含两个键值对，role和content。
# role表示消息的角色，content表示消息的内容。
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 记录当前会话记录，以时间命名
# strftime("%Y-%m-%d %H:%M:%S") 对时间进行格式化
if 'current_session' not in st.session_state:
    st.session_state.current_session = generate_session_name()


# 设置一个侧边栏
# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("昵称")
# with streamlit 的上下文管理器，侧边栏的设置都可以写在这个下面，不需要加上sidebar
with st.sidebar:
    st.subheader("AI控制面板")
    # st.button 返回值是true 就执行下面代码，只要点击了按钮，返回的就是true
    if st.button("新建会话",width="stretch",icon="✏️"):
        # 1 保存当前会话
        save_session()

        # 2 新建一个会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            # 保存当前新建的会话
            # save_session()
            # 刷新页面
            st.rerun ()
    # 展示历史会话
    st.text("历史会话")
    # 调用方法展示历史会话
    session_list = load_sessions()
    for session in session_list:
        # 页面布局，col1占四分,col2占一份
        col1,col2 = st.columns([4,1])
        # key=f"load_{session} 为每个按钮设置一个单独的key,
        # 如果不设置，默认的是第一个参数里的内容。如 session
        # 但是col2 里第一个参数都是“”，key就会重复会报错，所以要单独设置一个key
        with col1:
            # 如果会话记录列表中的会话就是当前会话，按钮会高亮红色显示 三元运算符 type="primary"表示为红色
            if st.button(session,width="stretch",icon="💌",key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                pass

    st.subheader("伴侣信息")
    if 'nick_name' not in st.session_state:
        st.session_state.nick_name = "张喜秀"
    if 'nature' not in st.session_state:
        st.session_state.nature = "温柔善良体贴的ai智能体"

    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    nature = st.text_area("性格描述",placeholder="请输入性格",value=st.session_state.nature)


    if nick_name:
        st.session_state.nick_name = nick_name

    if nature:
        st.session_state.nature = nature

    print(nature)
    print(st.session_state.nature)


st.text(f"会话名称: {st.session_state.current_session}")
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
    system_prompt = f''' 你叫 %s  ，现在是用户的真实伴侣，请完全代入伴侣角色。
            规则:
            1.每次只回1条消息
            2.禁止任何场景或状态描述性文字
            3.匹配用户的语言
            4.回复简短，像微信聊天一样可以有emoji表情
            5.有需要的话可以用
            6.用符合伴侣性格的方式对话
            7.回复的内容，要充分体现伴侣的性格
            你的性格是: %s
            你必须严格遵守上述规则来回复用户'''

    # 在界面上显示用户发送的消息
    # chat_message("user")：创建一个用户角色的消息气泡。
    # .write(prompt)：把用户输入的内容显示出来。
    st.chat_message("user").write(prompt)
    # 将用户输入的消息添加到聊天记录中。添加到列表中保存
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name,st.session_state.nature)},
            # {"role": "user", "content": prompt},
            # 将存储的聊天记录，解包出来，放到messages中,这样就可以解决记忆会话问题
            *st.session_state.messages,
        ],
        # 此代码不支持 stream=True 否则会报错
        # stream=True（流式模式）
        # response 是一段一段的数据流，每一段用 chunk.choices[0].delta.content 拿内容，choices[0].message.content
        # 没有完整的 .message.content。
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    full_response = ""
    # 创建一个空的容器，用于展示大模型返回的结果
    # 先在页面上占一个位置，后面可以反复替换这个位置的内容，而不会新增一行。
    # 它就像你在纸上先画一个空方框，后面所有内容都只写在这个方框里，而不是每次都新写一行。
    response_message = st.empty()
    # chunk 就是相当于是response的每个数据包
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # print("<------ai响应的内容------->", response.choices[0].message.content)
    # 显示AI 助手的回复消息。
    # chat_message("assistant")：AI 助手的消息气泡。
    # .write(...)：显示 AI 返回的内容。
    # 非流式输出的解析方式
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 将AI的回复消息添加到聊天记录中。添加到列表中保存
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # 不点击新建会话，也会保存会话记录
    save_session()


