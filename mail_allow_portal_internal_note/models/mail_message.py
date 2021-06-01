# Copyright 2021 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Message(models.Model):
    _inherit = "mail.message"

    def _get_search_domain_share(self):
        if (
            self.user_has_groups("base.group_portal")
            and self.env.user.special_portal_users
        ):
            return []
        else:
            return super(Message, self)._get_search_domain_share()
