# 📸 证件照处理工具

将任意照片一键处理为 **25mm × 35mm (295px × 413px)** 的标准证件照规格，输出 JPEG 格式，文件大小控制在 **10KB 以内**。
<img width="1379" height="942" alt="image" src="https://github.com/user-attachments/assets/13678cc5-39e2-4f9d-ae49-5dd7d944607a" />


## ✨ 功能特点

- ✅ 自动缩放并居中裁剪到标准证件照尺寸
- ✅ 自动调整图片质量，确保输出文件小于 10KB
- ✅ 支持拖放图片到程序图标上直接处理
- ✅ 支持多种输入格式：JPG、JPEG、PNG、BMP、TIFF
- ✅ **无需安装 Python，下载即用**

## 📥 下载使用

### 方式一：直接下载可执行文件（推荐）

从 [Releases](https://github.com/xuxiran/under10KB/releases) 页面下载最新版本的 `ID_Photo_Tool.exe`，双击运行即可。

**使用方法：**
1. **直接运行**：双击 exe → 弹出文件选择窗口 → 选择照片 → 自动处理
2. **拖放处理**：将照片文件直接拖到 exe 图标上 → 自动处理

处理完成后，会在 **exe 所在目录** 生成 `output.jpg` 文件。

### 方式二：自行打包

如果你有 Python 环境，也可以下载源码自行打包：

```bash
# 1. 克隆仓库
git clone https://github.com/xuxiran/under10KB.git
cd under10KB

# 2. 创建虚拟环境（推荐）
python -m venv ps_jpg
ps_jpg\Scripts\pip install -r requirements.txt

# 3. 打包为 exe
ps_jpg\Scripts\pyinstaller --onefile --name "ID_Photo_Tool" --windowed process_photo.py

# 4. 在 dist 目录中找到 exe 文件
```

或者在 Windows 上直接双击 `build_windows.bat` 自动完成虚拟环境创建和打包。

## 📋 输出规格

| 项目 | 规格 |
|------|------|
| 照片尺寸 | 25mm × 35mm |
| 像素尺寸 | 295px × 413px |
| 分辨率 | 300 DPI |
| 文件格式 | JPEG |
| 文件大小 | ≤ 10KB |

## 📄 许可证

MIT License
