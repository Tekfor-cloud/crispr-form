from odoo import models, api
from lxml import etree


class IrUiView(models.Model):
    _inherit = "ir.ui.view"

    def apply_view_form_arch_insert(self, arch):
        for insert_arch_tag in arch.xpath("//form-arch-insert"):
            view = self.env.ref(insert_arch_tag.get("view_ref"))
            view_arch = view.read_combined(["arch", "type"])["arch"]
            view_arch_tree = etree.fromstring(view_arch)

            parent_tag = insert_arch_tag.getparent()
            parent_tag.replace(insert_arch_tag, view_arch_tree)

        return arch

    @api.model
    def apply_inheritance_specs(
        self, source, specs_tree, pre_locate=lambda s: True
    ):
        source = self.apply_view_form_arch_insert(source)
        return super(IrUiView, self).apply_inheritance_specs(
            source, specs_tree, pre_locate
        )

    def _combine(self, hierarchy: dict):
        arch = super()._combine(hierarchy)
        arch = self.apply_view_form_arch_insert(arch)
        return arch

    # def _get_combined_arch(self):
    #     arch = super(IrUiView, self)._get_combined_arch()
    #     arch = self.apply_view_form_arch_insert(arch)
    #     return arch
