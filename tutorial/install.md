# 🧾 安装与导出教程

本教程将指导你如何配置环境并使用脚本从 Zotero 中导出文献为 Markdown 格式，方便后续在 Obsidian、CherryStudio 等工具中使用。

---

## ⏬ 0. 克隆项目

找一个你想保存本项目的文件夹，在终端中进入文件夹后执行以下命令

```bash
git clone https://github.com/KarlRaphel/zotero-markdown-exporter.git
cd zotero-markdown-exporter
```

## 🛠️ 1. 安装 Python

本工具基于 Python 编写，你必须首先安装 Python。推荐使用以下任一方式管理环境（直接使用原始环境也行）：

- **venv（标准）**
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  ```

- **conda（科学计算推荐）**
  ```bash
  conda create -n zotero-md python=3.12
  conda activate zotero-md
  ```

- **uv（推荐新工具）**
  ```bash
  uv venv
  source .venv/bin/activate
  ```

---

## 📦 2. 安装依赖包

```bash
pip install python-dotenv pyzotero
```

如果你需要使用 LLM 进行总结，你还需要额外安装以下依赖

```bash
pip install pypdf
```

---

## 📄 3. 配置环境变量

复制 `.env.example` 为 `.env` 并修改对应字段：

```bash
cp .env.example .env
```

打开 `.env`，修改如下字段：

```env
OUTPUT_DIR=你想保存导出文献的目录
```

如果需要使用 LLM 进行总结，你需要修改 `.env` 中以下字段：

```env
# 设置为true以启用LLM功能
USE_LLM=true

LLM_API_URL=https://api-inference.modelscope.cn/v1/chat/completions
LLM_API_KEY=abcdef123456
LLM_MODEL=Qwen/Qwen3-32B

# 总结的语言，目前支持中文（zh）和英语（en）
LLM_LANG=en

# Zotero数据库的存储目录
# pdf文件将从 “存储目录/论文ID/xxx.pdf” 中读取
ZOTERO_STORAGE_DIR=/Users/pht/Zotero/storage
```

<details>

<summary>点击展开注意事项</summary>

1. 读取一篇论文需要消耗大量的 Token，请关注你的用量消耗。
2. 一篇论文通常较长，请确保你使用的模型能够处理。默认使用的上下文长度为32k，如果你使用ollama等本地工具请进行配置。

</details>

### 🔧 OUTPUT_DIR 示例结构

导出后会生成如下目录结构（自动创建）：

```
OUTPUT_DIR/
├── tags/         # 按标签组织文献
├── journals/     # 按期刊组织文献
├── authors/      # 按作者组织文献
├── papers/       # 所有文献的 Markdown 文件
├── collections/  # 按 Zotero 收藏夹组织文献
└── series/       # 每个文件包含收藏夹下所有论文的详情内容，可以在与大模型对话时直接使用单个文件替代知识库
```

---

## 🖥️ 3.1 本地导出（推荐）

在 Zotero 中启用本地访问权限：

1. 打开 Zotero > **编辑** > **首选项**（或 macOS 上的 **Zotero > 设置**）
2. 进入 **高级** > **杂项**
3. 勾选：**允许此计算机上的其他应用程序与 Zotero 通信**

> ✅ 无需修改 `.env` 中的 `ZOTERO_API_KEY` 或 `ZOTERO_LIBRARY_ID`，默认使用本地数据库。

---

## 🌐 3.2 在线导出（可选折叠）

<details>
<summary>点击展开在线导出配置说明</summary>

如果你已经启用了 Zotero 的在线同步功能，可以通过 API 方式导出数据。

1. 登录 [Zotero 官网](https://www.zotero.org)
2. 进入 [API Key 页面](https://www.zotero.org/settings/security)
3. 创建一个新的 API Key

修改 `.env` 文件如下：

```env
ZOTERO_LOCAL=false
ZOTERO_LIBRARY_TYPE=user
ZOTERO_LIBRARY_ID=你的用户ID
ZOTERO_API_KEY=生成的API密钥
```

</details>

---

## ▶️ 4. 运行导出脚本

确保当前工作目录包含 `.env` 和 `main.py`，然后运行脚本：

```bash
python main.py
```

> 🕒 脚本会依次：
>
> 1. 创建目标输出目录；
> 2. 获取 Zotero 中所有收藏夹；
> 3. 遍历所有文献条目；
> 4. 导出 Markdown 格式并建立双向链接。

---

## 📁 示例输出文件内容（papers/xxx.md）

```markdown
# A Survey of the Recent Architectures of Deep Convolutional Neural Networks

**Authors:** [[Sina Alemohammad]], [[Bohan Zhai]]

**Journal:** [[Computer Science Review]]

**Zotero:** [Open](zotero://open-pdf/library/items/123456)

**Collections:** [[Deep Learning]], [[Survey]]

**Year:** 2022 | **Volume:** 40 | **Pages:** 100378

**DOI:** [10.1016/j.cosrev.2022.100378](https://doi.org/10.1016/j.cosrev.2022.100378)

**Tags:** [[CNN]], [[Neural Network]]

**Abstract:**

This paper provides a comprehensive overview of recent developments in deep convolutional neural networks, focusing on their architectures and applications ...
```

---

## 🙌 完成！现在你可以将导出的 Markdown 文件导入 Obsidian、CherryStudio 等知识管理工具，构建属于你自己的文献知识图谱。
