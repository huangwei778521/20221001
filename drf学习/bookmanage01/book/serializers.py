from rest_framework import serializers
from rest_framework.serializers import Serializer

from book.models import BookInfo


class HeroInfoSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    hname = serializers.CharField(max_length=30,min_length=1)
    hgender = serializers.IntegerField(default=0)
    hdescription = serializers.CharField(max_length=200)


class BookInfoSerializer(Serializer):
    """图书的序列化器"""
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    bname = serializers.CharField(max_length=30)
    bpub_date = serializers.DateField()
    bread_count = serializers.IntegerField()
    bcomment_count = serializers.IntegerField()
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # heroinfo_set = serializers.StringRelatedField(many=True,read_only=True)
    heroinfo_set = HeroInfoSerializer(read_only=True,many=True)

    def validate_bname(self, value):
        if value == "python":
            raise serializers.ValidationError("书名不能为python")
        return value

    def validate(self, attrs):
        if attrs["bcomment_count"] > attrs["bread_count"]:
            raise serializers.ValidationError("评论量不能大于阅读量")
        return attrs

    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        mydict = instance.__dict__
        instance.bname = validated_data.get("bname",mydict["bname"])
        instance.bpub_date = validated_data.get("bpub_date",mydict["bpub_date"])
        instance.bread_count = validated_data.get("bread_count",mydict["bread_count"])
        instance.bcomment_count = validated_data.get("bcomment_count",mydict["bcomment_count"])
        instance.is_deleted = validated_data.get("is_deleted",mydict["is_deleted"])
        instance.save()
        return instance





