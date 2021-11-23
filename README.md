# RaspberryPi-Auto-photos
> 树莓派自动拍照系统，通过修改photoInfo.json中的数据即可改变拍照分辨率和时间间隔，拍摄照片文件存储在 ./images 中

photoInfo.json中ID为设备名称，Resolution为拍摄分辨率，interval为拍摄时间间隔(单位为s)，amount为拍摄数量。

若无法正常打开摄像头，请修改Camara中的26行 frame = cv2.VideoCapture(0) 改变设备地址

输入`python3 main.py`即可运行。