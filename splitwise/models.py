from django.db import models


# Create your models here.

class User(models.Model):
    CURRENCY = (
        ("INR", "INDIA"),
        ("EURO", "GERMANY"),
        ("DLR", "DOLLAR")

    )
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
    default_current = models.CharField(max_length=5, choices=CURRENCY, default='INR')

    def __str__(self):
        return self.name


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    member = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name

    def add_group_member(self, new_member):
        self.member.add(new_member)

    def share_group_link(self):
        pass

    def group_member(self):
        member_list = self.member.all()
        members = [member for member in member_list]
        return members

    def settle_up(self):
        pass

    def balances(self):
        pass

    def total(self):
        pass

    def add_expense(self):
        pass


class Activity(models.Model):
    des = models.CharField(max_length=100)
    amount = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    SPLIT_CATEGORY = (
        ('EQUAL', 'EQUALLY'),
        ('UNEQUAL', 'UNEQUALLY'),
        ('PERCENT', 'BY PERCENTAGES')
    )
    split_category = models.CharField(choices=SPLIT_CATEGORY, max_length=10, default='EQUAL')

    def __str__(self):
        return "{} paid {} in {}".format(self.creator, self.amount, self.group)

    def save(self, *args, **kwargs):
        print("New save Method in which first existing Split Object will deleted then Multiple Split will be created")
        member_list = self.group.group_member()
        n = len(member_list)

        Split.objects.filter(activity = self).delete()
        for i in range(n):
            s = Split(activity=self, user=member_list[i], amount=self.amount / n)
            s.save()

        super(Activity, self).save(*args, **kwargs)


class Split(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "Id: {} {} owes {} to {}".format(self.id, self.user, self.amount, self.activity.creator)
