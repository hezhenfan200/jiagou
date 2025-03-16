import os
import tempfile
from PyPDF2 import PdfReader, PdfWriter

def remove_first_page(folder_path):
    """
    删除指定文件夹中所有PDF文件的第一页
    
    Args:
        folder_path: 包含PDF文件的文件夹路径
    """
    # 获取文件夹中所有PDF文件
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"在 {folder_path} 中没有找到PDF文件")
        return
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        
        try:
            # 打开PDF文件
            reader = PdfReader(pdf_path)
            
            # 检查PDF页数
            if len(reader.pages) <= 1:
                print(f"跳过 {pdf_file}，因为它只有一页或没有页面")
                continue
            
            # 创建一个新的PDF写入器
            writer = PdfWriter()
            
            # 添加除第一页外的所有页面
            for page_num in range(1, len(reader.pages)):
                writer.add_page(reader.pages[page_num])
            
            # 在同一目录下创建临时文件
            temp_path = os.path.join(folder_path, f"temp_{pdf_file}")
            
            # 将内容写入临时文件
            with open(temp_path, 'wb') as output_file:
                writer.write(output_file)
            
            # 替换原文件
            os.remove(pdf_path)
            os.rename(temp_path, pdf_path)
            
            print(f"已成功从 {pdf_file} 中删除第一页")
            
        except Exception as e:
            print(f"处理 {pdf_file} 时出错: {str(e)}")

if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    folder_path = input("请输入包含PDF文件的文件夹路径: ")
    
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print("指定的路径不是一个有效的文件夹")
    else:
        remove_first_page(folder_path)
        print("处理完成") 