

from app import App


if __name__ == "__main__":
    app = App()
    app.set_fps(60)
    app.start()
    app.main_loop()