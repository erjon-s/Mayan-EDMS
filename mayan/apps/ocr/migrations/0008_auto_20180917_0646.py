from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0007_auto_20170827_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpageocrcontent',
            name='content',
            field=models.TextField(
                blank=True, help_text='The actual text content extracted by '
                'the OCR backend.', verbose_name='Content'
            ),
        ),
    ]
