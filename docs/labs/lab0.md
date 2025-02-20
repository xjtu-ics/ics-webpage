# Lab0: Environment Build

## 实验简介
All you need is a Linux.

Lab0的目的是帮助大家熟悉环境并掌握一些基础工具的使用；我们也鼓励大家更多的进行一些课外的动手实践，并为大家整理/提供了一些额外的学习资源，有兴趣可自行学习/动手实践，强大动手能力会是大家学习CS路上的左膀右臂。

本文内容总共包含以下几个部分：

- ICS-Server （必做）
- VSCode配置 （必做）
!!! note
    ICS-Server需要在校园网环境下进行连接（包括但不限于XJTU-WLAN/XJTU-STU/宿舍组网等等），外网环境无法连接。

!!!warning
    使用vscode进行连接之前，请务必保证**你已经成功通过系统终端（bash/powershell等）进行连接并且成功修改密码了**，因为今年强制第一次登陆必须修改密码，直接使用vscode登陆的话会报错**无法请求tty**，因此无法进入交互式修改密码阶段，连接会直接断开。

- 本地Linux环境构建方法介绍 （选做）
- 实用工具学习与熟悉 （选做）

下面是比较推荐的连接服务器的步骤：

- 检查你确实处在**校园网**环境之下
- 首先使用系统终端（包括但不限于bash/powershell等），尝试登陆，**注意windows环境下也不要直接使用诸如putty等软件**
- 成功修改密码后会退出，此时再次尝试使用系统终端进行登陆，看看能否用自己设置的密码进行登陆
- 上述步骤均完成之后，再尝试使用vscode进行远程连接。
- 不管你的本地操作系统是什么，vscode可能会提示你选择目标平台，此时**注意选择linux环境**，因为服务器是linux，所有的连接程序将在服务器上运行，与自己的本地环境无关了

## ICS-Server
我们为每位同学准备了校内的服务器环境，服务器环境为`ubuntu22.04`，我们称这个环境为ICS-Server。ICS-Server是可以完成该课程所有实验的标准环境，后续部分实验的数据分发包也会直接放在各个同学的服务器目录中。因此，熟悉该环境是完成后续所有实验前置条件。

[ICS-Server 登录文档](../resources/ICS-Server.md)

## VSCode配置
Visual Studio Code（简称 VS Code）是一款由微软开发且跨平台的免费源代码编辑器。我们将帮助大家初步安装与配置，并帮助大家使用VSCode连接ICS-Server，后续可使用VSCode在ICS-Server上进行远程开发。

当然，我们也推荐大家采用自己习惯的工具进行开发。

[VSCode配置文档](../resources/VScodeRemote-SSH.md)

## 本地Linux环境构建方法简介 （选做）
本课程的实验在稳定的Linux环境下均可以顺利完成，考虑到课程后服务器账号将回收，并且Linux也是后续大家CS学习中重要开发平台与学习工具，我们非常鼓励大家自行搭建属于自己的Linux环境，但并不做强制要求。

!!! note
    如果你需要本地安装linux环境，推荐安装arch或者ubuntu两种发行版，ubuntu版本最好 >= 22.04。

[本地Linux构建文档](../resources/LinuxInstallation.md)

## 实用工具学习与熟悉（选做）
可能同学们并不熟悉Linux环境，我们提供一些资源希望帮助大家快速完成入门。

### Linux使用入门
考虑到绝大多数同学可能并没有Linux使用经验，这里简要为大家准备Linux入门相关视频资源，请大家结合自身情况进行学习：[Linux小白Shell入门—必知必会的基础命令](https://www.bilibili.com/video/BV1sK4y1b7NP/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)

学习工具没有捷径，只有：多查、多学、多用。

### MIT 6.NULL
这是MIT为计算机本科生开的一门课《你计算机科学教育中遗失的一学期》，主要用于系统的教学一些基本的工具使用，教学非常全面，大家可以作为简单入门Linux之后完整的计算机工具课。

B站中有对应的公开课[视频资源](https://www.bilibili.com/video/BV14E411J7n2/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)。

这门课可以学到很多有用的工具，但是由于这门课相对比较深入，更加建议以它作为工具类课程的进阶部分。

### vim/Emacs
除开本文中提到的VSCode代码编辑工具外，我们也非常推荐大家尝试使用vim/Emacs作为代码编辑工具。

vim是一个强大的代码编辑工具，近年来也有非常棒的中文vim学习资源出现，如果大家希望尝试更高效更geek的方式编写代码，可以进行自行学习。

vim学习资源：

- [Vim 中文文档计划](https://github.com/yianwillis/vimcdoc)
- [vi/vim keymap](../resources/quickreference.md)

## 评分方法与代码提交
本实验为环境搭建与工具熟悉实验，并不占最后实验分值计算，也无需提交任何形式的文件代码。

但是本实验是后续所有实验的前置基础，请大家务必完成所有必做部分，结合自身情况完成选做部分。
