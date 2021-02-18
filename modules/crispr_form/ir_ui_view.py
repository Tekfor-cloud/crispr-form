from odoo import models, api
from lxml import etree


class IrUiView(models.Model):

    _inherit = "ir.ui.view"

    @api.multi
    def read_combined(self, fields=None):
        view_data = super(IrUiView, self).read_combined(fields)

        if view_data.get("type") == "form":
            arch = self.apply_view_form_arch_insert(
                etree.fromstring(view_data["arch"])
            )
            view_data["arch"] = etree.tostring(arch, encoding="unicode")

        return view_data

    def apply_view_form_arch_insert(self, arch):

        for insert_arch_tag in arch.xpath("//form-arch-insert"):
            view = self.env.ref(insert_arch_tag.get("view_ref"))
            view_arch = view.read_combined(["arch"])["arch"]
            view_arch_tree = etree.fromstring(view_arch)

            parent_tag = insert_arch_tag.getparent()
            parent_tag.replace(insert_arch_tag, view_arch_tree)

        return arch
