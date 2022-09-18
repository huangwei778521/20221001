from django.db import models

# Create your models here.
from django.db.models import Model


class BookInfo(Model):
    """图书类模型"""
    bname = models.CharField(max_length=30, verbose_name="书名")
    bpub_date = models.DateField(null=True, verbose_name="出版日期")
    bread_count = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment_count = models.IntegerField(default=0, verbose_name="评论量")
    is_deleted = models.BooleanField(default=False, verbose_name="是否逻辑删除")

    class Meta:
        db_table = "books"
        verbose_name = "图书"
        verbose_name_plural = "图书集"

    def __str__(self):
        return self.bname


class HeroInfo(Model):
    """图书中英雄类模型"""
    GENDER_CHOICE = (
        (0, "female"),
        (1, "male")
    )
    hname = models.CharField(max_length=30, verbose_name="英雄名")
    hgender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name="性别")
    hdescription = models.CharField(max_length=200, verbose_name="英雄描述")
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="所属图书")
    is_deleted = models.BooleanField(default=False, verbose_name="是否逻辑删除")

    class Meta:
        db_table = "heros"
        verbose_name = "英雄"
        verbose_name_plural = "英雄集"

    def __str__(self):
        return self.hname+","+self.book.bname
