# Generated by Django 2.0.5 on 2018-05-27 22:03

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import internationalflavor.countries.models
import inventor.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'amenity',
                'verbose_name_plural': 'amenities',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('published', models.BooleanField(default=True, verbose_name='published')),
                ('promoted', models.BooleanField(default=False, verbose_name='promoted')),
                ('price_starts_at', models.BooleanField(default=False, verbose_name='price starts at')),
                ('price', models.DecimalField(blank=True, db_index=True, decimal_places=2, default=None, help_text='€', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('price_unit', models.CharField(blank=True, choices=[('PERSON', 'person'), ('NIGHT', 'night'), ('DAY', 'day')], max_length=6, verbose_name='price per unit')),
                ('street', models.CharField(max_length=200, verbose_name='street')),
                ('postcode', models.CharField(db_index=True, max_length=30, verbose_name='postcode')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('country', internationalflavor.countries.models.CountryField(db_index=True, verbose_name='country')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326, verbose_name='point')),
                ('image', models.ImageField(help_text='photo or image', max_length=1024, upload_to='images', verbose_name='image')),
                ('banner', models.ImageField(help_text='photo or image', max_length=5120, upload_to='banners', verbose_name='banner')),
                ('person', models.CharField(blank=True, max_length=100, verbose_name='person')),
                ('phone', models.CharField(blank=True, max_length=40, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('website', models.URLField(blank=True, max_length=400, verbose_name='website')),
                ('social_networks', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Google', 'Google'), ('Instagram', 'Instagram'), ('Vimeo', 'Vimeo'), ('YouTube', 'YouTube'), ('LinkedIn', 'LinkedIn'), ('Dribbble', 'Dribbble'), ('Skype', 'Skype'), ('Foursquare', 'Foursquare'), ('Behance', 'Behance')], max_length=10, verbose_name='social network'), blank=True, size=11, verbose_name='social networks')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'listing',
                'verbose_name_plural': 'listings',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('file', models.ImageField(help_text='photo, image or icon', max_length=5120, upload_to='photos', verbose_name='file')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventor.Album')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='as_photo', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('url', models.URLField(max_length=300, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'video',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'accommodation',
                'verbose_name_plural': 'accommodations',
                'ordering': ('title',),
            },
            bases=(inventor.mixins.BookingMixin, 'inventor.listing'),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'animal',
                'verbose_name_plural': 'animals',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'business',
                'verbose_name_plural': 'businesses',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'character',
                'verbose_name_plural': 'characters',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'goods',
                'verbose_name_plural': 'goods',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'restaurant or bar',
                'verbose_name_plural': 'restaurants and bars',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'travel',
                'verbose_name_plural': 'travels',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('listing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventor.Listing')),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicle',
                'ordering': ('title',),
            },
            bases=('inventor.listing',),
        ),
        migrations.AddField(
            model_name='video',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventor.Listing'),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='listings_having_amenity', to='inventor.Amenity', verbose_name='amenities'),
        ),
        migrations.AddField(
            model_name='listing',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='listing',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='listings_of_category', to='inventor.Category', verbose_name='categories'),
        ),
        migrations.AddField(
            model_name='listing',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='listings_with_features', to='inventor.Feature', verbose_name='features'),
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventor.Location'),
        ),
        migrations.AddField(
            model_name='album',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventor.Listing'),
        ),
    ]