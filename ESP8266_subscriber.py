'''
实验名称：MQTT通信
MQTT助手：http://www.tongxinmao.com/txm/webmqtt.php#collapseOne
'''
import network,time
from simple import MQTTClient #导入MQTT板块
from machine import SoftI2C,Pin,Timer
from ssd1306 import SSD1306_I2C

#初始化相关模块
i2c = SoftI2C(sda=Pin(4), scl=Pin(5))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

#WIFI连接函数
def WIFI_Connect():

    WIFI_LED=Pin(2, Pin.OUT) #初始化WIFI指示灯

    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('CMCC-jynY', 'wl180222') #输入WIFI账号密码

        while not wlan.isconnected():

            #LED闪烁提示
            WIFI_LED.value(1)
            time.sleep_ms(300)
            WIFI_LED.value(0)
            time.sleep_ms(300)

            #超时判断,15秒没连接成功判定为超时
            if time.time()-start_time > 15 :
                print('WIFI Connected Timeout!')
                break

    if wlan.isconnected():
        #LED点亮
        WIFI_LED.value(1)

        #串口打印信息
        print('network information:', wlan.ifconfig())

        #OLED数据显示（如果没接OLED，请将下面代码屏蔽）
        oled.fill(0)   #清屏背景黑色
        oled.text('IP/Subnet/GW:',0,0)
        oled.text(wlan.ifconfig()[0], 0, 20)
        oled.text(wlan.ifconfig()[1],0,38)
        oled.text(wlan.ifconfig()[2],0,56)
        oled.show()
        return True

    else:
        return False

def MQTT_callback(topic, msg):
    print('topic: {}'.format(topic))
    print('msg: {}'.format(msg))
    oled.fill(0)
    oled.text(msg,0,0)
    oled.show()

#接收数据任务
def MQTT_Rev(tim):
    client.check_msg()

#执行WIFI连接函数并判断是否已经连接成功
if WIFI_Connect():

    SERVER = 'bemfa.com'
    PORT = 9501
    CLIENT_ID = '71ab7601b669439f89ebf5910eab828a' # 客户端ID
    TOPIC = 'ESP8266MQTT' # TOPIC名称
    client = MQTTClient(CLIENT_ID, SERVER, PORT)

    oled.fill(0)
    oled.text("init>>>",0,0)
    oled.show()

    client.set_callback(MQTT_callback)  # 配置回调函数
    client.connect()
    client.subscribe(TOPIC)  # 订阅主题

    oled.fill(0)
    oled.text("connected",0,0)
    oled.show()


    #开启RTOS定时器，编号为-1,周期1000ms，执行socket通信接收任务
    tim = Timer(-1)
    tim.init(period=1000, mode=Timer.PERIODIC,callback=MQTT_Rev)
