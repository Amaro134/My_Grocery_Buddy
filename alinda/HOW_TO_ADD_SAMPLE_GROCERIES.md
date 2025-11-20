# How to Add Sample Groceries

After creating a user account, you can add sample grocery items to see how the application works.

## Steps:

1. **Run the migration** (if you haven't already):
   ```bash
   python manage.py migrate
   ```

2. **Create a user account** (if you haven't already):
   - Go to the signup page and create an account
   - Or use the Django admin to create a user

3. **Add sample groceries** using the management command:
   ```bash
   python manage.py add_sample_groceries YOUR_USERNAME
   ```
   
   Replace `YOUR_USERNAME` with the username you created.

   Example:
   ```bash
   python manage.py add_sample_groceries john
   ```

4. **Login and view your groceries**:
   - Login with your username
   - You should now see 15 sample grocery items with prices!

## Sample Items Included:

- Milk (Dairy) - $4.99
- Bread (Bakery) - $3.49
- Eggs (Dairy) - $5.99
- Bananas (Produce) - $2.99
- Chicken Breast (Meat) - $8.99
- Rice (Pantry) - $4.49
- Orange Juice (Beverages) - $3.99
- Potatoes (Produce) - $3.49
- Cheese (Dairy) - $5.99
- Tomatoes (Produce) - $2.49
- Pasta (Pantry) - $2.99
- Ice Cream (Frozen) - $6.99
- Chips (Snacks) - $3.99
- Yogurt (Dairy) - $5.49
- Apples (Produce) - $4.99

## Note:

The command will only add items that don't already exist for that user, so you can run it multiple times safely.

