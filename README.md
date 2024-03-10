<h1 align="center">深圳职业技术大学VPN模拟登录脚本 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="LICENSE" target="_blank">
    <img alt="License: LICENSE" src="https://img.shields.io/badge/License-LICENSE-yellow.svg" />
  </a>
</p>

> 使用 Python selenium模块 优雅模拟浏览器登录【深圳职业技术大学】的VPN系统。

## 🚫 免责声明
本程序仅对深职大VPN系统的接口进行了封装，作者不对程序的正确性或可靠性提供保证。 
请使用者自行判断具体场景是否适合使用该程序，使用该程序造成的问题或后果由使用者自行承担！

## ⚠ 温馨提示
- 在提出Issues或提交Pull requests切勿把暴露个人敏感信息，包括但不限于用户名，密码，学号，API Key等。
- 因authserver系统频繁更新原因，代码可能经常需要更新，建议关注本项目的动态。

## Install 
```sh
git clone https://github.com/HozukiKaede/szpu-connect-script
```
## Usage

```python
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

```

## Moudle

- 模拟脚本登录VPN

## Todo
- 注销VPN
- 获取VPN状态
- 保持心跳包

## Author

👤 **HozukiKaede 穗月枫**
* 作者
* Github: [@HozukiKaede](https://github.com/HozukiKaede/)


## 🤝 Contributing

欢迎贡献、问题和功能请求！<br />请随时检查 [issues page](https://github.com/HozukiKaede/szpu-connect-script/issues). 
您还可以查看 [contributing guide](https://github.com/HozukiKaede/szpu-connect-script/graphs/contributors).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2024 [HozukiKaede](https://github.com/HozukiKaede).<br />
This project is [LICENSE](https://github.com/HozukiKaede/szpu-connect-script/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_