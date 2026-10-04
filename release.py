import subprocess
import os

def run_cmd(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

try:
    print("==== GitHub Release 发布工具（多文件版） ====")
    tag = input("输入版本标签(例 v1.0.0) > ").strip()
    files_input = input("待上传文件，多个用空格分隔(例 app.apk app.exe) > ").strip()
    file_list = files_input.split()

    # 校验所有文件是否存在
    for f in file_list:
        if not os.path.exists(f):
            print(f"❌ 文件 {f} 不存在！")
            exit()

    title = input("Release标题 > ").strip()
    note = input("更新说明 > ").strip()

    cmd = [
        "gh", "release", "create",
        tag,
        *file_list,
        "--title", title,
        "--notes", note
    ]
    print("\n🚀 正在创建Release并上传文件...")
    res = run_cmd(cmd)
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("\n✅ Release 创建&上传成功！")
    else:
        print("\n❌ 发布失败")

except KeyboardInterrupt:
    print("\n⏹ 取消操作")
