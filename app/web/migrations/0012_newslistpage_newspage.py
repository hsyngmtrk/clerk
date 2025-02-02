# Generated by Django 3.2.3 on 2021-07-02 02:51

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import web.models.news


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('web', '0011_jobpage_closing_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(web.models.news.NewsRootMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'bold', 'italic', 'ol', 'ul', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.BlockQuoteBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=(web.models.news.NewsRootMixin, 'wagtailcore.page'),
        ),
    ]
