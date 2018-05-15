# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018
# Cedric Tan, cedric_mx@163.com
'''use PyPDF2 and reportlab package to watermark pdf by text'''

import os
import time

from PyPDF2 import PdfFileWriter, PdfFileReader
import reportlab.pdfbase.ttfonts
reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont('song', r'D:\temp\simsun.ttc'))
from reportlab.pdfgen import canvas

# Create pdf
def create_watermark(text):
    """
    创建PDF水印模板
    """
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('D:/watermark.pdf')
    # 设置字体和大小
    c.setFont('song', 60)
    # 水印文字颜色
    c.setFillColorRGB(0,0,0)
    # 水印透明度
    c.setFillAlpha(0.3)
    # 水印文字位置和内容
    c.drawCentredString(300, 450, text)

    c.save()

    pdf_watermark = PdfFileReader(open('D:/watermark.pdf', 'rb'))
    return pdf_watermark

def pdf_watermark_by_text(input_path, watermark_text, output_path):
    """给指定PDF文件文件加上水印
    input_path - 要加水印的源PDF文件
    pdf_watermark - PDF水印模板
    max_page - 加水印的最大页数
    """
    time_start = time.time()
    # Make sure inputfile exist
    if not os.path.exists(input_path):
        logger.error(input_path + ' ERROR:Input not exists')
        return {"status": 1, "msg": 'ERROR:Input not exists', "data": "", "result": 0}

    # Make sure output path exists
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    pdf_output = PdfFileWriter()
    with open(input_path, 'rb') as input_stream:
        pdf_input = PdfFileReader(input_stream)

    # PDF文件被加密了
    # if pdf_input.getIsEncrypted():
    # print '该PDF文件被加密了.'
    # # 尝试用空密码解密
    # try:
    #     pdf_input.decrypt('')
    # except Exception, e:
    #     print '尝试用空密码解密失败.'
    #     return False
    # else:
    #     print '用空密码解密成功.'

        # 获取PDF文件的页数
        pageNum = pdf_input.getNumPages()
        pdf_watermark = create_watermark(watermark_text)
        # 给每一页打水印
        for i in range(pageNum):
            page = pdf_input.getPage(i)
            page.mergePage(pdf_watermark.getPage(0))
            pdf_output.addPage(page)

        # 最后输出文件
        output_stream = open(output_path, 'wb')
        pdf_output.write(output_stream)
        output_stream.close()

        time_end = time.time()
        time_run = round(float(time_end-time_start), 2)
        data = str(time_run) + ' s'
        return {"status": 1, "msg": 'success', "data": data, "result": 1}



if __name__ == '__main__':
    # input_path = r'D:\temp\Test_watermark\pdftest.pdf'
    # watermark_text = u'To jianwei'
    # output_path = r'D:\temp\Test_watermark\result.pdf'
    # print (pdf_watermark_by_text(input_path, watermark_text, output_path))
    create_watermark(u'谭家成')

    # create_watermark(u'中文测试')
    # from reportlab.pdfbase import pdfmetrics
    # a = pdfmetrics.getRegisteredFontNames()
    # pdfmetrics.dumpFontData()
    # print(a)
