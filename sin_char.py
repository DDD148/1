import math, time, os
def draw_sin():
    try:
        x=0
        while True:
            os.system("clear")
            line = ""
            for i in range(60):
                t = x + i*0.1
                val = math.sin(t)
                pos = int((val+1)*15)
                arr = [" "]*30
                arr[pos] = "*"
                line += "".join(arr)+"\n"
            print(line)
            x += 0.1
            time.sleep(0.15)
    except KeyboardInterrupt:
        print("\n退出")
if __name__ == "__main__":
    draw_sin()
