## 1 网络基本知识
IP地址：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599173269-ecfe2630-d3c0-45e5-83d2-14db4ae9e8a7.png)

分为公网ip和内网ip

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">公网 IP（外网 IP）</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">是运营商给你家路由器分配的唯一地址，比如：</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">120.23.45.67</font>`

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">全球唯一</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">上海的公网 IP 段、北京的公网 IP 段不一样</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">互联网靠公网 IP区分地区</font>



域名：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599203505-57225c1f-1e96-4798-9bb5-388cc77c358f.png)



端口：

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599227874-eb471074-5334-45b9-944c-e608b8495ab6.png)



网络模型

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599253052-157c2cee-6966-4c99-a6f3-81ccb240a75b.png)

+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">应用层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：写好快递内容（聊天、网页、文件）</font>
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">传输层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：打包 + 贴运单，保证完整送到（TCP/UDP）</font>
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：查地址、规划走哪条路（IP 地址、路由）</font>
+ **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络接口层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：交给快递小哥，装车发货（网线 / Wi‑Fi）</font>

 **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">应用层：</font>**直接给**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">软件 / APP</font>**提供服务，规定数据长什么样、怎么发。  

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">常见协议 + 例子</font>**

1. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">HTTP/HTTPS</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：刷网页、逛淘宝、百度</font>
2. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">DNS</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：把 </font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">www.baidu.com</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> 翻译成 IP 地址（相当于查快递收件人地址）</font>
3. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">FTP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：上传下载文件</font>
4. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">SMTP/POP3</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：发邮件、收邮件</font>
5. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">DHCP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：手机连 WiFi 自动获取 IP</font>



**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">传输层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：只关心</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">两台设备之间</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">的传输，不关心走哪条路。用</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">端口号</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">区分不同软件，用 </font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">TCP/UDP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"> 两种方式发货。</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">类比：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">快递公司打包 + 负责送到收件人家门口</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，不管中间走高速还是国道。</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">两个最重要协议（必考）</font>**

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">1. TCP：靠谱慢件（顺丰特快，必须送到）</font>**

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">特点：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">可靠、有序、不丢包、可重传</font>**
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">机制：三次握手建立连接，四次挥手断开，丢包重发、流量控制</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">例子：刷网页、微信文字、下载文件、登录账号</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">通俗：必须确认对方收到，丢了就重发，慢一点但稳。</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">2. UDP：快递盲盒 / 广播（闪送，只管发，不管收没收到）</font>**

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">特点：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">速度极快、开销小、不可靠，丢了就丢了</font>**
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">例子：抖音直播、游戏、视频通话、DNS 查询</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">通俗：实时性优先，丢几帧画面不影响体验，不能重传。</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">端口号小知识</font>**

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">端口就是</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">家门号</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，一台电脑 IP 一样，靠端口区分：</font>

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">80 端口：网页</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">443：加密网页</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">443/8080：微信 / QQ</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：给数据包</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">分配 IP 地址</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，选择</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">从 A 到 B 走哪条路线</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">（路由）。只管 “</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">从哪个 IP 到哪个 IP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">”，不管软件、不管打包细节。</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">类比：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">快递分拣中心 + 导航</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，查收件人详细地址，规划走哪条高速。</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">常见协议 + 通俗例子</font>**

1. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">IP 协议</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：给设备分配 IP 地址（192.168.x.x），给数据包写收发 IP</font>
2. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">ICMP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：ping 命令！用来测试网络通不通</font>
    - <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">例：电脑输 </font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">ping baidu.com</font>`<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，就是发 ICMP 包问：你在吗？</font>
3. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">ARP</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：把 IP 地址翻译成 MAC 地址（相当于把 “门牌号” 翻译成 “身份证号”）</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">路由</font>**

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">数据包从你家 → 路由器 → 基站 → 对方路由器 → 对方手机，就是网络层在选路。‘</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络接口层：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">把上层的数据包，变成</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">电信号 / 光信号 / 无线电波</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，通过网线、WiFi 传输。处理</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">MAC 地址、网卡、交换机、以太网</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">。</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">类比：</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">快递小哥 + 货车 + 公路</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">，负责实际搬运、物理传输。</font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">通俗理解</font>**

+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网线、光纤、WiFi、5G 信号，都在这一层</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">MAC 地址：网卡出厂自带的唯一硬件地址（相当于身份证）</font>
+ <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">交换机：小区快递柜，转发局域网数据</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">完整流程：发一句微信消息，四层怎么工作？</font>**

1. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">应用层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：你输入 “你好”，微信把文字整理成数据</font>
2. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">传输层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：TCP 打包，加上端口号，保证消息完整</font>
3. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：加上你的 IP 和对方 IP，选路线</font>
4. **<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">网络接口层</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">：变成 WiFi 信号，发给路由器</font>
5. <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">对方反向逐层拆开，最后微信弹出消息</font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">总结：</font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778601032992-840ff5f2-ab92-4dbf-91de-d33c55636199.png)

<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);"></font>

HTTP协议

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599277168-0e5ae2e3-a4c6-42c2-9290-4f0340142b4f.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599298673-21450855-5680-43b1-88c1-faef2242da1d.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778599311035-1e44899a-515c-4760-9072-2eb80c77179f.png)



## 2 调用DeepSeek
### 2.1 postman接口调用deepseek
1、deepseek开放平台创建一个api key 记得将Key保存好，后面不能再次查看了

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778748702511-89fc30c0-74ea-4fcd-b3aa-6a2716d8a16f.png)

2、打开接口文档，查看请求报文

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778748820126-aac05dfd-8a26-4dfb-a430-b0b6b7e16369.png)

根据接口文档，在postman中填写请求头，请求体，请求链接，请求方式是post

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778748968199-7395e73b-654c-4a73-a349-216423d001c9.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778749064780-6fd31318-c968-4fde-bc66-8b7e75655408.png)

<font style="color:rgb(28, 30, 33);">stream 设置为 true 来使用流式输出，流式输出是一个字一个字往外蹦，非流式输出是一次性输出完。</font>

<font style="color:rgb(28, 30, 33);">将ai的回复，填到请求体中，可以读取上下文的内容</font>

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778771963315-abf09e16-a2eb-4604-83b6-7b63a2b02b87.png)



### 2.2 pyhton代码调用deepseek
1、 安装 OpenAI 官方的 Python 开发库（模块）  

<font style="color:rgba(0, 0, 0, 0.85);background-color:rgba(0, 0, 0, 0.04);">终端中输入：pip3 install openai</font>

```python
import os
from openai import OpenAI

client = OpenAI(
    # 获取环境变量中配置的api_key
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)
```



## 3 提示词工程
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778923950504-3858349b-02ad-48ff-adb0-ae8a2c0f39fa.png)

## 4 AI 应用实战
### 4.1 streamlit
#### 4.1.1 streamlit 入门
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778924486699-ea20c0ff-b2ea-49c1-bb08-97cdad2816e0.png)



<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/67415266/1778925947056-c4c2f15e-4693-429c-828c-ebfaad832be1.png)

<font style="background-color:#FBDE28;">快捷键：alt + p 可以出发Lingma提示</font>

#### 4.1.2 页面基本布局
```python
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

system_prompt = "你是一个脾气暴躁的ai智能助手，回答问题的语气是暴躁的，必要时可以说脏话，没有关系的"

# 页面标题
st.title("AI会话模型")
# 页面logo
st.logo('../resources/202_小猫.png')
prompt = st.chat_input("Say something")
# 判断用户输入是否为空，这里会将字符串自动转换成布尔值，如果用户输入了内容，则返回True，否则返回False
if prompt:
    # 在界面上显示用户发送的消息
    # chat_message("user")：创建一个用户角色的消息气泡。
    # .write(prompt)：把用户输入的内容显示出来。
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
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

```

