# 🪨 使用 Obsidian 教程

Obsidian 是一个基于 Markdown 的强大知识管理工具，支持双向链接和知识图谱功能。通过本项目导出的 Markdown 文献数据，你可以轻松在 Obsidian 中构建文献知识库，并探索它们之间的关联。

---

## 📥 第一步：下载并安装 Obsidian

前往 [Obsidian 官网](https://obsidian.md/) 下载并安装适合你系统的 Obsidian 客户端。

- 支持：Windows / macOS / Linux
- 安装完成后打开软件，你会看到一个简洁的界面。

---

## 📁 第二步：打开导出目录作为 Obsidian 仓库

1. 启动 Obsidian；
2. 点击 **"Open another vault"**（或在启动时选择）；
3. 选择你之前配置的 `OUTPUT_DIR` 路径（即导出的根目录）；
4. Obsidian 会加载该目录下的所有 Markdown 文件。

> ✅ 此目录结构如下：
>
> ```
> OUTPUT_DIR/
> ├── tags/
> ├── journals/
> ├── authors/
> ├── papers/
> └── collections/
> ```

---

## 🔍 第三步：探索你的文献知识库

### 📚 阅读文献笔记

- 打开左侧文件树，进入 `papers/` 文件夹，查看导出的文献笔记；
- 每个文献包含标题、作者、期刊、年份、摘要等信息，并自动关联到对应标签、作者、收藏夹等。

### 🔗 添加双向链接

你可以通过以下方式在笔记中引用这些文献：

```markdown
[[A Survey of the Recent Architectures of Deep Convolutional Neural Networks]]
```

Obsidian 会自动建立双向链接，方便你从笔记跳转到文献，或从文献跳转到笔记。

### 🌐 查看知识图谱

1. 点击左侧最上方的 **关系图谱图标**（两个节点连接的图形）；
2. 你可以看到文献与标签、作者、收藏夹之间的关系网络；
3. 可以点击节点查看关联内容，直观理解文献之间的联系。

---

## 🧩 小技巧：增强你的使用体验

### ✨ 启用社区插件（可选）

你可以安装一些社区插件来增强功能：

- **Knowledge Graph Viewer**：增强型知识图谱展示
- **Templater** 或 **Quick Add**：快速插入文献引用模板
- **Graph Analysis**：分析知识图谱中的节点关系
- **Dataview**：以表格、列表等方式浏览文献元信息

### 🗂️ 自定义笔记结构

你可以创建如下的笔记分类结构：

```
notes/
  └── research/
      ├── computer_vision/
      └── nlp/
```

并在这些笔记中引用文献，如：

```markdown
## CNN 架构综述

参考了这篇综述论文：[[A Survey of the Recent Architectures of Deep Convolutional Neural Networks]]
```

---

## 🎉 完成！

现在你已经成功将 Zotero 中的文献导入 Obsidian，并可以通过双向链接与知识图谱功能构建属于你自己的学术知识体系。
