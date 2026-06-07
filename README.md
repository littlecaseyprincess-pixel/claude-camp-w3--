# Claude Camp Week 3

本仓库用于提交第三周的 3 个数据处理项目，练习 CSV 数据分析、JSON 配置文件读写，以及带单元测试的字符串工具库。

## 项目 1：CSV 学员数据分析器

文件：
- `students.csv`
- `csv_student_analyzer.py`
- `report.json`

功能：
- 读取学员 CSV 数据
- 统计总人数
- 统计各国家人数
- 统计对赌完成率
- 将统计结果保存到 `report.json`

运行方式：

```bash
python csv_student_analyzer.py
```

测试方法：
- 运行程序后查看终端输出
- 使用 `cat report.json` 检查统计结果
- 使用 `wc -l csv_student_analyzer.py` 检查代码行数是否不超过 80 行

## 项目 2：JSON 配置文件读写器

文件：
- `config.json`
- `json_config_editor.py`

功能：
- 读取用户配置文件
- 显示当前配置
- 允许用户修改任意一个配置项
- 修改后保存回 `config.json`
- 验证 `font_size` 必须在 8 到 32 之间

运行方式：

```bash
python json_config_editor.py
```

测试方法：
- 修改 `theme`，确认 `config.json` 被更新
- 修改 `font_size` 为合法值，例如 `20`
- 输入非法字体大小，例如 `40`，确认程序提示错误
- 输入非数字字体大小，例如 `abc`，确认程序不会崩溃
- 使用 `wc -l json_config_editor.py` 检查代码行数是否不超过 80 行

## 项目 3：带单元测试的字符串工具库

文件：
- `string_utils.py`
- `test_string_utils.py`

功能：
- `reverse_words(s)`：反转单词顺序
- `count_vowels(s)`：统计元音字母数量
- `is_palindrome(s)`：判断字符串是否回文

运行测试：

```bash
pytest
```

如果没有激活虚拟环境，先运行：

```bash
source .venv/bin/activate
```

测试方法：
- 每个函数至少 3 个测试用例
- 包含正常情况、边界情况和异常/特殊情况
- 运行 `pytest`，确认所有测试通过
- 使用 `wc -l string_utils.py test_string_utils.py` 检查代码行数是否不超过 80 行

## 学习重点

通过本周项目，我练习了：

- CSV 文件读取与数据分析
- Pandas 基础使用
- JSON 文件读写
- 命令行交互
- 数据验证
- 函数拆分
- pytest 单元测试
- Git 分支开发流程