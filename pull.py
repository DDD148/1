import subprocess

def run_cmd(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

try:
    print("🔍 检查本地仓库状态...")
    status = run_cmd(["git", "status", "--porcelain"])
    changes = status.stdout.strip()

    if changes:
        print("⚠️ 警告：本地还有未提交的改动！")
        print(changes)
        inp = input("是否继续拉取远程更新？(y/n)：")
        if inp.lower() != "y":
            print("⏹ 已取消拉取")
            exit()
    else:
        print("✅ 本地无未提交文件，准备拉取远程更新")

    print("\n🔄 正在执行 git pull ...")
    res = run_cmd(["git", "pull"], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print(res.stderr)

    if res.returncode == 0:
        print("\n✅ 拉取成功，本地已经同步远程最新版本")
    else:
        print("\n❌ 拉取失败，大概率发生代码冲突，手动处理文件！")

except KeyboardInterrupt:
    print("\n⏹ 手动终止程序")
