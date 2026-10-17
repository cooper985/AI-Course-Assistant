# AI Course Assistant

当前流程：PDF → 文本切分 → Embedding → Top-K 检索。

使用 Python 3.11，在项目根目录创建并激活虚拟环境后安装依赖：

macOS：

```sh
python3.11 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell：

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

```sh
python -m pip install -r requirements.txt
```

将 PDF 放到 `data/` 下，可以放在子目录中；加载器会递归读取文件，支持 `.pdf` 和 `.PDF`。单文件示例自动选择按路径排序后的第一个 PDF，不要求存在名为 `test.pdf` 的文件。

VS Code 项目设置默认使用 `.venv`，Code Runner 跟随 Python 扩展选中的解释器。如果此前选过其他环境，通过“Python: Select Interpreter”切换到项目的 `.venv`。

```sh
python tests/test_loader.py
python tests/test_multi_loader.py
python tests/test_pipeline.py
python tests/test_retriever.py
python tests/test_rag_pipeline.py
python -m unittest tests.test_document_loader -v
```

脚本按自身位置定位项目和数据，从其他目录运行时请传入脚本的完整路径。单 PDF 读取失败会直接抛出原始异常；没有数据或没有可提取文字时，示例脚本会明确报错。

模型为 `BAAI/bge-small-zh`，首次编码需要下载模型，之后可使用本地缓存。检索脚本输出相似度、文本、文件来源和 PDF 页码；当前尚未接入生成回答。
