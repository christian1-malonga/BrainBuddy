import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.navigation import navigation_bp
from src.routes.transportation import transportation_bp
from src.routes.courses import courses_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(navigation_bp, url_prefix='/api/navigation')
app.register_blueprint(transportation_bp, url_prefix='/api/transportation')
app.register_blueprint(courses_bp, url_prefix='/api/elearning')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Import all models to ensure they are created
from src.models.building import Building
from src.models.transportation import BusRoute
from src.models.course import Course, Lesson, Assignment

with app.app_context():
    db.create_all()
    
    # Seed some initial data if tables are empty
    if Building.query.count() == 0:
        # Add sample buildings
        buildings = [
            Building(name='Veterinary Faculty', type='faculty', latitude=35.2281, longitude=33.3152, 
                    description='Faculty of Veterinary Medicine - Main building with laboratories and lecture halls'),
            Building(name='Main Library', type='facility', latitude=35.2285, longitude=33.3148,
                    description='Central library with study areas, computer labs, and research facilities'),
            Building(name='Engineering Faculty', type='faculty', latitude=35.2278, longitude=33.3155,
                    description='Faculty of Engineering - Computer labs, workshops, and lecture theaters'),
            Building(name='Medical Faculty', type='faculty', latitude=35.2283, longitude=33.3150,
                    description='Faculty of Medicine - Hospital, laboratories, and medical training facilities'),
            Building(name='Student Center', type='facility', latitude=35.2280, longitude=33.3153,
                    description='Student services, cafeteria, and recreational facilities'),
        ]
        for building in buildings:
            db.session.add(building)
    
    if BusRoute.query.count() == 0:
        import json
        # Add sample bus routes
        routes = [
            BusRoute(destination='KIZIBAS', route_type='capital', is_vacation_schedule=False,
                    departure_times=json.dumps(['07:15', '08:15', '09:15', '10:15', '11:15', '12:15', '13:15', '14:15', '15:15', '16:15', '17:15', '18:15', '19:15', '20:15', '21:15', '22:15']),
                    stops=json.dumps(['University Gate', 'Kızılbaş Junction', 'Kızılbaş Center', 'Kızılbaş Market', 'Final Stop']),
                    price='5 TL'),
            BusRoute(destination='GIRNE', route_type='outside', is_vacation_schedule=False,
                    departure_times=json.dumps(['07:00', '10:00', '13:00', '15:00', '18:00']),
                    stops=json.dumps(['University Gate', 'Girne Highway', 'Girne Junction', 'Girne Center', 'Girne Harbor']),
                    price='15 TL'),
        ]
        for route in routes:
            db.session.add(route)
    
    if Course.query.count() == 0:
        # Add sample courses
        courses = [
            Course(title='Advanced Mathematics', instructor='Dr. Smith', 
                  description='Advanced calculus and mathematical analysis covering derivatives, integrals, and differential equations.',
                  category='Mathematics', difficulty='Advanced', estimated_hours=40, total_lessons=12),
            Course(title='Quantum Physics', instructor='Prof. Johnson',
                  description='Introduction to quantum mechanics and modern physics principles.',
                  category='Physics', difficulty='Advanced', estimated_hours=50, total_lessons=15),
            Course(title='Computer Science Fundamentals', instructor='Dr. Williams',
                  description='Basic programming concepts, algorithms, and data structures.',
                  category='Computer Science', difficulty='Intermediate', estimated_hours=60, total_lessons=20),
        ]
        for course in courses:
            db.session.add(course)
        
        db.session.commit()
        
        # Add sample lessons and assignments
        math_course = Course.query.filter_by(title='Advanced Mathematics').first()
        if math_course:
            lessons = [
                Lesson(course_id=math_course.id, title='Introduction to Calculus', duration='45 min', order_index=1),
                Lesson(course_id=math_course.id, title='Derivatives and Applications', duration='60 min', order_index=2),
                Lesson(course_id=math_course.id, title='Integration Techniques', duration='55 min', order_index=3),
            ]
            assignments = [
                Assignment(course_id=math_course.id, title='Calculus Problem Set 1', due_date='2024-01-10', status='completed', grade='A'),
                Assignment(course_id=math_course.id, title='Integration Exercises', due_date='2024-01-15', status='pending'),
            ]
            for lesson in lessons:
                db.session.add(lesson)
            for assignment in assignments:
                db.session.add(assignment)
    
    db.session.commit()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

