from rest_framework import serializers

from .models import Item

# class PortfolioSerializer(serializers.ModelSerializer):
#     codes = serializers.SerializerMethodField()
#     class Meta:
#         model = Item
#         fields = ('username', 'codes')

#     def get_codes(self, obj):
#         return_data = None
#         if type(obj.codes) == list:
#             embedded_list = []
#             for item in obj.codes:
#                 embedded_dict = item.__dict__
#                 for key in list(embedded_dict.keys()):
#                     if key.startswith('_'):
#                         embedded_dict.pop(key)
#                 embedded_list.append(embedded_dict)
#             return_data = embedded_list
#         else:
#             embedded_dict = obj.embedded_field
#             for key in list(embedded_dict.keys()):
#                 if key.startswith('_'):
#                     embedded_dict.pop(key)
#             return_data = embedded_dict
#         return return_data
