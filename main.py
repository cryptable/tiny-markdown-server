import sys
from tiny_markdown_server.tiny_markdown_gui import gui_web_server


def main():
    hostname = "localhost"
    port = 8080

    if len(sys.argv) == 3:
        hostname = sys.argv[1]
        port = int(sys.argv[0])

    gui_web_server()


if __name__ == "__main__":
    main()