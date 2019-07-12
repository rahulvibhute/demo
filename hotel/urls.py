from rest_framework.routers import SimpleRouter
from hotel.views import *
router = SimpleRouter()
router.register("Hotel",HotelOp)
router.register("Address",AddressOp)
router.register("Menu",MenuOp)
router.register("Waiter",WaiterOp)


urlpatterns=router.urls