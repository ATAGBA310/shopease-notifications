class EcommercePlatform:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def create_order(self, customer_email, amount):
        order_data = {
            "customer_email": customer_email,
            "amount": amount
        }

        print(f"Commande créée pour {customer_email} - montant : {amount} €")
        self.event_manager.notify("order_created", order_data)

        if amount > 1000:
            self.event_manager.notify("high_value_order", order_data)

    def reject_payment(self, customer_email, support_email):
        payment_data = {
            "customer_email": customer_email,
            "support_email": support_email
        }

        print(f"Paiement refusé pour {customer_email}")
        self.event_manager.notify("payment_failed", payment_data)

    def ship_order(self, customer_phone, tracking_number):
        shipment_data = {
            "customer_phone": customer_phone,
            "tracking_number": tracking_number
        }

        print(f"Colis expédié - numéro de suivi : {tracking_number}")
        self.event_manager.notify("order_shipped", shipment_data)