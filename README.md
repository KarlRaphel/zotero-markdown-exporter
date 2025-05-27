# Zotero 文献 Markdown 导出器

> 📘 将 Zotero 中的文献一键导出为 Markdown 格式，构建你的个人知识图谱。

这个工具可以帮助你从 Zotero 中提取文献的核心信息（如标题、作者、摘要等），支持使用LLM进行论文精度和总结，并以 Markdown 格式导出。通过结构化的文件格式与双向链接机制，你可以轻松在 Obsidian 等笔记工具中建立知识图谱，快速构建基于文献的知识库。通过 NotebookLM 或 CherryStudio 等工具，高效根据自己的Zotero文献库进行对话。

---

## 🌟 功能亮点

### 🔗 双向链接，轻松关联文献

![双向链接](https://raw.githubusercontent.com/KarlRaphel/doc-attachments/main/img/bidirectional-links.gif)
支持在 Obsidian 中创建**双向链接**，实现文献间的相互跳转与关联阅读。

### 🧠 知识图谱，可视化关联

![知识图谱](https://raw.githubusercontent.com/KarlRaphel/doc-attachments/main/img/knowledge-graph.gif)
基于导出的 Markdown 文件，可在 Obsidian 中生成**知识图谱**，直观展示文献之间的关系。

### 🤖 论文精读，智能总结

![智能总结](https://raw.githubusercontent.com/KarlRaphel/doc-attachments/main/img/summarize-paper.png)

### 🔍 智能解释，辅助理解概念

![概念解释](https://raw.githubusercontent.com/KarlRaphel/doc-attachments/main/img/explain-concept.gif)
结合嵌入模型和语义搜索，大模型可根据相关论文，**智能解释复杂概念**。

### 📚 自动引用，高效写作

![参考文献](https://raw.githubusercontent.com/KarlRaphel/doc-attachments/main/img/add-references.gif)
借助语义匹配能力，自动为你的观点推荐**支撑文献**，提升写作效率与学术严谨性。

---

## ✅ 核心优势

1. **语义检索优于关键词匹配**
   相较于 Zotero 的关键词搜索，本工具结合向量模型，支持**语义层面的相似性检索**。

2. **轻量化导出，提升效率**
   仅导出文献关键信息（标题、作者、摘要等），避免全文嵌入，显著加快在 CherryStudio 等 LLM 客户端中的知识库构建速度。

3. **双向链接与知识图谱支持**
   支持在 Obsidian 中创建**双向链接与知识图谱**，便于构建个性化的文献管理系统。

---

## 🔧 主要功能

- 📝 导出文献关键字段（标题、作者、年份、摘要等）
- 🔗 支持 Zotero 链接跳转，一键打开文献
- 🔁 基于`文献集合（collections）`、`标签（tags）`、`作者（authors）`和`期刊（journals）`建立**双向链接**
- 📂 Markdown 文件统一管理，适配 CherryStudio 等 LLM 客户端的知识库构建流程

---

## 📖 教程文档

- [🔧 安装并导出文献](tutorial/install.md)
- [📚 在 AI 对话中简单使用](tutorial/simple_use.md)
- [📁 在 Obsidian 中导入文献](tutorial/obsidian.md)
- [🤖 在 CherryStudio 中导入文献](tutorial/cherry.md)

---

## 💡 其他推荐项目

- [elsevier-tracker-web](https://github.com/KarlRaphel/elsevier-tracker-web) — 一个无需客户端的审稿进度追踪工具
- [BearLLM](https://github.com/SIA-IDE/BearLLM) — 基于 LLM 的轴承健康管理统一框架

---

## ❤️ 支持我

如果您喜欢这个项目，欢迎通过以下方式支持我继续开发与维护：

![捐赠二维码](https://raw.githubusercontent.com/KarlRaphel/elsevier-tracker-web/main/public/donation_qr_code.jpg)

---

## 🤝 贡献指南

欢迎提交 PR、issue 或文档改进建议，共同完善 Zotero 与大模型结合的知识管理生态。

---

## 📝 许可证

本项目采用 MIT License。
