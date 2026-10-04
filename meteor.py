import time
import random

def star_rain():
    width = 60
    try:
        while True:
            x = random.randint(0, width - 1)
            line = [" "] * width
            line[x] = "✨"
            print("".join(line))
            time.sleep(0.08)
    except KeyboardInterrupt:
        print("\n🌙 流星雨结束，程序退出")

if __name__ == "__main__":
    print("🌌 Termux 流星雨，按 Ctrl+C 退出")
    star_rain()
