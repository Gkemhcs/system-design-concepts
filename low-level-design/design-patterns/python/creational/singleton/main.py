from logger_singleton import LoggerSingleton

def main():
    logger1 = LoggerSingleton()
    logger2 = LoggerSingleton()

    logger1.log("info", "This is an info message from logger1")
    logger2.log("error", "This is an error message from logger2")

    print(f"logger1 is logger2? {logger1 is logger2}")  # True

if __name__ == "__main__":
    main()
