from rest_framework import serializers
from .models import Task, WBS


class RecursiveField(serializers.BaseSerializer):
    def to_representation(self, value):
        ParentSerializer = self.parent.parent.__class__
        serializer = ParentSerializer(value, context=self.context)
        return serializer.data

    def to_internal_value(self, data):
        ParentSerializer = self.parent.parent.__class__
        Model = ParentSerializer.Meta.model
        try:
            instance = Model.objects.get(pk=data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Objeto {0} does not exists".format(
                    Model().__class__.__name__
                )
            )
        return instance


class TaskSerializer(serializers.ModelSerializer):
    sub_task = RecursiveField(source="children", many=True, required=False)
    extra_kwargs = {
            'sub_task': {
                'read_only': False, 
                'required': False
             }
        }

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'wbs',
            'parent',
            'sub_task')


class WBSSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='task-detail'
    )

    class Meta:
        model = WBS
        fields = (
            'id',
            'name',
            'created_date',
            'tasks')
