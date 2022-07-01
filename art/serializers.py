from rest_framework import serializers

from art.models import Category as CategoryModel, Product
from art.models import Product as ProductModel
from art.models import Log as LogModel
from art.models import ImageShape
        
from rest_framework import serializers
from .models import Category, Product, ImageShape, Log

##################################################################
### Main Page
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]

class ProductsMainSerializer(serializers.ModelSerializer):
    created_user = serializers.SerializerMethodField()
    def get_created_user(self, obj):
        return obj.created_user.fullname

    category = serializers.SerializerMethodField()
    def get_category(self,obj):
        return obj.category.name
    
    class Meta:
        model = Product
        fields = ["id", "category", "created_user", "img_path", "title", "description",
                  "price", "is_selling", "created_date"]

class LogsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    def get_product(self, obj):
        return obj.product.title

    old_owner = serializers.SerializerMethodField()
    def get_old_owner(self, obj):
        return obj.old_owner.fullname

    class Meta:
        model = Log
        fields = ['product', 'old_owner', 'updated_date', 'old_price']

##################################################################
### MyGalley Page
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogModel
        fields = ["product", "old_owner", "updated_date", "old_price", ]

class MyGallerySerializer(serializers.ModelSerializer):
    # created_user = serializers.SerializerMethodField()
    # def get_created_user(self, obj):
    #     return obj.created_user.fullname
    
    # owner_user = serializers.SerializerMethodField()
    # def get_owner_user(self, obj):
    #     return obj.owner_user.fullname
    
    # category = serializers.SerializerMethodField()
    # def get_category(self,obj):
    #     return obj.category.name
    
    def create(self, validated_data):
        print("create 도착!")
        img_path = validated_data["img_path"]
        print(f"img_path : {img_path}")
        instance = FileUpload()
        result = instance.file_upload(img_path)
        print(result["success"])
        validated_data["img_path"] = f"luckyseven-todaylunch.s3.ap-northeast-2.amazonaws.com/{img_path}"
        print(validated_data["img_path"])
        product = ProductModel(**validated_data)
        product.save()
        
        return product
    
    log = LogSerializer(many=True, source="log_set", read_only=True)
    
    class Meta:
        model = ProductModel

'''
import boto3
class FileUpload():
    def file_upload(self, img_path):
        file = img_path
        print(file)
        s3 = boto3.client('s3')
        # s3 = 	boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY, aws_secret_access_key = AWS_SECRET_KEY)
        s3.put_object(
            ACL="public-read",
            Bucket= "luckyseven-todaylunch", # "{버킷이름}",
            Body=file, # 업로드할 파일 객체
            Key=str(file), # S3에 업로드할 파일의 경로
            ContentType=file.content_type # 메타데이터 설정
        ) 
        return {'success': 'S3 업로드 완료'}
'''
