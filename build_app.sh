#!/data/data/com.termux/files/usr/bin/bash
# 编译C++，生成app，保留文件，不自动删除
if [ $# -ne 1 ];then
    echo "用法： ./build_app.sh 代码.cpp"
    echo "简写别名：brx test.cpp"
    exit 1
fi
SRC="$1"
OUT="app"
if [ ! -f "$SRC" ];then
    echo "❌ 源码文件 $SRC 不存在"
    exit 1
fi
echo "🔨 clang++ 编译 $SRC  --> app"
clang++ "$SRC" -o "$OUT"
if [ $? -eq 0 ];then
    echo "✅ 编译完成！产物：app（已保留，不会删除）"
    echo "▶ 开始运行程序："
    echo "----------------------------------------"
    ./$OUT
    echo "----------------------------------------"
    echo "🏁 程序运行结束，app文件留在当前目录，可以上传Release"
else
    echo "❌ 编译出错，请检查C++代码"
fi
