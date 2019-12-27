from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length= 200, verbose_name = '상품명')
    meta_description = models.TextField(blank= True)
    slug = models.SlugField(max_length= 200,db_index= True, unique= True, allow_unicode=True)
    # db_index 카테고리 정보가 저장되는 테이블은 이 이름 열을 인덱스 열로 설정
    # meta_description은 Search Engine Optimization을 위해 만드는 필드(구글 등 검색엔진에 잘 노출되기 위해)

    class Meta:
        ordering = ['name'] 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_in_category',args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True, unique=True, allow_unicode= True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField() # 오로지 양수만

    available_display = models.BooleanField('Display',default=True) # 상품 노출 여부
    available_order = models.BooleanField('Order',default=True) # 상품 주문 가능 여부
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id','slug']] # 멀티 컬럼 색인 기능 id와 slug 필드를 묶어서 색인이 가능하도록 하는 옵션
        

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])