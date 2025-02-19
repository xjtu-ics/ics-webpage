## Q1：Request Timeout。

- A：注意 ICSServer 需要在校园网环境下登录， （包括但不限于 XJTU-WLAN/XJTU-STU/宿舍组网等等），外网环境无法连接
- A：若处于校园网环境，仍显示 TimeOut 请联系助教查看服务器状态。
## Q2：PowerShell 等终端 ssh 尝试连接显示Bad owner or permissions on xxx/.ssh/config问题。

- A：请注意修改对应路径内的一些权限问题，参考资料 Bad owner or permissions on '.ssh/config' [SOLVED] - ShellHacks

## Q3：若 VSCode 尝试连接 ICSServer 也出现配置文件权限问题。

- A：可使用 Q2 中类似方法修改对应文件路径权限，或尝试以管理员身份运行 VSCode
- A：可以考虑采用默认第二个配置文件或者自定义配置文件重新按照 Visual Studio Code Remote SSH Setting | XJTU-ICS 中关于 VSCode 连接流程进行配置。
<figure markdown="span">
  ![Image title](../assets/images/FAQ-lab0-1.jpeg){ width=auto }
</figure>
## Q4：PowerShell 等终端键入命令ssh userid@igw.dfshan.net -p2291出现密码输入提示后，键入密码无反应。

- A：SSH 密码输入没有回显的，这是正常情况。

## Q5：SSH/VSCode 输入密码尝试登录后显示Permission denied, please try again. 。

- A：可能存在两种情况
    - 密码错误：若为第一次连接，注意 SHA256 加密时输入学号后无需加入回车，否则回车也会一同进入您的密码加密导致与初始密码不同。并且注意需要将所有字母保持为小写状态
    - 由于退选补选改选导致的选课名单变动将不包含账号，请联系助教创建账号。

## Q6：遇到某些诡异的软件问题，如突然 VSCode 按键无法点击，无法显示之类的问题。

  - A：请先尝试重启电脑 XD。