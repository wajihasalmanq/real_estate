from odoo import fields, models, api


class EstateProperties(models.Model):

	_name = "estate.property"
	_description = "Model for Real-Estate Properties"

	name = fields.Char(required=True)
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date()
	expected_price = fields.Float(required=True)
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean(default=False)
	garden = fields.Boolean(default=False)
	garden_area = fields.Integer()
	garden_orientation = fields.Selection(
        [('north', 'North'), ('east', 'East'), ('west', 'West'), ('south', 'South')],
        string="Garden Orientation")


	total_area = fields.Integer(compute='_compute_total_area', store=True)

	@api.depends('living_area', 'garden_area')
	def _compute_total_area(self):
			for property_record in self:
				property_record.total_area = property_record.living_area + property_record.garden_area