'''
@Author: your name
@Date: 2020-07-24 16:58:52
@LastEditTime: 2020-07-28 17:31:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \py\py1.py
'''
import serial
import time

com = serial.Serial()


def set_port(num, baud):
    com.port = num
    com.baudrate = baud
    com.bytesize = 8
    com.stopbits = 1
    com.parity = 'N'


def open_port():
    com.open()
    if (com.isOpen()):
        print("%s打开成功" % (com.port))
    else:
        print("%s打开失败" % (com.port))


def close_port():
    com.close()
    if (com.isOpen()):
        print("%s关闭失败" % (com.port))
    else:
        print("%s关闭成功" % (com.port))


# def write_port(hex):
#     com.write(hex)

hex_1 = bytes.fromhex(
    '01036E333132303131313233343536303130303030413839303030313646303030313639444330323032303036323931383030313231392E31323337312E313234373132332E31323536313131332E31323632303130332E313232343131332E3134363631332E31343638312E31323931CB16'
)
hex_2 = bytes.fromhex(
    '01036F333132303131313233343536303130303030413839303030313646303030313639444330323032303036323931383030313231392E31323337312E313234373132332E31323536313131332E31323632303130332E313232343131332E3134363631332E3134363831322E31323931007D'
)

#if __name__ == '__main__':
set_port('COM3', 115200)
#open_port()
# while (com.read() != 'q'):
#     com.write(hex_1)
#     time.sleep(10)
#     com.write(hex_2)
#     time.sleep(10)

close_port()