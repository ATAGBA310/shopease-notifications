from src.channels.email_channel import EmailChannel
from src.channels.sms_channel import SmsChannel
from src.channels.internal_channel import InternalChannel

from src.core.event_manager import EventManager
from src.core.notification_listener import NotificationListener

from src.app.ecommerce_platform import EcommercePlatform


def build_order_message(data):
    return f"Votre commande a bien été enregistrée. Montant : {data['amount']} €"


def build_payment_failed_message(data):
    return f"Paiement refusé pour le client {data['customer_email']}"


def build_shipping_message(data):
    return f"Votre colis a été expédié. Numéro de suivi : {data['tracking_number']}"


def build_logistic_message(data):
    return f"Commande à montant élevé détectée : {data['amount']} €"


event_manager = EventManager()

email_channel = EmailChannel()
sms_channel = SmsChannel()
internal_channel = InternalChannel()

order_email_listener = NotificationListener(
    email_channel,
    "client@shopease.com",
    build_order_message
)

payment_support_listener = NotificationListener(
    email_channel,
    "support@shopease.com",
    build_payment_failed_message
)

shipment_sms_listener = NotificationListener(
    sms_channel,
    "+33612345678",
    build_shipping_message
)

high_value_internal_listener = NotificationListener(
    internal_channel,
    "equipe_logistique",
    build_logistic_message
)

event_manager.subscribe("order_created", order_email_listener)
event_manager.subscribe("payment_failed", payment_support_listener)
event_manager.subscribe("order_shipped", shipment_sms_listener)
event_manager.subscribe("high_value_order", high_value_internal_listener)

platform = EcommercePlatform(event_manager)

print("=== Nouvelle commande standard ===")
platform.create_order("client@shopease.com", 120)

print("\n=== Paiement refusé ===")
platform.reject_payment("client@shopease.com", "support@shopease.com")

print("\n=== Colis expédié ===")
platform.ship_order("+33612345678", "TRK-2026-001")

print("\n=== Commande à montant élevé ===")
platform.create_order("vip@shopease.com", 2500)