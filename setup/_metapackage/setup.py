import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-email_template_qweb',
        'odoo14-addon-mail_debrand',
        'odoo14-addon-mail_preview_base',
        'odoo14-addon-mail_send_copy',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
