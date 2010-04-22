# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv
import tools
import crm_report

AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('cancel', 'Cancelled'),
    ('done', 'Closed'),
    ('pending','Pending')
]

class crm_opportunity_report(osv.osv):
    """ CRM Opportunity Report """
    _name = "crm.opportunity.report"
    _auto = False
    _inherit = "crm.case.report"
    _description = "CRM Opportunity Report"
    _columns = {
        'probability': fields.float('Avg. Probability', readonly=True,group_operator='avg'),
        'amount_revenue': fields.float('Est.Revenue', readonly=True),
        'amount_revenue_prob': fields.float('Est. Rev*Prob.', readonly=True),
        'delay_close': fields.float('Delay to close',digits=(16,2),readonly=True, group_operator="avg",help="Number of Days to close the case"),
        'categ_id': fields.many2one('crm.case.categ', 'Category',\
                     domain="[('section_id','=',section_id),\
                    ('object_id.model', '=', 'crm.opportunity')]", readonly=True),
        'stage_id':fields.many2one('crm.case.stage', 'Stage',\
                     domain="[('section_id','=',section_id),\
                     ('object_id.model', '=', 'crm.opportunity')]", readonly=True),
        'partner_id': fields.many2one('res.partner', 'Partner', readonly=True),
        'company_id': fields.many2one('res.company', 'Company', readonly=True),
        'user_id':fields.many2one('res.users', 'User', readonly=True),
        'date_closed': fields.datetime('Closed', readonly=True),
        'date_open': fields.datetime('Opened', readonly=True),
        'date_deadline': fields.date('Expected Closing', readonly=True),
        'priority': fields.selection(crm_report.AVAILABLE_PRIORITIES, 'Priority'),
        'date_action': fields.date('Next Action', readonly=True),
        'planned_revenue': fields.float('Expected Revenue', readonly=True),
    }

    def init(self, cr):
        """ Display Est.Revenue , Average Probability ,Est.Revenue Probability
            @param cr: the current row, from the database cursor
        """

        tools.drop_view_if_exists(cr, 'crm_opportunity_report')
        cr.execute("""
            create or replace view crm_opportunity_report as (
                select
                    min(c.id) as id,
                    to_char(c.create_date, 'YYYY') as name,
                    to_char(c.create_date, 'MM') as month,
                    to_char(c.create_date, 'YYYY-MM-DD') as day,
                    c.state as state,
                    c.user_id,
                    c.section_id,
                    c.categ_id,
                    c.stage_id,
                    c.partner_id,
                    c.company_id,
                    count(*) as nbr,
                    0 as avg_answers,
                    0.0 as perc_done,
                    0.0 as perc_cancel,
                    c.date_closed as date_closed,
                    c.date_open as date_open,
                    c.priority as priority,
                    c.date_action as date_action,
                    c.date_deadline as date_deadline,
                    sum(c.planned_revenue) as planned_revenue,
                    date_trunc('day',c.create_date) as create_date,
                    sum(planned_revenue) as amount_revenue,
                    sum((planned_revenue*probability)/100.0)::decimal(16,2) as amount_revenue_prob,
                    avg(probability)::decimal(16,2) as probability,
                    avg(extract('epoch' from (c.date_closed-c.create_date)))/(3600*24) as  delay_close
                from
                    crm_opportunity c
                group by
                    to_char(c.create_date, 'YYYY'),
                    to_char(c.create_date, 'MM'),
                    to_char(c.create_date, 'YYYY-MM-DD'),
                    c.state,
                    c.user_id,
                    c.section_id,
                    c.stage_id,
                    c.categ_id,
                    c.partner_id,
                    company_id,
                    create_date,
                    c.date_closed,
                    c.date_open,
                    c.priority,
                    c.date_action,
                    c.date_deadline
            )""")

crm_opportunity_report()
