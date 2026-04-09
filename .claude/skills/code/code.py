#!/usr/bin/env python3
"""
代码辅助 Skill - 提供 Python 代码格式化、检查和统计功能
"""

import os
import sys
import ast
import subprocess
from pathlib import Path


def find_python_files(path="."):
    """查找所有 Python 文件"""
    path = Path(path)
    if path.is_file() and path.suffix == '.py':
        return [path]
    elif path.is_dir():
        return list(path.rglob("*.py"))
    return []


def format_code(path):
    """使用 black 格式化代码"""
    files = find_python_files(path)
    if not files:
        print(f"在 {path} 中未找到 Python 文件")
        return

    for file in files:
        try:
            # 使用 black 格式化
            result = subprocess.run(
                ["black", "-q", str(file)],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0:
                print(f"✓ 已格式化: {file}")
            elif result.returncode == 123:
                # black 未安装或出错
                print(f"⚠ 格式化 {file} 失败: black 未安装")
                print("  尝试运行: pip install black")
                break
            else:
                print(f"⚠ 格式化 {file} 时出错")
        except FileNotFoundError:
            print("⚠ 未找到 black，请先安装: pip install black")
            break


def check_syntax(path):
    """检查代码语法"""
    files = find_python_files(path)
    if not files:
        print(f"在 {path} 中未找到 Python 文件")
        return

    error_count = 0
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                source = f.read()
            ast.parse(source)
            print(f"✓ {file} - 语法正确")
        except SyntaxError as e:
            error_count += 1
            print(f"✗ {file} - 语法错误 (第{e.lineno}行): {e.msg}")
        except Exception as e:
            error_count += 1
            print(f"✗ {file} - 读取错误: {e}")

    if error_count == 0:
        print(f"\n✓ 所有 {len(files)} 个文件语法检查通过！")
    else:
        print(f"\n✗ 发现 {error_count} 个文件有语法错误")


def stats(path):
    """统计代码信息"""
    files = find_python_files(path)
    if not files:
        print(f"在 {path} 中未找到 Python 文件")
        return

    total_lines = 0
    total_code_lines = 0
    total_functions = 0
    total_classes = 0

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            code_lines = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
            total_lines += len(lines)
            total_code_lines += code_lines

            # 解析 AST 统计函数和类
            with open(file, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    total_functions += 1
                elif isinstance(node, ast.ClassDef):
                    total_classes += 1

        except Exception as e:
            print(f"⚠ 无法解析 {file}: {e}")

    print(f"\n📊 代码统计 ({path})")
    print("=" * 40)
    print(f"Python 文件数: {len(files)}")
    print(f"总行数: {total_lines}")
    print(f"代码行数 (不含空行和注释): {total_code_lines}")
    print(f"函数数量: {total_functions}")
    print(f"类数量: {total_classes}")
    if len(files) > 0:
        print(f"平均每文件行数: {total_lines // len(files)}")


def list_files(path="."):
    """列出 Python 文件"""
    files = find_python_files(path)
    if not files:
        print(f"在 {path} 中未找到 Python 文件")
        return

    print(f"\n📁 Python 文件列表 ({len(files)} 个):")
    print("=" * 40)

    # 按目录分组
    by_dir = {}
    for f in sorted(files):
        dir_name = str(f.parent)
        if dir_name not in by_dir:
            by_dir[dir_name] = []
        by_dir[dir_name].append(f.name)

    for dir_name, filenames in sorted(by_dir.items()):
        print(f"\n{dir_name}/")
        for name in filenames:
            print(f"  - {name}")


def main():
    if len(sys.argv) < 2:
        print("用法: code.py <command> [args...]")
        print("\n可用命令:")
        print("  format [path]  - 格式化代码")
        print("  check [path]   - 检查语法")
        print("  stats [path]   - 统计代码信息")
        print("  list [path]    - 列出 Python 文件")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "."

    if command == "format":
        format_code(path)
    elif command == "check":
        check_syntax(path)
    elif command == "stats":
        stats(path)
    elif command == "list":
        list_files(path)
    else:
        print(f"未知命令: {command}")
        print("可用命令: format, check, stats, list")
        sys.exit(1)


if __name__ == "__main__":
    main()
