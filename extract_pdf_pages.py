#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("错误: 未安装PyPDF2库")
    print("请使用以下命令安装: pip install PyPDF2")
    sys.exit(1)

def extract_pages(input_path, output_path, start_page, end_page):
    """
    从PDF文件中提取指定页面范围并创建新的PDF文件
    
    参数:
        input_path (str): 输入PDF文件路径
        output_path (str): 输出PDF文件路径
        start_page (int): 起始页码 (从1开始)
        end_page (int): 结束页码 (从1开始)
    """
    if not os.path.exists(input_path):
        print(f"错误: 输入文件 '{input_path}' 不存在")
        return False
    
    try:
        # 打开输入PDF文件
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        # 检查页面范围是否有效
        total_pages = len(reader.pages)
        if start_page < 1 or end_page > total_pages or start_page > end_page:
            print(f"错误: 无效的页面范围。PDF文件共有 {total_pages} 页")
            return False
        
        print(f"正在从 '{input_path}' 提取第 {start_page} 到第 {end_page} 页...")
        
        # 提取指定页面范围的页面 (PyPDF2使用0为基础的索引)
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])
        
        # 保存新的PDF文件
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"已成功创建新的PDF文件: '{output_path}'")
        return True
    
    except Exception as e:
        print(f"处理PDF文件时出错: {str(e)}")
        return False

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='从PDF文件中提取指定页面范围')
    parser.add_argument('input_pdf', help='输入PDF文件路径')
    parser.add_argument('output_pdf', help='输出PDF文件路径')
    parser.add_argument('start_page', type=int, help='起始页码 (从1开始)')
    parser.add_argument('end_page', type=int, help='结束页码 (从1开始)')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 提取页面
    extract_pages(args.input_pdf, args.output_pdf, args.start_page, args.end_page)

if __name__ == '__main__':
    main() 