# V2raySwitch 

> 主要功能为快速切换v2ray状态快捷键。
>
> 默认F4为`自动配置系统代理`模式，F3为`清除系统代理`模式。
>
> 快捷键可以自己设置。
> 默认windows的v2rayN，稍作修改也可以在linux上运行[狗头]

### 安装

1. 安装AutoHotkey（本仓库里有在官网下载的安装包(在`dep`目录)，也可以自行在官网下载，双击傻瓜式安装）
2. 【可选步骤】在`switchV2rayToNormal.ahk`、 `switchV2rayToGlobal.ahk`文件第一行设置快捷键，默认为F4切换为全局模式，F3切换为正常无代理模式
3. 将`v2raySwitchL.exe`、`switchV2rayToNormal.ahk`、 `switchV2rayToGlobal.ahk`三个文件放入你的`v2rayN.exe`所在的目录
4. 每次双击`v2rayInit.bat`启动`v2rayN.exe`、`switchV2rayToNormal.ahk`、 `switchV2rayToGlobal.ahk`
5. 建议将`v2rayInit.bat`发送到桌面快捷方式或者开机启动目录以便于每次双击启动配置


## Moreover

- 打包exe命令：pyinstaller --noconsole -F v2raySwitchL.py
- 不想exe运行或者测试时，可以将`v2raySwitchL.py`放在`v2rayN.exe`所在目录后，直接命令行运行python文件:
  - 切换`自动配置系统代理`模式： `python  v2raySwitchL.py g`  
  - 切换`清除系统代理`模式：  `python  v2raySwitchL.py n`

### 声明

本仓库代码仅供技术研究使用，请勿用于非法用途，否则后果作者概不负责。
