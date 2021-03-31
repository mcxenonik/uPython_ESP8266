from machine import Pin, I2C
import ssd1306

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('PUPCIA', 0, 0)
oled.text('JEST', 0, 20)
oled.text('PUPCIOM', 0, 40)

oled.show()
