
### Requirement
```
pip install python-qbittorrent
```
### 首次运行
```
python autoremove.py
```
配置文件
.qBautoremove/config
webui_url = http://127.0.0.1:8080（默认端口号，请自行修改）
seedtime 单位小时
exception_tracker 排除tracker，填入相关tracker字符，用逗号分隔
比如：landof.tv,hdchina
upload_speed有问题，请留空

### 再次运行

```
nohup python autoremove.py &
```
