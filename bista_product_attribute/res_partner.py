from openerp.osv import osv, fields
import time
from datetime import datetime, timedelta
from openerp.tools.float_utils import float_round as round
import openerp.addons.decimal_precision as dp



class res_partner(osv.osv):
    _inherit= "res.partner"
    _columns={
        'x_vendor_id':fields.char('Vendor Id', size=128),
        'x_ein': fields.char('Employer Identification No',size=128),
        'x_street_3': fields.char('Street 3', size=128),



        'mudd_id':fields.char('ID', size=128),
        'x_agency_ae':fields.char('Agency AE ', size=128),
        'annual_revenue':fields.integer('Annual Revenue'),
        'x_bmw_dealer_code':fields.char('BMW Dealer Code', size=128),
        'billing_city':fields.char('Billing City', size=128),
        'billing_cntry':fields.many2one('res.country',"Billing Country"),
        'billing_post':fields.char('Billing Postal Code', size=64),
        'billing_state':fields.many2one('res.country.state', "Billing State"),
        'x_buick_bac_code':fields.char('Buick BAC Code', size=128),
        'x_buick_site_code':fields.char('Buick Site Code', size=128),
        'x_buick':fields.char('Buick', size=128),
        'x_cadillac_bac_code':fields.char('Cadillac BAC Code', size=128),
        'x_cadillac_site_code':fields.char('Cadillac Site Code', size=128),
        'x_cars_sold_new':fields.integer('Cars Sold New'),
        'x_cars_sold_used':fields.integer('Cars Sold Used'),
        'x_chevrolet_bac_code':fields.integer('Chevrolet BAC Code'),
        'x_chevrolet_site_code':fields.integer('Chevrolet Site Code'),
        'x_chrysler_dealer_code':fields.integer('Chrysler Dealer Code'),
        'x_client_id':fields.integer('Client ID'),
        'x_client_service':fields.char('Client Service', size=128),
        'created_by_id':fields.char('Created By Id', size=128),
        'created_date':fields.datetime('Date of Creation'),
        'x_current_user_is_tm':fields.boolean('Current User Is TM'),
        'dms':fields.char('DMS', size=128),
        'x_daimler_dealer_code':fields.char('Daimler Deale Code', size=128),
        'x_distance':fields.float('Distance'),
        'x_do_not_mail':fields.boolean('Do Not Mail'),
        'x_done_business_with':fields.boolean('Done Business With', size=128),
        'x_fiat_dealer_code':fields.char('Fiat Dealer Code', size=128),
        'x_ford_dealer_code':fields.char('Ford Dealer Code', size=128),
        'x_franchises_allowed':fields.char('Franchises Allowed', size=128),
        'x_franchises_assigned':fields.char('Franchises Assigned', size=128),
        'x_fuji_dealer_code':fields.char('Fuji Dealer Code', size=128),
        'x_gmc_bac_code':fields.char('GMC BAC Code', size=128),
        'x_gmc_site_code':fields.char('GMC Site Code', size=128),
        'x_gm_bac_code':fields.char('GM BAC Code', size=128),
        'x_gc_site_code':fields.char('GM Site Code', size=128),
        'x_geeley_dealer_code':fields.char('Geeley Dealer Code ', size=128),
        'geolocation_latitude':fields.float('Geolocation Latitude', digits_compute=dp.get_precision('Payment Term')),
        'geolocation_longitude':fields.float('Geolocation Longitude', digits_compute=dp.get_precision('Payment Term')),
        'x_honda_dealer_code':fields.char('Honda Dealer Code', size=128),
        'x_hyundai_dealer_code':fields.char('Hyundai Dealer Code', size=128),
        'industry':fields.selection([('auto','Automotive'),
                                    ('agri','Agriculture'),
                                    ('machine','Machinery'),
                                    ('edu','Education'),
                                    ('athlets','Athletics'),
                                    ('entertain','Entertainment'),
                                    ('health','Healthcare'),
                                    ('f&b','Food & Beverage'),
                                    ('bank','Banking'),
                                    ('retail','Retail'),
                                    ('no_profit','Not For Profit'),
                                    ('furni','Furniture'),
                                    ('other','Other')], 'Industry'),
        'is_deleted':fields.boolean('Is Deleted'),
        'jigsaw_cmpny_id':fields.char('Jigsaw Company Id', size=164),

        'last_modi_by_id':fields.char('Last Modified By Id', size=128),
        'last_modi_date':fields.datetime('Last Modified Date'),
        'x_last_activity_date':fields.date('Last Activity Date'),
        'x_last_contact_by':fields.char('Last Contacted By', size=128),
        'x_last_sold_date':fields.date('Last Sold Date'),
        'x_mazda_dealer_code':fields.char('Mazda Dealer Code', size=128),
        'x_media_agi_amount':fields.float('Media AGI Amount', size=128),
        'x_mitsubishi_dealer_code':fields.char('Mitsubishi Dealer Code', size=128),
        'x_nissan_dealer_code':fields.char('Nissan Dealer Code', size=128),
        'no_of_employees':fields.integer('Number Of Employees'),
        'owner_id':fields.char('OwnerId', size=128),
        'ownership':fields.char('Ownership', size=128),
        'parnt_id':fields.char('Parent ID', size=128),
        'x_primary_contact':fields.char('Primary Contact'),
        'x_sales_hrs_fri':fields.float('Sales Hours Friday'),
        'x_sales_hrs_mon':fields.float('Sales Hours Monday'),
        'x_sales_hrs_sat':fields.float('Sales Hours Saturday'),
        'x_sales_hrs_sun':fields.float('Sales Hours Sunday'),
        'x_sales_hrs_thr':fields.float('Sales Hours Thursday'),
        'x_sales_hrs_tue':fields.float('Sales Hours Tuesday'),
        'x_sales_hrs_wed':fields.float('Sales Hours Wednesday'),
        'x_sales_ppl':fields.integer('Sales People'),
        'x_service_technicians':fields.char('Service Technicians', size=128),
        'ship_city':fields.char('Shipping City', size=128),
        'ship_cntry':fields.many2one('res.country', 'Shipping Country'),
        'ship_post':fields.char('Shipping Postal Code', size=64),
        'ship_state':fields.many2one('res.country.state', 'Shipping State'),
        'ship_street':fields.char('Shipping Street', size=128),
        'x_finance_sold':fields.float('Special Finance Sold'),
        'x_suzuki_dealer_code':fields.char('Suzuki Dealer Code', size=128),
        'systm_stamp':fields.datetime('System Mod stamp', size=128),
        'x_tata_dealer_code':fields.char('Tata Dealer Code', size=128),
        'x_total_cars_sold':fields.char('Total Cars Sold', size=128),
        'x_toyota_dealer_code':fields.char('Toyota Dealer Code', size=128),
        'cust_type':fields.selection([('prospect','Prospect'),
                                    ('active','Active Customer'),
                                    ('inactive','Inactive Customer'),
                                    ('raving','Raving Fans')], 'Customer Type'),
        'x_use_as_ref':fields.boolean('Use as Reference'),
        'x_used_only':fields.boolean('Used Only'),
        'x_volkswagen_dealer_code':fields.char('Volkswagen Dealer Code', size=128),



        'account_id':fields.char('Account Id', size=128),
        'assistant':fields.char('Assistant Name', size=128),
        'assistant_ph':fields.char('Assistant Phone', size=128),
        'birth_date':fields.date('Birth Date'),
        'contact_id':fields.integer('Contact Id'),
        'do_not_call':fields.boolean('Do Not Call'),
        'email_bounced_date':fields.date('Email Bounced Date'),
        'email_bounced_reason':fields.text('Email Bounced Reason'),
        'first_name':fields.char('First Name', size=64),
        'last_name':fields.char('Last Name', size=64),
        'opt_out_fax':fields.char('Has Opted-Out Of Fax', size=128),
        'home_phone':fields.char('Home Phone', size=128),
        'last_cu_req_date':fields.date('Last CU Request Date'),
        'last_cu_update_date':fields.date('Last CU Update Date', size=128),
        'lead_src':fields.char('Lead Source', size=128),
        'mailing_city':fields.char('Mailing City', size=128),
        'mailing_cntry':fields.many2one('res.country','Mailing Country'),
        'mailing_post':fields.char('Mailing Postal Code', size=64),
        'mailing_state':fields.many2one('res.country.state','Mailing State'),
        'mailing_street':fields.char('Mailing Street', size=128),
        'master_record_id':fields.char('Master Record Id', size=128),
        'opt_out_email_date':fields.date('Opted-Out Of Email Date'),
        'other_city':fields.char('Other City', size=64),
        'other_cntry':fields.many2one('res.country', 'Other Country'),
        'other_state':fields.many2one('res.country.state','Other State'),
        'other_postal_code':fields.char('Other Postal Code', size=64),
        'other_street':fields.char('Other Street', size=128),
        'x_primary':fields.boolean('Primary'),
        'reports_told':fields.char('Reports Told', size=128),
        'salutation':fields.char('Salutation', size=128),


    }

#    _sql_constraints = [
#        ('vendor_uniq', 'unique(x_vendor_id)', 'Vendor ID should be unique!'),
#    ]


res_partner()