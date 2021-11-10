[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/master.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](http://www.odoo.com/documentation/15.0)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](http://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/15.0/administration/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/15.0/developer/howtos.html">the developer tutorials</a>

## HOW TO INSTALL

### CONFIGURE

Edit dockerize/odoo.conf, set `admin_passwd` to your admin password.

Edit docker-compose.yml, set `ODOO_DOMAIN` to main domain name, eg: localhost

### BUILD AND RUN DOCKER

```sh
docker-compose build web nginx
docker-compose up -d
```

### SETUP MAIN DOMAIN

Go https://<YOUR_DOMAIN>, enter following fields to create new database for main domain:
- Master Password: your admin password set in odoo.conf
- Database Name: same as `ODOO_DOMAIN`.
- Email: your admin email.
- Password: your admin password.

Install `New Database From Template` app, go Settings\General Settings\NDFT, set
- Conf Path: /var/lib/odoo/nginx/conf.d
- SSL Path: /var/lib/odoo/nginx/ssl

### CREATE NEW DATABASE FROM TEMPLATE

Go Settings\Users & Companies\NDFT Databases, create new database:
- Name: your database name, eg: s1.test
- Template: select a template for new database.
- Admin Email: your admin email to log in.
- Admin Password: your admin password.
- Server:
  - Domain: Same as database name, eg: s1.test
  - Enabled: enable or disable this server.
  - DB Filter: Use default database filter by backend or filter database by header.
  - Type: server type, currently only support Nginx.
  - Use HTTPS: server use HTTP or HTTPS.
  - SSL Cert CA:
    - Self Signed: auto generate self signed SSL Certs.
    - Let Encrypt: using Let's Encrypt to get free SSL Certs.
    - Custom: allow upload your own SSL Certs file.

Then open browser, go http://s1.test to access new website.
