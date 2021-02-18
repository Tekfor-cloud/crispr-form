from odoo.tests import common


class CrisprFormTestSuite(common.TransactionCase):
    def test_crispr(self):
        mdl_partner = self.env["res.partner"]

        view_a = mdl_partner.fields_view_get(
            self.env.ref("crispr_form_test.crispr_test_partner_form_a")
        )

        print(view_a["arch"])
