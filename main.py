import random

def play_game():
    print("===================================")
    print("🎮 به بازی حدس عدد خوش آمدید!")
    print("===================================")
    print("من یک عدد بین 1 تا 100 در ذهن دارم.")
    print("آیا می‌توانید آن را حدس بزنید؟")
    
    # تولید یک عدد تصادفی بین 1 تا 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # گرفتن حدس از کاربر
            guess = int(input("\nحدس شما چیست؟ (یک عدد بین 1 تا 100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("❌ لطفاً یک عدد بین 1 تا 100 وارد کنید.")
                continue
                
            # بررسی حدس کاربر
            if guess < secret_number:
                print("⬆️ عدد شما کوچک‌تر از عدد من است. یک عدد بزرگتر حدس بزنید.")
            elif guess > secret_number:
                print("⬇️ عدد شما بزرگ‌تر از عدد من است. یک عدد کوچک‌تر حدس بزنید.")
            else:
                print(f"\n🎉 آفرین! شما عدد {secret_number} را درست حدس زدید.")
                print(f"شما در {attempts} تلاش موفق شدید.")
                break # خروج از حلقه وقتی درست حدس زد
                
        except ValueError:
            print("❌ خطا! لطفاً فقط یک عدد وارد کنید (نه حروف).")

def main():
    while True:
        play_game()
        # پرسیدن اینکه آیا کاربر می‌خواهد دوباره بازی کند
        play_again = input("\nآیا می‌خواهید دوباره بازی کنید؟ (y/n): ").lower()
        if play_again != 'y':
            print("\nاز اینکه بازی کردید ممنون! خداحافظ. 👋")
            break

if __name__ == "__main__":
    main()
