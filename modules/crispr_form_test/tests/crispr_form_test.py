from xmldiff.main import diff_texts as xml_diff_texts
from odoo.tests import common
import os


class CrisprFormTestSuite(common.TransactionCase):
    def _compare_view_to_expected_result(self, view_name):
        mdl_partner = self.env["res.partner"]

        view_a = mdl_partner.fields_view_get(
            self.env.ref("crispr_form_test.{}".format(view_name)).id
        )

        test_data = view_a["arch"]

        print(os.getcwd())
        with open(
            "crispr_form_test/tests/expected_results/{}.xml".format(view_name)
        ) as f:
            ref_data = f.read()

        self.assertListEqual(xml_diff_texts(test_data, ref_data), [])

    def test_crispr_test_partner_form_a(self):
        self._compare_view_to_expected_result("crispr_test_partner_form_a")