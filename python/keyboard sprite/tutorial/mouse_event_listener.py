# https://lanshiqin.com/2fb233e2/

#鼠標事件監聽器

from pynput import mouse

# 屬標移動事件

def on_move(x,y):
    print('move',(x,y))

#屬標點擊事件
def on_click(x, y, button, pressed):# button参数对象的name属性值为left或者right,通过该属性值可以判断是鼠标的左键还是右键产生的点击事件。pressed参数值为True时表示当前鼠标左或右键按压，False时表示鼠标左或右键抬起事件
    print('[Click]', (x, y, button.name, pressed)) 

# 鼠标滚动事件
def on_scroll(x, y, x_axis, y_axis): #x_axis的值>0表示向上，<0表示向下，同样的y_axis的负值和正值代表左滑和右滑状态。
    print('[Scroll]', (x, y, x_axis, y_axis))


# 监听事件绑定
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
