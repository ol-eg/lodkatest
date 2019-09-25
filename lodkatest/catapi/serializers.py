from rest_framework import serializers
from lodkatest.catapi.models import Category

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class DetailsSerializer(serializers.ModelSerializer):
    children = ChildrenSerializer(many=True, read_only=True)
    parents = serializers.SerializerMethodField()
    siblings = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','name','parents','children','siblings']
    
    # realistically there could be only one parent
    # since names are unique, need to redo models if 
    # multiparents is a requirement
    # and this is just to preset one parent in the list
    def get_parents(self, obj):
        p = Category.objects.none()
        if obj.parent:
            p = Category.objects.filter(id=obj.parent.id)
        return ChildrenSerializer(p, many=True).data

    def get_siblings(self, obj):
        siblings = Category.objects.filter(
            parent=obj.parent).exclude(id=obj.id)
        return ChildrenSerializer(siblings, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'children')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True)
        return fields

    def create(self, validated_data):
        name = validated_data.pop('name')
        children = validated_data.pop('children')
        stack = [(name,children,None)]
        root = None
        while stack:
            name,children,parent = stack.pop()
            parent = Category.objects.create(
                            name=name, parent=parent)
            if not root:
                root = parent
            for child_data in children:
                name = child_data.pop('name')
                children = child_data.pop('children')
                stack.append((name,children,parent))
        return root
