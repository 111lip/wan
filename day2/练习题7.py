import os
import re
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox


def natural_sort_key(s):
    """
    自然排序的关键函数，将字符串拆分为数字和非数字部分
    使排序结果更符合人类直觉（例如：1.png < 10.png < 2.png）
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]


def batch_rename_images():
    """按自然顺序批量重命名ZIP中的图片"""
    # 创建GUI选择文件
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 选择ZIP文件
    zip_file_path = filedialog.askopenfilename(
        title="选择包含图片的ZIP文件",
        filetypes=[("ZIP文件", "*.zip")]
    )
    if not zip_file_path:
        messagebox.showinfo("提示", "未选择ZIP文件，程序退出")
        return

    # 选择TXT文件
    txt_file_path = filedialog.askopenfilename(
        title="选择包含新文件名的TXT文件",
        filetypes=[("TXT文件", "*.txt")]
    )
    if not txt_file_path:
        messagebox.showinfo("提示", "未选择TXT文件，程序退出")
        return

    # 选择输出目录
    output_dir = filedialog.askdirectory(
        title="选择输出目录",
        initialdir=os.path.dirname(zip_file_path)
    )
    if not output_dir:
        messagebox.showinfo("提示", "未选择输出目录，程序退出")
        return

    # 读取TXT文件中的新文件名
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            new_names = [line.strip() for line in f if line.strip()]
    except Exception as e:
        messagebox.showerror("错误", f"读取TXT文件失败: {str(e)}")
        return

    # 处理ZIP文件
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # 获取所有PNG文件并按自然顺序排序
            all_files = zip_ref.namelist()
            png_files = [f for f in all_files if f.lower().endswith('.png')]

            # 按自然顺序排序（与Windows资源管理器显示顺序一致）
            png_files.sort(key=lambda x: natural_sort_key(os.path.basename(x)))

            # 验证文件数量匹配
            if len(png_files) != len(new_names):
                messagebox.showerror(
                    "错误",
                    f"文件数量不匹配！\nPNG文件: {len(png_files)}个\n新名称: {len(new_names)}个"
                )
                return

            # 预览映射关系（最多显示前20条）
            preview = []
            for i in range(min(20, len(png_files))):
                original = os.path.basename(png_files[i])
                new_name = f"{new_names[i]}.png"
                preview.append(f"{i + 1}. {original} → {new_name}")

            preview_text = "\n".join(preview)
            if len(png_files) > 20:
                preview_text += f"\n...\n共{len(png_files)}个文件"

            # 确认对话框
            confirm_msg = (
                f"即将按自然顺序重命名 {len(png_files)} 个文件\n\n"
                f"输出目录: {output_dir}\n\n"
                f"前20个文件映射预览:\n{preview_text}\n\n"
                f"是否继续?"
            )

            answer = messagebox.askyesno("确认操作", confirm_msg)
            if not answer:
                return

            # 执行重命名
            for i, (old_name, new_name) in enumerate(zip(png_files, new_names), 1):
                new_file_name = f"{new_name}.png"
                new_path = os.path.join(output_dir, new_file_name)

                with zip_ref.open(old_name) as src, open(new_path, 'wb') as dst:
                    dst.write(src.read())

                print(f"已重命名 ({i}/{len(png_files)}): {os.path.basename(old_name)} → {new_file_name}")

            messagebox.showinfo("成功", f"重命名完成！\n共处理 {len(png_files)} 个文件")
            print(f"\n✅ 所有文件已按自然顺序重命名")

    except Exception as e:
        messagebox.showerror("错误", f"处理过程中出错: {str(e)}")
        print(f"错误: {str(e)}")


if __name__ == "__main__":
    batch_rename_images()