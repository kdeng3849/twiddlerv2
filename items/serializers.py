from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ('id', 'username', 'property', 'retweeted', 'content', 'timestamp')

    def get_property(self, obj):
        return_data = None
        if type(obj.property) == list:
            embedded_list = []
            for item in obj.property:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.property.__dict__
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data
        # return_data = None
        # if type(obj.embedded_field) == list:
        #     embedded_list = []
        #     for item in field:
        #         embedded_dict = item.__dict__
        #         for key in list(embedded_dict.keys()):
        #             if key.startswith('_'):
        #                 embedded_dict.pop(key)
        #         embedded_list.append(embedded_dict)
        #     return_data = embedded_list
        # else:
        #     embedded_dict = field.__dict__
        #     for key in list(embedded_dict.keys()):
        #         if key.startswith('_'):
        #             embedded_dict.pop(key)
        #     return_data = embedded_dict
        # return return_data