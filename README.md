Tiny Markdown Server
====================

 Introduction
--------------

This is a start of a very simple markdown web-server. The server must be started in the folder where your markdown files are located. You point the URL to the markdown-file, which will be converted on the fly.

Run the server
--------------

You need to create markdown files in the folder of tiny-markdown-server.

```python
cd tiny-markdown-server
poetry install
poetry run tiny_markdown_server
```
Or once you activate the virtual environment, you can run tiny_markdown_server.cmd everywhere.

TODO
----

- CSS as an argument parameter to customize the html.