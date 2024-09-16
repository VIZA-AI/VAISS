# - Import VAIPH Modules
from VAIPH.StripeHandler import *
# - Import VAIA Modules
from VAIA.ClientHandler import *
# - Import Required Header Files
from ReturnCodes import *

# - Import Required Libraries
from celery import Celery
import time

# - Setup Log File Full Path
CELERY_LOG_FILE = os.path.join(os.path.dirname(__file__), 'celery.log')

# - Celery Broker URL
CELERY_BROKER_URL = 'redis://localhost:6379/1'

# - Celery Backend URL
CELERY_BACKEND_URL = 'redis://localhost:6379/1'

# - Database Terminal Output
CELERY_HANDLER = f'\033[38;2;190;255;144m[VAISS]\033[0m'

# - Setup Celery Application
celery_app = Celery(
    'tasks',
    broker = CELERY_BROKER_URL,
    backend = CELERY_BACKEND_URL
)

# - Show Init Log
print(CELERY_HANDLER, "Celery Broker URL : {}{}{}".format(GREEN, celery_app.conf.broker_url, RESET))
print(CELERY_HANDLER, "Celery Backend URL : {}{}{}".format(GREEN, celery_app.conf.result_backend, RESET))

# - Celery Task to Create Subscription
@celery_app.task
def createSubscription(
    user_id,
    account_id,
    customer_id,
    price_id,
    client_id,
    iterations
):
    # - Create Stripe Handler Object
    stripe_handler = StripeHandler()
    # - Create Subscription
    status, status_message = stripe_handler.createSubscription(
        user_id,
        account_id,
        customer_id,
        price_id,
        client_id,
        iterations
    )
    # - Check Subscription Creation Status
    if status != RET.PAYMENT.STRIPE.SUBSCRIPTION.CREATE.SUCCESS:
        # print(CELERY_HANDLER, FAILED, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
        print("[ERROR] Creating Payment for Client {} : {}".format(client_id, status_message))

@celery_app.task
def print_message():
    # - Create Client Handler Object
    # client = ClientHandler(None, client_id)
    # # - Get Client Info
    # status, status_message = client.getClient()
    # # - Check Client Info Status
    # if status != RET.CLIENT.LOAD.SUCCESS:
    #     print(FLASK, FAILED, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     return jsonify({
    #         'status': "ERROR",
    #         'status_code': status,
    #         'message': status_message
    #     })
    # # - Check Checkout Session
    # status, status_message = stripe_handler.checkCheckoutSession(
    #     _session_id,
    #     stripe_handler.account_id,
    #     stripe_handler.price_id
    # )
    # # - Check Checkout Session Status
    # if status != RET.PAYMENT.STRIPE.CHECKOUT.CHECK.SUCCESS:
    #     print(FLASK, FAILED, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     return jsonify({
    #         'status': "ERROR",
    #         'status_code': status,
    #         'message': status_message
    #     })
    # # - Get Payment Plan
    # status, status_message = stripe_handler.loadPaymentPlan(stripe_handler.product_id)
    # # - Check Payment Plan Status
    # if status != RET.PAYMENT.STRIPE.PLAN.LOAD.SUCCESS:
    #     # - Check if Plan Already Activated
    #     if status == RET.PAYMENT.STRIPE.PLAN.ACTIVATE.FAILED.ALREADY_ACTIVATED:
    #         print(FLASK, WARNING, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #         print(CYAN, "Warning Here", RESET)
    #         return jsonify({
    #             'status': "ERROR",
    #             'status_code': status,
    #             'message': status_message
    #         })
    #     # - Other Errors
    #     print(FLASK, FAILED, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     return jsonify({
    #         'status': "ERROR",
    #         'status_code': status,
    #         'message': status_message
    #     })
    # # - Create Subscription
    # status, status_message = stripe_handler.createSubscription(
    #     client.user_id,
    #     stripe_handler.account_id,
    #     stripe_handler.customer_id,
    #     stripe_handler.price_id,
    #     client.client_id,
    #     stripe_handler.payment_plan_iterations
    # )
    # # - Check Subscription Creation Status
    # if status != RET.PAYMENT.STRIPE.SUBSCRIPTION.CREATE.SUCCESS:
    #     print(FLASK, FAILED, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     return jsonify({
    #         'status': "ERROR",
    #         'status_code': status,
    #         'message': status_message
    #     })
    # # - Set Invoice Info
    # invoice = status_message
    # # - Update Plan Activation Status
    # status, status_message = stripe_handler.activatePaymentPlan(stripe_handler.product_id)
    # # - Check Plan Activation Status
    # if status != RET.PAYMENT.STRIPE.PLAN.ACTIVATE.SUCCESS:
    #     print(FLASK, FAILED, "Creating Payment for Client {}{}{} : Subscription Activated, but {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     return jsonify({
    #         'status': "ERROR",
    #         'status_code': status,
    #         'message': status_message
    #     })
    # # - Create Account Handler Object
    # account = AccountHandler(client.user_id)
    # # - Get Account Info
    # status, status_message = account.getInfo(client.email)
    # # - Check Account Info Status
    # lawfirm = "Unknown"
    # if status != RET.USER.INFO.LOAD.SUCCESS:
    #     print(FLASK, WARNING, "Creating Payment for Client {}{}{} : {}{}{}".format(D_CYAN, client_id, RESET, ERR, status_message, RESET))
    #     print(CYAN, "Warning 2 Here", RESET)
    # else:
    #     lawfirm = account.lawfirm
    # Log a message
    # logging.error("this is error test logging")
    print(GREEN, "Celery Task Executed", RESET)