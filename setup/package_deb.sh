#!/bin/bash
python package.py --build-deb --build-dir /home/voi/Projects/SchoolERP/odoo-build/ --pub /home/voi/Projects/SchoolERP/odoo-public15/
echo "Fail dpkg-scanpackages is OK. Just grab deb file from pub dir"
