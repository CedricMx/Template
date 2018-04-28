# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com

'''
Use ffmpeg to watermark image and video by image or text
'''

import os

class watermark_position:
    # LeftUp = 0
    # LeftBottom = 1
    # RightBottom = 2
    # RightUp = 3
    # Center = 4
    position = [
        {'key':'LeftUp', 'value':'x=0:y=0'},
        {'key':'LeftBottom', 'value':'x=0:y=(h-th)'},
        {'key':'RightBottom', 'value':'x=(w-tw):y=(h-th)'},
        {'key':'RightUp', 'value':'x=(w-tw):y=0'},
        {'key':'Center', 'value':'x=(w-tw)/2:y=(h-th)/2'},
    ]

    @classmethod
    def text_position(self, key):
        for i in watermark_position.position:
            if (i['key']==key):
                return i['value']


class watermark_opacity:
    opacity = [
        {'key':'light', 'value':0.2},
        {'key':'mid', 'value':0.4},
        {'key':'heavy', 'value':0.6}
    ]

    @classmethod
    def text_opacity(self, key):
        for i in watermark_opacity.opacity:
            if (i['key']==key):
                return i['value']



def image_video_watermark_by_image(input_path, watermark_path, output_path):
    '''
    给图片或视频打图片水印
    成功返回 0
    失败返回 1
    '''
    cmd = r'ffmpeg -i {} -i {} -filter_complex "overlay=5:5" {}'.format(input_path, watermark_path, output_path)
    # cmd = r'ffmpeg -i {} -i {} -filter_complex "overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" {}'.format(input, watermark, output)
    print cmd
    status = os.system(cmd)

    print status
    return status

def image_video_watermark_by_text(input_path, watermark_text, output_path, position='Center', opacity='light'):
    '''
    给图片或视频打文本水印

    position传入水印位置参数:
        LeftUp : 左上
        LeftBottom : 左下
        Center : 中间
        RightUp : 右上
        RightBottom : 右下

    opacity传入水印透明度参数:
        ligth : 水印颜色浅
        mid : 水印颜色适中
        heavy :  水印颜色深

    成功返回 0
    失败返回 1
    '''
    text_position = watermark_position.text_position(position)
    text_opacity = watermark_opacity.text_opacity(opacity)
    # cmd = '''ffmpeg -y -i {} -b 1000k -vf drawtext=fontfile="simsun.ttc":text="{}":fontcolor=white@0.2:fontsize=96:x=(w-tw)/2:y=(h-th)/2 {}'''.format(input_path, watermark_text, output_path)
    # cmd = '''ffmpeg -y -i {} -vf drawtext=fontfile="simsun.ttc":text="{}":fix_bounds=true:fontcolor=white@0.2:fontsize=96:x=(w-tw)/2:y=(h-th)/2 {}'''.format(input_path, watermark_text, output_path)
    cmd = '''ffmpeg -y -i {0} -vf drawtext=fontfile="simsun.ttc":text="{1}":fix_bounds=true:fontcolor=white@{2}:fontsize=96:{3} {4}'''.format(input_path, watermark_text, text_opacity, text_position, output_path)
    # cmd = '''magick convert {} -gravity Center -fill #FFFFFF44 -pointsize 72 -font "simsun.ttc" -draw "text 0,0 '{}'" {}'''.format(input_path, watermark_text, output_path)
    print cmd
    status = os.system(cmd)

    print status
    return status

def word_excel_watermark_by_text():
    pass

def pdf_watermark_by_text():
    pass

if __name__ == '__main__':
    input = 'D:/temp/Test_watermark/watermark.jpg'
    input = 'D:/temp/Test_watermark/video.mp4'
    watermark = 'D:/temp/Test_watermark/wm.jpg'
    output = 'D:/temp/Test_watermark/result.jpg'
    output = 'D:/temp/Test_watermark/result.mp4'

    image_video_watermark_by_text(input, 'To Jianwei', output, 'RightBottom', 'light')
    image_video_watermark_by_text(input_path, watermark_text, output_path)
