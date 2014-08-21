# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
#   base_attribute.attributes for OpenERP                                     #
#   Copyright (C) 2011 Akretion Benoît GUILLOT <benoit.guillot@akretion.com>
#   Copyright (C) 2013 Akretion Raphaël VALYI <raphael.valyi@akretion.com>
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as            #
#   published by the Free Software Foundation, either version 3 of the        #
#   License, or (at your option) any later version.                           #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

import ast
from openerp.osv import orm, fields
from openerp.osv.osv import except_osv
from openerp.tools.translate import _
from lxml import etree
from unidecode import unidecode # Debian package python-unidecode
import re


class attribute_attribute(orm.Model):
    _inherit = "attribute.attribute"
   


    def write(self, cr, uid,ids ,vals,context=None):
        """ Create an attribute.attribute

        When a `field_id` is given, the attribute will be linked to the
        existing field. The use case is to create an attribute on a field
        created with Python `fields`.

        """
        global search_model_ids
        try:
            if search_model_ids:
                print search_model_ids
                pass
        except:
            search_model_ids = []

        res = super(attribute_attribute, self).write(cr, uid, ids,vals, context)
        print"uper vals",vals
        print"ids ka value",ids[0]
        sol=self.browse(cr,uid,ids[0])
        if not search_model_ids:
            search_model_ids=self.search(cr,uid,[('name','=',sol.name),('model', 'in',['product.product','product.template','sale.order.line'])])
        print "sol",sol.id,search_model_ids
        if sol.id in search_model_ids:
            search_model_ids.remove(sol.id)
            
            for each in search_model_ids:
                print"each value is:",each
                if sol.id != each:
                    self.write(cr, uid, [each], vals, context)
                    print"new vals",vals

        return res

    def create(self, cr, uid, vals, context=None):
        """ Create an attribute.attribute

        When a `field_id` is given, the attribute will be linked to the
        existing field. The use case is to create an attribute on a field
        created with Python `fields`.

        """
        global search_model_ids
        try:
            if search_model_ids:
                print search_model_ids
                pass
        except:
            search_model_ids = []
            
        if vals.get('field_id'):
            # when a 'field_id' is given, we create an attribute on an
            # existing 'ir.model.fields'.  As this model `_inherits`
            # 'ir.model.fields', calling `create()` with a `field_id`
            # will call `write` in `ir.model.fields`.
            # When the existing field is not a 'manual' field, we are
            # not allowed to write on it. So we call `create()` without
            # changing the fields values.
            field_obj = self.pool.get('ir.model.fields')
            
            print"field_obj got product class",field_obj
            field = field_obj.browse(cr, uid, vals['field_id'], context=context)
            if vals.get('serialized'):
                raise orm.except_orm(
                    _('Error'),
                    _("Can't create a serialized attribute on "
                      "an existing ir.model.fields (%s)") % field.name)
            if field.state != 'manual':
                # the ir.model.fields already exists and we want to map
                # an attribute on it. We can't change the field so we
                # won't add the ttype, relation and so on.
                return super(attribute_attribute, self).create(cr, uid, vals,
                                                               context=context)
        if vals.get('relation_model_id'):
            relation = self.pool.get('ir.model').read(
                cr, uid, [vals.get('relation_model_id')], ['model'])[0]['model']
            print"telation relation",relation
        else:
            relation = 'attribute.option'
        if vals['attribute_type'] == 'select':
            vals['ttype'] = 'many2one'
            vals['relation'] = relation
        elif vals['attribute_type'] == 'multiselect':
            vals['ttype'] = 'many2many'
            vals['relation'] = relation
            vals['serialized'] = True
        else:
            vals['ttype'] = vals['attribute_type']
        
        if vals.get('serialized'):
            field_obj = self.pool.get('ir.model.fields')
            serialized_ids = field_obj.search(cr, uid, [
                ('ttype', '=', 'serialized'),
                ('model_id', '=', vals['model_id']),
                ('name', '=', 'x_custom_json_attrs')],
                context=context)
            if serialized_ids:
                vals['serialization_field_id'] = serialized_ids[0]
            else:
                f_vals = {
                    'name': u'x_custom_json_attrs',
                    'field_description': u'Serialized JSON Attributes',
                    'ttype': 'serialized',
                    'model_id': vals['model_id'],

                }
                vals['serialization_field_id'] = field_obj.create(
                    cr, uid, f_vals, {'manual': True})

        vals['state'] = 'manual'
        res = super(attribute_attribute, self).create(cr, uid, vals, context)
        if not search_model_ids:
            search_model_ids=self.pool.get('ir.model').search(cr,uid,[('model', 'in',['product.product','product.template','sale.order.line'])])

        if vals['model_id'] in search_model_ids:
            search_model_ids.remove(vals['model_id'])
            for each in search_model_ids:
                if vals['model_id'] != each:
                    
                    if vals.get('serialized'):
                        field_obj = self.pool.get('ir.model.fields')
                        serialized_ids = field_obj.search(cr, uid, [
                            ('ttype', '=', 'serialized'),
                            ('model_id', '=', each),
                            ('name', '=', 'x_custom_json_attrs')],
                            context=context)
                        if serialized_ids:
                            vals['serialization_field_id'] = serialized_ids[0]
                        else:
                            f_vals = {
                                'name': u'x_custom_json_attrs',
                                'field_description': u'Serialized JSON Attributes',
                                'ttype': 'serialized',
                                'model_id': each,

                            }
                            vals['serialization_field_id'] = field_obj.create(
                                cr, uid, f_vals, {'manual': True})

                    vals['state'] = 'manual'
                    vals.update({'model_id' : each})
                    self.copy(cr, uid, res, vals, context)

        return res

  