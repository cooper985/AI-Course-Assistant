# AI Course Agent Development Log

> 项目开发过程记录


---

# 2026-09-10


## 项目初始化阶段


### 已完成

- Python环境搭建

- PyCharm开发环境配置

- Git初始化

- GitHub仓库建立


### 已学习

- Git基本使用流程

- Python项目结构

- 第三方库管理

- 面向对象基础



---

# PDF文档加载模块


## 完成内容

实现PDF文件读取功能。


技术：

- pdfplumber


实现流程：

PDF文件

↓

读取页面

↓

提取文本



## 学习内容

理解：

- PDF解析基本流程

- 文档处理模块设计

- Python模块化开发方式



## 当前问题

部分PDF可能存在：

- 图片文字无法提取

- 格式复杂导致文本混乱



## 下一步计划

实现文本切分模块（Text Splitter）


---

# 后续记录区域
## 2026.9.11

完成：
- 封装Embedding模块
- 使用BGE-small-zh生成文本向量
- 输出维度512

理解：
- Embedding作用
- self.model和model区别
- 类封装第三方模型的意义



## 2026.9.12
今日完成
1. 完善Document数据结构
   - 增加 metadata 字段，用于保存文档来源、页码等信息。
   - 为后续RAG检索结果溯源做准备。
2. 优化PDF Loader
   - Loader由返回纯文本升级为返回Document对象。
   - 实现PDF页面信息保存。
3. 优化TextSplitter
   - 从字符串切分升级为Document切分。
   - 保证chunk切分后仍保留metadata。
4. 完成Embedding模块
   - 封装 Embedder 类，调用 BAAI/bge-small-zh 模型。
   - 完成文本到向量转换测试。
   - 输出向量维度：512。
5. 完成Pipeline测试
   完成流程验证：
PDF
 ↓
Document
 ↓
Chunk
 ↓
Embedding
 ↓
Vector
测试通过，验证各模块可以正常连接。