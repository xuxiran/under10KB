#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
证件照处理工具 - 照片规格处理器
将任意图片处理为：25mm x 35mm (295px x 413px) 的证件照规格
输出文件小于 10KB，JPEG 格式
"""

from PIL import Image
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil


def process_photo(input_path, output_path=None):
    """
    处理照片：缩放到 295x413，并控制文件大小在 10KB 以内
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径（可选，默认为 input_path 所在目录的 output.jpg）
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"找不到输入文件: {input_path}")
    
    # 设置输出路径
    if output_path is None:
        base_dir = os.path.dirname(input_path) or '.'
        output_path = os.path.join(base_dir, 'output.jpg')
    
    # 打开图片
    print(f"📷 正在处理: {input_path}")
    img = Image.open(input_path)
    
    # 转换为 RGB 模式（处理 PNG 等格式）
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    print(f"   原始尺寸: {img.size[0]}x{img.size[1]} px")
    
    # 目标尺寸: 295px x 413px
    target_width = 295
    target_height = 413
    
    # 先按比例缩放，使高度达到413
    scale = target_height / img.size[1]
    new_width = int(img.size[0] * scale)
    new_height = target_height
    
    print(f"   缩放后尺寸: {new_width}x{new_height} px")
    
    # 缩放到高度为413
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # 居中裁剪到目标宽度
    if new_width > target_width:
        left = (new_width - target_width) // 2
        top = 0
        right = left + target_width
        bottom = target_height
        cropped_img = resized_img.crop((left, top, right, bottom))
    elif new_width < target_width:
        white_bg = Image.new('RGB', (target_width, target_height), (255, 255, 255))
        left = (target_width - new_width) // 2
        white_bg.paste(resized_img, (left, 0))
        cropped_img = white_bg
    else:
        cropped_img = resized_img
    
    print(f"   处理后尺寸: {cropped_img.size[0]}x{cropped_img.size[1]} px ✅")
    
    # 保存结果 - 调整质量使文件小于10KB
    # 从较低质量开始尝试，确保文件小于10KB
    best_quality = 85
    for quality in range(85, 0, -5):
        cropped_img.save(output_path, 'JPEG', quality=quality, optimize=True)
        file_size = os.path.getsize(output_path)
        print(f"   质量={quality}, 文件大小={file_size/1024:.2f} KB")
        if file_size < 10 * 1024:
            best_quality = quality
            break
    
    final_size = os.path.getsize(output_path)
    print(f"\n✅ 处理完成!")
    print(f"   输出文件: {output_path}")
    print(f"   最终尺寸: {cropped_img.size[0]}x{cropped_img.size[1]} px")
    print(f"   最终大小: {final_size/1024:.2f} KB")
    print(f"   照片规格: 25mm x 35mm (295px x 413px @ 300dpi)")
    
    return output_path


def select_file():
    """打开文件选择对话框"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    root.attributes('-topmost', True)  # 置顶
    
    file_path = filedialog.askopenfilename(
        title="请选择要处理的照片",
        filetypes=[
            ("图片文件", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("所有文件", "*.*")
        ]
    )
    
    root.destroy()
    return file_path


def main():
    print("=" * 50)
    print("  证件照处理工具 v1.0")
    print("  照片规格: 25mm x 35mm (295px x 413px)")
    print("=" * 50)
    print()
    
    # 判断是否有命令行参数（拖放文件）
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        if os.path.isfile(input_path):
            try:
                # 输出到原文件同目录
                base_dir = os.path.dirname(os.path.abspath(input_path))
                output_path = os.path.join(base_dir, 'output.jpg')
                process_photo(input_path, output_path)
                print(f"\n📁 输出文件位置: {output_path}")
                return
            except Exception as e:
                print(f"❌ 处理失败: {e}")
                input("\n按 Enter 键退出...")
                return
    
    # 没有命令行参数，弹出文件选择对话框
    print("📂 请选择要处理的照片...")
    input_path = select_file()
    
    if not input_path:
        print("❌ 未选择文件")
        input("\n按 Enter 键退出...")
        return
    
    try:
        # 输出到程序所在目录
        if getattr(sys, 'frozen', False):
            # 如果是打包后的 exe
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        
        output_path = os.path.join(base_dir, 'output.jpg')
        process_photo(input_path, output_path)
        print(f"\n📁 输出文件位置: {output_path}")
        
        # 弹出提示框
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            messagebox.showinfo("处理完成", f"✅ 照片处理完成！\n\n输出文件: {output_path}\n尺寸: 295x413 px\n大小: {os.path.getsize(output_path)/1024:.1f} KB")
            root.destroy()
        except:
            pass
            
    except Exception as e:
        print(f"❌ 处理失败: {e}")
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            messagebox.showerror("处理失败", f"❌ 处理失败: {e}")
            root.destroy()
        except:
            pass
    
    input("\n按 Enter 键退出...")


if __name__ == '__main__':
    main()
