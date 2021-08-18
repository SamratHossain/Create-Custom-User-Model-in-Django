from django.contrib.auth.models import BaseUserManager

class AccountUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, phone, gender, dateofbirth):
        if not email:
            raise ValueError("User Must Have an Email")

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, phone=phone, gender=gender, dateofbirth=dateofbirth)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, phone, gender, dateofbirth ):
        user = self.create_user(first_name, last_name, email, password, phone, gender, dateofbirth)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user