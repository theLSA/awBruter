awBruter - 千倍爆破一句话木马密码工具
===
<br/>
# 概述<br/>
简洁的千倍一句话木马密码爆破工具，支持apache,iis(php,asp,apsx),原理就是apache和iis支持多参数提交。<br/>
<br/>
<br/>


#需求<br/>
requests<br/>
<br/>
<br/>


#快速开始<br/>
python awBruter.py -h<br/>
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter00.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173/onewordshell.asp"
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter01.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173/onewordshell.asp" -v
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter02.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173/onewordshell.aspx" -v
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter03.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173/onewordshell.aspx" -f ../dic0.txt -v
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter04.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173:8999/onewordshell.php" -f ../dic0.txt -v
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter05.png)<br/>
<br/>
python awBruter.py -u "http://192.168.43.173:8999/onewordshell.php"
![](https://github.com/theLSA/awBruter/raw/master/demo/awbruter06.png)<br/>
<br/>
<br/>

#To Do List<br/>
1.增加随机user-agent,代理ip等附加功能<br/>
2.增加jsp一句话的密码爆破<br/>
<br/>
<br/>

#反馈<br/>
*博客: http://www.lsablog.com<br/>
*email: lsasguge196@gmail.com<br/> 
	2894400469@qq.com<br/>
*issue:
