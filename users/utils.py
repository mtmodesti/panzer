from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
  
  def _create_user(self, email, password, name, is_staff, is_superuser, **extra_fields):
    email = self.normalize_email(email)
    
    user = self.model(
      name = name,
      email = email,
      is_superuser = is_superuser,
      is_staff = is_staff,
      **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  
  
  def create_user(self, email, password, name, **extra_fields):
    return self._create_user(email, password, name, False, False, **extra_fields)
  
  def create_superuser(self, email, password, name, **extra_fields):
    return self._create_user(email, password, name, True, True, **extra_fields)
  
    