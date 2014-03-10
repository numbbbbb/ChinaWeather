ChinaWeather
===========
* 通过 BeautifulSoup 解析中国气象网上的数据
* 只支持Python2


安装
===========

    $ sudo pip install ChinaWeather


依赖
===========
BeautifulSoup


支持城市列表
===========
* [所有城市](http://wap.weather.gov.cn/forecast/AAH/index.html)


使用方法
===========
首先获取城市天气的网址，方法是在[所有城市](http://wap.weather.gov.cn/forecast/AAH/index.html)中找到具体的城市，注意先选省再选市，一定要具体到市，确定网页上显示的是该市的气象信息，然后复制网站。

    >>> import ChinaWeather
    >>> print ChinaWeather.get('http://wap.weather.gov.cn/forecast/AAH/hefei.html')[u'天气']      # 注意输入是刚才复制的网址
    多云
    >>> print ChinaWeather.get('http://wap.weather.gov.cn/forecast/AAH/hefei.html')[u'气压']
    1021hPa


返回值结构
===========
* 天气 —— 字符串；当前天气
* 气压 —— 字符串：当前气压
* 最新实况 —— 字符串；更新时间
* 温度 —— 字符串；温度
* 体感温度 —— 字符串；体感温度
* 舒适感 —— 字符串；舒适感
* 风向 —— 字符串；风向和风力
* 相对湿度 —— 字符串；相对湿度


协议
===========
基于[WTFPL](http://en.wikipedia.org/wiki/WTFPL)协议开源。
