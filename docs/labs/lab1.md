# XJTU-ICS lab 1: Data Lab 数据实验

## 实验简介

相信大家在前几节课中学习中已经学到了不少东西，这个小实验的目的是让大家更加熟悉计算机中信息表示的常见模式和整数的位级表示。你将通过解决一系列编程“谜题”来做到这一点。其中许多谜题可能看起来构造的非常刻意（human-made），但你会发现自己在处理它们的过程中更多地考虑了计算机中比特的表示法。

这些题目并不简单，但是相信在尝试求解它们的过程中你能感受到一些乐趣，并提升一些动手与编程能力。

Enjoy and Have fun! 😉

## 注意事项

- 这是一个“个人”作业，请不要抄袭或者尝试几个人一起完成.
- 这些问题并不是一些完全全新的问题，我们鼓励“Google”学习解决一些代码之外的问题（环境问题/工具使用问题），但是频繁的查询代码谜题相关的解将使得这个实验与课程失去意义.
- 不要使用诸如deepseek，chatgpt等大模型的帮助，当然你用了我们可能查不出来，但是建议自己动脑子完成这些题目，现在花时间了期末考试复习就简单了 😍

## 开发环境和实验前准备

前置要求： 学习完[lab0: 环境搭建](./lab0.md)，确保自己手边有可用的linux环境和完整的开发工具链(gcc, make等)，**不要试图在windows环境下完成实验**。

### 远程开发

如果你手边没有Linux环境，不用担心，我们为每一个同学准备了服务器账号。

不知道怎么使用服务器的同学，请移步[ICS Server](../resources/ICS-Server.md)学习完整流程，并且**确保你可以登陆上ICS服务器**

在服务器上开发方式选择：

- （推荐）使用vscode进行远程连接，具体可以查看教程[Vscode ssh配置](../resources/VScodeRemote-SSH.md)
- （能力强的同学可以尝试，同时可以向助教分享你的配置 🥳）使用tmux + ssh + vim/nvim/emacs等工具进行开发。

登陆成功之后，在自己的家目录下（`/home/username`），应该可以看到一个名为`datalab-sp25`的目录：

如果你缺少这个目录，有三种解决方式：

- 在课程网站上下载[datalab-sp25.tar](../assets/files/datalab-sp25.tar)，然后通过命令`tar xvf datalab-sp25`解压
- 进入本次实验的[公有仓库](https://github.com/xjtu-ics/datalab-sp25)，使用`git clone`克隆仓库到本地（推荐）
- 寻找助教进行解决

当然，助教们希望同学们还是尽量可以自己解决，毕竟一方面助教们平时都很忙，另一方面自己动手查阅资料，解决问题也可以培养自己这方面的能力，这也是这门课开设的初衷。 💪

### 本地开发

也可以自己搭建开发环境，环境要求为：

- Linux 或 WSL (推荐 Ubuntu 22.04 / Arch Linux)
- gcc-11
- GNU Make

!!!note
    上述工具版本仅供参考，使用更高版本的工具链只要不报错就可以。

有关本地环境的搭建指导，请移步[Linux Installation](../resources/LinuxInstallation.md)

自己本地开发的实验资源获取方式：

- 下载文件[datalab-sp25.tar](../assets/files/datalab-sp25.tar)，然后通过命令`tar xvf datalab-sp25.tar`进行解压
- 进入本次实验的[公有仓库](https://github.com/xjtu-ics/datalab-sp25)，使用`git clone`克隆仓库到本地（推荐）
- 找同学/助教发给你

如果你已经顺利的在本地安装或者申请到了一个稳定的Linux环境，并且准备好了实验相关目录，那么就可以顺利的开始你的实验~

### 使用自己的远程仓库进行备份（选做）

不管你使用什么方式获取实验资源，我们都**建议自己使用一个远程仓库进行备份**，以防服务器或者本地环境出现无法恢复的错误。

使用ICS Server的同学，我们已经在服务器上安装了git，本地开发的同学请自己检查是否安装了git，可以使用以下命令检查：

```bash
git --version
```

!!!note
    如果需要通过ssh使用github, 首先在本地生成ssh密钥对，然后将公钥添加到自己的github账户中。


如果你使用服务器或者通过下载压缩包的方式，那么你需要首先建立一个本地仓库，切换到`datalab-sp25`目录，然后输入以下命令：

```bash
git init
```

这会在你的项目根目录下面建立一个`.git`目录，存放你的本地仓库的一些信息。

之后你可以将我们的公开仓库和自己的本地仓库关联：

```bash
git remote add upstream git@github.com:xjtu-ics/datalab-sp25.git
```

这里我们建议你将公有仓库的名字命名为`upstream`，因为通常代表了**上游仓库**，在多人协同开发中，这种仓库通常用于同步本地信息，**即可以pull，但是没有push权限**的仓库。

对于自己建立的仓库，一般需要自己写一个`.gitignore`文件，以屏蔽项目使用的一些临时文件，对于这个实验，一个参考的`.gitignore`文件如下：

```text
*.o
*~
ishow
fshow
btest
```

如果你是直接使用`git clone`的方式，那么可以使用以下命令：

```bash
git clone -o upstream git@github.com:xjtu-ics/datalab-sp25.git
```

这会将本地仓库自动将上游仓库进行关联，并且设置上游仓库名为`upstream`

这么做的好处是，如果助教们或者老师修改了上游仓库的内容（比如README或者测试文件），你可以使用下面的命令进行同步：

```bash
git pull upstream main
```

之后，你可以再关联一个自己的远程仓库进行备份，但是**请务必确保你的仓库一定是私有的**，同时也不要试图在github等网站上搜索学长的代码，因为**每年题目都不一样**。

首先，你需要建立一个远程的私有仓库，可以使用github或其他类似网站，然后记录下自己仓库的url。

然后使用以下命令添加远程仓库：

```bash
git remote add origin git@github.com:your_username/your_repo.git
```

将上述url中的`your_username`和`your_repo`替换成自己的。一般来说，自己的远程仓库通常命名为origin。

添加成功之后，使用以下命令查看一下现有的仓库列表：

```bash
git remote -v
```

你应该可以看到类似以下列表：

```text
origin	git@github.com:Scorpicathe/mydatalab.git (fetch)
origin	git@github.com:Scorpicathe/mydatalab.git (push)
upstream	git@github.com:xjtu-ics/datalab-sp25.git (fetch)
upstream	git@github.com:xjtu-ics/datalab-sp25.git (push)
```

现在和你本地仓库关联的有两个远程仓库，一个是上游仓库，一个是你自己的远程仓库。

那么每次你完成一部分实验之后，可以使用`git add`和`git commit`将更改提交到本地仓库。

然后将本地的提交push到远程：

```bash
git push -u origin main
```

这样你自己的远程仓库包含了实验已完成的部分，即使服务器或者自己的本地环境出现错误无法恢复时，你也可以直接从自己的仓库进行clone，实现了一个备份的功能。

当然，每次push之前建议先从上游仓库pull一下，来同步一下自己本地仓库的内容：

```bash
git pull upstream main
```

### 实验环境测试流程

一个比较推荐的实验环境测试流程如下：

#### 检查文件完整性

解压完成后你将获得如下的一个完整目录，请检查你下载并解压的文件中是否包含如下目录：

```bash
linux$ ls
bits.c  bits.h  btest.c  btest.h  decl.c  dlc  Driverlib.pm  driver.pl  fshow.c  ishow.c  Makefile  README.md  tests.c
```

!!!warning
    如出现文件完整性问题请及时询问同学或者找助教解决相关问题。

#### 尝试`make`

`Makefile` 文件描述了 `Linux` 系统下 `C/C++` 工程的编译规则，它用来自动化编译 `C/C++` 项目。分发下去的实验包内已经有编写好的`Makefile` ，我们只需要在本机中尝试`make`，就可以获得一些 `Linux` 下的可执行文件。

（想要仔细了解`Makefile`相关信息：

[What is a Makefile and how does it work?](https://opensource.com/article/18/8/what-how-makefile)

[Tutorial on writing makefiles](https://www.math.colostate.edu/~yzhou/computer/writemakefile.html))

`make`方法：在对应路径下在命令行输入`make`，回车.

```bash
linux$ make
```

如果`make`成功，一个典型的输出结果如下所示：

```bash

linux$ make                                                                                   
gcc -O -Wall -m32 -lm -o btest bits.c btest.c decl.c tests.c
gcc -O -Wall -m32 -o fshow fshow.c
gcc -O -Wall -m32 -o ishow ishow.c
```

!!!note
    在make的过程中可能会出现一些warning，均属于正常现象~

#### 出错处理

一些可能出现的典型环境问题和解决方法将在附录中做简要解释，一个比较推荐的通用的问题解决方法的路径是：

- 查看报错，根据报错分析产生原因
- 直接咨询Google或者ChatGPT, DeepSeek等
- 若无法成功解决则咨询助教或登录[Piazza](https://piazza.com/stu.xjtu.edu.cn/spring2025/xjtuics)询问

#### 尝试运行

如果成功`make`此时你的实验目录将会变成如下：

```bash
linux$ ls
bits.c  bits.h  btest  btest.c  btest.h  decl.c  dlc  Driverhdrs.pm  Driverlib.pm  driver.pl  fshow  fshow.c  ishow  ishow.c  Makefile  README.md  tests.c  xxxxxx-handin.zip
```

简单验证可用性，我们简单运行一下`make`之后获得可执行文件`btest`

运行方法：命令行输入

```bash
linux$ ./btest
```

此时若运行成功，则会出现：

```bash
linux$ ./btest  
Score	Rating	Errors	Function
ERROR: Test isZero(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
ERROR: Test bitXor(-2147483648[0x80000000],-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
ERROR: Test copyLSB(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
ERROR: Test isNegative(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 1[0x1]
ERROR: Test allEvenBits(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
ERROR: Test byteSwap(-2147483648[0x80000000],0[0x0],0[0x0]) failed...
...Gives 2[0x2]. Should be -2147483648[0x80000000]
ERROR: Test removeRightmostOne(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
ERROR: Test maskBelowHighest(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be -1[0xffffffff]
ERROR: Test largerAbsVal(-2147483647[0x80000001],-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be -2147483648[0x80000000]
ERROR: Test bitReverse(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 1[0x1]
Total points: 0/80
```

出现如上或类似如上的输出结果，恭喜你！这证明您的本地环境已经准备好了，之后就可以快乐的开始Coding。

## 实验任务

实验准备中，我们在实验路径看到非常多的文件，你是否感到了一丝慌张？别慌！大多数的东西都是来帮助你更好的完成你的实验，你本地中唯一需要**更改与提交的代码文件**就是**bits.c**(This is all you need.)。找到这个文件，采用你心仪的编辑器，开始这个实验吧！

事实上，在`bits.c`中已经详细说明了实验的步骤，以及各种代码的规则，请大家仔细阅读`bits.c`的顶部注释部分：

```c
/* 
 * CS:APP Data Lab 
 * 
 * <Please put your name and userid here>
 * 
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.  
 */

#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES:

....
....
....

#endif

```

`#if 0`与`#endif`中的注释部分已经把这个实验要做什么以及怎么做写的很清楚了，这里只做一下总结。

### 第一步：仔细阅读以下实验要求以及代码规则

你的任务是通过修改`bits.c`文件中的函数，来提交你的实验结果。

#### 代码规则：

`bits.c`文件包含了针对10个编程谜题的基本框架。在这个实验中你的任务就是在一个严格的Coding Rules（代码编写规则）之下完成每个函数编写（一个函数就代表一个小谜题），即用一行或多行C代码替换每个函数中的“return”语句，以实现该函数，这个严格的代码代码编写规则如下：

假设你写的函数格式如下：
```c
int Funct(arg1, arg2, ...) {
    /* brief description of how your implementation works */
    int var1 = Expr1;
    ...
    int varM = ExprM;

    varJ = ExprJ;
    ...
    varN = ExprN;
    return ExprR;
}
```
每个"expr"**只能包含**以下这些：

- 整数常量`0`到`255`（`0xFF`），不允许使用大的常量如`0xffffffff`。
- 函数参数和局部变量（不允许使用全局变量）。
- 一元整数操作符 `! ~`
- 二元整数操作符 `& ^ | + << >>`

!!!note
    同时一些编程谜题（函数）进一步限制了运算符的个数，详细的规则在`bits.c`中每个函数上方的注释中有明确的说明，**注意，如果不按照运算符个数实现代码是要扣分的哦(关于评分细则在后面评分中有明确说明)**。

**明确禁止使用的操作包括：**

- 控制结构如`if, do, while, for, switch`等。
- 使用宏定义。例如`#define AND(a, b) ((a) & (b))`是不允许的。
- 在此文件中定义任何额外的函数。
- 调用任何函数。（我们在`bits.c`中包含了`printf`以供大家`debug`使用，其余只允许使用`C`语言基础的运算符进行求解，最终提交的代码请不要包含`printf`）
- 使用其他操作符，如`&&, ||, -, ?, :`，每个谜题的上方注释处都有明确的合法操作符种类（Legal Ops）。
- 使用任何形式的类型转换。
- 使用除`int`之外的任何数据类型，同时你不能使用数组、`struct`或`union`。
- 不允许使用`include`添加新的库。

#### 可以确定的假设：

在编写代码的时候，你可以建立如下假设：

- 数据类型`int`的值为`32`位。
- 带符号数据的右移以算术右移方式执行。
- 对于`int`数据类型，如果移位量小于`0`或大于`31`时，行为不可预测，也就是说当移位运算时，移动量应该在`0` 和 `31` 之间。

#### 注意事项：

- 可以使用`dlc`（`datalab checker`）编译器来检查你的答案是否符合代码规则。如果不符合代码规则，即使可以实现对应的功能，也不会得分。

- 每个函数都有最大操作符数量(`Max Ops`)，由`dlc`检查，如果超过使用的最大操作符数量，是可以允许的，但是要扣除一部分分数（具体在得分中说明）。

- 使用`btest`测试工具来检查你写的函数的正确性。

- 使用`driver.pl`正式验证你的函数。

!!! note
    由于dlc的一些实现细节所限，大家如果需要声明局部变量，请务必将所有局部变量的声明语句放在代码块开始之前，否则dlc会出现误判。

### 第二步：根据代码规则修改`bits.c`中的函数

**重要提示**：为避免评分时出现意外，请确保使用`dlc`编译器检查你的解决方案是否遵循编码规则，并使用`driver.pl`正式验证你的解决方案是否正确。

### 一个例子：

看完了以上的一些冗长的限制之后，你可能感受到了疑惑。没事，接下来我们将从一个小例子出发，来解释这个实验到底需要做些什么。

`bits.c`中的每个小的谜题都会有谜题本身的限制，限制的具体内容写在了谜题函数上面的注释格式中。一个典型的谜题例子如下：

```c
/* 
 * minusOne - return a value of -1 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 2
 *   Rating: 1
 */
int minusOne(void) {
  return 1;
}
```

如上题

- 题名：`minusOne`
- 题目要求：`return a value of -1` ，返回一个`-1`
- 合法的操作符：`! ~ & ^ | + << >>`
- 最多使用的操作符数量：2个
- 题目等级：1星

因此我们编写如下的程序代码：

```c
int minusOne(void) {
  return ~0;
}
```

如果在代码中使用了非法的操作符`-`，例如：

```c
int minusOne(void) {
  return -1;
}
```
尽管结果正确（使用`btest`测试没问题），这个谜题仍是不得分的。同样，如果在函数中使用了`if for`或`0xffffffff`，以及有任何规则禁止的操作，都是不得分的。

## 谜题

这个小节简要地介绍了你将要面临的小谜题，同时你可以参考解决一个谜题用到的操作符数量~

```text
Correctness Results	Perf Results
Points	Rating	Errors	Points	Ops	Puzzle
8	8	0	2	1	isZero
8	8	0	2	7	bitXor
8	8	0	2	2	copyLSB
8	8	0	2	2	isNegative
8	8	0	2	7	allEvenBits
8	8	0	2	17	byteSwap
8	8	0	2	3	removeRightmostOne
10	10	0	2	10	maskBelowHighest
10	10	0	2	18	largerAbsVal
4	4	0	2	40	bitReverse

Score = 100/100 [80/80 Corr + 20/20 Perf] (107 total operators)
```

一共有10道题等待你去解决，请**详细核对自己的题目和上述题目是否有出入，如有出入，请联系助教处理**。

## 评分

### 标准评分标准

细心的同学可能会注意到，在每个谜题的描述部分，还有一行`Ratings`，这代表了题目的难度，同时也决定了如何评分。

谜题的`Ratings`分为1星，2星，3星和4星共四个等级。当然，星级越高，难度越高，不同星级的题目难度可以概括为：

- 1星和2星题，只需要很简单的逻辑和少数几个操作符就可以完成
- 3星题，增加了思维难度，但是不需要大量的操作符（实现简单）
- 4星题，具有最高的思维难度或大量的操作符（实现复杂）

不过同学们也不用担心，我们为大家准备的10道题目包含了2道1星题，5道2星题，2道三星题和1道四星题，保证同学们可以很轻松的拿到一个基本分数。

你的最终得分的计算规则如下（共100分）：

- 1星和2星题，每题8分
- 3星题，每题10分
- 4星题，每题4分

因此，10道题的总分按照上述规则加起来一共80分，如果你可以通过`btest`的检查，并且代码符合上文提到的代码规则（即可以通过`dlc`的检查），你将得到基本的80分。

同时谜题的**最大操作符数量也是有限制**的，如果你可以实现在最大操作符数量之内完成函数，每个函数得2分，如果你可以保持正确性并且操作符数量在最大操作符数量之内，你将获得剩余的“性能分”20分。

### 迟交
在超过原定的截止时间后，我们仍然接受同学的提交。此时，在lab中能获得的最高分数将随着迟交天数的增加而减少，具体服从以下给分策略：

超时7天（含7天）以内时，每天扣除3%的分数
超时7~14天（含14天）时，每天扣除4%的分数
超时14天以上时，每天扣除7%的分数，直至扣完
以上策略中超时不足一天的，均按一天计，自ddl时间开始计算。届时在线学习平台将开放迟交通道。

评分样例：如某同学小H在lab中取得95分，但晚交3天，那么他的最终分数就为`95*(1-3*3%)=86.45`分。同样的分数在晚交8天时，最终分数则为`95*(1-7*3%-1*4%)=71.25`分。

## 本地自动测试你的工作
上一节中，我们简要地谈到了你的实验成绩的组成，你可能感到了慌张。我该怎么保证我本地的程序是bugfree的呢？难不成要我自己手动人肉测试吗！？这显然是一种苛求，事实上，我们将完整的测试程序在实验分发包中给了你。

- 你可以自行使用测试程序`btest`去测试你的程序的正确性。

- 与此同时，为了测试代码是否符合代码规则，我们给出了`dlc`文件，`dlc`文件可以测试你的答案中是否符合代码规则，是否超出了最大操作符数量。

- 最后可以使用`driver.pl`来测试程序的最终得分，`driver.pl`的测试这我们最终测试你提交上来文件的方法一致，换句话说，你如果在本地使用`driver.pl`测试得到了满分，那么你在最终的考核中也会得到一致的分数。

- 当然实验中还有两个程序可以帮助你完成这个实验，就是`ishow`和`fshow`。

### 代码功能正确性 -> `btest`
如果你的`bits.c`的程序编写满足C语言要求并可以通过编译，在本地根目录下`make`之后你将会获得：

```bash
linux$ make
```

如下的目录：

```bash
linux$ ls
bits.c  bits.h  btest  btest.c  btest.h  decl.c  dlc  Driverlib.pm  driver.pl  fshow  fshow.c  ishow  ishow.c  Makefile  README.md  tests.c
```

其中`btest`程序通过多次调用它们来检查`bits.c`中函数的正确性不同的参数值。要构建和使用它，请键入以下两个命令：

```bash
linux$ make
linux$ ./btest
```

需要注意的第一点是，你**每次修改你的`bits.c`文件之后，你需要通过`make`重新`build`之后再进行测试**：

即如果你新完成了一个谜题，你想要重新测试，则需要完成如下的流程：

```bash
linux$ make
linux$ ./btest
```

通常来说你会获得如下类型的运行结果：

```bash
linux$ ./btest
Score	Rating	Errors	Function
 8	8	0	isZero
 8	8	0	bitXor
ERROR: Test copyLSB(-2147483648[0x80000000]) failed...
...Gives 2[0x2]. Should be 0[0x0]
 8	8	0	isNegative
 8	8	0	allEvenBits
 8	8	0	byteSwap
 8	8	0	removeRightmostOne
 10	10	0	maskBelowHighest
 10	10	0	largerAbsVal
 4	4	0	bitReverse
Total points: 72/80
```

如上输出中告诉你每一题的得分，如果你的程序出错，则会输出对应的出错的题目与出错时候的输入和输出。

如上中，`btest`告诉我们：

*Test copyLSB*测试用例出差错
出错的输入是：`-2147483648[0x80000000]`
你的输出是：`2[0x2]`
正确的解应该是`0[0x0]`
根据输出的结果我们返回去继续修改我们的代码。

### 代码规则检测工具 -> `dlc`

btest并不会告诉我们写的代码是不是符合代码规则，这时候就需要使用`dlc`了。`dlc`的使用方法非常简单，如下：

```bash
linux$ ./dlc bits.c
```

如果你的代码都符合代码规则，那不会输出任何结果。

如果你的代码中有不符合代码规则的地方，一个典型的输出结果如下所示：

```bash
linux$ ./dlc bits.c
dlc:bits.c:202:copyLSB: Illegal if
dlc:bits.c:230:conditional: Illegal constant (0xffffffff) (only 0x0 - 0xff allowed)
dlc:bits.c:245:isPositive: Warning: 10 operators exceeds max of 8
```

如上，`dlc`告诉我们:
在202行，`copyLSB`函数中，使用了非法的`if`。
在230行，`conditional`函数中，使用了非法的常量`0xffffffff`。
在245行，`isPositive`函数中，使用了`10`个操作符，超过了`Maxops=8`个。

根据输出的结果我们返回去继续修改我们的代码。

`dlc`同时还有很多功能，例如`./dlc -e bits.c`等，你可以通过`./dlc -h`输出的帮助信息去自行了解。

### 实验最终得分工具 -> `driver.pl`

为了计算出自己的最终分数，我们提供了`driver.pl`来计算。

`driver.pl`的使用方法如下：

```bash
linux$ ./driver.pl
```

一个典型的结果如下：
```bash
linux$ ./driver.pl
1. Running './dlc -z' to identify coding rules violations.

2. Compiling and running './btest -g' to determine correctness score.
gcc -O1 -g -Wall   -lm -o btest bits.c btest.c decl.c tests.c 

3. Running './dlc -Z' to identify operator count violations.

4. Compiling and running './btest -g -r 2' to determine performance score.
gcc -O1 -g -Wall   -lm -o btest bits.c btest.c decl.c tests.c 

5. Running './dlc -e' to get operator count of each function.

Correctness Results	Perf Results
Points	Rating	Errors	Points	Ops	Puzzle
8	8	0	2	1	isZero
8	8	0	2	7	bitXor
0	8	1	0	0	copyLSB
8	8	0	2	2	isNegative
8	8	0	2	7	allEvenBits
8	8	0	2	17	byteSwap
8	8	0	2	3	removeRightmostOne
10	10	0	2	10	maskBelowHighest
10	10	0	2	18	largerAbsVal
4	4	0	2	40	bitReverse

Score = 90/100 [72/80 Corr + 18/20 Perf] (105 total operators)

```
可以看到，最终得了90分，其中`copyLSB`函数由于不符合代码规则，不得分。

### 进制转换工具

在题目编写过程中，您可能需要一些工具的帮助来确定一些10进制数的16进制格式。

我们为您提供了相应的便捷工具`ishow`、`fshow`，您可以使用提供的程序 `ishow `查看整数的十进制和十六进制表示形式。首先编译代码如下：

```bash
linux$ make
```

然后使用它来检查在命令行中键入的十六进制和十进制值：

```bash
linux$  ./ishow 0x80000000
Hex = 0x80000000,       Signed = -2147483648,   Unsigned = 2147483648
linux$  ./ishow -1
Hex = 0xffffffff,       Signed = -1,    Unsigned = 4294967295
```
它会帮助你完成进制的转换。

同理我们还提供了`fshow`工具，这是一个浮点数的转换器，但是这次的实验没有涉及，所以不做要求，大家有兴趣可以自行尝试，使用方法与`ishow`类似。


## 代码提交

在`datalab-sp25` 目录下执行`make submit`

```bash
linux$ make submit
```

目录下都会生成一个名为 `<userid>-handin.zip `的文件（其中 `<userid> `为`Linux`系统中你的用户名）。（每次修改代码后，记着要重新运行`make submit`）

在[在线学习平台](http://class.xjtu.edu.cn/)上的作业模块中，将该文件作为附件提交即可。

## 一些小的建议

- Start Early
- 谜题可能比较复杂，可能一时间不可以直接想出优秀的满足要求的解法，但是不要气馁，没有人可以马上给出最优的解法。一个比较好的解题尝试路径是：
  - 先尝试在纸上写出一般的解法
  - 从一般解中找出更一般性的规律，这些规律可能通常需要你的灵光一现，但是对相信聪明的你来说这不是问题。
- 如果您是采用自己本地的环境，那么总会出现一些依赖缺失，软件未安装等等之类的错误。请大家不要慌张，一个好的程序员需要更好的了解自己手里的工具，而自己搭建环境往往就是其中很重要的一部分，请大家自行查询相关环境问题，自己动手解决问题（折腾（笑））的能力在计算机专业的学习中是非常重要的。
- 找到适合自己的好工具的能力：请大家在不断地动手中学习并找到适合自己的工具，以提高自己的效率。

最后祝大家玩的愉快。

---

Copyright © 2025 XJTU ICS-TEAM

