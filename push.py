import subprocess
from datetime import datetime

def run_cmd(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

try:
    print("🔍 检查仓库状态...")
    status = run_cmd(["git", "status", "--porcelain"])
    changes = status.stdout.strip()

    if not changes:
        print("ℹ️ 没有检测到文件改动，无需提交，程序退出")
    else:
        print("📋 检测到改动：")
        print(changes)
        print("\n📤 执行 git add .")
        run_cmd(["git", "add", "."])
        msg = f"自动更新 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        print(f"📝 提交备注：{msg}")
        commit_res = run_cmd(["git", "commit", "-m", msg])
        if commit_res.returncode != 0:
            print("❌ commit失败：", commit_res.stderr)
        else:
            print("🚀 git push ...")
            push_res = run_cmd(["git", "push"])
            print(push_res.stdout)
            if push_res.stderr:
                print(push_res.stderr)
            print("\n✅ 推送完成")

except KeyboardInterrupt:
    print("\n⏹ 手动终止程序")
