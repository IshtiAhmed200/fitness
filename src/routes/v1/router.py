from fastapi import APIRouter
from src.controllers.api.v1 import bike_controller
from src.controllers.api.v1 import car_controller
from src.controllers.api.v1 import election_controller
from src.controllers.api.v1 import home_controller
from src.controllers.api.v1 import laptop_controller
from src.controllers.api.v1 import mobile_controller
from src.controllers.api.v1 import student
from src.controllers.api.v1 import teacher
from src.controllers.api.v1 import user_controller


router = APIRouter()


router.include_router(bike_controller.router, prefix="/bike")
router.include_router(car_controller.router, prefix="/car")
router.include_router(election_controller.router, prefix="/election")
router.include_router(home_controller.router, prefix="/home")
router.include_router(laptop_controller.router, prefix="/laptop")
router.include_router(mobile_controller.router, prefix="/mobile")
router.include_router(student.router, prefix="/student")
router.include_router(teacher.router, prefix="/teacher")
router.include_router(user_controller.router, prefix="/users")




