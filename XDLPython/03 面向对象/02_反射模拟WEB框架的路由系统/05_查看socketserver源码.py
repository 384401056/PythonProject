#!/usr/bin/env python
# -*- coding utf-8 -*-

import socketserver


def main():
    r = socketserver.ThreadingTCPServer()
    r.serve_forever()


if __name__ == '__main__':
    main()