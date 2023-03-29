Tiny Markdown Server
====================

 Introduction
--------------

This is a start of a very simple markdown web-server. The server must be started in the folder where your markdown files are located. You point the URL to the markdown-file, which will be converted on the fly.

Building the server
-------------------

This small web server uses *poetry* as building environment.

```bash
cd tiny-markdown-server
poetry install
```

You can also make a self-contained python executable which uses *pyinstaller*.

```bash
./build_app.bat
```

In the *dist* directory, you can find the application.

Run the server
--------------

### Locally when developing

You need to create markdown files in the folder of tiny-markdown-server.

```bash
poetry run tiny_markdown_server
```
Or once you activate the virtual environment, you can run tiny_markdown_server.cmd everywhere.

### Self-container executable

#### Windows.

When using the self-contained package, double-click on *tiny_md_server.exe* 
in the tiny_md_server directory.


TODO
----

- CSS as an argument parameter to customize the html.
- GUI show output in a textarea
- MacOS X and Linux support

Changelogs
----------

0.3.1 - Fixed the main.py, update the README with more information
0.3.0 - GUI added and TLS support
0.2.0 - Markdown support with no gui
0.1.0 - Initial