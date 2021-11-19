from flask_marshmallow import Marshmallow
from ESECAF.model.model import Family, Population
import sys
sys.path.append(".")
from ESECAF import app


ma = Marshmallow(app)

class PopulationSchema(ma.Schema):
    class Meta:
        model = Population
        fields = ('id', 'name', 'state', 'municipality', 'tn', 'tm')

class FamilySchema(ma.Schema):
    class Meta:
        model = Family
        fields = ('id', 'head_of_household', 'address', 'cp', 'number_of_children', 'donations','population_id')