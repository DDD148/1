#include <iostream>
#include <cstdlib>
#include <string>
#include <ctime>
using namespace std;

int main()
{
    time_t now = time(nullptr);
    string default_msg = "C++自动提交 " + string(ctime(&now));
    string commit_msg;

    cout << "📝 输入提交备注（直接回车使用默认）：\n> ";
    getline(cin, commit_msg);

    if (commit_msg.empty())
    {
        commit_msg = default_msg;
    }

    cout << "\n🔍 git status\n";
    system("git status");

    cout << "\n📤 git add .\n";
    system("git add .");

    string cmd = "git commit -m \"" + commit_msg + "\"";
    cout << "\n📝 " << cmd << "\n";
    int ret = system(cmd.c_str());

    if (ret != 0)
    {
        cout << "\nℹ️ 没有检测到改动，终止推送\n";
        return 0;
    }

    cout << "\n🚀 git push\n";
    system("git push");
    cout << "\n✅ 推送完毕\n";
    return 0;
}
