import sys
sys.path.append("app")

from app.controllers.main_controller import MainController
from app.models.database import create_tables
from app.views.main_view import MainView

def main():
    create_tables()
    controller = MainController()
    controller.run()

if __name__ == "__main__":
    main()
