from app import overlay

version: str = "0.0.1"

def main():
    print("Application starting...")
    print(f"Mic-Display Version: {version}")

    overlay.run()

if __name__ == '__main__':
    main()