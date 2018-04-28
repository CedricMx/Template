handlers:后端python程序，处理前端的请求，并操作数据库；

methods：放函数和类，如调用数据库的函数，由handlers里面的程序使用；

statics：静态文件，如图片、css和javascript文件等；

templates：放模板文件，以html为扩展名的，直接面对用户

-----------------------------------------------------------------------

url.py 设置网站的目录结构

application.py 对网站系统的基本配置，建立网站的请求处理集合

servers.py 将tornado服务器运行起来，囊括url.py和application.py的对象属性设置