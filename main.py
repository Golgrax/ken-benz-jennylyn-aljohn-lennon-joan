from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.metrics import dp
import sqlite3
import hashlib
import datetime

kv = '''
ScreenManager:
    LoginScreen:
    RegisterScreen:
    BrowseScreen:
    CartScreen:
    CheckoutScreen:
    HelpScreen:

<LoginScreen>:
    name: 'login'
    FloatLayout:
        Image:
            source: 'pup_monument.jpg'
            allow_stretch: True
            keep_ratio: False
            size: self.parent.size
            pos: self.parent.pos

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: dp(20)

            Image:
                source: 'pup_logo_circle.png'
                size_hint: None, None
                size: dp(100), dp(100)
                pos_hint: {'center_x': 0.5}

            Label:
                text: 'Welcome To PUP Study with Style'
                font_size: '20sp'
                color: 0,0,0,1
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_name: 'RocaOne'

            TextInput:
                id: username
                hint_text: 'Username'
                size_hint_y: None
                height: dp(40)
                multiline: False
                background_normal: ''
                background_color: 1,1,1,0.8
                font_name: 'RocaOne'
                foreground_color: 0,0,0,1

            TextInput:
                id: password
                hint_text: 'Password'
                password: True
                size_hint_y: None
                height: dp(40)
                multiline: False
                background_normal: ''
                background_color: 1,1,1,0.8
                font_name: 'RocaOne'
                foreground_color: 0,0,0,1

            BoxLayout:
                size_hint_y: None
                height: dp(40)
                spacing: dp(10)

                Button:
                    text: 'LOGIN'
                    on_release: app.login_user(username.text, password.text)
                    background_normal: ''
                    background_color: 0,1,1,1
                    font_name: 'RocaOne'
                    color: 0,0,0,1
                Button:
                    text: 'REGISTER'
                    on_release: app.root.current = 'register'
                    background_normal: ''
                    background_color: 0,1,1,1
                    font_name: 'RocaOne'
                    color: 0,0,0,1

        Button:
            text: '?'
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {'x': 0.9, 'y': 0.02}
            background_normal: ''
            background_color: 0,0,0,0.5
            color: 0,0,0,1
            on_press:
                app.previous_screen = 'login'
                app.root.current = 'help'

<RegisterScreen>:
    name: 'register'
    FloatLayout:
        Image:
            source: 'pup_monument.jpg'
            allow_stretch: True
            keep_ratio: False
            size: self.parent.size
            pos: self.parent.pos

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: dp(20)

            Image:
                source: 'pup_logo_circle.png'
                size_hint: None, None
                size: dp(100), dp(100)
                pos_hint: {'center_x': 0.5}

            Label:
                text: 'Register for PUP Study with Style'
                font_size: '20sp'
                color: 0,0,0,1
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                font_name: 'RocaOne'

            TextInput:
                id: username
                hint_text: 'Username'
                size_hint_y: None
                height: dp(40)
                multiline: False
                background_normal: ''
                background_color: 1,1,1,0.8
                font_name: 'RocaOne'
                foreground_color: 0,0,0,1

            TextInput:
                id: password
                hint_text: 'Password'
                password: True
                size_hint_y: None
                height: dp(40)
                multiline: False
                background_normal: ''
                background_color: 1,1,1,0.8
                font_name: 'RocaOne'
                foreground_color: 0,0,0,1

            Button:
                text: 'REGISTER'
                on_release: app.register_user(username.text, password.text)
                background_normal: ''
                background_color: 0,1,1,1
                font_name: 'RocaOne'
                color: 0,0,0,1

        Button:
            text: '?'
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {'x': 0.9, 'y': 0.02}
            background_normal: ''
            background_color: 0,0,0,0.5
            color: 0,0,0,1
            on_press:
                app.previous_screen = 'register'
                app.root.current = 'help'

<BrowseScreen>:
    name: 'browse'
    Image:
        source: 'pup_monument.jpg'
        allow_stretch: True
        keep_ratio: False
        size: root.size
        pos: root.pos
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: dp(10)
            spacing: dp(10)

            Image:
                source: 'pup_logo_small.png'
                size_hint_x: None
                width: dp(40)
            TextInput:
                id: search
                hint_text: 'Search'
                multiline: False
                background_normal: ''
                background_color: 1,1,1,0.8
                font_name: 'RocaOne'
                foreground_color: 0,0,0,1
            Button:
                text: 'Search'
                size_hint_x: None
                width: dp(60)
                on_press: app.root.get_screen('browse').search_products()
                font_name: 'RocaOne'
                color: 0,0,0,1
            Button:
                background_normal: 'cart.png'
                size_hint_x: None
                width: dp(40)
                on_press: app.root.current = 'cart'

        Label:
            text: 'Mula sayo para sa bayan'
            font_size: '24sp'
            color: 0,0,0,1
            size_hint_y: None
            height: self.texture_size[1]
            halign: 'center'
            valign: 'middle'
            font_name: 'RocaOne'

        GridLayout:
            cols: 2
            size_hint_y: None
            height: dp(100)
            spacing: dp(10)
            padding: dp(10)

            Button:
                background_normal: 'buttons/lanyards.png'
                on_press: app.root.get_screen('browse').filter_by_category('Lanyards')
            Button:
                background_normal: 'buttons/shirt.png'
                on_press: app.root.get_screen('browse').filter_by_category('Shirt')
            Button:
                background_normal: 'buttons/sticker.png'
                on_press: app.root.get_screen('browse').filter_by_category('Sticker')
            Button:
                background_normal: 'buttons/totebag.png'
                on_press: app.root.get_screen('browse').filter_by_category('Tote Bag')

        ScrollView:
            GridLayout:
                id: products_grid
                cols: 2
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

        Button:
            text: '?'
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {'x': 0.9, 'y': 0.02}
            background_normal: ''
            background_color: 0,0,0,0.5
            color: 0,0,0,1
            on_press:
                app.previous_screen = 'browse'
                app.root.current = 'help'

<CartScreen>:
    name: 'cart'
    Image:
        source: 'pup_monument.jpg'
        allow_stretch: True
        keep_ratio: False
        size: root.size
        pos: root.pos
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: dp(60)
            Button:
                text: '<'
                size_hint_x: None
                width: dp(40)
                on_press: app.root.current = 'browse'
                color: 0,0,0,1
            Image:
                source: 'pup_logo_small.png'
                size_hint_x: None
                width: dp(40)
            Label:
                text: 'Shopping cart'
                font_size: '20sp'
                font_name: 'RocaOne'
                color: 0,0,0,1

        ScrollView:
            GridLayout:
                id: cart_items
                cols: 1
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

        Button:
            text: 'Proceed to Checkout'
            size_hint_y: None
            height: dp(50)
            on_press: app.root.get_screen('cart').proceed_to_checkout()
            font_name: 'RocaOne'
            color: 0,0,0,1

        Button:
            text: '?'
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {'x': 0.9, 'y': 0.02}
            background_normal: ''
            background_color: 0,0,0,0.5
            color: 0,0,0,1
            on_press:
                app.previous_screen = 'cart'
                app.root.current = 'help'

<CheckoutScreen>:
    name: 'checkout'
    Image:
        source: 'pup_monument.jpg'
        allow_stretch: True
        keep_ratio: False
        size: root.size
        pos: root.pos
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: dp(60)
            Button:
                text: '<'
                size_hint_x: None
                width: dp(40)
                on_press: app.root.current = 'cart'
                color: 0,0,0,1
            Image:
                source: 'pup_logo_small.png'
                size_hint_x: None
                width: dp(40)
            Label:
                text: 'Checkout'
                font_size: '20sp'
                font_name: 'RocaOne'
                color: 0,0,0,1

        ScrollView:
            GridLayout:
                id: selected_items
                cols: 1
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(100)
            Label:
                id: subtotal
                text: 'Subtotal: ₱0.00'
                font_name: 'RocaOne'
                color: 0,0,0,1
            Label:
                text: 'Shipping: ₱36.00'
                font_name: 'RocaOne'
                color: 0,0,0,1
            Label:
                id: total
                text: 'Total: ₱36.00'
                font_name: 'RocaOne'
                color: 0,0,0,1

        Label:
            text: 'Payment Method: Cash on Delivery'
            font_name: 'RocaOne'
            color: 0,0,0,1

        Button:
            text: 'Confirm Order'
            size_hint_y: None
            height: dp(50)
            on_press: root.confirm_order()
            font_name: 'RocaOne'
            color: 0,0,0,1

<HelpScreen>:
    name: 'help'
    Image:
        source: 'pup_monument.jpg'
        allow_stretch: True
        keep_ratio: False
        size: root.size
        pos: root.pos
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Help Information\\n\\nThis is the help screen.\\nYou can add more details here.'
            font_size: '18sp'
            halign: 'center'
            font_name: 'RocaOne'
            color: 0,0,0,1
        Button:
            text: 'Back'
            size_hint_y: None
            height: dp(50)
            on_press: app.root.current = app.previous_screen
            font_name: 'RocaOne'
            color: 0,0,0,1
'''

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class BrowseScreen(Screen):
    def on_enter(self):
        self.load_products()

    def load_products(self):
        app = App.get_running_app()
        app.cursor.execute("SELECT id, name, price, image_path FROM products")
        products = app.cursor.fetchall()
        grid = self.ids.products_grid
        grid.clear_widgets()
        for product in products:
            product_id, name, price, image_path = product
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(180))
            image = Image(source=image_path)
            label = Label(text=f"{name}\n₱{price:.2f}", font_size='14sp', font_name='RocaOne', color=(0,0,0,1))
            add_button = Button(text='Add to Cart', size_hint_y=None, height=dp(30), font_name='RocaOne', color=(0,0,0,1))
            add_button.bind(on_press=lambda instance, pid=product_id: self.add_to_cart(pid))
            box.add_widget(image)
            box.add_widget(label)
            box.add_widget(add_button)
            grid.add_widget(box)

    def add_to_cart(self, product_id):
        app = App.get_running_app()
        if not hasattr(app, 'user_id'):
            print("Please log in first")
            app.root.current = 'login'
            return
        user_id = app.user_id
        app.cursor.execute("SELECT quantity FROM cart WHERE user_id = ? AND product_id = ?", (user_id, product_id))
        result = app.cursor.fetchone()
        if result:
            quantity = result[0] + 1
            app.cursor.execute("UPDATE cart SET quantity = ? WHERE user_id = ? AND product_id = ?", (quantity, user_id, product_id))
        else:
            app.cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, 1)", (user_id, product_id))
        app.db.commit()

    def filter_by_category(self, category):
        app = App.get_running_app()
        app.cursor.execute("SELECT id, name, price, image_path FROM products WHERE category = ?", (category,))
        products = app.cursor.fetchall()
        grid = self.ids.products_grid
        grid.clear_widgets()
        for product in products:
            product_id, name, price, image_path = product
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(180))
            image = Image(source=image_path)
            label = Label(text=f"{name}\n₱{price:.2f}", font_size='14sp', font_name='RocaOne', color=(0,0,0,1))
            add_button = Button(text='Add to Cart', size_hint_y=None, height=dp(30), font_name='RocaOne', color=(0,0,0,1))
            add_button.bind(on_press=lambda instance, pid=product_id: self.add_to_cart(pid))
            box.add_widget(image)
            box.add_widget(label)
            box.add_widget(add_button)
            grid.add_widget(box)

    def search_products(self):
        search_text = self.ids.search.text
        app = App.get_running_app()
        app.cursor.execute("SELECT id, name, price, image_path FROM products WHERE name LIKE ?", ('%'+search_text+'%',))
        products = app.cursor.fetchall()
        grid = self.ids.products_grid
        grid.clear_widgets()
        for product in products:
            product_id, name, price, image_path = product
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(180))
            image = Image(source=image_path)
            label = Label(text=f"{name}\n₱{price:.2f}", font_size='14sp', font_name='RocaOne', color=(0,0,0,1))
            add_button = Button(text='Add to Cart', size_hint_y=None, height=dp(30), font_name='RocaOne', color=(0,0,0,1))
            add_button.bind(on_press=lambda instance, pid=product_id: self.add_to_cart(pid))
            box.add_widget(image)
            box.add_widget(label)
            box.add_widget(add_button)
            grid.add_widget(box)

class CartScreen(Screen):
    def on_enter(self):
        self.selected_items = []
        self.load_cart()

    def load_cart(self):
        app = App.get_running_app()
        if not hasattr(app, 'user_id'):
            print("Please log in to view cart")
            app.root.current = 'login'
            return
        user_id = app.user_id
        app.cursor.execute("""
            SELECT p.name, p.price, p.image_path, c.quantity, p.id
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = ?
        """, (user_id,))
        cart_items = app.cursor.fetchall()
        grid = self.ids.cart_items
        grid.clear_widgets()
        self.checkbox_dict = {}
        for item in cart_items:
            name, price, image_path, quantity, product_id = item
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80))
            checkbox = CheckBox(size_hint=(None, None), size=(dp(30), dp(30)))
            checkbox.bind(active=lambda cb, value, pid=product_id: self.on_checkbox_active(cb, value, pid))
            self.checkbox_dict[checkbox] = product_id
            image = Image(source=image_path, size_hint=(None, None), size=(dp(60), dp(60)))
            label = Label(text=f"{name} x{quantity}\n₱{price*quantity:.2f}", text_size=(self.width, None), valign='middle', halign='left', font_name='RocaOne', color=(0,0,0,1))
            box.add_widget(checkbox)
            box.add_widget(image)
            box.add_widget(label)
            grid.add_widget(box)

    def on_checkbox_active(self, checkbox, value, product_id):
        if value:
            if product_id not in self.selected_items:
                self.selected_items.append(product_id)
        else:
            if product_id in self.selected_items:
                self.selected_items.remove(product_id)

    def proceed_to_checkout(self):
        if not self.selected_items:
            from kivy.uix.popup import Popup
            from kivy.uix.label import Label
            popup = Popup(title='Error', content=Label(text='Please select at least one item to checkout.', color=(0,0,0,1)), size_hint=(0.6, 0.4))
            popup.open()
            return
        app = App.get_running_app()
        checkout_screen = app.root.get_screen('checkout')
        checkout_screen.selected_items = self.selected_items
        app.root.current = 'checkout'

class CheckoutScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        if not hasattr(app, 'user_id'):
            print("Please log in first")
            app.root.current = 'login'
            return
        user_id = app.user_id
        selected_items = getattr(self, 'selected_items', [])
        if not selected_items:
            print("No items selected")
            return
        app.cursor.execute(f"""
            SELECT p.name, p.price, c.quantity, p.image_path
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = ? AND c.product_id IN ({','.join('?'*len(selected_items))})
        """, (user_id, *selected_items))
        cart_items = app.cursor.fetchall()
        grid = self.ids.selected_items
        grid.clear_widgets()
        subtotal = 0
        for item in cart_items:
            name, price, quantity, image_path = item
            subtotal += price * quantity
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80))
            image = Image(source=image_path, size_hint=(None, None), size=(dp(60), dp(60)))
            label = Label(text=f"{name} x{quantity}\n₱{price*quantity:.2f}", text_size=(self.width, None), valign='middle', halign='left', font_name='RocaOne', color=(0,0,0,1))
            box.add_widget(image)
            box.add_widget(label)
            grid.add_widget(box)
        self.ids.subtotal.text = f"Subtotal: ₱{subtotal:.2f}"
        shipping = 36.00
        total = subtotal + shipping
        self.ids.total.text = f"Total: ₱{total:.2f}"

    def confirm_order(self):
        app = App.get_running_app()
        app.confirm_order()
        from kivy.uix.popup import Popup
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Your order has been placed successfully.', color=(0,0,0,1)))
        btn = Button(text='OK', size_hint_y=None, height=dp(50), color=(0,0,0,1))
        layout.add_widget(btn)
        popup = Popup(title='Order Confirmed', content=layout, size_hint=(0.6, 0.4))
        btn.bind(on_press=popup.dismiss)


class HelpScreen(Screen):
    pass

class StudyWithStyleApp(App):
    def build(self):
        self.db = sqlite3.connect('study_with_style.db')
        self.cursor = self.db.cursor()
        self.create_tables()
        self.insert_sample_products()
        return Builder.load_string(kv)

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            image_path TEXT
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cart (
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            PRIMARY KEY (user_id, product_id)
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            total_amount REAL,
            order_date TEXT,
            status TEXT
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS order_items (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price REAL,
            PRIMARY KEY (order_id, product_id)
        )''')
        self.db.commit()

    def insert_sample_products(self):
        self.cursor.execute("SELECT COUNT(*) FROM products")
        count = self.cursor.fetchone()[0]
        if count == 0:
            products = [
                ('PUP Reversible Lanyard', 'Lanyards', 140.0, 'images/lanyard.png'),
                ('PUP Tote Bag', 'Tote Bag', 450.0, 'images/totebag.png'),
                ('PUP Minimalist Shirt', 'Shirt', 350.0, 'images/shirt.png'),
                ('PUP Minimalist Baybayin Lanyard', 'Lanyards', 140.0, 'images/lanyard2.png'),
                ('PUP Jeepney Signage', 'Sticker', 50.0, 'images/jeepney.png'),
                ('PUP Iskolar Tote Bag', 'Tote Bag', 450.0, 'images/totebag2.png'),
            ]
            for product in products:
                self.cursor.execute("INSERT INTO products (name, category, price, image_path) VALUES (?, ?, ?, ?)", product)
            self.db.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        if not username or not password:
            print("Please enter username and password")
            return
        password_hash = self.hash_password(password)
        try:
            self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            self.db.commit()
            print("Registration successful")
            self.root.current = 'login'
        except sqlite3.IntegrityError:
            print("Username already exists")

    def login_user(self, username, password):
        password_hash = self.hash_password(password)
        self.cursor.execute("SELECT id FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        user = self.cursor.fetchone()
        if user:
            self.user_id = user[0]
            self.root.current = 'browse'
        else:
            print("Invalid username or password")

    def confirm_order(self):
        checkout_screen = self.root.get_screen('checkout')
        selected_items = getattr(checkout_screen, 'selected_items', [])
        if not selected_items:
            print("No items selected")
            return
        user_id = self.user_id
        self.cursor.execute(f"""
            SELECT SUM(p.price * c.quantity)
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = ? AND c.product_id IN ({','.join('?'*len(selected_items))})
        """, (user_id, *selected_items))
        subtotal = self.cursor.fetchone()[0] or 0
        shipping = 36.00
        total = subtotal + shipping
        order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO orders (user_id, total_amount, order_date, status) VALUES (?, ?, ?, 'Pending')", (user_id, total, order_date))
        order_id = self.cursor.lastrowid
        self.cursor.execute(f"""
            SELECT c.product_id, c.quantity, p.price
            FROM cart c
            JOIN products p ON c.product_id = p.id
            WHERE c.user_id = ? AND c.product_id IN ({','.join('?'*len(selected_items))})
        """, (user_id, *selected_items))
        selected_cart_items = self.cursor.fetchall()
        for item in selected_cart_items:
            product_id, quantity, price = item
            self.cursor.execute("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)", (order_id, product_id, quantity, price))
        for product_id in selected_items:
            self.cursor.execute("DELETE FROM cart WHERE user_id = ? AND product_id = ?", (user_id, product_id))
        self.db.commit()
        print("Order confirmed. Order ID:", order_id)

    def on_stop(self):
        self.db.close()

if __name__ == '__main__':
    StudyWithStyleApp().run()
