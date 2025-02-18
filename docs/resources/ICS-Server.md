# ICS-Server

## 账号获取
我们为每位课程内同学建立了账号，这些账号密码以如下的形式分发：

### 用户名和初始密码
用户名：你的学号加`-ics`

密码：你的学号

例如：你的学号是2183311128，那么你的服务器用户名就是：`2183311128-ics`，密码为：`2183311128`。

!!! warning
    为了防止信息泄露，首次登录输入初始密码后，服务器会强制登录用户修改密码。请同学们保管好自己修改后的密码，或者可自行尝试ssh密钥登录。如果你因为任何原因（新选课或者密码被同学恶意篡改）无法登陆ics服务器，请立刻联系助教进行处理。


## 登录方式
使用 ssh 登录，登录所需信息如下：

- 地址：x86.ics.xjtu-ants.net
- 端口号：2291


=== "Windows"

    可以使用Windows自带的Powershell，使用如下命令登录：
    ```
    ssh username@x86.ics.xjtu-ants.net -p2291
    ```
    参考连接： Powershell连接ssh

    也可使用其他 ssh 客户端，如putty, xshell, tabby, windows terminal等。

    下载客户端后，配置好用户名、服务器地址、端口号，即可登录。

    参考链接：

    - putty: [PuTTY 新手使用教程（详细图文）](https://www.hostarr.com/putty-tutorial/)
    - xshell: [Xshell怎么用？详细的Xshell使用教程](https://cloud.tencent.com/developer/article/1822579)
    - tabby: [Tabby 使用指南：一个高度可配置的现代化终端模拟器](https://zhuanlan.zhihu.com/p/443550221)
    - windows terminal: [windows terminal 连接远程 ssh](https://www.jianshu.com/p/b7a105a67253)

=== "MacOS"

    打开系统自带的 Terminal 或者下载 iTerm 软件，使用如下命令登录

    ```
    ssh username@x86.ics.xjtu-ants.net -p2291
    ```
    其中，username 为各自的账户名。

=== "Linux"

    打开终端软件，使用如下命令登录

    ```
    ssh username@x86.ics.xjtu-ants.net -p2291
    ```
    其中，username 为各自的账户名。

=== "VSCode + remote ssh插件"

    详见 [vscode-setting](./VScodeRemote-SSH.md)

## 登录成功检查
无论大家使用上述的什么方式尝试登录ICSServer，在ICSServer的终端中键入如下命令：
```
whoami
```

若显示你对应的用户名（即学号+‘ics’），则表明你登录ICSServer成功且账号无误。


## 免密登录

暂不做要求。

具体可查阅如下资料尝试：
[详见 SSH 密钥登录](https://wangdoc.com/ssh/key)/[在win10和Linux上配置SSH免密登录](https://blog.csdn.net/qq_40156289/article/details/120342781)
!!! warning
    严禁使用服务器挖矿。

## WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
known_hosts文件是SSH客户端中的一个配置文件。当首次与一个SSH服务器建立连接时，客户端会记录下该服务器返回的的公钥，并保存在known_hosts文件中，以后每次连接该服务器时，客户端都会验证该服务器返回的公钥是否与known_hosts文件中保存的一致。如果不一致，则会发出警告，提示可能存在DNS劫持、中间人攻击等安全问题。

使用SSH连接远程服务器或者使用Git拉取代码时，偶尔会出现“WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!”警告，一般是以下几种情况导致的：

- 远程服务器重装或更换了系统，导致系统生成的密钥发生了变化。
- 本地计算机重装了系统或者更改了SSH客户端软件。
- 发生了中间人攻击，远程服务器可能是伪造的。

比较简单的解决方法：删除known_hosts文件中的对应行。

一般这个问题的报错如下：

<figure markdown="span">
  ![Image title](../assets/images/know_hosts.png){ width=auto }
</figure>

只需要根据这个红框提示的目录，找到对应的known_hosts文件，将这个文件中的有2291的行全部删去即可。（更绝的可以直接删除这个known_hosts文件）

下面给出ICS-Server的服务器公钥指纹（public key fingerprints），供大家参考：

- `SHA256:4ON3oPpCRU0uZdIc6SWPDBCKCYOrpKgXqvE5aiyCCzE`(RSA)
- `SHA256:/RIkpkRMvv3QGQPuVLwdBtQb39a+7WTxm6ffQxYGlNk`(DSA)
- `SHA256:H/DX2QMavSC6rbwxAvtLOy5vZYOECbpPxfxDIOAhj14`(ECDSA)
- `SHA256:TdWfFxmK+7Fc1Gwpkj1ZYhey676aTTwAstrX7QFDHsI`(ED25519)

你也可以将下列服务器公钥直接添加到你的`~/.ssh/known_hosts`文档里：

```text
[x86.ics.xjtu-ants.net]:2291 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJILyuHQY2bJ+WivExEjByZ2aG5tLayZkw9AqwGH4w4r
[x86.ics.xjtu-ants.net]:2291 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEBzKfIjDxQp0bKgBczbKq6Bk96CiCdGTAqbDnt/muT6GdLCy7Wh4k0JKwuRq8n65G/bhBSTOg+egZDwHTFG6q4=
[x86.ics.xjtu-ants.net]:2291 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCrNsqug9P4eeW9ewfSylBG/FsYvtjaK6Q+sUjfhBv8MN7OJoMm9MY/kCIi8C8CF3qOtzOq3aJMrRwvPbpt79zq1NetQNp6sw0LhEYWAUPUvFb9fS0gZAicETUFHVQm2uipYTIyXwKhm/kLRb1MWL638cWpVKCpPvTvt0FiOiOu6XTa4HADFNblTW48Tn93XH1Z12BDJTUbseicp1oeIbi9zDMENLihZCmsGTwM05d2omSQ2henYndD1he1fXwKAebhrFdqkrMdd0iet6GQESOGb5PBxwxhYphIa7Ue9tWuDfIRH1PK25uSYn4a4E9x1l1khvXc/ag7nGcEGqtoWOHK5pLjtUVp0VVYVFCy+wcHWkdiHL9zcxXIljV7VuNWCX49DzosVLacs4xFTes1F47UqOZocqK+q2kNXE6PeKt/PuDHNPPB7RfA9WgE5u3+jYS5S6KUhy9TimpGjV3UEAQyZbGPWbepzvxLkzBcpuDFBsWbPtErV/kYMZQYUC5hgzk=
```

