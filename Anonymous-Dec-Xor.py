import os
import time
from colorama import Fore, init
import sys
import webbrowser

# Colorama ইনিশিয়ালাইজ
init(autoreset=True)

# ASCII টেক্সট ব্যানার প্রদর্শন
def print_banner():
    print(Fore.CYAN + """
┏━━━┓────────────┏┓─┏┓────────────┏━━━┓
┃┏━┓┃────────────┃┃─┃┃────────────┃┏━┓┃
┃┃─┃┃┏━━┓┏━━┓┏━━┓┃┗━┛┃┏┓┏┓┏━━┓┏┓┏┓┃┗━━┓
┃┗━┛┃┃┏┓┃┃┏┓┃┃┏┓┃┗━┓┏┛┃┗┛┃┃┏┓┃┃┃┃┃┗━━┓┃
┃┏━┓┃┃┃┃┃┃┗┛┃┃┃┃┃┏━┛┃─┃┃┃┃┃┗┛┃┃┗┛┃┃┗━┛┃
┗┛━┗┛┗┛┗┛┗━━┛┗┛┗┛┗━━┛─┗┻┻┛┗━━┛┗━━┛┗━━━┛
┏━┓┏━┓────┏━━━┓
┗┓┗┛┏┛────┃┏━┓┃
─┗┓┏┛─┏━━┓┃┗━┛┃
─┏┛┗┓─┃┏┓┃┃┏┓┏┛
┏┛┏┓┗┓┃┗┛┃┃┃┃┗┓
┗━┛┗━┛┗━━┛┗┛┗━┛
┏━━━┓┏━━━┓┏━━━┓┏━━━┓┏┓──┏┓┏━━━┓┏━━━━┓
┗┓┏┓┃┃┏━━┛┃┏━┓┃┃┏━┓┃┃┗┓┏┛┃┃┏━┓┃┃┏┓┏┓┃
─┃┃┃┃┃┗━━┓┃┃─┗┛┃┗━┛┃┗┓┗┛┏┛┃┗━┛┃┗┛┃┃┗┛
─┃┃┃┃┃┏━━┛┃┃─┏┓┃┏┓┏┛─┗┓┏┛─┃┏━━┛──┃┃──
┏┛┗┛┃┃┗━━┓┃┗━┛┃┃┃┃┗┓──┃┃──┃┃─────┃┃──
┗━━━┛┗━━━┛┗━━━┛┗┛┗━┛──┗┛──┗┛─────┗┛──    """)
    print()  # নতুন লাইন

# XOR ডিক্রিপশন ফাংশন
def xor_decrypt(file_path, key, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        # XOR ডিক্রিপশন
        decrypted_data = bytes([b ^ (key % 256) for b in data])

        # ডিক্রিপ্টেড ফাইল আউটপুটে লিখুন
        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        # সফল ডিক্রিপশন মেসেজ দুই লাইনে
        print()
        print()  # নতুন লাইন
        print(Fore.GREEN + f"Ꭰ𝙴𝙲𝚁𝚈𝙿𝚃𝙴𝙳 Ꮪ𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 🥳")
        print()
        print(Fore.GREEN + f"💾 Ꮪ𝙰𝚅𝙴 Ꭲ𝙾:→{output_path}")
        print()  # নতুন লাইন

    except Exception as e:
        print(Fore.RED + f"ᎳᎢᎰ Ꭺ ᎬᏒᏒᏫᏒ ❗: {e}")
        print()  # নতুন লাইন

# ইউজার থেকে XOR কী ইনপুট নিন
def get_key():
    while True:
        try:
            print(Fore.YELLOW + "🔑 Ꭼ𝙽𝚃𝙴𝚁 𐒎ᏫᏒ Ꮶ𝙴𝚈 : ", end="")  # নতুন লাইনে প্রম্পট দেখান
            key = input().strip()  # ইনপুট নেওয়া
            if key.lower() == 'q':  # 'q' প্রেস করলে প্রোগ্রাম বন্ধ
                print(Fore.RED + "Ꮪ𝙲𝚁𝙸𝙿𝚃 Ꮯ𝙻𝙾𝚂𝙸𝙽𝙶...")
                exit()  # প্রোগ্রাম বন্ধ
            else:
                return int(key)  # কী রিটার্ন করুন
        except ValueError:
            print(Fore.RED + "Ꭾ𝙻𝚉 Ꭼ𝙽𝚃𝙴𝚁 Ꭺ Ꮩ𝙰𝙻𝙸𝙳 Ꮶ𝙴𝚈 ❗")
            print()  # নতুন লাইন

# ফাইল পাথ ইনপুট নিন এবং চেক করুন
def get_file_path():
    default_path = '/storage/emulated/0/MT2/apks/'  # ডিফল্ট পাথ
    while True:
        # ইউজারের জন্য পাথের প্রম্পট দেখানো
        print(Fore.YELLOW + f"📂 Ꭼ𝙽𝚃𝙴𝚁 Ꭹ𝙾𝚄𝚁 Ꭾ𝙰𝚃𝙷: ", end="")  
        file_path = input().strip()  # ইনপুট নেওয়া
        print()  # নতুন লাইন
        
        if file_path.lower() == "q":  # ইউজার যদি 'q' টাইপ করে
            print(Fore.RED + "Ꮪ𝙲𝚁𝙸𝙿𝚃 Ꮯ𝙻𝙾𝚂𝙸𝙽𝙶...")
            exit()  # প্রোগ্রাম বন্ধ
        
        # যদি ইউজার পাথ না দেন, ডিফল্ট পাথ সেট করুন
        if not file_path:
            file_path = default_path  # ডিফল্ট পাথ

        # ফাইল পাথ চেক করা এবং এটি সঠিক কিনা
        if os.path.exists(file_path):
            # যদি এটি একটি ডিরেক্টরি হয়
            if os.path.isdir(file_path):
                print(Fore.RED + "⚠️Ꭾ𝙻𝙴𝙰𝚂𝙴 Ꭼ𝙽𝚃𝙴𝚁 Ꮀ𝚄𝙻𝙻 Ꭾ𝙰𝚃𝙷, Ꮑ𝙾𝚃 Ꮀ𝙾𝙻𝙳𝙴𝚁 Ꮑ𝙰𝙼𝙴 Ꮻ𝙽𝙻𝚈")
                print()  # নতুন লাইন
            else:
                return file_path  # সঠিক ফাইল পাথ দিলে রিটার্ন করুন
        else:
            print(Fore.RED + "📂 ᎬᏁᎢᎬᏒ Ꭺ ᏙᎪᏞᏐᎠ ᎮᎪᎢᎻ")
            print()  # নতুন লাইন

# লোডিং এনিমেশন ফাংশন (এবার দ্রুত)
def loading_animation():
    print(Fore.YELLOW + "Ꮮ𝙾𝙰𝙳𝙸𝙽𝙶...", end="\r")
    for _ in range(2):  # ১ সেকেন্ডের মধ্যে
        print(Fore.YELLOW + "Ꮮ𝙾𝙰𝙳𝙸𝙽𝙶 .", end="\r")
        time.sleep(0.3)  # সময় কমানো (0.3 সেকেন্ড)
        print(Fore.YELLOW + "Ꮮ𝙾𝙰𝙳𝙸𝙽𝙶 ..", end="\r")
        time.sleep(0.3)
        print(Fore.YELLOW + "Ꮮ𝙾𝙰𝙳𝙸𝙽𝙶 ...", end="\r")
        time.sleep(0.3)
    print(Fore.YELLOW + "Ꭲ𝙾𝙾𝙻𝚂 Ꮯ𝚁𝙴𝙰𝚃𝙴 Ᏼ𝚈 Ꮧ𝙽𝙾𝙽𝚈𝙼𝙾𝚄Ꭶ")
    print("-" * 30)  # লম্বা লাইন
    print()  # নতুন লাইন
    print(Fore.GREEN + "Ꭾ𝚁𝙴𝚂𝚂 𝚀 Ꮀ𝙾𝚁 Ꭼ𝚇𝙸𝚃") # দুটি নতুন লাইন
    print()  
    print(Fore.GREEN + "Ꭾ𝚁𝙴𝚂𝚂 Ꭼ𝙽𝚃𝙴𝚁 Ꮀ𝙾𝚁 Ꭰ𝙴𝙵𝙰𝚄𝙻𝚃 Ꭾ𝙰𝚃𝙷")
    print("-" * 30)  # আরেকটি লম্বা লাইন
    print()  # নতুন লাইন

# টার্মিনাল ক্লিয়ার করার ফাংশন
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# টেলিগ্রাম চ্যানেল লিংক ওপেন করা
def open_telegram_channel():
    # আপনার চ্যানেলের URL এখানে দিন
    telegram_link = "https://t.me/Anonymous_Raihan"
    print(Fore.YELLOW + f"\n{telegram_link}")  # শুধুমাত্র লিংক প্রদর্শন
    webbrowser.open(telegram_link)  # লিংকটি ওপেন করা

def main():
    # টার্মিনাল ক্লিয়ার করা
    clear_terminal()

    # ASCII ব্যানার প্রদর্শন
    print_banner()

    # টেলিগ্রাম চ্যানেল লিংক প্রদর্শন
    open_telegram_channel()  # চ্যানেল লিংক দেখাবে এবং ওপেন করবে
    print()  # নতুন লাইন

    # লোডিং এনিমেশন দেখান
    loading_animation()
    
    # ইউজার থেকে ফাইল পাথ নেওয়া
    file_path = get_file_path()

    # ফাইল পাথ পাওয়া গেলে
    if file_path:
        # ইউজার থেকে XOR কী নেওয়া
        key = get_key()

        # আউটপুট পাথ যেখানে ডিক্রিপ্ট করা ফাইল সেভ হবে
        output_path = os.path.join(os.path.dirname(file_path), "anonymous_decrypt.apk")

        # ডিক্রিপ্ট ফাংশন কল করা
        xor_decrypt(file_path, key, output_path)

if __name__ == "__main__":
    main()