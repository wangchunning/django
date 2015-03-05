class Vendor(models.Model):

    STATUS_ACTIVE = 0
    STATUS_INACTIVE = 1

    VENDOR_STATUS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    )

    AUS_STATE = (('NSW', 'NSW'),
                 ('QLD', 'QLD'),
                 ('TAS', 'TAS'),
                 ('SA', 'SA'),
                 ('WA', 'WA'),
                 ('NT', 'NT'),
                 ('ACT', 'ACT'),)

    id = models.AutoField(primary_key=True)

    business_name = models.CharField(max_length=128, default='', db_index = True)
    status = models.SmallIntegerField(default=0, choices=VENDOR_STATUS)
    is_ext_agent = models.SmallIntegerField(default=0)
    is_gst_registered = models.SmallIntegerField(default=0)

    abn = models.CharField(max_length=20, default='', unique = True)
    acn = models.CharField(max_length=20, default='')

    main_phone = models.CharField(max_length=30, blank=True, default='')
    fax = models.CharField(max_length=30, blank=True, default='')

    main_business_email = models.EmailField(max_length=30, default='')
    notify_email = models.EmailField(max_length=30, default='')
    notify_mobile = models.CharField(max_length=20, default='')

    street_line_1 = models.CharField(max_length=50, default='')
    street_line_2 = models.CharField(max_length=50, default='', blank=True)
    suburb = models.CharField(max_length=50, default='')
    postcode = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=16, choices=AUS_STATE)
    state_other_country = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')

    postal_address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
