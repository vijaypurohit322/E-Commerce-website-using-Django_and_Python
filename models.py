# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carddetails(models.Model):
    card_details_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    card_type = models.ForeignKey('Cardtypes', models.DO_NOTHING, db_column='card_type', blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    card_exp_mo = models.IntegerField(blank=True, null=True)
    card_exp_yr = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CardDetails'


class Cardtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    card_type = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CardTypes'


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    product_id = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cart'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    category_image_url = models.CharField(max_length=250, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Countries(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_code = models.IntegerField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_active = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Countries'


class Customeraccessrecord(models.Model):
    access_record_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    ip_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    lat = models.TextField(blank=True, null=True)  # This field type is a guess.
    long = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CustomerAccessRecord'


class Customeractivity(models.Model):
    user_activity_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    ip_address = models.CharField(max_length=20)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    activity_record = models.CharField(max_length=250, blank=True, null=True)
    cart_items_id = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerActivity'


class Customeraddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    room_number = models.CharField(max_length=15, blank=True, null=True)
    building = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country', blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING, db_column='state', blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    address_type = models.ForeignKey('Customeraddresstypes', models.DO_NOTHING, db_column='address_type', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerAddress'


class Customeraddresstypes(models.Model):
    id = models.IntegerField(primary_key=True)
    address_type = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerAddressTypes'


class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    middle_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    avtar_url = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country', blank=True, null=True)
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    reward = models.BooleanField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    referral_code = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    total_coins = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customers'


class Discount(models.Model):
    discount_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    discount_type = models.CharField(max_length=50, blank=True, null=True)
    discount_amount = models.IntegerField(blank=True, null=True)
    dicount_note = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Discount'


class Fulfillstatus(models.Model):
    fulfilled_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=15, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FulfillStatus'


class Guestactivity(models.Model):
    guest_activity_id = models.IntegerField(primary_key=True)
    guest = models.ForeignKey('Guestuser', models.DO_NOTHING, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    activity_record = models.CharField(max_length=-1, blank=True, null=True)
    cart_items_id = models.CharField(max_length=-1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GuestActivity'


class Guestuser(models.Model):
    generated_guest_id = models.IntegerField(primary_key=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GuestUser'


class Orderdetails(models.Model):
    order_detail_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    fulfilled = models.IntegerField(blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderDetails'


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    order_number = models.CharField(max_length=200, blank=True, null=True)
    payment_id = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    freight = models.IntegerField(blank=True, null=True)
    sales_tax = models.IntegerField(blank=True, null=True)
    transact_status = models.CharField(max_length=250, blank=True, null=True)
    errloc = models.CharField(db_column='ErrLoc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    errmsg = models.CharField(db_column='ErrMsg', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fulfilled = models.ForeignKey(Fulfillstatus, models.DO_NOTHING, db_column='fulfilled', blank=True, null=True)
    paid = models.BooleanField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    product_id = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Orders'


class Paymentmethods(models.Model):
    method_id = models.IntegerField(primary_key=True)
    method_type = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PaymentMethods'


class ProductReview(models.Model):
    product_review_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    image_url = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product_review'


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    sku = models.IntegerField(blank=True, null=True)
    idsku = models.IntegerField(blank=True, null=True)
    vendor_procuct_id = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_description = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_type = models.CharField(max_length=50, blank=True, null=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    quantityperunit = models.IntegerField(db_column='quantityPerUnit', blank=True, null=True)  # Field name made lowercase.
    unit_price = models.TextField(blank=True, null=True)  # This field type is a guess.
    msrp = models.TextField(blank=True, null=True)  # This field type is a guess.
    available_size = models.IntegerField(blank=True, null=True)
    discount = models.TextField(blank=True, null=True)  # This field type is a guess.
    unitweight = models.FloatField(db_column='unitWeight', blank=True, null=True)  # Field name made lowercase.
    unitsinstock = models.IntegerField(db_column='unitsInStock', blank=True, null=True)  # Field name made lowercase.
    unitsonorder = models.IntegerField(db_column='unitsOnOrder', blank=True, null=True)  # Field name made lowercase.
    is_available = models.BooleanField(blank=True, null=True)
    is_discount_available = models.BooleanField(blank=True, null=True)
    product_image_url = models.CharField(max_length=250, blank=True, null=True)
    ranking = models.FloatField(blank=True, null=True)
    note = models.CharField(max_length=150, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products'


class Referralhistory(models.Model):
    ref_history_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    new_user_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ReferralHistory'


class Referrals(models.Model):
    referral_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    referral_code = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Referrals'


class Reward(models.Model):
    reward_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    reward_type = models.CharField(max_length=50, blank=True, null=True)
    reward_amount = models.IntegerField(blank=True, null=True)
    reward_note = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reward'


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_active = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'States'


class Suppliers(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    role = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.TextField()  # This field type is a guess.
    middle_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    landline_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    avtar_url = models.CharField(max_length=250, blank=True, null=True)
    payment_method = models.ForeignKey(Paymentmethods, models.DO_NOTHING, db_column='payment_method', blank=True, null=True)
    is_discount_available = models.BooleanField(blank=True, null=True)
    discount_type = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    logo_url = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_authorized = models.BooleanField(blank=True, null=True)
    is_block = models.BooleanField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Suppliers'


class Suppliersaddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    supplier = models.ForeignKey(Suppliers, models.DO_NOTHING)
    room_number = models.CharField(max_length=15, blank=True, null=True)
    building = models.CharField(max_length=25, blank=True, null=True)
    address_line1 = models.CharField(max_length=50, blank=True, null=True)
    address_line2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country')
    state = models.ForeignKey(States, models.DO_NOTHING, db_column='state')
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField()
    address_type = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SuppliersAddress'


class Coins(models.Model):
    coins_id = models.IntegerField(primary_key=True)
    coin_value = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coins'


class Customerearnedcoinhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    coin_earned = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerearnedcoinhistory'
