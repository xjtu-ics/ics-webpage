# Linux Installation
本文档主要简要介绍几种Linux环境搭建方式，大家有兴趣选择其中一种或几种搭建属于自己的Linux环境。

- 物理机
- 虚拟机
- WSL（Windows Linux子系统）
  
## 物理机系统
该方法直接将Ubuntu（一种Linux发行版）安装在你的本地物理机器上，同时您可以选择保留你本机的Windows，这样你就会拥有一个双系统的电脑。

=== "bilibili视频教程资源"

    [新手安装Ubuntu系统经验分享（超详细）](https://www.bilibili.com/video/BV15T4y1M7cf/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)

    [【入坑Linux】物理机安装Ubuntu20.04，体验马上要发布的新版Ubuntu系统](https://www.bilibili.com/video/BV1Cz411b7CA/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)

    或直接搜索”物理机安装Ubuntu“查看其他的视频，进行尝试

=== "文档资源"

    [如何安装 Ubuntu 22.04 LTS 桌面版 (图文教程) ?](https://zhuanlan.zhihu.com/p/569347838)

优点：

- 您将获得完整的Linux体验。
- 学习到完整的操作系统引导流程。
- 你可能并不熟悉Linux系统，作为物理机操作系统会强制你去解决（折腾）很多问题，此时你的Linux水平会得到很大的提升。
- 可以选择安装GUI （图形界面）。

缺点：

在物理机上直接进行修改，极小概率会导致你的物理机原始原始系统奔溃，这时候你需要寻求帮助。

## 虚拟机
物理机上的奔溃代价是昂贵的，你可能需要寻找其他人的帮助。为了防止出现如此高额的风险，我们也可以使用虚拟机的方式来安装Linux，虚拟机就是相当于在你的计算机上模拟了一台虚拟的机器，并在虚拟机上运行Linux。

推荐使用Virtual Box（相对简陋但免费）或VMware（更优秀但不免费需要找破解版）等虚拟机软件创建虚拟机，并在虚拟上安装并使用Linux。

=== "bilibili视频教程资源"

    VMware:
    [八分钟完成VMware和ubuntu系统安装](https://www.bilibili.com/video/BV1M94y1U7nc/?spm_id_from=333.337.search-card.all.click)
    [两分半钟完成VMware安装及Linux-Ubuntu安装](https://www.bilibili.com/video/BV1W34y1k7ge/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)
    Virtual box:
    [使用VirtualBox安装Ubuntu 22.04 LTS Desktop](https://www.bilibili.com/video/BV1Tu41167Jr/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)
    [第二讲：在VirtualBox虚拟机上安装Ubuntu系统](https://www.bilibili.com/video/BV1qZ4y187f8/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)
=== "文档资源"

    VMware：
    [2020最新版VMware安装Ubuntu20.04教程(巨细)！](https://zhuanlan.zhihu.com/p/141033713)
    Virtual Box
    [VirtualBox 安装 Ubuntu 开发环境详细图文教程](https://zhuanlan.zhihu.com/p/35619204)
优点：

- 虚拟机的崩坏几乎不会影响本机

- 可以安装Linux GUI（图形界面）

缺点：

- 虚拟机相较物理机存在性能损失

## WSL
Windows Subsystem for Linux（简称WSL）是一个在Windows 10\11上能够运行原生Linux二进制可执行文件（ELF格式）的兼容层。它是由微软与Canonical公司合作开发，其目标是使纯正的Ubuntu、Debian等映像能下载和解压到用户的本地计算机，并且映像内的工具和实用工具能在此子系统上原生运行。

[WSL微软官方介绍文档](https://learn.microsoft.com/zh-cn/windows/wsl/about)

WSL安装：

=== "bilibili视频教程资源"

    [Windows11安装WSL2](https://www.bilibili.com/video/BV1n14y1x7Y7/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)

    [Window10开发环境搭建(1) | 详细演示WSL2的安装](https://www.bilibili.com/video/BV1aA411s7PJ/?spm_id_from=333.337.search-card.all.click&vd_source=f03c62aca712083bc8b849d1d0e7cdb5)

=== "文档资源"

    [WSL官方文档](https://learn.microsoft.com/zh-cn/windows/wsl/install)

    [Windows10/11 三步安装wsl2 Ubuntu20.04（任意盘）](https://zhuanlan.zhihu.com/p/466001838)

优点：轻量、安装简单快捷

缺点：环境不完整