from szpu_connect_script.connect import Connect

username = "testuser"
password = "testpasswd"

# 为了防止登录失败，可以使用try...except...语句捕获异常，多次尝试登录
# 例如：
connect = Connect(username, password)
for i in range(3):
    try:
        connect.login()
        print("登录成功")
        break
    except Exception as e:
        print(e)
        print("登录失败，正在重试...")