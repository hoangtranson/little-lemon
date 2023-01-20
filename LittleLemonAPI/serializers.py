from rest_framework import serializers
from .models import Book, MenuItem, Category
import bleach


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'inventory', 'category', 'category_id']
        # extra_kwargs = {
        #     'price': {'min_value': 2},
        #     'inventory': {'min_value': 0}
        # }

    # def validate_title(self, value):
    #     return bleach.clean(value)

    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if (attrs['price'] < 2):
            raise serializers.ValidationError(
                'Price should not be less than 2.0')
        if (attrs['inventory'] < 0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
