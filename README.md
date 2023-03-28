# fofa-helper

### 简介

免费收集fofa数据，利用添加时间筛选原理
也可以自定义APIKEY获取更多数据
支持网站存活检测

### 安装

```shell
git clone https://github.com/chujian521/fofa-helper
```

```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 配置

无需账号可直接使用，也可以设置APIKEY

### 运行

运行`fofa.py` , `-k`或`--keyword` 参数传入搜索关键字

更多参数查看 `--help`

> python3 fofa.py --help

```shell
 ____    _____   ____    ______
/\  _`\ /\  __`\/\  _`\ /\  _  \
\ \ \L\_\ \ \/\ \ \ \L\_\ \ \L\ \
 \ \  _\/\ \ \ \ \ \  _\/\ \  __ \
  \ \ \/  \ \ \_\ \ \ \/  \ \ \/\ \
   \ \_\   \ \_____\ \_\   \ \_\ \_\
    \/_/    \/_____/\/_/    \/_/\/_/
 __  __          ___
/\ \/\ \        /\_ \
\ \ \_\ \     __\//\ \    _____      __   _ __
 \ \  _  \  /'__`\ \ \  /\ '__`\  /'__`\/\`'__\
  \ \ \ \ \/\  __/ \_\ \_\ \ \L\ \/\  __/\ \ \/
   \ \_\ \_\ \____\/\____\ \ ,__/\ \____\ \_\
    \/_/\/_/\/____/\/____/ \ \ \/  \/____/ \/_/
                            \ \_\
                             \/_/               V1.0.0


usage: fofa.py [-h] [--timesleep TIMESLEEP] [--timeout TIMEOUT] --keyword
               KEYWORD [--endcount ENDCOUNT] [--level LEVEL] [--output OUTPUT]
               [--fuzz] [--savepath SAVEPATH] [--savename SAVENAME]
               [--checkurl CHECKURL]

Fofa-helper v1.0.0 使用说明

optional arguments:
  -h, --help            show this help message and exit
  --timesleep TIMESLEEP, -t TIMESLEEP
                        爬取每一页等待秒数,防止IP被Ban,默认为3
  --timeout TIMEOUT, -to TIMEOUT
                        爬取每一页的超时时间
  --keyword KEYWORD, -k KEYWORD
                        fofa搜索关键字
  --endcount ENDCOUNT, -e ENDCOUNT
                        爬取结束数量
  --level LEVEL, -l LEVEL
                        爬取等级: 1-3 ,数字越大内容越详细,默认为 1
  --output OUTPUT, -o OUTPUT
                        输出格式:txt、json,默认为txt
  --fuzz, -f            关键字fuzz参数,增加内容获取粒度
  --savepath SAVEPATH, -sp SAVEPATH
                        保存结果的路径，默认为当前文件夹下的result目录
  --savename SAVENAME, -sn SAVENAME
                        保存结果的文件名称
  --checkurl CHECKURL, -ck CHECKURL
                        是否检查url有效性，默认为False
```

爬取的结果默认会存储到`result/查询关键字_时间戳.txt`文件中

### 测试

使用命令 

> python fofa.py --keyword thinkphp --endcount 100

爬取一百条数据轻轻松松

### 致谢

参考Cl0udG0d/Fofa-hack
