from rest_framework import serializers

from financial_records_02.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
        source='parent'
    )

    class Meta:
        model = Category
        fields = ('id', 'parent_id', 'name', 'type')

        def create(self, validated_data):
            user = self.context['request'].user  # Get the authenticated user from the request
            category = Category.objects.create(user=user, **validated_data)
            return category

        def validate_parent(self, value):
            # Check if the parent category is not itself
            if value == self.instance:
                raise serializers.ValidationError("A category cannot be its own parent.")
            return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.parent:
            representation['parent_id'] = instance.parent.id
        return representation
