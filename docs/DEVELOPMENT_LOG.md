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

---

## 2026-09-17：项目审阅与规划更新

### 记录性质

本条记录文档调整和静态审阅，不代表本次新增代码或运行验证；上方历史记录原样保留。过去记录中的“下一步”仅表示当时计划。

### 已确认的代码进展

基线：[8a4f93b](https://github.com/cooper985/AI-Course-Assistant/tree/8a4f93b2e10d8fb0b2f14644492b9933bee78480)。

- 已有 NumPy 内存向量存储与余弦相似度搜索，检索返回 Document。
- 当前 pipeline 脚本连接至 Embedding；向量检索示例使用手工向量。
- 尚未发现完整 RAG 回答、LangGraph、FastAPI 和 Vue 实现。

### 文档调整

- 更新 PROJECT_CONTEXT：保留原核心目标，明确 LangGraph 学习规划、范围与服务器验收。
- 新增 ROADMAP：12 周核心开发和 4 周缓冲，包含首周每日任务。
- 完善 EXPERIMENT_RECORD：定义对照、变量、指标及结果模板；实验均待运行。
- 新增 WEEKLY_REVIEW 和文档导航，建立后续记录入口。

### 待处理问题

切分参数校验；PDF 失败与空数据处理；Top-K、分数与向量校验；稳定块 ID；可复现测试资料和真实查询评测。

### 下一步

按 [路线图](ROADMAP.md) 完成基础检索闭环，先建立 baseline，再接入 LLM 和 LangGraph。

### 后续开发记录模板

- 日期与任务：
- 模块用途、架构位置及与 RAG／Agent 的关系：
- 实际完成与关联提交：
- 关键设计原因：
- 验证方法、运行结果及失败项：
- 是否需要效果实验，关联实验 ID：
- 学到的原理：
- 尚未解决的问题与下一步：
- Git 提交与文档同步情况：

