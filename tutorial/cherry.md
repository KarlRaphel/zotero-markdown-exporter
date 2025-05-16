# 🍒 在 CherryStudio 中使用文献知识库教程

CherryStudio 是一个强大的本地化 AI 助手，支持对话、知识检索与本地模型部署。通过将 Zotero 导出的文献 Markdown 文件导入 CherryStudio，你可以轻松实现基于文献内容的语义检索和问答。

---

## 📥 第一步：安装 CherryStudio

前往 [CherryStudio 官网](https://www.cherry-ai.com/) 下载并安装适合你系统的 CherryStudio 客户端。

> 📝 参考官方文档：[CherryStudio 安装](https://docs.cherry-ai.com/pre-basic/installation)

- 支持：Windows / macOS
- 安装完成后启动应用。

---

## 🔑 第二步：配置 API Key 和模型

CherryStudio 支持多种大模型和嵌入模型。以下是推荐的配置方式：

### 1. 配置对话模型 API（LLM）

参考教程

你可以在以下两个平台免费获取 API Key：

- **硅基流动 SiliconFlow**：支持主流开源模型，调用方式简单
  👉 [硅基流动官网](https://cloud.siliconflow.cn/)
  > 📝 参考官方文档：[硅基流动](https://docs.cherry-ai.com/pre-basic/providers/siliconcloud)

- **魔搭 ModelScope**：阿里云推出的模型开放平台
  👉 [ModelScope 官网](https://modelscope.cn/)
  > 📝 参考官方文档：[ModelScope](https://modelscope.cn/docs/model-service/API-Inference/intro)

在 CherryStudio 设置中找到 **"Providers" > "LLM"**，选择 “OpenAI Compatible” 或 “ModelScope”，并填写你的 API Key 。

### 2. 配置嵌入模型（推荐使用 `bge-m3`）

嵌入模型用于将知识库内容向量化，以便进行语义检索。推荐使用 `bge-m3` 模型：

#### ✅ 方式一：使用硅基流动 API（推荐新手）

1. 注册硅基流动账号；
2. 在 [模型页面](https://cloud.siliconflow.cn/model-store/text-embeddings) 找到 `bge-m3`；
3. 获取 API Key；
4. 在 CherryStudio 设置中为硅基流动添加模型。

#### 💻 方式二：本地部署（推荐进阶用户）

使用 Ollama 本地部署 `bge-m3` 模型：

1. 安装 [Ollama](https://ollama.ai)；
2. 运行命令下载模型（可能需要代理）：
   ```bash
   ollama pull bge-m3
   ```
3. 在 CherryStudio 设置中配置 Embedding 模型为本地服务：
   - Provider: `Ollama`
   - Host: `http://localhost:11434`
   - Model: `bge-m3`

> ✅ 嵌入模型对算力要求不高，本地部署即可满足大部分需求。

---

## 📁 第三步：导入文献知识库

> 📝 参考官方文档：[CherryStudio 知识库使用指南](https://docs.cherry-ai.com/knowledge-base/knowledge-base)

将 Zotero 导出的 Markdown 文件添加到 CherryStudio 的知识库中：

### ✅ 正确做法：仅导入 `papers` 子目录

不要将 Zotero 导出的整个根目录导入，只导入其中的 **`papers/` 文件夹**，原因如下：

- 该文件夹包含每篇文献的 Markdown 文件，结构清晰；
- 避免导入作者、标签等元信息文件，可提升向量化效率和检索准确性。

#### 操作步骤：

1. 打开 CherryStudio；
2. 点击左侧边栏的 **"Knowledge"** 标签；
3. 点击 **"Add Knowledge Base"**；
4. 选择 **"Add Folder"**，选中你的 `papers/` 文件夹；
5. 设置合适的 Embedding 模型；
6. 点击 **"Start Embedding"**，等待完成。

---

## 💬 第四步：使用知识库与大模型对话

现在你可以开始利用知识库进行语义检索和问答：

1. 打开 CherryStudio 的 **Chat** 页面；
2. 在输入框中提问，例如：
   ```
   如何理解神经架构搜索（NAS）的基本原理？
   ```
3. 系统会自动从知识库中检索相关文献内容，结合大模型生成回答。

> 🧠 提示：你可以在提问中指定使用某篇文献中的信息，例如：
>
> ```
> 根据 [[A Survey of the Recent Architectures of Deep Convolutional Neural Networks]]，解释 CNN 的演变过程。
> ```

---

## 🛠️ 小技巧：提升使用体验

- **定期更新知识库**：Zotero 导出更新后，可重新导入 `papers/` 文件夹；
- **结合 Obsidian 使用**：你可以在 Obsidian 中整理笔记，并将关键段落导出为 Markdown 导入 CherryStudio；
- **使用提示模板**：为常见查询任务设计模板，提升效率；
- **切换不同模型**：根据任务需求在对话模型（如 Qwen、Llama3）和嵌入模型之间灵活切换。

---

## 🎉 完成！

现在你已经成功将 Zotero 文献导入 CherryStudio，并可以结合大语言模型进行语义检索、问答和知识探索。
