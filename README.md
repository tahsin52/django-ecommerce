# Django-ecommerce
## In project scope;
1- With AbstractBaseUser, You can do user login, user registration 
2- You can add, delete or update products and you can add variations and set color and size from the admin panel.
3- You can create and edit a profile, you can see your orders
4- Paypal ready to use as payment system
5- You can list or add products according to their categories.
6- User registration includes e-mail verification

# Most of these processes are done through the admin panel!!
# Backend and frontend are used in the project.
# For Project security, admin honey_port is used for admin panel.
# If you want, you can add products without admin.

### Setup Project</br>
1- python manage.py makemigrations</br>
2- python manage.py migrate</br>
3- python manage.py createsuperuser </br>
4- Go to admin

### 1. Admin Access
* Admin Section: [http://127.0.0.1:8000/securelogin](http://127.0.0.1:8000/securelogin)

### 2. Accounts
* Registration: [http://127.0.0.1:8000/account/register/](http://127.0.0.1:8000/account/register/)
* Login: [http://127.0.0.1:8000/account/login/](http://127.0.0.1:8000/account/login/)
* Logout [http://127.0.0.1:8000/account/logout/](http://127.0.0.1:8000/account/logout/)
* Forgot Password [http://127.0.0.1:8000/account/forgotpassword/](http://127.0.0.1:8000/account/forgotpassword/)
* Reset Password [http://127.0.0.1:8000/account/resetpassword/](http://127.0.0.1:8000/account/resetpassword/)
* Change Password [http://127.0.0.1:8000/account/changePassword/](http://127.0.0.1:8000/account/changePassword/)
* Edit Profile [http://127.0.0.1:8000/account/edit_profile/](http://127.0.0.1:8000/account/edit_profile/)
* Your Orders [http://127.0.0.1:8000/account/my_orders/](http://127.0.0.1:8000/account/my_orders/)

### 3. Store
* GET [http://127.0.0.1:8000/store/](http://127.0.0.1:8000/store/)
* GET [http://127.0.0.1:8000/store/category/category_slug/](http://127.0.0.1:8000/store/category/<slug:category_slug>/)

### 4.Search
* GET and POST [http://127.0.0.1:8000/store/search/](http://127.0.0.1:8000/store/search/)

### 5.Review
* GET and POST [http://127.0.0.1:8000/store/submit_review/product_id/](http://127.0.0.1:8000/store/submit_review/<int:product_id>/)

### 6.Order and Payment
* POST [http://127.0.0.1:8000/order/place_order/](http://127.0.0.1:8000/order/place_order/)
* POST [http://127.0.0.1:8000/order/order_complete/](http://127.0.0.1:8000/order/order_complete/)

