#!/data/data/com.termux/files/usr/bin/bash
if [ $# -ne 1 ];then
    echo "用法：br 文件名.cpp"
    exit 1
fi
SRC="$1"
OUT="app"
if [ ! -f "$SRC" ];then
    echo "❌ 文件 $SRC 不存在"
    exit 1
fi
echo "🔨 编译 $SRC"
clang++ "$SRC" -o "$OUT"
if [ $? -eq 0 ];then
    echo "✅ 编译成功，运行程序："
    echo "----------------------------------------"
    ./$OUT
    echo "----------------------------------------"
    rm $OUT
    echo "🏁 结束"
else
    echo "❌ 编译失败"
fi
