# Segno - QR Code Generation in Python (Cheat Sheet)

Segno is a pure Python library for creating QR codes and Micro QR codes. It's easy to use, versatile, and offers customization options.

## Installation:

```bash
pip install segno
```
## Basic Usage:

```python

import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save("basic_qrcode.png")
