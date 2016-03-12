# coding: utf-8

from openerp import fields, models, _


def function_no_method():
    pass


class TestModel(models.Model):
    _name = 'test.model'

    _columns = {}  # deprecated columns
    _defaults = {}  # deprecated defaults

    name = fields.Char(
        _(u"Näme"),  # Don't need translate
        help=u"My hëlp",
        required=False)

    # Imported openerp.fields use Char (Upper case)
    other_field = fields.char(
        name=_("Other field"),
        copy=True,
    )

    other_field2 = fields.char(
        'Other Field2',
        copy=True,
    )

    def my_method1(self, variable1):
        #  Shouldn't show error of field-argument-translate
        self.my_method2(_('hello world'))

    def my_method2(self, variable2):
        return variable2

    def my_method3(self, variable2):
        self.env.cr.commit()  # Dangerous use of commit
        return variable2

    def my_method4(self, variable2):
        self.env.cr2.commit()  # This cr.commit() should not be detected
        return variable2

    def my_method4(self, variable2):
        self.env.cr.commit2()  # This cr.commit() should not be detected too
        return variable2
