import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod


class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element

    @abstractmethod
    def drawWidget(self):
        pass


class FoodOrderingApp(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.order_items = []
        self.total_price = 0.0
        self.animation_direction = 1
        self.animation_position = 0
        
        self.menu_items = [
            {"name": "Rabbit Special", "price": 12.99, "image": "images/rabbit.png"},
            {"name": "Veggie Delight", "price": 8.99, "image": "images/rabbit.png"},
            {"name": "Garden Salad", "price": 7.99, "image": "images/rabbit.png"},
            {"name": "Fresh Smoothie", "price": 6.99, "image": "images/rabbit.png"},
        ]
        
        self.setup_sounds()
    
    def setup_sounds(self):
        self.sound = js.Audio.new("sounds/rabbit1.wav")
    
    def play_click_sound(self):
        self.sound.play()
    
    def play_confirm_sound(self):
        self.sound.play()
    
    def create_header(self):
        header = document.createElement("div")
        header.className = "header"
        
        logo = document.createElement("img")
        logo.className = "logo"
        logo.src = "images/rabbit.png"
        logo.alt = "Logo"
        header.appendChild(logo)
        
        title = document.createElement("h1")
        title.className = "title"
        title.innerText = "Delicious Food Restaurant"
        header.appendChild(title)
        
        self.promo_banner = document.createElement("img")
        self.promo_banner.className = "promo"
        self.promo_banner.src = "images/rabbit.png"
        self.promo_banner.alt = "Special Offer"
        header.appendChild(self.promo_banner)
        
        self.setup_promo_animation()
        return header
    
    def setup_promo_animation(self):
        self.promo_animation_proxy = create_proxy(self.animate_promo)
        js.setInterval(self.promo_animation_proxy, 50)
    
    def animate_promo(self):
        self.animation_position += self.animation_direction
        if self.animation_position > 10:
            self.animation_direction = -1
        elif self.animation_position < -10:
            self.animation_direction = 1
        self.promo_banner.style.transform = f"translateY({self.animation_position}px)"
    
    def create_menu_section(self):
        menu_section = document.createElement("div")
        menu_section.className = "menu-section"
        
        title = document.createElement("h2")
        title.className = "section-title"
        title.innerText = "Menu"
        menu_section.appendChild(title)
        
        menu_grid = document.createElement("div")
        menu_grid.className = "menu-grid"
        
        for idx, item in enumerate(self.menu_items):
            menu_item = self.create_menu_item(item, idx)
            menu_grid.appendChild(menu_item)
        
        menu_section.appendChild(menu_grid)
        return menu_section
    
    def create_menu_item(self, item, idx):
        item_widget = document.createElement("div")
        item_widget.className = "menu-item"
        
        img = document.createElement("img")
        img.src = item['image']
        img.alt = item['name']
        item_widget.appendChild(img)
        
        name = document.createElement("h3")
        name.innerText = item['name']
        item_widget.appendChild(name)
        
        price = document.createElement("div")
        price.className = "price"
        price.innerText = f"${item['price']:.2f}"
        item_widget.appendChild(price)
        
        quantity = document.createElement("input")
        quantity.type = "number"
        quantity.min = "0"
        quantity.max = "10"
        quantity.value = "1"
        quantity.id = f"qty-{idx}"
        item_widget.appendChild(quantity)
        
        add_btn = document.createElement("button")
        add_btn.innerText = "Add to Order"
        add_btn.onclick = create_proxy(lambda e, i=item, q=quantity: self.add_to_order(i, q))
        item_widget.appendChild(add_btn)
        
        return item_widget
    
    def create_order_section(self):
        order_section = document.createElement("div")
        order_section.className = "order-section"
        
        title = document.createElement("h2")
        title.className = "section-title"
        title.innerText = "Your Order"
        order_section.appendChild(title)
        
        self.order_list = document.createElement("div")
        self.order_list.className = "order-list"
        self.order_list.id = "order-list"
        order_section.appendChild(self.order_list)
        
        self.total_label = document.createElement("div")
        self.total_label.className = "total"
        self.total_label.innerText = "Total: $0.00"
        order_section.appendChild(self.total_label)
        
        clear_btn = document.createElement("button")
        clear_btn.className = "action-button clear-btn"
        clear_btn.innerText = "Clear Order"
        clear_btn.onclick = create_proxy(self.clear_order)
        order_section.appendChild(clear_btn)
        
        return order_section
    
    def create_footer(self):
        footer = document.createElement("div")
        
        order_btn = document.createElement("button")
        order_btn.className = "action-button order-btn"
        order_btn.innerText = "Place Order"
        order_btn.onclick = create_proxy(self.place_order)
        footer.appendChild(order_btn)
        
        return footer
    
    def add_to_order(self, item, quantity_input):
        quantity = int(quantity_input.value)
        
        if quantity > 0:
            self.play_click_sound()
            
            order_item_div = document.createElement("div")
            order_item_div.className = "order-item"
            order_item_div.innerText = f"{item['name']} x{quantity} - ${item['price'] * quantity:.2f}"
            self.order_list.appendChild(order_item_div)
            
            self.order_items.append({
                'name': item['name'],
                'quantity': quantity,
                'price': item['price']
            })
            
            self.total_price += item['price'] * quantity
            self.update_total()
            quantity_input.value = "1"
    
    def update_total(self):
        self.total_label.innerText = f"Total: ${self.total_price:.2f}"
    
    def clear_order(self, event=None):
        self.play_click_sound()
        self.order_list.innerHTML = ""
        self.order_items = []
        self.total_price = 0.0
        self.update_total()
    
    def place_order(self, event=None):
        if not self.order_items:
            js.alert("Please add items to your order first!")
            return
        
        self.play_confirm_sound()
        
        order_summary = "Your Order:\n\n"
        for item in self.order_items:
            order_summary += f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}\n"
        order_summary += f"\nTotal: ${self.total_price:.2f}\n\n"
        order_summary += "Order placed successfully!\n"
        order_summary += "Estimated delivery: 30-45 minutes"
        
        js.alert(order_summary)
        self.clear_order()
    
    def drawWidget(self):
        header = self.create_header()
        self.element.appendChild(header)
        
        content = document.createElement("div")
        content.className = "content"
        
        menu = self.create_menu_section()
        content.appendChild(menu)
        
        order = self.create_order_section()
        content.appendChild(order)
        
        self.element.appendChild(content)
        
        footer = self.create_footer()
        self.element.appendChild(footer)


if __name__ == "__main__":
    app = FoodOrderingApp("container")
    app.drawWidget()
