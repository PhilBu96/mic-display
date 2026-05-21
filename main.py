from app import overlay
from setuptools_scm import get_version

APP_VERSION = get_version()

def main():
    print("Application starting...")
    print("Application version:", APP_VERSION)

    overlay.run()

if __name__ == '__main__':
    main()