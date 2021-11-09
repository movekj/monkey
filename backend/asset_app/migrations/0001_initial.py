# Generated by Django 3.2.5 on 2021-11-09 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='名称')),
            ],
            options={
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120, verbose_name='主机链接地址')),
                ('manage_port', models.CharField(max_length=10, verbose_name='管理端口')),
                ('hostname', models.CharField(max_length=200, verbose_name='主机名')),
                ('remark', models.CharField(max_length=512, verbose_name='备注')),
                ('status', models.CharField(choices=[('enable', '启用'), ('disable', '禁用')], max_length=40, verbose_name='状态')),
                ('tag', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name': 'Host',
            },
        ),
        migrations.CreateModel(
            name='Host_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_app.group')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_app.host')),
            ],
            options={
                'verbose_name': 'Host_Group',
            },
        ),
    ]