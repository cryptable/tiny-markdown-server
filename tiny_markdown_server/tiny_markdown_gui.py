import os

from .tiny_markdown_server import start_web_server, stop_web_server
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.hazmat.primitives import serialization
import PySimpleGUI as sg
from threading import Thread
t = Thread(target=print, args=[1])
t.run()


working_directory = os.getcwd()


def prepare_ssl_keys(pfx_file: str, password: str):
    pfx_data = None
    with open(pfx_file, 'rb') as f:
        pfx_data = f.read()
        f.close()
    p12 = load_key_and_certificates(pfx_data, password.encode("utf-8"))
    if p12[0]:
        with open("private_key.pem", "wb") as f:
            f.write(p12[0].private_bytes(encoding=serialization.Encoding.PEM,
                                         format=serialization.PrivateFormat.TraditionalOpenSSL,
                                         encryption_algorithm=serialization.NoEncryption()))
            f.close()
    if p12[1]:
        with open("cert_chain.pem", "wb") as f:
            f.write(p12[1].public_bytes(encoding=serialization.Encoding.PEM))
            f.close()
    if p12[2]:
        with open("cert_chain.pem", "ab") as f:
            for cert in p12[2]:
                f.write(cert.public_bytes(encoding=serialization.Encoding.PEM))
                f.close()
    return "cert_chain.pem", "private_key.pem"


def gui_web_server(hostname: str = "localhost", port: int = 8080):
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Tiny Markdown Server')],
        [sg.Text('PFX file'), sg.InputText(key='--PFX_FILE--'),
         sg.FileBrowse(initial_folder=working_directory,
                       file_types=[("Microsoft PFX Files", "*.pfx"), ("PKCS12 Files", "*.p12"), ("All Files", "*.*")])],
        [sg.Text('Password'), sg.InputText(key='--PASSWORD--')],
        [sg.Button('Exit'), sg.Button('Start Server')],
    ]
    window = sg.Window('Tiny Markdown Server', layout)
    cert_chain = None
    private_key = None
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            stop_web_server()
            break
        if event == 'Start Server':
            arguments = [hostname, port]
            if values['--PFX_FILE--']:
                (cert_chain, private_key) = prepare_ssl_keys(values['--PFX_FILE--'], values['--PASSWORD--'])
            if cert_chain:
                arguments.append(cert_chain)
                arguments.append(private_key)
            t = Thread(target=start_web_server, args=arguments)
            t.start()
